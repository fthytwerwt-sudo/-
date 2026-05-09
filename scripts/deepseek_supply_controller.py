#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
ALLOWED_ACTIONS = {"file_map", "risk_report", "context_summary", "missing_files", "auto"}
ALLOWED_TRIGGER_REASONS = {
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
            and (normalized_file == forbidden or normalized_file.startswith(forbidden.rstrip("/") + "/"))
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
    }
    return "\n".join(
        [
            "DeepSeek supply controller request for 视频工厂.",
            f"task_type: {task_type}",
            f"trigger_reason: {trigger_reason}",
            f"action: {actual_action}",
            action_prompts[actual_action],
            "Stay read-only. Do not write files. Do not decide project facts.",
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


def run_explorer(controller_task: str, context_files: list[Path]) -> dict[str, Any]:
    command = [sys.executable, str(EXPLORER_SCRIPT), "--task", controller_task]
    for path in context_files:
        command.extend(["--context-file", relative_label(path)])
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return {
        "returncode": result.returncode,
        "stdout_tail": result.stdout[-500:],
        "stderr_tail": result.stderr[-500:],
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


def decide_supply_source(status: dict[str, str], explorer_run: dict[str, Any]) -> str:
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
    actual_action = choose_auto_action(args.trigger_reason) if args.action == "auto" else args.action
    files_considered = [relative_label(path) for path in context_files]
    files_recommended = collect_recommended_files(
        sections.get("must_read_file_map"),
        fallback_files=files_considered,
    )
    risks = collect_risks(sections.get("risk_and_conflict_report"))
    missing_files = collect_missing_files(sections)
    not_deepseek_conclusion = supply_source != "deepseek_passed"
    codex_next_input = {
        "read_first": files_recommended[:8],
        "use_as": "readonly_supply_pack",
        "warning": (
            "This pack is local fallback, not a DeepSeek conclusion."
            if not_deepseek_conclusion
            else "DeepSeek generated the pack, but Codex must still verify original files."
        ),
    }
    return {
        "supply_id": supply_id,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "request_id": request_card.get("request_id") if request_card else supply_id,
        "request_file": getattr(args, "request_file", None),
        "request_validation_status": getattr(args, "request_validation_status", "unknown"),
        "current_goal": request_card.get("current_goal", "") if request_card else "",
        "current_step": request_card.get("current_step", "") if request_card else "",
        "known_context": request_card.get("known_context", []) if request_card else [],
        "missing_context": request_card.get("missing_context", []) if request_card else [],
        "decision_needed": request_card.get("decision_needed", "") if request_card else "",
        "task": args.task,
        "task_type": args.task_type,
        "trigger_reason": args.trigger_reason,
        "requested_action": args.action,
        "action": actual_action,
        "max_rounds": args.max_rounds,
        "supply_source": supply_source,
        "not_deepseek_conclusion": not_deepseek_conclusion,
        "context_pack_validation": status.get("context_pack_validation", "unknown"),
        "deepseek_generation_status": status.get("deepseek_generation_status", "unknown"),
        "fallback_status": status.get("fallback_status", "unknown"),
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
        "codex_next_input": codex_next_input,
        "not_allowed": [
            "Do not treat fallback_local_only as a DeepSeek conclusion.",
            "Do not claim DeepSeek is stable production supply.",
            "Do not claim multi-agent runtime is running.",
            "Do not let DeepSeek write files or decide project facts.",
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
        "codex_next_input": pack["codex_next_input"],
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
        "",
        "## request_state（请求状态）",
        "",
        "```json",
        json.dumps(
            {
                "request_file": pack["request_file"],
                "current_goal": pack["current_goal"],
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
    explorer_run = run_explorer(controller_task, context_files)
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
                "pipeline_status": pack["pipeline_status"],
                "latest_supply_pack": relative_label(output_dir / "latest_supply_pack.md"),
            },
            ensure_ascii=False,
        )
    )
    return 0 if pack["supply_source"] in {"deepseek_passed", "fallback_local_only"} else 1


if __name__ == "__main__":
    sys.exit(main())
