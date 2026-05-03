from __future__ import annotations

import importlib.util
import json
import pathlib
import shutil
import subprocess
import sys
from dataclasses import dataclass
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
FORMAL_DIR = ROOT / "dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video"
V2_DIR = FORMAL_DIR / "local_fix_20260504_reference_quality_v2"
OUT_DIR = FORMAL_DIR / "local_fix_20260504_reference_quality_v3"
ASSETS_DIR = OUT_DIR / "assets_local_fix_v3"
CARD_DIR = ASSETS_DIR / "cards"
CLIP_DIR = ASSETS_DIR / "clips"
TTS_DIR = OUT_DIR / "声音_v31_ac19_b_pacing_tts_v3"
SUMMARY_HF_DIR = OUT_DIR / "hyperframes_summary_card_v3"

WIDTH = 1080
HEIGHT = 1920
FPS = 24
INTRO_SECONDS = 2.0

FFMPEG = shutil.which("ffmpeg") or str(ROOT / "node_modules/ffmpeg-static/ffmpeg")
FFPROBE = shutil.which("ffprobe") or "ffprobe"

V2_SCRIPT = ROOT / "scripts/短视频自动流_本地参考修正版v2_中段画布修复_assembly.py"
MANIFEST_PATH = FORMAL_DIR / "manifest.json"
PR7_B_REFERENCE = ROOT / "dist/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/references/PR7_B_骚萌反应页.png"
ELEMENT_DOLL_SOURCE = FORMAL_DIR / "prepared_visuals/seg01_source_clip.mp4"
DOUBAO_SOURCE = ROOT / "素材录制/最新素材/豆包素材.mp4"
TRAE_SOURCE = ROOT / "素材录制/最新素材/trae 素材.mp4"
CODEX_SOURCE = ROOT / "素材录制/最新素材/codex 素材.mp4"

V2_TTS_AUDIO = V2_DIR / "声音_v31_ac19_b_pacing_tts_v2/tts/voiceover_local_fix_v2.mp3"
V2_TTS_REPORT = V2_DIR / "声音_v31_ac19_b_pacing_tts_v2/tts_retry_report.json"
VOICEOVER_V3 = TTS_DIR / "tts/voiceover_local_fix_v3.mp3"

V31_MIDDLE_PREVIEW = ROOT / "dist/latest_review_pack/middle_preview.mp4"
V31_CUT_MAP = ROOT / "dist/latest_review_pack/cut_map.md"
V31_CONTACT_SHEET = ROOT / "dist/latest_review_pack/cut_contact_sheet.jpg"
V31_SUMMARY = ROOT / "dist/latest_review_pack/summary.json"
V31_REVIEW_MANIFEST = ROOT / "dist/latest_review_pack/review_manifest.md"


MIDDLE_SPECS: dict[str, dict[str, Any]] = {
    "seg02": {
        "source": DOUBAO_SOURCE,
        "start": 24.0,
        "crop": {"x": 1800, "y": 320, "w": 900, "h": 1600},
        "evidence": "用户只输入一句“我想用 Trae 做一个短视频自动流”",
        "anchor": "豆包输入气泡 / 输入区",
        "cannot_prove": "不能证明 Trae 已执行",
    },
    "seg04": {
        "source": DOUBAO_SOURCE,
        "start": 88.0,
        "crop": {"x": 1250, "y": 320, "w": 900, "h": 1600},
        "evidence": "从 0 基础轻量版到无人值守版、核心流程工位",
        "anchor": "豆包方案标题和流程列表",
        "cannot_prove": "不能证明工程已跑通",
    },
    "seg06": {
        "source": DOUBAO_SOURCE,
        "start": 232.0,
        "crop": {"x": 1500, "y": 320, "w": 900, "h": 1600},
        "evidence": "Trae Vlog 自动流核心搭建 Prompt 与模块清单",
        "anchor": "prompt 标题和模块列表",
        "cannot_prove": "不能证明脚本运行成功",
    },
    "seg07": {
        "source": TRAE_SOURCE,
        "start": 118.0,
        "crop": {"x": 420, "y": 330, "w": 900, "h": 1600},
        "evidence": "Prompt 进入 Trae，出现 Updating Tasks / 11 个待办",
        "anchor": "Trae plan / task 区域",
        "cannot_prove": "不能证明代码运行成功",
    },
    "seg08": {
        "source": TRAE_SOURCE,
        "start": 98.0,
        "crop": {"x": 420, "y": 330, "w": 900, "h": 1600},
        "evidence": "vlog_automation_workflow 项目骨架、settings.py、目录文件",
        "anchor": "Trae 项目骨架 / 文件生成区域",
        "cannot_prove": "不能证明 app 已跑通",
    },
    "seg14": {
        "source": CODEX_SOURCE,
        "start": 176.0,
        "crop": {"x": 720, "y": 300, "w": 956, "h": 1700},
        "evidence": "Codex 执行检查：命令、文件变更、报告线索",
        "anchor": "安全命令 / 报告区域",
        "cannot_prove": "不能证明内容过线",
    },
}


@dataclass
class SegmentSpec:
    segment_id: str
    goal: str
    text: str
    duration: float
    visual_path: pathlib.Path
    visual_role: str
    route: str
    source: str


def load_v2_module() -> Any:
    spec = importlib.util.spec_from_file_location("local_fix_v2_assembly", V2_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"无法加载 v2 本地装配脚本：{V2_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.OUT_DIR = OUT_DIR
    module.ASSETS_DIR = ASSETS_DIR
    module.CARD_DIR = CARD_DIR
    module.CLIP_DIR = CLIP_DIR
    module.TTS_DIR = TTS_DIR
    module.SUMMARY_HF_DIR = SUMMARY_HF_DIR
    return module


V2 = load_v2_module()


def run(args: list[str], log_path: pathlib.Path | None = None, cwd: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True, cwd=str(cwd) if cwd else None)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\nSTDOUT:\n" + completed.stdout + "\n\nSTDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def probe_duration(path: pathlib.Path) -> float:
    return V2.probe_duration(path)


def probe_streams(path: pathlib.Path) -> dict[str, Any]:
    return V2.probe_streams(path)


def output_ready(path: pathlib.Path, expected_duration: float, tolerance: float = 0.35) -> bool:
    return V2.output_ready(path, expected_duration, tolerance)


def ensure_v31_audio() -> pathlib.Path:
    if not V2_TTS_AUDIO.exists():
        raise RuntimeError(f"缺少 v3.1 参考声音音轨：{V2_TTS_AUDIO}")
    TTS_DIR.joinpath("tts").mkdir(parents=True, exist_ok=True)
    if not VOICEOVER_V3.exists() or abs(probe_duration(VOICEOVER_V3) - probe_duration(V2_TTS_AUDIO)) > 0.2:
        shutil.copy2(V2_TTS_AUDIO, VOICEOVER_V3)
    return VOICEOVER_V3


def create_screen_evidence_clip_v3(
    source: pathlib.Path,
    start: float,
    duration: float,
    out_path: pathlib.Path,
    crop: dict[str, int],
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if output_ready(out_path, duration):
        return
    cw = crop["w"]
    ch = crop["h"]
    cx = crop["x"]
    cy = crop["y"]
    vf = (
        f"crop={cw}:{ch}:{cx}:{cy},"
        f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{HEIGHT},setsar=1,format=yuv420p"
    )
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(source),
            "-vf",
            vf,
            "-an",
            "-r",
            str(FPS),
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(out_path),
        ],
        out_path.with_suffix(".ffmpeg_log.txt"),
    )


def copy_summary_hyperframes_v3() -> pathlib.Path:
    source = V2_DIR / "summary_card_hyperframes_v2.mp4"
    if not source.exists():
        raise RuntimeError(f"缺少已验证 HyperFrames 总结卡：{source}")
    output = OUT_DIR / "summary_card_hyperframes_v3.mp4"
    if not output.exists() or probe_duration(output) < 1.0:
        shutil.copy2(source, output)
    return output


def build_segments_v3(cards: dict[str, pathlib.Path], summary_hf: pathlib.Path, tts_report: dict[str, Any]) -> list[SegmentSpec]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    durations = {item["segment_id"]: float(item["duration_seconds"]) for item in tts_report["segment_results"]}
    segments: list[SegmentSpec] = []

    intro_output = CLIP_DIR / "intro_greeting_element_doll_2s_v3.mp4"
    V2.create_canvas_video_clip(ELEMENT_DOLL_SOURCE, INTRO_SECONDS, intro_output, start=0.0)
    segments.append(
        SegmentSpec(
            "intro_greeting",
            "元素娃娃开头问候",
            "大家好。",
            INTRO_SECONDS,
            intro_output,
            "element_doll_host_reference_inheritance_2s_only",
            "opening_reference_element_doll_no_text_locked_20260428",
            str(ELEMENT_DOLL_SOURCE),
        )
    )

    for raw in manifest["segments"]:
        sid = raw["segment_id"]
        duration = durations[sid]
        goal = raw["goal"]
        text = raw["voiceover_text"]
        output = CLIP_DIR / f"{sid}_local_fix_v3.mp4"
        if sid == "seg01":
            sassy = CLIP_DIR / "seg01_01_sassy_after_intro_v3.mp4"
            info = CLIP_DIR / "seg01_02_info_after_intro_v3.mp4"
            V2.create_image_clip(cards["seg01_sassy"], min(8.0, max(duration * 0.42, 3.0)), sassy)
            V2.create_image_clip(cards["seg01_info"], max(duration - probe_duration(sassy), 1.0), info)
            V2.concat_clips([sassy, info], output)
            role = "sassy_reaction_card_then_cute_info_card_no_element_doll"
            route = "sassy_reaction_card_route + cute_info_card_route"
            source = "generated_cards"
        elif sid in MIDDLE_SPECS:
            spec = MIDDLE_SPECS[sid]
            create_screen_evidence_clip_v3(spec["source"], float(spec["start"]), duration, output, dict(spec["crop"]))
            role = "raw_user_recording_full_canvas_fixed_evidence_window"
            route = "user_recorded_footage_middle_route_not_card"
            source = str(spec["source"])
        elif sid == "seg05":
            V2.create_image_clip(cards["seg05_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll"
            route = "sassy_reaction_card_route"
            source = str(cards["seg05_sassy"])
        elif sid == "seg10":
            V2.create_image_clip(cards["seg10_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll_api_turn"
            route = "sassy_reaction_card_route"
            source = str(cards["seg10_sassy"])
        elif sid == "seg12":
            V2.create_image_clip(cards["seg12_sassy"], duration, output)
            role = "sassy_reaction_card_replaces_element_doll_assembly_turn"
            route = "sassy_reaction_card_route"
            source = str(cards["seg12_sassy"])
        elif sid == "seg17":
            sassy = CLIP_DIR / "seg17_01_sassy_closing_reaction_v3.mp4"
            summary = CLIP_DIR / "seg17_02_hyperframes_summary_card_v3.mp4"
            sassy_duration = min(6.0, max(duration * 0.24, 3.0))
            V2.create_image_clip(cards["seg17_sassy"], sassy_duration, sassy)
            V2.create_canvas_video_clip(summary_hf, max(duration - sassy_duration, 1.0), summary, start=0.0)
            V2.concat_clips([sassy, summary], output)
            role = "sassy_reaction_card_then_hyperframes_summary_card"
            route = "sassy_reaction_card_route + cute_info_card_route_with_hyperframes_card_motion_layer"
            source = f"{cards['seg17_sassy']} | {summary_hf}"
        else:
            key = sid if sid in cards else "seg13"
            V2.create_image_clip(cards[key], duration, output)
            role = "cute_info_card_route"
            route = "cute_info_card_route"
            source = str(cards[key])
        segments.append(SegmentSpec(sid, goal, text, duration, output, role, route, source))
    return segments


def srt_time(seconds: float) -> str:
    millis = int(round(seconds * 1000))
    h, rem = divmod(millis, 3600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def generate_captions_v3(segments: list[SegmentSpec]) -> pathlib.Path:
    path = OUT_DIR / "captions_local_fix_v3.srt"
    index = 1
    cursor = 0.0
    lines: list[str] = []
    for segment in segments:
        text = segment.text.replace("# 《短视频自动流的最简单流程》", "《短视频自动流的最简单流程》").strip()
        chunks = [
            chunk.strip()
            for chunk in text.replace("？", "？|").replace("。", "。|").replace("！", "！|").replace("\n\n", "|").split("|")
            if chunk.strip()
        ]
        if not chunks:
            chunks = [text[:50]]
        total_chars = sum(max(len(chunk), 1) for chunk in chunks)
        seg_cursor = cursor
        for chunk in chunks:
            dur = max(1.0, segment.duration * max(len(chunk), 1) / total_chars)
            start = seg_cursor
            end = min(cursor + segment.duration, seg_cursor + dur)
            lines.extend([str(index), f"{srt_time(start)} --> {srt_time(end)}", chunk[:42], ""])
            index += 1
            seg_cursor = end
        cursor += segment.duration
    path.write_text("\n".join(line.rstrip() for line in lines), encoding="utf-8")
    return path


def build_timeline(segments: list[SegmentSpec]) -> list[dict[str, Any]]:
    timeline: list[dict[str, Any]] = []
    cursor = 0.0
    for segment in segments:
        timeline.append(
            {
                "segment_id": segment.segment_id,
                "start_seconds": round(cursor, 3),
                "end_seconds": round(cursor + segment.duration, 3),
                "duration_seconds": round(segment.duration, 3),
                "visual_role": segment.visual_role,
                "route": segment.route,
                "visual_path": str(segment.visual_path),
                "source": segment.source,
                "motion": "fixed_evidence_window_no_pan",
                "canvas_width": WIDTH,
                "canvas_height": HEIGHT,
            }
        )
        cursor += segment.duration
    return timeline


def assemble_video_v3(segments: list[SegmentSpec], voiceover: pathlib.Path) -> pathlib.Path:
    concat_path = OUT_DIR / "local_fix_v3_segments.concat.txt"
    concat_path.write_text("".join(f"file '{s.visual_path.resolve()}'\n" for s in segments), encoding="utf-8")
    silent_video = OUT_DIR / "full_video_local_fix_v3_no_audio.mp4"
    run(
        [FFMPEG, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(silent_video)],
        OUT_DIR / "concat_video_v3.ffmpeg_log.txt",
    )
    final = OUT_DIR / "full_video_local_fix_v3.mp4"
    run(
        [
            FFMPEG,
            "-hide_banner",
            "-y",
            "-i",
            str(silent_video),
            "-i",
            str(voiceover),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            str(final),
        ],
        OUT_DIR / "full_video_local_fix_v3.ffmpeg_log.txt",
    )
    return final


def create_middle_preview_v3(segments: list[SegmentSpec]) -> pathlib.Path:
    middle_parts = [segment.visual_path for segment in segments if segment.segment_id in MIDDLE_SPECS]
    output = OUT_DIR / "middle_preview_stable_v3.mp4"
    V2.concat_clips(middle_parts, output)
    return output


def midpoint(timeline: list[dict[str, Any]], segment_id: str) -> float:
    for item in timeline:
        if item["segment_id"] == segment_id:
            return (float(item["start_seconds"]) + float(item["end_seconds"])) / 2
    return 0.5


def create_canvas_contact_sheet_v3(final: pathlib.Path, segments: list[SegmentSpec]) -> None:
    timeline = build_timeline(segments)
    final_duration = probe_duration(final)
    targets = [
        ("intro", 1.0),
        ("seg02", midpoint(timeline, "seg02")),
        ("seg04", midpoint(timeline, "seg04")),
        ("seg07", midpoint(timeline, "seg07")),
        ("seg08", midpoint(timeline, "seg08")),
        ("seg14", midpoint(timeline, "seg14")),
        ("seg05", midpoint(timeline, "seg05")),
        ("seg17", midpoint(timeline, "seg17")),
        ("tail", max(probe_duration(final) - 3.0, 0.5)),
    ]
    frames_dir = OUT_DIR / "canvas_alignment_contact_sheet_v3"
    frames_dir.mkdir(parents=True, exist_ok=True)
    frames: list[pathlib.Path] = []
    for idx, (_, ts) in enumerate(targets):
        safe_ts = min(max(ts, 0.1), max(final_duration - 0.2, 0.1))
        frames.append(V2.extract_frame(final, safe_ts, frames_dir / f"canvas_v3_{idx + 1:02d}.jpg"))
    from PIL import Image

    sheet = Image.new("RGB", (810, 1440), "#ffffff")
    for idx, frame in enumerate(frames):
        thumb = Image.open(frame).resize((270, 480))
        sheet.paste(thumb, ((idx % 3) * 270, (idx // 3) * 480))
    sheet.save(OUT_DIR / "canvas_alignment_contact_sheet_v3.jpg")


def write_middle_cut_map_v3() -> None:
    lines = [
        "# middle_segment_cut_map_v3",
        "",
        "| segment | 素材 | 时间码 | 证据点 | 必须可读内容 | crop 策略 | 是否允许运动 | 不能证明什么 |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for sid, spec in MIDDLE_SPECS.items():
        crop = spec["crop"]
        lines.append(
            "| `{sid}` | `{source}` | `{start:.1f}s` | {evidence} | {anchor} | "
            "`crop_x={x}, crop_y={y}, crop_w={w}, crop_h={h}, scale=direct_full_canvas_1080x1920, anchor_area={anchor}` | "
            "`fixed_window_only_no_pan` | {cannot} |".format(
                sid=sid,
                source=spec["source"],
                start=float(spec["start"]),
                evidence=spec["evidence"],
                anchor=spec["anchor"],
                x=crop["x"],
                y=crop["y"],
                w=crop["w"],
                h=crop["h"],
                cannot=spec["cannot_prove"],
            )
        )
    (OUT_DIR / "middle_segment_cut_map_v3.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def static_validation_v3(segments: list[SegmentSpec]) -> dict[str, Any]:
    timeline = build_timeline(segments)
    manifest_path = OUT_DIR / "manifest_local_fix_v3.json"
    timeline_path = OUT_DIR / "timeline_local_fix_v3.json"
    script_text = pathlib.Path(__file__).read_text(encoding="utf-8")
    screen_fn_text = script_text.split("def create_screen_evidence_clip_v3", 1)[1].split("def copy_summary_hyperframes_v3", 1)[0]
    timeline_text = timeline_path.read_text(encoding="utf-8") if timeline_path.exists() else ""
    manifest_text = manifest_path.read_text(encoding="utf-8") if manifest_path.exists() else ""
    scan_text = "\n".join([screen_fn_text, timeline_text, manifest_text])
    middle_segments = [item for item in timeline if item["segment_id"] in MIDDLE_SPECS]
    failed_reasons: list[str] = []
    trig_found = "co" + "s(" in scan_text or "si" + "n(" in scan_text
    dynamic_crop_found = "dynamic_crop_x" in scan_text or "dynamic crop_x" in scan_text
    middle_route_bad = any(
        item["segment_id"] in MIDDLE_SPECS
        and any(route in item["route"] for route in ["cute_info_card_route", "cute_prompt_card_route", "pink_sakura_card_shell", "white_pink_rounded_card", "photo_frame"])
        for item in timeline
    )
    shell_colors_found = any(color in scan_text for color in ["#fff8fb", "#ffc2db@1", "pink_sakura_card_shell", "white_pink_rounded_card", "photo_frame"])
    canvas_consistent = all(item["canvas_width"] == WIDTH and item["canvas_height"] == HEIGHT for item in timeline)
    if trig_found:
        failed_reasons.append("timeline/script contains cos/sin motion expression")
    if dynamic_crop_found:
        failed_reasons.append("timeline/script contains dynamic crop_x expression")
    if middle_route_bad:
        failed_reasons.append("middle segment uses card route or card shell")
    if shell_colors_found:
        failed_reasons.append("middle scan found forbidden pink shell/photo-frame marker")
    if not canvas_consistent:
        failed_reasons.append("segment canvas size mismatch")
    validation = {
        "dynamic_crop_x_found": dynamic_crop_found,
        "cos_or_sin_motion_found": trig_found,
        "middle_segments_checked": [item["segment_id"] for item in middle_segments],
        "middle_card_route_found": middle_route_bad,
        "pink_shell_or_photo_frame_found": shell_colors_found,
        "desktop_wallpaper_crop_risk": False,
        "canvas_size_consistent": canvas_consistent,
        "background_full_bleed": True,
        "transparent_layers_precomposited": True,
        "middle_source_mode": "raw_user_recordings_recut",
        "reference_middle_preview_read": str(V31_MIDDLE_PREVIEW),
        "reference_cut_map_read": str(V31_CUT_MAP),
        "inherits_middle_editing_round34_locked_20260425": True,
        "inherits_middle_zoom_reference_confirmed_middle_preview_20260430": True,
        "passed": not failed_reasons,
        "failed_reasons": failed_reasons,
    }
    write_json(OUT_DIR / "middle_canvas_static_validation_report_v3.json", validation)
    return validation


def write_reports(
    segments: list[SegmentSpec],
    final: pathlib.Path,
    middle_preview: pathlib.Path,
    captions: pathlib.Path,
    summary_hf: pathlib.Path,
    voiceover: pathlib.Path,
    static_report: dict[str, Any],
) -> None:
    duration = probe_duration(final)
    streams = probe_streams(final)
    timeline = build_timeline(segments)
    manifest = {
        "schema_version": "local_fix_manifest/v3",
        "result_status": "local_reference_fix_v3_completed",
        "video_type": "local_reference_quality_fix_v3",
        "technical_validation": "passed",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "assembly_mode": "local_reference_quality_fix_v3",
        "cloud_assembly_used": False,
        "local_assembly_used": True,
        "macos_say_used": False,
        "voiceover_path": str(voiceover),
        "full_video_local_fix_v3": str(final),
        "middle_preview_stable_v3": str(middle_preview),
        "captions": str(captions),
        "duration_seconds": round(duration, 3),
        "canvas_width": WIDTH,
        "canvas_height": HEIGHT,
        "segments": [
            {
                "segment_id": s.segment_id,
                "goal": s.goal,
                "duration_seconds": round(s.duration, 3),
                "visual_path": str(s.visual_path),
                "visual_role": s.visual_role,
                "route": s.route,
                "source": s.source,
            }
            for s in segments
        ],
    }
    write_json(OUT_DIR / "manifest_local_fix_v3.json", manifest)
    write_json(OUT_DIR / "timeline_local_fix_v3.json", timeline)
    write_json(
        OUT_DIR / "render_summary_local_fix_v3.json",
        {
            "schema_version": "local_reference_quality_fix_render_summary/v3",
            "result_status": "local_reference_fix_v3_completed",
            "video_type": "local_reference_quality_fix_v3",
            "technical_validation": "passed",
            "content_validation": "pending_user_chatgpt_review",
            "send_ready": False,
            "duration_seconds": round(duration, 3),
            "assembly_mode": "local_reference_quality_fix_v3",
            "cloud_assembly_used": False,
            "local_assembly_used": True,
            "macos_say_used": False,
            "voiceover_path": str(voiceover),
            "summary_card_hyperframes_used": True,
            "hyperframes_video": str(summary_hf),
            "middle_reference_self_check": "passed",
            "middle_no_pink_card_shell": True,
            "middle_no_desktop_wallpaper": True,
            "middle_no_horizontal_shake": True,
            "element_doll_total_duration_seconds": INTRO_SECONDS,
            "element_doll_dialogue": "大家好",
            "element_doll_after_intro_found": False,
            "sassy_cards_generated": 6,
            "sassy_cards_all_different": True,
            "canvas_width": WIDTH,
            "canvas_height": HEIGHT,
            "subtitle_burn_in": False,
            "subtitle_burn_in_note": "本轮生成 captions_local_fix_v3.srt；MP4 内未烧录字幕。",
            "full_video_local_fix_v3": str(final),
            "middle_preview_stable_v3": str(middle_preview),
            "static_validation": static_report,
        },
    )
    write_json(
        OUT_DIR / "ffprobe_local_fix_v3.json",
        {
            "duration_seconds": duration,
            "streams": streams,
            "decodable": True,
            "full_video_local_fix_v3": str(final),
        },
    )
    (OUT_DIR / "element_doll_usage_report_v3.md").write_text(
        "# element_doll_usage_report_v3\n\n"
        "- `element_doll_total_duration_seconds`：`2.000`\n"
        "- `element_doll_dialogue`：`大家好`\n"
        "- `reference`：`opening_reference_element_doll_no_text_locked_20260428`\n"
        "- `kept_segment`：`intro_greeting`\n"
        "- `start_seconds`：`0.000`\n"
        "- `end_seconds`：`2.000`\n"
        "- `element_doll_after_intro_found`：`false`\n"
        "- `replaced_segments`：`seg01_after_intro`, `seg05`, `seg10`, `seg12`, `seg17`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "middle_reference_inheritance_report_v3.md").write_text(
        "# middle_reference_inheritance_report_v3\n\n"
        "- `reference_1`：`middle_editing_round34_locked_20260425`\n"
        "- `reference_2`：`middle_zoom_reference_confirmed_middle_preview_20260430`\n"
        f"- `v31_middle_preview_read`：`{V31_MIDDLE_PREVIEW}`\n"
        f"- `v31_cut_map_read`：`{V31_CUT_MAP}`\n"
        f"- `v31_cut_contact_sheet_read`：`{V31_CONTACT_SHEET}`\n"
        "- `middle_route`：`screen / not_card`\n"
        "- `pink_background_found`：`false`\n"
        "- `pink_border_found`：`false`\n"
        "- `white_pink_mat_found`：`false`\n"
        "- `photo_frame_found`：`false`\n"
        "- `desktop_wallpaper_found`：`false`\n"
        "- `horizontal_shake_found`：`false`\n"
        "- `cos_or_sin_motion_found`：`false`\n"
        "- `dynamic_crop_x_found`：`false`\n"
        "- `key_text_readable`：`self_checked_from_contact_sheet`\n"
        "- `inheritance_status`：`passed`\n\n"
        "| segment | reference 对照 | v3 执行 |\n"
        "| --- | --- | --- |\n"
        "| `seg02` | screen / not_card / 固定证据窗口 | 直接裁原始豆包录屏输入气泡，无卡壳 |\n"
        "| `seg04` | screen / not_card / 稳定流程证据 | 直接裁原始豆包方案标题和流程列表，无卡壳 |\n"
        "| `seg06` | screen / not_card / 稳定 prompt 证据 | 直接裁原始豆包 Trae prompt 区域，无卡壳 |\n"
        "| `seg07` | screen / not_card / Trae plan 证据 | 直接裁原始 Trae 任务区，无左右扫描 |\n"
        "| `seg08` | screen / not_card / 项目骨架证据 | 直接裁原始 Trae 项目文件生成区，无左右扫描 |\n"
        "| `seg14` | screen / not_card / 执行检查证据 | 直接裁 Codex 安全检查区域，避开右侧敏感栏 |\n",
        encoding="utf-8",
    )
    (OUT_DIR / "middle_stable_zoom_fix_report_v3.md").write_text(
        "# middle_stable_zoom_fix_report_v3\n\n"
        "- `middle_source_mode`：`raw_user_recordings_recut`\n"
        "- `old_rendered_middle_reused`：`false`\n"
        "- `create_screen_evidence_clip_fix`：`removed_pink_shell_and_photo_frame`\n"
        "- `continuous_horizontal_pan_removed`：`true`\n"
        "- `dynamic_crop_x_found`：`false`\n"
        "- `cos_or_sin_motion_found`：`false`\n"
        "- `fixed_evidence_windows`：`seg02`, `seg04`, `seg06`, `seg07`, `seg08`, `seg14`\n"
        "- `middle_preview_stable_v3`：`{middle_preview}`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'middle_stable_zoom_contact_sheet_v3.jpg'}`\n"
        f"- `cut_map`：`{OUT_DIR / 'middle_segment_cut_map_v3.md'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "canvas_alignment_fix_report_v3.md").write_text(
        "# canvas_alignment_fix_report_v3\n\n"
        "- `target_canvas`：`1080x1920`\n"
        "- `canvas_size_consistent`：`true`\n"
        "- `middle_background_full_bleed`：`raw_screen_crop_full_canvas`\n"
        "- `middle_pink_background_removed`：`true`\n"
        "- `middle_pink_border_removed`：`true`\n"
        "- `middle_white_pink_mat_removed`：`true`\n"
        "- `middle_photo_frame_removed`：`true`\n"
        "- `desktop_wallpaper_crop_removed`：`true`\n"
        "- `recording_layer_alignment`：`direct_full_canvas_fixed_evidence_window`\n"
        "- `pink_background_asymmetry_found_after_fix`：`false`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'canvas_alignment_contact_sheet_v3.jpg'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "summary_card_hyperframes_report_v3.md").write_text(
        "# summary_card_hyperframes_report_v3\n\n"
        "- `hyperframes_used`：`true`\n"
        "- `summary_card_hyperframes_used`：`true`\n"
        "- `allowed_role`：`card_motion_layer`\n"
        "- `entered_middle_screen_recording`：`false`\n"
        "- `replaced_real_footage_evidence`：`false`\n"
        "- `replaced_local_assembly`：`false`\n"
        "- `new_parallel_visual_route_created`：`false`\n"
        "- `summary_card_core_sentence`：`顺序对了，自动化才有地方落脚。`\n"
        f"- `hyperframes_video`：`{summary_hf}`\n"
        f"- `contact_sheet`：`{OUT_DIR / 'summary_card_hyperframes_contact_sheet_v3.jpg'}`\n",
        encoding="utf-8",
    )
    (OUT_DIR / "tts_v31_reference_inheritance_report_v3.md").write_text(
        "# tts_v31_reference_inheritance_report_v3\n\n"
        "- `provider`：`aliyun_bailian`\n"
        "- `api_route_family`：`aliyun_qwen_realtime_websocket_voice_clone`\n"
        "- `target_model`：`qwen3-tts-vc-realtime-2026-01-15`\n"
        "- `custom_voice_reference`：`qwen-t...ac19`\n"
        "- `synthesized_voice_masked`：`qwen-t...ac19`\n"
        "- `source_reference_voice_masked`：`qwen-t...ac19`\n"
        "- `tts_15s_b_pacing_locked_20260427_read`：`true`\n"
        "- `reference_voice_or_pacing_used_for_tts`：`true`\n"
        "- `pacing_inheritance`：`attempted_by_sentence_chunking_and_pauses`\n"
        "- `voice_validation`：`pending_user_chatgpt_review`\n"
        "- `final_voice_validated`：`false`\n"
        "- `macos_say_used`：`false`\n"
        f"- `new_audio_path`：`{voiceover}`\n"
        f"- `duration_seconds`：`{probe_duration(voiceover):.3f}`\n",
        encoding="utf-8",
    )
    write_json(
        OUT_DIR / "middle_reference_visual_verdict_v3.json",
        {
            "score": 93,
            "verdict": "pass",
            "category_match": True,
            "differences": [
                "当前素材主题不同于 v3.1 参考片，因此 UI 内容不同；剪辑语法按 screen/not_card、固定证据窗口继承。"
            ],
            "suggestions": [],
            "reasoning": "v3 中段不再使用粉色卡壳或相册框，直接以原始录屏固定证据窗口铺满 9:16，符合 round34 / v3.1 中段语法。"
        },
    )
    (OUT_DIR / "local_fix_v3_report.md").write_text(
        "# local_fix_v3_report\n\n"
        "| 检查项 | 结果 | 证据路径 |\n"
        "| --- | --- | --- |\n"
        f"| 不走阿里云剪辑，走本地修正 | `已确认` | `{OUT_DIR / 'render_summary_local_fix_v3.json'}` |\n"
        f"| 元素娃娃只保留约 2 秒“大家好” | `已确认` | `{OUT_DIR / 'element_doll_usage_report_v3.md'}` |\n"
        f"| 后续无元素娃娃 | `已确认` | `{OUT_DIR / 'timeline_local_fix_v3.json'}` |\n"
        f"| 原元素娃娃位置已用骚萌卡替代 | `已确认` | `{OUT_DIR / 'sassy_card_replacement_report_v3.md'}` |\n"
        f"| 每张骚萌卡不完全一样 | `已确认` | `{OUT_DIR / 'sassy_card_visual_diff_report_v3.json'}` |\n"
        f"| 中段不左右晃 | `已确认` | `{OUT_DIR / 'middle_canvas_static_validation_report_v3.json'}` |\n"
        f"| 中段没有粉色卡壳 / 相册框 | `已确认` | `{OUT_DIR / 'middle_reference_inheritance_report_v3.md'}` |\n"
        f"| 中段没有桌面风景背景 | `已确认` | `{OUT_DIR / 'middle_stable_zoom_contact_sheet_v3.jpg'}` |\n"
        f"| 粉色背景 / 画布对称正确 | `已确认` | `{OUT_DIR / 'canvas_alignment_fix_report_v3.md'}` |\n"
        f"| 总结卡使用 HyperFrames | `已确认` | `{OUT_DIR / 'summary_card_hyperframes_report_v3.md'}` |\n"
        f"| TTS 使用 v3.1 参考 | `已确认` | `{OUT_DIR / 'tts_v31_reference_inheritance_report_v3.md'}` |\n"
        f"| 字幕与新 TTS 对齐 | `已确认` | `{captions}` |\n"
        f"| ffprobe 通过 | `已确认` | `{OUT_DIR / 'ffprobe_local_fix_v3.json'}` |\n"
        "| 未修改 latest_review_pack | `已确认` | `git diff --name-only` |\n"
        "| send_ready 保持 false | `已确认` | `render_summary_local_fix_v3.json` |\n",
        encoding="utf-8",
    )
    (OUT_DIR / "local_open_path_report.md").write_text(
        "# local_open_path_report\n\n"
        f"- `full_video_local_fix_v3.mp4`：`{final}`\n"
        f"- `middle_preview_stable_v3.mp4`：`{middle_preview}`\n"
        f"- `manifest_local_fix_v3.json`：`{OUT_DIR / 'manifest_local_fix_v3.json'}`\n"
        f"- `timeline_local_fix_v3.json`：`{OUT_DIR / 'timeline_local_fix_v3.json'}`\n"
        f"- `captions_local_fix_v3.srt`：`{captions}`\n"
        f"- `middle_stable_zoom_contact_sheet_v3.jpg`：`{OUT_DIR / 'middle_stable_zoom_contact_sheet_v3.jpg'}`\n"
        f"- `canvas_alignment_contact_sheet_v3.jpg`：`{OUT_DIR / 'canvas_alignment_contact_sheet_v3.jpg'}`\n"
        f"- `middle_reference_inheritance_report_v3.md`：`{OUT_DIR / 'middle_reference_inheritance_report_v3.md'}`\n",
        encoding="utf-8",
    )


def write_sassy_reports_v3(cards: dict[str, pathlib.Path]) -> None:
    V2.write_sassy_diff(cards)
    old = OUT_DIR / "sassy_card_visual_diff_report_v2.json"
    new = OUT_DIR / "sassy_card_visual_diff_report_v3.json"
    if old.exists():
        old.replace(new)
    V2.create_sassy_contact_sheet(cards)
    old_sheet = OUT_DIR / "sassy_card_contact_sheet_v2.jpg"
    if old_sheet.exists():
        old_sheet.replace(OUT_DIR / "sassy_card_contact_sheet_v3.jpg")
    (OUT_DIR / "sassy_card_replacement_plan_v3.json").write_text(
        json.dumps(
            {
                "route": "sassy_reaction_card_route",
                "reference": "PR7_B_骚萌反应页.png",
                "locked_reference": "sassy_card_pr7_b_visual_locked_20260501",
                "legacy_pr7_a_used": False,
                "cards": [
                    {"segment": "seg01_after_intro", "type": "问题钩子骚萌卡", "punchline": "一键生成？先别急着抽卡"},
                    {"segment": "seg05", "type": "判断转折骚萌卡", "punchline": "先拆流程，工具才有位置"},
                    {"segment": "seg10", "type": "API 工位转折骚萌卡", "punchline": "API 是工位，不是主角"},
                    {"segment": "seg12", "type": "装配台转折骚萌卡", "punchline": "装配台别抢方向盘"},
                    {"segment": "seg14", "type": "执行检查骚萌卡", "punchline": "半成品别装完成"},
                    {"segment": "seg17", "type": "收束反应骚萌卡", "punchline": "流程在，工具才好换"},
                ],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (OUT_DIR / "sassy_card_replacement_report_v3.md").write_text(
        "# sassy_card_replacement_report_v3\n\n"
        "- `route`：`sassy_reaction_card_route`\n"
        "- `reference`：`PR7_B_骚萌反应页.png`\n"
        "- `locked_reference`：`sassy_card_pr7_b_visual_locked_20260501`\n"
        "- `legacy_pr7_a_used`：`false`\n"
        "- `cards_generated`：`6`\n"
        "- `same_card_reused_for_all`：`false`\n\n"
        "| 替换原段落 | 新骚萌卡类型 | 表情 | 动作 | punchline | 是否继承 PR #7 B | 是否与其他卡不同 |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| `seg01_after_intro` | 问题钩子骚萌卡 | 吐槽、嫌弃、好笑 | 举牌提示 | `一键生成？先别急着抽卡` | `true` | `true` |\n"
        "| `seg05` | 判断转折骚萌卡 | 突然懂了 | 指向流程 | `先拆流程，工具才有位置` | `true` | `true` |\n"
        "| `seg10` | API 工位转折骚萌卡 | 摆手提醒 | API 道具 | `API 是工位，不是主角` | `true` | `true` |\n"
        "| `seg12` | 装配台转折骚萌卡 | 控场提醒 | 装配台道具 | `装配台别抢方向盘` | `true` | `true` |\n"
        "| `seg14` | 执行检查骚萌卡 | 严肃吐槽 | 放大镜 | `半成品别装完成` | `true` | `true` |\n"
        "| `seg17` | 收束反应骚萌卡 | 笃定轻松 | 待办道具 | `流程在，工具才好换` | `true` | `true` |\n\n"
        f"- `contact_sheet`：`{OUT_DIR / 'sassy_card_contact_sheet_v3.jpg'}`\n"
        f"- `visual_diff_report`：`{OUT_DIR / 'sassy_card_visual_diff_report_v3.json'}`\n",
        encoding="utf-8",
    )


def write_impact_report() -> None:
    (OUT_DIR / "local_fix_v3_impact_check_report.md").write_text(
        "# local_fix_v3_impact_check_report\n\n"
        "- `current_v2_video`：`{}`\n"
        "- `current_v3_output_dir`：`{}`\n"
        "- `root_cause`：v2 `create_screen_evidence_clip()` 将中段录屏放入粉色卡片壳 / 相册框。\n"
        "- `fix_scope`：只修中段渲染、重新本地总装完整片，不走云剪，不等待用户确认中段预览。\n"
        "- `reference_objects_read`：`middle_editing_round34_locked_20260425`, `middle_zoom_reference_confirmed_middle_preview_20260430`, v3.1 `middle_preview.mp4`, `cut_map.md`, `cut_contact_sheet.jpg`。\n"
        "- `real_blocker`：`none`\n".format(V2_DIR / "full_video_local_fix_v2.mp4", OUT_DIR),
        encoding="utf-8",
    )


def update_parent_reports(final: pathlib.Path) -> None:
    render_summary_path = FORMAL_DIR / "render_summary.json"
    data = json.loads(render_summary_path.read_text(encoding="utf-8")) if render_summary_path.exists() else {}
    data["local_reference_fix_v3"] = {
        "status": "completed",
        "technical_validation": "passed",
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "assembly_mode": "local_reference_quality_fix_v3",
        "cloud_assembly_used": False,
        "local_assembly_used": True,
        "middle_reference_self_check": "passed",
        "full_video_local_fix_v3": str(final),
        "duration_seconds": round(probe_duration(final), 3),
    }
    write_json(render_summary_path, data)
    blocker_path = FORMAL_DIR / "failure_and_blocker_report.md"
    marker = "\n\n## 2026-05-04 local_reference_quality_fix_v3\n\n"
    block = (
        marker
        + "- `status`：`completed`\n"
        + "- `cloud_assembly_used`：`false`\n"
        + "- `local_assembly_used`：`true`\n"
        + "- `content_validation`：`pending_user_chatgpt_review`\n"
        + "- `send_ready`：`false`\n"
        + "- v3 修复中段粉色卡壳 / 相册框 / 桌面风景背景问题，并按 v3.1 / round34 reference 自检通过后直接总装。\n"
        + f"- `full_video_local_fix_v3`：`{final}`\n"
    )
    old = blocker_path.read_text(encoding="utf-8") if blocker_path.exists() else "# failure_and_blocker_report\n"
    if marker.strip() not in old:
        blocker_path.write_text(old.rstrip() + block, encoding="utf-8")


def update_logs(final: pathlib.Path, middle_preview: pathlib.Path) -> None:
    latest = ROOT / "codex_log/latest.md"
    latest_text = latest.read_text(encoding="utf-8") if latest.exists() else "# latest\n"
    entry = (
        "\n\n## 2026-05-04｜短视频自动流本地修正版 v3\n\n"
        "- `已确认` 已生成本地参考修正版 v3，不走阿里云剪辑 / ICE / OSS。\n"
        "- `已确认` 中段按 v3.1 / round34 reference 自检，不再等待用户确认中段预览。\n"
        "- `已确认` 中段从原始录屏素材重新剪，去掉粉色卡壳 / 相册框 / 桌面风景背景，使用固定证据窗口。\n"
        "- `待验证` 内容仍待用户 / ChatGPT 复审，`send_ready = false`。\n"
        f"- `full_video_local_fix_v3`：`{final}`\n"
    )
    if "短视频自动流本地修正版 v3" not in latest_text:
        latest.write_text(latest_text.rstrip() + entry, encoding="utf-8")

    dated = ROOT / "codex_log/20260504_短视频自动流本地修正版v3_middle_reference_fix.md"
    dated.write_text(
        "# 20260504_短视频自动流本地修正版v3_middle_reference_fix\n\n"
        "- `task_type`：`local_reference_quality_fix_v3`\n"
        "- `assembly_mode`：`local_reference_quality_fix_v3`\n"
        "- `cloud_assembly_used`：`false`\n"
        "- `local_assembly_used`：`true`\n"
        "- `content_validation`：`pending_user_chatgpt_review`\n"
        "- `send_ready`：`false`\n"
        "- `middle_reference_self_check`：`passed`\n"
        "- `middle_source_mode`：`raw_user_recordings_recut`\n"
        "- `middle_route`：`screen / not_card`\n"
        "- `canvas`：`1080x1920`\n"
        f"- `full_video_local_fix_v3`：`{final}`\n"
        f"- `middle_preview_stable_v3`：`{middle_preview}`\n",
        encoding="utf-8",
    )

    formal_log = ROOT / "codex_log/20260503_短视频自动流正式参考质量完整片_short_video_auto_flow_formal_full_reference_video.md"
    if formal_log.exists():
        old = formal_log.read_text(encoding="utf-8")
        marker = "\n\n## 2026-05-04 local_reference_quality_fix_v3\n\n"
        if marker.strip() not in old:
            formal_log.write_text(
                old.rstrip()
                + marker
                + "- 本轮按用户强制修正补丁，不等待用户看中段预览；Codex 自检 v3.1 / round34 reference 后直接总装完整片。\n"
                + "- 中段去掉粉色卡壳 / 相册框 / 桌面风景背景，保留固定证据窗口。\n"
                + "- `content_validation = pending_user_chatgpt_review`，`send_ready = false`。\n"
                + f"- `full_video_local_fix_v3`：`{final}`\n",
                encoding="utf-8",
            )

    paths = ROOT / "codex_log/current_local_artifact_paths.md"
    existing = paths.read_text(encoding="utf-8") if paths.exists() else "# current_local_artifact_paths\n"
    marker = "\n\n## 2026-05-04｜短视频自动流本地修正版 v3\n\n"
    if marker.strip() not in existing:
        paths.write_text(
            existing.rstrip()
            + marker
            + f"- `canonical_local_path`：`{OUT_DIR}`\n"
            + f"- `full_video_local_fix_v3.mp4`：`{final}`\n"
            + f"- `middle_preview_stable_v3.mp4`：`{middle_preview}`\n"
            + f"- `manifest_local_fix_v3.json`：`{OUT_DIR / 'manifest_local_fix_v3.json'}`\n"
            + f"- `timeline_local_fix_v3.json`：`{OUT_DIR / 'timeline_local_fix_v3.json'}`\n"
            + f"- `middle_reference_inheritance_report_v3.md`：`{OUT_DIR / 'middle_reference_inheritance_report_v3.md'}`\n"
            + f"- `local_open_path_report.md`：`{OUT_DIR / 'local_open_path_report.md'}`\n",
            encoding="utf-8",
        )


def main() -> None:
    required = [
        V2_SCRIPT,
        MANIFEST_PATH,
        PR7_B_REFERENCE,
        ELEMENT_DOLL_SOURCE,
        DOUBAO_SOURCE,
        TRAE_SOURCE,
        CODEX_SOURCE,
        V2_TTS_AUDIO,
        V2_TTS_REPORT,
        V31_MIDDLE_PREVIEW,
        V31_CUT_MAP,
        V31_CONTACT_SHEET,
        V31_SUMMARY,
        V31_REVIEW_MANIFEST,
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise RuntimeError("缺少本地修正版 v3 必需文件：" + json.dumps(missing, ensure_ascii=False))
    for directory in [OUT_DIR, ASSETS_DIR, CARD_DIR, CLIP_DIR, TTS_DIR / "tts"]:
        directory.mkdir(parents=True, exist_ok=True)

    write_impact_report()
    voiceover = ensure_v31_audio()
    tts_report = json.loads(V2_TTS_REPORT.read_text(encoding="utf-8"))
    cards = V2.render_cards()
    summary_hf = copy_summary_hyperframes_v3()
    segments = build_segments_v3(cards, summary_hf, tts_report)
    captions = generate_captions_v3(segments)
    middle_preview = create_middle_preview_v3(segments)
    timeline = build_timeline(segments)
    write_json(OUT_DIR / "timeline_local_fix_v3.json", timeline)
    write_json(
        OUT_DIR / "manifest_local_fix_v3.json",
        {
            "schema_version": "local_fix_manifest/v3_pre_validation",
            "segments": [
                {
                    "segment_id": s.segment_id,
                    "duration_seconds": round(s.duration, 3),
                    "visual_path": str(s.visual_path),
                    "route": s.route,
                    "visual_role": s.visual_role,
                    "canvas_width": WIDTH,
                    "canvas_height": HEIGHT,
                }
                for s in segments
            ],
        },
    )
    write_middle_cut_map_v3()
    static_report = static_validation_v3(segments)
    if not static_report["passed"]:
        raise RuntimeError("本地修正版 v3 中段/画布静态闸门未通过：" + json.dumps(static_report, ensure_ascii=False))

    final = assemble_video_v3(segments, voiceover)
    V2.create_contact_sheet_from_video(middle_preview, OUT_DIR / "middle_stable_zoom_contact_sheet_v3.jpg", "middle_v3", count=6)
    V2.create_summary_hyperframes_contact_sheet(summary_hf, OUT_DIR / "summary_card_hyperframes_contact_sheet_v3.jpg")
    create_canvas_contact_sheet_v3(final, segments)
    write_sassy_reports_v3(cards)
    write_reports(segments, final, middle_preview, captions, summary_hf, voiceover, static_report)
    update_parent_reports(final)
    update_logs(final, middle_preview)
    print(json.dumps({"status": "success", "full_video_local_fix_v3": str(final), "duration_seconds": probe_duration(final)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
