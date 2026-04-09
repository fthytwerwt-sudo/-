from __future__ import annotations

import base64
import copy
import hashlib
import hmac
import json
import mimetypes
import os
import pathlib
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any

try:
    import openai
    from openai import OpenAI
except ImportError:  # pragma: no cover - exercised only when dependency is absent.
    openai = None
    OpenAI = None

from formal_api_demo_cloud_assembly import (
    execute_cloud_only_assembly as _execute_cloud_only_assembly,
)


ROOT = pathlib.Path(__file__).resolve().parent
FORMAL_CASE_PATH = ROOT / "cases" / "formal_api_demo.md"
FORMAL_MAINLINE_CASE_PATH = ROOT / "cases" / "formal_api_demo_human_self_footage.md"
FORMAL_EXAMPLE_CONFIG_PATH = ROOT / "config" / "formal_api_demo.example.toml"
OFFICIAL_FORMAL_LOCAL_CONFIG_PATH = (
    pathlib.Path.home() / ".config" / "video-factory" / "formal_api_demo.local.toml"
)
LEGACY_REPO_FORMAL_LOCAL_CONFIG_PATH = ROOT / "config" / "formal_api_demo.local.toml"
DEFAULT_FORMAL_OUTPUT_DIR = ROOT / "dist" / "formal_api_demo"

MANIFEST_SCHEMA_VERSION = "formal_api_demo_manifest/v1"
RESULT_SUMMARY_SCHEMA_VERSION = "formal_api_demo_result_summary/v1"
ALIYUN_ICE_API_VERSION = "2020-11-09"
ALIYUN_ICE_ENDPOINT_TEMPLATE = "https://ice.{region}.aliyuncs.com/"
ALIYUN_OSS_SIGNATURE_ALGORITHM = "OSS4-HMAC-SHA256"
ALIYUN_OSS_V4_REQUEST = "aliyun_v4_request"
DEFAULT_CLOUD_ASSEMBLY_PRESIGN_EXPIRES_SECONDS = 3600

STATUS_NOT_STARTED = "not_started"
STATUS_PLANNED = "planned"
STATUS_BLOCKED = "blocked"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"
STATUS_SKIPPED = "skipped"

PLACEHOLDER_PREFIX = "SET_"
PROVIDER_VOLCENGINE = "volcengine"
PROVIDER_ALIYUN_BAILIAN = "aliyun_bailian"
TTS_ROUTE_FAMILY_ARK = "ark_openai_compatible"
TTS_ROUTE_FAMILY_EDGE_GATEWAY = "edge_gateway_openai_compatible"
TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH = "doubao_openspeech_v3"
TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE = "aliyun_bailian_cosyvoice"
SUPPORTED_TTS_ROUTE_FAMILIES = {
    TTS_ROUTE_FAMILY_ARK,
    TTS_ROUTE_FAMILY_EDGE_GATEWAY,
    TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH,
    TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE,
}
DEFAULT_GENERAL_IMAGE_MODEL = "wan2.6-image"
DEFAULT_GENERAL_VIDEO_MODEL = "wan2.7-i2v"
DEFAULT_IMAGE_EDIT_MODEL = "qwen-image-edit-plus"
DEFAULT_VIDEO_EDIT_MODEL = "wan2.7-videoedit"
DEFAULT_PORTRAIT_DETECT_MODEL = "liveportrait-detect"
DEFAULT_PORTRAIT_VIDEO_MODEL = "liveportrait"
DEFAULT_PPT_ROUTE_PROFILE = "pure_ppt_cloud_only_secondary"
DEFAULT_MAINLINE_ROUTE_PROFILE = "api_human_local_footage_light_ppt_cloud_editing"
CARRIER_API_VISUAL = "api_visual"
CARRIER_HUMAN = "human"
CARRIER_SELF_FOOTAGE = "self_footage"
CARRIER_LIGHT_PPT = "light_ppt"
LOCAL_VIDEO_CARRIERS = {
    CARRIER_SELF_FOOTAGE,
}
USER_MEDIA_SOURCE = "user_media"
API_GENERATED_SOURCE = "api_generated"
FOOTAGE_ROLE_HUMAN_ON_CAMERA = "human_on_camera"
RESOURCE_KIND_TTS = "tts"
RESOURCE_KIND_IMAGE = "image_generation"
RESOURCE_KIND_VIDEO = "video_generation"
FAILURE_CATEGORY_AUTH = "auth_failed"
FAILURE_CATEGORY_QUOTA = "quota_exhausted"
FAILURE_CATEGORY_VOICE = "voice_unavailable"
FAILURE_CATEGORY_TIMEOUT = "provider_timeout"
FAILURE_CATEGORY_CANDIDATE = "candidate_invalid"
FAILURE_CATEGORY_UNKNOWN = "unknown"
DEFAULT_ALIYUN_TTS_STYLE_PROBE_TEXT = (
    "这套方案表面上堆满了参数，真正决定上限的其实只有供电、火控和协同链路。"
    "前两项还能补，第三项一旦掉队，再新的壳子也只是好看。"
    "说得更直白一点，它不是没亮点，是关键战力根本没站住。"
)


def _resolve_default_formal_local_config_path() -> pathlib.Path:
    env_override = os.environ.get("FORMAL_API_DEMO_LOCAL_CONFIG")
    if env_override:
        return pathlib.Path(env_override).expanduser()
    if OFFICIAL_FORMAL_LOCAL_CONFIG_PATH.exists():
        return OFFICIAL_FORMAL_LOCAL_CONFIG_PATH
    return LEGACY_REPO_FORMAL_LOCAL_CONFIG_PATH


DEFAULT_FORMAL_LOCAL_CONFIG_PATH = _resolve_default_formal_local_config_path()
DEFAULT_ALIYUN_TTS_STYLE_VARIANTS = (
    {
        "variant_id": "A",
        "label": "稳定版",
        "intent": "冷静利落，优先保住稳定判断感。",
        "instruction": "你说话的情感是neutral。",
        "speech_rate": 1.18,
        "pitch_rate": 0.92,
        "volume": 46,
        "recommended": True,
    },
    {
        "variant_id": "B",
        "label": "判断感更强版",
        "intent": "保留克制底色，同时把锋利感再往前推一点。",
        "instruction": "你说话的情感是disgusted。",
        "speech_rate": 1.24,
        "pitch_rate": 0.9,
        "volume": 48,
        "recommended": False,
    },
    {
        "variant_id": "C",
        "label": "更克制版",
        "intent": "进一步压低情绪起伏，保住冷静和收束。",
        "instruction": "你说话的情感是neutral。",
        "speech_rate": 1.08,
        "pitch_rate": 0.9,
        "volume": 44,
        "recommended": False,
    },
)
DEFAULT_FORMAL_TTS_BASELINE_PROFILE = "aliyun_old_A"
DEFAULT_FORMAL_TTS_BASELINE = {
    "profile_id": DEFAULT_FORMAL_TTS_BASELINE_PROFILE,
    "source_variant": "tts_style_probe_variant_A",
    "label": "旧 A 可用基线",
    "instruction": "你说话的情感是neutral。",
    "speech_rate": 1.18,
    "pitch_rate": 0.92,
    "volume": 46,
    "note": "当前正式链路继续沿用旧 A 作为默认可用配音基线，不再继续扩声音实验分支。",
}
DEFAULT_ALIYUN_TTS_STYLE_ROUND2_VARIANTS = (
    {
        "variant_id": "A1",
        "label": "更稳、更冷静",
        "intent": "在旧 A 的方向上进一步压住情绪起伏，让句尾更稳、更冷。",
        "instruction": "你说话的角色是军事装备分析员，你说话的情感是neutral。",
        "speech_rate": 1.14,
        "pitch_rate": 0.9,
        "volume": 45,
        "recommended": False,
        "why_recommended": "",
    },
    {
        "variant_id": "A2",
        "label": "更干、更利落",
        "intent": "保住旧 A 的冷静基础，把声线再压干一点，句尾更短更利落。",
        "instruction": "你说话的角色是军事装备拆解解说员，你说话的情感是neutral。",
        "speech_rate": 1.22,
        "pitch_rate": 0.9,
        "volume": 45,
        "recommended": True,
        "why_recommended": (
            "基于用户反馈“旧 A 更对，但还不完全对”，A2 保留旧 A 的冷静底座，"
            "同时把句尾压得更短、更干、更利落，偏移最小，最适合作为 round2 首推候选。"
        ),
    },
    {
        "variant_id": "A3",
        "label": "判断感更强一点",
        "intent": "在克制前提下把判断感略往前推一点，但不演讲、不煽动。",
        "instruction": "你说话的角色是军事鉴定解说员，你说话的情感是disgusted。",
        "speech_rate": 1.19,
        "pitch_rate": 0.91,
        "volume": 46,
        "recommended": False,
        "why_recommended": "",
    },
    {
        "variant_id": "A4",
        "label": "进一步去掉客服感/播音感",
        "intent": "进一步清掉客服播报感和新闻播音感，保持专业判断型口气。",
        "instruction": "你说话的场景是内部评估解说，你说话的情感是neutral。",
        "speech_rate": 1.16,
        "pitch_rate": 0.89,
        "volume": 44,
        "recommended": False,
        "why_recommended": "",
    },
)
DEFAULT_ALIYUN_TTS_STYLE_ROUND1_RECOMMENDATION = {
    "variant_id": "A",
    "reason": "第一轮只用于确认风格桥接与基础方向，A 保留为最稳基线，供后续继续收窄。",
}
DEFAULT_ALIYUN_TTS_STYLE_ROUND2_RECOMMENDATION = {
    "variant_id": "A2",
    "reason": "基于用户反馈“旧 A 更对，但还不完全对”，A2 保留旧 A 的冷静基线，同时把句尾压得更短、更干、更利落，偏移最小，最适合作为 round2 首推候选。",
}


class TtsRequestError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_code: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


class VisualGenerationError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        status: str = STATUS_FAILED,
        failure_reason: str = "",
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.status = status
        self.failure_reason = failure_reason


class CloudAssemblyError(RuntimeError):
    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        error_code: str | None = None,
        status: str = STATUS_FAILED,
        failure_reason: str = "",
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code
        self.status = status
        self.failure_reason = failure_reason

REQUIRED_TOP_LEVEL_SECTIONS = [
    "主题",
    "基础参数",
    "目标场景",
    "目标用户",
    "全局质量要求",
    "Hook",
    "结尾落点",
    "分段结构",
]

REQUIRED_SEGMENT_FIELDS = {
    "段落ID": "segment_id",
    "计划时长": "planned_duration_seconds",
    "段目标": "goal",
    "配音文案": "voiceover_text",
    "字幕文案": "caption_text",
    "画面意图": "visual_intent",
    "需要图片": "needs_image",
    "需要视频": "needs_video",
    "允许真实桌面素材": "allow_real_desktop_footage",
}

OPTIONAL_SEGMENT_FIELDS = {
    "段载体": "carrier",
    "素材键": "asset_key",
    "素材来源": "asset_source",
}


def parse_formal_case_markdown(path: pathlib.Path) -> dict[str, Any]:
    raw_sections: dict[str, list[str]] = {}
    segment_blocks: list[dict[str, Any]] = []
    current_section: str | None = None
    current_segment: dict[str, Any] | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            current_section = line[2:].strip()
            raw_sections[current_section] = []
            current_segment = None
            continue
        if line.startswith("## "):
            current_section = line[3:].strip()
            raw_sections[current_section] = []
            current_segment = None
            continue
        if line.startswith("### "):
            current_segment = {"heading": line[4:].strip(), "lines": []}
            segment_blocks.append(current_segment)
            continue

        if current_section == "分段结构" and current_segment is not None:
            current_segment["lines"].append(line)
            continue

        if current_section is not None:
            raw_sections[current_section].append(line)

    for name in REQUIRED_TOP_LEVEL_SECTIONS:
        if name == "分段结构":
            if name not in raw_sections:
                raise ValueError(f"缺少必填章节：{name}")
            continue
        if not _section_text(raw_sections.get(name, [])).strip():
            raise ValueError(f"缺少必填章节：{name}")

    base_params = _parse_bullet_kv(raw_sections["基础参数"])
    total_duration = _parse_seconds(base_params.get("总时长", ""))
    aspect_ratio = base_params.get("视频比例", "").strip()
    if total_duration <= 0:
        raise ValueError("基础参数缺少合法的总时长")
    if not aspect_ratio:
        raise ValueError("基础参数缺少视频比例")

    segments = [_parse_segment_block(block) for block in segment_blocks]
    if not segments:
        raise ValueError("分段结构不能为空")

    route_settings = _parse_bullet_kv(raw_sections.get("展示主线", []))
    route_profile = route_settings.get("路由画像", "").strip()
    video_route_strategy = route_settings.get("主策略", "").strip()
    route_reason = route_settings.get("路由理由", "").strip()
    if not route_profile:
        route_profile = _default_route_profile(segments)
    if not video_route_strategy:
        video_route_strategy = "hybrid" if route_profile == DEFAULT_MAINLINE_ROUTE_PROFILE else "ppt_primary"
    if not route_reason:
        route_reason = (
            "API 真人负责判断与收束，用户本地录制素材负责过程证据，少量 PPT / 图片负责关键词显影，最终统一进云端剪辑。"
            if route_profile == DEFAULT_MAINLINE_ROUTE_PROFILE
            else "当前样例仍以 pure PPT / 信息卡承载结构解释与结果收束。"
        )

    return {
        "theme": _section_text(raw_sections["主题"]),
        "total_duration_seconds": total_duration,
        "aspect_ratio": aspect_ratio,
        "target_scenario": _section_text(raw_sections["目标场景"]),
        "target_user": _section_text(raw_sections["目标用户"]),
        "quality_requirements": _section_list(raw_sections["全局质量要求"]),
        "hook": _section_text(raw_sections["Hook"]),
        "ending": _section_text(raw_sections["结尾落点"]),
        "route_profile": route_profile,
        "video_route_strategy": video_route_strategy,
        "route_reason": route_reason,
        "segments": segments,
    }


def build_presentation_route_plan(video_spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "formal_api_demo_route_plan/v1",
        "route_profile": video_spec.get("route_profile") or _default_route_profile(video_spec.get("segments", [])),
        "video_route_strategy": video_spec.get("video_route_strategy")
        or (
            "hybrid"
            if (video_spec.get("route_profile") or "") == DEFAULT_MAINLINE_ROUTE_PROFILE
            else "ppt_primary"
        ),
        "route_reason": video_spec.get("route_reason", ""),
        "blocks": [
            {
                "block_id": segment["segment_id"],
                "block_goal": segment["goal"],
                "block_carrier": segment["carrier"],
                "asset_source": segment["asset_source"],
                "asset_key": segment["asset_key"],
                "needs_image": segment["needs_image"],
                "needs_video": segment["needs_video"],
                "allow_real_desktop_footage": segment["allow_real_desktop_footage"],
                "visual_intent": segment["visual_intent"],
            }
            for segment in video_spec.get("segments", [])
        ],
    }


def _default_route_profile(segments: list[dict[str, Any]]) -> str:
    if any(segment.get("carrier") in LOCAL_VIDEO_CARRIERS for segment in segments):
        return DEFAULT_MAINLINE_ROUTE_PROFILE
    return DEFAULT_PPT_ROUTE_PROFILE


def _default_segment_carrier(
    *,
    needs_image: bool,
    needs_video: bool,
    allow_real_desktop_footage: bool,
) -> str:
    if allow_real_desktop_footage and needs_video:
        return CARRIER_SELF_FOOTAGE
    if needs_image and not needs_video:
        return CARRIER_LIGHT_PPT
    return CARRIER_API_VISUAL


def _default_segment_asset_source(
    *,
    carrier: str,
    allow_real_desktop_footage: bool,
) -> str:
    if carrier == CARRIER_SELF_FOOTAGE or allow_real_desktop_footage:
        return USER_MEDIA_SOURCE
    return API_GENERATED_SOURCE


def _resolve_visual_delivery_mode(segment_assets: list[dict[str, Any]]) -> str:
    origins = {
        asset.get("asset_origin") or API_GENERATED_SOURCE
        for asset in segment_assets
    }
    if origins == {USER_MEDIA_SOURCE}:
        return "user_provided_local_assets"
    if USER_MEDIA_SOURCE in origins and API_GENERATED_SOURCE in origins:
        return "mixed_user_and_api_local_assets"
    return "api_generated_local_assets"


def _visual_delivery_is_primary_asset_mode(delivery_mode: str) -> bool:
    return delivery_mode in {
        "api_generated_local_assets",
        "user_provided_local_assets",
        "mixed_user_and_api_local_assets",
    }


def load_formal_config(
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
) -> dict[str, Any]:
    example_config = _parse_simple_toml(example_config_path)
    merged_config = copy.deepcopy(example_config)
    has_local_config = False

    if local_config_path is not None and local_config_path.exists():
        local_config = _parse_simple_toml(local_config_path)
        _deep_merge(merged_config, local_config)
        has_local_config = True

    return {
        "config": merged_config,
        "has_local_config": has_local_config,
        "local_config_path": str(local_config_path) if local_config_path else None,
        "example_config_path": str(example_config_path),
    }


def run_generation_pipeline(
    input_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    video_spec = parse_formal_case_markdown(input_path)
    config_bundle = load_formal_config(example_config_path, local_config_path)
    config = config_bundle["config"]
    generation_gate = evaluate_generation_gate(
        video_spec=video_spec,
        config=config,
        has_local_config=config_bundle["has_local_config"],
        dry_run=dry_run,
    )
    tts_gate = generation_gate["stage_gates"]["tts_probe"]
    visual_gate = generation_gate["stage_gates"]["visual_generation"]

    output_dir.mkdir(parents=True, exist_ok=True)
    tts_probe = build_default_tts_probe(video_spec)
    voiceover = build_default_voiceover_generation(video_spec, config)
    caption_assets = build_default_caption_assets(video_spec)
    visual_generation = build_default_visual_generation(video_spec, config)
    rotation_state = _build_default_rotation_state()
    manifest = build_manifest(
        input_path=input_path,
        video_spec=video_spec,
        config=config,
        generation_gate=generation_gate,
        output_dir=output_dir,
        dry_run=dry_run,
        tts_probe=tts_probe,
    )
    manifest_path = output_dir / "manifest.json"
    generation_gate_path = output_dir / "generation_gate.json"
    route_plan_path = output_dir / "route_plan.json"

    if dry_run:
        tts_probe["candidate_pool"] = tts_gate.get("candidate_pool", {})
        tts_probe["current_missing_prerequisites"] = tts_gate["missing_prerequisites"]
        voiceover["current_missing_prerequisites"] = tts_gate["missing_prerequisites"]
        visual_generation["candidate_pool"] = visual_gate.get("candidate_pool", {})
        visual_generation["current_missing_prerequisites"] = visual_gate["missing_prerequisites"]
        visual_generation["missing_implementations"] = visual_gate["missing_implementations"]
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)
        manifest = apply_voiceover_to_manifest(manifest, voiceover)
        manifest = apply_caption_assets_to_manifest(manifest, caption_assets)
        manifest = apply_visual_generation_to_manifest(manifest, visual_generation)
    else:
        local_media_blocked = any(
            item.startswith("footage_input_")
            for item in visual_gate.get("missing_prerequisites", [])
        )
        if local_media_blocked:
            blocked_gate = copy.deepcopy(tts_gate)
            blocked_gate.update(
                {
                    "status": STATUS_BLOCKED,
                    "blocked_reason": generation_gate.get("blocked_reason", ""),
                    "failure_reason": "",
                    "missing_prerequisites": generation_gate.get(
                        "missing_prerequisites",
                        [],
                    ),
                }
            )
            tts_probe = build_blocked_tts_probe(video_spec, blocked_gate)
            manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)

            voiceover = build_blocked_voiceover_generation(
                video_spec,
                tts_probe,
                blocked_gate,
            )
            manifest = apply_voiceover_to_manifest(manifest, voiceover)

            caption_assets = write_formal_script_and_captions(
                video_spec=video_spec,
                output_dir=output_dir,
            )
            manifest = apply_caption_assets_to_manifest(manifest, caption_assets)

            visual_generation = build_visual_generation_plan(
                video_spec=video_spec,
                config=config,
                output_dir=output_dir,
                visual_gate=visual_gate,
                rotation_state=rotation_state,
            )
            manifest = apply_visual_generation_to_manifest(manifest, visual_generation)
        elif tts_gate["status"] == STATUS_SUCCESS:
            tts_probe = execute_tts_probe(
                video_spec=video_spec,
                config=config,
                output_dir=output_dir,
                rotation_state=rotation_state,
            )
        else:
            tts_probe = build_blocked_tts_probe(video_spec, tts_gate)
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)

        if tts_probe["status"] == STATUS_SUCCESS:
            voiceover = execute_formal_voiceover_generation(
                video_spec=video_spec,
                config=config,
                output_dir=output_dir,
                rotation_state=rotation_state,
            )
        else:
            voiceover = build_blocked_voiceover_generation(video_spec, tts_probe, tts_gate)
        manifest = apply_voiceover_to_manifest(manifest, voiceover)

        caption_assets = write_formal_script_and_captions(
            video_spec=video_spec,
            output_dir=output_dir,
        )
        manifest = apply_caption_assets_to_manifest(manifest, caption_assets)

        visual_generation = build_visual_generation_plan(
            video_spec=video_spec,
            config=config,
            output_dir=output_dir,
            visual_gate=visual_gate,
            rotation_state=rotation_state,
        )
        manifest = apply_visual_generation_to_manifest(manifest, visual_generation)

    manifest["generation"]["status"] = _combine_stage_statuses(
        [
            manifest["generation"]["tts_probe"]["status"],
            manifest["generation"]["voiceover"]["status"],
            manifest["generation"]["captions"]["status"],
            manifest["generation"]["visual_generation"]["status"],
        ],
        dry_run=dry_run,
    )
    manifest["current_status"] = manifest["generation"]["status"]
    manifest["status_summary"] = {
        "generation": manifest["generation"]["status"],
        "local_assembly": manifest.get("status_summary", {}).get("local_assembly", STATUS_NOT_STARTED),
        "cloud_assembly": manifest.get("status_summary", {}).get("cloud_assembly", STATUS_NOT_STARTED),
        "overall_status": manifest["generation"]["status"],
    }
    manifest["known_issues"] = _merge_known_issues(
        manifest["known_issues"],
        _voiceover_known_issues(manifest["generation"]["voiceover"]),
        _visual_generation_known_issues(manifest["generation"]["visual_generation"]),
    )

    write_json(manifest_path, manifest)
    write_json(generation_gate_path, generation_gate)
    write_json(route_plan_path, manifest["presentation_routing"])

    result_summary = build_generation_result_summary(
        manifest=manifest,
        generation_gate=generation_gate,
        output_dir=output_dir,
        dry_run=dry_run,
    )
    write_json(output_dir / "result_summary.json", result_summary)
    return result_summary


def build_blocked_tts_probe(
    video_spec: dict[str, Any],
    tts_gate: dict[str, Any],
) -> dict[str, Any]:
    blocked_probe = build_default_tts_probe(video_spec)
    blocked_probe.update(
        {
            "status": tts_gate["status"],
            "blocked_reason": tts_gate.get("blocked_reason", ""),
            "failure_reason": tts_gate.get("failure_reason", ""),
            "error_code": "",
            "error_message": tts_gate.get("blocked_reason", ""),
            "current_missing_prerequisites": tts_gate["missing_prerequisites"],
            "candidate_pool": tts_gate.get("candidate_pool", {}),
        }
    )
    return blocked_probe


def build_blocked_voiceover_generation(
    video_spec: dict[str, Any],
    tts_probe: dict[str, Any],
    tts_gate: dict[str, Any],
) -> dict[str, Any]:
    voiceover = build_default_voiceover_generation(video_spec, {})
    voiceover.update(
        {
            "status": tts_probe.get("status", STATUS_BLOCKED),
            "blocked_reason": tts_probe.get("blocked_reason") or tts_gate.get("blocked_reason", ""),
            "failure_reason": tts_probe.get("failure_reason", ""),
            "error_message": tts_probe.get("error_message", ""),
            "current_missing_prerequisites": tts_gate.get("missing_prerequisites", []),
        }
    )
    return voiceover


def run_aliyun_tts_style_probe_variants(
    input_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    return _run_aliyun_tts_style_probe_round(
        input_path=input_path,
        example_config_path=example_config_path,
        local_config_path=local_config_path,
        output_dir=output_dir,
        round_id="round1",
        round_goal="基于声音目标稿 v1 做第一轮 A/B/C 对照，先确认风格桥接与基础方向。",
        summary_filename="tts_style_probe_variants.json",
        variant_defaults=DEFAULT_ALIYUN_TTS_STYLE_VARIANTS,
        variant_section_prefix="tts_style_probe_variant_",
        recommendation_basis="第一轮结果只用于建立基线，不代替人工试听定稿。",
        round_section_name=None,
    )


def run_aliyun_tts_style_probe_round2(
    input_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    return _run_aliyun_tts_style_probe_round(
        input_path=input_path,
        example_config_path=example_config_path,
        local_config_path=local_config_path,
        output_dir=output_dir,
        round_id="round2",
        round_goal="围绕旧 A 做第二轮更窄的微调，不重新切模型族，也不推进 assembly。",
        summary_filename="tts_style_probe_round2.json",
        variant_defaults=DEFAULT_ALIYUN_TTS_STYLE_ROUND2_VARIANTS,
        variant_section_prefix="tts_style_probe_round2_variant_",
        recommendation_basis="当前推荐基于用户反馈“旧 A 更对”与参数设计判断，仍需人工试听确认，不代表最终定稿。",
        round_section_name="tts_style_probe_round2",
    )


def _run_aliyun_tts_style_probe_round(
    *,
    input_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
    round_id: str,
    round_goal: str,
    summary_filename: str,
    variant_defaults: tuple[dict[str, Any], ...],
    variant_section_prefix: str,
    recommendation_basis: str,
    round_section_name: str | None,
) -> dict[str, Any]:
    video_spec = parse_formal_case_markdown(input_path)
    config_bundle = load_formal_config(example_config_path, local_config_path)
    config = config_bundle["config"]
    gate = _evaluate_tts_generation_gate(
        video_spec=video_spec,
        config=config,
        has_local_config=config_bundle["has_local_config"],
        dry_run=False,
    )
    route_family = _get_tts_api_route_family(config)
    probe_text, probe_text_source = _get_aliyun_tts_style_probe_text(config)
    variants = _load_tts_style_probe_variants(
        config=config,
        default_variants=variant_defaults,
        section_prefix=variant_section_prefix,
    )
    recommended_variant = _resolve_recommended_tts_style_variant(
        config=config,
        variants=variants,
        round_section_name=round_section_name,
    )
    recommendation_reason = _resolve_tts_style_recommendation_reason(
        config=config,
        round_section_name=round_section_name,
        recommended_variant=recommended_variant,
    )
    variants_path = output_dir / summary_filename
    output_dir.mkdir(parents=True, exist_ok=True)

    result: dict[str, Any] = {
        "round_id": round_id,
        "round_goal": round_goal,
        "overall_status": STATUS_BLOCKED,
        "failure_reason": "",
        "blocked_reason": "",
        "api_route_family": route_family,
        "provider": _get_tts_provider_name(config, route_family=route_family),
        "model_identifier": _get_tts_model_identifier(config, route_family=route_family),
        "voice": _nested_get(config, "tts", "voice"),
        "style_probe_text": probe_text,
        "style_probe_text_source": probe_text_source,
        "style_draft_in_request": False,
        "recommended_variant_id": recommended_variant["variant_id"] if recommended_variant else "",
        "recommended_variant_label": recommended_variant["label"] if recommended_variant else "",
        "recommendation_reason": recommendation_reason,
        "recommendation_basis": recommendation_basis,
        "variants": [],
    }

    if gate["status"] != STATUS_SUCCESS:
        result["overall_status"] = gate["status"]
        result["failure_reason"] = gate.get("failure_reason", "")
        result["blocked_reason"] = gate.get("blocked_reason", "")
        write_json(variants_path, result)
        return result

    if route_family != TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        result["blocked_reason"] = (
            "当前 style probe variants 仅支持 aliyun_bailian_cosyvoice route family。"
        )
        write_json(variants_path, result)
        return result

    variant_results: list[dict[str, Any]] = []

    for variant in variants:
        probe = execute_tts_probe(
            video_spec=video_spec,
            config=config,
            output_dir=output_dir,
            probe_text=probe_text,
            probe_text_source=probe_text_source,
            output_stem=f"voice_probe_{variant['variant_id']}",
            tts_override={
                "instruction": variant["instruction"],
                "speech_rate": variant["speech_rate"],
                "pitch_rate": variant["pitch_rate"],
                "volume": variant["volume"],
            },
        )
        variant_results.append(
            {
                "variant_id": variant["variant_id"],
                "label": variant["label"],
                "intent": variant["intent"],
                "instruction": variant["instruction"],
                "speech_rate": variant["speech_rate"],
                "pitch_rate": variant["pitch_rate"],
                "volume": variant["volume"],
                "status": probe["status"],
                "audio_path": probe.get("audio_path"),
                "failure_reason": probe.get("failure_reason", ""),
                "error_message": probe.get("error_message", ""),
                "request_debug": probe.get("request_debug", {}),
                "probe_text": probe.get("probe_text"),
                "probe_text_source": probe.get("probe_text_source"),
            }
        )

    result["variants"] = variant_results
    result["style_draft_in_request"] = all(
        item.get("request_debug", {}).get("style_draft_in_request") is True
        for item in variant_results
    )
    result["overall_status"] = _summarize_tts_style_variant_status(variant_results)
    if result["overall_status"] == STATUS_FAILED:
        first_failed = next(
            (item for item in variant_results if item.get("status") == STATUS_FAILED),
            None,
        )
        if first_failed is not None:
            result["failure_reason"] = first_failed.get("failure_reason", "")
    if result["overall_status"] == STATUS_BLOCKED:
        first_blocked = next(
            (item for item in variant_results if item.get("status") == STATUS_BLOCKED),
            None,
        )
        if first_blocked is not None:
            result["blocked_reason"] = first_blocked.get("error_message", "")

    write_json(variants_path, result)
    return result


def run_assembly_pipeline(
    manifest_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    config_bundle = load_formal_config(example_config_path, local_config_path)
    config = config_bundle["config"]
    assembly_gate = evaluate_assembly_gate(
        manifest=manifest,
        config=config,
        has_local_config=config_bundle["has_local_config"],
        dry_run=dry_run,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    assembly_plan = build_assembly_plan(
        manifest=manifest,
        config=config,
        assembly_gate=assembly_gate,
    )
    manifest["machine_gate"]["assembly_gate"] = assembly_gate
    local_assembly_result = build_default_local_assembly(output_dir)
    preview_result = build_default_assembly_preview(output_dir)
    cloud_result: dict[str, Any] = {
        "status": STATUS_PLANNED if dry_run else assembly_gate["status"],
        "blocked_reason": "" if dry_run else assembly_gate.get("blocked_reason", ""),
        "failure_reason": "",
        "error_message": "" if dry_run else assembly_gate.get("blocked_reason", ""),
        "missing_prerequisites": list(assembly_gate["missing_prerequisites"]),
        "missing_implementations": list(assembly_gate["missing_implementations"]),
        "project_id": None,
        "project_title": _nested_get(config, "aliyun_ims", "cloud_project_name"),
        "job_id": None,
        "media_id": None,
        "output_url": None,
        "media_url": None,
        "timeline_path": str(output_dir / "assembly" / "cloud_timeline.json"),
        "request_ids": {},
        "uploaded_assets": [],
    }
    if dry_run:
        local_assembly_result["status"] = STATUS_PLANNED
        preview_result["status"] = STATUS_PLANNED
    elif assembly_gate["allow_execution"]:
        cloud_result = _execute_cloud_only_assembly(
            manifest=manifest,
            config=config,
            output_dir=output_dir,
        )
    local_assembly_status = STATUS_PLANNED if dry_run else STATUS_NOT_STARTED
    cloud_assembly_status = STATUS_PLANNED if dry_run else cloud_result["status"]
    delivery_status = STATUS_PLANNED if dry_run else cloud_assembly_status
    delivery_mode = "oss_cloud_assembly"
    overall_status = _combine_stage_statuses(
        [
            manifest.get("generation", {}).get("status", STATUS_NOT_STARTED),
            delivery_status,
        ],
        dry_run=dry_run,
    )
    manifest["assembly"] = {
        "status": delivery_status,
        "task_id": cloud_result.get("job_id"),
        "resource_id": cloud_result.get("project_id"),
        "output_id": cloud_result.get("media_id"),
        "delivery_mode": delivery_mode,
        "delivery_video_path": cloud_result.get("output_url") or cloud_result.get("media_url"),
        "local": local_assembly_result,
        "cloud": {
            "status": cloud_assembly_status,
            "blocked_reason": cloud_result.get("blocked_reason", ""),
            "failure_reason": cloud_result.get("failure_reason", ""),
            "error_message": cloud_result.get("error_message", ""),
            "missing_prerequisites": cloud_result.get("missing_prerequisites", []),
            "missing_implementations": cloud_result.get("missing_implementations", []),
            "is_primary_path": True,
            "project_id": cloud_result.get("project_id"),
            "project_title": cloud_result.get("project_title"),
            "job_id": cloud_result.get("job_id"),
            "media_id": cloud_result.get("media_id"),
            "output_url": cloud_result.get("output_url"),
            "media_url": cloud_result.get("media_url"),
            "timeline_path": cloud_result.get("timeline_path"),
            "request_ids": cloud_result.get("request_ids", {}),
            "uploaded_assets": cloud_result.get("uploaded_assets", []),
            "target": build_cloud_assembly_target(config),
        },
        "preview": preview_result,
    }
    manifest["status_summary"] = {
        "generation": manifest.get("generation", {}).get("status", STATUS_NOT_STARTED),
        "assembly_delivery": delivery_status,
        "local_assembly": local_assembly_status,
        "cloud_assembly": cloud_assembly_status,
        "overall_status": overall_status,
    }
    manifest["current_status"] = overall_status
    manifest["known_issues"] = _merge_known_issues(
        manifest.get("known_issues", []),
        _local_assembly_known_issues(local_assembly_result),
        _assembly_preview_known_issues(preview_result),
        _cloud_assembly_known_issues(manifest["assembly"]["cloud"]),
    )

    write_json(manifest_path, manifest)
    write_json(output_dir / "assembly_gate.json", assembly_gate)
    write_json(output_dir / "assembly_plan.json", assembly_plan)

    result_summary = build_assembly_result_summary(
        manifest=manifest,
        assembly_gate=assembly_gate,
        output_dir=output_dir,
        dry_run=dry_run,
    )
    write_json(output_dir / "result_summary.json", result_summary)
    return result_summary


def _evaluate_tts_generation_gate(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    route_family = _get_tts_api_route_family(config)
    tts_provider = _get_tts_provider_name(config, route_family=route_family)
    configured_provider = _nested_get(config, "provider", "name")
    tts_candidates = _resolve_tts_candidate_pool(config)
    candidate_pool = _summarize_tts_candidate_pool(tts_candidates)
    available_candidates = [
        candidate
        for candidate in tts_candidates
        if not _tts_candidate_missing_prerequisites(candidate)
    ]
    missing = [] if available_candidates else _generation_missing_prerequisites(
        video_spec,
        config,
        has_local_config,
        route_family=route_family,
    )
    implementation_missing: list[str] = []
    failure_reason = ""
    checks = [
        {
            "name": "input_segments_present",
            "status": "pass" if len(video_spec["segments"]) >= 1 else "fail",
            "detail": f"当前共有 {len(video_spec['segments'])} 个段落。",
        },
        {
            "name": "provider_selected",
            "status": "pass"
            if tts_provider in {PROVIDER_VOLCENGINE, PROVIDER_ALIYUN_BAILIAN}
            else "fail",
            "detail": (
                f"configured_provider={configured_provider or 'missing'}, "
                f"resolved_tts_provider={tts_provider or 'missing'}"
            ),
        },
        {
            "name": "tts_route_family_selected",
            "status": "pass" if route_family in SUPPORTED_TTS_ROUTE_FAMILIES else "fail",
            "detail": f"api_route_family={route_family}",
        },
        {
            "name": "tts_route_family_ready",
            "status": "pass"
            if route_family != TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH
            else "fail",
            "detail": (
                "当前 Ark、Edge Gateway 和阿里百炼 CosyVoice 已接入真实 probe；"
                "Doubao OpenSpeech 仍是 gate-only。"
            ),
        },
        {
            "name": "tts_api_key_present",
            "status": "pass"
            if available_candidates
            else "fail",
            "detail": "当前 preflight 已升级为整条候选链检查，不再只看单个 auth.api_key。",
        },
        {
            "name": "tts_voice_present",
            "status": "pass"
            if available_candidates
            else "fail",
            "detail": "当前 preflight 已升级为整条候选链检查，不再只看单个 tts.voice。",
        },
        {
            "name": "tts_usable_candidate_present",
            "status": "pass"
            if available_candidates
            else "fail",
            "detail": f"available_candidates={len(available_candidates)} / total_candidates={len(tts_candidates)}",
        },
        {
            "name": "cloud_only_assembly_route_locked",
            "status": "pass",
            "detail": "正式默认主线已锁定为北京区 OSS + 云剪唯一 assembly 路线，本地 fallback 不再作为正常交付。",
        },
    ]
    checks.extend(
        _build_tts_route_family_checks(
            config=config,
            route_family=route_family,
        )
    )

    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        implementation_missing.append("doubao_openspeech_v3_provider")

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif route_family not in SUPPORTED_TTS_ROUTE_FAMILIES:
        status = STATUS_BLOCKED
        blocked_reason = f"当前不支持的 TTS route family：{route_family}"
    elif not available_candidates:
        status = STATUS_BLOCKED
        blocked_reason = "缺少 TTS probe 前提：" + "、".join(missing)
    elif OpenAI is None and route_family in {
        TTS_ROUTE_FAMILY_ARK,
        TTS_ROUTE_FAMILY_EDGE_GATEWAY,
    }:
        status = STATUS_BLOCKED
        blocked_reason = "本地缺少 openai Python SDK，无法发起当前 route family 的 TTS probe。"
        failure_reason = "missing_openai_sdk"
        implementation_missing.append("openai_python_sdk")
    elif route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        status = STATUS_BLOCKED
        blocked_reason = (
            "doubao openspeech v3 route family 已拆出，但 provider implementation 尚未接入。"
        )
    elif tts_provider not in {PROVIDER_VOLCENGINE, PROVIDER_ALIYUN_BAILIAN}:
        status = STATUS_BLOCKED
        blocked_reason = f"当前 TTS probe 还不支持 provider：{tts_provider or 'missing'}"
    else:
        status = STATUS_SUCCESS
        blocked_reason = ""

    return {
        "gate_name": "generation_gate",
        "status": status,
        "scope": "tts_probe_only",
        "allow_execution": not dry_run and status == STATUS_SUCCESS,
        "blocked_reason": blocked_reason,
        "failure_reason": failure_reason,
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "candidate_pool": candidate_pool,
        "tts_target": {
            "api_route_family": route_family,
            "model_identifier": _get_tts_model_identifier(config, route_family=route_family),
            "endpoint_id": _nested_get(config, "tts", "endpoint_id"),
            "model": _nested_get(config, "tts", "model"),
            "resource_id": _nested_get(config, "tts", "resource_id"),
            "voice": _nested_get(config, "tts", "voice"),
            "region": _nested_get(config, "provider", "region"),
            "provider": tts_provider,
        },
        "checks": checks,
        "notes": [
            "当前子 Gate 只评估 TTS probe / voiceover 所需前提。",
            "dry-run 只验证输入、契约和 Gate，不调用远端。",
            "route family 已显式拆分为 Ark / Edge Gateway / 阿里百炼 CosyVoice / Doubao OpenSpeech，不再默认混走 Ark。",
            "当前 TTS preflight 已升级为候选链检查；只要存在 1 个可用候选，就不再把单个 primary 缺失误判成整体 blocked。",
        ],
    }


def evaluate_generation_gate(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    tts_gate = _evaluate_tts_generation_gate(
        video_spec=video_spec,
        config=config,
        has_local_config=has_local_config,
        dry_run=dry_run,
    )
    visual_gate = _evaluate_visual_generation_gate(
        video_spec=video_spec,
        config=config,
        has_local_config=has_local_config,
        dry_run=dry_run,
    )
    overall_status = _combine_stage_statuses(
        [
            tts_gate["status"],
            visual_gate["status"],
        ],
        dry_run=dry_run,
    )
    missing = _merge_unique_values(
        tts_gate["missing_prerequisites"],
        visual_gate["missing_prerequisites"],
    )
    missing_implementations = _merge_unique_values(
        tts_gate["missing_implementations"],
        visual_gate["missing_implementations"],
    )
    failure_reason = tts_gate.get("failure_reason", "")
    blocked_reason = tts_gate.get("blocked_reason", "")
    if visual_gate["status"] == STATUS_BLOCKED and visual_gate.get("blocked_reason"):
        blocked_reason = (
            f"{blocked_reason}；{visual_gate['blocked_reason']}"
            if blocked_reason
            else visual_gate["blocked_reason"]
        )

    return {
        "gate_name": "generation_gate",
        "status": overall_status,
        "scope": "tts_voiceover_and_visual_generation",
        "allow_execution": not dry_run and overall_status == STATUS_SUCCESS,
        "blocked_reason": blocked_reason,
        "failure_reason": failure_reason,
        "missing_prerequisites": missing,
        "missing_implementations": missing_implementations,
        "tts_target": tts_gate["tts_target"],
        "visual_target": {
            "provider": _nested_get(config, "provider", "name"),
            "region": _nested_get(config, "provider", "region"),
            "image_model": _nested_get(config, "image_generation", "model"),
            "video_model": _nested_get(config, "video_generation", "model"),
            "general_video_model": _nested_get(config, "video_generation", "model"),
            "portrait_detect_model": _nested_get(config, "portrait_detect", "model"),
            "portrait_video_model": _nested_get(config, "portrait_video_generation", "model"),
            "model_routes": _build_visual_model_routes(config),
        },
        "stage_gates": {
            "tts_probe": tts_gate,
            "visual_generation": visual_gate,
        },
        "checks": tts_gate["checks"] + visual_gate["checks"],
        "notes": [
            "正式 generation success 仍要求配音 API 成功，且视觉层必须真实拿到可组装资产：默认人物段走 API 真人，过程段走用户本地素材，少量信息卡走 API 图像。",
            "visual plan / preview storyboard 只能算辅助产物，不能再冒充 visual generation success。",
            "默认正式主线已切到 API human + user local footage + light_ppt；本地 preview 只保留辅助调试意义。",
            "assembly 主线继续固定为北京区 OSS + 云剪 cloud-only，不回退 local assembly 默认主路径。",
        ],
    }


def _segment_requires_local_media(segment: dict[str, Any]) -> bool:
    return bool(segment.get("asset_key")) and segment.get("asset_source") == USER_MEDIA_SOURCE


def _segment_uses_api_human(segment: dict[str, Any]) -> bool:
    return (
        segment.get("carrier") == CARRIER_HUMAN
        and segment.get("asset_source") != USER_MEDIA_SOURCE
        and bool(segment.get("needs_video"))
    )


def _segment_needs_api_image(segment: dict[str, Any]) -> bool:
    return _segment_uses_api_human(segment) or (
        bool(segment.get("needs_image")) and not _segment_requires_local_media(segment)
    )


def _segment_needs_api_video(segment: dict[str, Any]) -> bool:
    return bool(segment.get("needs_video")) and not _segment_requires_local_media(segment)


def _resolve_footage_input(config: dict[str, Any], asset_key: str) -> dict[str, Any]:
    payload = _nested_get(config, "footage_inputs", asset_key) or {}
    local_path = _normalize_optional_text(payload.get("local_path"))
    source_type = _normalize_optional_text(payload.get("source_type")) or "user_recorded_video"
    verified_role = _normalize_optional_text(payload.get("verified_role"))
    media_kind = "image" if source_type in {"user_image", "user_ppt_image"} else "video"
    return {
        "asset_key": asset_key,
        "local_path": local_path,
        "source_type": source_type,
        "verified_role": verified_role,
        "media_kind": media_kind,
    }


def _evaluate_visual_generation_gate(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    missing: list[str] = []
    implementation_missing: list[str] = []
    visual_routes = _build_visual_model_routes(config)
    image_candidates = _resolve_visual_candidate_pool(config, resource_kind=RESOURCE_KIND_IMAGE)
    video_candidates = _resolve_visual_candidate_pool(config, resource_kind=RESOURCE_KIND_VIDEO)
    candidate_pool = _summarize_visual_candidate_pool(image_candidates, video_candidates)
    available_image_candidates = [
        candidate
        for candidate in image_candidates
        if not _visual_candidate_missing_prerequisites(candidate, resource_kind=RESOURCE_KIND_IMAGE)
    ]
    available_video_candidates = [
        candidate
        for candidate in video_candidates
        if not _visual_candidate_missing_prerequisites(candidate, resource_kind=RESOURCE_KIND_VIDEO)
    ]
    visual_provider = available_image_candidates[0]["provider"] if available_image_candidates else _nested_get(config, "provider", "name")
    portrait_provider_supported = _nested_get(config, "provider", "name") == PROVIDER_ALIYUN_BAILIAN
    image_provider_supported = any(
        candidate.get("provider") == PROVIDER_ALIYUN_BAILIAN
        for candidate in available_image_candidates
    ) if available_image_candidates else (_nested_get(config, "provider", "name") == PROVIDER_ALIYUN_BAILIAN)
    video_provider_supported = any(
        candidate.get("provider") == PROVIDER_ALIYUN_BAILIAN
        for candidate in available_video_candidates
    ) if available_video_candidates else (_nested_get(config, "provider", "name") == PROVIDER_ALIYUN_BAILIAN)
    needs_image = any(
        _segment_needs_api_image(segment) for segment in video_spec.get("segments", [])
    )
    needs_video = any(
        _segment_needs_api_video(segment) for segment in video_spec.get("segments", [])
    )
    portrait_detect_enabled = visual_routes["portrait_detect"]["enabled"]
    portrait_video_enabled = visual_routes["portrait_video_generation"]["enabled"]
    required_local_media_inputs = [
        segment for segment in video_spec.get("segments", []) if _segment_requires_local_media(segment)
    ]
    image_missing_union = _candidate_missing_union(
        image_candidates,
        missing_fn=lambda candidate: _visual_candidate_missing_prerequisites(
            candidate,
            resource_kind=RESOURCE_KIND_IMAGE,
        ),
    )
    video_missing_union = _candidate_missing_union(
        video_candidates,
        missing_fn=lambda candidate: _visual_candidate_missing_prerequisites(
            candidate,
            resource_kind=RESOURCE_KIND_VIDEO,
        ),
    )
    if not has_local_config:
        missing.append("local_config_file")
    if not available_image_candidates and not available_video_candidates:
        missing.append("api_key")
    if _is_missing_secret(_nested_get(config, "provider", "region")) and not (
        available_image_candidates or available_video_candidates
    ):
        missing.append("provider_region")
    if needs_image and not available_image_candidates:
        for item in image_missing_union or ["image_generation_model"]:
            if item not in missing:
                missing.append(item)
    if needs_video and not available_video_candidates:
        for item in video_missing_union or ["video_generation_model"]:
            if item not in missing:
                missing.append(item)
    if portrait_video_enabled and not portrait_detect_enabled:
        missing.append("portrait_detect_enabled")
    if portrait_detect_enabled and _is_missing_secret(_nested_get(config, "portrait_detect", "model")):
        missing.append("portrait_detect_model")
    if portrait_video_enabled and _is_missing_secret(
        _nested_get(config, "portrait_video_generation", "model")
    ):
        missing.append("portrait_video_generation_model")
    for segment in required_local_media_inputs:
        asset_key = segment.get("asset_key") or segment["segment_id"]
        footage_input = _resolve_footage_input(config, asset_key)
        local_path = footage_input["local_path"]
        if _is_missing_secret(local_path):
            missing_name = f"footage_input_{asset_key}_local_path"
            if missing_name not in missing:
                missing.append(missing_name)
            continue
        if not pathlib.Path(local_path).expanduser().exists():
            missing_name = f"footage_input_{asset_key}_file_exists"
            if missing_name not in missing:
                missing.append(missing_name)
        if (
            segment.get("carrier") == CARRIER_HUMAN
            and footage_input["verified_role"] != FOOTAGE_ROLE_HUMAN_ON_CAMERA
        ):
            missing_name = f"footage_input_{asset_key}_verified_role_human_on_camera"
            if missing_name not in missing:
                missing.append(missing_name)
    if needs_image and not image_provider_supported:
        implementation_missing.append("image_generation_provider_implementation")
    if needs_video and not video_provider_supported:
        implementation_missing.append("video_generation_provider_implementation")
    if portrait_detect_enabled and not portrait_provider_supported:
        implementation_missing.append("portrait_detect_provider_implementation")
    if portrait_video_enabled and not portrait_provider_supported:
        implementation_missing.append("portrait_video_generation_provider_implementation")

    checks = [
        {
            "name": "visual_segments_present",
            "status": "pass" if video_spec.get("segments") else "fail",
            "detail": f"segments={len(video_spec.get('segments', []))}",
        },
        {
            "name": "image_model_present_when_required",
            "status": "pass"
            if not needs_image or bool(available_image_candidates)
            else "fail",
            "detail": f"有图片段落时必须存在至少 1 个可用 image candidate；available={len(available_image_candidates)}。",
        },
        {
            "name": "video_model_present_when_required",
            "status": "pass"
            if not needs_video or bool(available_video_candidates)
            else "fail",
            "detail": f"有视频段落时必须存在至少 1 个可用 video candidate；available={len(available_video_candidates)}。",
        },
        {
            "name": "required_user_footage_present",
            "status": "pass"
            if not required_local_media_inputs
            or all(
                not _is_missing_secret(_resolve_footage_input(config, segment.get("asset_key") or segment["segment_id"])["local_path"])
                and pathlib.Path(
                    _resolve_footage_input(config, segment.get("asset_key") or segment["segment_id"])["local_path"]
                )
                .expanduser()
                .exists()
                for segment in required_local_media_inputs
            )
            else "fail",
            "detail": "默认正式主线要求的用户本地录制素材必须先在本地配置里注入真实文件路径。",
        },
        {
            "name": "human_carrier_requires_verified_on_camera_footage",
            "status": "pass"
            if all(
                segment.get("carrier") != CARRIER_HUMAN
                or segment.get("asset_source") != USER_MEDIA_SOURCE
                or _resolve_footage_input(
                    config,
                    segment.get("asset_key") or segment["segment_id"],
                )["verified_role"]
                == FOOTAGE_ROLE_HUMAN_ON_CAMERA
                for segment in required_local_media_inputs
            )
            else "fail",
            "detail": "只有当 carrier=human 且素材来源=user_media 时，才必须显式标记 verified_role=\"human_on_camera\"；API 真人段不读取本地人物槽位。",
        },
        {
            "name": "portrait_detect_enabled_before_liveportrait",
            "status": "pass" if not portrait_video_enabled or portrait_detect_enabled else "fail",
            "detail": "启用 liveportrait 前必须先启用 portrait_detect。",
        },
        {
            "name": "portrait_detect_model_present_when_enabled",
            "status": "pass"
            if not portrait_detect_enabled
            or not _is_missing_secret(_nested_get(config, "portrait_detect", "model"))
            else "fail",
            "detail": "启用 portrait_detect 时必须显式提供 portrait_detect.model。",
        },
        {
            "name": "portrait_video_model_present_when_enabled",
            "status": "pass"
            if not portrait_video_enabled
            or not _is_missing_secret(_nested_get(config, "portrait_video_generation", "model"))
            else "fail",
            "detail": "启用 liveportrait 时必须显式提供 portrait_video_generation.model。",
        },
    ]

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif missing:
        status = STATUS_BLOCKED
        blocked_reason = "缺少视觉生成前提：" + "、".join(missing)
    elif implementation_missing:
        blocked_parts: list[str] = []
        if any(
            item in implementation_missing
            for item in (
                "image_generation_provider_implementation",
                "video_generation_provider_implementation",
            )
        ):
            blocked_parts.append(
                "当前普通图片 / 视频主线 provider 仅真实接入 aliyun_bailian / DashScope；"
                f"当前 provider={visual_provider or 'missing'} 仍无法执行 "
                f"{visual_routes['image_generation']['model'] or DEFAULT_GENERAL_IMAGE_MODEL}"
                " -> "
                f"{visual_routes['general_video_generation']['model'] or DEFAULT_GENERAL_VIDEO_MODEL}"
                "。"
            )
        if any(
            item in implementation_missing
            for item in (
                "portrait_detect_provider_implementation",
                "portrait_video_generation_provider_implementation",
            )
        ):
            blocked_parts.append(
                "真人开口分支仍固定为 liveportrait-detect -> liveportrait；"
                "当前 provider implementation 尚未接入。"
            )
        status = STATUS_BLOCKED
        blocked_reason = "；".join(blocked_parts) or (
            "当前免费优先模型路线已定，但相关 provider implementation 尚未接入；"
            "当前只能落 visual plan / storyboard，不能把 generation 写成 success。"
        )
    else:
        status = STATUS_SUCCESS
        blocked_reason = ""

    return {
        "gate_name": "visual_generation_gate",
        "status": status,
        "allow_execution": not dry_run and not missing and not implementation_missing,
        "blocked_reason": blocked_reason,
        "failure_reason": "",
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "candidate_pool": candidate_pool,
        "checks": checks,
        "notes": [
            "visual_generation Gate 继续代表图片 / 视频生成 API 的正式 generation 前提。",
            "默认正式主线已切到 API human + user local footage + light_ppt；hook / close 默认走 API 真人，过程证据默认走用户本地素材。",
            "普通视频默认主线固定为 wan2.6-image -> wan2.7-i2v；先出首帧 / 底图，再转视频。",
            f"人物图 / 人像底图默认走 {DEFAULT_GENERAL_IMAGE_MODEL}；需要修图时走 {DEFAULT_IMAGE_EDIT_MODEL}，不再默认依赖 facechain-generation。",
            "真人开口分支固定为 liveportrait-detect + liveportrait；liveportrait 必须先经过 liveportrait-detect。",
            f"{DEFAULT_VIDEO_EDIT_MODEL} 只用于后期修补 / 编辑增强，不是主生成模型。",
            "缺少 image_generation.model / video_generation.model 时，generation 不能写成 success。",
            "provider implementation 尚未接入时，当前必须诚实 blocked，不能再把 visual plan / preview 写成 success。",
            "当前 visual preflight 已升级为候选链检查；只要存在 1 个可用 image/video 候选，就不再把单个 primary 缺失误判成整体 blocked。",
        ],
    }


def _build_tts_route_family_checks(
    config: dict[str, Any],
    route_family: str,
) -> list[dict[str, str]]:
    if route_family in {
        TTS_ROUTE_FAMILY_EDGE_GATEWAY,
        TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE,
    }:
        detail = "Edge Gateway OpenAI 兼容 TTS 使用 tts.model，不读取 endpoint_id。"
        if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
            detail = "阿里百炼 CosyVoice 使用 tts.model + voice，不读取 endpoint_id。"
        return [
            {
                "name": "tts_model_present",
                "status": "pass"
                if not _is_missing_secret(_nested_get(config, "tts", "model"))
                else "fail",
                "detail": detail,
            },
        ]
    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        return [
            {
                "name": "openspeech_app_id_present",
                "status": "pass"
                if not _is_missing_secret(_nested_get(config, "auth", "app_id"))
                else "fail",
                "detail": "Doubao OpenSpeech v3 需要 app_id。",
            },
            {
                "name": "openspeech_resource_id_present",
                "status": "pass"
                if not _is_missing_secret(_nested_get(config, "tts", "resource_id"))
                else "fail",
                "detail": "Doubao OpenSpeech v3 需要 resource_id。",
            },
        ]
    return [
        {
            "name": "tts_model_or_endpoint_present",
            "status": "pass"
            if _get_tts_model_identifier(config, route_family=route_family)
            else "fail",
            "detail": "优先使用 endpoint_id；若未提供则退回 model。",
        },
    ]


def evaluate_assembly_gate(
    manifest: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    missing = _assembly_missing_prerequisites(manifest, config, has_local_config)
    implementation_missing: list[str] = []
    checks = [
        {
            "name": "manifest_schema_present",
            "status": "pass"
            if manifest.get("schema_version") == MANIFEST_SCHEMA_VERSION
            else "fail",
            "detail": manifest.get("schema_version", "missing"),
        },
        {
            "name": "segments_present",
            "status": "pass" if manifest.get("segments") else "fail",
            "detail": f"segments={len(manifest.get('segments', []))}",
        },
        {
            "name": "cloud_only_route_locked",
            "status": "pass",
            "detail": "正式默认主线已锁定为北京区 OSS + 云剪唯一 assembly 主路径，不再接受 local assembly fallback。",
        },
    ]
    checks.extend(_cloud_assembly_checks(config))

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif missing:
        status = STATUS_BLOCKED
        blocked_reason = "缺少北京区 OSS + 云剪主路径前提：" + "、".join(missing)
    else:
        status = STATUS_SUCCESS
        blocked_reason = ""

    return {
        "gate_name": "assembly_gate",
        "status": status,
        "allow_execution": not dry_run and not missing,
        "blocked_reason": blocked_reason,
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "checks": checks,
        "notes": [
            "assembly Gate 负责标记正式默认主线的北京区 OSS + 云剪唯一主路径，不得再把本地 assembly 写成默认交付。",
            "manifest 是修正循环和复审的事实锚点，assembly 不得绕开 manifest 自由猜测。",
            "当前正式默认主线已经改为 cloud-only；缺密钥、缺云端参数、缺真实素材或缺 provider implementation 时必须如实 blocked，不得再用 local mp4 补位。",
        ],
    }


def build_manifest(
    input_path: pathlib.Path,
    video_spec: dict[str, Any],
    config: dict[str, Any],
    generation_gate: dict[str, Any],
    output_dir: pathlib.Path,
    dry_run: bool,
    tts_probe: dict[str, Any],
) -> dict[str, Any]:
    tts_baseline = _resolve_formal_tts_baseline(config)
    route_plan = build_presentation_route_plan(video_spec)
    segments: list[dict[str, Any]] = []
    cursor = 0.0
    for index, segment in enumerate(video_spec["segments"], start=1):
        start_seconds = round(cursor, 2)
        end_seconds = round(cursor + segment["planned_duration_seconds"], 2)
        segments.append(
            {
                "sequence": index,
                "segment_id": segment["segment_id"],
                "goal": segment["goal"],
                "voiceover_text": segment["voiceover_text"],
                "caption_text": segment["caption_text"],
                "visual_intent": segment["visual_intent"],
                "material_requirements": {
                    "needs_image": segment["needs_image"],
                    "needs_video": segment["needs_video"],
                    "allow_real_desktop_footage": segment[
                        "allow_real_desktop_footage"
                    ],
                    "carrier": segment["carrier"],
                    "asset_key": segment["asset_key"],
                    "asset_source": segment["asset_source"],
                },
                "presentation": {
                    "carrier": segment["carrier"],
                    "asset_key": segment["asset_key"],
                    "asset_source": segment["asset_source"],
                },
                "provider_plan": {
                    "tts_provider": _get_tts_provider_name(config),
                    "tts_api_route_family": _get_tts_api_route_family(config),
                    "tts_model": _nested_get(config, "tts", "model"),
                    "tts_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
                    "tts_resource_id": _nested_get(config, "tts", "resource_id"),
                    "image_model": _nested_get(config, "image_generation", "model"),
                    "video_model": _nested_get(config, "video_generation", "model"),
                    "general_video_model": _nested_get(config, "video_generation", "model"),
                    "portrait_detect_model": _nested_get(config, "portrait_detect", "model"),
                    "portrait_video_model": _nested_get(
                        config,
                        "portrait_video_generation",
                        "model",
                    ),
                    "visual_model_routes": _build_visual_model_routes(config),
                    "tts_baseline_profile": tts_baseline["profile_id"],
                },
                "task_slots": {
                    "voice_task_id": None,
                    "image_task_id": None,
                    "video_task_id": None,
                },
                "resource_slots": {
                    "voice_resource_id": None,
                    "image_resource_id": None,
                    "video_resource_id": None,
                },
                "output_slots": {
                    "voice_uri": None,
                    "subtitle_uri": None,
                    "visual_uri": None,
                },
                "timeline": {
                    "planned_start_seconds": start_seconds,
                    "planned_end_seconds": end_seconds,
                    "planned_duration_seconds": segment["planned_duration_seconds"],
                },
                "known_issues": [],
                "current_status": generation_gate["status"]
                if not dry_run
                else STATUS_PLANNED,
            }
        )
        cursor = end_seconds

    return {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "pipeline_kind": "formal_api_demo",
        "current_status": generation_gate["status"]
        if not dry_run
        else STATUS_PLANNED,
        "input_snapshot": {
            "input_path": str(input_path),
            "theme": video_spec["theme"],
            "hook": video_spec["hook"],
            "ending": video_spec["ending"],
            "segment_count": len(video_spec["segments"]),
        },
        "video_spec": {
            "theme": video_spec["theme"],
            "total_duration_seconds": video_spec["total_duration_seconds"],
            "aspect_ratio": video_spec["aspect_ratio"],
            "target_scenario": video_spec["target_scenario"],
            "target_user": video_spec["target_user"],
            "quality_requirements": video_spec["quality_requirements"],
            "route_profile": video_spec.get("route_profile", ""),
            "video_route_strategy": video_spec.get("video_route_strategy", ""),
            "route_reason": video_spec.get("route_reason", ""),
        },
        "presentation_routing": route_plan,
        "segments": segments,
        "provider_summary": {
            "provider": _nested_get(config, "provider", "name"),
            "tts_provider": _get_tts_provider_name(config),
            "region": _nested_get(config, "provider", "region"),
            "tts_baseline": tts_baseline,
            "models": {
                "tts_api_route_family": _get_tts_api_route_family(config),
                "tts": _nested_get(config, "tts", "model"),
                "tts_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
                "tts_resource_id": _nested_get(config, "tts", "resource_id"),
                "image_generation": _nested_get(config, "image_generation", "model"),
                "video_generation": _nested_get(config, "video_generation", "model"),
                "general_video_generation": _nested_get(config, "video_generation", "model"),
                "portrait_detect": _nested_get(config, "portrait_detect", "model"),
                "portrait_video_generation": _nested_get(
                    config,
                    "portrait_video_generation",
                    "model",
                ),
                "visual_model_routes": _build_visual_model_routes(config),
            },
        },
        "config_summary": {
            "assembly_mode": _nested_get(config, "assembly", "mode"),
            "subtitle_mode": _nested_get(config, "assembly", "subtitle_mode"),
            "output_dir": str(output_dir),
            "quality_gate": copy.deepcopy(config.get("quality_gate", {})),
        },
        "timeline": {
            "planned_total_duration_seconds": video_spec["total_duration_seconds"],
            "planned_segment_count": len(segments),
        },
        "status_summary": {
            "generation": generation_gate["status"] if not dry_run else STATUS_PLANNED,
            "local_assembly": STATUS_NOT_STARTED,
            "cloud_assembly": STATUS_NOT_STARTED,
            "overall_status": generation_gate["status"] if not dry_run else STATUS_PLANNED,
        },
        "generation": {
            "status": generation_gate["status"] if not dry_run else STATUS_PLANNED,
            "task_id": None,
            "resource_id": None,
            "output_id": None,
            "tts_baseline": tts_baseline,
            "tts_probe": tts_probe,
            "voiceover": build_default_voiceover_generation(video_spec, config),
            "captions": build_default_caption_assets(video_spec),
            "visual_generation": build_default_visual_generation(video_spec, config),
        },
        "assembly": {
            "status": STATUS_NOT_STARTED,
            "task_id": None,
            "resource_id": None,
            "output_id": None,
            "delivery_mode": "oss_cloud_assembly",
            "delivery_video_path": None,
            "local": build_default_local_assembly(output_dir),
            "cloud": {
                "status": STATUS_NOT_STARTED,
                "blocked_reason": "",
                "missing_prerequisites": [],
                "missing_implementations": [],
                "is_primary_path": True,
                "target": build_cloud_assembly_target(config),
            },
            "preview": build_default_assembly_preview(output_dir),
        },
        "known_issues": _gate_known_issues(generation_gate),
        "machine_gate": {
            "generation_gate": generation_gate,
            "assembly_gate": {
                "gate_name": "assembly_gate",
                "status": STATUS_NOT_STARTED,
                "allow_execution": False,
                "blocked_reason": "",
                "missing_prerequisites": [],
                "missing_implementations": [],
                "checks": [],
                "notes": [],
            },
        },
    }


def build_generation_result_summary(
    manifest: dict[str, Any],
    generation_gate: dict[str, Any],
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    tts_probe = manifest.get("generation", {}).get("tts_probe", {})
    voiceover = manifest.get("generation", {}).get("voiceover", {})
    captions = manifest.get("generation", {}).get("captions", {})
    visual_generation = manifest.get("generation", {}).get("visual_generation", {})
    visual_assets = [
        asset.get("video_asset_path") or asset.get("image_asset_path")
        for asset in visual_generation.get("segment_assets", [])
        if asset.get("video_asset_path") or asset.get("image_asset_path")
    ]
    status = STATUS_PLANNED if dry_run else manifest.get("generation", {}).get("status", generation_gate["status"])
    cloud_visual = visual_generation.get("cloud", {})
    return {
        "schema_version": RESULT_SUMMARY_SCHEMA_VERSION,
        "stage": "generation",
        "overall_status": status,
        "generation_status": status,
        "assembly_status": STATUS_NOT_STARTED,
        "local_assembly_status": STATUS_NOT_STARTED,
        "cloud_assembly_status": STATUS_NOT_STARTED,
        "tts_probe_status": tts_probe.get("status", STATUS_NOT_STARTED),
        "voiceover_status": voiceover.get("status", STATUS_NOT_STARTED),
        "captions_status": captions.get("status", STATUS_NOT_STARTED),
        "visual_generation_status": visual_generation.get("status", STATUS_NOT_STARTED),
        "cloud_visual_generation_status": cloud_visual.get("status", STATUS_NOT_STARTED),
        "failure_reason": (
            voiceover.get("failure_reason")
            or visual_generation.get("failure_reason")
            or tts_probe.get("failure_reason", "")
        ),
        "error_message": (
            voiceover.get("error_message")
            or visual_generation.get("error_message")
            or visual_generation.get("blocked_reason")
            or tts_probe.get("error_message", "")
        ),
        "machine_gate_result": {
            "generation_gate": generation_gate["status"],
            "assembly_gate": STATUS_NOT_STARTED,
        },
        "blocked_reason": ""
        if dry_run
        else (
            tts_probe.get("blocked_reason")
            or voiceover.get("blocked_reason")
            or visual_generation.get("blocked_reason")
            or generation_gate.get("blocked_reason", "")
        ),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "generation_gate": str(output_dir / "generation_gate.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "route_plan": str(output_dir / "route_plan.json"),
            "tts_audio": tts_probe.get("audio_path"),
            "voiceover_audio": voiceover.get("audio_path"),
            "script": captions.get("script_path"),
            "captions": captions.get("captions_path"),
            "visual_plan": visual_generation.get("plan_path"),
            "preview_storyboard": visual_generation.get("preview_storyboard_path"),
            "visual_assets": visual_assets,
        },
        "rotation_summary": {
            "tts_candidate_pool": tts_probe.get("candidate_pool", {}),
            "tts_fallback_events": tts_probe.get("fallback_events", []),
            "tts_selected_candidate_id": tts_probe.get("selected_candidate_id", ""),
            "voiceover_last_success_candidate_id": voiceover.get("last_success_candidate_id", ""),
            "visual_candidate_pool": visual_generation.get("candidate_pool", {}),
        },
        "next_action_hint": _generation_next_action_hint(generation_gate, tts_probe, dry_run),
        "current_missing_prerequisites": generation_gate["missing_prerequisites"],
        "current_missing_implementations": generation_gate["missing_implementations"],
        "cloud_missing_prerequisites": cloud_visual.get("missing_prerequisites", []),
        "known_issues": manifest["known_issues"],
    }


def build_assembly_plan(
    manifest: dict[str, Any],
    config: dict[str, Any],
    assembly_gate: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema_version": "formal_api_demo_assembly_plan/v1",
        "manifest_schema_version": manifest.get("schema_version"),
        "assembly_mode": _nested_get(config, "assembly", "mode"),
        "subtitle_mode": _nested_get(config, "assembly", "subtitle_mode"),
        "resolution": _nested_get(config, "assembly", "resolution"),
        "fps": _nested_get(config, "assembly", "fps"),
        "segments": [
            {
                "segment_id": segment["segment_id"],
                "carrier": _nested_get(segment, "presentation", "carrier"),
                "asset_source": _nested_get(segment, "presentation", "asset_source"),
                "asset_key": _nested_get(segment, "presentation", "asset_key"),
                "planned_duration_seconds": segment["timeline"][
                    "planned_duration_seconds"
                ],
                "needs_subtitle": True,
                "needs_visual_asset": True,
                "voice_uri": segment["output_slots"].get("voice_uri"),
                "subtitle_uri": segment["output_slots"].get("subtitle_uri"),
                "visual_uri": segment["output_slots"].get("visual_uri"),
            }
            for segment in manifest.get("segments", [])
        ],
        "gate_status": assembly_gate["status"],
        "cloud_target": build_cloud_assembly_target(config),
        "legacy_local_preview_target": str(pathlib.Path(_nested_get(config, "output", "dist_dir") or DEFAULT_FORMAL_OUTPUT_DIR) / "assembly" / "formal_api_demo_preview.mp4"),
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run=True),
    }


def build_assembly_result_summary(
    manifest: dict[str, Any],
    assembly_gate: dict[str, Any],
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    generation_status = manifest.get("generation", {}).get("status", STATUS_NOT_STARTED)
    assembly = manifest.get("assembly", {})
    local = assembly.get("local", {})
    cloud = assembly.get("cloud", {})
    preview = assembly.get("preview", {})
    assembly_status = STATUS_PLANNED if dry_run else assembly.get("status", STATUS_NOT_STARTED)
    local_status = STATUS_PLANNED if dry_run else local.get("status", STATUS_NOT_STARTED)
    cloud_status = STATUS_PLANNED if dry_run else cloud.get("status", assembly_gate["status"])
    overall_status = _combine_stage_statuses(
        [
            generation_status,
            assembly_status,
        ],
        dry_run=dry_run,
    )
    return {
        "schema_version": RESULT_SUMMARY_SCHEMA_VERSION,
        "stage": "assembly",
        "overall_status": overall_status,
        "generation_status": generation_status,
        "assembly_status": assembly_status,
        "local_assembly_status": local_status,
        "cloud_assembly_status": cloud_status,
        "assembly_preview_status": preview.get("status", STATUS_NOT_STARTED),
        "delivery_mode": assembly.get("delivery_mode"),
        "machine_gate_result": {
            "generation_gate": manifest.get("machine_gate", {})
            .get("generation_gate", {})
            .get("status", STATUS_NOT_STARTED),
            "assembly_gate": assembly_gate["status"],
        },
        "blocked_reason": ""
        if dry_run
        else (
            cloud.get("blocked_reason")
            or cloud.get("error_message")
            or (assembly_gate.get("blocked_reason", "") if overall_status == STATUS_BLOCKED else "")
        ),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "assembly_gate": str(output_dir / "assembly_gate.json"),
            "assembly_plan": str(output_dir / "assembly_plan.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "route_plan": str(output_dir / "route_plan.json"),
            "final_video": assembly.get("delivery_video_path") if assembly_status == STATUS_SUCCESS else None,
            "preview_video": preview.get("video_path"),
            "preview_manifest": preview.get("preview_manifest_path"),
        },
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run),
        "current_missing_prerequisites": []
        if overall_status == STATUS_SUCCESS
        else cloud.get("missing_prerequisites", assembly_gate["missing_prerequisites"]),
        "current_missing_implementations": []
        if overall_status == STATUS_SUCCESS
        else cloud.get("missing_implementations", assembly_gate["missing_implementations"]),
        "cloud_missing_prerequisites": cloud.get("missing_prerequisites", assembly_gate["missing_prerequisites"]),
        "known_issues": manifest.get("known_issues", []),
    }


def build_default_voiceover_generation(
    video_spec: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    return {
        "status": STATUS_PLANNED,
        "baseline_profile": _resolve_formal_tts_baseline(config),
        "audio_path": None,
        "segment_audio_paths": [],
        "segment_results": [
            {
                "segment_id": segment["segment_id"],
                "status": STATUS_NOT_STARTED,
                "audio_path": None,
                "request_id": None,
                "failure_reason": "",
                "error_message": "",
            }
            for segment in video_spec.get("segments", [])
        ],
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "current_missing_prerequisites": [],
        "fallback_events": [],
        "last_success_candidate_id": "",
    }


def build_default_caption_assets(video_spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "status": STATUS_PLANNED,
        "script_path": None,
        "captions_path": None,
        "timeline_path": None,
        "segment_count": len(video_spec.get("segments", [])),
    }


def build_default_visual_generation(
    video_spec: dict[str, Any],
    config: dict[str, Any],
) -> dict[str, Any]:
    visual_routes = _build_visual_model_routes(config)
    return {
        "status": STATUS_PLANNED,
        "delivery_mode": "api_generated_visual_assets_required",
        "provider": _nested_get(config, "provider", "name"),
        "image_model": visual_routes["image_generation"]["model"],
        "video_model": visual_routes["general_video_generation"]["model"],
        "general_video_generation": {
            "status": STATUS_NOT_STARTED,
            **copy.deepcopy(visual_routes["general_video_generation"]),
            "blocked_reason": "",
        },
        "portrait_detect": {
            "status": STATUS_NOT_STARTED,
            **copy.deepcopy(visual_routes["portrait_detect"]),
            "blocked_reason": "",
        },
        "portrait_video_generation": {
            "status": STATUS_NOT_STARTED,
            **copy.deepcopy(visual_routes["portrait_video_generation"]),
            "blocked_reason": "",
        },
        "plan_path": None,
        "preview_storyboard_path": None,
        "segment_assets": [
            {
                "segment_id": segment["segment_id"],
                "carrier": segment.get("carrier", CARRIER_API_VISUAL),
                "asset_key": segment.get("asset_key", ""),
                "asset_source": segment.get("asset_source", API_GENERATED_SOURCE),
                "needs_image": segment["needs_image"],
                "needs_video": segment["needs_video"],
                "image_prompt": "",
                "video_prompt": "",
                "image_task_id": None,
                "video_task_id": None,
                "image_asset_path": None,
                "video_asset_path": None,
                "local_asset_path": None,
                "asset_origin": API_GENERATED_SOURCE,
                "failure_reason": "",
                "error_message": "",
                "status": STATUS_NOT_STARTED,
            }
            for segment in video_spec.get("segments", [])
        ],
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "current_missing_prerequisites": [],
        "missing_implementations": [],
        "candidate_pool": {},
        "cloud": {
            "status": STATUS_NOT_STARTED,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "missing_prerequisites": [],
            "missing_implementations": [],
        },
    }


def build_default_local_assembly(output_dir: pathlib.Path) -> dict[str, Any]:
    _ = output_dir
    return {
        "status": STATUS_NOT_STARTED,
        "video_path": None,
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "current_missing_prerequisites": [],
        "missing_implementations": [],
        "deprecated": True,
        "deprecated_reason": "正式默认主线已改为 cloud-only；local assembly 已移出主线，不再承担 fallback 或正常交付。",
    }


def build_default_assembly_preview(output_dir: pathlib.Path) -> dict[str, Any]:
    preview_dir = output_dir / "assembly"
    return {
        "status": STATUS_NOT_STARTED,
        "video_path": str(preview_dir / "formal_api_demo_preview.mp4"),
        "preview_manifest_path": str(preview_dir / "preview_manifest.json"),
        "captions_path": str(output_dir / "captions.srt"),
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "deprecated": True,
        "deprecated_reason": "local preview 只保留历史调试意义，已移出正式默认主线路由，不再作为 fallback / 验收路径。",
    }


def build_default_tts_probe(video_spec: dict[str, Any]) -> dict[str, Any]:
    probe_text, probe_text_source = _select_tts_probe_text(video_spec)
    return {
        "status": STATUS_PLANNED,
        "blocked_reason": "",
        "failure_reason": "",
        "http_status_code": None,
        "error_code": "",
        "error_message": "",
        "audio_path": None,
        "request_id": None,
        "provider": None,
        "api_route_family": None,
        "model_identifier": None,
        "probe_text": probe_text,
        "probe_text_source": probe_text_source,
        "voice": None,
        "used_endpoint_id": None,
        "used_model_id": None,
        "used_resource_id": None,
        "response_format": None,
        "request_debug": {},
        "current_missing_prerequisites": [],
        "candidate_pool": {},
        "fallback_events": [],
        "selected_candidate_id": "",
        "selected_candidate_label": "",
        "selected_voice": "",
        "failure_category": "",
        "resource_pool_exhausted": False,
    }


def apply_tts_probe_to_manifest(
    manifest: dict[str, Any],
    tts_probe: dict[str, Any],
    generation_gate: dict[str, Any],
) -> dict[str, Any]:
    manifest["generation"]["tts_probe"] = tts_probe
    manifest["generation"]["status"] = tts_probe.get("status", manifest["generation"]["status"])
    manifest["current_status"] = tts_probe.get("status", manifest["current_status"])
    manifest["known_issues"] = _merge_known_issues(
        _gate_known_issues(generation_gate),
        _tts_probe_known_issues(tts_probe),
    )
    if manifest.get("segments"):
        manifest["segments"][0]["output_slots"]["voice_uri"] = tts_probe.get("audio_path")
        manifest["segments"][0]["task_slots"]["voice_task_id"] = tts_probe.get("request_id")
        manifest["segments"][0]["current_status"] = tts_probe.get("status", manifest["segments"][0]["current_status"])
    return manifest


def apply_voiceover_to_manifest(
    manifest: dict[str, Any],
    voiceover: dict[str, Any],
) -> dict[str, Any]:
    manifest["generation"]["voiceover"] = voiceover
    for segment, segment_result in zip(
        manifest.get("segments", []),
        voiceover.get("segment_results", []),
    ):
        segment["output_slots"]["voice_uri"] = segment_result.get("audio_path")
        segment["task_slots"]["voice_task_id"] = segment_result.get("request_id")
        segment["current_status"] = segment_result.get("status", segment["current_status"])
    return manifest


def apply_caption_assets_to_manifest(
    manifest: dict[str, Any],
    caption_assets: dict[str, Any],
) -> dict[str, Any]:
    manifest["generation"]["captions"] = caption_assets
    for segment in manifest.get("segments", []):
        segment["output_slots"]["subtitle_uri"] = caption_assets.get("captions_path")
    return manifest


def apply_visual_generation_to_manifest(
    manifest: dict[str, Any],
    visual_generation: dict[str, Any],
) -> dict[str, Any]:
    manifest["generation"]["visual_generation"] = visual_generation
    for segment, asset in zip(
        manifest.get("segments", []),
        visual_generation.get("segment_assets", []),
    ):
        segment["task_slots"]["image_task_id"] = asset.get("image_task_id")
        segment["task_slots"]["video_task_id"] = asset.get("video_task_id")
        segment["output_slots"]["visual_uri"] = (
            asset.get("video_asset_path") or asset.get("image_asset_path")
        )
        segment.setdefault("presentation", {})["resolved_asset_origin"] = asset.get(
            "asset_origin",
            API_GENERATED_SOURCE,
        )
        segment["current_status"] = asset.get("status", segment["current_status"])
    return manifest


def execute_tts_probe(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
    *,
    probe_text: str | None = None,
    probe_text_source: str | None = None,
    output_stem: str = "voice_probe",
    tts_override: dict[str, Any] | None = None,
    rotation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    probe = build_default_tts_probe(video_spec)
    if probe_text is not None:
        probe["probe_text"] = probe_text.strip()
        probe["probe_text_source"] = probe_text_source or "runtime_override"
    runtime_state = rotation_state or _build_default_rotation_state()
    candidates = _resolve_tts_candidate_pool(config)
    probe["candidate_pool"] = _summarize_tts_candidate_pool(candidates)
    ordered_candidates = _ordered_runtime_candidates(
        candidates,
        runtime_state=runtime_state,
        resource_kind=RESOURCE_KIND_TTS,
        missing_fn=lambda candidate: _tts_candidate_missing_prerequisites(candidate),
    )
    if not ordered_candidates:
        probe.update(
            {
                "status": STATUS_BLOCKED,
                "blocked_reason": "TTS 资源池没有可用候选；请补齐候补 key / voice / provider。",
                "error_message": "TTS 资源池没有可用候选；请补齐候补 key / voice / provider。",
                "current_missing_prerequisites": ["tts_candidate_pool_exhausted"],
                "resource_pool_exhausted": True,
            }
        )
        return probe

    fallback_events: list[dict[str, Any]] = []
    for index, candidate in enumerate(ordered_candidates):
        effective_config = _build_effective_tts_config(config, candidate)
        attempt_result = _execute_tts_probe_once(
            probe=probe,
            config=effective_config,
            output_dir=output_dir,
            output_stem=output_stem,
            tts_override=tts_override,
        )
        failure_category = _categorize_tts_probe_failure(attempt_result)
        remaining_candidate_count = max(0, len(ordered_candidates) - index - 1)
        if attempt_result.get("status") == STATUS_SUCCESS:
            attempt_result.update(
                {
                    "candidate_pool": probe["candidate_pool"],
                    "fallback_events": fallback_events,
                    "selected_candidate_id": candidate["candidate_id"],
                    "selected_candidate_label": candidate["label"],
                    "selected_voice": candidate.get("voice") or "",
                    "failure_category": "",
                    "resource_pool_exhausted": False,
                }
            )
            runtime_state.setdefault("last_success", {})[RESOURCE_KIND_TTS] = candidate["candidate_id"]
            return attempt_result

        next_candidate_id = (
            ordered_candidates[index + 1]["candidate_id"]
            if remaining_candidate_count
            else ""
        )
        fallback_events.append(
            {
                "resource_kind": RESOURCE_KIND_TTS,
                "from_candidate_id": candidate["candidate_id"],
                "from_provider": candidate["provider"],
                "from_voice": "" if _is_missing_secret(candidate.get("voice")) else candidate.get("voice"),
                "reason_category": failure_category,
                "reason": attempt_result.get("error_message") or attempt_result.get("blocked_reason") or "",
                "switch_to_candidate_id": next_candidate_id,
                "remaining_candidate_count": remaining_candidate_count,
            }
        )
        if _should_disable_tts_candidate(failure_category):
            _disable_runtime_candidate(
                runtime_state,
                resource_kind=RESOURCE_KIND_TTS,
                candidate_id=candidate["candidate_id"],
                reason=failure_category,
            )
        if remaining_candidate_count:
            continue
        attempt_result.update(
            {
                "candidate_pool": probe["candidate_pool"],
                "fallback_events": fallback_events,
                "selected_candidate_id": candidate["candidate_id"],
                "selected_candidate_label": candidate["label"],
                "selected_voice": "" if _is_missing_secret(candidate.get("voice")) else candidate.get("voice"),
                "failure_category": failure_category,
                "resource_pool_exhausted": True,
                "blocked_reason": (
                    attempt_result.get("blocked_reason")
                    or attempt_result.get("error_message")
                    or "TTS 资源池已耗尽，没有可继续切换的候选。"
                ),
            }
        )
        return attempt_result

    return probe


def _execute_tts_probe_once(
    *,
    probe: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
    output_stem: str,
    tts_override: dict[str, Any] | None,
) -> dict[str, Any]:
    attempt_probe = copy.deepcopy(probe)
    route_family = _get_tts_api_route_family(config)
    model_identifier = _get_tts_model_identifier(config, route_family=route_family)
    base_url = _build_tts_base_url(config, route_family)
    response_format = (_nested_get(config, "tts", "response_format") or "mp3").strip() or "mp3"
    tts_options = _resolve_tts_runtime_options(config, tts_override=tts_override)
    audio_path = output_dir / "tts" / f"{output_stem}.{response_format}"
    attempt_probe.update(
        {
            "provider": _get_tts_provider_name(config, route_family=route_family),
            "api_route_family": route_family,
            "model_identifier": model_identifier,
            "voice": tts_options["voice"],
            "used_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
            "used_model_id": _nested_get(config, "tts", "model"),
            "used_resource_id": _nested_get(config, "tts", "resource_id"),
            "response_format": response_format,
            "request_debug": _build_tts_request_debug(
                config=config,
                route_family=route_family,
                base_url=base_url,
                model_identifier=model_identifier,
                response_format=response_format,
                effective_voice=tts_options["voice"],
                style=tts_options["style"],
                instruction=tts_options["instruction"],
                speech_rate=tts_options["speech_rate"],
                pitch_rate=tts_options["pitch_rate"],
                volume=tts_options["volume"],
            ),
        }
    )

    try:
        if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
            raise RuntimeError(
                "doubao_openspeech_v3 provider implementation 尚未接入，当前不应直接发起真实 probe。"
            )
        if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
            request_id = _execute_aliyun_bailian_tts_probe(
                config=config,
                probe=attempt_probe,
                audio_path=audio_path,
                base_url=base_url,
                model_identifier=model_identifier,
                response_format=response_format,
                tts_options=tts_options,
            )
            attempt_probe.update(
                {
                    "status": STATUS_SUCCESS,
                    "audio_path": str(audio_path),
                    "request_id": request_id,
                }
            )
            return attempt_probe

        client = OpenAI(
            api_key=_nested_get(config, "auth", "api_key"),
            base_url=base_url,
        )
        request_kwargs: dict[str, Any] = {
            "model": model_identifier,
            "voice": tts_options["voice"],
            "input": attempt_probe["probe_text"],
            "response_format": response_format,
        }
        style = tts_options["style"]
        if style:
            request_kwargs["extra_body"] = {"style": style}

        with client.audio.speech.with_streaming_response.create(**request_kwargs) as response:
            audio_path.parent.mkdir(parents=True, exist_ok=True)
            response.stream_to_file(str(audio_path))
            if not audio_path.exists() or audio_path.stat().st_size == 0:
                raise TtsRequestError(
                    "tts probe audio file missing or empty after provider response",
                    error_code="TtsAudioFileMissing",
                )
            attempt_probe.update(
                {
                    "status": STATUS_SUCCESS,
                    "audio_path": str(audio_path),
                    "request_id": _extract_request_id(response),
                }
            )
    except Exception as exc:  # pragma: no cover - exercised in integration path.
        status, failure_reason, http_status_code, error_code, error_message = _classify_tts_exception(
            exc, config
        )
        attempt_probe.update(
            {
                "status": status,
                "blocked_reason": error_message if status == STATUS_BLOCKED else "",
                "failure_reason": failure_reason,
                "http_status_code": http_status_code,
                "error_code": error_code,
                "error_message": error_message,
            }
        )
    return attempt_probe


def _ordered_runtime_candidates(
    candidates: list[dict[str, Any]],
    *,
    runtime_state: dict[str, Any],
    resource_kind: str,
    missing_fn: Any,
) -> list[dict[str, Any]]:
    disabled = runtime_state.get("disabled_candidates", {}).get(resource_kind, {})
    last_success = runtime_state.get("last_success", {}).get(resource_kind)
    eligible = [
        candidate
        for candidate in candidates
        if candidate.get("candidate_id") not in disabled and not missing_fn(candidate)
    ]
    return sorted(
        eligible,
        key=lambda candidate: (
            0 if candidate.get("candidate_id") == last_success else 1,
            candidate.get("priority", 999),
            candidate.get("candidate_id", ""),
        ),
    )


def _build_effective_tts_config(config: dict[str, Any], candidate: dict[str, Any]) -> dict[str, Any]:
    effective = copy.deepcopy(config)
    _nested_set(effective, "provider", "name", value=candidate.get("provider"))
    _nested_set(effective, "provider", "region", value=candidate.get("region"))
    _nested_set(effective, "auth", "api_key", value=candidate.get("api_key"))
    _nested_set(effective, "auth", "app_id", value=candidate.get("app_id"))
    _nested_set(effective, "tts", "api_route_family", value=candidate.get("api_route_family"))
    _nested_set(effective, "tts", "model", value=candidate.get("model"))
    _nested_set(effective, "tts", "endpoint_id", value=candidate.get("endpoint_id"))
    _nested_set(effective, "tts", "resource_id", value=candidate.get("resource_id"))
    _nested_set(effective, "tts", "voice", value=candidate.get("voice"))
    _nested_set(effective, "tts", "style", value=candidate.get("style"))
    _nested_set(effective, "tts", "instruction", value=candidate.get("instruction"))
    _nested_set(effective, "tts", "speech_rate", value=candidate.get("speech_rate"))
    _nested_set(effective, "tts", "pitch_rate", value=candidate.get("pitch_rate"))
    _nested_set(effective, "tts", "volume", value=candidate.get("volume"))
    _nested_set(effective, "tts", "response_format", value=candidate.get("response_format"))
    return effective


def _categorize_tts_probe_failure(result: dict[str, Any]) -> str:
    http_status_code = result.get("http_status_code")
    message = (
        str(result.get("error_message") or result.get("blocked_reason") or "")
        .strip()
        .lower()
    )
    if http_status_code in {401, 403} or any(
        token in message
        for token in ("invalid key", "unauthorized", "forbidden", "auth", "authentication")
    ):
        return FAILURE_CATEGORY_AUTH
    if http_status_code == 429 or any(
        token in message
        for token in ("quota", "rate limit", "too many requests", "exhausted", "insufficient_quota")
    ):
        return FAILURE_CATEGORY_QUOTA
    if any(token in message for token in ("voice", "speaker")) and any(
        token in message
        for token in ("invalid", "not found", "unsupported", "unavailable", "illegal")
    ):
        return FAILURE_CATEGORY_VOICE
    if http_status_code in {404} and any(
        token in message for token in ("model", "endpoint", "resource", "route")
    ):
        return FAILURE_CATEGORY_CANDIDATE
    if http_status_code in {408, 500, 502, 503, 504} or any(
        token in message
        for token in (
            "timeout",
            "temporarily unavailable",
            "connection reset",
            "connection refused",
            "network",
            "unavailable",
        )
    ):
        return FAILURE_CATEGORY_TIMEOUT
    return FAILURE_CATEGORY_UNKNOWN


def _should_disable_tts_candidate(failure_category: str) -> bool:
    return failure_category in {
        FAILURE_CATEGORY_AUTH,
        FAILURE_CATEGORY_QUOTA,
        FAILURE_CATEGORY_VOICE,
        FAILURE_CATEGORY_CANDIDATE,
        FAILURE_CATEGORY_TIMEOUT,
    }


def _disable_runtime_candidate(
    runtime_state: dict[str, Any],
    *,
    resource_kind: str,
    candidate_id: str,
    reason: str,
) -> None:
    disabled = runtime_state.setdefault("disabled_candidates", {}).setdefault(resource_kind, {})
    disabled[candidate_id] = reason


def _build_effective_visual_config(
    config: dict[str, Any],
    candidate: dict[str, Any],
    *,
    resource_kind: str,
) -> dict[str, Any]:
    effective = copy.deepcopy(config)
    section_name = "image_generation" if resource_kind == RESOURCE_KIND_IMAGE else "video_generation"
    _nested_set(effective, "provider", "name", value=candidate.get("provider"))
    _nested_set(effective, "provider", "region", value=candidate.get("region"))
    _nested_set(effective, "auth", "api_key", value=candidate.get("api_key"))
    _nested_set(effective, section_name, "model", value=candidate.get("model"))
    return effective


def _categorize_visual_generation_failure(result: dict[str, Any]) -> str:
    http_status_code = result.get("http_status_code")
    message = (
        str(result.get("error_message") or result.get("blocked_reason") or "")
        .strip()
        .lower()
    )
    if http_status_code in {401, 403} or any(
        token in message
        for token in ("invalid key", "unauthorized", "forbidden", "auth", "authentication")
    ):
        return FAILURE_CATEGORY_AUTH
    if http_status_code == 429 or any(
        token in message
        for token in ("quota", "rate limit", "too many requests", "exhausted", "insufficient_quota")
    ):
        return FAILURE_CATEGORY_QUOTA
    if http_status_code in {404} and any(
        token in message for token in ("model", "route", "provider", "not found")
    ):
        return FAILURE_CATEGORY_CANDIDATE
    if http_status_code in {408, 500, 502, 503, 504} or any(
        token in message
        for token in (
            "timeout",
            "temporarily unavailable",
            "connection reset",
            "connection refused",
            "network",
            "unavailable",
        )
    ):
        return FAILURE_CATEGORY_TIMEOUT
    return FAILURE_CATEGORY_UNKNOWN


def _should_disable_visual_candidate(failure_category: str) -> bool:
    return failure_category in {
        FAILURE_CATEGORY_AUTH,
        FAILURE_CATEGORY_QUOTA,
        FAILURE_CATEGORY_CANDIDATE,
        FAILURE_CATEGORY_TIMEOUT,
    }


def execute_formal_voiceover_generation(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
    *,
    rotation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    voiceover = build_default_voiceover_generation(video_spec, config)
    segment_results: list[dict[str, Any]] = []
    segment_audio_paths: list[pathlib.Path] = []
    runtime_state = rotation_state or _build_default_rotation_state()

    for segment in video_spec.get("segments", []):
        probe = execute_tts_probe(
            video_spec=video_spec,
            config=config,
            output_dir=output_dir,
            probe_text=segment["voiceover_text"],
            probe_text_source=f"{segment['segment_id']}_voiceover",
            output_stem=f"segment_{segment['segment_id']}",
            rotation_state=runtime_state,
        )
        segment_result = {
            "segment_id": segment["segment_id"],
            "status": probe.get("status", STATUS_FAILED),
            "audio_path": probe.get("audio_path"),
            "request_id": probe.get("request_id"),
            "failure_reason": probe.get("failure_reason", ""),
            "error_message": probe.get("error_message", ""),
            "selected_candidate_id": probe.get("selected_candidate_id", ""),
            "fallback_events": probe.get("fallback_events", []),
        }
        segment_results.append(segment_result)
        if probe.get("status") != STATUS_SUCCESS:
            voiceover.update(
                {
                    "status": probe.get("status", STATUS_FAILED),
                    "segment_results": segment_results,
                    "segment_audio_paths": [str(path) for path in segment_audio_paths],
                    "blocked_reason": probe.get("blocked_reason", ""),
                    "failure_reason": probe.get("failure_reason", ""),
                    "error_message": probe.get("error_message", ""),
                    "fallback_events": probe.get("fallback_events", []),
                }
            )
            return voiceover
        audio_path = probe.get("audio_path")
        if audio_path:
            segment_audio_paths.append(pathlib.Path(audio_path))

    bundle_path = output_dir / "tts" / "formal_voiceover.mp3"
    concatenate_audio_files(segment_audio_paths, bundle_path)
    voiceover.update(
        {
            "status": STATUS_SUCCESS,
            "audio_path": str(bundle_path),
            "segment_audio_paths": [str(path) for path in segment_audio_paths],
            "segment_results": segment_results,
            "last_success_candidate_id": runtime_state.get("last_success", {}).get(RESOURCE_KIND_TTS, ""),
        }
    )
    return voiceover


def write_formal_script_and_captions(
    video_spec: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    script_path = output_dir / "script.txt"
    captions_path = output_dir / "captions.srt"
    timeline_path = output_dir / "timeline.json"

    script_lines: list[str] = []
    caption_rows: list[str] = []
    timeline_entries: list[dict[str, Any]] = []
    cursor = 0.0

    for index, segment in enumerate(video_spec.get("segments", []), start=1):
        start = round(cursor, 2)
        end = round(start + segment["planned_duration_seconds"], 2)
        script_lines.append(f"第{index}段：{segment['voiceover_text']}")
        caption_rows.extend(
            [
                str(index),
                f"{seconds_to_srt(start)} --> {seconds_to_srt(end)}",
                segment["caption_text"],
                "",
            ]
        )
        timeline_entries.append(
            {
                "segment_id": segment["segment_id"],
                "start_seconds": start,
                "end_seconds": end,
                "duration_seconds": segment["planned_duration_seconds"],
                "caption_text": segment["caption_text"],
            }
        )
        cursor = end

    script_path.write_text("\n".join(script_lines).strip() + "\n", encoding="utf-8")
    captions_path.write_text("\n".join(caption_rows).strip() + "\n", encoding="utf-8")
    write_json(timeline_path, {"segments": timeline_entries})
    return {
        "status": STATUS_SUCCESS,
        "script_path": str(script_path),
        "captions_path": str(captions_path),
        "timeline_path": str(timeline_path),
        "segment_count": len(timeline_entries),
    }


def build_visual_generation_plan(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
    visual_gate: dict[str, Any],
    *,
    rotation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    visual_generation = build_default_visual_generation(video_spec, config)
    plan_path = output_dir / "visual_generation_plan.json"
    preview_storyboard_path = output_dir / "preview_storyboard.json"
    segment_assets: list[dict[str, Any]] = []
    has_video_segments = False
    video_model = _nested_get(config, "video_generation", "model") or DEFAULT_GENERAL_VIDEO_MODEL
    video_requires_seed_image = _video_model_requires_seed_image(video_model)

    for index, segment in enumerate(video_spec.get("segments", []), start=1):
        uses_local_media = _segment_requires_local_media(segment)
        local_asset = None
        if uses_local_media:
            asset_key = segment.get("asset_key") or segment["segment_id"]
            local_asset = _resolve_footage_input(config, asset_key)
        api_human_segment = _segment_uses_api_human(segment)
        segment_needs_image = (
            not uses_local_media
            and (
                api_human_segment
                or segment["needs_image"]
                or (segment["needs_video"] and video_requires_seed_image)
            )
        )
        image_prompt = ""
        video_prompt = ""
        if uses_local_media and local_asset is not None:
            if _is_missing_secret(local_asset["local_path"]):
                visual_generation.update(
                    {
                        "status": STATUS_BLOCKED,
                        "blocked_reason": f"缺少 {segment.get('asset_key') or segment['segment_id']} 的本地真实素材路径。",
                        "error_message": f"缺少 {segment.get('asset_key') or segment['segment_id']} 的本地真实素材路径。",
                    }
                )
                _write_visual_generation_files(
                    visual_generation=visual_generation,
                    video_spec=video_spec,
                    plan_path=plan_path,
                    preview_storyboard_path=preview_storyboard_path,
                )
                return visual_generation
            local_path = pathlib.Path(local_asset["local_path"]).expanduser()
            if not local_path.exists():
                visual_generation.update(
                    {
                        "status": STATUS_BLOCKED,
                        "blocked_reason": f"找不到 {segment.get('asset_key') or segment['segment_id']} 的本地真实素材文件：{local_path}",
                        "error_message": f"找不到 {segment.get('asset_key') or segment['segment_id']} 的本地真实素材文件：{local_path}",
                    }
                )
                _write_visual_generation_files(
                    visual_generation=visual_generation,
                    video_spec=video_spec,
                    plan_path=plan_path,
                    preview_storyboard_path=preview_storyboard_path,
                )
                return visual_generation
            if (
                segment.get("carrier") == CARRIER_HUMAN
                and local_asset["verified_role"] != FOOTAGE_ROLE_HUMAN_ON_CAMERA
            ):
                asset_key = segment.get("asset_key") or segment["segment_id"]
                visual_generation.update(
                    {
                        "status": STATUS_BLOCKED,
                        "blocked_reason": (
                            f"{asset_key} 是 carrier=human 槽位，但本地配置未显式标记 "
                            'verified_role="human_on_camera"；屏幕录制不得静默占用人物槽位。'
                        ),
                        "error_message": (
                            f"{asset_key} 是 carrier=human 槽位，但本地配置未显式标记 "
                            'verified_role="human_on_camera"；屏幕录制不得静默占用人物槽位。'
                        ),
                    }
                )
                _write_visual_generation_files(
                    visual_generation=visual_generation,
                    video_spec=video_spec,
                    plan_path=plan_path,
                    preview_storyboard_path=preview_storyboard_path,
                )
                return visual_generation
            asset_record = {
                "segment_id": segment["segment_id"],
                "sequence": index,
                "carrier": segment.get("carrier", CARRIER_API_VISUAL),
                "asset_key": segment.get("asset_key", ""),
                "asset_source": segment.get("asset_source", API_GENERATED_SOURCE),
                "verified_role": local_asset["verified_role"],
                "needs_image": local_asset["media_kind"] == "image",
                "needs_video": local_asset["media_kind"] == "video",
                "seed_image_required": False,
                "image_prompt": "",
                "video_prompt": "",
                "image_task_id": None,
                "video_task_id": None,
                "image_asset_path": str(local_path) if local_asset["media_kind"] == "image" else None,
                "video_asset_path": str(local_path) if local_asset["media_kind"] == "video" else None,
                "local_asset_path": str(local_path),
                "asset_origin": USER_MEDIA_SOURCE,
                "preview_visual_ref": f"preview_slide_{index}",
                "failure_reason": "",
                "error_message": "",
                "status": STATUS_SUCCESS,
            }
            segment_assets.append(asset_record)
            continue
        if segment_needs_image:
            if api_human_segment:
                if segment["segment_id"] == "seg01":
                    image_prompt = (
                        "9:16 竖版，东亚职场创作者面对镜头，半身构图，固定背景，"
                        "眼神稳定，语气克制但有判断感，真实摄影质感，像在给团队下判断。"
                        "不要大字，不要卡片感，不要课件感，不要夸张动作。"
                    )
                else:
                    image_prompt = (
                        "9:16 竖版，同一位东亚职场创作者面对镜头做结尾收束，半身构图，固定背景，"
                        "有轻微点头和收束手势，真实摄影质感，像在强调最小行动。"
                        "不要大字，不要卡片感，不要课件感，不要夸张动作。"
                    )
            elif segment["segment_id"] == "seg01":
                image_prompt = (
                    f"{segment['visual_intent']}。9:16 竖版，真实工作台 / 白板视角，"
                    "让人一眼看出信息很多但流程没有拉齐；纪录片式案例讲解画面，"
                    "不要 PPT 模板，不要广告感，不要人物正脸，不要大段字幕。"
                )
            elif segment["segment_id"] == "seg02":
                image_prompt = (
                    f"{segment['visual_intent']}。9:16 竖版，单一主镜头的起始状态，"
                    "桌面上散着目标、输入、口径、素材便签和断开的箭头，"
                    "看起来很忙但没人能接；不要 PPT，不要广告感，不要人物正脸。"
                )
            else:
                image_prompt = (
                    f"{segment['visual_intent']}。9:16 竖版，结构已经收束，"
                    "SOP 看板旁边带样片缩略图和修正清单，像真实项目收口画面；"
                    "不要 PPT 模板，不要广告感，不要人物正脸。"
                )
        if segment["needs_video"] and not api_human_segment:
            has_video_segments = True
            video_prompt = (
                f"{segment['visual_intent']}。9:16 竖版，单一固定镜头里，"
                "目标、输入、口径、素材这些散乱便签从画面四周被吸附、整理、归位，"
                "依次进入同一张 SOP 表单的字段槽位，最后形成清晰的可交接链路，"
                "画面末尾要出现明确的“可交接”状态条；不要分屏，不要 PPT，"
                "不要广告感，不要人物正脸，不要大段说明字幕。"
            )
        segment_assets.append(
            {
                "segment_id": segment["segment_id"],
                "sequence": index,
                "carrier": segment.get("carrier", CARRIER_API_VISUAL),
                "asset_key": segment.get("asset_key", ""),
                "asset_source": segment.get("asset_source", API_GENERATED_SOURCE),
                "needs_image": segment_needs_image,
                "needs_video": segment["needs_video"],
                "seed_image_required": segment["needs_video"] and video_requires_seed_image,
                "image_prompt": image_prompt,
                "video_prompt": video_prompt,
                "image_task_id": None,
                "video_task_id": None,
                "image_asset_path": None,
                "video_asset_path": None,
                "local_asset_path": None,
                "asset_origin": API_GENERATED_SOURCE,
                "preview_visual_ref": f"preview_slide_{index}",
                "failure_reason": "",
                "error_message": "",
                "status": STATUS_NOT_STARTED,
            }
        )

    visual_generation.update(
        {
            "plan_path": str(plan_path),
            "preview_storyboard_path": str(preview_storyboard_path),
            "segment_assets": segment_assets,
            "candidate_pool": visual_gate.get("candidate_pool", {}),
        }
    )

    if visual_gate["status"] != STATUS_SUCCESS:
        visual_status = visual_gate["status"]
        visual_blocked_reason = visual_gate.get("blocked_reason", "") or (
            "当前只生成 visual plan / preview storyboard；真实图片 / 视频 API 产物尚未落出，"
            "generation 不得写成 success。"
        )
        for asset in segment_assets:
            asset["status"] = visual_status
            asset["error_message"] = visual_blocked_reason
        visual_generation.update(
            {
                "status": visual_status,
                "delivery_mode": "auxiliary_plan_and_storyboard_only",
                "blocked_reason": visual_blocked_reason if visual_status == STATUS_BLOCKED else "",
                "failure_reason": visual_gate.get("failure_reason", "")
                if visual_status == STATUS_FAILED
                else "",
                "error_message": visual_blocked_reason,
                "current_missing_prerequisites": list(
                    visual_gate.get("missing_prerequisites", [])
                ),
                "missing_implementations": list(
                    visual_gate.get("missing_implementations", [])
                ),
                "cloud": {
                    "status": visual_status,
                    "blocked_reason": visual_blocked_reason if visual_status == STATUS_BLOCKED else "",
                    "failure_reason": visual_gate.get("failure_reason", "")
                    if visual_status == STATUS_FAILED
                    else "",
                    "error_message": visual_blocked_reason,
                    "missing_prerequisites": visual_gate.get("missing_prerequisites", []),
                    "missing_implementations": visual_gate.get("missing_implementations", []),
                },
            }
        )
        visual_generation["general_video_generation"].update(
            {
                "status": visual_status
                if visual_generation["general_video_generation"]["enabled"] and has_video_segments
                else STATUS_SKIPPED,
                "blocked_reason": visual_blocked_reason
                if visual_status == STATUS_BLOCKED
                and visual_generation["general_video_generation"]["enabled"]
                and has_video_segments
                else "",
                "failure_reason": visual_generation["failure_reason"]
                if visual_status == STATUS_FAILED
                and visual_generation["general_video_generation"]["enabled"]
                and has_video_segments
                else "",
                "error_message": visual_blocked_reason
                if visual_generation["general_video_generation"]["enabled"] and has_video_segments
                else "",
            }
        )
        visual_generation["portrait_detect"].update(
            {
                "status": STATUS_BLOCKED
                if visual_generation["portrait_detect"]["enabled"]
                else STATUS_SKIPPED,
                "blocked_reason": (
                    "liveportrait-detect 是真人开口分支前置检测；当前 provider implementation 尚未接入。"
                    if visual_generation["portrait_detect"]["enabled"]
                    else ""
                ),
            }
        )
        visual_generation["portrait_video_generation"].update(
            {
                "status": STATUS_BLOCKED
                if visual_generation["portrait_video_generation"]["enabled"]
                else STATUS_SKIPPED,
                "blocked_reason": (
                    "liveportrait 属于固定背景 / 人物开口分支，执行前必须先过 liveportrait-detect；"
                    "当前 provider implementation 尚未接入。"
                    if visual_generation["portrait_video_generation"]["enabled"]
                    else ""
                ),
            }
        )
        _write_visual_generation_files(
            visual_generation=visual_generation,
            video_spec=video_spec,
            plan_path=plan_path,
            preview_storyboard_path=preview_storyboard_path,
        )
        return visual_generation

    visual_generation.update(
        {
            "status": STATUS_SUCCESS,
            "delivery_mode": "api_generated_local_assets",
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "current_missing_prerequisites": [],
            "missing_implementations": [],
            "cloud": {
                "status": STATUS_SUCCESS,
                "blocked_reason": "",
                "failure_reason": "",
                "error_message": "",
                "missing_prerequisites": [],
                "missing_implementations": [],
            },
        }
    )
    portrait_route_in_use = (
        visual_generation["portrait_video_generation"]["enabled"]
        and any(
            asset.get("carrier") == CARRIER_HUMAN
            and asset.get("asset_origin") != USER_MEDIA_SOURCE
            and asset.get("needs_video")
            for asset in segment_assets
        )
    )
    visual_generation["general_video_generation"].update(
        {
            "status": STATUS_SKIPPED
            if not any(
                asset.get("needs_video")
                and asset.get("asset_origin") != USER_MEDIA_SOURCE
                and asset.get("carrier") != CARRIER_HUMAN
                for asset in segment_assets
            )
            else STATUS_NOT_STARTED,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
        }
    )
    visual_generation["portrait_detect"].update(
        {
            "status": STATUS_NOT_STARTED if portrait_route_in_use else STATUS_SKIPPED,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "request_id": None,
            "source_image_url": None,
        }
    )
    visual_generation["portrait_video_generation"].update(
        {
            "status": STATUS_NOT_STARTED if portrait_route_in_use else STATUS_SKIPPED,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "task_id": None,
            "request_id": None,
            "asset_path": None,
            "source_image_url": None,
            "source_audio_url": None,
        }
    )
    runtime_state = rotation_state or _build_default_rotation_state()

    for segment, asset in zip(video_spec.get("segments", []), segment_assets):
        if asset.get("asset_origin") == USER_MEDIA_SOURCE:
            continue
        image_result = {
            "status": STATUS_SKIPPED,
            "task_id": None,
            "asset_path": None,
            "source_url": None,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "fallback_events": [],
            "selected_candidate_id": "",
        }
        video_result = {
            "status": STATUS_SKIPPED,
            "task_id": None,
            "asset_path": None,
            "source_url": None,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "fallback_events": [],
            "selected_candidate_id": "",
        }

        if asset["needs_image"]:
            image_result = _execute_aliyun_wan_image_generation(
                config=config,
                output_dir=output_dir,
                segment_id=segment["segment_id"],
                prompt=asset["image_prompt"],
                rotation_state=runtime_state,
            )
            asset["image_task_id"] = image_result["task_id"]
            asset["image_asset_path"] = image_result["asset_path"]
            asset["image_candidate_id"] = image_result.get("selected_candidate_id", "")
            asset["image_fallback_events"] = image_result.get("fallback_events", [])

        if asset["needs_video"]:
            use_portrait_route = (
                portrait_route_in_use
                and asset.get("carrier") == CARRIER_HUMAN
                and asset.get("asset_origin") != USER_MEDIA_SOURCE
            )
            if use_portrait_route:
                portrait_result = _execute_aliyun_liveportrait_video_generation(
                    config=config,
                    output_dir=output_dir,
                    segment_id=segment["segment_id"],
                    image_path=pathlib.Path(image_result["asset_path"] or ""),
                    audio_path=output_dir / "tts" / f"segment_{segment['segment_id']}.mp3",
                )
                video_result = {
                    "status": portrait_result["status"],
                    "task_id": portrait_result["generation"].get("task_id"),
                    "asset_path": portrait_result["generation"].get("asset_path"),
                    "blocked_reason": portrait_result["generation"].get("blocked_reason", ""),
                    "failure_reason": portrait_result["generation"].get("failure_reason", ""),
                    "error_message": portrait_result["generation"].get("error_message", ""),
                    "fallback_events": [],
                    "selected_candidate_id": "",
                }
                asset["video_task_id"] = portrait_result["generation"].get("task_id")
                asset["video_asset_path"] = portrait_result["generation"].get("asset_path")
                visual_generation["portrait_detect"].update(portrait_result["detect"])
                visual_generation["portrait_video_generation"].update(
                    portrait_result["generation"]
                )
            else:
                seed_image_url = None
                if asset.get("seed_image_required"):
                    seed_image_url = image_result.get("source_url")
                    if not seed_image_url and image_result.get("asset_path"):
                        seed_image_url = pathlib.Path(image_result["asset_path"]).resolve().as_uri()
                if asset.get("seed_image_required") and not seed_image_url:
                    video_result = {
                        "status": STATUS_BLOCKED,
                        "task_id": None,
                        "asset_path": None,
                        "source_url": None,
                        "blocked_reason": "wan2.7-i2v 缺少首帧图片输入，无法继续视频生成。",
                        "failure_reason": "i2v_seed_image_missing",
                        "error_message": "wan2.7-i2v 缺少首帧图片输入，无法继续视频生成。",
                        "fallback_events": [],
                        "selected_candidate_id": "",
                    }
                else:
                    video_result = _execute_aliyun_wan_video_generation(
                        config=config,
                        output_dir=output_dir,
                        segment_id=segment["segment_id"],
                        prompt=asset["video_prompt"],
                        duration_seconds=segment["planned_duration_seconds"],
                        seed_image_url=seed_image_url,
                        rotation_state=runtime_state,
                    )
                asset["video_task_id"] = video_result["task_id"]
                asset["video_asset_path"] = video_result["asset_path"]
                asset["video_candidate_id"] = video_result.get("selected_candidate_id", "")
                asset["video_fallback_events"] = video_result.get("fallback_events", [])
                visual_generation["general_video_generation"].update(
                    {
                        "status": video_result["status"],
                        "blocked_reason": video_result["blocked_reason"],
                        "failure_reason": video_result["failure_reason"],
                        "error_message": video_result["error_message"],
                    }
                )

        asset["status"] = _combine_stage_statuses(
            [image_result["status"], video_result["status"]],
            dry_run=False,
        )
        asset["failure_reason"] = (
            image_result["failure_reason"] or video_result["failure_reason"] or ""
        )
        asset["error_message"] = (
            image_result["error_message"]
            or image_result["blocked_reason"]
            or video_result["error_message"]
            or video_result["blocked_reason"]
            or ""
        )
        if asset["status"] != STATUS_SUCCESS:
            visual_generation.update(
                {
                    "status": asset["status"],
                    "blocked_reason": asset["error_message"]
                    if asset["status"] == STATUS_BLOCKED
                    else "",
                    "failure_reason": asset["failure_reason"]
                    if asset["status"] == STATUS_FAILED
                    else "",
                    "error_message": asset["error_message"],
                    "cloud": {
                        "status": asset["status"],
                        "blocked_reason": asset["error_message"]
                        if asset["status"] == STATUS_BLOCKED
                        else "",
                        "failure_reason": asset["failure_reason"]
                        if asset["status"] == STATUS_FAILED
                        else "",
                        "error_message": asset["error_message"],
                        "missing_prerequisites": [],
                        "missing_implementations": [],
                    },
                }
            )
            _write_visual_generation_files(
                visual_generation=visual_generation,
                video_spec=video_spec,
                plan_path=plan_path,
                preview_storyboard_path=preview_storyboard_path,
            )
            return visual_generation

    visual_generation["delivery_mode"] = _resolve_visual_delivery_mode(segment_assets)
    _write_visual_generation_files(
        visual_generation=visual_generation,
        video_spec=video_spec,
        plan_path=plan_path,
        preview_storyboard_path=preview_storyboard_path,
    )
    return visual_generation


def _write_visual_generation_files(
    *,
    visual_generation: dict[str, Any],
    video_spec: dict[str, Any],
    plan_path: pathlib.Path,
    preview_storyboard_path: pathlib.Path,
) -> None:
    write_json(
        plan_path,
        {
            "schema_version": "formal_api_demo_visual_plan/v1",
            "status": visual_generation["status"],
            "delivery_mode": visual_generation["delivery_mode"],
            "provider": visual_generation["provider"],
            "image_model": visual_generation["image_model"],
            "video_model": visual_generation["video_model"],
            "general_video_generation": visual_generation["general_video_generation"],
            "portrait_detect": visual_generation["portrait_detect"],
            "portrait_video_generation": visual_generation["portrait_video_generation"],
            "blocked_reason": visual_generation.get("blocked_reason", ""),
            "failure_reason": visual_generation.get("failure_reason", ""),
            "error_message": visual_generation.get("error_message", ""),
            "current_missing_prerequisites": visual_generation["current_missing_prerequisites"],
            "missing_implementations": visual_generation["missing_implementations"],
            "candidate_pool": visual_generation.get("candidate_pool", {}),
            "auxiliary_only": not _visual_delivery_is_primary_asset_mode(
                visual_generation["delivery_mode"]
            ),
            "cloud": visual_generation["cloud"],
            "segment_assets": visual_generation["segment_assets"],
        },
    )
    write_json(
        preview_storyboard_path,
        {
            "schema_version": "formal_api_demo_preview_storyboard/v1",
            "auxiliary_only": not _visual_delivery_is_primary_asset_mode(
                visual_generation["delivery_mode"]
            ),
            "segments": [
                {
                    "segment_id": segment["segment_id"],
                    "goal": segment["goal"],
                    "visual_intent": segment["visual_intent"],
                    "caption_text": segment["caption_text"],
                }
                for segment in video_spec.get("segments", [])
            ],
        },
    )


def _execute_aliyun_wan_image_generation(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    prompt: str,
    rotation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return _execute_aliyun_visual_generation_with_fallback(
        config=config,
        output_dir=output_dir,
        segment_id=segment_id,
        resource_kind=RESOURCE_KIND_IMAGE,
        prompt=prompt,
        duration_seconds=None,
        seed_image_url=None,
        rotation_state=rotation_state,
    )


def _video_model_requires_seed_image(model: str | None) -> bool:
    normalized = str(model or "").strip().lower()
    return normalized.endswith("-i2v") or normalized.endswith("_i2v")


def _build_aliyun_video_generation_payload(
    *,
    config: dict[str, Any],
    prompt: str,
    duration_seconds: float,
    seed_image_url: str | None = None,
) -> dict[str, Any]:
    model = _nested_get(config, "video_generation", "model") or DEFAULT_GENERAL_VIDEO_MODEL
    payload: dict[str, Any] = {
        "model": model,
        "input": {
            "prompt": prompt,
        },
        "parameters": {
            "size": "720*1280",
            "duration": max(2, int(round(duration_seconds))),
            "prompt_extend": True,
        },
    }
    if seed_image_url and _video_model_requires_seed_image(model):
        payload["input"]["img_url"] = seed_image_url
    return payload


def _execute_aliyun_wan_video_generation(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    prompt: str,
    duration_seconds: float,
    seed_image_url: str | None = None,
    rotation_state: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return _execute_aliyun_visual_generation_with_fallback(
        config=config,
        output_dir=output_dir,
        segment_id=segment_id,
        resource_kind=RESOURCE_KIND_VIDEO,
        prompt=prompt,
        duration_seconds=duration_seconds,
        seed_image_url=seed_image_url,
        rotation_state=rotation_state,
    )


def _execute_aliyun_visual_generation_with_fallback(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    resource_kind: str,
    prompt: str,
    duration_seconds: float | None,
    seed_image_url: str | None,
    rotation_state: dict[str, Any] | None,
) -> dict[str, Any]:
    runtime_state = rotation_state or _build_default_rotation_state()
    candidates = _resolve_visual_candidate_pool(config, resource_kind=resource_kind)
    summary = _summarize_visual_candidate_pool(
        candidates if resource_kind == RESOURCE_KIND_IMAGE else _resolve_visual_candidate_pool(config, resource_kind=RESOURCE_KIND_IMAGE),
        candidates if resource_kind == RESOURCE_KIND_VIDEO else _resolve_visual_candidate_pool(config, resource_kind=RESOURCE_KIND_VIDEO),
    )
    ordered_candidates = _ordered_runtime_candidates(
        candidates,
        runtime_state=runtime_state,
        resource_kind=resource_kind,
        missing_fn=lambda candidate: _visual_candidate_missing_prerequisites(candidate, resource_kind=resource_kind),
    )
    if not ordered_candidates:
        # Compatibility path: low-level helpers can still be called directly in
        # focused unit tests before gate checks run.
        ordered_candidates = candidates[:1]

    fallback_events: list[dict[str, Any]] = []
    for index, candidate in enumerate(ordered_candidates):
        effective_config = _build_effective_visual_config(config, candidate, resource_kind=resource_kind)
        if resource_kind == RESOURCE_KIND_IMAGE:
            payload = {
                "model": _nested_get(effective_config, "image_generation", "model") or DEFAULT_GENERAL_IMAGE_MODEL,
                "input": {
                    "messages": [
                        {
                            "role": "user",
                            "content": [{"text": prompt}],
                        }
                    ]
                },
                "parameters": {
                    "size": "720*1280",
                    "max_images": 1,
                    "enable_interleave": True,
                },
            }
            attempt_result = _execute_aliyun_visual_generation_task(
                config=effective_config,
                output_dir=output_dir,
                segment_id=segment_id,
                asset_kind="image",
                create_relative_path="/services/aigc/image-generation/generation",
                payload=payload,
                result_url_extractor=_extract_aliyun_image_result_url,
                default_extension=".png",
            )
        else:
            payload = _build_aliyun_video_generation_payload(
                config=effective_config,
                prompt=prompt,
                duration_seconds=duration_seconds or 0,
                seed_image_url=seed_image_url,
            )
            attempt_result = _execute_aliyun_visual_generation_task(
                config=effective_config,
                output_dir=output_dir,
                segment_id=segment_id,
                asset_kind="video",
                create_relative_path="/services/aigc/video-generation/video-synthesis",
                payload=payload,
                result_url_extractor=_extract_aliyun_video_result_url,
                default_extension=".mp4",
            )

        failure_category = _categorize_visual_generation_failure(attempt_result)
        remaining_candidate_count = max(0, len(ordered_candidates) - index - 1)
        if attempt_result.get("status") == STATUS_SUCCESS:
            attempt_result.update(
                {
                    "candidate_pool": summary.get(resource_kind, {}),
                    "fallback_events": fallback_events,
                    "selected_candidate_id": candidate["candidate_id"],
                    "selected_candidate_label": candidate["label"],
                    "resource_pool_exhausted": False,
                }
            )
            runtime_state.setdefault("last_success", {})[resource_kind] = candidate["candidate_id"]
            return attempt_result

        next_candidate_id = (
            ordered_candidates[index + 1]["candidate_id"]
            if remaining_candidate_count
            else ""
        )
        fallback_events.append(
            {
                "resource_kind": resource_kind,
                "from_candidate_id": candidate["candidate_id"],
                "from_provider": candidate["provider"],
                "reason_category": failure_category,
                "reason": attempt_result.get("error_message") or attempt_result.get("blocked_reason") or "",
                "switch_to_candidate_id": next_candidate_id,
                "remaining_candidate_count": remaining_candidate_count,
            }
        )
        if _should_disable_visual_candidate(failure_category):
            _disable_runtime_candidate(
                runtime_state,
                resource_kind=resource_kind,
                candidate_id=candidate["candidate_id"],
                reason=failure_category,
            )
        if remaining_candidate_count:
            continue
        attempt_result.update(
            {
                "candidate_pool": summary.get(resource_kind, {}),
                "fallback_events": fallback_events,
                "selected_candidate_id": candidate["candidate_id"],
                "selected_candidate_label": candidate["label"],
                "resource_pool_exhausted": True,
                "blocked_reason": (
                    attempt_result.get("blocked_reason")
                    or attempt_result.get("error_message")
                    or f"{resource_kind} 资源池已耗尽，没有可继续切换的候选。"
                ),
            }
        )
        return attempt_result

    return {
        "status": STATUS_BLOCKED,
        "task_id": None,
        "request_id": None,
        "asset_path": None,
        "source_url": None,
        "blocked_reason": f"{resource_kind} 资源池没有可用候选。",
        "failure_reason": f"{resource_kind}_candidate_pool_exhausted",
        "error_message": f"{resource_kind} 资源池没有可用候选。",
        "http_status_code": None,
        "error_code": "",
        "candidate_pool": summary.get(resource_kind, {}),
        "fallback_events": fallback_events,
        "selected_candidate_id": "",
        "resource_pool_exhausted": True,
    }


def _execute_aliyun_visual_generation_task_once(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    asset_kind: str,
    create_relative_path: str,
    payload: dict[str, Any],
    result_url_extractor: Any,
    default_extension: str,
) -> dict[str, Any]:
    task_id: str | None = None
    request_id: str | None = None
    try:
        create_request = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1" + create_relative_path,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
                "Content-Type": "application/json",
                "X-DashScope-Async": "enable",
            },
            method="POST",
        )
        try:
            create_payload = _urlopen_json_request(
                create_request,
                error_cls=VisualGenerationError,
                invalid_json_message=f"aliyun {asset_kind} create returned invalid JSON payload",
            )
        except VisualGenerationError as exc:
            if not exc.failure_reason:
                exc.failure_reason = f"aliyun_{asset_kind}_task_create_failed"
            raise
        task_id = _nested_get(create_payload, "output", "task_id")
        request_id = create_payload.get("request_id")
        if not task_id:
            raise VisualGenerationError(
                f"aliyun {asset_kind} create response missing task_id",
                failure_reason=f"aliyun_{asset_kind}_task_id_missing",
            )

        task_payload = _poll_aliyun_visual_task(
            config=config,
            task_id=task_id,
            asset_kind=asset_kind,
        )
        request_id = request_id or task_payload.get("request_id")
        result_url = result_url_extractor(task_payload)
        if not result_url:
            raise VisualGenerationError(
                f"aliyun {asset_kind} task succeeded but missing result url",
                failure_reason=f"aliyun_{asset_kind}_result_url_missing",
            )
        output_path = _build_visual_asset_output_path(
            output_dir=output_dir,
            segment_id=segment_id,
            asset_kind=asset_kind,
            source_url=result_url,
            default_extension=default_extension,
        )
        try:
            _download_binary_file(
                result_url,
                output_path,
                error_cls=VisualGenerationError,
                empty_error_message=f"aliyun {asset_kind} download is empty",
                empty_error_code=f"Aliyun{asset_kind.title()}Empty",
            )
        except VisualGenerationError as exc:
            if not exc.failure_reason:
                exc.failure_reason = f"aliyun_{asset_kind}_download_failed"
            raise
        return {
            "status": STATUS_SUCCESS,
            "task_id": task_id,
            "request_id": request_id,
            "asset_path": str(output_path),
            "source_url": result_url,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "http_status_code": None,
            "error_code": "",
        }
    except VisualGenerationError as exc:
        message = _sanitize_message(str(exc), config)
        return {
            "status": exc.status,
            "task_id": task_id,
            "request_id": request_id,
            "asset_path": None,
            "source_url": None,
            "blocked_reason": message if exc.status == STATUS_BLOCKED else "",
            "failure_reason": exc.failure_reason or "",
            "error_message": message,
            "http_status_code": exc.status_code,
            "error_code": exc.error_code or "",
        }


def _execute_aliyun_visual_generation_task(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    asset_kind: str,
    create_relative_path: str,
    payload: dict[str, Any],
    result_url_extractor: Any,
    default_extension: str,
) -> dict[str, Any]:
    return _execute_aliyun_visual_generation_task_once(
        config=config,
        output_dir=output_dir,
        segment_id=segment_id,
        asset_kind=asset_kind,
        create_relative_path=create_relative_path,
        payload=payload,
        result_url_extractor=result_url_extractor,
        default_extension=default_extension,
    )


def _poll_aliyun_visual_task(
    *,
    config: dict[str, Any],
    task_id: str,
    asset_kind: str,
) -> dict[str, Any]:
    interval_seconds = max(
        0.0,
        float(_nested_get(config, "polling", "interval_seconds") or 0),
    )
    timeout_seconds = max(
        0.0,
        float(_nested_get(config, "polling", "timeout_seconds") or 0),
    )
    deadline = time.monotonic() + timeout_seconds

    while True:
        task_request = urllib.request.Request(
            f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}",
            headers={
                "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
            },
            method="GET",
        )
        try:
            task_payload = _urlopen_json_request(
                task_request,
                error_cls=VisualGenerationError,
                invalid_json_message=f"aliyun {asset_kind} task poll returned invalid JSON payload",
            )
        except VisualGenerationError as exc:
            if not exc.failure_reason:
                exc.failure_reason = f"aliyun_{asset_kind}_task_poll_failed"
            raise
        task_status = str(_nested_get(task_payload, "output", "task_status") or "").upper()
        if task_status == "SUCCEEDED":
            return task_payload
        if task_status in {"FAILED", "UNKNOWN", "CANCELED", "CANCELLED"}:
            raise VisualGenerationError(
                _extract_aliyun_task_error_message(task_payload)
                or f"aliyun {asset_kind} task ended with status {task_status}",
                failure_reason=f"aliyun_{asset_kind}_task_failed",
            )
        if time.monotonic() >= deadline:
            raise VisualGenerationError(
                f"aliyun {asset_kind} task poll timeout: task_id={task_id}",
                status=STATUS_BLOCKED,
                failure_reason=f"aliyun_{asset_kind}_task_poll_timeout",
            )
        if interval_seconds > 0:
            time.sleep(interval_seconds)


def _extract_aliyun_task_error_message(task_payload: dict[str, Any]) -> str:
    return (
        _normalize_optional_text(_nested_get(task_payload, "output", "message"))
        or _normalize_optional_text(task_payload.get("message"))
        or _normalize_optional_text(_nested_get(task_payload, "output", "task_status_msg"))
        or ""
    )


def _extract_aliyun_image_result_url(task_payload: dict[str, Any]) -> str | None:
    output = task_payload.get("output", {})
    for choice in output.get("choices", []):
        content_items = _nested_get(choice, "message", "content") or []
        for item in content_items:
            if isinstance(item, dict) and item.get("image"):
                return str(item["image"])
    for item in output.get("results", []):
        if isinstance(item, dict) and item.get("url"):
            return str(item["url"])
        if isinstance(item, dict) and item.get("image"):
            return str(item["image"])
    return None


def _extract_aliyun_video_result_url(task_payload: dict[str, Any]) -> str | None:
    output = task_payload.get("output", {})
    if output.get("video_url"):
        return str(output["video_url"])
    for item in output.get("results", []):
        if isinstance(item, dict) and item.get("video_url"):
            return str(item["video_url"])
        if isinstance(item, dict) and item.get("url"):
            return str(item["url"])
    if isinstance(output.get("results"), dict) and output["results"].get("video_url"):
        return str(output["results"]["video_url"])
    return None


def _execute_aliyun_liveportrait_video_generation(
    *,
    config: dict[str, Any],
    output_dir: pathlib.Path,
    segment_id: str,
    image_path: pathlib.Path,
    audio_path: pathlib.Path,
) -> dict[str, Any]:
    detect_result = {
        "status": STATUS_NOT_STARTED,
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "request_id": None,
        "source_image_url": None,
    }
    generation_result = {
        "status": STATUS_NOT_STARTED,
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "task_id": None,
        "request_id": None,
        "asset_path": None,
        "source_image_url": None,
        "source_audio_url": None,
    }
    try:
        detect_result = _execute_aliyun_liveportrait_detect(
            config=config,
            image_path=image_path,
        )
        if detect_result["status"] != STATUS_SUCCESS:
            detect_message = (
                detect_result["blocked_reason"]
                or detect_result["error_message"]
            )
            generation_result.update(
                {
                    "status": detect_result["status"],
                    "blocked_reason": detect_result["blocked_reason"],
                    "failure_reason": detect_result["failure_reason"],
                    "error_message": detect_message,
                    "source_image_url": detect_result.get("source_image_url"),
                }
            )
            return {
                "status": detect_result["status"],
                "blocked_reason": detect_result["blocked_reason"],
                "failure_reason": detect_result["failure_reason"],
                "error_message": detect_message,
                "detect": detect_result,
                "generation": generation_result,
            }

        image_upload = _upload_file_to_aliyun_temp_storage(
            config=config,
            model=DEFAULT_PORTRAIT_VIDEO_MODEL,
            source_path=image_path,
        )
        audio_upload = _upload_file_to_aliyun_temp_storage(
            config=config,
            model=DEFAULT_PORTRAIT_VIDEO_MODEL,
            source_path=audio_path,
        )
        generation_result["source_image_url"] = image_upload["oss_url"]
        generation_result["source_audio_url"] = audio_upload["oss_url"]

        payload = {
            "model": _nested_get(config, "portrait_video_generation", "model")
            or DEFAULT_PORTRAIT_VIDEO_MODEL,
            "input": {
                "image_url": image_upload["oss_url"],
                "audio_url": audio_upload["oss_url"],
            },
            "parameters": {
                "template_id": "normal",
                "video_fps": 30,
                "paste_back": True,
            },
        }
        create_request = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/video-synthesis/",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        create_request.headers["X-DashScope-Async"] = "enable"
        create_request.headers["X-DashScope-OssResourceResolve"] = "enable"
        create_payload = _urlopen_json_request(
            create_request,
            error_cls=VisualGenerationError,
            invalid_json_message="aliyun liveportrait create returned invalid JSON payload",
        )
        task_id = _nested_get(create_payload, "output", "task_id")
        request_id = create_payload.get("request_id")
        if not task_id:
            raise VisualGenerationError(
                "aliyun liveportrait create response missing task_id",
                failure_reason="portrait_video_task_id_missing",
            )
        generation_result["task_id"] = task_id
        generation_result["request_id"] = request_id

        task_payload = _poll_aliyun_visual_task(
            config=config,
            task_id=task_id,
            asset_kind="portrait_video",
        )
        generation_result["request_id"] = request_id or task_payload.get("request_id")
        result_url = _extract_aliyun_video_result_url(task_payload)
        if not result_url:
            raise VisualGenerationError(
                "aliyun liveportrait task succeeded but missing result url",
                failure_reason="portrait_video_result_url_missing",
            )
        output_path = _build_visual_asset_output_path(
            output_dir=output_dir,
            segment_id=segment_id,
            asset_kind="video",
            source_url=result_url,
            default_extension=".mp4",
        )
        _download_binary_file(
            result_url,
            output_path,
            error_cls=VisualGenerationError,
            empty_error_message="aliyun liveportrait video download is empty",
            empty_error_code="AliyunLivePortraitEmptyVideo",
        )
        if not output_path.exists():
            raise VisualGenerationError(
                "liveportrait succeeded but local video file missing",
                failure_reason="portrait_video_local_file_missing",
            )
        generation_result.update(
            {
                "status": STATUS_SUCCESS,
                "blocked_reason": "",
                "failure_reason": "",
                "error_message": "",
                "asset_path": str(output_path),
            }
        )
        return {
            "status": STATUS_SUCCESS,
            "blocked_reason": "",
            "failure_reason": "",
            "error_message": "",
            "detect": detect_result,
            "generation": generation_result,
        }
    except VisualGenerationError as exc:
        message = _sanitize_message(str(exc), config)
        is_timeout = _looks_like_timeout_message(message)
        status = STATUS_BLOCKED if is_timeout else exc.status
        blocked_reason = _normalize_timeout_blocked_reason(message) if is_timeout else ""
        failure_reason = exc.failure_reason or (
            "portrait_video_timeout"
            if status == STATUS_BLOCKED
            else "portrait_video_generation_failed"
        )
        generation_result.update(
            {
                "status": status,
                "blocked_reason": blocked_reason if status == STATUS_BLOCKED else "",
                "failure_reason": failure_reason,
                "error_message": message,
            }
        )
        return {
            "status": status,
            "blocked_reason": generation_result["blocked_reason"],
            "failure_reason": generation_result["failure_reason"],
            "error_message": generation_result["error_message"],
            "detect": detect_result,
            "generation": generation_result,
        }


def _execute_aliyun_liveportrait_detect(
    *,
    config: dict[str, Any],
    image_path: pathlib.Path,
) -> dict[str, Any]:
    detect_result = {
        "status": STATUS_NOT_STARTED,
        "blocked_reason": "",
        "failure_reason": "",
        "error_message": "",
        "request_id": None,
        "source_image_url": None,
    }
    try:
        image_upload = _upload_file_to_aliyun_temp_storage(
            config=config,
            model=DEFAULT_PORTRAIT_DETECT_MODEL,
            source_path=image_path,
        )
        detect_result["source_image_url"] = image_upload["oss_url"]
        payload = {
            "model": _nested_get(config, "portrait_detect", "model")
            or DEFAULT_PORTRAIT_DETECT_MODEL,
            "input": {
                "image_url": image_upload["oss_url"],
            },
        }
        request = urllib.request.Request(
            "https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/face-detect",
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        request.headers["X-DashScope-OssResourceResolve"] = "enable"
        response_payload = _urlopen_json_request(
            request,
            error_cls=VisualGenerationError,
            invalid_json_message="aliyun liveportrait detect returned invalid JSON payload",
        )
        detect_result["request_id"] = response_payload.get("request_id")
        if _nested_get(response_payload, "output", "pass"):
            detect_result["status"] = STATUS_SUCCESS
            return detect_result
        message = _normalize_optional_text(_nested_get(response_payload, "output", "message")) or (
            "liveportrait-detect did not pass."
        )
        detect_result.update(
            {
                "status": STATUS_BLOCKED,
                "blocked_reason": message,
                "failure_reason": "portrait_detect_rejected",
                "error_message": message,
            }
        )
        return detect_result
    except VisualGenerationError as exc:
        message = _sanitize_message(str(exc), config)
        is_timeout = _looks_like_timeout_message(message)
        status = STATUS_BLOCKED if is_timeout else exc.status
        detect_result.update(
            {
                "status": status,
                "blocked_reason": _normalize_timeout_blocked_reason(message)
                if status == STATUS_BLOCKED and is_timeout
                else (message if status == STATUS_BLOCKED else ""),
                "failure_reason": exc.failure_reason
                or (
                    "portrait_detect_timeout"
                    if status == STATUS_BLOCKED
                    else "portrait_detect_request_failed"
                ),
                "error_message": message,
            }
        )
        return detect_result


def _upload_file_to_aliyun_temp_storage(
    *,
    config: dict[str, Any],
    model: str,
    source_path: pathlib.Path,
) -> dict[str, Any]:
    if not source_path.exists():
        raise VisualGenerationError(
            f"local source file missing: {source_path.name}",
            failure_reason="portrait_local_input_missing",
        )
    policy_request = urllib.request.Request(
        "https://dashscope.aliyuncs.com/api/v1/uploads?"
        + urllib.parse.urlencode({"action": "getPolicy", "model": model}),
        headers={
            "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
            "Content-Type": "application/json",
        },
        method="GET",
    )
    policy_payload = _urlopen_json_request(
        policy_request,
        error_cls=VisualGenerationError,
        invalid_json_message="aliyun upload policy returned invalid JSON payload",
    )
    policy_data = policy_payload.get("data") or {}
    upload_host = _normalize_optional_text(policy_data.get("upload_host"))
    upload_dir = _normalize_optional_text(policy_data.get("upload_dir")).rstrip("/")
    oss_access_key_id = _normalize_optional_text(policy_data.get("oss_access_key_id"))
    policy = _normalize_optional_text(policy_data.get("policy"))
    signature = _normalize_optional_text(policy_data.get("signature"))
    object_acl = _normalize_optional_text(policy_data.get("x_oss_object_acl"))
    forbid_overwrite = _normalize_optional_text(
        policy_data.get("x_oss_forbid_overwrite")
    )
    if not all(
        [
            upload_host,
            upload_dir,
            oss_access_key_id,
            policy,
            signature,
            object_acl,
            forbid_overwrite,
        ]
    ):
        raise VisualGenerationError(
            "aliyun upload policy response missing required fields",
            failure_reason="portrait_upload_policy_invalid",
        )

    key = f"{upload_dir}/{uuid.uuid4().hex}_{source_path.name}"
    boundary = f"----CodexBoundary{uuid.uuid4().hex}"
    content_type = mimetypes.guess_type(source_path.name)[0] or "application/octet-stream"
    upload_body = _build_multipart_form_data(
        boundary=boundary,
        fields=[
            ("OSSAccessKeyId", oss_access_key_id),
            ("policy", policy),
            ("Signature", signature),
            ("x-oss-object-acl", object_acl),
            ("x-oss-forbid-overwrite", forbid_overwrite),
            ("key", key),
            ("success_action_status", "200"),
        ],
        file_field_name="file",
        file_name=source_path.name,
        file_content=source_path.read_bytes(),
        file_content_type=content_type,
    )
    upload_request = urllib.request.Request(
        upload_host,
        data=upload_body,
        headers={
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(upload_request, timeout=60) as response:
            response.read()
    except urllib.error.HTTPError as exc:
        raise VisualGenerationError(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
            failure_reason="portrait_upload_failed",
        ) from exc
    except urllib.error.URLError as exc:
        raise VisualGenerationError(
            str(exc.reason or exc),
            error_code="UrlUploadError",
            status=STATUS_BLOCKED if _looks_like_timeout_message(str(exc.reason or exc)) else STATUS_FAILED,
            failure_reason="portrait_upload_timeout"
            if _looks_like_timeout_message(str(exc.reason or exc))
            else "portrait_upload_failed",
        ) from exc
    return {
        "request_id": policy_payload.get("request_id"),
        "upload_host": upload_host,
        "upload_key": key,
        "oss_url": f"oss://{key}",
    }


def _build_multipart_form_data(
    *,
    boundary: str,
    fields: list[tuple[str, str]],
    file_field_name: str,
    file_name: str,
    file_content: bytes,
    file_content_type: str,
) -> bytes:
    body = bytearray()
    for key, value in fields:
        body.extend(f"--{boundary}\r\n".encode("utf-8"))
        body.extend(
            f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode(
                "utf-8"
            )
        )
        body.extend(str(value).encode("utf-8"))
        body.extend(b"\r\n")
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(
        (
            f'Content-Disposition: form-data; name="{file_field_name}"; '
            f'filename="{file_name}"\r\n'
        ).encode("utf-8")
    )
    body.extend(f"Content-Type: {file_content_type}\r\n\r\n".encode("utf-8"))
    body.extend(file_content)
    body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode("utf-8"))
    return bytes(body)


def _build_visual_asset_output_path(
    *,
    output_dir: pathlib.Path,
    segment_id: str,
    asset_kind: str,
    source_url: str,
    default_extension: str,
) -> pathlib.Path:
    parsed_path = urllib.parse.urlparse(source_url).path
    extension = pathlib.Path(parsed_path).suffix or default_extension
    return output_dir / "visual" / f"{segment_id}_{asset_kind}{extension}"


def execute_local_preview_assembly(
    manifest: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    preview = build_default_assembly_preview(output_dir)
    preview_dir = output_dir / "assembly"
    preview_dir.mkdir(parents=True, exist_ok=True)

    missing: list[str] = []
    voiceover_audio = pathlib.Path(
        _nested_get(manifest, "generation", "voiceover", "audio_path") or ""
    )
    captions_path = pathlib.Path(
        _nested_get(manifest, "generation", "captions", "captions_path") or ""
    )
    if not voiceover_audio.exists():
        missing.append("voiceover_audio")
    if not captions_path.exists():
        missing.append("captions_srt")
    if shutil.which("swift") is None:
        missing.append("swift")
    if not (ROOT / "video_builder.swift").exists():
        missing.append("video_builder_swift")
    if not manifest.get("segments"):
        missing.append("manifest_segments")

    if missing:
        preview.update(
            {
                "status": STATUS_BLOCKED,
                "blocked_reason": "缺少本地预览组装前提：" + "、".join(missing),
            }
        )
        return preview

    preview_manifest_path = preview_dir / "preview_manifest.json"
    preview_video_path = preview_dir / "formal_api_demo_preview.mp4"
    final_video_path = output_dir / "final.mp4"
    preview_fps = int(_nested_get(config, "assembly", "fps") or 10)
    preview_manifest = {
        "width": 1080,
        "height": 1920,
        "fps": preview_fps,
        "audioPath": str(voiceover_audio.resolve()),
        "outputPath": str(preview_video_path.resolve()),
        "slides": _build_preview_slides(manifest),
    }
    write_json(preview_manifest_path, preview_manifest)

    try:
        run_subprocess(
            [
                "swift",
                str(ROOT / "video_builder.swift"),
                str(preview_manifest_path),
            ]
        )
    except subprocess.CalledProcessError as exc:
        preview.update(
            {
                "status": STATUS_FAILED,
                "failure_reason": "local_preview_assembly_failed",
                "error_message": str(exc),
            }
        )
        return preview

    if not preview_video_path.exists():
        preview.update(
            {
                "status": STATUS_FAILED,
                "failure_reason": "local_preview_video_missing",
                "error_message": "Swift 组装已执行，但 preview 视频文件未落出。",
            }
        )
        return preview

    shutil.copyfile(preview_video_path, final_video_path)

    preview.update(
        {
            "status": STATUS_SUCCESS,
            "video_path": str(preview_video_path),
            "final_video_path": str(final_video_path),
            "preview_manifest_path": str(preview_manifest_path),
            "captions_path": str(captions_path),
        }
    )
    return preview


def write_json(path: pathlib.Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _parse_segment_block(block: dict[str, Any]) -> dict[str, Any]:
    values = _parse_bullet_kv(block["lines"])
    missing_keys = [name for name in REQUIRED_SEGMENT_FIELDS if name not in values]
    if missing_keys:
        raise ValueError(
            f"段落 {block['heading']} 缺少必填字段：{', '.join(missing_keys)}"
        )

    needs_image = _parse_yes_no(values["需要图片"])
    needs_video = _parse_yes_no(values["需要视频"])
    allow_real_desktop_footage = _parse_yes_no(values["允许真实桌面素材"])
    carrier = values.get("段载体", "").strip() or _default_segment_carrier(
        needs_image=needs_image,
        needs_video=needs_video,
        allow_real_desktop_footage=allow_real_desktop_footage,
    )
    asset_key = values.get("素材键", "").strip()
    asset_source = values.get("素材来源", "").strip() or _default_segment_asset_source(
        carrier=carrier,
        allow_real_desktop_footage=allow_real_desktop_footage,
    )

    return {
        "segment_heading": block["heading"],
        "segment_id": values["段落ID"].strip(),
        "planned_duration_seconds": _parse_seconds(values["计划时长"]),
        "goal": values["段目标"].strip(),
        "voiceover_text": values["配音文案"].strip(),
        "caption_text": values["字幕文案"].strip(),
        "visual_intent": values["画面意图"].strip(),
        "needs_image": needs_image,
        "needs_video": needs_video,
        "allow_real_desktop_footage": allow_real_desktop_footage,
        "carrier": carrier,
        "asset_key": asset_key,
        "asset_source": asset_source,
    }


def _parse_bullet_kv(lines: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        if "：" not in stripped[2:]:
            continue
        key, value = stripped[2:].split("：", 1)
        result[key.strip()] = value.strip()
    return result


def _section_text(lines: list[str]) -> str:
    return "\n".join(line.strip() for line in lines if line.strip()).strip()


def _section_list(lines: list[str]) -> list[str]:
    items: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
        elif stripped:
            items.append(stripped)
    return items


def _parse_seconds(raw: str) -> float:
    normalized = raw.strip().replace("秒", "").strip()
    if not normalized:
        raise ValueError("时长字段不能为空")
    return float(normalized)


def _parse_yes_no(raw: str) -> bool:
    normalized = raw.strip()
    if normalized == "是":
        return True
    if normalized == "否":
        return False
    raise ValueError(f"布尔字段只能写“是”或“否”，当前值：{raw}")


def _parse_simple_toml(path: pathlib.Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    current_section: dict[str, Any] | None = None

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = _strip_toml_inline_comment(line).strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            section_name = stripped[1:-1].strip()
            current_section = _ensure_nested_section(result, section_name)
            continue
        if "=" not in stripped or current_section is None:
            continue
        key, raw_value = stripped.split("=", 1)
        current_section[key.strip()] = _parse_toml_value(raw_value.strip())

    return result


def _parse_toml_value(raw_value: str) -> Any:
    if raw_value.startswith('"') and raw_value.endswith('"'):
        return raw_value[1:-1]
    if raw_value.startswith("[") and raw_value.endswith("]"):
        inner = raw_value[1:-1].strip()
        if not inner:
            return []
        return [_parse_toml_value(part.strip()) for part in _split_toml_array(inner)]
    lowered = raw_value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    try:
        if "." in raw_value:
            return float(raw_value)
        return int(raw_value)
    except ValueError:
        return raw_value


def _deep_merge(target: dict[str, Any], source: dict[str, Any]) -> None:
    for key, value in source.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_merge(target[key], value)
        else:
            target[key] = value


def _strip_toml_inline_comment(line: str) -> str:
    in_string = False
    escaped = False
    chars: list[str] = []
    for char in line:
        if char == '"' and not escaped:
            in_string = not in_string
        if char == "#" and not in_string:
            break
        chars.append(char)
        escaped = char == "\\" and not escaped
    return "".join(chars).rstrip()


def _split_toml_array(raw_value: str) -> list[str]:
    items: list[str] = []
    buffer: list[str] = []
    in_string = False
    escaped = False
    for char in raw_value:
        if char == '"' and not escaped:
            in_string = not in_string
        if char == "," and not in_string:
            items.append("".join(buffer))
            buffer = []
            escaped = False
            continue
        buffer.append(char)
        escaped = char == "\\" and not escaped
    if buffer:
        items.append("".join(buffer))
    return items


def _ensure_nested_section(root: dict[str, Any], section_name: str) -> dict[str, Any]:
    current = root
    for key in [part.strip() for part in section_name.split(".") if part.strip()]:
        current = current.setdefault(key, {})
    return current


def _nested_set(payload: dict[str, Any], *keys: str, value: Any) -> None:
    current = payload
    for key in keys[:-1]:
        current = current.setdefault(key, {})
    current[keys[-1]] = value


def _build_default_rotation_state() -> dict[str, Any]:
    return {
        "disabled_candidates": {
            RESOURCE_KIND_TTS: {},
            RESOURCE_KIND_IMAGE: {},
            RESOURCE_KIND_VIDEO: {},
        },
        "last_success": {},
    }


def _candidate_priority(section: dict[str, Any], default: int) -> int:
    return _coerce_int_or_none(section.get("priority")) or default


def _candidate_enabled(section: dict[str, Any]) -> bool:
    return _config_flag({"section": section}, "section", "enabled", default=True)


def _candidate_label(candidate_id: str, section: dict[str, Any], default: str) -> str:
    return _normalize_optional_text(section.get("label")) or default or candidate_id


def _primary_tts_candidate(config: dict[str, Any]) -> dict[str, Any]:
    route_family = _get_tts_api_route_family(config)
    return {
        "candidate_id": "primary",
        "label": "primary",
        "priority": 10,
        "enabled": True,
        "provider": _get_tts_provider_name(config, route_family=route_family),
        "api_route_family": route_family,
        "region": _nested_get(config, "provider", "region"),
        "api_key": _nested_get(config, "auth", "api_key"),
        "app_id": _nested_get(config, "auth", "app_id"),
        "model": _nested_get(config, "tts", "model"),
        "endpoint_id": _nested_get(config, "tts", "endpoint_id"),
        "resource_id": _nested_get(config, "tts", "resource_id"),
        "voice": _nested_get(config, "tts", "voice"),
        "style": _nested_get(config, "tts", "style"),
        "instruction": _nested_get(config, "tts", "instruction"),
        "speech_rate": _nested_get(config, "tts", "speech_rate"),
        "pitch_rate": _nested_get(config, "tts", "pitch_rate"),
        "volume": _nested_get(config, "tts", "volume"),
        "response_format": _nested_get(config, "tts", "response_format"),
        "style_profile": _normalize_optional_text(_nested_get(config, "tts", "style_profile"))
        or "default",
        "source": "base_config",
    }


def _resolve_tts_candidate_pool(config: dict[str, Any]) -> list[dict[str, Any]]:
    primary = _primary_tts_candidate(config)
    candidates: list[dict[str, Any]] = [primary]
    pool = _nested_get(config, "tts_pool")
    if not isinstance(pool, dict):
        return _sort_tts_candidates(candidates)

    for candidate_id, section in pool.items():
        if not isinstance(section, dict):
            continue
        if candidate_id == "primary":
            target = primary
        else:
            target = dict(primary)
            target["candidate_id"] = candidate_id
            target["source"] = "tts_pool"
            candidates.append(target)
        route_family = _normalize_optional_text(section.get("api_route_family")) or target["api_route_family"]
        target.update(
            {
                "label": _candidate_label(candidate_id, section, target["label"]),
                "priority": _candidate_priority(section, 100 + len(candidates)),
                "enabled": _candidate_enabled(section),
                "api_route_family": route_family,
                "provider": _normalize_optional_text(section.get("provider"))
                or (
                    PROVIDER_ALIYUN_BAILIAN
                    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE
                    else PROVIDER_VOLCENGINE
                ),
                "region": _normalize_optional_text(section.get("region")) or target["region"],
                "api_key": section.get("api_key", target["api_key"]),
                "app_id": section.get("app_id", target["app_id"]),
                "model": section.get("model", target["model"]),
                "endpoint_id": section.get("endpoint_id", target["endpoint_id"]),
                "resource_id": section.get("resource_id", target["resource_id"]),
                "voice": section.get("voice", target["voice"]),
                "style": section.get("style", target["style"]),
                "instruction": section.get("instruction", target["instruction"]),
                "speech_rate": section.get("speech_rate", target["speech_rate"]),
                "pitch_rate": section.get("pitch_rate", target["pitch_rate"]),
                "volume": section.get("volume", target["volume"]),
                "response_format": section.get("response_format", target["response_format"]),
                "style_profile": _normalize_optional_text(section.get("style_profile"))
                or target["style_profile"],
            }
        )
    return _sort_tts_candidates(candidates)


def _sort_tts_candidates(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda candidate: (
            len(_tts_candidate_missing_prerequisites(candidate)) > 0,
            candidate.get("priority", 999),
            candidate.get("candidate_id", ""),
        ),
    )


def _tts_candidate_model_identifier(candidate: dict[str, Any]) -> str | None:
    route_family = candidate.get("api_route_family") or TTS_ROUTE_FAMILY_ARK
    if route_family in {
        TTS_ROUTE_FAMILY_EDGE_GATEWAY,
        TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE,
    }:
        model = candidate.get("model")
        return None if _is_missing_secret(model) else str(model).strip()
    endpoint_id = candidate.get("endpoint_id")
    if not _is_missing_secret(endpoint_id):
        return str(endpoint_id).strip()
    model = candidate.get("model")
    return None if _is_missing_secret(model) else str(model).strip()


def _tts_candidate_missing_prerequisites(candidate: dict[str, Any]) -> list[str]:
    missing: list[str] = []
    if not candidate.get("enabled", True):
        missing.append("candidate_disabled")
        return missing
    route_family = candidate.get("api_route_family") or TTS_ROUTE_FAMILY_ARK
    if route_family not in SUPPORTED_TTS_ROUTE_FAMILIES:
        missing.append("tts_api_route_family")
        return missing
    if _is_missing_secret(candidate.get("api_key")):
        missing.append("api_key")
    if _is_missing_secret(candidate.get("voice")):
        missing.append("tts_voice")
    if route_family == TTS_ROUTE_FAMILY_ARK:
        if _is_missing_secret(candidate.get("region")):
            missing.append("provider_region")
        if not _tts_candidate_model_identifier(candidate):
            missing.append("tts_model_or_endpoint")
    elif route_family in {
        TTS_ROUTE_FAMILY_EDGE_GATEWAY,
        TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE,
    }:
        if _is_missing_secret(candidate.get("model")):
            missing.append("tts_model")
    elif route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        if _is_missing_secret(candidate.get("app_id")):
            missing.append("app_id")
        if _is_missing_secret(candidate.get("resource_id")):
            missing.append("tts_resource_id")
    return missing


def _summarize_tts_candidate_pool(candidates: list[dict[str, Any]]) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    available_candidate_count = 0
    for candidate in _sort_tts_candidates(candidates):
        missing = _tts_candidate_missing_prerequisites(candidate)
        available = not missing
        if available:
            available_candidate_count += 1
        entries.append(
            {
                "candidate_id": candidate["candidate_id"],
                "label": candidate["label"],
                "provider": candidate["provider"],
                "api_route_family": candidate["api_route_family"],
                "voice": "" if _is_missing_secret(candidate.get("voice")) else candidate.get("voice"),
                "model_identifier": _tts_candidate_model_identifier(candidate),
                "style_profile": candidate.get("style_profile", "default"),
                "priority": candidate.get("priority"),
                "enabled": candidate.get("enabled", True),
                "available": available,
                "missing_prerequisites": missing,
            }
        )
    return {
        "total_candidate_count": len(candidates),
        "available_candidate_count": available_candidate_count,
        "backup_candidate_count": max(0, len(candidates) - 1),
        "candidates": entries,
    }


def _resolve_visual_candidate_pool(
    config: dict[str, Any],
    *,
    resource_kind: str,
) -> list[dict[str, Any]]:
    section_name = "image_generation" if resource_kind == RESOURCE_KIND_IMAGE else "video_generation"
    primary = {
        "candidate_id": "primary",
        "label": "primary",
        "priority": 10,
        "enabled": True,
        "provider": _nested_get(config, "provider", "name"),
        "region": _nested_get(config, "provider", "region"),
        "api_key": _nested_get(config, "auth", "api_key"),
        "model": _nested_get(config, section_name, "model"),
        "style_profile": _normalize_optional_text(_nested_get(config, section_name, "style_profile"))
        or "default",
        "source": "base_config",
    }
    candidates: list[dict[str, Any]] = [primary]
    pool = _nested_get(config, f"{resource_kind}_pool")
    if not isinstance(pool, dict):
        return _sort_visual_candidates(candidates, resource_kind=resource_kind)

    for candidate_id, section in pool.items():
        if not isinstance(section, dict):
            continue
        if candidate_id == "primary":
            target = primary
        else:
            target = dict(primary)
            target["candidate_id"] = candidate_id
            target["source"] = f"{resource_kind}_pool"
            candidates.append(target)
        target.update(
            {
                "label": _candidate_label(candidate_id, section, target["label"]),
                "priority": _candidate_priority(section, 100 + len(candidates)),
                "enabled": _candidate_enabled(section),
                "provider": _normalize_optional_text(section.get("provider")) or target["provider"],
                "region": _normalize_optional_text(section.get("region")) or target["region"],
                "api_key": section.get("api_key", target["api_key"]),
                "model": section.get("model", target["model"]),
                "style_profile": _normalize_optional_text(section.get("style_profile"))
                or target["style_profile"],
            }
        )
    return _sort_visual_candidates(candidates, resource_kind=resource_kind)


def _sort_visual_candidates(
    candidates: list[dict[str, Any]],
    *,
    resource_kind: str,
) -> list[dict[str, Any]]:
    return sorted(
        candidates,
        key=lambda candidate: (
            len(_visual_candidate_missing_prerequisites(candidate, resource_kind=resource_kind)) > 0,
            candidate.get("priority", 999),
            candidate.get("candidate_id", ""),
        ),
    )


def _visual_candidate_missing_prerequisites(
    candidate: dict[str, Any],
    *,
    resource_kind: str,
) -> list[str]:
    missing: list[str] = []
    if not candidate.get("enabled", True):
        missing.append("candidate_disabled")
        return missing
    if _is_missing_secret(candidate.get("provider")):
        missing.append("provider")
    if _is_missing_secret(candidate.get("region")):
        missing.append("provider_region")
    if _is_missing_secret(candidate.get("api_key")):
        missing.append("api_key")
    if _is_missing_secret(candidate.get("model")):
        missing.append(f"{resource_kind}_model")
    return missing


def _summarize_visual_candidate_pool(
    image_candidates: list[dict[str, Any]],
    video_candidates: list[dict[str, Any]],
) -> dict[str, Any]:
    def build_summary(candidates: list[dict[str, Any]], resource_kind: str) -> dict[str, Any]:
        entries: list[dict[str, Any]] = []
        available_candidate_count = 0
        for candidate in _sort_visual_candidates(candidates, resource_kind=resource_kind):
            missing = _visual_candidate_missing_prerequisites(candidate, resource_kind=resource_kind)
            available = not missing
            if available:
                available_candidate_count += 1
            entries.append(
                {
                    "candidate_id": candidate["candidate_id"],
                    "label": candidate["label"],
                    "provider": candidate["provider"],
                    "model": candidate["model"],
                    "style_profile": candidate.get("style_profile", "default"),
                    "priority": candidate.get("priority"),
                    "enabled": candidate.get("enabled", True),
                    "available": available,
                    "missing_prerequisites": missing,
                }
            )
        return {
            "total_candidate_count": len(candidates),
            "available_candidate_count": available_candidate_count,
            "backup_candidate_count": max(0, len(candidates) - 1),
            "candidates": entries,
        }

    return {
        RESOURCE_KIND_IMAGE: build_summary(image_candidates, RESOURCE_KIND_IMAGE),
        RESOURCE_KIND_VIDEO: build_summary(video_candidates, RESOURCE_KIND_VIDEO),
    }


def _candidate_missing_union(
    candidates: list[dict[str, Any]],
    *,
    missing_fn: Any,
) -> list[str]:
    merged: list[str] = []
    for candidate in candidates:
        for item in missing_fn(candidate):
            if item != "candidate_disabled" and item not in merged:
                merged.append(item)
    return merged


def _generation_missing_prerequisites(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    route_family: str,
) -> list[str]:
    missing: list[str] = []
    if not has_local_config:
        missing.append("local_config_file")
    if route_family not in SUPPORTED_TTS_ROUTE_FAMILIES:
        missing.append("tts_api_route_family")
        return missing
    if _is_missing_secret(_nested_get(config, "auth", "api_key")):
        missing.append("api_key")
    if _is_missing_secret(_nested_get(config, "tts", "voice")):
        missing.append("tts_voice")
    if route_family == TTS_ROUTE_FAMILY_ARK:
        if _is_missing_secret(_nested_get(config, "provider", "region")):
            missing.append("provider_region")
        if not _get_tts_model_identifier(config, route_family=route_family):
            missing.append("tts_model_or_endpoint")
    elif route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
        if _is_missing_secret(_nested_get(config, "tts", "model")):
            missing.append("tts_model")
    elif route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        if _is_missing_secret(_nested_get(config, "tts", "model")):
            missing.append("tts_model")
    elif route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        if _is_missing_secret(_nested_get(config, "auth", "app_id")):
            missing.append("app_id")
        if _is_missing_secret(_nested_get(config, "tts", "resource_id")):
            missing.append("tts_resource_id")
    return missing


def _assembly_missing_prerequisites(
    manifest: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
) -> list[str]:
    missing: list[str] = []
    if not has_local_config:
        missing.append("local_config_file")
    for keys, missing_name, _detail in _cloud_assembly_required_fields():
        if _is_missing_secret(_nested_get(config, *keys)):
            missing.append(missing_name)
    if not manifest.get("segments"):
        missing.append("manifest_segments")
    if manifest.get("generation", {}).get("voiceover", {}).get("status") != STATUS_SUCCESS:
        missing.append("voiceover_assets_not_ready")
    if manifest.get("generation", {}).get("captions", {}).get("status") != STATUS_SUCCESS:
        missing.append("subtitle_assets_not_ready")
    if manifest.get("generation", {}).get("visual_generation", {}).get("status") != STATUS_SUCCESS:
        missing.append("visual_assets_not_ready")
    return missing


def _cloud_assembly_required_fields() -> list[tuple[tuple[str, ...], str, str]]:
    return [
        (("aliyun_oss", "bucket"), "aliyun_oss_bucket", "北京区 OSS bucket；当前已确认可写入仓库。"),
        (("aliyun_oss", "region"), "aliyun_oss_region", "北京区 OSS region；纯 PPT 主线固定为 cn-beijing。"),
        (("aliyun_oss", "endpoint"), "aliyun_oss_endpoint", "北京区 OSS endpoint；云端上传必须显式配置。"),
        (("aliyun_oss", "bucket_domain"), "aliyun_oss_bucket_domain", "北京区 OSS bucket domain；云端资源定位需要该字段。"),
        (("aliyun_oss", "access_key_id"), "aliyun_oss_access_key_id", "OSS AccessKey ID 仅允许在本地注入，仓库示例必须留占位。"),
        (("aliyun_oss", "access_key_secret"), "aliyun_oss_access_key_secret", "OSS AccessKey Secret 仅允许在本地注入，仓库示例必须留占位。"),
        (("aliyun_oss", "prefix_raw"), "aliyun_oss_prefix_raw", "raw 前缀用于云端组装原始素材上传路径。"),
        (("aliyun_oss", "prefix_final"), "aliyun_oss_prefix_final", "final 前缀用于云端导出成片路径。"),
        (("aliyun_oss", "prefix_temp"), "aliyun_oss_prefix_temp", "temp 前缀用于云端临时文件路径。"),
        (("aliyun_ims", "region"), "aliyun_ims_region", "IMS / 云剪区域；当前主线固定为 cn-beijing。"),
        (("aliyun_ims", "storage_address"), "aliyun_ims_storage_address", "IMS 存储地址；当前已确认为北京区 OSS domain。"),
        (("aliyun_ims", "cloud_project_name"), "aliyun_ims_cloud_project_name", "云剪工程名称；当前主线应指向 video-factory-ppt-master-v1。"),
    ]


def _cloud_assembly_checks(config: dict[str, Any]) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    for keys, missing_name, detail in _cloud_assembly_required_fields():
        checks.append(
            {
                "name": missing_name,
                "status": "pass" if not _is_missing_secret(_nested_get(config, *keys)) else "fail",
                "detail": detail,
            }
        )
    return checks


def build_cloud_assembly_target(config: dict[str, Any]) -> dict[str, Any]:
    return {
        "assembly_mode": _nested_get(config, "assembly", "mode"),
        "subtitle_mode": _nested_get(config, "assembly", "subtitle_mode"),
        "resolution": _nested_get(config, "assembly", "resolution"),
        "fps": _nested_get(config, "assembly", "fps"),
        "oss_bucket": _nested_get(config, "aliyun_oss", "bucket"),
        "oss_region": _nested_get(config, "aliyun_oss", "region"),
        "oss_endpoint": _nested_get(config, "aliyun_oss", "endpoint"),
        "oss_bucket_domain": _nested_get(config, "aliyun_oss", "bucket_domain"),
        "oss_prefix_raw": _nested_get(config, "aliyun_oss", "prefix_raw"),
        "oss_prefix_final": _nested_get(config, "aliyun_oss", "prefix_final"),
        "oss_prefix_temp": _nested_get(config, "aliyun_oss", "prefix_temp"),
        "ims_region": _nested_get(config, "aliyun_ims", "region"),
        "ims_storage_address": _nested_get(config, "aliyun_ims", "storage_address"),
        "ims_cloud_project_name": _nested_get(config, "aliyun_ims", "cloud_project_name"),
    }


def _is_missing_secret(value: Any) -> bool:
    if value is None:
        return True
    normalized = str(value).strip()
    return not normalized or normalized.startswith(PLACEHOLDER_PREFIX)


def _nested_get(payload: dict[str, Any], *keys: str) -> Any:
    current: Any = payload
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _config_flag(payload: dict[str, Any], *keys: str, default: bool = False) -> bool:
    value = _nested_get(payload, *keys)
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    normalized = str(value).strip().lower()
    if normalized in {"true", "1", "yes", "on"}:
        return True
    if normalized in {"false", "0", "no", "off", ""}:
        return False
    return default


def _build_visual_model_routes(config: dict[str, Any]) -> dict[str, Any]:
    image_model = _nested_get(config, "image_generation", "model")
    general_video_model = _nested_get(config, "video_generation", "model")
    portrait_detect_enabled = _config_flag(
        config,
        "portrait_detect",
        "enabled",
        default=False,
    )
    portrait_video_enabled = _config_flag(
        config,
        "portrait_video_generation",
        "enabled",
        default=False,
    )
    return {
        "image_generation": {
            "enabled": _config_flag(config, "image_generation", "enabled", default=True),
            "model": image_model,
            "role": "首帧 / 背景 / 人像底图生成",
            "recommended_free_model": DEFAULT_GENERAL_IMAGE_MODEL,
        },
        "general_video_generation": {
            "enabled": _config_flag(config, "video_generation", "enabled", default=True),
            "model": general_video_model,
            "role": "普通视频主线（先图后视频）",
            "recommended_free_model": DEFAULT_GENERAL_VIDEO_MODEL,
        },
        "portrait_detect": {
            "enabled": portrait_detect_enabled,
            "model": _nested_get(config, "portrait_detect", "model"),
            "role": "liveportrait 前置检测",
            "recommended_free_model": DEFAULT_PORTRAIT_DETECT_MODEL,
        },
        "portrait_video_generation": {
            "enabled": portrait_video_enabled,
            "model": _nested_get(config, "portrait_video_generation", "model"),
            "role": "固定背景 / 人物开口分支",
            "recommended_free_model": DEFAULT_PORTRAIT_VIDEO_MODEL,
            "requires": ["portrait_detect"],
        },
    }


def _gate_known_issues(gate: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if gate["missing_prerequisites"]:
        issues.append(
            "当前仍缺正式执行前提：" + "、".join(gate["missing_prerequisites"])
        )
    if gate["missing_implementations"]:
        issues.append(
            "当前仍缺 provider 实现：" + "、".join(gate["missing_implementations"])
        )
    return issues


def _tts_probe_known_issues(tts_probe: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if tts_probe.get("status") == STATUS_BLOCKED and tts_probe.get("blocked_reason"):
        issues.append("TTS probe blocked：" + tts_probe["blocked_reason"])
    if tts_probe.get("status") == STATUS_FAILED and tts_probe.get("error_message"):
        issues.append("TTS probe failed：" + tts_probe["error_message"])
    if tts_probe.get("status") == STATUS_SUCCESS:
        issues.append(
            "当前 TTS 调用已接通；正式主线下一步取决于用户真实素材注入或辅助图片资产准备，再进入北京区 OSS + 云剪主路径。"
        )
    return issues


def _generation_next_action_hint(
    gate: dict[str, Any],
    tts_probe: dict[str, Any],
    dry_run: bool,
) -> str:
    route_family = (
        tts_probe.get("api_route_family")
        or _nested_get(gate, "tts_target", "api_route_family")
        or TTS_ROUTE_FAMILY_ARK
    )
    if dry_run:
        return "当前为 dry-run；下一步应先确认配音与图片/视频 API 前提，再执行真实 generation。visual plan 只算辅助产物。"
    footage_missing = [
        item
        for item in gate.get("missing_prerequisites", [])
        if item.startswith("footage_input_")
    ]
    if footage_missing:
        return (
            "先在 formal_api_demo.local.toml 的 [footage_inputs.*] 里注入用户本地过程素材路径；"
            "只有当你显式把人物段改回本地真人素材时，才需要 verified_role=\"human_on_camera\"。"
        )
    if any(
        item in gate.get("missing_prerequisites", [])
        for item in ("image_generation_model", "video_generation_model")
    ):
        return "先补齐 image_generation.model / video_generation.model；默认主线要求 API 真人和轻量信息卡都可用，缺模型时不能继续推进。"
    if any(
        item in gate.get("missing_prerequisites", [])
        for item in (
            "portrait_detect_enabled",
            "portrait_detect_model",
            "portrait_video_generation_model",
        )
    ):
        return "若要走真人开口分支，先补齐 portrait_detect.enabled / portrait_detect.model / portrait_video_generation.model；liveportrait 必须先过 liveportrait-detect。"
    if gate["missing_prerequisites"]:
        if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
            return "先补齐阿里百炼的 API Key、tts.model 和 voice，再进入真实 TTS probe。"
        if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
            return "先补齐 Edge Gateway 的访问密钥、tts.model 和 voice，再进入真实 TTS probe。"
        if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
            return "先补齐 OpenSpeech 的 app_id、Access-Key、resource_id 和 voice；不要继续按 Ark 问题处理。"
        return "先补齐 Ark route family 所需的 API Key、region、TTS model/endpoint 和 voice，再进入真实 TTS probe。"
    if any(
        item in gate.get("missing_implementations", [])
        for item in (
            "image_generation_provider_implementation",
            "video_generation_provider_implementation",
            "portrait_detect_provider_implementation",
            "portrait_video_generation_provider_implementation",
        )
    ):
        return (
            "当前默认路线已定：hook / close 走 API 真人 liveportrait-detect -> liveportrait；"
            "轻量信息卡走 wan2.6-image；"
            "普通辅助视频段才走 wan2.6-image -> wan2.7-i2v。"
            "wan2.7-videoedit 只做后期编辑增强，provider implementation 未接通前不要把 preview 当 generation success。"
        )
    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH and gate["missing_implementations"]:
        return "当前已拆出 doubao openspeech v3 family，但 provider implementation 尚未接入；下一步应补请求体与返回解析。"
    if (
        tts_probe.get("status") == STATUS_FAILED
        and tts_probe.get("http_status_code") == 404
        and route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE
    ):
        return "当前阿里百炼 404 已压缩到接口路由 / 模型标识层；优先核对 base_url、relative_path 与 tts.model。"
    if (
        tts_probe.get("status") == STATUS_FAILED
        and tts_probe.get("http_status_code") == 404
        and route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY
    ):
        return "当前 Edge Gateway 404 已压缩到网关路由 / 目标模型匹配层；优先核对 base_url、tts.model 与网关访问密钥。"
    if (
        tts_probe.get("status") == STATUS_FAILED
        and tts_probe.get("http_status_code") == 404
        and route_family == TTS_ROUTE_FAMILY_ARK
    ):
        return "当前 Ark 404 已压缩到请求路由 / endpoint-model 匹配层；优先核对 Ark 路由与 endpoint/model 用法。"
    if tts_probe.get("status") == STATUS_FAILED:
        return "当前已进入真实请求层失败；优先核对远端返回码、请求结构和 provider 接口兼容性。"
    if tts_probe.get("status") == STATUS_SUCCESS:
        return "当前配音链路已通；下一步只要把真人口播、自录过程素材和结果卡准备齐，或补齐必要的辅助图片段资产，就可以继续推进北京区 OSS + 云剪 cloud-only 主路径。"
    return "当前已具备部分 generation 前提；下一步可执行真实 generation，并把失败压到字段或 provider 层。"


def _assembly_next_action_hint(
    gate: dict[str, Any],
    dry_run: bool,
) -> str:
    if dry_run:
        return "当前为 assembly dry-run；正式主线已锁定北京区 OSS + 云剪唯一主路径，下一步先在本地注入 AccessKey 并核对 OSS / IMS / 云剪工程参数。"
    if "visual_assets_not_ready" in gate.get("missing_prerequisites", []):
        return "当前缺少真实 visual assets；应先补图片 / 视频 API provider，再推进北京区 OSS + 云剪 cloud-only 主路径。"
    if gate["missing_prerequisites"]:
        return "先补齐北京区 OSS + 云剪主路径缺失前提；缺密钥时只允许标记待注入 / 待验证，不得再回退本地 assembly。"
    return "北京区 OSS + 云剪 assembly 已接入代码主链；下一步是在本地配置文件填入真实 AccessKey / Secret，然后执行真实云端导出验证。"


def _select_tts_probe_text(video_spec: dict[str, Any]) -> tuple[str, str]:
    if video_spec.get("segments"):
        return video_spec["segments"][0]["voiceover_text"], "segment_1_voiceover"
    return video_spec["hook"], "hook"


def _get_tts_api_route_family(config: dict[str, Any]) -> str:
    route_family = _nested_get(config, "tts", "api_route_family")
    if _is_missing_secret(route_family):
        return TTS_ROUTE_FAMILY_ARK
    return str(route_family).strip()


def _get_tts_model_identifier(
    config: dict[str, Any],
    route_family: str | None = None,
) -> str | None:
    route_family = route_family or _get_tts_api_route_family(config)
    if route_family in {
        TTS_ROUTE_FAMILY_EDGE_GATEWAY,
        TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE,
    }:
        model = _nested_get(config, "tts", "model")
        if not _is_missing_secret(model):
            return str(model).strip()
        return None
    endpoint_id = _nested_get(config, "tts", "endpoint_id")
    if not _is_missing_secret(endpoint_id):
        return str(endpoint_id).strip()
    model = _nested_get(config, "tts", "model")
    if not _is_missing_secret(model):
        return str(model).strip()
    return None


def _build_ark_base_url(config: dict[str, Any]) -> str:
    region = _nested_get(config, "provider", "region") or "cn-beijing"
    return f"https://ark.{region}.volces.com/api/v3"


def _get_tts_provider_name(
    config: dict[str, Any],
    route_family: str | None = None,
) -> str:
    route_family = route_family or _get_tts_api_route_family(config)
    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        return PROVIDER_ALIYUN_BAILIAN
    return PROVIDER_VOLCENGINE


def _build_tts_base_url(config: dict[str, Any], route_family: str) -> str:
    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        return "https://dashscope.aliyuncs.com/api/v1"
    if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
        return "https://ai-gateway.vei.volces.com/v1"
    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        return "https://openspeech.bytedance.com/api/v3"
    return _build_ark_base_url(config)


def _execute_aliyun_bailian_tts_probe(
    config: dict[str, Any],
    probe: dict[str, Any],
    audio_path: pathlib.Path,
    base_url: str,
    model_identifier: str | None,
    response_format: str,
    tts_options: dict[str, Any],
) -> str | None:
    relative_path = "/services/audio/tts/SpeechSynthesizer"
    payload = {
        "model": model_identifier,
        "input": _build_aliyun_bailian_tts_input_payload(
            probe_text=probe["probe_text"],
            voice=tts_options["voice"],
            response_format=response_format,
            instruction=tts_options["instruction"],
            speech_rate=tts_options["speech_rate"],
            pitch_rate=tts_options["pitch_rate"],
            volume=tts_options["volume"],
        ),
    }
    request = urllib.request.Request(
        f"{base_url}{relative_path}",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {_nested_get(config, 'auth', 'api_key')}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    response_payload = _urlopen_json_request(request)
    audio_url = _nested_get(response_payload, "output", "audio", "url")
    if not audio_url:
        raise TtsRequestError(
            "aliyun_bailian response missing output.audio.url",
            error_code="AliyunBailianMissingAudioUrl",
        )

    audio_path.parent.mkdir(parents=True, exist_ok=True)
    _download_binary_file(str(audio_url), audio_path)
    return response_payload.get("request_id")


def _urlopen_json_request(
    request: urllib.request.Request,
    *,
    error_cls: type[RuntimeError] = TtsRequestError,
    invalid_json_message: str = "aliyun_bailian returned invalid JSON payload",
) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        raise error_cls(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
        ) from exc
    except urllib.error.URLError as exc:
        raise error_cls(
            str(exc.reason or exc),
            error_code="UrlOpenError",
        ) from exc

    try:
        return json.loads(payload.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise error_cls(
            invalid_json_message,
            error_code="InvalidJson",
        ) from exc


def _download_binary_file(
    url: str,
    destination: pathlib.Path,
    *,
    error_cls: type[RuntimeError] = TtsRequestError,
    empty_error_message: str = "aliyun_bailian audio download is empty",
    empty_error_code: str = "AliyunBailianEmptyAudio",
) -> None:
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
    except urllib.error.HTTPError as exc:
        raise error_cls(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
        ) from exc
    except urllib.error.URLError as exc:
        raise error_cls(
            str(exc.reason or exc),
            error_code="UrlDownloadError",
        ) from exc

    if not data:
        raise error_cls(
            empty_error_message,
            error_code=empty_error_code,
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def _build_aliyun_bailian_tts_input_payload(
    *,
    probe_text: str,
    voice: Any,
    response_format: str,
    instruction: Any,
    speech_rate: float | None,
    pitch_rate: float | None,
    volume: int | None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "text": probe_text,
        "voice": voice,
        "format": response_format,
    }
    normalized_instruction = _normalize_optional_text(instruction)
    if normalized_instruction:
        payload["instruction"] = normalized_instruction
    if speech_rate is not None:
        payload["rate"] = speech_rate
    if pitch_rate is not None:
        payload["pitch"] = pitch_rate
    if volume is not None:
        payload["volume"] = volume
    return payload


def _read_urllib_error_message(exc: urllib.error.HTTPError) -> str:
    body = ""
    if exc.fp is not None:
        try:
            body = exc.read().decode("utf-8", errors="replace").strip()
        except Exception:  # pragma: no cover - best effort only.
            body = ""
    return body or str(exc)


def _classify_tts_exception(
    exc: Exception,
    config: dict[str, Any],
) -> tuple[str, str, int | None, str, str]:
    route_family = _get_tts_api_route_family(config)
    raw_message = _sanitize_message(str(exc), config)
    error_code = getattr(exc, "error_code", None) or exc.__class__.__name__
    http_status_code = _extract_http_status_code(exc)

    if http_status_code == 404:
        if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
            return (
                STATUS_FAILED,
                "aliyun_bailian_tts_route_or_model_not_found",
                http_status_code,
                error_code,
                raw_message,
            )
        if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
            return (
                STATUS_FAILED,
                "edge_gateway_tts_route_or_model_not_found",
                http_status_code,
                error_code,
                raw_message,
            )
        return (
            STATUS_FAILED,
            "ark_tts_route_or_identifier_not_found",
            http_status_code,
            error_code,
            raw_message,
        )
    if http_status_code is not None and 400 <= http_status_code < 600:
        return (
            STATUS_FAILED,
            _tts_failure_reason_by_route_family(route_family),
            http_status_code,
            error_code,
            raw_message,
        )
    if openai is not None and isinstance(exc, openai.APIError):
        return (
            STATUS_FAILED,
            _tts_failure_reason_by_route_family(route_family),
            http_status_code,
            error_code,
            raw_message,
        )
    return (
        STATUS_FAILED,
        _tts_failure_reason_by_route_family(route_family),
        http_status_code,
        error_code,
        raw_message,
    )


def _tts_failure_reason_by_route_family(route_family: str) -> str:
    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        return "aliyun_bailian_tts_request_failed"
    if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
        return "edge_gateway_tts_request_failed"
    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        return "doubao_openspeech_tts_request_failed"
    return "ark_tts_request_failed"


def _extract_http_status_code(exc: Exception) -> int | None:
    status_code = getattr(exc, "status_code", None)
    if isinstance(status_code, int):
        return status_code
    code = getattr(exc, "code", None)
    if isinstance(code, int):
        return code
    response = getattr(exc, "response", None)
    if response is None:
        return None
    response_status = getattr(response, "status_code", None)
    if isinstance(response_status, int):
        return response_status
    return None


def _build_tts_request_debug(
    config: dict[str, Any],
    route_family: str,
    base_url: str,
    model_identifier: str | None,
    response_format: str,
    *,
    effective_voice: Any = None,
    style: Any = None,
    instruction: Any = None,
    speech_rate: float | None = None,
    pitch_rate: float | None = None,
    volume: int | None = None,
) -> dict[str, Any]:
    provider = _get_tts_provider_name(config, route_family=route_family)
    endpoint_id = _nested_get(config, "tts", "endpoint_id")
    model = _nested_get(config, "tts", "model")
    resource_id = _nested_get(config, "tts", "resource_id")
    app_id = _nested_get(config, "auth", "app_id")
    voice = effective_voice if effective_voice is not None else _nested_get(config, "tts", "voice")
    style = style if style is not None else _nested_get(config, "tts", "style")
    instruction = instruction if instruction is not None else _nested_get(config, "tts", "instruction")
    relative_path = "/audio/speech"
    sdk_call = "client.audio.speech.with_streaming_response.create"
    voice_location = "payload.voice"
    instruction_location = None
    model_identifier_source = (
        "endpoint_id"
        if not _is_missing_secret(endpoint_id)
        else "model"
    )
    if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
        model_identifier_source = "model"
    if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
        relative_path = "/tts/..."
        sdk_call = "provider_implementation_pending"
        model_identifier_source = "resource_id"
    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        relative_path = "/services/audio/tts/SpeechSynthesizer"
        sdk_call = "urllib.request.urlopen"
        voice_location = "payload.input.voice"
        instruction_location = "payload.input.instruction"
        model_identifier_source = "model"
    debug = {
        "provider": provider,
        "api_route_family": route_family,
        "provider_route_family": route_family,
        "request_method": "POST",
        "base_url": base_url,
        "relative_path": relative_path,
        "sdk_call": sdk_call,
        "model_identifier_source": model_identifier_source,
        "model_identifier_shape": _shape_debug_value(model_identifier),
        "endpoint_id_shape": _shape_debug_value(endpoint_id),
        "model_shape": _shape_debug_value(model),
        "resource_id_shape": _shape_debug_value(resource_id),
        "app_id_shape": _shape_debug_value(app_id),
        "voice_location": voice_location,
        "voice_shape": _shape_debug_value(voice),
        "style_shape": _shape_debug_value(style),
        "response_format": response_format,
    }
    if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
        input_keys = ["text", "voice", "format"]
        if _normalize_optional_text(instruction):
            input_keys.append("instruction")
        if speech_rate is not None:
            input_keys.append("rate")
        if pitch_rate is not None:
            input_keys.append("pitch")
        if volume is not None:
            input_keys.append("volume")
        debug.update(
            {
                "instruction_location": instruction_location,
                "instruction_shape": _shape_debug_value(instruction),
                "speech_rate": speech_rate,
                "pitch_rate": pitch_rate,
                "volume": volume,
                "request_input_keys": input_keys,
                "style_draft_in_request": bool(_normalize_optional_text(instruction)),
            }
        )
    else:
        debug["style_draft_in_request"] = bool(_normalize_optional_text(style))
    return debug


def _resolve_tts_runtime_options(
    config: dict[str, Any],
    *,
    tts_override: dict[str, Any] | None,
) -> dict[str, Any]:
    overrides = tts_override or {}
    return {
        "voice": overrides["voice"] if "voice" in overrides else _nested_get(config, "tts", "voice"),
        "style": overrides["style"] if "style" in overrides else _nested_get(config, "tts", "style"),
        "instruction": (
            overrides["instruction"]
            if "instruction" in overrides
            else _nested_get(config, "tts", "instruction")
        ),
        "speech_rate": _coerce_float_or_none(
            overrides["speech_rate"]
            if "speech_rate" in overrides
            else _nested_get(config, "tts", "speech_rate")
        ),
        "pitch_rate": _coerce_float_or_none(
            overrides["pitch_rate"]
            if "pitch_rate" in overrides
            else _nested_get(config, "tts", "pitch_rate")
        ),
        "volume": _coerce_int_or_none(
            overrides["volume"] if "volume" in overrides else _nested_get(config, "tts", "volume")
        ),
    }


def _get_aliyun_tts_style_probe_text(config: dict[str, Any]) -> tuple[str, str]:
    configured_text = _normalize_optional_text(_nested_get(config, "tts_style_probe", "text"))
    if configured_text:
        return configured_text, "tts_style_probe.text"
    return DEFAULT_ALIYUN_TTS_STYLE_PROBE_TEXT, "code_default"


def _load_tts_style_probe_variants(
    *,
    config: dict[str, Any],
    default_variants: tuple[dict[str, Any], ...],
    section_prefix: str,
) -> list[dict[str, Any]]:
    variants: list[dict[str, Any]] = []
    for default_variant in default_variants:
        section_name = f"{section_prefix}{default_variant['variant_id']}"
        section = _nested_get(config, section_name) or {}
        variant = dict(default_variant)
        if isinstance(section, dict):
            variant["label"] = _normalize_optional_text(section.get("label")) or variant["label"]
            variant["intent"] = _normalize_optional_text(section.get("intent")) or variant["intent"]
            variant["instruction"] = (
                _normalize_optional_text(section.get("instruction")) or variant["instruction"]
            )
            variant["why_recommended"] = (
                _normalize_optional_text(section.get("why_recommended"))
                or _normalize_optional_text(variant.get("why_recommended"))
            )
            speech_rate = _coerce_float_or_none(section.get("speech_rate"))
            if speech_rate is not None:
                variant["speech_rate"] = speech_rate
            pitch_rate = _coerce_float_or_none(section.get("pitch_rate"))
            if pitch_rate is not None:
                variant["pitch_rate"] = pitch_rate
            volume = _coerce_int_or_none(section.get("volume"))
            if volume is not None:
                variant["volume"] = volume
            if "recommended" in section:
                variant["recommended"] = bool(section.get("recommended"))
        variants.append(variant)
    return variants


def _get_recommended_tts_style_variant(variants: list[dict[str, Any]]) -> dict[str, Any] | None:
    for variant in variants:
        if variant.get("recommended"):
            return variant
    if variants:
        return variants[0]
    return None


def _resolve_recommended_tts_style_variant(
    *,
    config: dict[str, Any],
    variants: list[dict[str, Any]],
    round_section_name: str | None,
) -> dict[str, Any] | None:
    configured_variant_id = ""
    if round_section_name:
        configured_variant_id = _normalize_optional_text(
            _nested_get(config, round_section_name, "recommended_variant_id")
        )
    if configured_variant_id:
        for variant in variants:
            if str(variant.get("variant_id")) == configured_variant_id:
                return variant
    return _get_recommended_tts_style_variant(variants)


def _resolve_tts_style_recommendation_reason(
    *,
    config: dict[str, Any],
    round_section_name: str | None,
    recommended_variant: dict[str, Any] | None,
) -> str:
    if round_section_name:
        configured_reason = _normalize_optional_text(
            _nested_get(config, round_section_name, "recommendation_reason")
        )
        if configured_reason:
            return configured_reason
    if recommended_variant is None:
        return ""
    return _normalize_optional_text(recommended_variant.get("why_recommended"))


def _summarize_tts_style_variant_status(variants: list[dict[str, Any]]) -> str:
    if not variants:
        return STATUS_BLOCKED
    if all(item.get("status") == STATUS_SUCCESS for item in variants):
        return STATUS_SUCCESS
    if any(item.get("status") == STATUS_FAILED for item in variants):
        return STATUS_FAILED
    return STATUS_BLOCKED


def _normalize_optional_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _coerce_float_or_none(value: Any) -> float | None:
    normalized = _normalize_optional_text(value)
    if not normalized:
        return None
    try:
        return float(normalized)
    except ValueError:
        return None


def _coerce_int_or_none(value: Any) -> int | None:
    normalized = _normalize_optional_text(value)
    if not normalized:
        return None
    try:
        return int(float(normalized))
    except ValueError:
        return None


def _shape_debug_value(value: Any) -> dict[str, Any]:
    if value is None:
        raw = ""
    else:
        raw = str(value).strip()
    return {
        "present": bool(raw),
        "length": len(raw),
        "has_digit": any(char.isdigit() for char in raw),
        "has_dash": "-" in raw,
        "prefix": raw[:2],
        "suffix": raw[-2:] if raw else "",
    }


def _sanitize_message(message: str, config: dict[str, Any]) -> str:
    sanitized = message.strip()
    api_key = _nested_get(config, "auth", "api_key")
    if api_key:
        sanitized = sanitized.replace(str(api_key), "***")
    return sanitized[:500]


def _looks_like_timeout_message(message: str) -> bool:
    normalized = message.lower()
    return "timeout" in normalized or "timed out" in normalized


def _normalize_timeout_blocked_reason(message: str) -> str:
    normalized = message.strip()
    if "timeout" in normalized.lower():
        return normalized
    return f"timeout: {normalized}" if normalized else "timeout"


def _extract_request_id(response: Any) -> str | None:
    headers = getattr(response, "headers", None)
    if headers is None and hasattr(response, "response"):
        headers = getattr(response.response, "headers", None)
    if headers is None:
        return None
    return headers.get("x-request-id") or headers.get("x-tt-logid")


def _merge_known_issues(*issue_groups: list[str]) -> list[str]:
    merged: list[str] = []
    for issues in issue_groups:
        for issue in issues:
            if issue and issue not in merged:
                merged.append(issue)
    return merged


def _merge_unique_values(*value_groups: list[str]) -> list[str]:
    merged: list[str] = []
    for values in value_groups:
        for value in values:
            if value and value not in merged:
                merged.append(value)
    return merged


def _combine_stage_statuses(statuses: list[str], *, dry_run: bool = False) -> str:
    if dry_run:
        return STATUS_PLANNED
    filtered = [status for status in statuses if status]
    if not filtered:
        return STATUS_NOT_STARTED
    if all(status == STATUS_SKIPPED for status in filtered):
        return STATUS_SKIPPED
    filtered = [status for status in filtered if status != STATUS_SKIPPED]
    if not filtered:
        return STATUS_SUCCESS
    if any(status == STATUS_FAILED for status in filtered):
        return STATUS_FAILED
    if any(status == STATUS_BLOCKED for status in filtered):
        return STATUS_BLOCKED
    if all(status == STATUS_SUCCESS for status in filtered):
        return STATUS_SUCCESS
    if any(status == STATUS_PLANNED for status in filtered):
        return STATUS_PLANNED
    return STATUS_NOT_STARTED


def _resolve_formal_tts_baseline(config: dict[str, Any]) -> dict[str, Any]:
    baseline = dict(DEFAULT_FORMAL_TTS_BASELINE)
    configured_profile = _normalize_optional_text(_nested_get(config, "tts", "baseline_profile"))
    if configured_profile:
        baseline["profile_id"] = configured_profile
    return baseline


def resolve_ffmpeg_binary() -> str:
    system_ffmpeg = shutil.which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg
    bundled_ffmpeg = ROOT / "node_modules" / "ffmpeg-static" / "ffmpeg"
    if bundled_ffmpeg.exists():
        return str(bundled_ffmpeg)
    raise RuntimeError("缺少 ffmpeg，可先安装依赖或补齐本地 ffmpeg 可执行文件。")


def run_subprocess(args: list[str]) -> None:
    subprocess.run(args, check=True)


def concatenate_audio_files(input_paths: list[pathlib.Path], output_path: pathlib.Path) -> None:
    if not input_paths:
        raise RuntimeError("没有可拼接的音频分段。")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        ffmpeg_binary = resolve_ffmpeg_binary()
    except RuntimeError:
        output_path.write_bytes(b"".join(path.read_bytes() for path in input_paths))
        return
    concat_list_path = output_path.parent / "concat_inputs.txt"
    concat_list_path.write_text(
        "".join(f"file '{path.resolve()}'\n" for path in input_paths),
        encoding="utf-8",
    )
    try:
        try:
            run_subprocess(
                [
                    ffmpeg_binary,
                    "-y",
                    "-f",
                    "concat",
                    "-safe",
                    "0",
                    "-i",
                    str(concat_list_path),
                    "-codec:a",
                    "libmp3lame",
                    "-b:a",
                    "128k",
                    str(output_path),
                ]
            )
        except subprocess.CalledProcessError:
            output_path.write_bytes(b"".join(path.read_bytes() for path in input_paths))
    finally:
        concat_list_path.unlink(missing_ok=True)


def seconds_to_srt(value: float) -> str:
    milliseconds = round(value * 1000)
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    seconds, milliseconds = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"


def _build_preview_slides(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    segment_assets = {
        asset.get("segment_id"): asset
        for asset in _nested_get(manifest, "generation", "visual_generation", "segment_assets")
        or []
        if asset.get("segment_id")
    }
    raw_slides: list[dict[str, Any]] = []

    for segment in manifest.get("segments", []):
        segment_id = segment["segment_id"]
        asset = segment_assets.get(segment_id, {})
        image_path = asset.get("image_asset_path")
        video_path = asset.get("video_asset_path")
        planned_duration = segment["timeline"]["planned_duration_seconds"]

        if segment_id == "seg01":
            raw_slides.append(
                {
                    "segment_id": segment_id,
                    "role": "hook",
                    "eyebrow": "问题卡点",
                    "headline": segment["caption_text"],
                    "support": "先把卡点看清，再决定怎么推进。",
                    "detail": segment["visual_intent"],
                    "chips": ["想法很多", "流程没拉齐"],
                    "accent": "#2563EB",
                    "background": "#F5F7FB",
                    "duration": planned_duration,
                    "background_image_path": image_path,
                    "background_video_path": None,
                }
            )
            continue

        if segment_id == "seg02":
            raw_slides.append(
                {
                    "segment_id": segment_id,
                    "role": "process",
                    "eyebrow": "收束动作",
                    "headline": segment["caption_text"],
                    "support": "散乱字段一进表，后面这条链就能接手。",
                    "detail": "目标、输入、输出归到同一张 SOP 表后，这一步已经能直接交接。",
                    "chips": ["目标", "输入", "输出"],
                    "accent": "#0F766E",
                    "background": "#F1FAF8",
                    "duration": planned_duration,
                    "background_image_path": image_path if not video_path else None,
                    "background_video_path": video_path,
                }
            )
            continue

        raw_slides.append(
            {
                "segment_id": segment_id,
                "role": "outcome",
                "eyebrow": "结果落点",
                "headline": segment["caption_text"],
                "support": "先出可审样片，再逐轮压质量。",
                "detail": segment["visual_intent"],
                "chips": ["先稳住样片", "再逐轮提质"],
                "accent": "#C2410C",
                "background": "#FFF7ED",
                "duration": planned_duration,
                "background_image_path": image_path,
                "background_video_path": video_path,
            }
        )

    total = len(raw_slides)
    slides: list[dict[str, Any]] = []
    for index, slide in enumerate(raw_slides, start=1):
        slides.append(
            {
                "sequence": index,
                "total": total,
                **slide,
            }
        )
    return slides


def _voiceover_known_issues(voiceover: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if voiceover.get("status") == STATUS_BLOCKED and voiceover.get("blocked_reason"):
        issues.append("正式配音 blocked：" + voiceover["blocked_reason"])
    if voiceover.get("status") == STATUS_FAILED and voiceover.get("error_message"):
        issues.append("正式配音 failed：" + voiceover["error_message"])
    return issues


def _visual_generation_known_issues(visual_generation: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if visual_generation.get("status") == STATUS_BLOCKED and visual_generation.get("blocked_reason"):
        issues.append("视觉生成 blocked：" + visual_generation["blocked_reason"])
    if visual_generation.get("status") == STATUS_FAILED and visual_generation.get("error_message"):
        issues.append("视觉生成 failed：" + visual_generation["error_message"])
    if visual_generation.get("missing_implementations"):
        issues.append(
            "视觉生成 provider 尚未接入："
            + "、".join(visual_generation["missing_implementations"])
        )
    cloud = visual_generation.get("cloud", {})
    if cloud.get("status") == STATUS_BLOCKED and cloud.get("blocked_reason"):
        issues.append("cloud visual generation blocked：" + cloud["blocked_reason"])
    if cloud.get("missing_implementations"):
        issues.append(
            "cloud visual generation provider 尚未接入："
            + "、".join(cloud["missing_implementations"])
        )
    portrait_detect = visual_generation.get("portrait_detect", {})
    if portrait_detect.get("status") == STATUS_BLOCKED and portrait_detect.get("blocked_reason"):
        issues.append("真人开口检测 blocked：" + portrait_detect["blocked_reason"])
    portrait_video = visual_generation.get("portrait_video_generation", {})
    if portrait_video.get("status") == STATUS_BLOCKED and portrait_video.get("blocked_reason"):
        issues.append("真人开口视频 blocked：" + portrait_video["blocked_reason"])
    return issues


def _cloud_assembly_known_issues(cloud_assembly: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if cloud_assembly.get("status") == STATUS_BLOCKED and cloud_assembly.get("blocked_reason"):
        issues.append("cloud assembly blocked：" + cloud_assembly["blocked_reason"])
    if cloud_assembly.get("status") == STATUS_FAILED and cloud_assembly.get("error_message"):
        issues.append("cloud assembly failed：" + cloud_assembly["error_message"])
    return issues


def _local_assembly_known_issues(local_assembly: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if local_assembly.get("status") == STATUS_BLOCKED and local_assembly.get("blocked_reason"):
        issues.append("正式本地 assembly blocked：" + local_assembly["blocked_reason"])
    if local_assembly.get("status") == STATUS_FAILED and local_assembly.get("error_message"):
        issues.append("正式本地 assembly failed：" + local_assembly["error_message"])
    return issues


def _assembly_preview_known_issues(preview: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if preview.get("status") == STATUS_BLOCKED and preview.get("blocked_reason"):
        issues.append("本地 preview 组装 blocked：" + preview["blocked_reason"])
    if preview.get("status") == STATUS_FAILED and preview.get("error_message"):
        issues.append("本地 preview 组装 failed：" + preview["error_message"])
    return issues
