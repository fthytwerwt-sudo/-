#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from DeepSeek运行时供应商_deepseek_runtime_provider import (
    build_child_env,
    load_runtime,
    redact_sensitive,
)


ROOT = Path(__file__).resolve().parent.parent
CONTROLLER_SCRIPT = ROOT / "scripts" / "deepseek_supply_controller.py"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run DeepSeek supply controller in process-env-only safe mode."
    )
    parser.add_argument("--request-file", required=True, help="JSON supply request task card.")
    parser.add_argument("--output-dir", help="Optional controller output directory.")
    return parser.parse_args(argv)


def relative_or_raw(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    args = parse_args(sys.argv[1:])
    request_path = Path(args.request_file)
    if not request_path.is_absolute():
        request_path = ROOT / request_path
    request_path = request_path.resolve()

    command = [
        sys.executable,
        str(CONTROLLER_SCRIPT),
        "--request-file",
        relative_or_raw(request_path),
        "--allow-process-env-api-key",
    ]
    if args.output_dir:
        command.extend(["--output-dir", args.output_dir])

    runtime = load_runtime()
    if runtime.status != "ready":
        report = {
            "runner": relative_or_raw(Path(__file__).resolve()),
            "request_file": relative_or_raw(request_path),
            "controller_returncode": 2,
            "safe_call_mode": "project_runtime_provider",
            "runtime_provider": runtime.public_status(),
            "runtime_setup_required": True,
            "env_file_read": False,
            "process_env_key_allowed": True,
            "process_env_key_present": False,
            "api_key_printed": False,
            "api_key_written": False,
            "stdout_tail": "",
            "stderr_tail": "runtime_setup_required",
        }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 2
    env = build_child_env(runtime, os.environ.copy())
    process_env_key_present = bool(env.get("DEEPSEEK_API_KEY"))

    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    report = {
        "runner": relative_or_raw(Path(__file__).resolve()),
        "request_file": relative_or_raw(request_path),
        "controller_returncode": result.returncode,
        "safe_call_mode": "project_runtime_provider",
        "runtime_provider": runtime.public_status(),
        "env_file_read": False,
        "process_env_key_allowed": True,
        "process_env_key_present": process_env_key_present,
        "api_key_printed": False,
        "api_key_written": False,
        "stdout_tail": redact_sensitive(result.stdout[-800:], runtime),
        "stderr_tail": redact_sensitive(result.stderr[-800:], runtime),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
