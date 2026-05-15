#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
LOCAL_RUNTIME_DIR = ROOT / "本地运行配置_local_runtime"
LOCAL_AUTH_PATH = LOCAL_RUNTIME_DIR / "deepseek_runtime_authorization.local.json"
PROJECT_ENV_LOCAL = ROOT / ".env.local"
PROJECT_ENV = ROOT / ".env"
ALLOWED_KEY_NAME = "DEEPSEEK_API_KEY"
DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-v4-flash"
DEFAULT_ESCALATION_MODEL = "deepseek-v4-pro"
KEY_PATTERN = re.compile(r"sk-[A-Za-z0-9_\-]{8,}")


@dataclass
class RuntimeCredential:
    status: str
    key_found: bool
    key_source: str
    key_source_path: str
    api_key: str
    base_url: str
    model: str
    escalation_model: str
    setup_required_reason: str
    load_attempts: list[dict[str, str]]

    def public_status(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "key_found": self.key_found,
            "key_source": self.key_source,
            "key_source_path": self.key_source_path,
            "auto_load_enabled": True,
            "allowed_key_name": [ALLOWED_KEY_NAME],
            "never_print_key": True,
            "never_write_key": True,
            "inject_to_child_process_only": True,
            "redact_stdout_stderr": True,
            "base_url": self.base_url,
            "model": self.model,
            "escalation_model": self.escalation_model,
            "setup_required_reason": self.setup_required_reason,
            "load_order": [
                "process_env",
                "project_env_local",
                "project_env",
                "local_runtime_authorization",
            ],
            "load_attempts": self.load_attempts,
        }


def relative_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, raw_value = stripped.split("=", 1)
        value = raw_value.strip().strip("'").strip('"')
        values[key.strip()] = value
    return values


def parse_local_authorization(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("local_runtime_authorization_top_level_not_object")
    result: dict[str, str] = {}
    for key in (ALLOWED_KEY_NAME, "DEEPSEEK_BASE_URL", "DEEPSEEK_MODEL", "DEEPSEEK_ESCALATION_MODEL"):
        value = data.get(key)
        if isinstance(value, str):
            result[key] = value.strip()
    deepseek = data.get("deepseek")
    if isinstance(deepseek, dict):
        nested_key = deepseek.get(ALLOWED_KEY_NAME)
        if isinstance(nested_key, str) and nested_key.strip():
            result[ALLOWED_KEY_NAME] = nested_key.strip()
    return result


def source_candidates() -> list[tuple[str, Path | None, dict[str, str]]]:
    return [
        ("process_env", None, dict(os.environ)),
        ("project_env_local", PROJECT_ENV_LOCAL, parse_env_file(PROJECT_ENV_LOCAL)),
        ("project_env", PROJECT_ENV, parse_env_file(PROJECT_ENV)),
        ("local_runtime_authorization", LOCAL_AUTH_PATH, parse_local_authorization(LOCAL_AUTH_PATH)),
    ]


def load_runtime() -> RuntimeCredential:
    attempts: list[dict[str, str]] = []
    selected_source = ""
    selected_path = ""
    selected_values: dict[str, str] = {}
    api_key = ""
    for source_name, source_path, values in source_candidates():
        key_value = values.get(ALLOWED_KEY_NAME, "").strip()
        exists = "true" if source_path is None or source_path.exists() else "false"
        attempts.append(
            {
                "source": source_name,
                "path": "process_env" if source_path is None else relative_label(source_path),
                "exists": exists,
                "key_field_present": "true" if ALLOWED_KEY_NAME in values else "false",
                "key_nonempty": "true" if bool(key_value) else "false",
            }
        )
        if key_value:
            selected_source = source_name
            selected_path = "process_env" if source_path is None else relative_label(source_path)
            selected_values = values
            api_key = key_value
            break

    if not api_key:
        return RuntimeCredential(
            status="setup_required",
            key_found=False,
            key_source="none",
            key_source_path="none",
            api_key="",
            base_url=os.environ.get("DEEPSEEK_BASE_URL", DEFAULT_BASE_URL),
            model=os.environ.get("DEEPSEEK_MODEL", DEFAULT_MODEL),
            escalation_model=os.environ.get("DEEPSEEK_ESCALATION_MODEL", DEFAULT_ESCALATION_MODEL),
            setup_required_reason="runtime_setup_required_missing_deepseek_api_key",
            load_attempts=attempts,
        )

    return RuntimeCredential(
        status="ready",
        key_found=True,
        key_source=selected_source,
        key_source_path=selected_path,
        api_key=api_key,
        base_url=selected_values.get("DEEPSEEK_BASE_URL")
        or os.environ.get("DEEPSEEK_BASE_URL")
        or DEFAULT_BASE_URL,
        model=selected_values.get("DEEPSEEK_MODEL")
        or os.environ.get("DEEPSEEK_MODEL")
        or DEFAULT_MODEL,
        escalation_model=selected_values.get("DEEPSEEK_ESCALATION_MODEL")
        or os.environ.get("DEEPSEEK_ESCALATION_MODEL")
        or DEFAULT_ESCALATION_MODEL,
        setup_required_reason="",
        load_attempts=attempts,
    )


def build_child_env(runtime: RuntimeCredential, base_env: dict[str, str] | None = None) -> dict[str, str]:
    if runtime.status != "ready" or not runtime.api_key:
        raise RuntimeError(runtime.setup_required_reason or "deepseek_runtime_provider_not_ready")
    env = dict(base_env or os.environ)
    env[ALLOWED_KEY_NAME] = runtime.api_key
    env["DEEPSEEK_BASE_URL"] = runtime.base_url
    env["DEEPSEEK_MODEL"] = runtime.model
    env["DEEPSEEK_ESCALATION_MODEL"] = runtime.escalation_model
    env["DEEPSEEK_ALLOW_PROCESS_ENV_KEY"] = "1"
    env["DEEPSEEK_DISABLE_ENV_FILE"] = "1"
    env["DEEPSEEK_RUNTIME_PROVIDER_STATUS"] = "ready"
    env["DEEPSEEK_RUNTIME_AUTO_LOAD_ENABLED"] = "1"
    env["DEEPSEEK_RUNTIME_KEY_SOURCE"] = runtime.key_source
    env["DEEPSEEK_RUNTIME_KEY_SOURCE_PATH"] = runtime.key_source_path
    env["DEEPSEEK_RUNTIME_PROVIDER_VERSION"] = "20260515"
    return env


def redact_sensitive(text: str, runtime: RuntimeCredential | None = None) -> str:
    redacted = text
    if runtime and runtime.api_key:
        redacted = redacted.replace(runtime.api_key, "[REDACTED_DEEPSEEK_API_KEY]")
    return KEY_PATTERN.sub("[REDACTED_API_KEY]", redacted)


def run_child(
    command: list[str],
    *,
    cwd: Path = ROOT,
    timeout: int | None = None,
) -> dict[str, Any]:
    runtime = load_runtime()
    if runtime.status != "ready":
        return {
            "returncode": 2,
            "runtime_provider": runtime.public_status(),
            "stdout": "",
            "stderr": "runtime_setup_required",
        }
    result = subprocess.run(
        command,
        cwd=cwd,
        env=build_child_env(runtime),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    return {
        "returncode": result.returncode,
        "runtime_provider": runtime.public_status(),
        "stdout": redact_sensitive(result.stdout, runtime),
        "stderr": redact_sensitive(result.stderr, runtime),
    }


def git_tracked(path: Path) -> bool:
    try:
        path.relative_to(ROOT)
    except ValueError:
        return False
    result = subprocess.run(
        ["git", "ls-files", "--error-unmatch", relative_label(path)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    return result.returncode == 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="DeepSeek project runtime provider.")
    subparsers = parser.add_subparsers(dest="command_name")
    subparsers.add_parser("status", help="Print redacted runtime status.")
    run_parser = subparsers.add_parser("run", help="Run a child command with runtime env injected.")
    run_parser.add_argument("child_command", nargs=argparse.REMAINDER)
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args(sys.argv[1:])
    if args.command_name in {None, "status"}:
        runtime = load_runtime()
        print(json.dumps(runtime.public_status(), ensure_ascii=False, indent=2))
        return 0 if runtime.status == "ready" else 2
    if args.command_name == "run":
        command = list(args.child_command)
        if command and command[0] == "--":
            command = command[1:]
        if not command:
            print(json.dumps({"status": "blocked", "reason": "missing_child_command"}, ensure_ascii=False))
            return 2
        result = run_child(command)
        print(
            json.dumps(
                {
                    "returncode": result["returncode"],
                    "runtime_provider": result["runtime_provider"],
                    "stdout_tail": result["stdout"][-1200:],
                    "stderr_tail": result["stderr"][-1200:],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return int(result["returncode"])
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
