#!/usr/bin/env python3
"""Offline vector-sync dry run for the Video Factory RAG Router design branch.

This script only simulates what a future vector sync would do. It does not call
external APIs, generate embeddings, create collections, or write to a vector DB.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path("/Users/fan/Documents/视频工厂").resolve()
REPO_FULL_NAME = "fthytwerwt-sudo/-"
PROJECT_ROUTE = "video_factory"
EXPECTED_BRANCH = "feature/vector-rag-router-design-20260611"

OUTPUT_DIR = ROOT / "codex_log/vector_rag_router_design/vector_sync_dry_run"
PLAN_PATH = OUTPUT_DIR / "20260611_vector_sync_dry_run_plan.json"
SUMMARY_PATH = OUTPUT_DIR / "20260611_vector_sync_dry_run_summary.md"

TEXT_EXTENSIONS = {".md", ".json", ".py"}
MEDIA_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".wav",
    ".mp3",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".psd",
    ".zip",
}
SECRET_PATH_SIGNALS = ("secret", "token", "credential", "authorization.local")
REQUIRED_CHUNK_FIELDS = [
    "repo_full_name",
    "project_route",
    "branch",
    "commit_sha",
    "source_path",
    "heading_path",
    "content_hash",
    "authority_level",
    "status_label",
    "updated_at",
    "conflict_tags",
    "do_not_use_for_completion_claim",
]
CANONICAL_CURRENT_PATHS = {
    "AGENTS.md",
    "GPT数据源/08_当前正式事实.md",
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/21_codex_judgment_permission_matrix.md",
    "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
}
ALLOWED_DIST_REVIEW_PACK = {
    "dist/latest_review_pack/summary.json",
    "dist/latest_review_pack/review_manifest.md",
    "dist/latest_review_pack/visual_route_map.json",
    "dist/latest_review_pack/visual_route_validation_report.json",
}


def run_git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {completed.stderr.strip()}")
    return completed.stdout


def ensure_repo_guard() -> dict[str, Any]:
    cwd = Path.cwd().resolve()
    if not cwd.is_relative_to(ROOT):
        raise RuntimeError(f"cwd must be under {ROOT}, got {cwd}")

    branch = run_git(["branch", "--show-current"]).strip()
    remotes = run_git(["remote", "-v"])
    remote_ok = "fthytwerwt-sudo/-" in remotes
    branch_ok = branch == EXPECTED_BRANCH
    root_ok = cwd == ROOT

    guard = {
        "cwd": str(cwd),
        "expected_cwd": str(ROOT),
        "cwd_is_expected_root": root_ok,
        "cwd_under_expected_root": True,
        "branch": branch,
        "branch_ok": branch_ok,
        "remote_ok": remote_ok,
        "expected_remote": REPO_FULL_NAME,
    }
    if not root_ok:
        raise RuntimeError(f"cwd must be exactly {ROOT}, got {cwd}")
    if not remote_ok:
        raise RuntimeError(f"remote must contain {REPO_FULL_NAME}")
    if not branch_ok:
        raise RuntimeError(f"branch must be {EXPECTED_BRANCH}, got {branch}")
    return guard


def parse_name_status(diff_text: str) -> list[dict[str, str | None]]:
    changed: list[dict[str, str | None]] = []
    for line in diff_text.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        old_path: str | None = None
        path: str | None = None
        if status.startswith(("R", "C")) and len(parts) >= 3:
            old_path = parts[1]
            path = parts[2]
        elif len(parts) >= 2:
            path = parts[1]
        else:
            path = None
        if path:
            changed.append({"status": status, "path": path, "old_path": old_path})
    return changed


def is_secret_path(path: str) -> bool:
    lower = path.lower()
    parts = Path(path).parts
    if any(part in {".env", ".env.local"} or part.startswith(".env.") for part in parts):
        return True
    return any(signal in lower for signal in SECRET_PATH_SIGNALS)


def is_media_path(path: str) -> bool:
    return Path(path).suffix.lower() in MEDIA_EXTENSIONS


def is_allowed_dist_path(path: str) -> bool:
    return path in ALLOWED_DIST_REVIEW_PACK


def is_blacklisted_path(path: str) -> bool:
    if path.startswith("public/"):
        return True
    if path.startswith("dist/") and not is_allowed_dist_path(path):
        return True
    if path.startswith("review_loop/screenshots/") and Path(path).suffix.lower() == ".png":
        return True
    if "/samples/" in path and Path(path).suffix.lower() in {".mp3", ".wav"}:
        return True
    return False


def is_readable_text_candidate(path: str) -> bool:
    if is_secret_path(path) or is_media_path(path) or is_blacklisted_path(path):
        return False
    return Path(path).suffix.lower() in TEXT_EXTENSIONS


def is_demote_only_source(path: str) -> bool:
    return (
        path.startswith("project_source/")
        or path == "codex_log/current_gray_test_target.md"
        or path.startswith("codex_log/deepseek_supply/")
    )


def read_text_from_head(head_ref: str, path: str) -> str:
    return run_git(["show", f"{head_ref}:{path}"])


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def chunk_id_for(path: str, heading_path: str, content_hash: str) -> str:
    seed = f"{path}\0{heading_path}\0{content_hash}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:20]


def sensitive_text_risk(text: str) -> str | None:
    patterns = [
        (r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}", "bearer_token_like_value"),
        (r"\bsk-[A-Za-z0-9]{20,}", "openai_style_key_like_value"),
        (r"\bAKIA[0-9A-Z]{16}\b", "access_key_like_value"),
        (
            r"(?i)(api[_-]?key|access[_-]?key|secret|token)\s*[:=]\s*[\"'][^\"']{12,}[\"']",
            "credential_assignment_like_value",
        ),
        (r"(?i)X-Amz-Signature=|Signature=", "signed_url_credential_query"),
    ]
    for pattern, reason in patterns:
        if re.search(pattern, text):
            return reason
    return None


def chunk_markdown(text: str) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    heading_stack: list[str] = []
    current_heading = "(root)"
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_lines, current_heading
        body = "\n".join(current_lines).strip()
        if body:
            chunks.append({"heading_path": current_heading, "text": body})
        current_lines = []

    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            flush()
            level = len(match.group(1))
            title = match.group(2).strip()
            heading_stack[:] = heading_stack[: level - 1] + [title]
            current_heading = " > ".join(heading_stack)
        current_lines.append(line)
    flush()
    if not chunks and text.strip():
        chunks.append({"heading_path": "(root)", "text": text.strip()})
    return chunks


def chunk_json(text: str) -> list[dict[str, Any]]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return [{"heading_path": "json:unparseable", "text": text}]

    chunks: list[dict[str, Any]] = []

    def dump(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2)

    if isinstance(data, dict):
        for list_key in ("fixtures", "results", "cases"):
            if isinstance(data.get(list_key), list):
                for index, item in enumerate(data[list_key]):
                    if isinstance(item, dict):
                        item_id = (
                            item.get("case_id")
                            or item.get("fixture_id")
                            or item.get("id")
                            or item.get("chunk_id")
                            or str(index)
                        )
                        chunks.append({"heading_path": f"/{list_key}/{item_id}", "text": dump(item)})
                    else:
                        chunks.append({"heading_path": f"/{list_key}/{index}", "text": dump(item)})
                return chunks
        for key, value in data.items():
            chunks.append({"heading_path": f"/{key}", "text": dump(value)})
    elif isinstance(data, list):
        for index, item in enumerate(data):
            if isinstance(item, dict):
                item_id = item.get("case_id") or item.get("fixture_id") or item.get("id") or str(index)
                chunks.append({"heading_path": f"/{item_id}", "text": dump(item)})
            else:
                chunks.append({"heading_path": f"/{index}", "text": dump(item)})
    else:
        chunks.append({"heading_path": "/", "text": dump(data)})
    return chunks


def chunk_python(text: str) -> list[dict[str, Any]]:
    chunks: list[dict[str, Any]] = []
    try:
        tree = ast.parse(text)
        docstring = ast.get_docstring(tree)
    except SyntaxError:
        docstring = None

    if docstring:
        chunks.append({"heading_path": "python:module_docstring", "text": docstring})

    lines = text.splitlines()
    constant_lines = [
        line
        for line in lines
        if re.match(r"^[A-Z][A-Z0-9_]+\s*=", line.strip())
        or re.match(r"^[A-Z][A-Z0-9_]+:\s*", line.strip())
    ]
    cli_lines = [line for line in lines if ".add_argument(" in line or "ArgumentParser(" in line]
    output_schema_lines = [
        line
        for line in lines
        if any(
            key in line
            for key in (
                "sync_status",
                "would_index_chunks",
                "blocked_chunks",
                "demoted_chunks",
                "metadata_validation_result",
                "can_apply",
            )
        )
    ]
    blocked_condition_lines = [
        line
        for line in lines
        if any(
            key in line.lower()
            for key in (
                "blocked",
                "secret",
                "media",
                "external_api_called",
                "vector_written",
                "embedding_generated",
                "deepseek_called",
            )
        )
    ]

    for heading_path, selected_lines in (
        ("python:constants", constant_lines),
        ("python:cli_args", cli_lines),
        ("python:output_schema", output_schema_lines),
        ("python:blocked_conditions", blocked_condition_lines),
    ):
        text_block = "\n".join(selected_lines).strip()
        if text_block:
            chunks.append({"heading_path": heading_path, "text": text_block})
    if not chunks and text.strip():
        chunks.append({"heading_path": "python:source_summary", "text": text[:4000]})
    return chunks


def chunk_text(path: str, text: str) -> list[dict[str, Any]]:
    suffix = Path(path).suffix.lower()
    if suffix == ".md":
        return chunk_markdown(text)
    if suffix == ".json":
        return chunk_json(text)
    if suffix == ".py":
        return chunk_python(text)
    return [{"heading_path": "(root)", "text": text}]


def infer_source_metadata(path: str) -> dict[str, Any]:
    conflict_tags: list[str] = []
    validation_required = True
    workflow_type = None
    task_type = None

    if path in CANONICAL_CURRENT_PATHS:
        authority_level = "canonical_current"
        status_label = "confirmed_by_repo"
        do_not_use = False
        reason = "canonical current source"
    elif path == "codex_log/latest.md":
        authority_level = "current_runtime_evidence"
        status_label = "confirmed_by_repo"
        do_not_use = False
        reason = "latest runtime log source"
    elif path.startswith("codex_log/vector_rag_router_design/fixtures/") and path.endswith(".json"):
        authority_level = "current_runtime_evidence"
        status_label = "confirmed_by_repo"
        do_not_use = True
        conflict_tags.append("fixture_validation_only")
        reason = "router fixture validation evidence"
    elif path.startswith("codex_log/vector_rag_router_design/"):
        authority_level = "current_auxiliary"
        status_label = "recommendation"
        do_not_use = True
        conflict_tags.append("strategy_design_only")
        reason = "vector RAG router design artifact; not completion proof"
    elif path.startswith("scripts/vector_rag_router_design/") or path.startswith("scripts/vector_sync/"):
        authority_level = "current_runtime_evidence"
        status_label = "pending_validation"
        do_not_use = True
        conflict_tags.append("dry_run_tooling_only")
        reason = "local dry-run tooling; not project completion proof"
    elif path.startswith("project_source/"):
        authority_level = "legacy_demoted"
        status_label = "deprecated"
        do_not_use = True
        conflict_tags.append("historical_archaeology_only")
        reason = "project_source is demoted historical material"
    elif path.startswith("codex_log/deepseek_supply/"):
        authority_level = "reference_only"
        status_label = "partial"
        do_not_use = True
        conflict_tags.extend(["not_completion_proof", "fallback_local_only_not_real_deepseek"])
        reason = "DeepSeek supply pack is reference only and cannot prove completion"
    elif path.startswith("GPT数据源/"):
        authority_level = "canonical_current"
        status_label = "confirmed_by_repo"
        do_not_use = False
        reason = "formal GPT data source"
    elif path.startswith("codex_source/"):
        authority_level = "canonical_current"
        status_label = "confirmed_by_repo"
        do_not_use = False
        reason = "Codex-side formal rule source"
    elif path in ALLOWED_DIST_REVIEW_PACK:
        authority_level = "current_runtime_evidence"
        status_label = "confirmed_by_repo"
        do_not_use = True
        conflict_tags.append("review_pack_pointer_only")
        reason = "review pack metadata pointer only"
    elif path.startswith("review_loop/"):
        authority_level = "current_auxiliary"
        status_label = "partial"
        do_not_use = True
        workflow_type = "data_review_loop"
        reason = "review-loop auxiliary evidence"
    else:
        authority_level = "current_auxiliary"
        status_label = "pending_validation"
        do_not_use = True
        reason = "allowed text candidate with pending validation"

    if "technical_preview" in path:
        conflict_tags.append("completion_truth_conflict")
    if "current_gray_test_target" in path:
        conflict_tags.append("phase_conflict")
    if "voice" in path.lower() or "声音" in path:
        conflict_tags.append("voice_identity_conflict")

    return {
        "authority_level": authority_level,
        "status_label": status_label,
        "conflict_tags": sorted(set(conflict_tags)),
        "do_not_use_for_completion_claim": do_not_use,
        "validation_required": validation_required,
        "workflow_type": workflow_type,
        "task_type": task_type,
        "reason": reason,
    }


def build_chunk_record(
    path: str,
    heading_path: str,
    text: str,
    branch: str,
    commit_sha: str,
    updated_at: str,
    action: str,
    reason: str,
) -> dict[str, Any]:
    content_hash = sha256_text(text)
    source_meta = infer_source_metadata(path)
    merged_tags = sorted(set(source_meta["conflict_tags"]))
    return {
        "chunk_id": chunk_id_for(path, heading_path, content_hash),
        "repo_full_name": REPO_FULL_NAME,
        "project_route": PROJECT_ROUTE,
        "branch": branch,
        "commit_sha": commit_sha,
        "source_path": path,
        "heading_path": heading_path,
        "content_hash": content_hash,
        "char_count": len(text),
        "authority_level": source_meta["authority_level"],
        "status_label": source_meta["status_label"],
        "updated_at": updated_at,
        "supersedes": None,
        "superseded_by": None,
        "conflict_tags": merged_tags,
        "workflow_type": source_meta["workflow_type"],
        "task_type": source_meta["task_type"],
        "validation_required": source_meta["validation_required"],
        "do_not_use_for_completion_claim": source_meta["do_not_use_for_completion_claim"],
        "action": action,
        "reason": reason or source_meta["reason"],
    }


def metadata_validation(chunks: list[dict[str, Any]]) -> dict[str, Any]:
    missing: list[dict[str, Any]] = []
    for chunk in chunks:
        missing_fields = [
            field
            for field in REQUIRED_CHUNK_FIELDS
            if field not in chunk or chunk[field] is None or chunk[field] == ""
        ]
        if not isinstance(chunk.get("conflict_tags"), list):
            missing_fields.append("conflict_tags:list")
        if not isinstance(chunk.get("do_not_use_for_completion_claim"), bool):
            missing_fields.append("do_not_use_for_completion_claim:bool")
        if missing_fields:
            missing.append({"chunk_id": chunk.get("chunk_id"), "missing_fields": missing_fields})
    return {
        "status": "passed" if not missing else "blocked",
        "required_fields": REQUIRED_CHUNK_FIELDS,
        "checked_chunk_count": len(chunks),
        "invalid_chunks": missing,
    }


def target_collection_for_branch(branch: str) -> tuple[str, bool]:
    if branch == "main":
        return "video_factory_main", True
    return "video_factory_branch_staging", False


def build_plan(base_ref: str, head_ref: str) -> dict[str, Any]:
    guard = ensure_repo_guard()
    branch = str(guard["branch"])
    head_commit_sha = run_git(["rev-parse", head_ref]).strip()
    updated_at = run_git(["show", "-s", "--format=%cI", head_commit_sha]).strip()
    if not updated_at:
        updated_at = datetime.now(timezone.utc).isoformat()

    changed_files = parse_name_status(run_git(["diff", "--name-status", base_ref, head_ref]))
    target_collection, allowed_for_real_tasks = target_collection_for_branch(branch)

    would_index_chunks: list[dict[str, Any]] = []
    skipped_chunks: list[dict[str, Any]] = []
    blocked_chunks: list[dict[str, Any]] = []
    demoted_chunks: list[dict[str, Any]] = []
    deleted_chunks: list[dict[str, Any]] = []

    for changed in changed_files:
        path = str(changed["path"])
        status = str(changed["status"])
        if status == "D":
            deleted_chunks.append({
                "source_path": path,
                "action": "would_delete_or_tombstone",
                "reason": "file deleted in diff; future apply would tombstone or delete matching chunks",
            })
            continue

        if is_secret_path(path):
            blocked_chunks.append({
                "source_path": path,
                "action": "blocked",
                "reason": "secret path filter matched; file content was not read",
            })
            continue

        if is_media_path(path):
            skipped_chunks.append({
                "source_path": path,
                "action": "skipped",
                "reason": "raw media/binary extension excluded; file content was not read",
            })
            continue

        if is_blacklisted_path(path):
            skipped_chunks.append({
                "source_path": path,
                "action": "skipped",
                "reason": "blacklist path filter matched; file content was not read",
            })
            continue

        if not is_readable_text_candidate(path):
            skipped_chunks.append({
                "source_path": path,
                "action": "skipped",
                "reason": "not an allowlisted text candidate for dry-run chunking",
            })
            continue

        try:
            text = read_text_from_head(head_ref, path)
        except RuntimeError as exc:
            blocked_chunks.append({
                "source_path": path,
                "action": "blocked",
                "reason": f"unable to read text from head ref: {exc}",
            })
            continue

        text_risk = sensitive_text_risk(text)
        if text_risk:
            blocked_chunks.append({
                "source_path": path,
                "action": "blocked",
                "reason": f"sensitive text filter matched: {text_risk}",
            })
            continue

        for chunk in chunk_text(path, text):
            source_meta = infer_source_metadata(path)
            if is_demote_only_source(path):
                demoted_chunks.append(
                    build_chunk_record(
                        path=path,
                        heading_path=chunk["heading_path"],
                        text=chunk["text"],
                        branch=branch,
                        commit_sha=head_commit_sha,
                        updated_at=updated_at,
                        action="would_demote_or_reference_only",
                        reason=source_meta["reason"],
                    )
                )
            else:
                would_index_chunks.append(
                    build_chunk_record(
                        path=path,
                        heading_path=chunk["heading_path"],
                        text=chunk["text"],
                        branch=branch,
                        commit_sha=head_commit_sha,
                        updated_at=updated_at,
                        action="would_index",
                        reason=source_meta["reason"],
                    )
                )

    metadata_result = metadata_validation(would_index_chunks)
    conflict_tags_added = sorted(
        {
            tag
            for chunk in [*would_index_chunks, *demoted_chunks]
            for tag in chunk.get("conflict_tags", [])
        }
    )
    secret_status = "blocked" if any("secret path" in item["reason"] for item in blocked_chunks) else "passed"
    media_skipped = [item for item in skipped_chunks if "media" in item["reason"]]
    blacklist_skipped = [item for item in skipped_chunks if "blacklist" in item["reason"]]
    blocking_present = bool(blocked_chunks) or metadata_result["status"] != "passed"

    return {
        "sync_status": "blocked" if blocking_present else "passed",
        "dry_run_only": True,
        "external_api_called": False,
        "secrets_read_or_printed": False,
        "media_content_read": False,
        "deepseek_called": False,
        "vector_index_created": False,
        "embedding_generated": False,
        "vector_written": False,
        "repo_full_name": REPO_FULL_NAME,
        "project_route": PROJECT_ROUTE,
        "branch": branch,
        "repo_guard": guard,
        "base_ref": base_ref,
        "head_ref": head_ref,
        "head_commit_sha": head_commit_sha,
        "target_collection": target_collection,
        "allowed_for_real_tasks": allowed_for_real_tasks,
        "changed_files": changed_files,
        "would_index_chunks": would_index_chunks,
        "skipped_chunks": skipped_chunks,
        "blocked_chunks": blocked_chunks,
        "demoted_chunks": demoted_chunks,
        "deleted_chunks": deleted_chunks,
        "secret_scan_result": {
            "status": secret_status,
            "secret_paths_read": False,
            "blocked_secret_path_count": sum(1 for item in blocked_chunks if "secret path" in item["reason"]),
        },
        "media_exclusion_result": {
            "status": "passed",
            "media_files_read": False,
            "skipped_media_count": len(media_skipped),
        },
        "blacklist_filter_result": {
            "status": "passed",
            "blacklisted_files_read": False,
            "skipped_blacklisted_count": len(blacklist_skipped),
        },
        "metadata_validation_result": metadata_result,
        "conflict_tags_added": conflict_tags_added,
        "can_apply": False,
        "apply_blocked_reason": (
            "dry_run_only: real vector sync apply requires explicit future authorization, "
            "remote HEAD verification, provider configuration, and a separate apply execution order"
        ),
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_summary(path: Path, plan: dict[str, Any]) -> None:
    lines = [
        "# 20260611 Vector Sync Dry Run Summary",
        "",
        "## status",
        "",
        f"- sync_status: `{plan['sync_status']}`",
        "- dry_run_only: `true`",
        "- external_api_called: `false`",
        "- vector_index_created: `false`",
        "- embedding_generated: `false`",
        "- vector_written: `false`",
        "- deepseek_called: `false`",
        f"- target_collection: `{plan['target_collection']}`",
        f"- allowed_for_real_tasks: `{str(plan['allowed_for_real_tasks']).lower()}`",
        f"- can_apply: `{str(plan['can_apply']).lower()}`",
        "",
        "## counts",
        "",
        f"- changed_files: `{len(plan['changed_files'])}`",
        f"- would_index_chunks: `{len(plan['would_index_chunks'])}`",
        f"- skipped_chunks: `{len(plan['skipped_chunks'])}`",
        f"- blocked_chunks: `{len(plan['blocked_chunks'])}`",
        f"- demoted_chunks: `{len(plan['demoted_chunks'])}`",
        f"- deleted_chunks: `{len(plan['deleted_chunks'])}`",
        "",
        "## safety_results",
        "",
        f"- secret_scan_result: `{plan['secret_scan_result']['status']}`",
        f"- media_exclusion_result: `{plan['media_exclusion_result']['status']}`",
        f"- blacklist_filter_result: `{plan['blacklist_filter_result']['status']}`",
        f"- metadata_validation_result: `{plan['metadata_validation_result']['status']}`",
        "",
        "## changed_files",
        "",
    ]
    for changed in plan["changed_files"]:
        old = f" (from `{changed['old_path']}`)" if changed.get("old_path") else ""
        lines.append(f"- `{changed['status']}` `{changed['path']}`{old}")
    lines.extend([
        "",
        "## conflict_tags_added",
        "",
    ])
    if plan["conflict_tags_added"]:
        for tag in plan["conflict_tags_added"]:
            lines.append(f"- `{tag}`")
    else:
        lines.append("- none")
    lines.extend([
        "",
        "## apply_boundary",
        "",
        f"- apply_blocked_reason: {plan['apply_blocked_reason']}",
        "- This file is a dry-run summary only. It does not prove RAG runtime, embedding generation, or vector DB writes.",
        "",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run a local-only vector sync dry-run.")
    parser.add_argument("--base-ref", required=True, help="Base git ref, for example origin/main")
    parser.add_argument("--head-ref", required=True, help="Head git ref, for example HEAD")
    args = parser.parse_args(argv)

    plan = build_plan(base_ref=args.base_ref, head_ref=args.head_ref)
    write_json(PLAN_PATH, plan)
    write_summary(SUMMARY_PATH, plan)
    return 0 if plan["sync_status"] in {"passed", "blocked"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
