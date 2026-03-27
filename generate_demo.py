from __future__ import annotations

import json
import math
import pathlib
import shutil
import subprocess
import tempfile
import wave
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parent
CASE_PATH = ROOT / "cases" / "demo.md"
DIST_DIR = ROOT / "dist" / "demo"
GAP_SECONDS = 0.25
TARGET_SECONDS = 15.0
VOICE_NAME = "Tingting"
VOICE_RATES = [220, 240, 265, 280, 300]


def parse_case_markdown(path: pathlib.Path) -> dict[str, Any]:
    """Parse the fixed markdown input into a small structured dictionary."""
    raw_sections: dict[str, list[str]] = {}
    current_heading: str | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            current_heading = line[2:].strip()
            raw_sections[current_heading] = []
            continue
        if line.startswith("## "):
            current_heading = line[3:].strip()
            raw_sections[current_heading] = []
            continue
        if current_heading is not None:
            raw_sections[current_heading].append(line)

    def section_text(name: str) -> str:
        lines = [line.strip() for line in raw_sections.get(name, []) if line.strip()]
        return "\n".join(lines)

    video_params: dict[str, str] = {}
    for line in raw_sections.get("视频参数", []):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        key, value = stripped[2:].split("：", 1)
        video_params[key.strip()] = value.strip()

    return {
        "title": section_text("标题"),
        "video_params": video_params,
        "target_user": section_text("目标用户"),
        "original_problem": section_text("原始问题"),
        "key_action": section_text("关键动作"),
        "before_after": [
            line.strip()
            for line in section_text("前后变化").splitlines()
            if line.strip()
        ],
        "result": section_text("结果"),
        "cta": section_text("CTA"),
    }


def simplify_problem(problem: str) -> str:
    """Compress the raw problem statement into natural narration."""
    if "说不清" in problem:
        return "想法很多，但目标和需求说不清"
    return problem.replace("导致项目推进很慢", "").strip("，。 ")


def spoken_result(result: str) -> str:
    """Make the result sentence sound a little more natural for TTS."""
    return result.replace("15分钟", "十五分钟")


def build_demo_plan(case: dict[str, Any]) -> dict[str, Any]:
    """Build a fixed three-slide PPT-style narration plan."""
    title = case["title"]
    target_user = case["target_user"]
    problem = simplify_problem(case["original_problem"])
    action = case["key_action"].rstrip("。")
    result = spoken_result(case["result"]).rstrip("。")
    before_after = case["before_after"]

    prefix = "很多 AI 项目" if "AI" in f"{title}{target_user}" else "很多这类项目"
    sentence_one = f"{prefix}卡住，不是没想法，而是{problem}。"
    sentence_two = f"{action}。"
    sentence_three = f"结果是{result}。"

    slides = [
        {
            "title": title,
            "body": f"目标用户：{target_user}\n当前问题：{problem}",
            "accent": "#2563EB",
            "background": "#F5F7FB",
            "badge": "demo案例",
            "footer": "AI配音 / demo案例",
        },
        {
            "title": "关键动作",
            "body": action,
            "accent": "#0F766E",
            "background": "#F4FBF9",
            "badge": "PPT讲解",
            "footer": "AI配音 / demo案例",
        },
        {
            "title": "结果变化",
            "body": "\n".join(
                [
                    before_after[0] if before_after else "",
                    before_after[1] if len(before_after) > 1 else "",
                    case["result"],
                ]
            ).strip(),
            "accent": "#7C3AED",
            "background": "#F8F5FF",
            "badge": "结果页",
            "footer": "AI配音 / demo案例",
        },
    ]

    captions = [{"text": text} for text in [sentence_one, sentence_two, sentence_three]]
    script = "\n".join(
        [
            f"第1页：{sentence_one}",
            f"第2页：{sentence_two}",
            f"第3页：{sentence_three}",
        ]
    )

    return {
        "slides": slides,
        "captions": captions,
        "script": script,
        "narration": [sentence_one, sentence_two, sentence_three],
    }


def ensure_tools_exist() -> None:
    """Fail early with a clear message if a required macOS tool is missing."""
    for tool_name in ["say", "afconvert", "swift"]:
        if shutil.which(tool_name) is None:
            raise RuntimeError(f"缺少系统命令：{tool_name}")


def run_command(args: list[str]) -> None:
    """Run a command and surface stderr directly if it fails."""
    subprocess.run(args, check=True)


def resolve_ffmpeg() -> str:
    """Resolve an ffmpeg binary from PATH or the local npm dependency."""
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg

    bundled_ffmpeg = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled_ffmpeg.exists():
        return str(bundled_ffmpeg)

    raise RuntimeError("缺少 ffmpeg，可通过 npm install 安装本项目依赖后再运行。")


def wav_duration_seconds(path: pathlib.Path) -> float:
    """Read the duration from a PCM wave file."""
    with wave.open(str(path), "rb") as handle:
        return handle.getnframes() / float(handle.getframerate())


def synthesize_segments(
    narration: list[str],
    rate: int,
    workdir: pathlib.Path,
) -> list[pathlib.Path]:
    """Generate one AIFF and one WAV per sentence for timing control."""
    wav_paths: list[pathlib.Path] = []

    for index, text in enumerate(narration, start=1):
        aiff_path = workdir / f"segment_{index}.aiff"
        wav_path = workdir / f"segment_{index}.wav"
        run_command(["say", "-v", VOICE_NAME, "-r", str(rate), text, "-o", str(aiff_path)])
        run_command(
            [
                "afconvert",
                "-f",
                "WAVE",
                "-d",
                "LEI16@22050",
                str(aiff_path),
                str(wav_path),
            ]
        )
        wav_paths.append(wav_path)

    return wav_paths


def pick_best_voice_rate(narration: list[str], workdir: pathlib.Path) -> tuple[int, list[pathlib.Path], list[float]]:
    """Pick the speaking rate whose total duration lands closest to 15 seconds."""
    best_rate = VOICE_RATES[0]
    best_paths: list[pathlib.Path] = []
    best_durations: list[float] = []
    best_distance = math.inf

    for rate in VOICE_RATES:
        rate_dir = workdir / f"rate_{rate}"
        rate_dir.mkdir(parents=True, exist_ok=True)
        wav_paths = synthesize_segments(narration, rate, rate_dir)
        durations = [wav_duration_seconds(path) for path in wav_paths]
        total_duration = sum(durations) + GAP_SECONDS * (len(durations) - 1)
        distance = abs(total_duration - TARGET_SECONDS)

        if distance < best_distance:
            best_rate = rate
            best_paths = wav_paths
            best_durations = durations
            best_distance = distance

    return best_rate, best_paths, best_durations


def concatenate_wavs(input_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    """Concatenate WAV files with short silence gaps between sentences."""
    if not input_paths:
        raise RuntimeError("没有可拼接的音频片段")

    with wave.open(str(input_paths[0]), "rb") as first_input:
        params = first_input.getparams()
        silence_frame_count = int(params.framerate * GAP_SECONDS)
        silence = b"\x00" * silence_frame_count * params.sampwidth * params.nchannels

    with wave.open(str(output_path), "wb") as output:
        output.setparams(params)
        for index, path in enumerate(input_paths):
            with wave.open(str(path), "rb") as current:
                output.writeframes(current.readframes(current.getnframes()))
            if index < len(input_paths) - 1:
                output.writeframes(silence)


def build_voice(narration: list[str], output_dir: pathlib.Path) -> dict[str, Any]:
    """Generate a final MP3 voice track and precise segment timings."""
    ensure_tools_exist()
    ffmpeg_path = resolve_ffmpeg()
    with tempfile.TemporaryDirectory(prefix="demo_voice_") as temp_dir:
        temp_root = pathlib.Path(temp_dir)
        rate, wav_paths, segment_durations = pick_best_voice_rate(narration, temp_root)
        wav_output = output_dir / "voice.wav"
        mp3_output = output_dir / "voice.mp3"
        concatenate_wavs(wav_paths, wav_output)
        run_command(
            [
                ffmpeg_path,
                "-y",
                "-i",
                str(wav_output),
                "-codec:a",
                "libmp3lame",
                "-b:a",
                "128k",
                str(mp3_output),
            ]
        )
        total_duration = wav_duration_seconds(wav_output)

    return {
        "rate": rate,
        "segment_durations": segment_durations,
        "total_duration": total_duration,
        "wav_path": wav_output,
        "mp3_path": mp3_output,
    }


def seconds_to_srt(value: float) -> str:
    """Format seconds as an SRT timestamp."""
    milliseconds = round(value * 1000)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def write_script_and_captions(
    plan: dict[str, Any],
    voice_info: dict[str, Any],
    output_dir: pathlib.Path,
) -> list[dict[str, Any]]:
    """Write script.txt and captions.srt based on measured audio timing."""
    (output_dir / "script.txt").write_text(plan["script"], encoding="utf-8")

    current = 0.0
    caption_rows: list[str] = []
    caption_entries: list[dict[str, Any]] = []
    durations = voice_info["segment_durations"]

    for index, (caption, duration) in enumerate(zip(plan["captions"], durations), start=1):
        start = current
        end = start + duration
        caption_entries.append(
            {
                "text": caption["text"],
                "start": start,
                "end": end,
                "slide_duration": duration + (GAP_SECONDS if index < len(durations) else 0.0),
            }
        )
        caption_rows.extend(
            [
                str(index),
                f"{seconds_to_srt(start)} --> {seconds_to_srt(end)}",
                caption["text"],
                "",
            ]
        )
        current = end + (GAP_SECONDS if index < len(durations) else 0.0)

    (output_dir / "captions.srt").write_text("\n".join(caption_rows).strip() + "\n", encoding="utf-8")
    return caption_entries


def write_manifest(
    plan: dict[str, Any],
    caption_entries: list[dict[str, Any]],
    voice_info: dict[str, Any],
    output_dir: pathlib.Path,
) -> pathlib.Path:
    """Write the slide manifest consumed by the Swift video builder."""
    slides = []
    for slide, caption in zip(plan["slides"], caption_entries):
        slides.append({**slide, "duration": caption["slide_duration"]})

    manifest = {
        "width": 1080,
        "height": 1920,
        "fps": 10,
        "audioPath": str((output_dir / "voice.mp3").resolve()),
        "outputPath": str((output_dir / "final.mp4").resolve()),
        "slides": slides,
        "totalDuration": voice_info["total_duration"],
    }
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest_path


def build_video(manifest_path: pathlib.Path) -> bool:
    """Attempt to render final.mp4 via the bundled Swift AVFoundation helper."""
    swift_path = ROOT / "video_builder.swift"
    if not swift_path.exists():
        return False

    try:
        run_command(["swift", str(swift_path), str(manifest_path)])
    except subprocess.CalledProcessError:
        return False

    return (DIST_DIR / "final.mp4").exists()


def main() -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    case = parse_case_markdown(CASE_PATH)
    plan = build_demo_plan(case)
    voice_info = build_voice(plan["narration"], DIST_DIR)
    caption_entries = write_script_and_captions(plan, voice_info, DIST_DIR)
    manifest_path = write_manifest(plan, caption_entries, voice_info, DIST_DIR)
    if build_video(manifest_path):
        pathlib.Path(voice_info["wav_path"]).unlink(missing_ok=True)
        manifest_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
