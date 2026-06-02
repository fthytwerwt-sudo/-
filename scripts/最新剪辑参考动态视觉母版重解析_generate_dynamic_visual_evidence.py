#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import math
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import cv2
from PIL import Image, ImageDraw


ROOT = Path("/Users/fan/Documents/视频工厂")
SOURCE_DIR = ROOT / "素材录制/剪辑参考/最新剪辑参考"
LOG_DIR = ROOT / "codex_log/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse"
DIST_DIR = ROOT / "dist/reference_analysis/20260602_最新剪辑参考4条动态视觉母版重解析_latest_4_dynamic_visual_master_reparse"
PROBE_SCRIPT = Path("/Users/fan/.codex/skills/video-metadata-probe/scripts/probe_video.sh")


@dataclass
class ReferenceVideo:
    ref_id: str
    path: Path


def run_command(args: list[str], *, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=timeout,
        check=False,
    )


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise RuntimeError(f"missing required tool: {name}")
    return path


def list_reference_videos() -> list[ReferenceVideo]:
    videos = sorted(
        p
        for p in SOURCE_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in {".mp4", ".mov", ".m4v"}
    )
    if len(videos) != 4:
        raise RuntimeError(f"expected exactly 4 reference videos, found {len(videos)}")
    return [ReferenceVideo(f"reference_{idx:02d}", path) for idx, path in enumerate(videos, start=1)]


def ffprobe_json(video: Path, output_path: Path) -> dict[str, Any]:
    result = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-print_format",
            "json",
            "-show_format",
            "-show_streams",
            str(video),
        ],
        timeout=120,
    )
    output_path.write_text(result.stdout, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed for {video}: {result.stderr}")
    return json.loads(result.stdout)


def parse_stream_metadata(probe: dict[str, Any]) -> dict[str, Any]:
    video_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    audio_streams = [s for s in probe.get("streams", []) if s.get("codec_type") == "audio"]
    duration = float(probe.get("format", {}).get("duration") or video_stream.get("duration") or 0)
    fps_raw = video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate") or "0/1"
    try:
        n, d = fps_raw.split("/")
        fps = float(n) / float(d) if float(d) else 0.0
    except Exception:
        fps = 0.0
    return {
        "duration_seconds": duration,
        "width": int(video_stream.get("width") or 0),
        "height": int(video_stream.get("height") or 0),
        "fps": fps,
        "video_codec": video_stream.get("codec_name"),
        "audio_present": bool(audio_streams),
        "audio_codec": audio_streams[0].get("codec_name") if audio_streams else None,
        "audio_channels": audio_streams[0].get("channels") if audio_streams else None,
    }


def run_skill_probe(video: Path, output_path: Path) -> dict[str, Any]:
    if not PROBE_SCRIPT.exists():
        output_path.write_text("probe_video.sh missing\n", encoding="utf-8")
        return {"status": "missing_probe_script"}
    result = run_command([str(PROBE_SCRIPT), str(video)], timeout=180)
    output_path.write_text(result.stdout + ("\nSTDERR:\n" + result.stderr if result.stderr else ""), encoding="utf-8")
    return {"status": "passed" if result.returncode == 0 else "failed", "returncode": result.returncode}


def extract_ffmpeg_smoke_frame(video: Path, ref_id: str) -> dict[str, Any]:
    out_dir = DIST_DIR / "ffmpeg_smoke" / ref_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "t0001s.jpg"
    result = run_command(
        ["ffmpeg", "-y", "-v", "error", "-ss", "1", "-i", str(video), "-frames:v", "1", "-q:v", "2", str(out_path)],
        timeout=180,
    )
    return {
        "path": rel(out_path),
        "status": "passed" if result.returncode == 0 and out_path.exists() else "failed",
        "returncode": result.returncode,
        "stderr": result.stderr.strip(),
    }


def open_cv_capture(video: Path) -> tuple[cv2.VideoCapture, dict[str, Any]]:
    cap = cv2.VideoCapture(str(video))
    opened = cap.isOpened()
    metadata = {
        "opencv_opened": opened,
        "frame_count": int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0),
        "fps": float(cap.get(cv2.CAP_PROP_FPS) or 0),
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0),
    }
    if not opened:
        cap.release()
        raise RuntimeError(f"OpenCV cannot open {video}")
    return cap, metadata


def grab_frame(cap: cv2.VideoCapture, timestamp: float) -> Any | None:
    cap.set(cv2.CAP_PROP_POS_MSEC, max(timestamp, 0.0) * 1000.0)
    ok, frame = cap.read()
    return frame if ok else None


def save_frame(frame: Any, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path), frame, [int(cv2.IMWRITE_JPEG_QUALITY), 88])


def frame_metrics(frame: Any) -> dict[str, float]:
    small = cv2.resize(frame, (96, 96), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    return {
        "brightness": float(gray.mean()),
        "contrast": float(gray.std()),
        "saturation": float(hsv[:, :, 1].mean()),
        "edge_density": float(cv2.Canny(gray, 80, 160).mean() / 255.0),
    }


def visual_diff(prev_frame: Any | None, frame: Any) -> float:
    if prev_frame is None:
        return 0.0
    prev = cv2.resize(prev_frame, (96, 96), interpolation=cv2.INTER_AREA)
    current = cv2.resize(frame, (96, 96), interpolation=cv2.INTER_AREA)
    return float(cv2.absdiff(prev, current).mean())


def make_contact_sheets(frame_paths: list[Path], out_prefix: Path, *, title: str, per_page: int = 20) -> list[Path]:
    outputs: list[Path] = []
    for page_idx, page_paths in enumerate(chunks(frame_paths, per_page), start=1):
        outputs.append(make_contact_sheet(page_paths, out_prefix.with_name(f"{out_prefix.name}_page_{page_idx:02d}.jpg"), title=f"{title} p{page_idx}"))
    return outputs


def make_contact_sheet(frame_paths: list[Path], output_path: Path, *, title: str) -> Path:
    thumbs = []
    for path in frame_paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((260, 180))
        thumbs.append((path, img.copy()))
        img.close()
    cols = 4
    cell_w, cell_h = 280, 220
    rows = max(1, math.ceil(len(thumbs) / cols))
    canvas = Image.new("RGB", (cols * cell_w, rows * cell_h + 40), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text((12, 10), title, fill=(0, 0, 0))
    for idx, (path, img) in enumerate(thumbs):
        row = idx // cols
        col = idx % cols
        x = col * cell_w + 10
        y = row * cell_h + 45
        canvas.paste(img, (x, y))
        draw.text((x, y + img.height + 4), path.stem, fill=(0, 0, 0))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, quality=88)
    return output_path


def chunks(items: list[Path], size: int) -> list[list[Path]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


def select_dynamic_clip_timestamps(duration: float, scene_rows: list[dict[str, Any]]) -> list[tuple[str, float]]:
    candidates = sorted(scene_rows, key=lambda row: float(row.get("diff_from_previous", 0)), reverse=True)
    selected: list[tuple[str, float]] = [
        ("opening_first_impression", 0.0),
        ("opening_after_first_second", min(3.0, max(duration - 1.0, 0.0))),
    ]
    label_plan = [
        "first_layout_split_or_large_change",
        "subtitle_or_keyword_highlight_change",
        "evidence_window_change",
        "bridge_reset_change",
        "density_layer_change",
        "late_section_change",
    ]
    used = {0}
    for label in label_plan:
        match = None
        for row in candidates:
            ts = int(float(row["timestamp"]))
            if ts in used:
                continue
            if label == "late_section_change" and ts < duration * 0.55:
                continue
            match = float(row["timestamp"])
            used.add(ts)
            break
        if match is None:
            match = min(duration - 1.0, len(selected) * max(duration / 8.0, 1.0))
        selected.append((label, max(0.0, min(match, max(duration - 1.0, 0.0)))))
    return selected


def extract_dynamic_clip(video: Path, ref_id: str, label: str, timestamp: float) -> dict[str, Any]:
    clip_dir = DIST_DIR / ref_id / "dynamic_1s_clips"
    clip_dir.mkdir(parents=True, exist_ok=True)
    start = max(timestamp - 0.25, 0.0)
    out_path = clip_dir / f"{label}_t{int(round(timestamp)):04d}s.mp4"
    result = run_command(
        [
            "ffmpeg",
            "-y",
            "-v",
            "error",
            "-ss",
            f"{start:.3f}",
            "-i",
            str(video),
            "-t",
            "1.0",
            "-an",
            "-vf",
            "scale=540:-2",
            "-c:v",
            "libx264",
            "-preset",
            "ultrafast",
            "-crf",
            "28",
            str(out_path),
        ],
        timeout=240,
    )
    return {
        "label": label,
        "timestamp": timestamp,
        "path": rel(out_path),
        "status": "passed" if result.returncode == 0 and out_path.exists() else "failed",
        "stderr": result.stderr.strip(),
    }


def sample_reference(ref: ReferenceVideo, metadata: dict[str, Any]) -> dict[str, Any]:
    ref_dir = DIST_DIR / ref.ref_id
    frames_5s_dir = ref_dir / "frames_5s"
    scene_dir = ref_dir / "scene_candidates"
    frames_5s_dir.mkdir(parents=True, exist_ok=True)
    scene_dir.mkdir(parents=True, exist_ok=True)

    duration = float(metadata["duration_seconds"])
    cap, opencv_meta = open_cv_capture(ref.path)
    rows_5s: list[dict[str, Any]] = []
    frame_paths_5s: list[Path] = []
    timestamps_5s = list(range(0, max(int(math.floor(duration)), 0) + 1, 5))
    if duration and (not timestamps_5s or timestamps_5s[-1] < duration - 1):
        timestamps_5s.append(max(0, int(duration)))

    for ts in timestamps_5s:
        frame = grab_frame(cap, float(ts))
        if frame is None:
            continue
        out_path = frames_5s_dir / f"t{int(ts):04d}s.jpg"
        save_frame(frame, out_path)
        row = {"timestamp": ts, "frame_path": rel(out_path)}
        row.update(frame_metrics(frame))
        rows_5s.append(row)
        frame_paths_5s.append(out_path)

    metrics_path = ref_dir / "frame_metrics_5s.csv"
    write_csv(metrics_path, rows_5s)

    prev = None
    scene_rows_all: list[dict[str, Any]] = []
    max_ts = max(0, int(math.floor(duration)))
    for ts in range(0, max_ts + 1, 2):
        frame = grab_frame(cap, float(ts))
        if frame is None:
            continue
        metrics = frame_metrics(frame)
        diff = visual_diff(prev, frame)
        row = {"timestamp": ts, "diff_from_previous": diff}
        row.update(metrics)
        scene_rows_all.append(row)
        prev = frame
    cap.release()

    top_scene_rows = sorted(scene_rows_all, key=lambda row: float(row["diff_from_previous"]), reverse=True)[:26]
    first_seconds = [row for row in scene_rows_all if int(row["timestamp"]) in {0, 1, 2, 3, 5}]
    merged: dict[int, dict[str, Any]] = {}
    for row in first_seconds + top_scene_rows:
        merged[int(row["timestamp"])] = row
    scene_rows = [merged[k] for k in sorted(merged)]

    scene_paths: list[Path] = []
    cap, _ = open_cv_capture(ref.path)
    for row in scene_rows:
        ts = int(row["timestamp"])
        frame = grab_frame(cap, float(ts))
        if frame is None:
            continue
        out_path = scene_dir / f"t{ts:04d}s_scene.jpg"
        save_frame(frame, out_path)
        row["frame_path"] = rel(out_path)
        scene_paths.append(out_path)
    cap.release()

    scene_csv_path = ref_dir / "scene_change_candidates.csv"
    write_csv(scene_csv_path, scene_rows)

    contact_sheets = make_contact_sheets(
        frame_paths_5s,
        ref_dir / "contact_sheet_5s",
        title=f"{ref.ref_id} 5s frames",
        per_page=20,
    )
    scene_contact_sheet = make_contact_sheet(
        scene_paths,
        ref_dir / "contact_sheet_scene_candidates.jpg",
        title=f"{ref.ref_id} scene candidates",
    )

    clip_reports = [
        extract_dynamic_clip(ref.path, ref.ref_id, label, ts)
        for label, ts in select_dynamic_clip_timestamps(duration, scene_rows)
    ]

    return {
        "opencv": opencv_meta,
        "frames_5s_count": len(frame_paths_5s),
        "frames_5s_dir": rel(frames_5s_dir),
        "frame_metrics_5s_csv": rel(metrics_path),
        "scene_candidate_count": len(scene_rows),
        "scene_candidates_csv": rel(scene_csv_path),
        "scene_candidates_dir": rel(scene_dir),
        "contact_sheets": [rel(path) for path in contact_sheets],
        "scene_contact_sheet": rel(scene_contact_sheet),
        "dynamic_1s_clips": clip_reports,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def write_inventory_md(videos: list[ReferenceVideo], summary: dict[str, Any]) -> None:
    lines = [
        "# Reference Video Inventory",
        "",
        "status_boundary:",
        "- `task_result.status = dynamic_visual_master_parse_evidence_generated`",
        "- `content_validation = not_applicable`",
        "- `send_ready = false`",
        "- `video_rendered = false`",
        "- `new_fourth_episode_modified = false`",
        "- `formal_mechanism_updated = false`",
        "",
        "| reference_id | source_path | duration | resolution | fps | video_codec | audio_present | ffprobe | ffmpeg_smoke | opencv |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for ref in videos:
        item = summary["references"][ref.ref_id]
        meta = item["metadata"]
        lines.append(
            "| `{}` | `{}` | `{:.3f}s` | `{}x{}` | `{:.3f}` | `{}` | `{}` | `{}` | `{}` | `{}` |".format(
                ref.ref_id,
                ref.path,
                meta["duration_seconds"],
                meta["width"],
                meta["height"],
                meta["fps"],
                meta["video_codec"],
                meta["audio_present"],
                item["ffprobe_json"],
                item["ffmpeg_smoke"]["status"],
                item["sampling"]["opencv"]["opencv_opened"],
            )
        )
    lines.extend(
        [
            "",
            "## Evidence Outputs",
            "",
            "- `ffprobe_json`: `codex_log/reference_analysis/.../metadata/reference_XX_ffprobe.json`",
            "- `probe_video_report`: `codex_log/reference_analysis/.../metadata/reference_XX_video_metadata_probe.md`",
            "- `ffmpeg_smoke`: `dist/reference_analysis/.../ffmpeg_smoke/reference_XX/t0001s.jpg`",
            "- `frames_5s`: `dist/reference_analysis/.../reference_XX/frames_5s/`",
            "- `scene_candidates`: `dist/reference_analysis/.../reference_XX/scene_candidates/`",
            "- `dynamic_1s_clips`: `dist/reference_analysis/.../reference_XX/dynamic_1s_clips/`",
            "- `contact_sheets`: `dist/reference_analysis/.../reference_XX/contact_sheet_*.jpg`",
        ]
    )
    (LOG_DIR / "reference_video_inventory.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    require_tool("ffprobe")
    require_tool("ffmpeg")
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    metadata_dir = LOG_DIR / "metadata"
    metadata_dir.mkdir(parents=True, exist_ok=True)

    videos = list_reference_videos()
    summary: dict[str, Any] = {
        "analysis_id": "20260602_latest_4_dynamic_visual_master_reparse",
        "source_dir": str(SOURCE_DIR),
        "log_dir": rel(LOG_DIR),
        "dist_dir": rel(DIST_DIR),
        "reference_count": len(videos),
        "ffprobe_available": True,
        "ffmpeg_available": True,
        "opencv_version": cv2.__version__,
        "references": {},
        "status_boundary": {
            "video_rendered": False,
            "new_fourth_episode_modified": False,
            "formal_mechanism_updated": False,
            "content_validation": "not_applicable",
            "send_ready": False,
        },
    }

    for ref in videos:
        probe_path = metadata_dir / f"{ref.ref_id}_ffprobe.json"
        probe = ffprobe_json(ref.path, probe_path)
        metadata = parse_stream_metadata(probe)
        probe_report_path = metadata_dir / f"{ref.ref_id}_video_metadata_probe.md"
        skill_probe = run_skill_probe(ref.path, probe_report_path)
        ffmpeg_smoke = extract_ffmpeg_smoke_frame(ref.path, ref.ref_id)
        sampling = sample_reference(ref, metadata)
        summary["references"][ref.ref_id] = {
            "source_path": str(ref.path),
            "metadata": metadata,
            "ffprobe_json": rel(probe_path),
            "probe_video_report": rel(probe_report_path),
            "probe_video_skill_status": skill_probe,
            "ffmpeg_smoke": ffmpeg_smoke,
            "sampling": sampling,
        }

    summary_path = LOG_DIR / "media_probe_and_sampling_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_inventory_md(videos, summary)
    print(json.dumps({"status": "ok", "summary_path": rel(summary_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
