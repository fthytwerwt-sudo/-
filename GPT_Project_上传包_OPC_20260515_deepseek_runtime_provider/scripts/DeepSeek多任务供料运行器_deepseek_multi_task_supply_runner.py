#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from DeepSeek运行时供应商_deepseek_runtime_provider import ROOT, load_runtime, redact_sensitive


SAFE_RUNNER = ROOT / "scripts" / "DeepSeek安全供料运行器_deepseek_safe_supply_runner.py"
DEFAULT_OUTPUT_ROOT = ROOT / "dist" / "deepseek_runtime_validation"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run multiple DeepSeek supply requests.")
    parser.add_argument("--request-file", action="append", required=True, help="Supply request JSON. Repeatable.")
    parser.add_argument(
        "--output-root",
        default=str(DEFAULT_OUTPUT_ROOT.relative_to(ROOT)),
        help="Output root for per-task and combined reports.",
    )
    parser.add_argument(
        "--execution-mode",
        choices=["serial", "bounded_parallel"],
        default="serial",
    )
    parser.add_argument("--max-workers", type=int, default=3)
    parser.add_argument("--require-real", action="store_true", help="Fail if any request does not pass DeepSeek.")
    return parser.parse_args(argv)


def resolve_inside_root(raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    path.relative_to(ROOT)
    return path


def relative_label(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"json_top_level_not_object:{relative_label(path)}")
    return data


def task_output_dir(output_root: Path, request_path: Path) -> Path:
    card = load_json(request_path)
    request_id = str(card.get("request_id") or request_path.stem)
    safe_id = "".join(char if char.isalnum() or char in "-_" else "_" for char in request_id)
    return output_root / safe_id


def run_one(request_path: Path, output_root: Path) -> dict[str, Any]:
    runtime = load_runtime()
    output_dir = task_output_dir(output_root, request_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        str(SAFE_RUNNER),
        "--request-file",
        relative_label(request_path),
        "--output-dir",
        relative_label(output_dir),
    ]
    result = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    stdout = redact_sensitive(result.stdout, runtime)
    stderr = redact_sensitive(result.stderr, runtime)
    pack_path = output_dir / "latest_supply_pack.json"
    manifest_path = output_dir / "latest_supply_manifest.json"
    md_path = output_dir / "latest_supply_pack.md"
    pack: dict[str, Any] = {}
    if pack_path.exists():
        pack = load_json(pack_path)
    manifest: dict[str, Any] = {}
    if manifest_path.exists():
        manifest = load_json(manifest_path)
    participation = pack.get("deepseek_participation_report") or manifest.get("deepseek_participation_report") or {}
    supply_source = str(pack.get("supply_source") or manifest.get("supply_source") or "blocked")
    fallback_status = str(pack.get("fallback_status") or manifest.get("fallback_status") or "unknown")
    blocked_reason = str(pack.get("blocked_reason") or manifest.get("blocked_reason") or "unknown")
    deepseek_actual_participation = str(
        pack.get("deepseek_actual_participation")
        or manifest.get("deepseek_actual_participation")
        or "not_attempted_policy_violation"
    )
    report = {
        "request_file": relative_label(request_path),
        "request_id": str(pack.get("request_id") or manifest.get("request_id") or request_path.stem),
        "runner_returncode": result.returncode,
        "output_dir": relative_label(output_dir),
        "deepseek_actual_participation": deepseek_actual_participation,
        "deepseek_actual_participation_bool": deepseek_actual_participation == "deepseek_passed",
        "supply_source": supply_source,
        "fallback_status": fallback_status,
        "blocked_reason": blocked_reason,
        "supply_pack_exists": md_path.exists() and pack_path.exists(),
        "manifest_exists": manifest_path.exists(),
        "participation_report": participation,
        "stdout_tail": stdout[-800:],
        "stderr_tail": stderr[-800:],
        "files": {
            "latest_supply_pack_md": relative_label(md_path),
            "latest_supply_pack_json": relative_label(pack_path),
            "latest_supply_manifest_json": relative_label(manifest_path),
            "participation_report_json": relative_label(output_dir / "participation_report.json"),
        },
    }
    (output_dir / "participation_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return report


def write_combined(output_root: Path, reports: list[dict[str, Any]], execution_mode: str) -> dict[str, Any]:
    deepseek_passed_count = sum(1 for report in reports if report["supply_source"] == "deepseek_passed")
    fallback_count = sum(1 for report in reports if report["supply_source"] == "fallback_local_only")
    blocked_count = sum(1 for report in reports if report["supply_source"] not in {"deepseek_passed", "fallback_local_only"})
    combined = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "execution_mode": execution_mode,
        "total_requests": len(reports),
        "deepseek_passed_count": deepseek_passed_count,
        "blocked_count": blocked_count,
        "fallback_count": fallback_count,
        "all_outputs_exist": all(
            report["supply_pack_exists"] and report["manifest_exists"] and Path(ROOT / report["files"]["participation_report_json"]).exists()
            for report in reports
        ),
        "per_task_report": reports,
        "completion_rule": {
            "deepseek_passed_count_gte_2": deepseek_passed_count >= 2,
            "fallback_count_eq_0": fallback_count == 0,
            "blocked_count_eq_0": blocked_count == 0,
        },
    }
    output_root.mkdir(parents=True, exist_ok=True)
    json_path = output_root / "latest_combined_participation_report.json"
    md_path = output_root / "latest_combined_participation_report.md"
    json_path.write_text(json.dumps(combined, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# DeepSeek multi-task participation report",
        "",
        f"- `total_requests`: `{combined['total_requests']}`",
        f"- `deepseek_passed_count`: `{combined['deepseek_passed_count']}`",
        f"- `fallback_count`: `{combined['fallback_count']}`",
        f"- `blocked_count`: `{combined['blocked_count']}`",
        f"- `all_outputs_exist`: `{str(combined['all_outputs_exist']).lower()}`",
        "",
        "```json",
        json.dumps(combined, ensure_ascii=False, indent=2),
        "```",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return combined


def main() -> int:
    args = parse_args(sys.argv[1:])
    output_root = resolve_inside_root(args.output_root)
    request_paths = [resolve_inside_root(path) for path in args.request_file]
    reports: list[dict[str, Any]] = []
    if args.execution_mode == "bounded_parallel":
        with ThreadPoolExecutor(max_workers=max(1, min(args.max_workers, len(request_paths)))) as executor:
            future_map = {executor.submit(run_one, path, output_root): path for path in request_paths}
            for future in as_completed(future_map):
                reports.append(future.result())
        order = {relative_label(path): index for index, path in enumerate(request_paths)}
        reports.sort(key=lambda report: order.get(report["request_file"], 999))
    else:
        for request_path in request_paths:
            reports.append(run_one(request_path, output_root))
    combined = write_combined(output_root, reports, args.execution_mode)
    print(json.dumps(combined, ensure_ascii=False, indent=2))
    if args.require_real and (
        combined["fallback_count"] > 0 or combined["blocked_count"] > 0 or combined["deepseek_passed_count"] != combined["total_requests"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
