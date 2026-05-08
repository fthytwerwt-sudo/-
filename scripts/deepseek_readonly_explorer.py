#!/usr/bin/env python3
from __future__ import annotations

import json
import os
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
    payload = {
        "model": model,
        "temperature": 0,
        "max_tokens": 300,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a readonly explorer for the 视频工厂 project. "
                    "Return compact markdown only. Do not claim write access. "
                    "Output exactly three sections: prefetch_context_pack, must_read_file_map, risk_and_conflict_report."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Provide a tiny readonly smoke-test response for the 视频工厂 project. "
                    "Keep it brief and avoid inventing unverified project facts."
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
        content = body["choices"][0]["message"]["content"].strip()
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

    write_report(
        [
            "# DeepSeek readonly explorer latest_prefetch_context_pack",
            "",
            "- `validation_status`: `passed`",
            f"- `validated_at_utc`: `{timestamp}`",
            f"- `base_url`: `{base_url}`",
            f"- `model`: `{model}`",
            "- `scope`: `readonly_explorer_minimal_api_validation`",
            "- `note`: `This proves only the readonly explorer API call path. It does not prove multi-agent runtime.`",
            "",
            content,
        ]
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
