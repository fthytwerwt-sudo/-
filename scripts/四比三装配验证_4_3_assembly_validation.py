from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "dist" / "20260514_4_3_aspect_ratio_assembly_fix"
TARGET_WIDTH = 1440
TARGET_HEIGHT = 1080
TARGET_RATIO = 4 / 3
RATIO_TOLERANCE = 0.01


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def probe_video(path: pathlib.Path) -> dict[str, Any]:
    payload = run(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "v:0",
            "-show_entries",
            "stream=width,height,r_frame_rate,duration",
            "-of",
            "json",
            str(path),
        ]
    )
    data = json.loads(payload.stdout)
    streams = data.get("streams") or []
    if not streams:
        raise RuntimeError(f"blocked_unreadable_video_stream: {path}")
    stream = streams[0]
    width = int(stream["width"])
    height = int(stream["height"])
    ratio = width / height
    return {
        "path": str(path),
        "width": width,
        "height": height,
        "ratio": ratio,
        "duration": float(stream.get("duration") or 0),
        "r_frame_rate": stream.get("r_frame_rate"),
        "is_4_3": abs(ratio - TARGET_RATIO) <= RATIO_TOLERANCE,
    }


def render_4_3(source: pathlib.Path, output_path: pathlib.Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    video_filter = (
        f"scale={TARGET_WIDTH}:{TARGET_HEIGHT}:force_original_aspect_ratio=decrease,"
        f"pad={TARGET_WIDTH}:{TARGET_HEIGHT}:(ow-iw)/2:(oh-ih)/2,"
        "setsar=1,format=yuv420p"
    )
    subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(source),
            "-map",
            "0:v:0",
            "-map",
            "0:a?",
            "-vf",
            video_filter,
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(output_path),
        ],
        check=True,
    )


def build_route_card(source_probe: dict[str, Any], output_probe: dict[str, Any], output_path: pathlib.Path) -> dict[str, Any]:
    return {
        "content_route_card_v2": {
            "meta": {
                "target_aspect_ratio": "4:3",
                "source_material_aspect_ratio": {
                    "width": source_probe["width"],
                    "height": source_probe["height"],
                    "ratio": round(source_probe["ratio"], 6),
                    "is_4_3": source_probe["is_4_3"],
                },
                "current_target": "4:3 technical assembly fix for current rework; latest_review_pack not overwritten",
                "technical_validation": "passed_for_4_3_assembly",
                "content_validation": "not_evaluated",
                "send_ready": False,
            },
            "opening_route_decision": {
                "selected_opening_route": "screen_first_opening",
                "route_reason": "本轮只做 4:3 技术装配验证，使用 4:3 用户录制素材先行，不因比例变化强制元素娃娃或梗图 GIF 开头。",
                "aspect_ratio_adjustment_note": "4:3 画布保留源素材完整信息；不开启 9:16 竖屏模板。",
            },
            "evidence_plan": {
                "core_evidence": "FocuSee 4:3 用户录制素材",
                "evidence_type": ["user_recording"],
                "evidence_window": "技术验证版保持素材连续，不插卡打断证据窗口；最终文案时间码仍待内容执行轮判断。",
            },
            "middle_carrier_decision": {
                "middle_carrier": "用户录制素材",
                "source_material_ratio": "4:3",
                "focusee_middle_editing_decision": {
                    "recording_layer_motion_baked_in": True,
                    "selected_editing_policy": "direct_cut_by_script_keep_original_motion",
                    "no_secondary_zoom_by_default": True,
                    "blocked_if_key_evidence_unclear": True,
                },
                "segment_split_plan": "本轮技术验证使用单段连续素材；真实内容执行时再按最终文案切时间码。",
                "trim_policy": "trim_dead_time_only_after_script_timecodes_are_known",
            },
            "card_placement_decision": {
                "card_plan": [
                    {
                        "card_type": "no_card_needed",
                        "selected_position": "not_applicable_for_technical_probe",
                        "position_reason": "本轮验证画布和素材比例，不强行插总结卡、反转卡、结果差卡或 Prompt 尾卡。",
                        "interrupt_risk": "none_in_output",
                        "safe_area_note": "若后续插卡，4:3 安全区建议保留左右 96px、上下 72px，避开主体证据与字幕底部区。",
                    }
                ],
                "summary_card_usage": "not_used_in_technical_probe",
                "reversal_card_usage": "not_used_in_technical_probe",
                "result_diff_card_usage": "not_used_in_technical_probe",
                "prompt_tail_card_usage": "not_used_in_technical_probe",
            },
            "subtitle_safe_area": {
                "caption_position": "bottom_center_inside_4_3_safe_area",
                "max_lines": 2,
                "avoid_covering_evidence": True,
                "safe_area_note": "1440x1080 输出下，字幕建议限制在 y=876-1008 区间，保留底部 72px 和主体证据区。",
            },
            "api_human_usage": {
                "usage_count": 0,
                "usage_role": "not_used_in_technical_probe",
                "aspect_ratio_note": "若后续使用 API 生成人物，需按 4:3 重新布局，不套 9:16 人物位置。",
            },
            "ppt_usage": {
                "usage_type": "not_used_in_technical_probe",
                "density_line": "少量 PPT 仅在文案需要时使用，不替代中段录屏证据。",
                "aspect_ratio_note": "PPT / 卡片后续必须按 4:3 安全区重排。",
            },
            "blocked_if": [
                "material_not_4_3",
                "evidence_window_unclear",
                "subtitles_cover_key_area",
                "cards_cover_key_area",
            ],
            "output_validation": {
                "output_path": str(output_path),
                "output_width": output_probe["width"],
                "output_height": output_probe["height"],
                "output_ratio": round(output_probe["ratio"], 6),
                "is_4_3": output_probe["is_4_3"],
            },
        }
    }


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and render a 4:3 local technical assembly.")
    parser.add_argument("--source", required=True, type=pathlib.Path)
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, type=pathlib.Path)
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    if not source.exists() or not source.is_file():
        raise RuntimeError(f"blocked_source_material_missing: {source}")

    source_probe = probe_video(source)
    if not source_probe["is_4_3"]:
        raise RuntimeError(
            "blocked_material_not_4_3: "
            f"{source} width={source_probe['width']} height={source_probe['height']} ratio={source_probe['ratio']:.6f}"
        )

    output_dir = args.output_dir.resolve()
    output_path = output_dir / "4_3_assembly_validation_preview.mp4"
    render_4_3(source, output_path)
    output_probe = probe_video(output_path)
    if not output_probe["is_4_3"] or output_probe["width"] != TARGET_WIDTH or output_probe["height"] != TARGET_HEIGHT:
        raise RuntimeError(
            "blocked_output_not_4_3: "
            f"{output_path} width={output_probe['width']} height={output_probe['height']} ratio={output_probe['ratio']:.6f}"
        )

    route_card = build_route_card(source_probe, output_probe, output_path)
    summary = {
        "technical_validation": "passed_for_4_3_assembly",
        "content_validation": "not_evaluated",
        "send_ready": False,
        "source_material_probe": source_probe,
        "output_validation": route_card["content_route_card_v2"]["output_validation"],
        "subtitle_and_card_safe_area_check": {
            "subtitle_safe_area": route_card["content_route_card_v2"]["subtitle_safe_area"],
            "card_placement_decision": route_card["content_route_card_v2"]["card_placement_decision"],
            "result": "passed_for_technical_probe_no_subtitles_or_cards_inserted",
        },
        "forbidden_status_check": {
            "content_validation_promoted": False,
            "send_ready_promoted": False,
            "publish_status_changed": False,
            "voice_validation_changed": False,
            "final_voice_validated_changed": False,
            "visual_master_locked_changed": False,
            "raw_source_modified": False,
        },
    }
    write_json(output_dir / "content_route_card_v2.json", route_card)
    write_json(output_dir / "assembly_summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
