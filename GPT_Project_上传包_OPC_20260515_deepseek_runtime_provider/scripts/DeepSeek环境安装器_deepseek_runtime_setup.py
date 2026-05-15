#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from DeepSeek运行时供应商_deepseek_runtime_provider import LOCAL_AUTH_PATH, LOCAL_RUNTIME_DIR, ROOT, load_runtime


EXAMPLE_PATH = LOCAL_RUNTIME_DIR / "deepseek_runtime_authorization.example.json"
README_PATH = LOCAL_RUNTIME_DIR / "DeepSeek运行时授权说明_DEEPSEEK_RUNTIME_AUTH.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare local DeepSeek runtime config files.")
    parser.add_argument("--create-local-placeholder", action="store_true")
    return parser.parse_args()


def relative_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args()
    LOCAL_RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    if not EXAMPLE_PATH.exists():
        EXAMPLE_PATH.write_text(
            json.dumps(
                {
                    "DEEPSEEK_API_KEY": "replace_with_your_deepseek_api_key",
                    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
                    "DEEPSEEK_MODEL": "deepseek-v4-flash",
                    "DEEPSEEK_ESCALATION_MODEL": "deepseek-v4-pro",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    if args.create_local_placeholder and not LOCAL_AUTH_PATH.exists():
        LOCAL_AUTH_PATH.write_text(
            json.dumps(
                {
                    "DEEPSEEK_API_KEY": "replace_with_real_key_once_locally_do_not_commit",
                    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
                    "DEEPSEEK_MODEL": "deepseek-v4-flash",
                    "DEEPSEEK_ESCALATION_MODEL": "deepseek-v4-pro",
                },
                ensure_ascii=False,
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
    runtime = load_runtime()
    print(
        json.dumps(
            {
                "status": runtime.status,
                "runtime_dir": relative_label(LOCAL_RUNTIME_DIR),
                "example_path": relative_label(EXAMPLE_PATH),
                "readme_path": relative_label(README_PATH),
                "local_authorization_path": relative_label(LOCAL_AUTH_PATH),
                "local_authorization_exists": LOCAL_AUTH_PATH.exists(),
                "key_found": runtime.key_found,
                "key_source": runtime.key_source,
                "setup_required_output": "runtime_setup_required" if runtime.status != "ready" else "",
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0 if runtime.status == "ready" else 2


if __name__ == "__main__":
    raise SystemExit(main())
