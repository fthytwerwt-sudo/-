#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXPLORER_SCRIPT = ROOT / "scripts" / "deepseek_readonly_explorer.py"
EXPLORER_OUTPUT = ROOT / "dist" / "deepseek_readonly_explorer" / "latest_prefetch_context_pack.md"
DEFAULT_OUTPUT_DIR = ROOT / "dist" / "deepseek_supply_controller"
ALLOWED_ACTIONS = {
    "file_map",
    "risk_report",
    "context_summary",
    "missing_files",
    "visual_asset_requirement_pack",
    "api_asset_generation_pack",
    "image_prompt_pack",
    "asset_validation_pack",
    "assembly_decision_pack",
    "editing_decision_pack",
    "auto",
}
EXECUTION_SUPPLY_ACTIONS = {
    "visual_asset_requirement_pack",
    "api_asset_generation_pack",
    "image_prompt_pack",
    "asset_validation_pack",
    "assembly_decision_pack",
}
ALLOWED_TRIGGER_REASONS = {
    "mandatory_pre_supply",
    "mandatory_post_risk_review",
    "missing_context",
    "rule_conflict",
    "stale_context_risk",
    "large_context",
    "before_write_gate",
    "after_read_gap",
    "user_explicit_deepseek",
}
FORBIDDEN_PARTS = {
    ".git",
    "dist/latest_review_pack",
    "视频工厂归档+删除",
}
FORBIDDEN_SUFFIXES = {
    ".mp4",
    ".mov",
    ".m4v",
    ".mp3",
    ".wav",
    ".m4a",
    ".aac",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".psd",
    ".ai",
}
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".py",
    ".yaml",
    ".yml",
    ".toml",
    ".csv",
}
REQUIRED_REQUEST_FIELDS = {
    "request_id",
    "project_route",
    "task_type",
    "trigger_reason",
    "action",
    "mandatory_for_every_task",
    "participation_level",
    "pre_supply_required",
    "post_review_required",
    "codex_vertical_completion_required",
    "token_usage_expectation",
    "fallback_allowed",
    "fallback_not_completion",
    "user_explicit_deepseek_required",
    "deepseek_must_not_be_skipped_by_codex_discretion",
    "current_goal",
    "current_step",
    "known_context",
    "missing_context",
    "candidate_files",
    "forbidden_paths",
    "expected_output",
    "not_allowed",
    "blocked_if",
    "return_to_codex",
}
REQUEST_LIST_FIELDS = {
    "known_context",
    "missing_context",
    "candidate_files",
    "must_read_files",
    "optional_files",
    "forbidden_paths",
    "expected_output",
    "not_allowed",
    "blocked_if",
}
REQUIRED_NOT_ALLOWED_PATTERNS = {
    "write_files": ("写文件", "write files"),
    "decide_project_facts": ("拍板项目事实", "decide project facts"),
    "fallback_not_conclusion": ("fallback", "本地兜底"),
    "no_multi_agent_runtime_claim": ("multi-agent runtime", "多 agent"),
}
EDITING_DECISION_SAMPLE_FIELDS = (
    "source_segments",
    "narration_lines",
    "frame_descriptions",
    "editing_question",
)
EXECUTION_SUPPLY_SAMPLE_FIELDS = {
    "visual_asset_requirement_pack": (
        "script_blocks",
        "segments",
        "content_route_card",
    ),
    "api_asset_generation_pack": (
        "visual_asset_requirements",
        "api_generation_targets",
        "api_call_policy",
        "secret_policy",
    ),
    "image_prompt_pack": (
        "api_generation_targets",
        "image_prompt_specs",
    ),
    "asset_validation_pack": (
        "visual_asset_requirements",
        "asset_validation_criteria",
    ),
    "assembly_decision_pack": (
        "segments",
        "visual_asset_requirements",
        "assembly_slots",
    ),
}
EXECUTION_SUPPLY_OUTPUT_KEYS = {
    "visual_asset_requirement_pack": "visual_asset_requirement_pack",
    "api_asset_generation_pack": "api_asset_generation_pack",
    "image_prompt_pack": "image_prompt_pack",
    "asset_validation_pack": "asset_validation_pack",
    "assembly_decision_pack": "assembly_decision_pack",
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the DeepSeek supply controller and write a Codex-readable supply pack."
    )
    parser.add_argument("--request-file", help="JSON supply request task card.")
    parser.add_argument("--task", help="Supply task description.")
    parser.add_argument("--task-type", help="Task type for the supply request.")
    parser.add_argument(
        "--trigger-reason",
        choices=sorted(ALLOWED_TRIGGER_REASONS),
        help="Why Codex is triggering the supply controller.",
    )
    parser.add_argument(
        "--action",
        choices=sorted(ALLOWED_ACTIONS),
        help="Small readonly action to run.",
    )
    parser.add_argument(
        "--context-file",
        action="append",
        default=[],
        help="Readonly context file. Repeatable.",
    )
    parser.add_argument(
        "--max-rounds",
        type=int,
        default=1,
        help="Reserved for future refill loops. Minimal controller runs one round.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR.relative_to(ROOT)),
        help="Output directory for supply pack files.",
    )
    parser.add_argument(
        "--allow-process-env-api-key",
        action="store_true",
        help="When a request forbids .env, allow DeepSeek API via process environment only.",
    )
    return parser.parse_args(argv)


def require_cli_args(args: argparse.Namespace) -> None:
    missing = [
        name
        for name in ("task", "task_type", "trigger_reason", "action")
        if not getattr(args, name)
    ]
    if missing:
        raise ValueError(f"missing_cli_args:{','.join(missing)}")


def relative_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def resolve_inside_root(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = ROOT / path
    return path.resolve()


def assert_safe_context_file(path: Path) -> None:
    path_label = str(path)
    rel_label = relative_label(path)
    if not path.exists():
        raise ValueError(f"context_file_missing:{rel_label}")
    if not path.is_file():
        raise ValueError(f"context_file_not_file:{rel_label}")
    try:
        path.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"context_file_outside_workspace:{path_label}") from exc
    if path.name == ".env" or path.name.startswith(".env."):
        raise ValueError(f"forbidden_env_file:{rel_label}")
    normalized = rel_label.replace("\\", "/")
    if any(part in normalized for part in FORBIDDEN_PARTS):
        raise ValueError(f"forbidden_context_path:{rel_label}")
    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        raise ValueError(f"forbidden_binary_or_media_file:{rel_label}")
    if path.suffix.lower() not in TEXT_SUFFIXES:
        raise ValueError(f"unsupported_context_file_type:{rel_label}")


def resolve_context_files(raw_paths: list[str]) -> list[Path]:
    paths: list[Path] = []
    for raw_path in raw_paths:
        path = resolve_inside_root(raw_path)
        assert_safe_context_file(path)
        paths.append(path)
    return paths


def resolve_request_file(raw_path: str) -> Path:
    path = resolve_inside_root(raw_path)
    assert_safe_context_file(path)
    if path.suffix.lower() != ".json":
        raise ValueError(f"request_file_must_be_json:{relative_label(path)}")
    return path


def load_request_card(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"request_file_json_parse_error:{exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("request_file_top_level_not_object")
    return data


def ensure_string_list(value: Any, field_name: str) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError(f"request_field_not_array:{field_name}")
    normalized: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError(f"request_field_item_not_string:{field_name}")
        normalized.append(item)
    return normalized


def validate_not_allowed(items: list[str]) -> None:
    joined = "\n".join(items).lower()
    missing_patterns: list[str] = []
    for label, patterns in REQUIRED_NOT_ALLOWED_PATTERNS.items():
        if not any(pattern.lower() in joined for pattern in patterns):
            missing_patterns.append(label)
    if missing_patterns:
        raise ValueError(f"request_not_allowed_missing:{','.join(missing_patterns)}")


def validate_forbidden_path_policy(
    *,
    file_paths: list[str],
    forbidden_paths: list[str],
) -> None:
    normalized_forbidden = [path.replace("\\", "/") for path in forbidden_paths]
    for file_path in file_paths:
        normalized_file = file_path.replace("\\", "/")
        if any(
            forbidden
            and (
                normalized_file == forbidden
                or normalized_file.startswith(forbidden.rstrip("/") + "/")
                or (
                    forbidden.startswith("*.")
                    and normalized_file.lower().endswith(forbidden[1:].lower())
                )
                or (
                    forbidden.endswith(".*")
                    and normalized_file.startswith(forbidden[:-1])
                )
            )
            for forbidden in normalized_forbidden
        ):
            raise ValueError(f"request_file_matches_forbidden_path:{file_path}")


def validate_request_card(card: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_REQUEST_FIELDS - set(card))
    if missing:
        raise ValueError(f"request_missing_required_fields:{','.join(missing)}")
    if card.get("project_route") != "video_factory":
        raise ValueError(f"unsupported_project_route:{card.get('project_route')}")
    if card.get("trigger_reason") not in ALLOWED_TRIGGER_REASONS:
        raise ValueError(f"invalid_trigger_reason:{card.get('trigger_reason')}")
    if card.get("action") not in ALLOWED_ACTIONS:
        raise ValueError(f"invalid_action:{card.get('action')}")

    for field_name in REQUEST_LIST_FIELDS:
        ensure_string_list(card.get(field_name), field_name)

    not_allowed = ensure_string_list(card.get("not_allowed"), "not_allowed")
    validate_not_allowed(not_allowed)

    candidate_files = ensure_string_list(card.get("candidate_files"), "candidate_files")
    must_read_files = ensure_string_list(card.get("must_read_files"), "must_read_files")
    optional_files = ensure_string_list(card.get("optional_files"), "optional_files")
    forbidden_paths = ensure_string_list(card.get("forbidden_paths"), "forbidden_paths")
    validate_forbidden_path_policy(
        file_paths=candidate_files + must_read_files + optional_files,
        forbidden_paths=forbidden_paths,
    )


def ordered_unique(values: list[str]) -> list[str]:
    result: list[str] = []
    for value in values:
        if value not in result:
            result.append(value)
    return result


def context_files_from_request(card: dict[str, Any]) -> list[str]:
    max_context_files = card.get("max_context_files", 8)
    if not isinstance(max_context_files, int) or max_context_files < 1:
        raise ValueError("request_invalid_max_context_files")
    raw_files = ordered_unique(
        ensure_string_list(card.get("must_read_files"), "must_read_files")
        + ensure_string_list(card.get("candidate_files"), "candidate_files")
        + ensure_string_list(card.get("optional_files"), "optional_files")
    )
    return raw_files[:max_context_files]


def task_from_request(card: dict[str, Any]) -> str:
    payload = {
        "request_id": card.get("request_id"),
        "task_id": card.get("task_id", ""),
        "mandatory_for_every_task": card.get("mandatory_for_every_task"),
        "participation_level": card.get("participation_level"),
        "pre_supply_required": card.get("pre_supply_required"),
        "post_review_required": card.get("post_review_required"),
        "codex_vertical_completion_required": card.get("codex_vertical_completion_required"),
        "token_usage_expectation": card.get("token_usage_expectation"),
        "fallback_allowed": card.get("fallback_allowed"),
        "fallback_not_completion": card.get("fallback_not_completion"),
        "user_explicit_deepseek_required": card.get("user_explicit_deepseek_required"),
        "deepseek_must_not_be_skipped_by_codex_discretion": card.get(
            "deepseek_must_not_be_skipped_by_codex_discretion"
        ),
        "current_goal": card.get("current_goal"),
        "current_step": card.get("current_step"),
        "known_context": card.get("known_context"),
        "missing_context": card.get("missing_context"),
        "decision_needed": card.get("decision_needed", ""),
        "expected_output": card.get("expected_output"),
        "codex_next_input": card.get("codex_next_input", ""),
        "return_to_codex": card.get("return_to_codex"),
        "stop_condition": card.get("stop_condition", ""),
        "blocked_if": card.get("blocked_if"),
        "not_allowed": card.get("not_allowed"),
    }
    for field_name in (
        "source_segments",
        "narration_lines",
        "contact_sheet_description",
        "ocr_text",
        "frame_descriptions",
        "reference_quality_points",
        "editing_question",
        "script_blocks",
        "segments",
        "content_route_card",
        "data_goal_anchor",
        "current_north_star_goal",
        "current_stage_goal",
        "main_bottleneck",
        "primary_variable",
        "supporting_variables",
        "forbidden_variables",
        "success_metric",
        "failure_metric",
        "post_publish_validation_metric",
        "next_video_execution_prompt",
        "threshold_config_v1",
        "video_goal_card",
        "post_publish_review_card",
        "data_flywheel_memory",
        "content_structure_feedback_card",
        "next_video_structure_plan",
        "data_goal_alignment_check_required",
        "data_goal_alignment_check",
        "data_goal_supply_questions",
        "visual_asset_requirements",
        "api_generation_targets",
        "image_prompt_specs",
        "asset_validation_criteria",
        "assembly_slots",
        "fallback_plan",
        "vendor_constraints",
        "api_call_policy",
        "secret_policy",
        "allow_process_env_api_key",
        "disable_env_file",
        "safe_deepseek_process_env_test",
        "deepseek_readiness_check_required",
        "safe_call_mode",
        "readiness_expected_fields",
    ):
        if field_name in card:
            payload[field_name] = card.get(field_name)
    return (
        "Use this supply_request task card as the only current task context. "
        "Do not infer missing project state from memory.\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
    )


def namespace_from_request(
    *,
    args: argparse.Namespace,
    card: dict[str, Any],
    request_file: Path,
) -> argparse.Namespace:
    output_dir = args.output_dir
    return_to_codex = card.get("return_to_codex")
    if isinstance(return_to_codex, dict) and isinstance(return_to_codex.get("output_dir"), str):
        output_dir = return_to_codex["output_dir"]
    return argparse.Namespace(
        request_file=str(request_file),
        task=task_from_request(card),
        task_type=str(card["task_type"]),
        trigger_reason=str(card["trigger_reason"]),
        action=str(card["action"]),
        context_file=context_files_from_request(card),
        max_rounds=args.max_rounds,
        output_dir=output_dir,
        allow_process_env_api_key=args.allow_process_env_api_key,
        request_card=card,
        request_validation_status="passed",
    )


def namespace_from_cli(args: argparse.Namespace) -> argparse.Namespace:
    require_cli_args(args)
    args.request_card = None
    args.request_validation_status = "not_applicable_cli"
    return args


def resolve_output_dir(raw_output_dir: str) -> Path:
    output_dir = resolve_inside_root(raw_output_dir)
    try:
        output_dir.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"output_dir_outside_workspace:{output_dir}") from exc
    normalized = relative_label(output_dir).replace("\\", "/")
    if any(part in normalized for part in FORBIDDEN_PARTS) or ".git" in output_dir.parts:
        raise ValueError(f"forbidden_output_dir:{relative_label(output_dir)}")
    return output_dir


def choose_auto_action(trigger_reason: str) -> str:
    if trigger_reason == "mandatory_pre_supply":
        return "file_map"
    if trigger_reason == "mandatory_post_risk_review":
        return "risk_report"
    if trigger_reason in {"missing_context", "after_read_gap"}:
        return "missing_files"
    if trigger_reason in {"rule_conflict", "stale_context_risk", "before_write_gate"}:
        return "risk_report"
    if trigger_reason == "large_context":
        return "context_summary"
    return "file_map"


def build_controller_task(
    *,
    task: str,
    task_type: str,
    trigger_reason: str,
    action: str,
    context_labels: list[str],
    request_card: dict[str, Any] | None = None,
) -> str:
    actual_action = choose_auto_action(trigger_reason) if action == "auto" else action
    action_prompts = {
        "file_map": "Output a compact file map: which files Codex should read next and why.",
        "risk_report": "Output a compact risk report: stale context, rule conflicts, overreach, and blocked-if items.",
        "context_summary": "Compress the provided context into a compact Codex-ready summary.",
        "missing_files": "Identify missing files or evidence Codex should request or read next.",
        "visual_asset_requirement_pack": (
            "Output a visual_asset_requirement_pack for a final script entering execution. "
            "DeepSeek must stay readonly, must not read media files or .env/API keys, and must not "
            "decide project facts. Help Codex decide which script blocks need user_recording, "
            "screenshot, api_generated_image, info_card, prompt_tail_card, character_host, "
            "background, icon_or_marker, or no_extra_asset. Mark which assets must be real "
            "evidence and which can only be auxiliary."
        ),
        "api_asset_generation_pack": (
            "Output an api_asset_generation_pack. This round forbids real API calls and forbids "
            "reading .env or API keys. Generate only a plan: vendor candidate, model/service, "
            "asset count, aspect ratio, resolution, style constraints, segment usage, prompt needs, "
            "negative prompt needs, fallback plan, and blocked_if. API-generated images must not "
            "replace real screen-recording evidence. Future real API calls require explicit user authorization."
        ),
        "image_prompt_pack": (
            "Output an image_prompt_pack without generating images. Write positive_prompt, "
            "negative_prompt, style_anchor, composition, text_policy, acceptance_criteria, and "
            "rejected_if. Do not default Chinese readable text to the image model; if text is "
            "needed, route it to a later card layer. Do not reuse official Minecraft assets, logos, "
            "fonts, textures, models, or sounds."
        ),
        "asset_validation_pack": (
            "Output an asset_validation_pack. Judge whether proposed API images, cards, or assets "
            "can enter assembly. AI images cannot replace real screen-recording evidence. Use "
            "validation_result values pass, revise, reject, or pending_human_review, and mark "
            "style_fit, evidence_fit, readability, platform risk, copyright/official asset risk, "
            "human feel, required_fix, and blocked_if."
        ),
        "assembly_decision_pack": (
            "Output an assembly_decision_pack. Decide which asset goes into which segment, which "
            "carrier is primary evidence, which is secondary support, where API-generated images "
            "may appear, and where no image should interrupt the evidence chain. Include TTS, "
            "subtitle, transition, evidence_chain_note, and whether the segment needs "
            "editing_decision_pack follow-up."
        ),
        "editing_decision_pack": (
            "Output an editing_decision_pack based only on text samples supplied by Codex. "
            "DeepSeek must not read media files, cut video, or decide final visual quality. "
            "Help Codex decide where to use full_frame, zoom_in, crop_focus, highlight_box, "
            "freeze_frame, insert_card, split_compare, or do_not_touch while protecting the "
            "real evidence chain. Mark missing_context and blocked_if_insufficient_editing_sample "
            "when source_segments, narration_lines, frame_descriptions, or editing_question are insufficient."
        ),
    }
    return "\n".join(
        [
            "DeepSeek supply controller request for 视频工厂.",
            f"task_type: {task_type}",
            f"trigger_reason: {trigger_reason}",
            f"action: {actual_action}",
            action_prompts[actual_action],
            "Stay read-only. Do not write files. Do not decide project facts.",
            "This request is part of mandatory_deepseek_supply_loop: DeepSeek supplies readonly material every Codex task, while Codex integrates and verifies.",
            "Do not read .env, API keys, token files, media files, or dist/latest_review_pack/.",
            "Do not call Aliyun, Doubao, or any image/video/audio generation API.",
            "After supply output, Codex must verify original files and task boundaries.",
            "After Codex edits, a post risk review must check status promotion, forbidden changes, missed sync files, fallback mislabel risk, and remaining work.",
            "Do not claim multi-agent runtime is running.",
            "If evidence is insufficient, say what Codex should read next.",
            "Context files under consideration:",
            json.dumps(context_labels, ensure_ascii=False),
            "Task:",
            task,
        ]
        + (
            [
                "Structured supply_request:",
                json.dumps(request_card, ensure_ascii=False, indent=2),
            ]
            if request_card
            else []
        )
    )


def run_explorer(
    controller_task: str,
    context_files: list[Path],
    *,
    allow_process_env_api_key: bool = False,
) -> dict[str, Any]:
    command = [sys.executable, str(EXPLORER_SCRIPT), "--task", controller_task]
    env = os.environ.copy()
    if allow_process_env_api_key:
        command.append("--no-env-file")
        env["DEEPSEEK_DISABLE_ENV_FILE"] = "1"
        env["DEEPSEEK_ALLOW_PROCESS_ENV_KEY"] = "1"
    for path in context_files:
        command.extend(["--context-file", relative_label(path)])
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "returncode": result.returncode,
        "stdout_tail": result.stdout[-500:],
        "stderr_tail": result.stderr[-500:],
    }


def request_forbids_env_or_secret(card: dict[str, Any] | None) -> bool:
    if not isinstance(card, dict):
        return False
    forbidden_paths = "\n".join(ensure_string_list(card.get("forbidden_paths"), "forbidden_paths"))
    not_allowed = "\n".join(ensure_string_list(card.get("not_allowed"), "not_allowed"))
    policy_text = "\n".join(
        str(card.get(field_name, ""))
        for field_name in ("secret_policy", "api_call_policy", "fallback_policy")
    )
    joined = f"{forbidden_paths}\n{not_allowed}\n{policy_text}".lower()
    return any(marker in joined for marker in (".env", "api key", "secret", "密钥", "token"))


def allow_process_env_api_key_enabled(args: argparse.Namespace, card: dict[str, Any] | None) -> bool:
    if getattr(args, "allow_process_env_api_key", False):
        return True
    if os.environ.get("DEEPSEEK_ALLOW_PROCESS_ENV_KEY") == "1":
        return True
    return isinstance(card, dict) and card.get("allow_process_env_api_key") is True


def build_local_fallback_explorer_pack(
    *,
    controller_task: str,
    context_labels: list[str],
    request_card: dict[str, Any] | None,
    reason: str,
) -> dict[str, Any]:
    current_goal = request_card.get("current_goal", "") if isinstance(request_card, dict) else ""
    missing_context = request_card.get("missing_context", []) if isinstance(request_card, dict) else []
    return {
        "status": {
            "validation_status": "fallback",
            "api_validation": "not_started",
            "context_pack_validation": "fallback_local_only",
            "deepseek_generation_status": reason,
            "fallback_status": "used",
            "pipeline_status": "usable_with_fallback",
            "env_file_read": "false",
            "process_env_key_allowed": "false",
            "process_env_key_present": "false",
            "api_key_printed": "false",
            "api_key_written": "false",
            "safe_call_mode": "local_fallback_no_deepseek_call",
            "deepseek_actual_participation": "fallback_local_only",
            "token_usage_observed": "not_available_user_check_required",
        },
        "sections": {
            "prefetch_context_pack": {
                "confirmed": [
                    "controller skipped DeepSeek explorer to respect forbidden .env / secret policy",
                    "fallback_local_only is not a DeepSeek conclusion",
                ],
                "pending_verification": missing_context,
                "source_summary": context_labels,
            },
            "must_read_file_map": {
                "required_files": context_labels,
                "optional_files": [],
                "reason": "Use request-provided text files only; do not read .env, secrets, media, or dist/latest_review_pack/.",
            },
            "risk_and_conflict_report": {
                "risks": [
                    "本轮禁止读取 .env / API key，因此未调用 DeepSeek API。",
                    "供料包来自本地 fallback，不得写成 DeepSeek 结论。",
                    "Codex 仍必须复核原文件后再执行。",
                ],
                "conflicts": [],
                "blocked_if": [
                    "需要读取 .env、API key、媒体文件或 dist/latest_review_pack/。",
                    "需要真实调用阿里、豆包或其他生成 API。",
                    "需要把 fallback_local_only 写成 deepseek_passed。",
                ],
            },
            "candidate_summary": {
                "summary": current_goal,
                "recommended_next_step": "Codex reads the generated supply pack, reviews original files, and continues only inside allowed scope.",
                "not_allowed": [
                    "Do not treat fallback_local_only as a DeepSeek conclusion.",
                    "Do not read .env or API keys.",
                    "Do not call real generation APIs.",
                ],
            },
        },
        "markdown_exists": False,
        "controller_task": controller_task,
    }


def parse_header_status(markdown: str) -> dict[str, str]:
    status: dict[str, str] = {}
    for line in markdown.splitlines():
        match = re.match(r"- `([^`]+)`: `([^`]*)`", line.strip())
        if match:
            status[match.group(1)] = match.group(2)
    return status


def extract_json_section(markdown: str, section_title: str) -> Any:
    heading_index = markdown.find(section_title)
    if heading_index < 0:
        return None
    fence_start = markdown.find("```json", heading_index)
    if fence_start < 0:
        return None
    content_start = markdown.find("\n", fence_start)
    fence_end = markdown.find("```", content_start + 1)
    if content_start < 0 or fence_end < 0:
        return None
    raw_json = markdown[content_start:fence_end].strip()
    try:
        return json.loads(raw_json)
    except json.JSONDecodeError:
        return None


def read_explorer_pack() -> dict[str, Any]:
    if not EXPLORER_OUTPUT.exists():
        return {"status": {}, "sections": {}, "markdown_exists": False}
    markdown = EXPLORER_OUTPUT.read_text(encoding="utf-8")
    sections = {
        "prefetch_context_pack": extract_json_section(
            markdown, "## prefetch_context_pack（预读取上下文包）"
        ),
        "must_read_file_map": extract_json_section(
            markdown, "## must_read_file_map（必读文件地图）"
        ),
        "risk_and_conflict_report": extract_json_section(
            markdown, "## risk_and_conflict_report（风险与冲突报告）"
        ),
        "candidate_summary": extract_json_section(
            markdown, "## candidate_summary（候选摘要）"
        ),
    }
    return {
        "status": parse_header_status(markdown),
        "sections": sections,
        "markdown_exists": True,
    }


def listify(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def collect_recommended_files(must_read_file_map: Any, fallback_files: list[str]) -> list[str]:
    files: list[str] = []
    if isinstance(must_read_file_map, dict):
        for key in ("required_files", "optional_files"):
            for item in listify(must_read_file_map.get(key)):
                if isinstance(item, str) and item not in files:
                    files.append(item)
                elif isinstance(item, dict):
                    path = item.get("path") or item.get("file")
                    if isinstance(path, str) and path not in files:
                        files.append(path)
    for fallback_file in fallback_files:
        if fallback_file not in files:
            files.append(fallback_file)
    return files


def collect_risks(risk_report: Any) -> list[Any]:
    if not isinstance(risk_report, dict):
        return []
    risks: list[Any] = []
    for key in ("risks", "conflicts", "blocked_if"):
        risks.extend(listify(risk_report.get(key)))
    return risks


def collect_missing_files(sections: dict[str, Any]) -> list[Any]:
    missing: list[Any] = []
    for section in sections.values():
        if isinstance(section, dict):
            missing.extend(listify(section.get("missing_files")))
            missing.extend(listify(section.get("missing")))
    return [item for item in missing if item]


def request_has_sample_value(card: dict[str, Any], field_name: str) -> bool:
    value = card.get(field_name)
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    if isinstance(value, dict):
        return bool(value)
    return value is not None


def first_list_item(value: Any) -> Any:
    if isinstance(value, list) and value:
        return value[0]
    return None


def data_goal_fields_from_request(card: dict[str, Any]) -> dict[str, Any]:
    anchor = card.get("data_goal_anchor") if isinstance(card.get("data_goal_anchor"), dict) else {}
    return {
        "data_goal_anchor_used": anchor or card.get("data_goal_anchor", {}),
        "main_bottleneck": anchor.get("main_bottleneck", card.get("main_bottleneck", "")),
        "primary_variable": anchor.get("primary_variable", card.get("primary_variable", "")),
        "forbidden_variables": anchor.get(
            "forbidden_variables",
            card.get("forbidden_variables", []),
        ),
        "success_metric": anchor.get("success_metric", card.get("success_metric", "")),
        "failure_metric": anchor.get("failure_metric", card.get("failure_metric", "")),
        "post_publish_validation_metric": anchor.get(
            "post_publish_validation_metric",
            card.get("post_publish_validation_metric", ""),
        ),
    }


def build_editing_decision_support(
    *,
    request_card: dict[str, Any] | None,
    action: str,
) -> dict[str, Any] | None:
    if action != "editing_decision_pack":
        return None
    card = request_card if isinstance(request_card, dict) else {}
    missing_context = [
        field_name
        for field_name in EDITING_DECISION_SAMPLE_FIELDS
        if not request_has_sample_value(card, field_name)
    ]
    source_segment = first_list_item(card.get("source_segments"))
    frame_description = first_list_item(card.get("frame_descriptions"))
    narration_line = first_list_item(card.get("narration_lines"))
    reference_quality_point = first_list_item(card.get("reference_quality_points"))
    if not isinstance(source_segment, dict):
        source_segment = {}
    if not isinstance(frame_description, dict):
        frame_description = {}
    data_goal_fields = data_goal_fields_from_request(card)
    return {
        "sample_source": "supply_request_text_fields_only",
        "data_goal_anchor_used": data_goal_fields["data_goal_anchor_used"],
        "line_group_goal": "待 Codex 基于 script_to_timeline_map 复核",
        "primary_variable_support": data_goal_fields["primary_variable"],
        "evidence_role_for_metric": data_goal_fields["success_metric"],
        "forbidden_visuals_by_goal": data_goal_fields["forbidden_variables"],
        "edit_action_reason_against_data_goal": (
            "剪辑建议必须服务主变量，并避免引入 forbidden_variables；具体动作需 Codex 复核原素材。"
        ),
        "post_publish_validation_metric": data_goal_fields["post_publish_validation_metric"],
        "missing_context": missing_context,
        "blocked_if_insufficient_editing_sample": bool(missing_context),
        "source_segment": {
            "file_reference": source_segment.get("file_reference", ""),
            "time_range": source_segment.get("time_range", ""),
            "visible_content": source_segment.get("visible_content")
            or frame_description.get("visible_content", ""),
            "evidence_role": source_segment.get("evidence_role", ""),
        },
        "narration_intent": {
            "line": narration_line or "",
            "function": "待 DeepSeek / fallback 基于文字样料补充",
            "viewer_should_understand": "待 Codex 复核原文件后确认",
        },
        "visual_action": {
            "action_type": "do_not_touch" if missing_context else "full_frame",
            "target_area": "待 Codex 复核原素材后确认",
            "timing": source_segment.get("time_range", ""),
        },
        "reason": "供料只能基于文字样料生成剪辑建议，不能替代 Codex 原文件复核。",
        "reference_quality_point": reference_quality_point or "",
        "risk": [
            "DeepSeek 不直接读取或判断媒体文件。",
            "fallback_local_only 不是 DeepSeek 结论。",
            "文字化样料不足时不得进入真实剪辑执行。",
        ],
        "blocked_if": [
            "缺少 source_segments / narration_lines / frame_descriptions / editing_question 中的关键样料。",
            "需要 DeepSeek 直接读取视频、音频、图片或 dist/latest_review_pack/。",
            "需要把剪辑建议写成最终内容判断。",
        ],
        "codex_execution_note": (
            "Codex 必须先复核素材证据、原文件和当前规则，再决定是否执行剪辑动作。"
        ),
    }


def build_execution_supply_support(
    *,
    request_card: dict[str, Any] | None,
    action: str,
) -> dict[str, Any] | None:
    if action not in EXECUTION_SUPPLY_ACTIONS:
        return None
    card = request_card if isinstance(request_card, dict) else {}
    sample_fields = EXECUTION_SUPPLY_SAMPLE_FIELDS[action]
    missing_context = [
        field_name
        for field_name in sample_fields
        if not request_has_sample_value(card, field_name)
    ]
    data_goal_fields = data_goal_fields_from_request(card)
    base: dict[str, Any] = {
        "action": action,
        "sample_source": "supply_request_text_fields_only",
        "data_goal_anchor_used": data_goal_fields["data_goal_anchor_used"],
        "main_bottleneck": data_goal_fields["main_bottleneck"],
        "primary_variable": data_goal_fields["primary_variable"],
        "forbidden_variables": data_goal_fields["forbidden_variables"],
        "success_metric": data_goal_fields["success_metric"],
        "failure_metric": data_goal_fields["failure_metric"],
        "post_publish_validation_metric": data_goal_fields["post_publish_validation_metric"],
        "missing_context": missing_context,
        "blocked_if_insufficient_execution_sample": bool(missing_context),
        "codex_original_file_review_required": True,
        "media_file_read_allowed": False,
        "env_or_secret_read_allowed": False,
        "real_api_call_allowed": False,
        "not_deepseek_final_judgment": True,
        "risk": [
            "DeepSeek / fallback 只能基于任务卡文字样料供料。",
            "AI/API 生成图片不能替代真实录屏证据。",
            "Codex 必须复核原文件和执行边界。",
        ],
    }
    if action == "visual_asset_requirement_pack":
        base[EXECUTION_SUPPLY_OUTPUT_KEYS[action]] = {
            "script_block": first_list_item(card.get("script_blocks")) or "",
            "segment": first_list_item(card.get("segments")) or "",
            "viewer_task": "待 Codex 基于最终文案和内容路由卡复核",
            "required_asset_type": "no_extra_asset" if missing_context else "user_recording",
            "evidence_role": "must_be_real_evidence_when_core_claim",
            "why_needed": "判断每段需要真实录屏、截图、卡片或 API 辅助图。",
            "can_be_api_generated": False,
            "must_be_real_evidence": True,
            "fallback_if_missing": card.get("fallback_plan", "少量 PPT / 信息卡 / 真实截图 / no_extra_asset / blocked"),
            "blocked_if": "核心证据缺失却试图用 API 图片冒充。",
        }
    elif action == "api_asset_generation_pack":
        base[EXECUTION_SUPPLY_OUTPUT_KEYS[action]] = {
            "generation_needed": bool(card.get("api_generation_targets")),
            "vendor_candidate": "aliyun" if card.get("api_generation_targets") else "not_needed",
            "model_or_service": "待未来真实 API 授权前确认",
            "asset_count": len(card.get("api_generation_targets", []))
            if isinstance(card.get("api_generation_targets"), list)
            else 0,
            "aspect_ratio": "按 segment / card 使用场景决定",
            "resolution": "待执行前确认",
            "style_constraints": card.get("vendor_constraints", {}),
            "segment_usage": card.get("api_generation_targets", []),
            "prompt_needed": True,
            "negative_prompt_needed": True,
            "api_call_allowed_this_round": False,
            "secret_required": False,
            "fallback_plan": card.get("fallback_plan", "少量 PPT / 信息卡 / 真实截图 / no_extra_asset / blocked"),
            "blocked_if": "需要真实 API 调用、读取密钥，或把 API 图当真实证据。",
        }
    elif action == "image_prompt_pack":
        base[EXECUTION_SUPPLY_OUTPUT_KEYS[action]] = {
            "asset_id": "from_image_prompt_specs",
            "segment": first_list_item(card.get("segments")) or "",
            "purpose": "辅助表达，不替代核心证据",
            "positive_prompt": "待基于 image_prompt_specs 细化",
            "negative_prompt": "no official Minecraft assets, logos, fonts, textures, models, sounds; no unreadable Chinese text",
            "style_anchor": "Minecraft-inspired 原创体素方块风",
            "composition": "按后期卡片和 segment 使用位置决定",
            "text_policy": "no_readable_text_by_default",
            "must_not_include": [
                "官方 Minecraft 资产",
                "官方 logo / font / texture / model / sound",
                "素材里没有的证据结论",
            ],
            "acceptance_criteria": "风格匹配、主次清楚、不抢真实证据。",
            "rejected_if": "AI 感过强、文字错误、冒充证据或版权风险。",
        }
    elif action == "asset_validation_pack":
        base[EXECUTION_SUPPLY_OUTPUT_KEYS[action]] = {
            "asset_id": "from_asset_validation_criteria",
            "source": "text_sample_or_future_asset_manifest",
            "intended_use": "待 Codex 复核",
            "validation_result": "pending_human_review",
            "style_fit": "pending",
            "evidence_fit": "must_not_replace_real_evidence",
            "readability": "pending",
            "platform_risk": "pending",
            "copyright_or_official_asset_risk": "pending",
            "human_feel": "pending",
            "required_fix": "revise / reject / downgrade_to_card / no_extra_asset",
            "blocked_if": "素材抢真实证据位、平台误解风险或官方资产复用风险无法排除。",
        }
    elif action == "assembly_decision_pack":
        base[EXECUTION_SUPPLY_OUTPUT_KEYS[action]] = {
            "data_goal_anchor_used": data_goal_fields["data_goal_anchor_used"],
            "segment_goal": "待 Codex 基于 content_route_card 和 script_to_timeline_map 复核",
            "carrier_reason": "主证据优先使用真实录屏 / 截图，辅助素材不得替代证据。",
            "metric_supported": data_goal_fields["success_metric"],
            "variable_preserved": data_goal_fields["primary_variable"],
            "forbidden_variable_avoided": data_goal_fields["forbidden_variables"],
            "post_publish_validation_metric": data_goal_fields["post_publish_validation_metric"],
            "segment": first_list_item(card.get("segments")) or "",
            "primary_carrier": "user_recording_or_screenshot_for_core_evidence",
            "secondary_carrier": "api_generated_image_or_info_card_only_when_auxiliary",
            "asset_to_use": first_list_item(card.get("assembly_slots")) or "",
            "timing": "待 Codex 基于时间线复核",
            "transition": "avoid_hard_splice",
            "tts_relation": "TTS 解释不能抢画面证据",
            "subtitle_relation": "字幕跟随口播，不替代画面判断",
            "evidence_chain_note": "核心证据段不得被 API 图或装饰图打断。",
            "needs_editing_decision_pack": True,
            "blocked_if": "无法判断主证据 / 辅助素材职责，或需要用 AI 图冒充证据。",
        }
    return base


def decide_supply_source(status: dict[str, str], explorer_run: dict[str, Any]) -> str:
    joined_status = "\n".join(str(value) for value in status.values())
    joined_status = f"{joined_status}\n{explorer_run.get('stderr_tail', '')}\n{explorer_run.get('stdout_tail', '')}"
    if "blocked_missing_process_env_api_key" in joined_status or "not_tested_missing_process_env_key" in joined_status:
        return "blocked_missing_process_env_api_key"
    if "blocked_invalid_api_key" in joined_status or "invalid_api_key" in joined_status:
        return "blocked_invalid_api_key"
    if "blocked_network_or_timeout" in joined_status or "timeout" in joined_status:
        return "blocked_network_or_timeout"
    if (
        status.get("validation_status") == "passed"
        and status.get("context_pack_validation") == "passed"
        and status.get("deepseek_generation_status") in {"passed", "passed_with_retries"}
    ):
        return "deepseek_passed"
    if (
        status.get("validation_status") == "fallback"
        and status.get("context_pack_validation") == "fallback_local_only"
        and status.get("fallback_status") == "used"
    ):
        return "fallback_local_only"
    if explorer_run["returncode"] == 0 and status.get("pipeline_status") == "usable_with_fallback":
        return "fallback_local_only"
    return "blocked"


def infer_deepseek_actual_participation(
    *,
    status: dict[str, str],
    supply_source: str,
) -> str:
    joined_status = "\n".join(status.values())
    if supply_source == "deepseek_passed":
        return "deepseek_passed"
    if supply_source in {
        "fallback_local_only",
        "blocked_missing_process_env_api_key",
        "blocked_invalid_api_key",
        "blocked_network_or_timeout",
        "not_attempted_policy_violation",
    }:
        return supply_source
    if "not_tested_missing_process_env_key" in joined_status or "missing_process_env_api_key" in joined_status:
        return "blocked_missing_process_env_api_key"
    return "not_attempted_policy_violation"


def infer_blocked_reason(
    *,
    status: dict[str, str],
    supply_source: str,
    explorer_run: dict[str, Any],
) -> str:
    if supply_source == "blocked_missing_process_env_api_key":
        return "missing_process_env_api_key"
    if supply_source == "blocked_invalid_api_key":
        return "invalid_api_key"
    if supply_source == "blocked_network_or_timeout":
        return "network_or_timeout"
    if supply_source != "blocked":
        return "none"
    joined_status = "\n".join(str(value) for value in status.values())
    joined_status = f"{joined_status}\n{explorer_run.get('stderr_tail', '')}\n{explorer_run.get('stdout_tail', '')}"
    if "blocked_missing_process_env_api_key" in joined_status or "missing_process_env_api_key" in joined_status:
        return "missing_process_env_api_key"
    if "blocked_invalid_api_key" in joined_status or "invalid_api_key" in joined_status:
        return "invalid_api_key"
    if "blocked_network_or_timeout" in joined_status or "timeout" in joined_status:
        return "network_or_timeout"
    if "blocked_invalid_context_pack" in joined_status:
        return "invalid_context_pack"
    if explorer_run.get("returncode") not in {0, None}:
        return "explorer_failed"
    return "unknown_blocked"


def infer_safe_call_mode(status: dict[str, str], supply_source: str) -> str:
    env_file_read = status.get("env_file_read", "unknown")
    process_env_key_allowed = status.get("process_env_key_allowed", "unknown")
    if env_file_read == "true":
        return "legacy_env_file_mode"
    if process_env_key_allowed == "true":
        return "process_env_only"
    if supply_source == "fallback_local_only":
        return "local_fallback_no_deepseek_call"
    return "safe_no_env_file_default"


def build_deepseek_readiness_check(
    *,
    request_validation_status: str,
    supply_source: str,
    fallback_status: str,
    not_deepseek_conclusion: bool,
    deepseek_actual_participation: str,
    context_pack_validation: str,
    status: dict[str, str],
    blocked_reason: str,
) -> dict[str, Any]:
    return {
        "required": True,
        "env_file_read": status.get("env_file_read", "unknown"),
        "process_env_key_allowed": status.get("process_env_key_allowed", "unknown"),
        "process_env_key_present": status.get("process_env_key_present", "unknown"),
        "safe_call_mode": infer_safe_call_mode(status, supply_source),
        "request_validation_status": request_validation_status,
        "supply_source": supply_source,
        "fallback_status": fallback_status,
        "not_deepseek_conclusion": not_deepseek_conclusion,
        "context_pack_validation": context_pack_validation,
        "deepseek_actual_participation": deepseek_actual_participation,
        "blocked_reason": blocked_reason,
        "completion_rule": [
            "deepseek_passed 才能写 DeepSeek 真实参与。",
            "fallback_local_only 必须写 not_deepseek_conclusion = true。",
            "missing_process_env_key 必须写 blocked_missing_process_env_api_key。",
            "token 未观察到减少时，不得写 DeepSeek 已深度参与。",
            "不得把 fallback 写成 DeepSeek 稳定供料。",
        ],
    }


def build_deepseek_supply_gate(
    *,
    request_card: dict[str, Any] | None,
    supply_source: str,
    fallback_status: str,
    not_deepseek_conclusion: bool,
    deepseek_actual_participation: str,
    blocked_reason: str,
) -> dict[str, Any]:
    token_expectation = (
        request_card.get("token_usage_expectation", "token_should_decrease_if_real_call")
        if isinstance(request_card, dict)
        else "token_should_decrease_if_real_call"
    )
    return {
        "mandatory_for_every_task": bool(
            request_card.get("mandatory_for_every_task", True) if isinstance(request_card, dict) else True
        ),
        "supply_request_created": isinstance(request_card, dict),
        "deepseek_call_required": True,
        "deepseek_call_attempted": supply_source == "deepseek_passed",
        "deepseek_actual_participation": deepseek_actual_participation,
        "supply_source": supply_source,
        "fallback_status": fallback_status,
        "not_deepseek_conclusion": not_deepseek_conclusion,
        "blocked_reason": blocked_reason,
        "token_usage_expected": token_expectation,
        "token_usage_observed_or_user_check_required": (
            "user_check_required" if supply_source != "deepseek_passed" else "token_decrement_expected"
        ),
        "fallback_not_completion": bool(
            request_card.get("fallback_not_completion", True) if isinstance(request_card, dict) else True
        ),
        "deepseek_must_not_be_skipped_by_codex_discretion": bool(
            request_card.get("deepseek_must_not_be_skipped_by_codex_discretion", True)
            if isinstance(request_card, dict)
            else True
        ),
    }


def build_token_usage_expectation_check(
    *,
    supply_source: str,
    status: dict[str, str],
    request_card: dict[str, Any] | None,
) -> dict[str, Any]:
    observed = status.get("token_usage_delta") or status.get("token_usage_observed") or "not_available_user_check_required"
    return {
        "token_usage_expectation": (
            request_card.get("token_usage_expectation", "token_should_decrease_if_real_call")
            if isinstance(request_card, dict)
            else "token_should_decrease_if_real_call"
        ),
        "expected_to_decrease": supply_source == "deepseek_passed",
        "observed_token_usage": observed,
        "token_usage_observed_or_user_check_required": (
            "token_decrement_expected" if supply_source == "deepseek_passed" else "user_check_required"
        ),
        "cannot_claim_deepseek_deep_participation_if_token_not_decreased": True,
        "fallback_local_only_token_rule": "fallback_local_only 不应减少 DeepSeek token，也不能写 DeepSeek 已深度参与。",
    }


def build_deepseek_participation_report(
    *,
    supply_source: str,
    deepseek_actual_participation: str,
    fallback_status: str,
    not_deepseek_conclusion: bool,
    blocked_reason: str,
    token_usage_expectation_check: dict[str, Any],
) -> dict[str, Any]:
    return {
        "deepseek_call_real": supply_source == "deepseek_passed",
        "deepseek_actual_participation": deepseek_actual_participation,
        "supply_source": supply_source,
        "fallback_status": fallback_status,
        "not_deepseek_conclusion": not_deepseek_conclusion,
        "blocked_reason": blocked_reason,
        "token_usage_expectation_check": token_usage_expectation_check,
        "codex_original_file_review_required": True,
        "deepseek_may_write_files": False,
        "deepseek_may_decide_project_facts": False,
        "multi_agent_runtime_validation": "not_started",
    }


def build_post_risk_review_support(
    *,
    trigger_reason: str,
    supply_source: str,
    not_deepseek_conclusion: bool,
) -> dict[str, Any] | None:
    if trigger_reason != "mandatory_post_risk_review":
        return None
    return {
        "status_promotion_risk": "check_required_no_forbidden_status_promotion",
        "forbidden_change_risk": "check_required_no_env_media_or_latest_review_pack_change",
        "missed_sync_files": "check_required_docs_scripts_schema_fixture_logs_package_paths",
        "fallback_mislabel_risk": (
            "present" if not_deepseek_conclusion or supply_source != "deepseek_passed" else "none_observed"
        ),
        "remaining_work": "Codex must run validation, sync logs/package/path index, and report token check boundary.",
    }


def build_supply_pack(
    *,
    args: argparse.Namespace,
    output_dir: Path,
    context_files: list[Path],
    explorer_run: dict[str, Any],
    explorer_pack: dict[str, Any],
    supply_id: str,
) -> dict[str, Any]:
    status = explorer_pack["status"]
    sections = explorer_pack["sections"]
    request_card = getattr(args, "request_card", None)
    supply_source = decide_supply_source(status, explorer_run)
    deepseek_actual_participation = infer_deepseek_actual_participation(
        status=status,
        supply_source=supply_source,
    )
    blocked_reason = infer_blocked_reason(
        status=status,
        supply_source=supply_source,
        explorer_run=explorer_run,
    )
    actual_action = choose_auto_action(args.trigger_reason) if args.action == "auto" else args.action
    files_considered = [relative_label(path) for path in context_files]
    files_recommended = collect_recommended_files(
        sections.get("must_read_file_map"),
        fallback_files=files_considered,
    )
    risks = collect_risks(sections.get("risk_and_conflict_report"))
    missing_files = collect_missing_files(sections)
    editing_decision_pack = build_editing_decision_support(
        request_card=request_card,
        action=actual_action,
    )
    execution_supply_pack = build_execution_supply_support(
        request_card=request_card,
        action=actual_action,
    )
    request_missing_context = request_card.get("missing_context", []) if request_card else []
    if editing_decision_pack:
        request_missing_context = list(request_missing_context) + [
            f"editing_decision_pack_missing:{field_name}"
            for field_name in editing_decision_pack["missing_context"]
        ]
    if execution_supply_pack:
        request_missing_context = list(request_missing_context) + [
            f"{actual_action}_missing:{field_name}"
            for field_name in execution_supply_pack["missing_context"]
        ]
    not_deepseek_conclusion = supply_source != "deepseek_passed"
    request_validation_status = getattr(args, "request_validation_status", "unknown")
    context_pack_validation = status.get("context_pack_validation", "unknown")
    fallback_status = status.get("fallback_status", "unknown")
    deepseek_readiness_check = build_deepseek_readiness_check(
        request_validation_status=request_validation_status,
        supply_source=supply_source,
        fallback_status=fallback_status,
        not_deepseek_conclusion=not_deepseek_conclusion,
        deepseek_actual_participation=deepseek_actual_participation,
        context_pack_validation=context_pack_validation,
        status=status,
        blocked_reason=blocked_reason,
    )
    token_usage_expectation_check = build_token_usage_expectation_check(
        supply_source=supply_source,
        status=status,
        request_card=request_card,
    )
    deepseek_supply_gate = build_deepseek_supply_gate(
        request_card=request_card,
        supply_source=supply_source,
        fallback_status=fallback_status,
        not_deepseek_conclusion=not_deepseek_conclusion,
        deepseek_actual_participation=deepseek_actual_participation,
        blocked_reason=blocked_reason,
    )
    deepseek_participation_report = build_deepseek_participation_report(
        supply_source=supply_source,
        deepseek_actual_participation=deepseek_actual_participation,
        fallback_status=fallback_status,
        not_deepseek_conclusion=not_deepseek_conclusion,
        blocked_reason=blocked_reason,
        token_usage_expectation_check=token_usage_expectation_check,
    )
    post_risk_review = build_post_risk_review_support(
        trigger_reason=args.trigger_reason,
        supply_source=supply_source,
        not_deepseek_conclusion=not_deepseek_conclusion,
    )
    codex_next_input = {
        "read_first": files_recommended[:8],
        "use_as": "readonly_supply_pack",
        "warning": (
            "This pack is local fallback, not a DeepSeek conclusion."
            if not_deepseek_conclusion
            else "DeepSeek generated the pack, but Codex must still verify original files."
        ),
    }
    if editing_decision_pack:
        codex_next_input.update(
            {
                "editing_decision_pack_review_required": True,
                "blocked_if_insufficient_editing_sample": editing_decision_pack[
                    "blocked_if_insufficient_editing_sample"
                ],
                "codex_original_file_review_required": True,
            }
        )
    if execution_supply_pack:
        codex_next_input.update(
            {
                "execution_supply_pack_review_required": True,
                "execution_supply_action": actual_action,
                "blocked_if_insufficient_execution_sample": execution_supply_pack[
                    "blocked_if_insufficient_execution_sample"
                ],
                "codex_original_file_review_required": True,
                "api_call_allowed_this_round": False,
                "env_or_secret_read_allowed": False,
                "media_file_read_allowed": False,
            }
        )
    if post_risk_review:
        codex_next_input.update(
            {
                "post_risk_review_required": True,
                "status_promotion_risk": post_risk_review["status_promotion_risk"],
                "forbidden_change_risk": post_risk_review["forbidden_change_risk"],
                "missed_sync_files": post_risk_review["missed_sync_files"],
                "fallback_mislabel_risk": post_risk_review["fallback_mislabel_risk"],
                "remaining_work": post_risk_review["remaining_work"],
            }
        )
    return {
        "supply_id": supply_id,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "request_id": request_card.get("request_id") if request_card else supply_id,
        "request_file": getattr(args, "request_file", None),
        "request_validation_status": request_validation_status,
        "current_goal": request_card.get("current_goal", "") if request_card else "",
        "data_goal_anchor": request_card.get("data_goal_anchor", {}) if request_card else {},
        "current_stage_goal": request_card.get("current_stage_goal", "") if request_card else "",
        "main_bottleneck": request_card.get("main_bottleneck", "") if request_card else "",
        "primary_variable": request_card.get("primary_variable", "") if request_card else "",
        "forbidden_variables": request_card.get("forbidden_variables", []) if request_card else [],
        "success_metric": request_card.get("success_metric", "") if request_card else "",
        "failure_metric": request_card.get("failure_metric", "") if request_card else "",
        "post_publish_validation_metric": request_card.get("post_publish_validation_metric", "") if request_card else "",
        "current_step": request_card.get("current_step", "") if request_card else "",
        "known_context": request_card.get("known_context", []) if request_card else [],
        "missing_context": request_missing_context,
        "decision_needed": request_card.get("decision_needed", "") if request_card else "",
        "task": args.task,
        "task_type": args.task_type,
        "trigger_reason": args.trigger_reason,
        "requested_action": args.action,
        "action": actual_action,
        "max_rounds": args.max_rounds,
        "supply_source": supply_source,
        "not_deepseek_conclusion": not_deepseek_conclusion,
        "deepseek_actual_participation": deepseek_actual_participation,
        "blocked_reason": blocked_reason,
        "deepseek_supply_gate": deepseek_supply_gate,
        "deepseek_readiness_check": deepseek_readiness_check,
        "deepseek_participation_report": deepseek_participation_report,
        "token_usage_expectation_check": token_usage_expectation_check,
        "post_risk_review": post_risk_review,
        "env_file_read": status.get("env_file_read", "unknown"),
        "process_env_key_allowed": status.get("process_env_key_allowed", "unknown"),
        "process_env_key_present": status.get("process_env_key_present", "unknown"),
        "api_key_printed": status.get("api_key_printed", "false"),
        "api_key_written": status.get("api_key_written", "false"),
        "context_pack_validation": context_pack_validation,
        "deepseek_generation_status": status.get("deepseek_generation_status", "unknown"),
        "fallback_status": fallback_status,
        "pipeline_status": (
            "usable"
            if supply_source == "deepseek_passed"
            else "usable_with_fallback"
            if supply_source == "fallback_local_only"
            else "blocked"
        ),
        "multi_agent_runtime_validation": "not_started",
        "files_considered": files_considered,
        "files_recommended": files_recommended,
        "risks": risks,
        "missing_files": missing_files,
        "editing_decision_pack": editing_decision_pack,
        "execution_supply_pack": execution_supply_pack,
        "codex_next_input": codex_next_input,
        "not_allowed": [
            "Do not treat fallback_local_only as a DeepSeek conclusion.",
            "Do not claim DeepSeek is stable production supply.",
            "Do not claim multi-agent runtime is running.",
            "Do not let DeepSeek write files or decide project facts.",
            "Do not read .env, API keys, media files, or dist/latest_review_pack/.",
            "Do not call Aliyun or other real generation APIs in mechanism-only tests.",
        ],
        "explorer_status": status,
        "explorer_returncode": explorer_run["returncode"],
        "explorer_pack_path": relative_label(EXPLORER_OUTPUT),
        "output_dir": relative_label(output_dir),
        "sections": sections if supply_source != "blocked" else {},
    }


def write_supply_outputs(pack: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    pack_json_path = output_dir / "latest_supply_pack.json"
    manifest_path = output_dir / "latest_supply_manifest.json"
    pack_md_path = output_dir / "latest_supply_pack.md"
    pack_json_path.write_text(json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    manifest = {
        "supply_id": pack["supply_id"],
        "generated_at_utc": pack["generated_at_utc"],
        "request_id": pack["request_id"],
        "request_file": pack["request_file"],
        "request_validation_status": pack["request_validation_status"],
        "current_goal": pack["current_goal"],
        "data_goal_anchor": pack.get("data_goal_anchor", {}),
        "current_stage_goal": pack.get("current_stage_goal", ""),
        "main_bottleneck": pack.get("main_bottleneck", ""),
        "primary_variable": pack.get("primary_variable", ""),
        "forbidden_variables": pack.get("forbidden_variables", []),
        "success_metric": pack.get("success_metric", ""),
        "failure_metric": pack.get("failure_metric", ""),
        "post_publish_validation_metric": pack.get("post_publish_validation_metric", ""),
        "current_step": pack["current_step"],
        "known_context": pack["known_context"],
        "missing_context": pack["missing_context"],
        "decision_needed": pack["decision_needed"],
        "task_type": pack["task_type"],
        "trigger_reason": pack["trigger_reason"],
        "action": pack["action"],
        "supply_source": pack["supply_source"],
        "context_pack_validation": pack["context_pack_validation"],
        "fallback_status": pack["fallback_status"],
        "pipeline_status": pack["pipeline_status"],
        "multi_agent_runtime_validation": pack["multi_agent_runtime_validation"],
        "not_deepseek_conclusion": pack["not_deepseek_conclusion"],
        "deepseek_actual_participation": pack["deepseek_actual_participation"],
        "blocked_reason": pack["blocked_reason"],
        "deepseek_supply_gate": pack["deepseek_supply_gate"],
        "deepseek_readiness_check": pack["deepseek_readiness_check"],
        "deepseek_participation_report": pack["deepseek_participation_report"],
        "token_usage_expectation_check": pack["token_usage_expectation_check"],
        "post_risk_review": pack["post_risk_review"],
        "env_file_read": pack["env_file_read"],
        "process_env_key_allowed": pack["process_env_key_allowed"],
        "process_env_key_present": pack["process_env_key_present"],
        "api_key_printed": pack["api_key_printed"],
        "api_key_written": pack["api_key_written"],
        "codex_next_input": pack["codex_next_input"],
        "editing_decision_pack": pack.get("editing_decision_pack"),
        "execution_supply_pack": pack.get("execution_supply_pack"),
        "post_risk_review": pack.get("post_risk_review"),
        "not_allowed": pack["not_allowed"],
        "files": {
            "latest_supply_pack_md": relative_label(pack_md_path),
            "latest_supply_pack_json": relative_label(pack_json_path),
            "latest_supply_manifest_json": relative_label(manifest_path),
            "explorer_pack": pack["explorer_pack_path"],
        },
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# DeepSeek supply controller latest_supply_pack",
        "",
        f"- `supply_id`: `{pack['supply_id']}`",
        f"- `request_id`: `{pack['request_id']}`",
        f"- `request_validation_status`: `{pack['request_validation_status']}`",
        f"- `task_type`: `{pack['task_type']}`",
        f"- `trigger_reason`: `{pack['trigger_reason']}`",
        f"- `action`: `{pack['action']}`",
        f"- `supply_source`: `{pack['supply_source']}`",
        f"- `context_pack_validation`: `{pack['context_pack_validation']}`",
        f"- `deepseek_generation_status`: `{pack['deepseek_generation_status']}`",
        f"- `fallback_status`: `{pack['fallback_status']}`",
        f"- `pipeline_status`: `{pack['pipeline_status']}`",
        "- `multi_agent_runtime_validation`: `not_started`",
        f"- `not_deepseek_conclusion`: `{str(pack['not_deepseek_conclusion']).lower()}`",
        f"- `deepseek_actual_participation`: `{pack['deepseek_actual_participation']}`",
        f"- `blocked_reason`: `{pack['blocked_reason']}`",
        f"- `token_usage_observed_or_user_check_required`: `{pack['token_usage_expectation_check']['token_usage_observed_or_user_check_required']}`",
        f"- `env_file_read`: `{pack['env_file_read']}`",
        f"- `process_env_key_allowed`: `{pack['process_env_key_allowed']}`",
        f"- `process_env_key_present`: `{pack['process_env_key_present']}`",
        f"- `api_key_printed`: `{pack['api_key_printed']}`",
        f"- `api_key_written`: `{pack['api_key_written']}`",
        "",
        "## request_state（请求状态）",
        "",
        "```json",
        json.dumps(
            {
                "request_file": pack["request_file"],
                "current_goal": pack["current_goal"],
                "data_goal_anchor": pack.get("data_goal_anchor", {}),
                "current_stage_goal": pack.get("current_stage_goal", ""),
                "main_bottleneck": pack.get("main_bottleneck", ""),
                "primary_variable": pack.get("primary_variable", ""),
                "forbidden_variables": pack.get("forbidden_variables", []),
                "success_metric": pack.get("success_metric", ""),
                "failure_metric": pack.get("failure_metric", ""),
                "post_publish_validation_metric": pack.get("post_publish_validation_metric", ""),
                "current_step": pack["current_step"],
                "known_context": pack["known_context"],
                "missing_context": pack["missing_context"],
                "decision_needed": pack["decision_needed"],
            },
            ensure_ascii=False,
            indent=2,
        ),
        "```",
        "",
        "## deepseek_supply_gate（DeepSeek 供料闸门）",
        "",
        "```json",
        json.dumps(pack["deepseek_supply_gate"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## deepseek_readiness_check（DeepSeek 就绪检查）",
        "",
        "```json",
        json.dumps(pack["deepseek_readiness_check"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## deepseek_participation_report（DeepSeek 参与报告）",
        "",
        "```json",
        json.dumps(pack["deepseek_participation_report"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## token_usage_expectation_check（token 使用预期检查）",
        "",
        "```json",
        json.dumps(pack["token_usage_expectation_check"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## task（任务）",
        "",
        pack["task"],
        "",
        "## files_considered（已考虑文件）",
        "",
        "```json",
        json.dumps(pack["files_considered"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## files_recommended（建议读取文件）",
        "",
        "```json",
        json.dumps(pack["files_recommended"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## risks（风险）",
        "",
        "```json",
        json.dumps(pack["risks"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## missing_files（缺失文件）",
        "",
        "```json",
        json.dumps(pack["missing_files"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## editing_decision_pack（剪辑决策包）",
        "",
        "```json",
        json.dumps(pack.get("editing_decision_pack"), ensure_ascii=False, indent=2),
        "```",
        "",
        "## execution_supply_pack（执行供料包）",
        "",
        "```json",
        json.dumps(pack.get("execution_supply_pack"), ensure_ascii=False, indent=2),
        "```",
        "",
        "## post_risk_review（执行后风险复核）",
        "",
        "```json",
        json.dumps(pack.get("post_risk_review"), ensure_ascii=False, indent=2),
        "```",
        "",
        "## codex_next_input（给 Codex 的下一步输入）",
        "",
        "```json",
        json.dumps(pack["codex_next_input"], ensure_ascii=False, indent=2),
        "```",
        "",
        "## not_allowed（禁止事项）",
        "",
        "```json",
        json.dumps(pack["not_allowed"], ensure_ascii=False, indent=2),
        "```",
    ]
    pack_md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_blocked_manifest(
    *,
    output_dir: Path,
    args: argparse.Namespace,
    supply_id: str,
    error: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    request_card = getattr(args, "request_card", None)
    manifest = {
        "supply_id": supply_id,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "request_id": request_card.get("request_id") if isinstance(request_card, dict) else None,
        "request_file": getattr(args, "request_file", None),
        "request_validation_status": "blocked",
        "task_type": (
            request_card.get("task_type")
            if isinstance(request_card, dict)
            else getattr(args, "task_type", None)
        ),
        "trigger_reason": (
            request_card.get("trigger_reason")
            if isinstance(request_card, dict)
            else getattr(args, "trigger_reason", None)
        ),
        "action": request_card.get("action") if isinstance(request_card, dict) else getattr(args, "action", None),
        "supply_source": "blocked",
        "context_pack_validation": "blocked",
        "fallback_status": "not_used",
        "pipeline_status": "blocked",
        "multi_agent_runtime_validation": "not_started",
        "not_deepseek_conclusion": True,
        "blocked_reason": error,
        "deepseek_supply_gate": {
            "mandatory_for_every_task": True,
            "supply_request_created": isinstance(request_card, dict),
            "deepseek_call_required": True,
            "deepseek_call_attempted": False,
            "deepseek_actual_participation": "not_attempted_policy_violation",
            "supply_source": "blocked",
            "fallback_status": "not_used",
            "not_deepseek_conclusion": True,
            "blocked_reason": error,
            "token_usage_expected": "token_should_decrease_if_real_call",
            "token_usage_observed_or_user_check_required": "user_check_required",
            "fallback_not_completion": True,
            "deepseek_must_not_be_skipped_by_codex_discretion": True,
        },
        "deepseek_readiness_check": {
            "required": True,
            "env_file_read": "false",
            "process_env_key_allowed": "unknown",
            "process_env_key_present": "unknown",
            "safe_call_mode": "blocked_before_context_read",
            "request_validation_status": "blocked",
            "supply_source": "blocked",
            "fallback_status": "not_used",
            "not_deepseek_conclusion": True,
            "context_pack_validation": "blocked",
            "deepseek_actual_participation": "not_attempted_policy_violation",
            "blocked_reason": error,
        },
        "deepseek_participation_report": {
            "deepseek_call_real": False,
            "deepseek_actual_participation": "not_attempted_policy_violation",
            "supply_source": "blocked",
            "fallback_status": "not_used",
            "not_deepseek_conclusion": True,
            "blocked_reason": error,
            "token_usage_expectation_check": {
                "token_usage_expectation": "token_should_decrease_if_real_call",
                "expected_to_decrease": False,
                "observed_token_usage": "not_available_user_check_required",
                "token_usage_observed_or_user_check_required": "user_check_required",
                "cannot_claim_deepseek_deep_participation_if_token_not_decreased": True,
            },
            "codex_original_file_review_required": True,
            "deepseek_may_write_files": False,
            "deepseek_may_decide_project_facts": False,
            "multi_agent_runtime_validation": "not_started",
        },
        "codex_next_input": {
            "read_first": [],
            "use_as": "blocked_request_validation_manifest",
            "warning": "Request validation blocked before any context file was read.",
        },
        "error": error,
    }
    (output_dir / "latest_supply_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    raw_args = parse_args(sys.argv[1:])
    supply_id = datetime.now(timezone.utc).strftime("supply_%Y%m%dT%H%M%SZ")
    try:
        if raw_args.request_file:
            request_file = resolve_request_file(raw_args.request_file)
            request_card = load_request_card(request_file)
            raw_args.request_card = request_card
            raw_args.request_file = str(request_file)
            validate_request_card(request_card)
            args = namespace_from_request(
                args=raw_args,
                card=request_card,
                request_file=request_file,
            )
        else:
            args = namespace_from_cli(raw_args)
        output_dir = resolve_output_dir(args.output_dir)
        context_files = resolve_context_files(args.context_file)
    except Exception as exc:  # noqa: BLE001
        output_dir = DEFAULT_OUTPUT_DIR
        write_blocked_manifest(
            output_dir=output_dir,
            args=raw_args,
            supply_id=supply_id,
            error=f"{type(exc).__name__}:{exc}",
        )
        print(json.dumps({"supply_source": "blocked", "error": str(exc)}, ensure_ascii=False))
        return 2

    context_labels = [relative_label(path) for path in context_files]
    controller_task = build_controller_task(
        task=args.task,
        task_type=args.task_type,
        trigger_reason=args.trigger_reason,
        action=args.action,
        context_labels=context_labels,
        request_card=getattr(args, "request_card", None),
    )
    request_card = getattr(args, "request_card", None)
    allow_process_env_api_key = allow_process_env_api_key_enabled(args, request_card)
    if request_forbids_env_or_secret(request_card) and not allow_process_env_api_key:
        explorer_run = {
            "returncode": 0,
            "stdout_tail": "local fallback used because request forbids .env / secrets and process env key was not allowed",
            "stderr_tail": "",
        }
        explorer_pack = build_local_fallback_explorer_pack(
            controller_task=controller_task,
            context_labels=context_labels,
            request_card=request_card,
            reason="skipped_for_forbidden_env_or_secret_policy_process_env_not_allowed",
        )
    else:
        explorer_run = run_explorer(
            controller_task,
            context_files,
            allow_process_env_api_key=allow_process_env_api_key,
        )
        explorer_pack = read_explorer_pack()
    pack = build_supply_pack(
        args=args,
        output_dir=output_dir,
        context_files=context_files,
        explorer_run=explorer_run,
        explorer_pack=explorer_pack,
        supply_id=supply_id,
    )
    write_supply_outputs(pack, output_dir)
    print(
        json.dumps(
            {
                "supply_source": pack["supply_source"],
                "context_pack_validation": pack["context_pack_validation"],
                "fallback_status": pack["fallback_status"],
                "deepseek_actual_participation": pack["deepseek_actual_participation"],
                "blocked_reason": pack["blocked_reason"],
                "deepseek_supply_gate": pack["deepseek_supply_gate"],
                "deepseek_participation_report": pack["deepseek_participation_report"],
                "token_usage_expectation_check": pack["token_usage_expectation_check"],
                "post_risk_review": pack["post_risk_review"],
                "deepseek_readiness_check": pack["deepseek_readiness_check"],
                "env_file_read": pack["env_file_read"],
                "api_key_printed": pack["api_key_printed"],
                "api_key_written": pack["api_key_written"],
                "pipeline_status": pack["pipeline_status"],
                "latest_supply_pack": relative_label(output_dir / "latest_supply_pack.md"),
            },
            ensure_ascii=False,
        )
    )
    return 0 if pack["supply_source"] in {"deepseek_passed", "fallback_local_only"} else 1


if __name__ == "__main__":
    sys.exit(main())
