#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/fan/Documents/视频工厂").resolve()

CANDIDATES = [
    ROOT / ".env",
    ROOT / ".env.local",
    Path.home() / ".zshrc",
    Path.home() / ".zprofile",
    Path.home() / ".bashrc",
    Path.home() / ".bash_profile",
]

KEY_PATTERN = re.compile(r"^\s*(?:export\s+)?DEEPSEEK_API_KEY\s*=\s*(.*)\s*$")


def parse_value(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith(("'", '"')) and raw.endswith(("'", '"')) and len(raw) >= 2:
        raw = raw[1:-1]
    return raw.strip()


def load_key() -> tuple[str | None, str | None]:
    if os.environ.get("DEEPSEEK_API_KEY"):
        return os.environ["DEEPSEEK_API_KEY"], "process_environment"

    for path in CANDIDATES:
        if not path.exists() or not path.is_file():
            continue
        try:
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                match = KEY_PATTERN.match(line)
                if match:
                    value = parse_value(match.group(1))
                    if value:
                        return value, path.name
        except Exception:
            continue
    return None, None


def redact_tail(text: str, key: str | None) -> str:
    tail = text[-600:]
    if key:
        tail = tail.replace(key, "[REDACTED_DEEPSEEK_API_KEY]")
    return tail


def main() -> int:
    key, source = load_key()
    print("DEEPSEEK_API_KEY_PRESENT=", bool(key))
    print("DEEPSEEK_API_KEY_SOURCE=", source or "missing")
    print("API_KEY_VALUE_PRINTED= false")
    print("ENV_FILE_VALUE_WRITTEN= false")

    if not key:
        print("BLOCKED_REASON= missing_deepseek_api_key_in_allowed_sources")
        return 2

    env = os.environ.copy()
    env["DEEPSEEK_API_KEY"] = key
    env["DEEPSEEK_ALLOW_PROCESS_ENV_KEY"] = "1"
    env["DEEPSEEK_DISABLE_ENV_FILE"] = "1"

    request_path = ROOT / "dist/deepseek_supply_controller/deepseek_live_participation_smoke_test_request.json"
    output_dir = ROOT / "dist/deepseek_supply_controller/live_smoke_test_20260515"

    cmd = [
        sys.executable,
        "scripts/deepseek_supply_controller.py",
        "--request-file",
        str(request_path.relative_to(ROOT)),
        "--allow-process-env-api-key",
        "--output-dir",
        str(output_dir.relative_to(ROOT)),
    ]

    result = subprocess.run(
        cmd,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    print("CONTROLLER_RETURN_CODE=", result.returncode)
    print("STDOUT_TAIL=", redact_tail(result.stdout, key))
    print("STDERR_TAIL=", redact_tail(result.stderr, key))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
