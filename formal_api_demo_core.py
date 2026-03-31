from __future__ import annotations

import copy
import json
import pathlib
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

PLACEHOLDER_PREFIX = "SET_"

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
    generation_gate = evaluate_generation_gate(
        video_spec=video_spec,
        config=config_bundle["config"],
        has_local_config=config_bundle["has_local_config"],
        dry_run=dry_run,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    tts_probe = build_default_tts_probe(video_spec)
    manifest = build_manifest(
        input_path=input_path,
        video_spec=video_spec,
        config=config_bundle["config"],
        generation_gate=generation_gate,
        output_dir=output_dir,
        dry_run=dry_run,
        tts_probe=tts_probe,
    )
    manifest_path = output_dir / "manifest.json"
    generation_gate_path = output_dir / "generation_gate.json"

    if dry_run:
        tts_probe["current_missing_prerequisites"] = generation_gate["missing_prerequisites"]
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)
    elif generation_gate["status"] == STATUS_SUCCESS:
        tts_probe = execute_tts_probe(
            video_spec=video_spec,
            config=config_bundle["config"],
            output_dir=output_dir,
        )
        manifest = apply_tts_probe_to_manifest(manifest, tts_probe, generation_gate)
    else:
        blocked_probe = build_default_tts_probe(video_spec)
        blocked_probe.update(
            {
                "status": generation_gate["status"],
                "blocked_reason": generation_gate.get("blocked_reason", ""),
                "failure_reason": generation_gate.get("failure_reason", ""),
                "error_code": "",
                "error_message": generation_gate.get("blocked_reason", ""),
                "current_missing_prerequisites": generation_gate["missing_prerequisites"],
            }
        )
        manifest = apply_tts_probe_to_manifest(manifest, blocked_probe, generation_gate)

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


def run_assembly_pipeline(
    manifest_path: pathlib.Path,
    example_config_path: pathlib.Path,
    local_config_path: pathlib.Path | None,
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    config_bundle = load_formal_config(example_config_path, local_config_path)
    assembly_gate = evaluate_assembly_gate(
        manifest=manifest,
        config=config_bundle["config"],
        has_local_config=config_bundle["has_local_config"],
        dry_run=dry_run,
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    assembly_plan = build_assembly_plan(
        manifest=manifest,
        config=config_bundle["config"],
        assembly_gate=assembly_gate,
    )
    manifest["machine_gate"]["assembly_gate"] = assembly_gate
    manifest["assembly"] = {
        "status": assembly_gate["status"],
        "task_id": None,
        "resource_id": None,
        "output_id": None,
    }
    manifest["current_status"] = assembly_gate["status"]

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


def evaluate_generation_gate(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
    dry_run: bool,
) -> dict[str, Any]:
    missing = _generation_missing_prerequisites(video_spec, config, has_local_config)
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
            if _nested_get(config, "provider", "name") == "volcengine"
            else "fail",
            "detail": f"provider={_nested_get(config, 'provider', 'name') or 'missing'}",
        },
        {
            "name": "tts_api_key_present",
            "status": "pass"
            if not _is_missing_secret(_nested_get(config, "auth", "api_key"))
            else "fail",
            "detail": "方舟 TTS probe 只读取 local 配置中的 API Key。",
        },
        {
            "name": "tts_model_or_endpoint_present",
            "status": "pass" if _get_tts_model_identifier(config) else "fail",
            "detail": "优先使用 endpoint_id；若未提供则退回 model。",
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

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif missing:
        status = STATUS_BLOCKED
        blocked_reason = "缺少 TTS probe 前提：" + "、".join(missing)
    elif OpenAI is None:
        status = STATUS_FAILED
        blocked_reason = "本地缺少 openai Python SDK，无法发起方舟兼容调用。"
        failure_reason = "missing_openai_sdk"
        implementation_missing.append("openai_python_sdk")
    elif _nested_get(config, "provider", "name") != "volcengine":
        status = STATUS_BLOCKED
        blocked_reason = "当前 TTS probe 仅支持 volcengine 方舟兼容入口。"
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
            "model_identifier": _get_tts_model_identifier(config),
            "endpoint_id": _nested_get(config, "tts", "endpoint_id"),
            "model": _nested_get(config, "tts", "model"),
            "voice": _nested_get(config, "tts", "voice"),
            "region": _nested_get(config, "provider", "region"),
        },
        "checks": checks,
        "notes": [
            "本轮 generation 只接 TTS，不接图像、视频和云端组装。",
            "dry-run 只验证输入、契约和 Gate，不调用远端。",
        ],
    }


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
            "detail": "正式组装阶段禁止回退到本地 Swift / ffmpeg。",
        },
    ]

    if dry_run:
        status = STATUS_PLANNED
        blocked_reason = ""
    elif missing:
        status = STATUS_BLOCKED
        blocked_reason = "缺少正式组装前提：" + "、".join(missing)
    else:
        status = STATUS_BLOCKED
        blocked_reason = "正式云端组装实现尚未接入，本轮只提供骨架与 Gate。"

    return {
        "gate_name": "assembly_gate",
        "status": status,
        "allow_execution": not dry_run and not missing and False,
        "blocked_reason": blocked_reason,
        "missing_prerequisites": missing,
        "missing_implementations": implementation_missing,
        "checks": checks,
        "notes": [
            "assembly dry-run 只落 assembly plan 与 result_summary。",
            "manifest 是修正循环和复审的事实锚点，assembly 不得绕开 manifest 自由猜测。",
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
                    "tts_model": _nested_get(config, "tts", "model"),
                    "tts_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
                    "image_model": _nested_get(config, "image_generation", "model"),
                    "video_model": _nested_get(config, "video_generation", "model"),
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
            "region": _nested_get(config, "provider", "region"),
            "models": {
                "tts": _nested_get(config, "tts", "model"),
                "tts_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
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
        "generation": {
            "status": generation_gate["status"] if not dry_run else STATUS_PLANNED,
            "task_id": None,
            "resource_id": None,
            "output_id": None,
            "tts_probe": tts_probe,
        },
        "assembly": {
            "status": STATUS_NOT_STARTED,
            "task_id": None,
            "resource_id": None,
            "output_id": None,
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
    status = STATUS_PLANNED if dry_run else tts_probe.get("status", generation_gate["status"])
    return {
        "schema_version": RESULT_SUMMARY_SCHEMA_VERSION,
        "stage": "generation",
        "overall_status": status,
        "generation_status": status,
        "assembly_status": STATUS_NOT_STARTED,
        "tts_probe_status": tts_probe.get("status", STATUS_NOT_STARTED),
        "failure_reason": tts_probe.get("failure_reason", ""),
        "error_message": tts_probe.get("error_message", ""),
        "machine_gate_result": {
            "generation_gate": generation_gate["status"],
            "assembly_gate": STATUS_NOT_STARTED,
        },
        "blocked_reason": ""
        if dry_run
        else tts_probe.get("blocked_reason") or generation_gate.get("blocked_reason", ""),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "generation_gate": str(output_dir / "generation_gate.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "tts_audio": tts_probe.get("audio_path"),
        },
        "next_action_hint": _generation_next_action_hint(generation_gate, tts_probe, dry_run),
        "current_missing_prerequisites": tts_probe.get(
            "current_missing_prerequisites", generation_gate["missing_prerequisites"]
        ),
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
            }
            for segment in manifest.get("segments", [])
        ],
        "gate_status": assembly_gate["status"],
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run=True),
    }


def build_assembly_result_summary(
    manifest: dict[str, Any],
    assembly_gate: dict[str, Any],
    output_dir: pathlib.Path,
    dry_run: bool,
) -> dict[str, Any]:
    generation_status = manifest.get("generation", {}).get("status", STATUS_NOT_STARTED)
    status = STATUS_PLANNED if dry_run else assembly_gate["status"]
    return {
        "schema_version": RESULT_SUMMARY_SCHEMA_VERSION,
        "stage": "assembly",
        "overall_status": status,
        "generation_status": generation_status,
        "assembly_status": status,
        "machine_gate_result": {
            "generation_gate": manifest.get("machine_gate", {})
            .get("generation_gate", {})
            .get("status", STATUS_NOT_STARTED),
            "assembly_gate": assembly_gate["status"],
        },
        "blocked_reason": "" if dry_run else assembly_gate.get("blocked_reason", ""),
        "artifact_paths": {
            "manifest": str(output_dir / "manifest.json"),
            "assembly_gate": str(output_dir / "assembly_gate.json"),
            "assembly_plan": str(output_dir / "assembly_plan.json"),
            "result_summary": str(output_dir / "result_summary.json"),
            "final_video": None,
        },
        "next_action_hint": _assembly_next_action_hint(assembly_gate, dry_run),
        "current_missing_prerequisites": assembly_gate["missing_prerequisites"],
        "known_issues": manifest.get("known_issues", []),
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
        "model_identifier": None,
        "probe_text": probe_text,
        "probe_text_source": probe_text_source,
        "voice": None,
        "used_endpoint_id": None,
        "used_model_id": None,
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


def execute_tts_probe(
    video_spec: dict[str, Any],
    config: dict[str, Any],
    output_dir: pathlib.Path,
) -> dict[str, Any]:
    probe = build_default_tts_probe(video_spec)
    model_identifier = _get_tts_model_identifier(config)
    base_url = _build_ark_base_url(config)
    response_format = (_nested_get(config, "tts", "response_format") or "mp3").strip() or "mp3"
    audio_path = output_dir / "tts" / f"voice_probe.{response_format}"
    probe.update(
        {
            "model_identifier": model_identifier,
            "voice": _nested_get(config, "tts", "voice"),
            "used_endpoint_id": _nested_get(config, "tts", "endpoint_id"),
            "used_model_id": _nested_get(config, "tts", "model"),
            "response_format": response_format,
            "request_debug": _build_tts_request_debug(
                config=config,
                base_url=base_url,
                model_identifier=model_identifier,
                response_format=response_format,
            ),
        }
    )

    try:
        client = OpenAI(
            api_key=_nested_get(config, "auth", "api_key"),
            base_url=base_url,
        )
        request_kwargs: dict[str, Any] = {
            "model": model_identifier,
            "voice": _nested_get(config, "tts", "voice"),
            "input": probe["probe_text"],
            "response_format": response_format,
        }
        style = _nested_get(config, "tts", "style")
        if style:
            request_kwargs["extra_body"] = {"style": style}

        with client.audio.speech.with_streaming_response.create(**request_kwargs) as response:
            audio_path.parent.mkdir(parents=True, exist_ok=True)
            response.stream_to_file(str(audio_path))
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
) -> list[str]:
    missing: list[str] = []
    if not has_local_config:
        missing.append("local_config_file")
    if _is_missing_secret(_nested_get(config, "auth", "api_key")):
        missing.append("api_key")
    if _is_missing_secret(_nested_get(config, "provider", "region")):
        missing.append("provider_region")
    if not _get_tts_model_identifier(config):
        missing.append("tts_model_or_endpoint")
    if _is_missing_secret(_nested_get(config, "tts", "voice")):
        missing.append("tts_voice")
    return missing


def _assembly_missing_prerequisites(
    manifest: dict[str, Any],
    config: dict[str, Any],
    has_local_config: bool,
) -> list[str]:
    missing: list[str] = []
    if not has_local_config:
        missing.append("local_config_file")
    if _is_missing_secret(_nested_get(config, "auth", "access_key_id")):
        missing.append("access_key_id")
    if _is_missing_secret(_nested_get(config, "auth", "secret_access_key")):
        missing.append("secret_access_key")
    if _is_missing_secret(_nested_get(config, "storage", "space_name")):
        missing.append("space_name")
    if _is_missing_secret(_nested_get(config, "assembly", "template_id")):
        missing.append("assembly_template_id")
    if _is_missing_secret(_nested_get(config, "provider", "region")):
        missing.append("provider_region")
    if not manifest.get("segments"):
        missing.append("manifest_segments")
    if manifest.get("generation", {}).get("status") != STATUS_SUCCESS:
        missing.append("generation_assets_not_ready")
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
        issues.append("当前仅验证 TTS 调用已接通，未覆盖视觉生成与云端组装。")
    return issues


def _generation_next_action_hint(
    gate: dict[str, Any],
    tts_probe: dict[str, Any],
    dry_run: bool,
) -> str:
    if dry_run:
        return "当前为 dry-run；下一步应补齐 local 配置中的方舟 API Key、可调用 model/endpoint 和 voice 后再尝试真实 TTS probe。"
    if gate["missing_prerequisites"]:
        return "先补齐 local 配置中的 API Key、TTS model/endpoint 和 voice，再进入真实 TTS probe。"
    if tts_probe.get("status") == STATUS_FAILED and tts_probe.get("http_status_code") == 404:
        return "当前 404 已压缩到请求路由 / 接入标识匹配层；优先核对 provider 路由与 endpoint/model 用法。"
    if tts_probe.get("status") == STATUS_FAILED:
        return "当前已进入真实请求层失败；优先核对远端返回码、请求结构和 provider 接口兼容性。"
    if tts_probe.get("status") == STATUS_SUCCESS:
        return "当前仅证明 TTS 调用已接通；下一步应试听音频质量，但不要误写成整条正式链路已跑通。"
    return "当前已具备 TTS probe 前提；下一步可执行真实 TTS 调用并检查输出音频质量。"


def _assembly_next_action_hint(gate: dict[str, Any], dry_run: bool) -> str:
    if dry_run:
        return "当前为 assembly dry-run；下一步应补齐云端组装配置和 provider 实现后再尝试非 dry-run。"
    if gate["missing_prerequisites"]:
        return "先补齐云端组装模板、空间配置和 local 配置，再进入真实组装联调。"
    return "补齐正式云端组装实现后，再进入首轮样片联调。"


def _select_tts_probe_text(video_spec: dict[str, Any]) -> tuple[str, str]:
    if video_spec.get("segments"):
        return video_spec["segments"][0]["voiceover_text"], "segment_1_voiceover"
    return video_spec["hook"], "hook"


def _get_tts_model_identifier(config: dict[str, Any]) -> str | None:
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


def _classify_tts_exception(
    exc: Exception,
    config: dict[str, Any],
) -> tuple[str, str, int | None, str, str]:
    raw_message = _sanitize_message(str(exc), config)
    error_code = exc.__class__.__name__
    http_status_code = _extract_http_status_code(exc)

    if http_status_code == 404:
        return (
            STATUS_FAILED,
            "ark_tts_route_or_identifier_not_found",
            http_status_code,
            error_code,
            raw_message,
        )
    if http_status_code is not None and 400 <= http_status_code < 600:
        return STATUS_FAILED, "ark_tts_request_failed", http_status_code, error_code, raw_message
    if openai is not None and isinstance(exc, openai.APIError):
        return STATUS_FAILED, "ark_tts_request_failed", http_status_code, error_code, raw_message
    return STATUS_FAILED, "ark_tts_request_failed", http_status_code, error_code, raw_message


def _extract_http_status_code(exc: Exception) -> int | None:
    status_code = getattr(exc, "status_code", None)
    if isinstance(status_code, int):
        return status_code
    response = getattr(exc, "response", None)
    if response is None:
        return None
    response_status = getattr(response, "status_code", None)
    if isinstance(response_status, int):
        return response_status
    return None


def _build_tts_request_debug(
    config: dict[str, Any],
    base_url: str,
    model_identifier: str | None,
    response_format: str,
) -> dict[str, Any]:
    endpoint_id = _nested_get(config, "tts", "endpoint_id")
    model = _nested_get(config, "tts", "model")
    voice = _nested_get(config, "tts", "voice")
    return {
        "provider_route_family": "ark_openai_compatible",
        "request_method": "POST",
        "base_url": base_url,
        "relative_path": "/audio/speech",
        "sdk_call": "client.audio.speech.with_streaming_response.create",
        "model_identifier_source": "endpoint_id"
        if not _is_missing_secret(endpoint_id)
        else "model",
        "model_identifier_shape": _shape_debug_value(model_identifier),
        "endpoint_id_shape": _shape_debug_value(endpoint_id),
        "model_shape": _shape_debug_value(model),
        "voice_location": "payload.voice",
        "voice_shape": _shape_debug_value(voice),
        "response_format": response_format,
    }


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
