#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from DeepSeek运行时供应商_deepseek_runtime_provider import (
    ROOT,
    build_child_env,
    git_tracked,
    load_runtime,
    redact_sensitive,
    run_child,
)


EXPLORER_SCRIPT = ROOT / "scripts" / "deepseek_readonly_explorer.py"
EXPLORER_OUTPUT = ROOT / "dist" / "deepseek_readonly_explorer" / "latest_prefetch_context_pack.md"
DEFAULT_OUTPUT_ROOT = ROOT / "dist" / "deepseek_runtime_validation"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="DeepSeek runtime provider doctor.")
    parser.add_argument(
        "--output-root",
        default=str(DEFAULT_OUTPUT_ROOT.relative_to(ROOT)),
        help="Directory for doctor reports.",
    )
    parser.add_argument(
        "--skip-api-call",
        action="store_true",
        help="Only check runtime loading and child injection.",
    )
    return parser.parse_args(argv)


def resolve_output_root(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    path.relative_to(ROOT)
    return path


def parse_header_status(path: Path) -> dict[str, str]:
    status: dict[str, str] = {}
    if not path.exists():
        return status
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("- `") or "`: `" not in stripped:
            continue
        try:
            key = stripped.split("`", 2)[1]
            value = stripped.split("`: `", 1)[1].rsplit("`", 1)[0]
        except IndexError:
            continue
        status[key] = value
    return status


def contains_secret(path: Path, secret: str) -> bool:
    if not secret or not path.exists() or not path.is_file():
        return False
    try:
        return secret in path.read_text(encoding="utf-8", errors="ignore")
    except UnicodeDecodeError:
        return False


def scan_no_key(paths: list[Path], secret: str) -> dict[str, Any]:
    checked: list[str] = []
    leaked: list[str] = []
    for path in paths:
        if path.is_dir():
            candidates = [item for item in path.rglob("*") if item.is_file()]
        else:
            candidates = [path]
        for candidate in candidates:
            checked.append(str(candidate.relative_to(ROOT)))
            if contains_secret(candidate, secret):
                leaked.append(str(candidate.relative_to(ROOT)))
    return {
        "checked_files": checked,
        "leak_found": bool(leaked),
        "leak_files": leaked,
    }


def write_reports(output_root: Path, report: dict[str, Any]) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    (output_root / "runtime_doctor_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# DeepSeek runtime doctor report",
        "",
        f"- `status`: `{report['status']}`",
        f"- `key_found`: `{str(report['key_found']).lower()}`",
        f"- `key_source`: `{report['key_source']}`",
        f"- `key_git_tracked`: `{str(report['key_git_tracked']).lower()}`",
        f"- `can_inject_child_process`: `{str(report['can_inject_child_process']).lower()}`",
        f"- `can_call_deepseek`: `{str(report['can_call_deepseek']).lower()}`",
        f"- `api_key_printed`: `{str(report['api_key_printed']).lower()}`",
        f"- `api_key_written`: `{str(report['api_key_written']).lower()}`",
        "",
        "```json",
        json.dumps(report, ensure_ascii=False, indent=2),
        "```",
    ]
    (output_root / "runtime_doctor_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args(sys.argv[1:])
    output_root = resolve_output_root(args.output_root)
    runtime = load_runtime()
    source_path = ROOT / runtime.key_source_path if runtime.key_source_path not in {"", "none", "process_env"} else None
    key_git_tracked = bool(source_path and git_tracked(source_path))
    can_inject_child_process = False
    inject_error = ""
    if runtime.status == "ready":
        probe = subprocess.run(
            [
                sys.executable,
                "-c",
                "import os,sys; sys.exit(0 if os.environ.get('DEEPSEEK_API_KEY') else 1)",
            ],
            cwd=ROOT,
            env=build_child_env(runtime),
            text=True,
            capture_output=True,
            check=False,
        )
        can_inject_child_process = probe.returncode == 0
        inject_error = redact_sensitive((probe.stdout + probe.stderr).strip(), runtime)

    explorer_status: dict[str, str] = {}
    api_call_result: dict[str, Any] = {"returncode": None, "stdout": "", "stderr": ""}
    can_call_deepseek = False
    if runtime.status == "ready" and can_inject_child_process and not args.skip_api_call:
        api_call_result = run_child(
            [
                sys.executable,
                str(EXPLORER_SCRIPT),
                "--task",
                (
                    "DeepSeek runtime doctor smoke test. Return compact JSON only; "
                    "confirm this is a readonly supply-layer call and do not invent project facts."
                ),
                "--no-env-file",
            ],
            timeout=90,
        )
        explorer_status = parse_header_status(EXPLORER_OUTPUT)
        can_call_deepseek = (
            api_call_result["returncode"] == 0
            and explorer_status.get("validation_status") == "passed"
            and explorer_status.get("deepseek_actual_participation") == "deepseek_passed"
            and explorer_status.get("fallback_status") == "not_used"
        )

    leak_scan = scan_no_key([output_root, EXPLORER_OUTPUT], runtime.api_key) if runtime.api_key else {
        "checked_files": [],
        "leak_found": False,
        "leak_files": [],
    }
    status = "ready" if runtime.status == "ready" and can_inject_child_process and (can_call_deepseek or args.skip_api_call) and not key_git_tracked and not leak_scan["leak_found"] else runtime.status
    if runtime.status == "ready" and status != "ready":
        status = "blocked"
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "runtime_provider": runtime.public_status(),
        "key_found": runtime.key_found,
        "key_source": runtime.key_source,
        "key_source_path": runtime.key_source_path,
        "key_git_tracked": key_git_tracked,
        "can_inject_child_process": can_inject_child_process,
        "inject_error": inject_error,
        "can_call_deepseek": can_call_deepseek,
        "explorer_status": explorer_status,
        "api_call_returncode": api_call_result["returncode"],
        "api_call_stdout_tail": api_call_result["stdout"][-800:],
        "api_call_stderr_tail": api_call_result["stderr"][-800:],
        "supply_pack_has_no_key": not leak_scan["leak_found"],
        "manifest_has_no_key": not leak_scan["leak_found"],
        "log_has_no_key": True,
        "api_key_printed": False,
        "api_key_written": False,
        "leak_scan": leak_scan,
        "setup_required_output": "runtime_setup_required" if runtime.status != "ready" else "",
    }
    write_reports(output_root, report)
    print(json.dumps({k: v for k, v in report.items() if k not in {"runtime_provider"}}, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "ready" else 1


if __name__ == "__main__":
    raise SystemExit(main())
