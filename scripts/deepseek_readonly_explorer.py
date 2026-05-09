#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT / ".env"
OUTPUT_PATH = ROOT / "dist" / "deepseek_readonly_explorer" / "latest_prefetch_context_pack.md"
DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-pro"
REQUIRED_TOP_LEVEL_KEYS = [
    "prefetch_context_pack",
    "must_read_file_map",
    "risk_and_conflict_report",
    "candidate_summary",
]


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


def json_block(value: object) -> list[str]:
    return [
        "```json",
        json.dumps(value, ensure_ascii=False, indent=2),
        "```",
    ]


def write_failed_report(
    *,
    timestamp: str,
    base_url: str,
    model: str,
    error_category: str,
    detail_lines: list[str],
) -> None:
    write_report(
        [
            "# DeepSeek readonly explorer latest_prefetch_context_pack",
            "",
            "- `validation_status`: `failed`",
            "- `context_pack_validation`: `failed_unexpected_output`",
            f"- `validated_at_utc`: `{timestamp}`",
            f"- `base_url`: `{base_url}`",
            f"- `model`: `{model}`",
            "- `scope`: `readonly_explorer_minimal_api_validation`",
            f"- `error_category`: `{error_category}`",
            "",
            *detail_lines,
        ]
    )


def render_context_pack(
    *,
    timestamp: str,
    base_url: str,
    model: str,
    parsed_content: dict[str, object],
) -> None:
    write_report(
        [
            "# DeepSeek readonly explorer latest_prefetch_context_pack",
            "",
            "- `validation_status`: `passed`",
            "- `context_pack_validation`: `passed`",
            f"- `validated_at_utc`: `{timestamp}`",
            f"- `base_url`: `{base_url}`",
            f"- `model`: `{model}`",
            "- `scope`: `readonly_explorer_minimal_api_validation`",
            "- `note`: `This proves only the readonly explorer API call path and context-pack shape. It does not prove multi-agent runtime.`",
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
        ]
    )


def main() -> int:
    env = load_env(ENV_PATH)
    api_key = env.get("DEEPSEEK_API_KEY", "")
    base_url = env.get("DEEPSEEK_BASE_URL", DEFAULT_BASE_URL)
    model = env.get("DEEPSEEK_MODEL", DEFAULT_MODEL)
    timestamp = datetime.now(timezone.utc).isoformat()

    if not api_key:
        write_report(
            [
                "# DeepSeek readonly explorer latest_prefetch_context_pack",
                "",
                "- `validation_status`: `blocked_missing_api_key`",
                f"- `validated_at_utc`: `{timestamp}`",
                f"- `base_url`: `{base_url}`",
                f"- `model`: `{model}`",
                "- `reason`: `.env` 中未检测到 `DEEPSEEK_API_KEY`，因此未执行真实 API 调用。",
                "",
                "## next_action",
                "",
                "请先在项目根目录 `.env` 中填写 `DEEPSEEK_API_KEY`，再重新执行最小只读验证。",
            ]
        )
        return 2

    url = f"{base_url.rstrip('/')}/chat/completions"
    json_example = json.dumps(JSON_OUTPUT_EXAMPLE, ensure_ascii=False, indent=2)
    payload = {
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
                "content": (
                    "Return JSON only. Do not include Markdown fences or prose. "
                    "Provide a tiny readonly smoke-test response for the 视频工厂 project. "
                    "Keep it brief and avoid inventing unverified project facts. "
                    "Use this exact JSON shape:\n"
                    f"{json_example}"
                ),
            },
        ],
    }
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
        with urllib.request.urlopen(request, timeout=30) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        write_report(
            [
                "# DeepSeek readonly explorer latest_prefetch_context_pack",
                "",
                "- `validation_status`: `blocked_http_error`",
                f"- `validated_at_utc`: `{timestamp}`",
                f"- `base_url`: `{base_url}`",
                f"- `model`: `{model}`",
                f"- `http_status`: `{exc.code}`",
                "",
                "## error_excerpt",
                "",
                "```text",
                detail[:1500],
                "```",
            ]
        )
        return 3
    except Exception as exc:  # noqa: BLE001
        write_report(
            [
                "# DeepSeek readonly explorer latest_prefetch_context_pack",
                "",
                "- `validation_status`: `blocked_runtime_error`",
                f"- `validated_at_utc`: `{timestamp}`",
                f"- `base_url`: `{base_url}`",
                f"- `model`: `{model}`",
                f"- `error_type`: `{type(exc).__name__}`",
                f"- `error_message`: `{exc}`",
            ]
        )
        return 4

    content = ""
    try:
        choice = body["choices"][0]
        content = (choice["message"].get("content") or "").strip()
        finish_reason = choice.get("finish_reason")
    except Exception as exc:  # noqa: BLE001
        write_report(
            [
                "# DeepSeek readonly explorer latest_prefetch_context_pack",
                "",
                "- `validation_status`: `blocked_unexpected_response_shape`",
                f"- `validated_at_utc`: `{timestamp}`",
                f"- `base_url`: `{base_url}`",
                f"- `model`: `{model}`",
                f"- `error_type`: `{type(exc).__name__}`",
                "",
                "## response_excerpt",
                "",
                "```json",
                json.dumps(body, ensure_ascii=False, indent=2)[:2000],
                "```",
            ]
        )
        return 5

    if not content:
        write_failed_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            error_category="empty_content",
            detail_lines=[
                "## error_detail",
                "",
                "DeepSeek JSON Output 返回空 `content`，本轮未生成有效上下文包。",
            ],
        )
        return 6

    if finish_reason == "length":
        write_failed_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            error_category="truncated_json",
            detail_lines=[
                "## error_detail",
                "",
                "`finish_reason = length`，JSON 可能被截断。",
            ],
        )
        return 7

    try:
        parsed_content = json.loads(content)
    except json.JSONDecodeError as exc:
        write_failed_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            error_category="json_parse_error",
            detail_lines=[
                "## error_detail",
                "",
                f"- `json_error`: `{exc}`",
                "",
                "## content_excerpt",
                "",
                "```text",
                content[:2000],
                "```",
            ],
        )
        return 8

    if not isinstance(parsed_content, dict):
        write_failed_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            error_category="json_not_object",
            detail_lines=[
                "## error_detail",
                "",
                "JSON Output 不是 object，因此不能作为上下文包。",
            ],
        )
        return 9

    missing_keys = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in parsed_content]
    if missing_keys:
        write_failed_report(
            timestamp=timestamp,
            base_url=base_url,
            model=model,
            error_category="missing_required_keys",
            detail_lines=[
                "## missing_required_keys",
                "",
                *[f"- `{key}`" for key in missing_keys],
            ],
        )
        return 10

    render_context_pack(
        timestamp=timestamp,
        base_url=base_url,
        model=model,
        parsed_content=parsed_content,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
