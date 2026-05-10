#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import socket
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
OUTPUT_PATH = ROOT / "dist" / "deepseek_readonly_explorer" / "latest_prefetch_context_pack.md"
DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"
ESCALATION_MODEL = "deepseek-v4-pro"
REQUEST_TIMEOUT_SECONDS = 60
MAX_CHARS_PER_CONTEXT_FILE = 6000
MAX_TOTAL_CONTEXT_CHARS = 18000
RETRY_PLANS = [
    {
        "mode": "single_call_safe",
        "per_file_limit": MAX_CHARS_PER_CONTEXT_FILE,
        "total_limit": MAX_TOTAL_CONTEXT_CHARS,
        "headings_only": False,
        "output_constraints": (
            "Keep every list short. Limit each list to at most 4 items. "
            "Keep every sentence compact."
        ),
    },
    {
        "mode": "compressed_retry",
        "per_file_limit": 3000,
        "total_limit": 9000,
        "headings_only": False,
        "output_constraints": (
            "Reduce output size. Limit each list to at most 3 items. "
            "Keep summary strings under 90 characters."
        ),
    },
    {
        "mode": "minimal_retry",
        "per_file_limit": 1200,
        "total_limit": 3600,
        "headings_only": True,
        "output_constraints": (
            "Use the smallest valid JSON that still answers the task. "
            "Limit each list to at most 2 items. "
            "Keep summary strings under 60 characters."
        ),
    },
]
REQUIRED_TOP_LEVEL_KEYS = [
    "prefetch_context_pack",
    "must_read_file_map",
    "risk_and_conflict_report",
    "candidate_summary",
]
STOPWORDS = {
    "请",
    "作为",
    "只读",
    "分析",
    "当前",
    "仓库",
    "规则",
    "输出",
    "文件",
    "不要",
    "项目",
    "事实",
    "相关",
    "任务",
    "问题",
    "哪些",
    "给出",
    "下一轮",
    "优先",
    "读取",
    "修正",
    "真实",
    "最小",
    "测试",
    "project",
    "readonly",
    "explorer",
}
RETRYABLE_FAILURES = {
    "timeout",
    "empty_content",
    "finish_reason_length",
    "json_parse_error",
    "missing_required_keys",
    "schema_validation_failed",
    "runtime_error",
}


JSON_OUTPUT_EXAMPLE = {
    "prefetch_context_pack": {
        "confirmed": [],
        "pending_verification": [],
        "source_summary": [],
    },
    "must_read_file_map": {
        "required_files": [],
        "optional_files": [],
        "reason": "",
    },
    "risk_and_conflict_report": {
        "risks": [],
        "conflicts": [],
        "blocked_if": [],
    },
    "candidate_summary": {
        "summary": "",
        "recommended_next_step": "",
        "not_allowed": [],
    },
}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run DeepSeek readonly explorer validation or a real-task supply probe."
    )
    parser.add_argument(
        "--task",
        help="Optional readonly analysis task to replace the default smoke-test prompt.",
    )
    parser.add_argument(
        "--context-file",
        action="append",
        default=[],
        help="Optional file path to include as readonly analysis context. Repeatable.",
    )
    parser.add_argument(
        "--no-env-file",
        action="store_true",
        help="Do not read .env; use process environment only for DeepSeek settings.",
    )
    return parser.parse_args(argv)


def load_env(path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    if not path.exists():
        return data
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def write_report(lines: list[str]) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def resolve_context_paths(raw_paths: list[str]) -> list[Path]:
    resolved_paths: list[Path] = []
    for raw_path in raw_paths:
        path = Path(raw_path)
        if not path.is_absolute():
            path = ROOT / path
        resolved_paths.append(path.resolve())
    return resolved_paths


def read_context_sources(paths: list[Path]) -> list[dict[str, object]]:
    sources: list[dict[str, object]] = []
    for path in paths:
        try:
            relative_label = str(path.relative_to(ROOT))
        except ValueError:
            relative_label = str(path)
        sources.append(
            {
                "path": path,
                "label": relative_label,
                "text": path.read_text(encoding="utf-8"),
            }
        )
    return sources


def json_block(value: object) -> list[str]:
    return [
        "```json",
        json.dumps(value, ensure_ascii=False, indent=2),
        "```",
    ]


def tokenize_task(task_prompt: str) -> list[str]:
    raw_tokens = re.findall(r"[A-Za-z0-9_./-]{3,}|[\u4e00-\u9fff]{2,}", task_prompt)
    tokens: list[str] = []
    for token in raw_tokens:
        lowered = token.lower()
        if lowered in STOPWORDS:
            continue
        if token not in tokens:
            tokens.append(token)
    return tokens[:14]


def select_relevant_lines(text: str, task_keywords: list[str], headings_only: bool) -> list[str]:
    lines = text.splitlines()
    intro_lines = [line for line in lines if line.strip()][:8]
    heading_lines = [line for line in lines if line.lstrip().startswith("#")]
    keyword_lines = [
        line
        for line in lines
        if any(keyword in line for keyword in task_keywords) and line.strip()
    ]
    selected = intro_lines + heading_lines + keyword_lines
    if headings_only:
        selected = intro_lines[:3] + heading_lines + keyword_lines[:10]
    deduped: list[str] = []
    seen: set[str] = set()
    for line in selected:
        normalized = line.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(line)
    return deduped


def compress_source(
    source: dict[str, object],
    task_keywords: list[str],
    per_file_limit: int,
    remaining_total_chars: int,
    headings_only: bool,
) -> tuple[str, dict[str, object]]:
    label = str(source["label"])
    text = str(source["text"])
    heading_candidates = [
        line.strip()
        for line in text.splitlines()
        if line.lstrip().startswith("#") and line.strip()
    ][:8]
    selected_lines = select_relevant_lines(text, task_keywords, headings_only=headings_only)
    excerpt = "\n".join(selected_lines).strip() or text[:per_file_limit]
    excerpt_limit = min(per_file_limit, remaining_total_chars)
    if excerpt_limit <= 0:
        excerpt = ""
    elif len(excerpt) > excerpt_limit:
        excerpt = excerpt[:excerpt_limit].rstrip() + "\n...[truncated]"
    truncated = len(excerpt) < len(text)
    metadata = {
        "path": label,
        "original_chars": len(text),
        "used_chars": len(excerpt),
        "truncated": truncated,
        "headings": heading_candidates,
    }
    if not excerpt:
        return "", metadata
    wrapped_excerpt = (
        f"FILE: {label}\n"
        f"ORIGINAL_CHARS: {len(text)}\n"
        f"USED_CHARS: {len(excerpt)}\n"
        f"TRUNCATED: {'true' if truncated else 'false'}\n"
        "BEGIN_CONTENT\n"
        f"{excerpt}\n"
        "END_CONTENT"
    )
    return wrapped_excerpt, metadata


def build_context_bundle(
    sources: list[dict[str, object]],
    task_prompt: str,
    plan: dict[str, object],
) -> tuple[str, dict[str, object]]:
    task_keywords = tokenize_task(task_prompt)
    remaining_total_chars = int(plan["total_limit"])
    context_parts: list[str] = []
    metadata_entries: list[dict[str, object]] = []
    truncated_files: list[str] = []
    for source in sources:
        excerpt, metadata = compress_source(
            source,
            task_keywords,
            per_file_limit=int(plan["per_file_limit"]),
            remaining_total_chars=remaining_total_chars,
            headings_only=bool(plan["headings_only"]),
        )
        metadata_entries.append(metadata)
        if metadata["truncated"]:
            truncated_files.append(str(metadata["path"]))
        if excerpt:
            context_parts.append(excerpt)
            remaining_total_chars -= len(excerpt)
            if remaining_total_chars <= 0:
                break
    context_bundle = "\n\n".join(context_parts)
    metadata = {
        "context_truncated": bool(truncated_files),
        "truncated_files": truncated_files,
        "context_files": metadata_entries,
        "context_size_chars": len(context_bundle),
        "task_keywords": task_keywords,
    }
    return context_bundle, metadata


def build_user_prompt(
    *,
    task_prompt: str,
    context_bundle: str,
    plan: dict[str, object],
) -> str:
    json_example = json.dumps(JSON_OUTPUT_EXAMPLE, ensure_ascii=False, indent=2)
    prompt_parts = [
        "Return JSON only. Do not include Markdown fences or prose.",
        "Use the provided repository context when it exists.",
        "Do not claim write access. Do not say you changed files.",
        "Do not upgrade project facts to confirmed unless they are explicitly stated in the provided context.",
        "Every top-level field must be useful and concise.",
        str(plan["output_constraints"]),
        task_prompt,
        "Use this exact JSON shape:\n" + json_example,
    ]
    if context_bundle:
        prompt_parts.extend(
            [
                "Analyze only the following provided file contents and name relevant files explicitly in your output where useful.",
                context_bundle,
            ]
        )
    return "\n\n".join(prompt_parts)


def classify_http_error(exc: urllib.error.HTTPError, detail: str) -> tuple[str, bool]:
    lowered = detail.lower()
    if exc.code in {401, 403} or "invalid api key" in lowered or "authentication" in lowered:
        return "invalid_api_key", False
    if "model" in lowered and ("not found" in lowered or "does not exist" in lowered):
        return "model_not_found", False
    if exc.code == 429:
        return "rate_limited", True
    if exc.code in {408, 500, 502, 503, 504}:
        return "http_retryable_error", True
    return "http_error", False


def classify_runtime_error(exc: Exception) -> str:
    if isinstance(exc, TimeoutError | socket.timeout):
        return "timeout"
    message = str(exc).lower()
    if "timed out" in message:
        return "timeout"
    return "runtime_error"


def validate_context_pack_schema(
    parsed_content: dict[str, object],
    require_read_files: bool,
) -> tuple[bool, list[str]]:
    issues: list[str] = []
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in parsed_content:
            issues.append(f"missing_required_key:{key}")
            continue
        value = parsed_content[key]
        if isinstance(value, str):
            if not value.strip():
                issues.append(f"empty_string_value:{key}")
            else:
                issues.append(f"string_value_not_allowed:{key}")
        elif not isinstance(value, (dict, list)):
            issues.append(f"invalid_value_type:{key}")

    if issues:
        return False, issues

    must_read = parsed_content["must_read_file_map"]
    if isinstance(must_read, dict):
        required_files = must_read.get("required_files")
        optional_files = must_read.get("optional_files")
        if require_read_files and not (required_files or optional_files):
            issues.append("must_read_file_map_missing_files")
    else:
        issues.append("must_read_file_map_not_object")

    risk_report = parsed_content["risk_and_conflict_report"]
    if isinstance(risk_report, dict):
        if "risks" not in risk_report:
            issues.append("risk_and_conflict_report_missing_risks")
    else:
        issues.append("risk_and_conflict_report_not_object")

    candidate_summary = parsed_content["candidate_summary"]
    if isinstance(candidate_summary, dict):
        summary = candidate_summary.get("summary", "")
        if not isinstance(summary, str) or not summary.strip():
            issues.append("candidate_summary_missing_summary")
    else:
        issues.append("candidate_summary_not_object")

    return (not issues), issues


def infer_related_files(text: str) -> list[str]:
    files = re.findall(r"`([^`]+\.md)`", text)
    ordered_files: list[str] = []
    for file_path in files:
        if file_path not in ordered_files:
            ordered_files.append(file_path)
    return ordered_files


def build_local_fallback_pack(
    *,
    task_prompt: str,
    context_metadata: dict[str, object],
    raw_sources: list[dict[str, object]],
    attempt_logs: list[dict[str, object]],
    final_reason: str,
) -> dict[str, object]:
    source_map = {str(source["label"]): str(source["text"]) for source in raw_sources}
    required_files: list[str] = []
    for entry in context_metadata["context_files"]:
        label = str(entry["path"])
        if label not in required_files:
            required_files.append(label)
    related_files: list[str] = []
    for entry in context_metadata["context_files"]:
        text = source_map.get(str(entry["path"]), "")
        for referenced_file in infer_related_files(text):
            if referenced_file not in related_files and referenced_file not in required_files:
                related_files.append(referenced_file)
    risks: list[str] = []
    conflicts: list[str] = []
    for label, text in source_map.items():
        if "固定素材锚点" in text or "fixed_material_anchor" in text:
            risks.append(f"{label} 保留了固定素材锚点表述，单独阅读时可能被误解为固定 SOP。")
        if "必须先读" in text and "locked_reference_inheritance_rules" in text:
            risks.append(f"{label} 对 locked reference 的执行闸门很强，可能在脱离 OPC 口径时被读成固定流程。")
        if "不锁死每条内容" in text and "固定流程" in text:
            conflicts.append(f"{label} 同时包含反 SOP 口径与历史强约束口径，Codex 下一轮需要做冲突辨析。")
    if not risks:
        risks.append("本地回退未观察到足够证据证明 reference 已被误写为固定 SOP，但需要人工复核相关规则。")
    if not conflicts:
        conflicts.append("本地回退无法替代 DeepSeek 风险归纳，不能把这份 fallback 当成 DeepSeek 结论。")

    prefetch_context_pack = {
        "task": task_prompt,
        "input_files": required_files,
        "context_truncated": context_metadata["context_truncated"],
        "truncated_files": context_metadata["truncated_files"],
        "source_summary": [
            {
                "path": entry["path"],
                "used_chars": entry["used_chars"],
                "truncated": entry["truncated"],
                "headings": entry["headings"][:4],
            }
            for entry in context_metadata["context_files"]
        ],
    }
    must_read_file_map = {
        "required_files": required_files[:4],
        "optional_files": related_files[:4],
        "reason": "DeepSeek 三次尝试后未产出稳定 JSON，当前文件地图来自 Codex 本地回退提取。",
    }
    risk_and_conflict_report = {
        "risks": risks[:4],
        "conflicts": conflicts[:4],
        "blocked_if": [
            "不要把 fallback_local_only 当成 DeepSeek 结论。",
            "不要把 fallback_local_only 写成 multi-agent runtime 已跑通。",
            f"最终失败原因：{final_reason}",
        ],
    }
    candidate_summary = {
        "summary": "DeepSeek 真实任务输出未稳定，当前资料包来自本地回退。",
        "recommended_next_step": "继续收紧输入与输出约束，再重试真实任务。",
        "not_allowed": [
            "不要把 fallback 当成 DeepSeek passed。",
            "不要据此直接改写正式项目事实。",
            "不要写成机制修正已完成。",
        ],
    }
    return {
        "prefetch_context_pack": prefetch_context_pack,
        "must_read_file_map": must_read_file_map,
        "risk_and_conflict_report": risk_and_conflict_report,
        "candidate_summary": candidate_summary,
        "attempt_logs": attempt_logs,
    }


def render_context_pack(
    *,
    timestamp: str,
    base_url: str,
    model: str,
    parsed_content: dict[str, object],
    attempt_logs: list[dict[str, object]],
    context_metadata: dict[str, object],
    api_validation: str,
    deepseek_generation_status: str,
    context_pack_validation: str,
    fallback_status: str,
    validation_status: str,
    fallback_reason: str | None = None,
    env_file_read: bool = False,
    process_env_key_allowed: bool = False,
    process_env_key_present: bool = False,
    api_key_printed: bool = False,
    api_key_written: bool = False,
) -> None:
    pipeline_status = "passed"
    if fallback_status == "used":
        pipeline_status = "usable_with_fallback"
    header_lines = [
        "# DeepSeek readonly explorer latest_prefetch_context_pack",
        "",
        f"- `validation_status`: `{validation_status}`",
        f"- `api_validation`: `{api_validation}`",
        f"- `deepseek_generation_status`: `{deepseek_generation_status}`",
        f"- `context_pack_validation`: `{context_pack_validation}`",
        f"- `fallback_status`: `{fallback_status}`",
        f"- `pipeline_status`: `{pipeline_status}`",
        "- `multi_agent_runtime_validation`: `not_started`",
        f"- `validated_at_utc`: `{timestamp}`",
        f"- `base_url`: `{base_url}`",
        f"- `model`: `{model}`",
        "- `scope`: `readonly_explorer_minimal_api_validation`",
        f"- `env_file_read`: `{str(env_file_read).lower()}`",
        f"- `process_env_key_allowed`: `{str(process_env_key_allowed).lower()}`",
        f"- `process_env_key_present`: `{str(process_env_key_present).lower()}`",
        f"- `api_key_printed`: `{str(api_key_printed).lower()}`",
        f"- `api_key_written`: `{str(api_key_written).lower()}`",
        f"- `context_truncated`: `{'true' if context_metadata['context_truncated'] else 'false'}`",
        f"- `truncated_files`: `{json.dumps(context_metadata['truncated_files'], ensure_ascii=False)}`",
    ]
    if fallback_reason:
        header_lines.append(f"- `fallback_reason`: `{fallback_reason}`")
    header_lines.extend(
        [
            "",
            "## prefetch_context_pack（预读取上下文包）",
            "",
            *json_block(parsed_content["prefetch_context_pack"]),
            "",
            "## must_read_file_map（必读文件地图）",
            "",
            *json_block(parsed_content["must_read_file_map"]),
            "",
            "## risk_and_conflict_report（风险与冲突报告）",
            "",
            *json_block(parsed_content["risk_and_conflict_report"]),
            "",
            "## candidate_summary（候选摘要）",
            "",
            *json_block(parsed_content["candidate_summary"]),
            "",
            "## attempt_log（尝试日志）",
            "",
            *json_block(attempt_logs),
        ]
    )
    write_report(header_lines)


def write_terminal_failure_report(
    *,
    timestamp: str,
    base_url: str,
    model: str,
    api_validation: str,
    error_category: str,
    detail_lines: list[str],
    deepseek_generation_status: str = "failed",
    context_pack_validation: str = "failed_unexpected_output",
    env_file_read: bool = False,
    process_env_key_allowed: bool = False,
    process_env_key_present: bool = False,
    api_key_printed: bool = False,
    api_key_written: bool = False,
) -> None:
    write_report(
        [
            "# DeepSeek readonly explorer latest_prefetch_context_pack",
            "",
            "- `validation_status`: `blocked`",
            f"- `api_validation`: `{api_validation}`",
            f"- `deepseek_generation_status`: `{deepseek_generation_status}`",
            f"- `context_pack_validation`: `{context_pack_validation}`",
            "- `fallback_status`: `not_used`",
            "- `pipeline_status`: `blocked`",
            "- `multi_agent_runtime_validation`: `not_started`",
            f"- `validated_at_utc`: `{timestamp}`",
            f"- `base_url`: `{base_url}`",
            f"- `model`: `{model}`",
            "- `scope`: `readonly_explorer_minimal_api_validation`",
            f"- `env_file_read`: `{str(env_file_read).lower()}`",
            f"- `process_env_key_allowed`: `{str(process_env_key_allowed).lower()}`",
            f"- `process_env_key_present`: `{str(process_env_key_present).lower()}`",
            f"- `api_key_printed`: `{str(api_key_printed).lower()}`",
            f"- `api_key_written`: `{str(api_key_written).lower()}`",
            f"- `error_category`: `{error_category}`",
            "",
            *detail_lines,
        ]
    )


def build_request_payload(
    *,
    model: str,
    task_prompt: str,
    context_bundle: str,
    plan: dict[str, object],
) -> dict[str, object]:
    user_prompt = build_user_prompt(
        task_prompt=task_prompt,
        context_bundle=context_bundle,
        plan=plan,
    )
    return {
        "model": model,
        "temperature": 0,
        "max_tokens": 1200,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are DeepSeek readonly explorer for the 视频工厂 project. "
                    "You are read-only. You cannot write files. "
                    "You cannot decide project facts. "
                    "You only produce a JSON object for Codex integrator. "
                    "Your output must be valid JSON. "
                    "Do not output Markdown. "
                    "Do not output explanations outside JSON. "
                    "The JSON object must contain exactly these top-level keys: "
                    "prefetch_context_pack, must_read_file_map, "
                    "risk_and_conflict_report, candidate_summary."
                ),
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    }


def execute_request(
    *,
    api_key: str,
    base_url: str,
    payload: dict[str, object],
) -> tuple[dict[str, object] | None, str | None, dict[str, object]]:
    url = f"{base_url.rstrip('/')}/chat/completions"
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            body = json.loads(response.read().decode("utf-8"))
        return body, None, {"api_reached": True}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        error_category, retryable = classify_http_error(exc, detail)
        return None, error_category, {"detail": detail[:1500], "retryable": retryable, "api_reached": False}
    except Exception as exc:  # noqa: BLE001
        error_category = classify_runtime_error(exc)
        return None, error_category, {"detail": str(exc), "retryable": error_category in RETRYABLE_FAILURES, "api_reached": False}


def try_generate_context_pack(
    *,
    api_key: str,
    base_url: str,
    model: str,
    task_prompt: str,
    sources: list[dict[str, object]],
) -> tuple[dict[str, object] | None, list[dict[str, object]], dict[str, object], str]:
    api_validation = "failed"
    attempt_logs: list[dict[str, object]] = []
    final_context_metadata: dict[str, object] = {
        "context_truncated": False,
        "truncated_files": [],
        "context_files": [],
    }

    for attempt_index, plan in enumerate(RETRY_PLANS, start=1):
        context_bundle, context_metadata = build_context_bundle(sources, task_prompt, plan)
        final_context_metadata = context_metadata
        payload = build_request_payload(
            model=model,
            task_prompt=task_prompt,
            context_bundle=context_bundle,
            plan=plan,
        )
        prompt_size_chars = len(json.dumps(payload, ensure_ascii=False))
        body, failure_reason, request_meta = execute_request(
            api_key=api_key,
            base_url=base_url,
            payload=payload,
        )
        attempt_log = {
            "attempt_index": attempt_index,
            "mode": plan["mode"],
            "prompt_size_chars": prompt_size_chars,
            "context_size_chars": context_metadata["context_size_chars"],
            "failure_reason": failure_reason or "none",
            "finish_reason": None,
        }
        if request_meta.get("api_reached"):
            api_validation = "passed"

        if body is None:
            attempt_logs.append(attempt_log)
            if request_meta.get("retryable"):
                continue
            attempt_log["detail"] = request_meta.get("detail", "")
            return None, attempt_logs, final_context_metadata, api_validation

        try:
            choice = body["choices"][0]
            content = (choice["message"].get("content") or "").strip()
            finish_reason = choice.get("finish_reason")
            attempt_log["finish_reason"] = finish_reason
        except Exception as exc:  # noqa: BLE001
            attempt_log["failure_reason"] = "unexpected_response_shape"
            attempt_log["detail"] = type(exc).__name__
            attempt_logs.append(attempt_log)
            return None, attempt_logs, final_context_metadata, api_validation

        if not content:
            attempt_log["failure_reason"] = "empty_content"
            attempt_logs.append(attempt_log)
            continue

        if finish_reason == "length":
            attempt_log["failure_reason"] = "finish_reason_length"
            attempt_logs.append(attempt_log)
            continue

        try:
            parsed_content = json.loads(content)
        except json.JSONDecodeError as exc:
            attempt_log["failure_reason"] = "json_parse_error"
            attempt_log["detail"] = str(exc)
            attempt_logs.append(attempt_log)
            continue

        if not isinstance(parsed_content, dict):
            attempt_log["failure_reason"] = "schema_validation_failed"
            attempt_log["detail"] = "top_level_not_object"
            attempt_logs.append(attempt_log)
            continue

        valid, schema_issues = validate_context_pack_schema(
            parsed_content,
            require_read_files=bool(sources),
        )
        if not valid:
            if any(issue.startswith("missing_required_key:") for issue in schema_issues):
                attempt_log["failure_reason"] = "missing_required_keys"
            else:
                attempt_log["failure_reason"] = "schema_validation_failed"
            attempt_log["detail"] = schema_issues
            attempt_logs.append(attempt_log)
            continue

        attempt_log["failure_reason"] = "none"
        attempt_logs.append(attempt_log)
        generation_status = "passed" if attempt_index == 1 else "passed_with_retries"
        return (
            {
                "parsed_content": parsed_content,
                "generation_status": generation_status,
            },
            attempt_logs,
            final_context_metadata,
            api_validation,
        )

    return None, attempt_logs, final_context_metadata, api_validation


def main() -> int:
    args = parse_args(sys.argv[1:])
    disable_env_file = args.no_env_file or os.environ.get("DEEPSEEK_DISABLE_ENV_FILE") == "1"
    process_env_key_allowed = disable_env_file or os.environ.get("DEEPSEEK_ALLOW_PROCESS_ENV_KEY") == "1"
    env = {} if disable_env_file else load_env(ENV_PATH)
    process_api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    api_key = process_api_key or env.get("DEEPSEEK_API_KEY", "")
    base_url = os.environ.get("DEEPSEEK_BASE_URL") or env.get("DEEPSEEK_BASE_URL", DEFAULT_BASE_URL)
    model = os.environ.get("DEEPSEEK_MODEL") or env.get("DEEPSEEK_MODEL", DEFAULT_MODEL)
    env_file_read = bool(not disable_env_file and ENV_PATH.exists())
    process_env_key_present = bool(process_api_key)
    timestamp = datetime.now(timezone.utc).isoformat()

    if not api_key:
        if disable_env_file:
            write_terminal_failure_report(
                timestamp=timestamp,
                base_url=base_url,
                model=model,
                api_validation="blocked_missing_process_env_api_key",
                error_category="missing_process_env_api_key",
                deepseek_generation_status="not_tested_missing_process_env_key",
                context_pack_validation="blocked_missing_process_env_api_key",
                env_file_read=env_file_read,
                process_env_key_allowed=process_env_key_allowed,
                process_env_key_present=process_env_key_present,
                detail_lines=[
                    "## error_detail",
                    "",
                    "process environment 中未检测到 `DEEPSEEK_API_KEY`；安全模式禁止读取 `.env` 补救。",
                ],
            )
            return 2
        write_terminal_failure_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            api_validation="blocked_missing_api_key",
            error_category="missing_api_key",
            env_file_read=env_file_read,
            process_env_key_allowed=process_env_key_allowed,
            process_env_key_present=process_env_key_present,
            detail_lines=[
                "## error_detail",
                "",
                "`.env` 中未检测到 `DEEPSEEK_API_KEY`，因此未执行真实 API 调用。",
            ],
        )
        return 2

    try:
        context_paths = resolve_context_paths(args.context_file)
        sources = read_context_sources(context_paths)
    except Exception as exc:  # noqa: BLE001
        write_terminal_failure_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            api_validation="failed",
            error_category="context_load_error",
            env_file_read=env_file_read,
            process_env_key_allowed=process_env_key_allowed,
            process_env_key_present=process_env_key_present,
            detail_lines=[
                "## error_detail",
                "",
                f"- `error_type`: `{type(exc).__name__}`",
                f"- `error_message`: `{exc}`",
            ],
        )
        return 11

    task_prompt = args.task or (
        "Provide a tiny readonly smoke-test response for the 视频工厂 project. "
        "Keep it brief and avoid inventing unverified project facts."
    )
    result, attempt_logs, context_metadata, api_validation = try_generate_context_pack(
        api_key=api_key,
        base_url=base_url,
        model=model,
        task_prompt=task_prompt,
        sources=sources,
    )

    if result is not None:
        render_context_pack(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            parsed_content=result["parsed_content"],
            attempt_logs=attempt_logs,
            context_metadata=context_metadata,
            api_validation=api_validation,
            deepseek_generation_status=result["generation_status"],
            context_pack_validation="passed",
            fallback_status="not_used",
            validation_status="passed",
            env_file_read=env_file_read,
            process_env_key_allowed=process_env_key_allowed,
            process_env_key_present=process_env_key_present,
        )
        return 0

    non_retryable_failures = {
        log["failure_reason"]
        for log in attempt_logs
        if log["failure_reason"] not in RETRYABLE_FAILURES and log["failure_reason"] != "none"
    }
    if non_retryable_failures:
        write_terminal_failure_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            api_validation=api_validation,
            error_category=sorted(non_retryable_failures)[0],
            env_file_read=env_file_read,
            process_env_key_allowed=process_env_key_allowed,
            process_env_key_present=process_env_key_present,
            detail_lines=[
                "## attempt_log（尝试日志）",
                "",
                *json_block(attempt_logs),
            ],
        )
        return 12

    final_reason = attempt_logs[-1]["failure_reason"] if attempt_logs else "unknown_failure"
    fallback_pack = build_local_fallback_pack(
        task_prompt=task_prompt,
        context_metadata=context_metadata,
        raw_sources=sources,
        attempt_logs=attempt_logs,
        final_reason=final_reason,
    )
    render_context_pack(
        timestamp=timestamp,
        base_url=base_url,
        model=model,
        parsed_content=fallback_pack,
        attempt_logs=attempt_logs,
        context_metadata=context_metadata,
        api_validation=api_validation,
        deepseek_generation_status="failed",
        context_pack_validation="fallback_local_only",
        fallback_status="used",
        validation_status="fallback",
        fallback_reason=final_reason,
        env_file_read=env_file_read,
        process_env_key_allowed=process_env_key_allowed,
        process_env_key_present=process_env_key_present,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
