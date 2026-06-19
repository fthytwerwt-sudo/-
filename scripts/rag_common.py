#!/usr/bin/env python3
"""Shared helpers for the Video Factory RAG sync scripts.

The helpers are deliberately narrow:
- no secret values are printed or written;
- vectors are never written to disk;
- dynamic audit artifacts are excluded from the formal source corpus.
"""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "codex_log" / "rag_vector_sync"
EMBEDDING_PROBE_SCRIPT = ROOT / "scripts" / "probe_dashscope_embedding_dimension.py"

PROJECT_ROUTE = "video_factory"
REPO_FULL_NAME = "fthytwerwt-sudo/-"
EMBEDDING_MODEL = "text-embedding-v4"
EMBEDDING_DIMENSION = 1024
VECTOR_STORE_PROVIDER = "DashVector"
DEFAULT_COLLECTION = "video_factory_docs_test"

SOURCE_INVENTORY_PATH = OUT_DIR / "latest_source_inventory.json"
CHUNK_MANIFEST_PATH = OUT_DIR / "latest_chunk_manifest.json"
INDEX_MANIFEST_PATH = OUT_DIR / "latest_index_manifest.json"
RETRIEVAL_REPORT_JSON_PATH = OUT_DIR / "latest_retrieval_probe_report.json"
RETRIEVAL_REPORT_MD_PATH = OUT_DIR / "latest_retrieval_probe_report.md"
SUPPLY_REPORT_JSON_PATH = OUT_DIR / "latest_supply_bus_report.json"
SUPPLY_REPORT_MD_PATH = OUT_DIR / "latest_supply_bus_report.md"
SECRET_SCAN_PATH = OUT_DIR / "latest_secret_scan_report.json"

ALLOW_PATTERNS = (
    "AGENTS.md",
    "GPT数据源/**/*.md",
    "codex_source/**/*.md",
    "codex_source/**/*.yaml",
    "codex_source/**/*.py",
    "codex_log/latest.md",
    "codex_log/**/*.md",
    "review_loop/**/*.md",
    "review_loop/**/*.json",
    "scripts/**/*.py",
)

DENY_PATTERNS = (
    ".env",
    ".env.*",
    "**/*secret*",
    "**/*token*",
    "**/*key*",
    "**/*.mp4",
    "**/*.mov",
    "**/*.wav",
    "**/*.mp3",
    "**/*.png",
    "**/*.jpg",
    "**/*.jpeg",
    "**/*.webp",
    "**/*.zip",
    "dist/**/*",
    "public/**/*",
    "node_modules/**/*",
    ".git/**/*",
    "归档删除区_archive_delete_zone/**/*",
    "raw_reference/**/*",
)

DYNAMIC_AUDIT_PREFIXES = (
    "codex_log/rag_vector_sync/",
)

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json"}
MAX_CHUNK_LINES = 80
MAX_CHUNK_CHARS = 3200
MIN_CHUNK_CHARS = 400

SECRET_TEXT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("bearer_token", re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}")),
    ("openai_style_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    (
        "named_secret_assignment",
        re.compile(
            r"(?i)(api[_-]?key|access[_-]?key|secret|token)\s*[:=]\s*[\"'][^\"']{12,}[\"']"
        ),
    ),
    ("signed_url", re.compile(r"(?i)X-Amz-Signature=|Signature=")),
)


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    source_path: str
    line_start: int
    line_end: int
    text: str
    chunk_hash: str
    file_hash: str
    commit_sha: str
    indexed_at: str

    @property
    def line_range(self) -> str:
        return f"{self.line_start}-{self.line_end}"


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: pathlib.Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def rel_path(path: pathlib.Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_markdown(path: pathlib.Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def run_git(args: list[str], *, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and completed.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed")
    return completed.stdout.strip()


def current_branch() -> str:
    return run_git(["branch", "--show-current"])


def current_commit() -> str:
    return run_git(["rev-parse", "HEAD"])


def git_status_short() -> list[str]:
    output = run_git(["status", "--short"], check=False)
    return [line for line in output.splitlines() if line.strip()]


def match_pattern(path: str, pattern: str) -> bool:
    if pattern.endswith("/**/*"):
        return path.startswith(pattern[: -len("/**/*")] + "/")
    if "/**/*" in pattern:
        prefix, suffix = pattern.split("/**/*", 1)
        return path.startswith(prefix + "/") and path.endswith(suffix)
    return fnmatch.fnmatch(path, pattern)


def deny_reason(path: str) -> str | None:
    lower = path.lower()
    if any(path.startswith(prefix) for prefix in DYNAMIC_AUDIT_PREFIXES):
        return "excluded_dynamic_audit_artifact"
    if "第三方原文全文" in path:
        return "excluded_third_party_raw_reference"
    for pattern in DENY_PATTERNS:
        if match_pattern(path, pattern) or match_pattern(lower, pattern.lower()):
            return f"denylist:{pattern}"
    return None


def allowed_by_pattern(path: str) -> bool:
    return any(match_pattern(path, pattern) for pattern in ALLOW_PATTERNS)


def is_text_candidate(path: pathlib.Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES


def iter_candidate_files() -> list[pathlib.Path]:
    paths: set[pathlib.Path] = set()
    for pattern in ALLOW_PATTERNS:
        if pattern == "AGENTS.md":
            candidate = ROOT / pattern
            if candidate.exists():
                paths.add(candidate)
            continue
        paths.update(candidate for candidate in ROOT.glob(pattern) if candidate.is_file())
    return sorted(paths, key=lambda item: rel_path(item))


def secret_scan_text(text: str) -> list[str]:
    matches: list[str] = []
    for name, pattern in SECRET_TEXT_PATTERNS:
        if pattern.search(text):
            matches.append(name)
    return matches


def build_source_inventory() -> dict[str, Any]:
    generated_at = now_iso()
    branch = current_branch()
    commit_sha = current_commit()
    allowed_files: list[dict[str, Any]] = []
    excluded_files: list[dict[str, Any]] = []
    secret_hits: list[dict[str, Any]] = []

    for path in iter_candidate_files():
        relative = rel_path(path)
        denial = deny_reason(relative)
        if denial:
            excluded_files.append({"source_path": relative, "reason": denial})
            continue
        if not is_text_candidate(path):
            excluded_files.append({"source_path": relative, "reason": "not_indexable_text"})
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        hits = secret_scan_text(text)
        if hits:
            secret_hits.append({"source_path": relative, "patterns": hits})
            excluded_files.append({"source_path": relative, "reason": "excluded_by_secret_or_privacy_scan"})
            continue
        allowed_files.append(
            {
                "source_path": relative,
                "file_hash": sha256_file(path),
                "byte_size": path.stat().st_size,
                "line_count": len(text.splitlines()),
            }
        )

    allowlist_check_passed = all(allowed_by_pattern(item["source_path"]) for item in allowed_files)
    denylist_check_passed = all(deny_reason(item["source_path"]) is None for item in allowed_files)
    indexed_secret_hits = [
        hit for hit in secret_hits if any(item["source_path"] == hit["source_path"] for item in allowed_files)
    ]
    secret_scan_passed = not indexed_secret_hits
    inventory = {
        "manifest_type": "source_inventory",
        "project_route": PROJECT_ROUTE,
        "repo_full_name": REPO_FULL_NAME,
        "branch": branch,
        "commit_sha": commit_sha,
        "generated_at": generated_at,
        "allow_patterns": list(ALLOW_PATTERNS),
        "deny_patterns": list(DENY_PATTERNS),
        "dynamic_audit_prefixes_excluded": list(DYNAMIC_AUDIT_PREFIXES),
        "secret_scan_passed": secret_scan_passed,
        "allowlist_check_passed": allowlist_check_passed,
        "denylist_check_passed": denylist_check_passed,
        "allowed_file_count": len(allowed_files),
        "excluded_file_count": len(excluded_files),
        "secret_hit_count": len(secret_hits),
        "excluded_by_secret_or_privacy_scan_count": len(secret_hits),
        "indexed_secret_hit_count": len(indexed_secret_hits),
        "allowed_files": allowed_files,
        "excluded_files": excluded_files,
        "secret_hits": secret_hits,
        "indexed_secret_hits": indexed_secret_hits,
        "blocked": not (secret_scan_passed and allowlist_check_passed and denylist_check_passed),
        "blocked_if": [
            "secret_scan_failed",
            "allowlist_check_failed",
            "denylist_hit_in_allowed_files",
        ],
    }
    return inventory


def stable_chunk_id(source_path: str, line_start: int, line_end: int, chunk_hash: str) -> str:
    seed = f"{PROJECT_ROUTE}\0{source_path}\0{line_start}\0{line_end}\0{chunk_hash}"
    return "vf_" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:40]


def chunk_lines(lines: list[str]) -> list[tuple[int, int, str]]:
    chunks: list[tuple[int, int, str]] = []
    start = 1
    current: list[str] = []
    current_chars = 0
    for index, line in enumerate(lines, start=1):
        line_len = len(line) + 1
        should_flush = bool(current) and (
            len(current) >= MAX_CHUNK_LINES
            or current_chars + line_len > MAX_CHUNK_CHARS
            or (line.startswith("#") and current_chars >= MIN_CHUNK_CHARS)
        )
        if should_flush:
            text = "\n".join(current).strip()
            if text:
                chunks.append((start, index - 1, text))
            start = index
            current = []
            current_chars = 0
        current.append(line)
        current_chars += line_len
    if current:
        text = "\n".join(current).strip()
        if text:
            chunks.append((start, start + len(current) - 1, text))
    return chunks


def build_chunks(inventory: dict[str, Any]) -> dict[str, Any]:
    generated_at = now_iso()
    commit_sha = str(inventory["commit_sha"])
    chunks: list[Chunk] = []
    for item in inventory.get("allowed_files", []):
        source_path = item["source_path"]
        abs_path = ROOT / source_path
        text = abs_path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        file_hash = item["file_hash"]
        for line_start, line_end, chunk_text in chunk_lines(lines):
            chunk_hash = sha256_text(chunk_text)
            chunks.append(
                Chunk(
                    chunk_id=stable_chunk_id(source_path, line_start, line_end, chunk_hash),
                    source_path=source_path,
                    line_start=line_start,
                    line_end=line_end,
                    text=chunk_text,
                    chunk_hash=chunk_hash,
                    file_hash=file_hash,
                    commit_sha=commit_sha,
                    indexed_at=generated_at,
                )
            )
    manifest = {
        "manifest_type": "chunk_manifest",
        "project_route": PROJECT_ROUTE,
        "repo_full_name": REPO_FULL_NAME,
        "branch": inventory["branch"],
        "commit_sha": commit_sha,
        "generated_at": generated_at,
        "source_inventory_path": SOURCE_INVENTORY_PATH.as_posix(),
        "chunk_count": len(chunks),
        "file_count": len(inventory.get("allowed_files", [])),
        "chunk_manifest_valid": bool(chunks) and not inventory.get("blocked", True),
        "chunks": [
            {
                "chunk_id": chunk.chunk_id,
                "source_path": chunk.source_path,
                "line_range": chunk.line_range,
                "line_start": chunk.line_start,
                "line_end": chunk.line_end,
                "chunk_hash": chunk.chunk_hash,
                "file_hash": chunk.file_hash,
                "commit_sha": chunk.commit_sha,
                "indexed_at": chunk.indexed_at,
                "char_count": len(chunk.text),
            }
            for chunk in chunks
        ],
        "blocked": not (bool(chunks) and not inventory.get("blocked", True)),
        "blocked_if": [
            "source_inventory_blocked",
            "chunk_missing_metadata",
            "chunk_manifest_empty",
        ],
    }
    return manifest


def chunks_from_manifest(manifest: dict[str, Any]) -> list[Chunk]:
    chunks: list[Chunk] = []
    for item in manifest.get("chunks", []):
        source_path = item["source_path"]
        text = read_line_range(source_path, int(item["line_start"]), int(item["line_end"]))
        chunks.append(
            Chunk(
                chunk_id=item["chunk_id"],
                source_path=source_path,
                line_start=int(item["line_start"]),
                line_end=int(item["line_end"]),
                text=text.strip(),
                chunk_hash=item["chunk_hash"],
                file_hash=item["file_hash"],
                commit_sha=item["commit_sha"],
                indexed_at=item["indexed_at"],
            )
        )
    return chunks


def read_line_range(source_path: str, line_start: int, line_end: int) -> str:
    path = ROOT / source_path
    lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    return "\n".join(lines[line_start - 1 : line_end])


def readback_for_chunk(item: dict[str, Any]) -> dict[str, Any]:
    source_path = str(item["source_path"])
    line_start = int(item.get("line_start") or str(item["line_range"]).split("-", 1)[0])
    line_end = int(item.get("line_end") or str(item["line_range"]).split("-", 1)[1])
    text = read_line_range(source_path, line_start, line_end).strip()
    chunk_hash = sha256_text(text)
    file_hash = sha256_file(ROOT / source_path)
    return {
        "source_path": source_path,
        "line_range": f"{line_start}-{line_end}",
        "chunk_id": item["chunk_id"],
        "readback": text[:1200],
        "readback_hash_match": chunk_hash == item["chunk_hash"],
        "file_hash_match": file_hash == item["file_hash"],
        "current_chunk_hash": chunk_hash,
        "current_file_hash": file_hash,
    }


def load_env_local() -> dict[str, str]:
    path = ROOT / ".env.local"
    values: dict[str, str] = {}
    if not path.exists():
        return values
    for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        if key in {"DASHVECTOR_API_KEY", "DASHVECTOR_ENDPOINT", "DASHVECTOR_COLLECTION"}:
            values[key] = value.strip().strip('"').strip("'")
    return values


PLACEHOLDER_RE = re.compile(r"(^SET_|PLACEHOLDER|REPLACE|EXAMPLE|YOUR_|填入|填写|^XXX$|<.*>)", re.I)


def is_placeholder(value: str) -> bool:
    return not value.strip() or bool(PLACEHOLDER_RE.search(value.strip()))


def normalize_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip().rstrip("/")
    if not endpoint:
        return ""
    if endpoint.startswith("http://") or endpoint.startswith("https://"):
        return endpoint
    return f"https://{endpoint}"


def load_dashvector_config() -> tuple[str, str, str]:
    values = load_env_local()
    api_key = values.get("DASHVECTOR_API_KEY") or os.environ.get("DASHVECTOR_API_KEY", "")
    endpoint = values.get("DASHVECTOR_ENDPOINT") or os.environ.get("DASHVECTOR_ENDPOINT", "")
    collection = values.get("DASHVECTOR_COLLECTION") or os.environ.get("DASHVECTOR_COLLECTION", DEFAULT_COLLECTION)
    if not api_key or is_placeholder(api_key):
        raise RuntimeError("blocked_dashvector_key_missing")
    if not endpoint or is_placeholder(endpoint):
        raise RuntimeError("blocked_dashvector_endpoint_missing")
    if not collection or is_placeholder(collection):
        raise RuntimeError("blocked_dashvector_collection_missing")
    return api_key, normalize_endpoint(endpoint), collection


def load_embedding_probe_module() -> Any:
    spec = importlib.util.spec_from_file_location("embedding_probe", EMBEDDING_PROBE_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("embedding_probe_import_failed")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_dashscope_key() -> tuple[str, str, str]:
    module = load_embedding_probe_module()
    api_key, source_type, variable_name, placeholder = module.load_key(module._resolve_default_config())
    if not api_key or placeholder:
        raise RuntimeError("blocked_embedding_auth_missing")
    return api_key, source_type, variable_name


def embed_texts(texts: list[str]) -> list[list[float]]:
    module = load_embedding_probe_module()
    api_key, _source_type, _variable_name = load_dashscope_key()
    if not texts:
        return []
    status, data = module._post_json(
        module.COMPATIBLE_ENDPOINT,
        api_key,
        {
            "model": EMBEDDING_MODEL,
            "input": texts if len(texts) > 1 else texts[0],
            "encoding_format": "float",
            "dimensions": EMBEDDING_DIMENSION,
        },
    )
    if status is None or status >= 400:
        raise RuntimeError("blocked_embedding_api_call_failed")
    rows = data.get("data") or []
    if not isinstance(rows, list):
        raise RuntimeError("blocked_embedding_vector_missing")
    rows = sorted((row for row in rows if isinstance(row, dict)), key=lambda row: int(row.get("index", 0)))
    vectors: list[list[float]] = []
    for row in rows:
        vector = row.get("embedding")
        if not isinstance(vector, list) or not all(isinstance(item, (int, float)) for item in vector):
            raise RuntimeError("blocked_embedding_vector_missing")
        if len(vector) != EMBEDDING_DIMENSION:
            raise RuntimeError("blocked_embedding_dimension_unexpected")
        vectors.append(vector)
    if len(vectors) != len(texts):
        raise RuntimeError("blocked_embedding_vector_count_mismatch")
    return vectors


def dashvector_request(method: str, path: str, payload: dict[str, Any] | None = None) -> tuple[int, dict[str, Any]]:
    api_key, endpoint, _collection = load_dashvector_config()
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        endpoint + path,
        data=data,
        method=method,
        headers={"dashvector-auth-token": api_key, "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            data_obj = json.loads(body) if body else {}
        except json.JSONDecodeError:
            data_obj = {"message": body[:160]}
        return exc.code, data_obj


def find_key_recursive(value: Any, keys: set[str]) -> Any:
    if isinstance(value, dict):
        for key, item in value.items():
            if key.lower() in keys:
                return item
        for item in value.values():
            found = find_key_recursive(item, keys)
            if found is not None:
                return found
    if isinstance(value, list):
        for item in value:
            found = find_key_recursive(item, keys)
            if found is not None:
                return found
    return None


def dashvector_collection_check() -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    status, data = dashvector_request("GET", f"/v1/collections/{urllib.parse.quote(collection)}")
    if status >= 400 or data.get("code") not in {0, None}:
        raise RuntimeError("blocked_dashvector_collection_describe_failed")
    dimension = find_key_recursive(data, {"dimension"})
    metric = find_key_recursive(data, {"metric", "metric_type"})
    dtype = find_key_recursive(data, {"dtype", "data_type", "vector_type"})
    return {
        "collection": collection,
        "collection_exists": True,
        "dimension_actual": int(dimension) if str(dimension).isdigit() else dimension,
        "metric_actual": str(metric).lower() if metric is not None else None,
        "dtype_actual": str(dtype).upper() if dtype is not None else None,
        "dimension_ok": str(dimension) == str(EMBEDDING_DIMENSION),
    }


def dashvector_doc_from_chunk(chunk: Chunk, vector: list[float]) -> dict[str, Any]:
    return {
        "id": chunk.chunk_id,
        "vector": vector,
        "fields": {
            "project_route": PROJECT_ROUTE,
            "repo_full_name": REPO_FULL_NAME,
            "source_path": chunk.source_path,
            "line_range": chunk.line_range,
            "line_start": chunk.line_start,
            "line_end": chunk.line_end,
            "chunk_id": chunk.chunk_id,
            "chunk_hash": chunk.chunk_hash,
            "file_hash": chunk.file_hash,
            "commit_sha": chunk.commit_sha,
            "indexed_at": chunk.indexed_at,
            "embedding_model": EMBEDDING_MODEL,
            "content_storage_policy": "source_readback_only",
        },
    }


def upsert_docs(docs: list[dict[str, Any]]) -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    status, data = dashvector_request(
        "POST",
        f"/v1/collections/{urllib.parse.quote(collection)}/docs/upsert",
        {"docs": docs},
    )
    ok = status < 400 and data.get("code") in {0, None}
    return {
        "http_status": status,
        "success": ok,
        "code": data.get("code"),
        "message_preview": str(data.get("message", ""))[:160],
        "request_id_present": bool(data.get("request_id")),
    }


def parse_query_docs(data: dict[str, Any]) -> list[dict[str, Any]]:
    output = data.get("output")
    if isinstance(output, dict):
        for key in ("docs", "results", "documents"):
            if isinstance(output.get(key), list):
                return output[key]
    if isinstance(output, list):
        return output
    for key in ("docs", "results", "documents"):
        if isinstance(data.get(key), list):
            return data[key]
    return []


def query_dashvector(vector: list[float], topk: int = 5, filter_expression: str | None = None) -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    payload = {
        "vector": vector,
        "topk": topk,
        "include_vector": False,
        "output_fields": [
            "project_route",
            "repo_full_name",
            "source_path",
            "line_range",
            "line_start",
            "line_end",
            "chunk_id",
            "chunk_hash",
            "file_hash",
            "commit_sha",
            "indexed_at",
            "embedding_model",
            "content_storage_policy",
        ],
    }
    if filter_expression:
        payload["filter"] = filter_expression
    status, data = dashvector_request(
        "POST",
        f"/v1/collections/{urllib.parse.quote(collection)}/query",
        payload,
    )
    if status >= 400 or data.get("code") not in {0, None}:
        return {"success": False, "http_status": status, "code": data.get("code"), "docs": []}
    docs: list[dict[str, Any]] = []
    for doc in parse_query_docs(data):
        if not isinstance(doc, dict):
            continue
        fields = doc.get("fields") if isinstance(doc.get("fields"), dict) else {}
        docs.append(
            {
                "id": doc.get("id"),
                "score": doc.get("score") if doc.get("score") is not None else doc.get("distance"),
                "fields": fields,
                "content_preview": "",
            }
        )
    return {"success": True, "http_status": status, "code": data.get("code"), "docs": docs}


def load_chunk_by_id(manifest: dict[str, Any]) -> dict[str, Any]:
    return {item["chunk_id"]: item for item in manifest.get("chunks", [])}


def has_only_allowed_dirty_paths(allowed_prefixes: tuple[str, ...] = DYNAMIC_AUDIT_PREFIXES) -> bool:
    for line in git_status_short():
        path = line[3:].strip()
        if path == "public/" or path.startswith("public/"):
            continue
        if not any(path.startswith(prefix) for prefix in allowed_prefixes):
            return False
    return True


def build_arg_parser(description: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--output-dir", default=str(OUT_DIR), help="Audit output directory.")
    return parser


def main_guard() -> None:
    if ROOT.name != "视频工厂":
        raise SystemExit("blocked_wrong_workspace_root")
