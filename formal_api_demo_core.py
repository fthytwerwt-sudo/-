from __future__ import annotations

import copy
import json
import pathlib
import shutil
import subprocess
import urllib.error
import urllib.request
from typing import Any

try:
    import openai
    from openai import OpenAI
except ImportError:  # pragma: no cover - exercised only when dependency is absent.
    openai = None
    OpenAI = None


ROOT = pathlib.Path(__file__).resolve().parent
FORMAL_CASE_PATH = ROOT / "cases" / "formal_api_demo.md"
FORMAL_EXAMPLE_CONFIG_PATH = ROOT / "config" / "formal_api_demo.example.toml"
DEFAULT_FORMAL_LOCAL_CONFIG_PATH = ROOT / "config" / "formal_api_demo.local.toml"
DEFAULT_FORMAL_OUTPUT_DIR = ROOT / "dist" / "formal_api_demo"

MANIFEST_SCHEMA_VERSION = "formal_api_demo_manifest/v1"
RESULT_SUMMARY_SCHEMA_VERSION = "formal_api_demo_result_summary/v1"

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
DEFAULT_ALIYUN_TTS_STYLE_PROBE_TEXT = (
    "这套方案表面上堆满了参数，真正决定上限的其实只有供电、火控和协同链路。"
    "前两项还能补，第三项一旦掉队，再新的壳子也只是好看。"
    "说得更直白一点，它不是没亮点，是关键战力根本没站住。"
)
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

    return {
        "theme": _section_text(raw_sections["主题"]),
        "total_duration_seconds": total_duration,
        "aspect_ratio": aspect_ratio,
        "target_scenario": _section_text(raw_sections["目标场景"]),
        "target_user": _section_text(raw_sections["目标用户"]),
        "quality_requirements": _section_list(raw_sections["全局质量要求"]),
        "hook": _section_text(raw_sections["Hook"]),
        "ending": _section_text(raw_sections["结尾落点"]),
        "segments": segments,
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

    if dry_run:
        tts_probe["current_missing_prerequisites"] = tts_gate["missing_prerequisites"]
        voiceover["current_missing_prerequisites"] = tts_gate["missing_prerequisites"]
        visual_generation["current_missing_prerequisites"] = visual_gate["missing_prerequisites"]
        visual_generation["missing_implementations"] = visual_gate["missing_implementations"]
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)
        manifest = apply_voiceover_to_manifest(manifest, voiceover)
        manifest = apply_caption_assets_to_manifest(manifest, caption_assets)
        manifest = apply_visual_generation_to_manifest(manifest, visual_generation)
    else:
        if tts_gate["status"] == STATUS_SUCCESS:
            tts_probe = execute_tts_probe(
                video_spec=video_spec,
                config=config,
                output_dir=output_dir,
            )
        else:
            tts_probe = build_blocked_tts_probe(video_spec, tts_gate)
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)

        if tts_probe["status"] == STATUS_SUCCESS:
            voiceover = execute_formal_voiceover_generation(
                video_spec=video_spec,
                config=config,
                output_dir=output_dir,
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
    preview_result = build_default_assembly_preview(output_dir)
    if not dry_run:
        preview_result = execute_local_preview_assembly(
            manifest=manifest,
            output_dir=output_dir,
        )
    local_assembly_status = STATUS_PLANNED if dry_run else preview_result["status"]
    cloud_assembly_status = STATUS_PLANNED if dry_run else assembly_gate["status"]
    overall_status = _combine_stage_statuses(
        [
            manifest.get("generation", {}).get("status", STATUS_NOT_STARTED),
            local_assembly_status,
        ],
        dry_run=dry_run,
    )
    manifest["assembly"] = {
        "status": local_assembly_status,
        "task_id": None,
        "resource_id": None,
        "output_id": None,
        "delivery_mode": "local_mp4",
        "delivery_video_path": preview_result.get("video_path")
        if local_assembly_status == STATUS_SUCCESS
        else None,
        "local": preview_result,
        "cloud": {
            "status": cloud_assembly_status,
            "blocked_reason": "" if dry_run else assembly_gate.get("blocked_reason", ""),
            "missing_prerequisites": assembly_gate["missing_prerequisites"],
            "missing_implementations": assembly_gate["missing_implementations"],
        },
        "preview": preview_result,
    }
    manifest["status_summary"] = {
        "generation": manifest.get("generation", {}).get("status", STATUS_NOT_STARTED),
        "local_assembly": local_assembly_status,
        "cloud_assembly": cloud_assembly_status,
        "overall_status": overall_status,
    }
    manifest["current_status"] = overall_status
    manifest["known_issues"] = _merge_known_issues(
        manifest.get("known_issues", []),
        _assembly_preview_known_issues(preview_result),
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
    missing = _generation_missing_prerequisites(
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
            if not _is_missing_secret(_nested_get(config, "auth", "api_key"))
            else "fail",
            "detail": "TTS probe 从 local 配置读取访问密钥，不回显真实值。",
        },
        {
            "name": "tts_voice_present",
            "status": "pass"
            if not _is_missing_secret(_nested_get(config, "tts", "voice"))
            else "fail",
            "detail": "当前 TTS probe 默认要求显式 voice，避免调用时隐式失败。",
        },
        {
            "name": "local_fallback_forbidden",
            "status": "pass"
            if _nested_get(config, "quality_gate", "allow_local_fallback") is False
            else "fail",
            "detail": "正式版骨架禁止回退到本地 say / ffmpeg / Swift 链路。",
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
    elif missing:
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
    overall_status = tts_gate["status"] if not dry_run else STATUS_PLANNED
    missing = list(tts_gate["missing_prerequisites"])
    missing_implementations = list(tts_gate["missing_implementations"])
    failure_reason = tts_gate.get("failure_reason", "")
    blocked_reason = tts_gate.get("blocked_reason", "")

    return {
        "gate_name": "generation_gate",
        "status": overall_status,
        "scope": "tts_voiceover_and_local_visual_plan",
        "allow_execution": not dry_run,
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
        },
        "stage_gates": {
            "tts_probe": tts_gate,
            "visual_generation": visual_gate,
        },
        "checks": tts_gate["checks"] + visual_gate["checks"],
        "notes": [
            "当前 generation 会继续执行 TTS probe、整段配音、字幕与视觉计划，不再只停在 TTS probe。",
            "本地 0-1 阶段默认以视觉计划可落出为成功口径；cloud visual generation 降级为可选增强项。",
            "generation 顶层状态按本地可交付链路统计，不再被 cloud visual generation 的未配置状态直接压成 blocked。",
        ],
    }


def _evaluate_visual_generation_gate(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    missing: list[str] = []
    implementation_missing: list[str] = []
    needs_image = any(segment.get("needs_image") for segment in video_spec.get("segments", []))
    needs_video = any(segment.get("needs_video") for segment in video_spec.get("segments", []))
    if not has_local_config:
        missing.append("local_config_file")
    if _is_missing_secret(_nested_get(config, "auth", "api_key")):
        missing.append("api_key")
    if _is_missing_secret(_nested_get(config, "provider", "region")):
        missing.append("provider_region")
    if needs_image and _is_missing_secret(_nested_get(config, "image_generation", "model")):
        missing.append("image_generation_model")
    if needs_video and _is_missing_secret(_nested_get(config, "video_generation", "model")):
        missing.append("video_generation_model")
    if needs_image:
        implementation_missing.append("image_generation_provider_implementation")
    if needs_video:
        implementation_missing.append("video_generation_provider_implementation")

    checks = [
        {
            "name": "visual_segments_present",
            "status": "pass" if video_spec.get("segments") else "fail",
            "detail": f"segments={len(video_spec.get('segments', []))}",
        },
        {
            "name": "image_model_present_when_required",
            "status": "pass"
            if not needs_image or not _is_missing_secret(_nested_get(config, "image_generation", "model"))
            else "fail",
            "detail": "有图片段落时必须显式提供 image_generation.model。",
        },
        {
            "name": "video_model_present_when_required",
            "status": "pass"
            if not needs_video or not _is_missing_secret(_nested_get(config, "video_generation", "model"))
            else "fail",
            "detail": "有视频段落时必须显式提供 video_generation.model。",
        },
    ]

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif missing:
        status = STATUS_SKIPPED
        blocked_reason = "cloud visual generation 未配置；当前阶段继续沿用视觉计划 + 本地 assembly。"
    else:
        status = STATUS_BLOCKED
        blocked_reason = "cloud visual generation provider implementation 尚未接入；当前先落视觉计划与本地预览素材。"

    return {
        "gate_name": "visual_generation_gate",
        "status": status,
        "allow_execution": not dry_run and not missing,
        "blocked_reason": blocked_reason,
        "failure_reason": "",
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "checks": checks,
        "notes": [
            "visual_generation Gate 仅代表 cloud visual generation 状态。",
            "当前阶段即使 cloud visual generation skipped / blocked，仍允许落 visual plan，避免本地链路继续停在纯骨架。",
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
    implementation_missing = ["provider_assembly_implementation"]
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
            "name": "local_fallback_forbidden",
            "status": "pass"
            if _nested_get(config, "quality_gate", "allow_local_fallback") is False
            else "fail",
            "detail": "正式组装仍以云端为目标；本地 preview 只作预览，不得冒充正式云端成功。",
        },
    ]

    cloud_optional_missing = {
        "space_name",
        "assembly_template_id",
    }
    blocking_missing = [
        item for item in missing if item not in cloud_optional_missing
    ]

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif blocking_missing:
        status = STATUS_BLOCKED
        blocked_reason = "缺少本地组装前提：" + "、".join(blocking_missing)
    elif missing:
        status = STATUS_SKIPPED
        blocked_reason = "cloud assembly 未配置；当前阶段默认交付本地 mp4。"
    else:
        status = STATUS_BLOCKED
        blocked_reason = "正式云端组装实现尚未接入；当前阶段默认交付本地 mp4。"

    return {
        "gate_name": "assembly_gate",
        "status": status,
        "allow_execution": not dry_run and not missing and False,
        "blocked_reason": blocked_reason,
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "checks": checks,
        "notes": [
            "assembly Gate 仅代表 cloud assembly 状态，不再代表当前阶段整体交付状态。",
            "manifest 是修正循环和复审的事实锚点，assembly 不得绕开 manifest 自由猜测。",
            "当前阶段默认交付本地 mp4；cloud assembly 降级为可选增强项。",
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
                },
                "provider_plan": {
                    "tts_provider": _get_tts_provider_name(config),
                    "tts_api_route_family": _get_tts_api_route_family(config),
                    "tts_model": _nested_get(config, "tts", "model"),
                    "tts_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
                    "tts_resource_id": _nested_get(config, "tts", "resource_id"),
                    "image_model": _nested_get(config, "image_generation", "model"),
                    "video_model": _nested_get(config, "video_generation", "model"),
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
        },
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
            "delivery_mode": "local_mp4",
            "delivery_video_path": None,
            "local": build_default_assembly_preview(output_dir),
            "cloud": {
                "status": STATUS_NOT_STARTED,
                "blocked_reason": "",
                "missing_prerequisites": [],
                "missing_implementations": [],
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
            or generation_gate.get("blocked_reason", "")
        ),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "generation_gate": str(output_dir / "generation_gate.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "tts_audio": tts_probe.get("audio_path"),
            "voiceover_audio": voiceover.get("audio_path"),
            "script": captions.get("script_path"),
            "captions": captions.get("captions_path"),
            "visual_plan": visual_generation.get("plan_path"),
        },
        "next_action_hint": _generation_next_action_hint(generation_gate, tts_probe, dry_run),
        "current_missing_prerequisites": generation_gate["missing_prerequisites"],
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
        "preview_target": str(pathlib.Path(_nested_get(config, "output", "dist_dir") or DEFAULT_FORMAL_OUTPUT_DIR) / "assembly" / "formal_api_demo_preview.mp4"),
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run=True),
    }


def build_assembly_result_summary(
    manifest: dict[str, Any],
    assembly_gate: dict[str, Any],
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    generation_status = manifest.get("generation", {}).get("status", STATUS_NOT_STARTED)
    preview = manifest.get("assembly", {}).get("preview", {})
    local_status = STATUS_PLANNED if dry_run else preview.get("status", STATUS_NOT_STARTED)
    cloud_status = STATUS_PLANNED if dry_run else assembly_gate["status"]
    overall_status = _combine_stage_statuses(
        [
            generation_status,
            local_status,
        ],
        dry_run=dry_run,
    )
    return {
        "schema_version": RESULT_SUMMARY_SCHEMA_VERSION,
        "stage": "assembly",
        "overall_status": overall_status,
        "generation_status": generation_status,
        "assembly_status": local_status,
        "local_assembly_status": local_status,
        "cloud_assembly_status": cloud_status,
        "assembly_preview_status": preview.get("status", STATUS_NOT_STARTED),
        "machine_gate_result": {
            "generation_gate": manifest.get("machine_gate", {})
            .get("generation_gate", {})
            .get("status", STATUS_NOT_STARTED),
            "assembly_gate": assembly_gate["status"],
        },
        "blocked_reason": ""
        if dry_run
        else (
            preview.get("blocked_reason")
            or preview.get("error_message")
            or (assembly_gate.get("blocked_reason", "") if overall_status == STATUS_BLOCKED else "")
        ),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "assembly_gate": str(output_dir / "assembly_gate.json"),
            "assembly_plan": str(output_dir / "assembly_plan.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "final_video": preview.get("video_path") if local_status == STATUS_SUCCESS else None,
            "preview_video": preview.get("video_path"),
            "preview_manifest": preview.get("preview_manifest_path"),
        },
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run),
        "current_missing_prerequisites": []
        if overall_status == STATUS_SUCCESS
        else assembly_gate["missing_prerequisites"],
        "cloud_missing_prerequisites": assembly_gate["missing_prerequisites"],
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
    return {
        "status": STATUS_PLANNED,
        "delivery_mode": "local_visual_plan",
        "provider": _nested_get(config, "provider", "name"),
        "image_model": _nested_get(config, "image_generation", "model"),
        "video_model": _nested_get(config, "video_generation", "model"),
        "plan_path": None,
        "preview_storyboard_path": None,
        "segment_assets": [
            {
                "segment_id": segment["segment_id"],
                "needs_image": segment["needs_image"],
                "needs_video": segment["needs_video"],
                "image_prompt": "",
                "video_prompt": "",
                "status": STATUS_NOT_STARTED,
            }
            for segment in video_spec.get("segments", [])
        ],
        "blocked_reason": "",
        "failure_reason": "",
        "current_missing_prerequisites": [],
        "missing_implementations": [],
        "cloud": {
            "status": STATUS_NOT_STARTED,
            "blocked_reason": "",
            "missing_prerequisites": [],
            "missing_implementations": [],
        },
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
        segment["output_slots"]["visual_uri"] = asset.get("preview_visual_ref")
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
) -> dict[str, Any]:
    probe = build_default_tts_probe(video_spec)
    if probe_text is not None:
        probe["probe_text"] = probe_text.strip()
        probe["probe_text_source"] = probe_text_source or "runtime_override"
    route_family = _get_tts_api_route_family(config)
    model_identifier = _get_tts_model_identifier(config, route_family=route_family)
    base_url = _build_tts_base_url(config, route_family)
    response_format = (_nested_get(config, "tts", "response_format") or "mp3").strip() or "mp3"
    tts_options = _resolve_tts_runtime_options(config, tts_override=tts_override)
    audio_path = output_dir / "tts" / f"{output_stem}.{response_format}"
    probe.update(
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
                probe=probe,
                audio_path=audio_path,
                base_url=base_url,
                model_identifier=model_identifier,
                response_format=response_format,
                tts_options=tts_options,
            )
            probe.update(
                {
                    "status": STATUS_SUCCESS,
                    "audio_path": str(audio_path),
                    "request_id": request_id,
                }
            )
            return probe

        client = OpenAI(
            api_key=_nested_get(config, "auth", "api_key"),
            base_url=base_url,
        )
        request_kwargs: dict[str, Any] = {
            "model": model_identifier,
            "voice": tts_options["voice"],
            "input": probe["probe_text"],
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
            probe.update(
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
        probe.update(
            {
                "status": status,
                "blocked_reason": error_message if status == STATUS_BLOCKED else "",
                "failure_reason": failure_reason,
                "http_status_code": http_status_code,
                "error_code": error_code,
                "error_message": error_message,
            }
        )

    return probe


def execute_formal_voiceover_generation(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    voiceover = build_default_voiceover_generation(video_spec, config)
    segment_results: list[dict[str, Any]] = []
    segment_audio_paths: list[pathlib.Path] = []

    for segment in video_spec.get("segments", []):
        probe = execute_tts_probe(
            video_spec=video_spec,
            config=config,
            output_dir=output_dir,
            probe_text=segment["voiceover_text"],
            probe_text_source=f"{segment['segment_id']}_voiceover",
            output_stem=f"segment_{segment['segment_id']}",
        )
        segment_result = {
            "segment_id": segment["segment_id"],
            "status": probe.get("status", STATUS_FAILED),
            "audio_path": probe.get("audio_path"),
            "request_id": probe.get("request_id"),
            "failure_reason": probe.get("failure_reason", ""),
            "error_message": probe.get("error_message", ""),
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
) -> dict[str, Any]:
    visual_generation = build_default_visual_generation(video_spec, config)
    plan_path = output_dir / "visual_generation_plan.json"
    preview_storyboard_path = output_dir / "preview_storyboard.json"
    segment_assets: list[dict[str, Any]] = []

    for index, segment in enumerate(video_spec.get("segments", []), start=1):
        image_prompt = ""
        video_prompt = ""
        if segment["needs_image"]:
            image_prompt = (
                f"{segment['visual_intent']}。保持 9:16 竖版，PPT 卡片式信息层级，"
                "中文 AI 项目讲解场景，避免写实人物和广告感。"
            )
        if segment["needs_video"]:
            video_prompt = (
                f"{segment['visual_intent']}。镜头应表现信息从散乱到收束，"
                "节奏克制，适合 9:16 中文案例讲解短视频。"
            )
        asset_status = STATUS_PLANNED if visual_gate["status"] == STATUS_PLANNED else STATUS_BLOCKED
        if not visual_gate["missing_prerequisites"] and visual_gate["status"] == STATUS_BLOCKED:
            asset_status = STATUS_BLOCKED
        segment_assets.append(
            {
                "segment_id": segment["segment_id"],
                "sequence": index,
                "needs_image": segment["needs_image"],
                "needs_video": segment["needs_video"],
                "image_prompt": image_prompt,
                "video_prompt": video_prompt,
                "preview_visual_ref": f"preview_slide_{index}",
                "status": asset_status,
            }
        )

    cloud_status = visual_gate["status"]
    cloud_blocked_reason = visual_gate.get("blocked_reason", "")
    visual_generation.update(
        {
            "status": STATUS_SUCCESS,
            "plan_path": str(plan_path),
            "preview_storyboard_path": str(preview_storyboard_path),
            "segment_assets": segment_assets,
            "blocked_reason": "",
            "failure_reason": "",
            "current_missing_prerequisites": [],
            "missing_implementations": [],
            "cloud": {
                "status": cloud_status,
                "blocked_reason": cloud_blocked_reason,
                "missing_prerequisites": visual_gate.get("missing_prerequisites", []),
                "missing_implementations": visual_gate.get("missing_implementations", []),
            },
        }
    )
    write_json(
        plan_path,
        {
            "schema_version": "formal_api_demo_visual_plan/v1",
            "status": visual_generation["status"],
            "provider": visual_generation["provider"],
            "image_model": visual_generation["image_model"],
            "video_model": visual_generation["video_model"],
            "current_missing_prerequisites": visual_generation["current_missing_prerequisites"],
            "missing_implementations": visual_generation["missing_implementations"],
            "cloud": visual_generation["cloud"],
            "segment_assets": segment_assets,
        },
    )
    write_json(
        preview_storyboard_path,
        {
            "schema_version": "formal_api_demo_preview_storyboard/v1",
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
    return visual_generation


def execute_local_preview_assembly(
    manifest: dict[str, Any],
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
    preview_manifest = {
        "width": 1080,
        "height": 1920,
        "fps": 10,
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

    preview.update(
        {
            "status": STATUS_SUCCESS,
            "video_path": str(preview_video_path),
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

    return {
        "segment_heading": block["heading"],
        "segment_id": values["段落ID"].strip(),
        "planned_duration_seconds": _parse_seconds(values["计划时长"]),
        "goal": values["段目标"].strip(),
        "voiceover_text": values["配音文案"].strip(),
        "caption_text": values["字幕文案"].strip(),
        "visual_intent": values["画面意图"].strip(),
        "needs_image": _parse_yes_no(values["需要图片"]),
        "needs_video": _parse_yes_no(values["需要视频"]),
        "allow_real_desktop_footage": _parse_yes_no(values["允许真实桌面素材"]),
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
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            section_name = stripped[1:-1].strip()
            current_section = result.setdefault(section_name, {})
            continue
        if "=" not in stripped or current_section is None:
            continue
        key, raw_value = stripped.split("=", 1)
        current_section[key.strip()] = _parse_toml_value(raw_value.strip())

    return result


def _parse_toml_value(raw_value: str) -> Any:
    if raw_value.startswith('"') and raw_value.endswith('"'):
        return raw_value[1:-1]
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
    if _is_missing_secret(_nested_get(config, "storage", "space_name")):
        missing.append("space_name")
    if _is_missing_secret(_nested_get(config, "assembly", "template_id")):
        missing.append("assembly_template_id")
    if _is_missing_secret(_nested_get(config, "provider", "region")):
        missing.append("provider_region")
    if not manifest.get("segments"):
        missing.append("manifest_segments")
    if manifest.get("generation", {}).get("voiceover", {}).get("status") != STATUS_SUCCESS:
        missing.append("voiceover_assets_not_ready")
    if manifest.get("generation", {}).get("captions", {}).get("status") != STATUS_SUCCESS:
        missing.append("subtitle_assets_not_ready")
    if manifest.get("generation", {}).get("visual_generation", {}).get("status") != STATUS_SUCCESS:
        missing.append("visual_assets_not_ready")
    return missing


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
        issues.append("当前 TTS 调用已接通；cloud visual generation / cloud assembly 仍作为后续增强项单独记录。")
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
        return "当前为 dry-run；下一步应先确认 TTS 前提，再执行真实 generation。本阶段 cloud visual generation 不再阻断本地出片。"
    if gate["missing_prerequisites"]:
        if route_family == TTS_ROUTE_FAMILY_ALIYUN_BAILIAN_COSYVOICE:
            return "先补齐阿里百炼的 API Key、tts.model 和 voice，再进入真实 TTS probe。"
        if route_family == TTS_ROUTE_FAMILY_EDGE_GATEWAY:
            return "先补齐 Edge Gateway 的访问密钥、tts.model 和 voice，再进入真实 TTS probe。"
        if route_family == TTS_ROUTE_FAMILY_DOUBAO_OPENSPEECH:
            return "先补齐 OpenSpeech 的 app_id、Access-Key、resource_id 和 voice；不要继续按 Ark 问题处理。"
        return "先补齐 Ark route family 所需的 API Key、region、TTS model/endpoint 和 voice，再进入真实 TTS probe。"
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
        return "当前 generation 已可落出脚本、配音、字幕和视觉计划；下一步应继续执行本地 assembly，稳定产出本地 mp4。"
    return "当前已具备部分 generation 前提；下一步可执行真实 generation，并把失败压到字段或 provider 层。"


def _assembly_next_action_hint(gate: dict[str, Any], dry_run: bool) -> str:
    if dry_run:
        return "当前为 assembly dry-run；下一步应实际运行非 dry-run，验证本地 mp4 是否可稳定落出。"
    if gate["status"] == STATUS_SKIPPED:
        return "cloud assembly 当前未配置；当前阶段继续沿用本地 mp4 作为默认交付件。"
    if gate["missing_prerequisites"]:
        return "先补齐本地 assembly 缺失素材，再继续本地出片；cloud assembly 仍是后续增强项。"
    return "若要继续推进云端组装，下一步是补正式云端组装实现；当前本地 mp4 已是默认交付路径。"


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


def _urlopen_json_request(request: urllib.request.Request) -> dict[str, Any]:
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        raise TtsRequestError(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
        ) from exc
    except urllib.error.URLError as exc:
        raise TtsRequestError(
            str(exc.reason or exc),
            error_code="UrlOpenError",
        ) from exc

    try:
        return json.loads(payload.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise TtsRequestError(
            "aliyun_bailian returned invalid JSON payload",
            error_code="AliyunBailianInvalidJson",
        ) from exc


def _download_binary_file(url: str, destination: pathlib.Path) -> None:
    request = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read()
    except urllib.error.HTTPError as exc:
        raise TtsRequestError(
            _read_urllib_error_message(exc),
            status_code=exc.code,
            error_code=f"HTTP{exc.code}",
        ) from exc
    except urllib.error.URLError as exc:
        raise TtsRequestError(
            str(exc.reason or exc),
            error_code="UrlDownloadError",
        ) from exc

    if not data:
        raise TtsRequestError(
            "aliyun_bailian audio download is empty",
            error_code="AliyunBailianEmptyAudio",
        )
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
    ffmpeg_binary = resolve_ffmpeg_binary()
    output_path.parent.mkdir(parents=True, exist_ok=True)
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
    accents = ["#2563EB", "#0F766E", "#C2410C", "#7C3AED"]
    backgrounds = ["#F5F7FB", "#F4FBF9", "#FFF7ED", "#F8F5FF"]
    slides: list[dict[str, Any]] = []
    for index, segment in enumerate(manifest.get("segments", []), start=1):
        accent = accents[(index - 1) % len(accents)]
        background = backgrounds[(index - 1) % len(backgrounds)]
        slides.append(
            {
                "title": segment["goal"],
                "body": "\n".join(
                    [
                        segment["visual_intent"],
                        segment["caption_text"],
                    ]
                ),
                "accent": accent,
                "background": background,
                "badge": f"第{index}段",
                "footer": "formal_api_demo / 本地预览",
                "duration": segment["timeline"]["planned_duration_seconds"],
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
    cloud = visual_generation.get("cloud", {})
    if cloud.get("status") == STATUS_BLOCKED and cloud.get("blocked_reason"):
        issues.append("cloud visual generation blocked：" + cloud["blocked_reason"])
    if cloud.get("missing_implementations"):
        issues.append(
            "cloud visual generation provider 尚未接入："
            + "、".join(cloud["missing_implementations"])
        )
    return issues


def _assembly_preview_known_issues(preview: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    if preview.get("status") == STATUS_BLOCKED and preview.get("blocked_reason"):
        issues.append("本地 preview 组装 blocked：" + preview["blocked_reason"])
    if preview.get("status") == STATUS_FAILED and preview.get("error_message"):
        issues.append("本地 preview 组装 failed：" + preview["error_message"])
    return issues
