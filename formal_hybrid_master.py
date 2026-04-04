from __future__ import annotations

import copy
import json
import pathlib
import re
import shutil
import socket
import subprocess
from typing import Any

from formal_api_demo_core import (
    DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    DEFAULT_GENERAL_IMAGE_MODEL,
    DEFAULT_GENERAL_VIDEO_MODEL,
    FORMAL_EXAMPLE_CONFIG_PATH,
    ROOT,
    STATUS_SUCCESS,
    _execute_aliyun_wan_image_generation,
    _execute_aliyun_wan_video_generation,
    _video_model_requires_seed_image,
    execute_formal_voiceover_generation,
    load_formal_config,
    parse_formal_case_markdown,
    resolve_ffmpeg_binary,
    run_subprocess,
    write_json,
)


HYBRID_CASE_PATH = ROOT / "cases" / "formal_api_demo_30s_hybrid.md"
HYBRID_OUTPUT_DIR = ROOT / "dist" / "formal_api_demo_30s_hybrid"


def normalize_generation_models(config: dict[str, Any]) -> dict[str, Any]:
    normalized = copy.deepcopy(config)
    image_generation = normalized.setdefault("image_generation", {})
    video_generation = normalized.setdefault("video_generation", {})
    if not image_generation.get("model"):
        image_generation["model"] = DEFAULT_GENERAL_IMAGE_MODEL
    if not video_generation.get("model"):
        video_generation["model"] = DEFAULT_GENERAL_VIDEO_MODEL
    return normalized


def build_hybrid_routing_plan() -> dict[str, Any]:
    blocks = [
        {
            "block_id": "block_01",
            "block_goal": "抓手 / 判断 / 进入感",
            "block_need_first": "代入 + 相信",
            "block_carrier": "human",
            "asset_requirement": "真人承载视频，固定背景，半身镜头，轻手势，判断感强于表演感",
            "why_this_carrier": "开头先让观众完成“这事跟我有关，而且说话的人知道问题在哪”。",
        },
        {
            "block_id": "block_02",
            "block_goal": "结构证据 / before-after 对比",
            "block_need_first": "看懂",
            "block_carrier": "mixed",
            "asset_requirement": "结构证据视频 + 叠加信息卡，肉眼可见地把散乱状态压进 SOP 接手表",
            "why_this_carrier": "这段要证明差异，不是再复述判断，所以用证据和层次替代口头解释。",
        },
        {
            "block_id": "block_03",
            "block_goal": "收束 / 最小行动 / 掌控感",
            "block_need_first": "行动 + 相信",
            "block_carrier": "human_with_overlay",
            "asset_requirement": "真人收束视频 + 轻量 SOP 行动卡",
            "why_this_carrier": "结尾要把方法压成观众今天就能做的一步，同时保住真人判断感。",
        },
    ]
    return {
        "video_scene": "AI 项目讲解",
        "video_goal": "让观众一眼看懂 AI 项目推进卡点不在 prompt，而在没有可交接的 SOP 接手链路，并给出最小行动。",
        "primary_value": "结构",
        "audience_need_first": "两者都要",
        "video_route_strategy": "hybrid",
        "why_this_strategy": "开头和结尾需要真人承担判断、进入感和可信度，中段需要结构证据把 before/after 做成肉眼可见。",
        "blocks": blocks,
        "fallback_rules": [
            "若真人视频生成失败，本轮不得降级成纯 PPT 完成态，应直接报真人链路阻断。",
            "若结构证据段不清楚，优先重做证据段而不是改回整条真人口播。",
        ],
        "review_diagnosis": {
            "should_be_hybrid": True,
            "human_carries_judgement": True,
            "evidence_carries_structure": True,
        },
    }


def build_slide_specs(
    *,
    video_spec: dict[str, Any],
    asset_map: dict[str, dict[str, str | None]],
) -> list[dict[str, Any]]:
    slides: list[dict[str, Any]] = []
    total = len(video_spec["segments"])

    for index, segment in enumerate(video_spec["segments"], start=1):
        segment_id = segment["segment_id"]
        asset = asset_map.get(segment_id, {})
        video_path = asset.get("video")
        image_path = asset.get("image")
        base = {
            "sequence": index,
            "total": total,
            "segment_id": segment_id,
            "headline": segment["caption_text"],
            "duration": segment["timeline"]["planned_duration_seconds"],
            "background_video_path": video_path,
            "background_image_path": image_path if not video_path else None,
        }

        if segment_id == "seg01":
            slides.append(
                {
                    **base,
                    "role": "hook",
                    "eyebrow": "问题判断",
                    "support": "真正卡住的，往往不是 prompt。",
                    "detail": "不是没想法，是没有一条别人能接住的 SOP 链路。",
                    "chips": ["不是 prompt", "是接手链路"],
                    "accent": "#2563EB",
                    "background": "#F5F7FB",
                }
            )
            continue

        if segment_id == "seg02":
            slides.append(
                {
                    **base,
                    "role": "process",
                    "eyebrow": "结构证据",
                    "support": "把五件事压进一张表，后面才接得住。",
                    "detail": "Before 是每次重讲；After 是目标、输入输出、口径素材已经能交接。",
                    "chips": ["目标", "输入输出", "口径素材"],
                    "accent": "#0F766E",
                    "background": "#F1FAF8",
                }
            )
            continue

        slides.append(
            {
                **base,
                "role": "outcome",
                "eyebrow": "最小行动",
                "support": "先压一张表，再谈工具和自动化。",
                "detail": "先把目标、输入、输出、口径写清，AI 和人后面才真的接得住。",
                "chips": ["先压成表", "再接给 AI"],
                "accent": "#C2410C",
                "background": "#FFF7ED",
            }
        )

    return slides


def build_visual_prompts() -> dict[str, str]:
    return {
        "seg01": (
            "9:16 竖版，30岁左右东亚女性创作者面对镜头在安静工作室里做短视频口播，"
            "半身构图，目光看镜头，轻微手势，语气克制但有判断感，真实肤质，真实摄影质感，"
            "固定背景，不要字幕，不要大字，不要夸张表演，不要广告感。"
        ),
        "seg02": (
            "9:16 竖版，单一固定镜头的项目工作台。前半段目标、输入、输出、口径、素材五类便签"
            "散乱堆叠，箭头断裂，明显没人接得住；后半段这些便签被吸附、整理、归位，进入同一张"
            "清晰的 SOP 接手表，字段标题明确，最后出现“下一步谁接 / 交什么”的可交接状态。"
            "真实案例质感，不要分屏，不要人物，不要广告感，不要大段字幕。"
        ),
        "seg03": (
            "9:16 竖版，同一位东亚女性创作者回到镜头前收束判断，半身构图，目光稳定，"
            "有轻微点头和收束手势，固定背景，真实摄影质感，像在给团队下一步指令。"
            "不要字幕，不要大字，不要夸张表演，不要广告感。"
        ),
    }


def audio_duration_seconds(path: pathlib.Path) -> float:
    if shutil.which("afinfo"):
        output = subprocess.run(
            ["afinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        match = re.search(r"estimated duration:\s*([0-9.]+)\s*sec", output)
        if match:
            return float(match.group(1))

    ffmpeg_binary = resolve_ffmpeg_binary()
    result = subprocess.run(
        [ffmpeg_binary, "-i", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stderr or "") + (result.stdout or "")
    match = re.search(r"Duration:\s*(\d+):(\d+):(\d+\.\d+)", output)
    if not match:
        raise RuntimeError(f"无法解析音频时长：{path}")
    hours = int(match.group(1))
    minutes = int(match.group(2))
    seconds = float(match.group(3))
    return hours * 3600 + minutes * 60 + seconds


def split_caption_chunks(text: str) -> list[str]:
    chunks = [item.strip() for item in re.split(r"(?<=[。！？；])", text) if item.strip()]
    normalized: list[str] = []
    for chunk in chunks:
        if len(chunk) <= 20 or "，" not in chunk:
            normalized.append(chunk)
            continue
        comma_parts = [part.strip() for part in re.split(r"(?<=，)", chunk) if part.strip()]
        if len(comma_parts) >= 2:
            midpoint = max(1, len(comma_parts) // 2)
            normalized.append("".join(comma_parts[:midpoint]).strip())
            normalized.append("".join(comma_parts[midpoint:]).strip())
        else:
            normalized.append(chunk)
    return normalized or [text]


def format_srt_timestamp(seconds: float) -> str:
    milliseconds = max(0, int(round(seconds * 1000)))
    hours, remainder = divmod(milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def write_runtime_script_and_captions(
    *,
    video_spec: dict[str, Any],
    output_dir: pathlib.Path,
    duration_map: dict[str, float],
) -> dict[str, Any]:
    script_path = output_dir / "script.txt"
    captions_path = output_dir / "captions.srt"
    timeline_path = output_dir / "timeline.json"

    script_lines: list[str] = []
    caption_rows: list[str] = []
    timeline_entries: list[dict[str, Any]] = []
    cursor = 0.0
    caption_index = 1

    for segment in video_spec["segments"]:
        segment_id = segment["segment_id"]
        duration = round(duration_map.get(segment_id, segment["planned_duration_seconds"]), 3)
        segment["timeline"] = {
            "planned_start_seconds": round(cursor, 3),
            "planned_end_seconds": round(cursor + duration, 3),
            "planned_duration_seconds": duration,
        }
        timeline_entries.append(
            {
                "segment_id": segment_id,
                "start_seconds": round(cursor, 3),
                "end_seconds": round(cursor + duration, 3),
                "duration_seconds": duration,
                "caption_text": segment["caption_text"],
            }
        )
        script_lines.append(f"{segment_id}: {segment['voiceover_text']}")

        chunks = split_caption_chunks(segment["caption_text"])
        visible_chars = [max(1, len(chunk.replace(" ", ""))) for chunk in chunks]
        total_chars = sum(visible_chars)
        chunk_cursor = cursor
        for idx, chunk in enumerate(chunks):
            if idx == len(chunks) - 1:
                chunk_end = cursor + duration
            else:
                chunk_share = duration * visible_chars[idx] / total_chars
                chunk_end = chunk_cursor + chunk_share
            caption_rows.extend(
                [
                    str(caption_index),
                    f"{format_srt_timestamp(chunk_cursor)} --> {format_srt_timestamp(chunk_end)}",
                    chunk,
                    "",
                ]
            )
            caption_index += 1
            chunk_cursor = chunk_end

        cursor += duration

    script_path.write_text("\n".join(script_lines).strip() + "\n", encoding="utf-8")
    captions_path.write_text("\n".join(caption_rows).strip() + "\n", encoding="utf-8")
    write_json(timeline_path, {"segments": timeline_entries})
    return {
        "script_path": str(script_path),
        "captions_path": str(captions_path),
        "timeline_path": str(timeline_path),
        "total_duration_seconds": round(cursor, 3),
    }


def generate_visual_assets(
    *,
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, dict[str, str | None]]:
    prompts = build_visual_prompts()
    asset_map: dict[str, dict[str, str | None]] = {}
    visual_plan = {
        "schema_version": "formal_hybrid_visual_plan/v1",
        "segments": [],
    }
    video_model = (
        config.get("video_generation", {}).get("model") or DEFAULT_GENERAL_VIDEO_MODEL
    )
    video_requires_seed_image = _video_model_requires_seed_image(video_model)

    for segment in video_spec["segments"]:
        segment_id = segment["segment_id"]
        existing_image = output_dir / "visual" / f"{segment_id}_image.png"
        existing_video = output_dir / "visual" / f"{segment_id}_video.mp4"
        if existing_video.exists():
            asset_map[segment_id] = {
                "video": str(existing_video),
                "image": str(existing_image) if existing_image.exists() else None,
            }
            visual_plan["segments"].append(
                {
                    "segment_id": segment_id,
                    "prompt": prompts.get(segment_id, ""),
                    "task_id": None,
                    "request_id": None,
                    "asset_path": str(existing_video),
                    "reused_existing_asset": True,
                }
            )
            continue

        seed_image_url: str | None = None
        image_asset_path: str | None = None
        if video_requires_seed_image:
            if existing_image.exists():
                image_asset_path = str(existing_image)
                seed_image_url = existing_image.resolve().as_uri()
            else:
                image_result = _execute_aliyun_wan_image_generation(
                    config=config,
                    output_dir=output_dir,
                    segment_id=segment_id,
                    prompt=prompts[segment_id],
                )
                if image_result.get("status") != STATUS_SUCCESS:
                    raise RuntimeError(f"{segment_id} 首帧图片生成失败：{image_result}")
                image_asset_path = image_result["asset_path"]
                seed_image_url = image_result.get("source_url")
                if not seed_image_url and image_asset_path:
                    seed_image_url = pathlib.Path(image_asset_path).resolve().as_uri()

        last_error: Exception | None = None
        result: dict[str, Any] | None = None
        for _attempt in range(3):
            try:
                result = _execute_aliyun_wan_video_generation(
                    config=config,
                    output_dir=output_dir,
                    segment_id=segment_id,
                    prompt=prompts[segment_id],
                    duration_seconds=segment["timeline"]["planned_duration_seconds"],
                    seed_image_url=seed_image_url,
                )
                if result.get("status") == STATUS_SUCCESS:
                    break
                if result.get("failure_reason") not in {
                    "aliyun_video_task_poll_failed",
                    "aliyun_video_download_failed",
                }:
                    break
            except socket.timeout as exc:
                last_error = exc

        if result is None and last_error is not None:
            raise RuntimeError(f"{segment_id} 视频生成轮询超时：{last_error}") from last_error
        if result is None or result["status"] != STATUS_SUCCESS:
            raise RuntimeError(f"{segment_id} 视频生成失败：{result}")
        asset_map[segment_id] = {
            "video": result["asset_path"],
            "image": image_asset_path,
        }
        visual_plan["segments"].append(
            {
                "segment_id": segment_id,
                "prompt": prompts[segment_id],
                "task_id": result["task_id"],
                "request_id": result["request_id"],
                "asset_path": result["asset_path"],
                "seed_image_path": image_asset_path,
                "seed_image_url": seed_image_url,
            }
        )

    write_json(output_dir / "visual_generation_plan.json", visual_plan)
    return asset_map


def load_or_generate_voiceover(
    *,
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    tts_dir = output_dir / "tts"
    bundle_path = tts_dir / "formal_voiceover.mp3"
    segment_audio_paths = [
        tts_dir / f"segment_{segment['segment_id']}.mp3"
        for segment in video_spec["segments"]
    ]
    if bundle_path.exists() and all(path.exists() for path in segment_audio_paths):
        return {
            "status": STATUS_SUCCESS,
            "audio_path": str(bundle_path),
            "segment_audio_paths": [str(path) for path in segment_audio_paths],
            "segment_results": [
                {
                    "segment_id": segment["segment_id"],
                    "status": STATUS_SUCCESS,
                    "audio_path": str(tts_dir / f"segment_{segment['segment_id']}.mp3"),
                    "request_id": None,
                    "failure_reason": "",
                    "error_message": "",
                }
                for segment in video_spec["segments"]
            ],
        }

    return execute_formal_voiceover_generation(
        video_spec=video_spec,
        config=config,
        output_dir=output_dir,
    )


def write_review_record(
    *,
    output_dir: pathlib.Path,
    route_plan: dict[str, Any],
    final_video_path: pathlib.Path,
) -> pathlib.Path:
    review_path = output_dir / "review_record.md"
    lines = [
        "# 视频回审记录",
        "",
        "- `review_id`: formal_api_demo_30s_hybrid",
        "- `date`: 2026-04-04",
        "- `video_title`: 为什么很多 AI 项目不是没想法，而是没有可交接的 SOP 接手链路",
        "- `stage`: formal_master_local_review",
        f"- `sample_path`: {final_video_path}",
        "- `local_only`: true",
        "",
        "## 本条视频主路由策略",
        f"- `video_scene`: {route_plan['video_scene']}",
        f"- `video_goal`: {route_plan['video_goal']}",
        f"- `primary_value`: {route_plan['primary_value']}",
        f"- `audience_need_first`: {route_plan['audience_need_first']}",
        f"- `video_route_strategy`: {route_plan['video_route_strategy']}",
        f"- `why_this_strategy`: {route_plan['why_this_strategy']}",
        "",
        "## 本条 block 路由表",
        "",
        "| block_id | block_goal | block_need_first | block_carrier | asset_requirement | why_this_carrier |",
        "|---|---|---|---|---|---|",
    ]
    for block in route_plan["blocks"]:
        lines.append(
            f"| {block['block_id']} | {block['block_goal']} | {block['block_need_first']} | "
            f"{block['block_carrier']} | {block['asset_requirement']} | {block['why_this_carrier']} |"
        )
    lines.extend(
        [
            "",
            "## 当前问题归因",
            "",
            "- `main_problem_layer`: 当前以质量基线自审为主，未见展示路由错位。",
            "- `is_presentation_route_wrong`: false",
            "- `content_issue_or_route_issue`: 当前主问题不再是 route 选择，而是质量确认。",
            "- `should_be_ppt_but_used_human`: false",
            "- `should_be_human_but_used_ppt`: false",
            "- `should_be_hybrid_but_forced_single_route`: false",
            "- `highest_priority_fix`: 若复审不过线，优先修开头真人段和 seg02 证据段的衔接。",
            "",
            "## 回退与下一轮动作",
            "",
            "- `fallback_needed`: false",
            "- `fallback_target`: 保持 hybrid",
            "- `fallback_reason`: 当前主路由与 block 职责一致。",
            "- `next_round_keep_or_switch_route`: keep_route",
            "- `next_round_only_change_this_one_thing`: 若要再提质，只动最弱的一段素材，不同时改结构。",
        ]
    )
    review_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return review_path


def export_review_frames(
    *,
    video_path: pathlib.Path,
    output_dir: pathlib.Path,
    duration_map: dict[str, float],
) -> pathlib.Path:
    review_dir = output_dir / "review_frames"
    review_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg_binary = resolve_ffmpeg_binary()

    seg01 = duration_map["seg01"]
    seg02 = duration_map["seg02"]
    total = sum(duration_map.values())
    captures = [
        ("final_01_hook.png", min(1.4, max(0.4, seg01 / 3))),
        ("final_02_seg02_before.png", seg01 + min(1.2, max(0.6, seg02 / 4))),
        ("final_03_seg02_after.png", seg01 + max(seg02 - 1.6, seg02 / 2)),
        ("final_04_outcome.png", max(total - 1.2, seg01 + seg02 + 0.6)),
    ]

    for filename, second in captures:
        run_subprocess(
            [
                ffmpeg_binary,
                "-y",
                "-ss",
                f"{second:.3f}",
                "-i",
                str(video_path),
                "-frames:v",
                "1",
                "-update",
                "1",
                str(review_dir / filename),
            ]
        )

    return review_dir


def assemble_preview_video(
    *,
    preview_manifest_path: pathlib.Path,
    preview_video_path: pathlib.Path,
    voiceover_path: pathlib.Path,
) -> None:
    video_only_path = preview_video_path.parent / "video_only.mp4"
    result = subprocess.run(
        [
            "swift",
            str(ROOT / "video_builder.swift"),
            str(preview_manifest_path),
        ],
        check=False,
    )
    if preview_video_path.exists():
        return
    if not video_only_path.exists():
        raise RuntimeError(f"本地渲染失败，且未生成 video_only：returncode={result.returncode}")

    ffmpeg_binary = resolve_ffmpeg_binary()
    run_subprocess(
        [
            ffmpeg_binary,
            "-y",
            "-i",
            str(video_only_path),
            "-i",
            str(voiceover_path),
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-shortest",
            str(preview_video_path),
        ]
    )


def render_formal_hybrid_master(
    *,
    input_path: pathlib.Path = HYBRID_CASE_PATH,
    example_config_path: pathlib.Path = FORMAL_EXAMPLE_CONFIG_PATH,
    local_config_path: pathlib.Path = DEFAULT_FORMAL_LOCAL_CONFIG_PATH,
    output_dir: pathlib.Path = HYBRID_OUTPUT_DIR,
) -> dict[str, Any]:
    video_spec = parse_formal_case_markdown(input_path)
    config_bundle = load_formal_config(example_config_path, local_config_path)
    config = normalize_generation_models(config_bundle["config"])
    output_dir.mkdir(parents=True, exist_ok=True)

    route_plan = build_hybrid_routing_plan()
    write_json(output_dir / "route_plan.json", route_plan)

    voiceover = load_or_generate_voiceover(
        video_spec=video_spec,
        config=config,
        output_dir=output_dir,
    )
    if voiceover["status"] != STATUS_SUCCESS:
        raise RuntimeError(f"配音链路失败：{json.dumps(voiceover, ensure_ascii=False)}")

    duration_map = {
        result["segment_id"]: round(audio_duration_seconds(pathlib.Path(result["audio_path"])), 3)
        for result in voiceover["segment_results"]
        if result.get("audio_path")
    }
    assets_meta = write_runtime_script_and_captions(
        video_spec=video_spec,
        output_dir=output_dir,
        duration_map=duration_map,
    )

    asset_map = generate_visual_assets(
        video_spec=video_spec,
        config=config,
        output_dir=output_dir,
    )

    slides = build_slide_specs(video_spec=video_spec, asset_map=asset_map)
    preview_dir = output_dir / "assembly"
    preview_dir.mkdir(parents=True, exist_ok=True)
    preview_manifest_path = preview_dir / "preview_manifest.json"
    preview_video_path = preview_dir / "formal_api_demo_preview.mp4"
    final_video_path = output_dir / "final.mp4"
    preview_manifest = {
        "width": 1080,
        "height": 1920,
        "fps": 25,
        "audioPath": voiceover["audio_path"],
        "outputPath": str(preview_video_path.resolve()),
        "slides": slides,
    }
    write_json(preview_manifest_path, preview_manifest)

    assemble_preview_video(
        preview_manifest_path=preview_manifest_path,
        preview_video_path=preview_video_path,
        voiceover_path=pathlib.Path(voiceover["audio_path"]),
    )
    shutil.copyfile(preview_video_path, final_video_path)
    review_frames_dir = export_review_frames(
        video_path=final_video_path,
        output_dir=output_dir,
        duration_map=duration_map,
    )
    review_record_path = write_review_record(
        output_dir=output_dir,
        route_plan=route_plan,
        final_video_path=final_video_path,
    )

    result = {
        "status": STATUS_SUCCESS,
        "case_path": str(input_path),
        "route_plan_path": str(output_dir / "route_plan.json"),
        "script_path": assets_meta["script_path"],
        "captions_path": assets_meta["captions_path"],
        "timeline_path": assets_meta["timeline_path"],
        "voiceover_path": voiceover["audio_path"],
        "segment_audio_paths": voiceover["segment_audio_paths"],
        "preview_manifest_path": str(preview_manifest_path),
        "preview_video_path": str(preview_video_path),
        "final_video_path": str(final_video_path),
        "review_frames_path": str(review_frames_dir),
        "review_record_path": str(review_record_path),
        "total_duration_seconds": assets_meta["total_duration_seconds"],
        "duration_map": duration_map,
        "asset_map": asset_map,
        "route_plan": route_plan,
    }
    write_json(output_dir / "result_summary.json", result)
    return result
