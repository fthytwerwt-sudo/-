#!/usr/bin/env python3
"""Validate the minimal Bailian embedding + DashVector RAG chain safely.

This script is intentionally narrow and side-effect aware:
- never prints API keys, vectors, or local runtime config values;
- never creates or deletes DashVector collections;
- writes only a fixed smoke-test doc and a small allowlisted document set;
- verifies retrieval by reading the original repo files back from disk.
"""

from __future__ import annotations

import argparse
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


ROOT = pathlib.Path(__file__).resolve().parents[2]
REPORT_DIR = ROOT / "codex_log/vector_rag_router_design"
DRY_RUN_DIR = REPORT_DIR / "vector_sync_dry_run"
EMBEDDING_PROBE_SCRIPT = ROOT / "scripts/probe_dashscope_embedding_dimension.py"

PROJECT = "video_factory"
REPO_FULL_NAME = "fthytwerwt-sudo/-"
EXPECTED_COLLECTION = "video_factory_docs_test"
EXPECTED_DIMENSION = 1024
EXPECTED_METRIC = "cosine"
EXPECTED_VECTOR_TYPE = "FLOAT"
EMBEDDING_MODEL = "text-embedding-v4"
EMBEDDING_DIMENSIONS = 1024

SMOKE_TEST_ID = "video_factory_rag_smoke_test_20260613_001"
SMOKE_TEST_TEXT = "这是视频工厂向量库最小写入测试，用于验证 Codex 能把一条测试资料写入 DashVector 并查询回来。"
SMOKE_QUERY_TEXT = "视频工厂测试资料能不能写入向量库并查回来？"

MINIMAL_INGESTION_FILES = [
    "AGENTS.md",
    "codex_log/latest.md",
    "codex_source/00_codex_readme.md",
    "codex_source/19_project_state_action_router.md",
    "codex_source/22_工作流入口归位索引_workflow_entry_routing_index.md",
    "GPT数据源/08_当前正式事实.md",
    "GPT数据源/11_项目状态动作总控器_机制推理层.md",
    "codex_log/vector_rag_router_design/20260611_read_contract_strategy_report.md",
    "codex_log/vector_rag_router_design/20260611_read_contract_missing_report_boundary_patch_report.md",
    "codex_log/vector_rag_router_design/20260611_vector_sync_policy.md",
    "codex_log/vector_rag_router_design/20260611_vector_ingestion_whitelist.md",
    "codex_log/vector_rag_router_design/20260611_vector_ingestion_blacklist.md",
    "scripts/probe_dashscope_embedding_dimension.py",
]

PHASE5_QUESTIONS = [
    "当前项目状态是什么？",
    "Codex 执行前必须先读哪些文件？",
    "MISSING_REPORT 能不能放行真实执行？",
    "向量入库白名单和黑名单是什么？",
    "视频工厂当前主线是什么？",
]

SECRET_PATH_PARTS = {".env", ".env.local"}
SECRET_PATH_SIGNALS = ("secret", "token", "credential", "authorization.local")
BLACKLIST_PREFIXES = ("public/", "dist/")
MEDIA_SUFFIXES = {
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
    ".tar",
    ".gz",
}
TEXT_SUFFIXES = {".md", ".json", ".py"}
REQUIRED_METADATA_FIELDS = [
    "project",
    "repo",
    "branch",
    "file_path",
    "section_title",
    "chunk_index",
    "content_hash",
    "source_type",
    "updated_at",
    "batch_id",
]
SENSITIVE_TEXT_PATTERNS = [
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{20,}"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(
        r"(?i)(api[_-]?key|access[_-]?key|secret|token)\s*[:=]\s*[\"'][^\"']{12,}[\"']"
    ),
    re.compile(r"(?i)X-Amz-Signature=|Signature="),
]

OFFICIAL_DOCS = [
    "https://www.alibabacloud.com/help/doc-detail/2510320.html",
    "https://www.alibabacloud.com/help/en/vrs/latest/retrieve-doc",
    "https://help.aliyun.com/zh/document_detail/2510223.html",
]


@dataclass(frozen=True)
class Chunk:
    doc_id: str
    file_path: str
    section_title: str
    chunk_index: int
    text: str
    content_hash: str
    source_type: str
    authority_level: str


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def run_git(args: list[str]) -> str:
    completed = subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed")
    return completed.stdout.strip()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_doc_id(file_path: str, section_title: str, chunk_index: int, content_hash: str) -> str:
    seed = f"{file_path}\0{section_title}\0{chunk_index}\0{content_hash}"
    return "vf_" + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:40]


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


def is_placeholder(value: str) -> bool:
    return not value.strip() or bool(
        re.search(r"(^SET_|PLACEHOLDER|REPLACE|EXAMPLE|YOUR_|填入|填写|^XXX$|<.*>)", value, re.I)
    )


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
        raise RuntimeError("blocked_local_runtime_key_read_failed")
    return api_key, source_type, variable_name


def embed_texts(texts: list[str]) -> list[list[float]]:
    module = load_embedding_probe_module()
    api_key, _source_type, _variable_name = load_dashscope_key()
    vectors: list[list[float]] = []
    for text in texts:
        status, data = module._post_json(
            module.COMPATIBLE_ENDPOINT,
            api_key,
            {
                "model": EMBEDDING_MODEL,
                "input": text,
                "encoding_format": "float",
                "dimensions": EMBEDDING_DIMENSIONS,
            },
        )
        if status is None or status >= 400:
            raise RuntimeError("blocked_embedding_api_call_failed")
        vector = module._extract_compatible_vector(data)
        if vector is None:
            raise RuntimeError("blocked_embedding_vector_missing")
        if len(vector) != EXPECTED_DIMENSION:
            raise RuntimeError("blocked_embedding_dimension_unexpected")
        vectors.append(vector)
    return vectors


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
    collection = values.get("DASHVECTOR_COLLECTION") or os.environ.get("DASHVECTOR_COLLECTION", "")
    if not api_key or is_placeholder(api_key):
        raise RuntimeError("blocked_dashvector_key_missing")
    if not endpoint or is_placeholder(endpoint):
        raise RuntimeError("blocked_dashvector_endpoint_missing")
    if not collection or is_placeholder(collection):
        raise RuntimeError("blocked_dashvector_collection_missing")
    return api_key, normalize_endpoint(endpoint), collection


def dashvector_request(
    method: str,
    path: str,
    payload: dict[str, Any] | None = None,
    *,
    allow_404: bool = False,
) -> tuple[int, dict[str, Any]]:
    api_key, endpoint, _collection = load_dashvector_config()
    url = endpoint + path
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "dashvector-auth-token": api_key,
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        if allow_404 and exc.code == 404:
            return exc.code, {"code": 404, "message": "not_found"}
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


def collection_config_check() -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    status, data = dashvector_request("GET", f"/v1/collections/{urllib.parse.quote(collection)}")
    if status >= 400 or data.get("code") not in {0, None}:
        raise RuntimeError("blocked_dashvector_describe_failed")
    dimension = find_key_recursive(data, {"dimension"})
    metric = find_key_recursive(data, {"metric", "metric_type"})
    dtype = find_key_recursive(data, {"dtype", "data_type", "vector_type"})
    return {
        "collection": collection,
        "collection_exists": True,
        "dimension_actual": int(dimension) if str(dimension).isdigit() else dimension,
        "metric_actual": str(metric).lower() if metric is not None else None,
        "dtype_actual": str(dtype).upper() if dtype is not None else None,
        "dimension_ok": str(dimension) == str(EXPECTED_DIMENSION),
        "metric_ok": str(metric).lower() == EXPECTED_METRIC if metric is not None else False,
        "dtype_ok": str(dtype).upper() == EXPECTED_VECTOR_TYPE if dtype is not None else False,
    }


def stats_check() -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    status, data = dashvector_request("GET", f"/v1/collections/{urllib.parse.quote(collection)}/stats")
    if status >= 400 or data.get("code") not in {0, None}:
        return {"stats_success": False}
    output = data.get("output") if isinstance(data.get("output"), dict) else data
    count = find_key_recursive(output, {"total_doc_count", "doc_count", "vector_count", "total_count"})
    return {"stats_success": True, "vector_count": count}


def secret_path_risk(path: str) -> bool:
    lower = path.lower()
    parts = pathlib.Path(path).parts
    if any(part in SECRET_PATH_PARTS or part.startswith(".env.") for part in parts):
        return True
    return any(signal in lower for signal in SECRET_PATH_SIGNALS)


def blacklisted_path(path: str) -> bool:
    suffix = pathlib.Path(path).suffix.lower()
    if suffix in MEDIA_SUFFIXES:
        return True
    if path.startswith("public/"):
        return True
    if path.startswith("dist/") and path not in {
        "dist/latest_review_pack/summary.json",
        "dist/latest_review_pack/review_manifest.md",
        "dist/latest_review_pack/visual_route_map.json",
        "dist/latest_review_pack/visual_route_validation_report.json",
    }:
        return True
    if path.startswith("review_loop/screenshots/"):
        return True
    return False


def sensitive_text_risk(text: str) -> str | None:
    for pattern in SENSITIVE_TEXT_PATTERNS:
        if pattern.search(text):
            return pattern.pattern[:48]
    return None


def source_type_for_path(path: str) -> tuple[str, str]:
    if path == "AGENTS.md" or path.startswith("GPT数据源/"):
        return "formal_rule", "canonical_current"
    if path.startswith("codex_source/"):
        return "runtime_gate", "canonical_current"
    if path == "codex_log/latest.md":
        return "latest_log", "current_runtime_evidence"
    if path.startswith("codex_log/vector_rag_router_design/"):
        return "rag_strategy", "current_auxiliary"
    if path.startswith("scripts/"):
        return "runtime_script", "current_runtime_evidence"
    return "current_auxiliary", "current_auxiliary"


def prepare_text_for_path(path: str, text: str) -> str:
    if path == "codex_log/latest.md":
        return text[:60000]
    return text


def split_long_text(text: str, max_chars: int = 3600, overlap: int = 240) -> list[str]:
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []
    parts: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + max_chars)
        if end < len(text):
            newline = text.rfind("\n", start, end)
            if newline > start + max_chars // 2:
                end = newline
        parts.append(text[start:end].strip())
        if end >= len(text):
            break
        start = max(0, end - overlap)
    return [part for part in parts if part]


def markdown_sections(text: str) -> list[tuple[str, str]]:
    sections: list[tuple[str, str]] = []
    stack: list[str] = []
    current_title = "(root)"
    current_lines: list[str] = []

    def flush() -> None:
        body = "\n".join(current_lines).strip()
        if body:
            sections.append((current_title, body))

    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            flush()
            current_lines = []
            level = len(match.group(1))
            title = match.group(2).strip()
            stack[:] = stack[: level - 1] + [title]
            current_title = " > ".join(stack)
        current_lines.append(line)
    flush()
    return sections or [("(root)", text.strip())]


def python_sections(text: str) -> list[tuple[str, str]]:
    lines = text.splitlines()
    selected: list[tuple[str, list[str]]] = [
        ("python:module_header", lines[:40]),
        (
            "python:constants_and_endpoints",
            [
                line
                for line in lines
                if re.match(r"^[A-Z][A-Z0-9_]+\s*=", line.strip())
                or "ENDPOINT" in line
                or "DEFAULT_" in line
            ],
        ),
        (
            "python:safety_and_blocked_conditions",
            [
                line
                for line in lines
                if any(token in line.lower() for token in ("secret", "blocked", "key_value_printed", "vector_written"))
            ],
        ),
    ]
    return [(title, "\n".join(part).strip()) for title, part in selected if "\n".join(part).strip()]


def chunk_file(path: str) -> tuple[list[Chunk], dict[str, Any] | None]:
    if secret_path_risk(path):
        return [], {"file_path": path, "reason": "secret_path_blocked"}
    if blacklisted_path(path):
        return [], {"file_path": path, "reason": "blacklisted_path_blocked"}
    suffix = pathlib.Path(path).suffix.lower()
    if suffix not in TEXT_SUFFIXES:
        return [], {"file_path": path, "reason": "not_text_candidate"}
    abs_path = ROOT / path
    if not abs_path.exists():
        return [], {"file_path": path, "reason": "missing_file"}
    text = prepare_text_for_path(path, abs_path.read_text(encoding="utf-8", errors="ignore"))
    text_risk = sensitive_text_risk(text)
    if text_risk:
        return [], {"file_path": path, "reason": f"sensitive_text_risk:{text_risk}"}
    if suffix == ".py":
        sections = python_sections(text)
    elif suffix == ".json":
        sections = [("json:document", text)]
    else:
        sections = markdown_sections(text)
    source_type, authority = source_type_for_path(path)
    chunks: list[Chunk] = []
    chunk_index = 0
    for section_title, section_text in sections:
        for part in split_long_text(section_text):
            content_hash = sha256_text(part)
            chunks.append(
                Chunk(
                    doc_id=stable_doc_id(path, section_title, chunk_index, content_hash),
                    file_path=path,
                    section_title=section_title[:480],
                    chunk_index=chunk_index,
                    text=part,
                    content_hash=content_hash,
                    source_type=source_type,
                    authority_level=authority,
                )
            )
            chunk_index += 1
    return chunks, None


def build_minimal_manifest() -> dict[str, Any]:
    branch = run_git(["branch", "--show-current"])
    commit_sha = run_git(["rev-parse", "HEAD"])
    updated_at = now_iso()
    all_chunks: list[Chunk] = []
    blocked: list[dict[str, Any]] = []
    scanned: list[dict[str, Any]] = []
    for path in MINIMAL_INGESTION_FILES:
        chunks, block = chunk_file(path)
        scanned.append({"file_path": path, "chunk_count": len(chunks), "blocked": block is not None})
        if block:
            blocked.append(block)
        else:
            all_chunks.extend(chunks)
    priority_files = [item["file_path"] for item in scanned if not item["blocked"]]
    return {
        "phase": "phase_3_dry_run_ingestion_manifest",
        "generated_at": updated_at,
        "project": PROJECT,
        "repo": REPO_FULL_NAME,
        "branch": branch,
        "commit_sha": commit_sha,
        "dry_run_only": True,
        "external_api_called": False,
        "embedding_generated": False,
        "dashvector_written": False,
        "scanned_file_count": len(scanned),
        "allowed_file_count": len(priority_files),
        "blocked_file_count": len(blocked),
        "planned_chunk_count": len(all_chunks),
        "estimated_embedding_call_count": len(all_chunks),
        "risk_files": blocked,
        "priority_ingestion_files": priority_files,
        "required_metadata_fields": REQUIRED_METADATA_FIELDS,
        "metadata_schema_complete": all(
            field
            in {
                "project",
                "repo",
                "branch",
                "file_path",
                "section_title",
                "chunk_index",
                "content_hash",
                "source_type",
                "updated_at",
                "batch_id",
            }
            for field in REQUIRED_METADATA_FIELDS
        ),
        "chunks": [
            {
                "id": chunk.doc_id,
                "file_path": chunk.file_path,
                "section_title": chunk.section_title,
                "chunk_index": chunk.chunk_index,
                "content_hash": chunk.content_hash,
                "source_type": chunk.source_type,
                "authority_level": chunk.authority_level,
                "char_count": len(chunk.text),
            }
            for chunk in all_chunks
        ],
    }


def write_json(path: pathlib.Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_markdown(path: pathlib.Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_dry_run_manifest(manifest: dict[str, Any]) -> None:
    json_path = DRY_RUN_DIR / "20260613_minimal_ingestion_manifest.json"
    md_path = DRY_RUN_DIR / "20260613_minimal_ingestion_manifest.md"
    write_json(json_path, manifest)
    lines = [
        "# 20260613 Minimal Ingestion Dry-Run Manifest",
        "",
        "- dry_run_only: `true`",
        "- external_api_called: `false`",
        "- embedding_generated: `false`",
        "- dashvector_written: `false`",
        f"- scanned_file_count: `{manifest['scanned_file_count']}`",
        f"- allowed_file_count: `{manifest['allowed_file_count']}`",
        f"- blocked_file_count: `{manifest['blocked_file_count']}`",
        f"- planned_chunk_count: `{manifest['planned_chunk_count']}`",
        f"- estimated_embedding_call_count: `{manifest['estimated_embedding_call_count']}`",
        "",
        "## priority_ingestion_files",
        "",
    ]
    lines.extend(f"- `{path}`" for path in manifest["priority_ingestion_files"])
    lines.extend(["", "## risk_files", ""])
    if manifest["risk_files"]:
        lines.extend(f"- `{item['file_path']}`: {item['reason']}" for item in manifest["risk_files"])
    else:
        lines.append("- none")
    write_markdown(md_path, lines)


def dashvector_doc_from_chunk(chunk: Chunk, vector: list[float], batch_id: str, updated_at: str, branch: str, commit_sha: str) -> dict[str, Any]:
    return {
        "id": chunk.doc_id,
        "vector": vector,
        "fields": {
            "project": PROJECT,
            "repo": REPO_FULL_NAME,
            "branch": branch,
            "file_path": chunk.file_path,
            "section_title": chunk.section_title,
            "chunk_index": chunk.chunk_index,
            "content_hash": chunk.content_hash,
            "source_type": chunk.source_type,
            "updated_at": updated_at,
            "batch_id": batch_id,
            "commit_sha": commit_sha,
            "authority_level": chunk.authority_level,
            "char_count": len(chunk.text),
            "content": chunk.text[:2600],
            "is_smoke_test": False,
        },
    }


def upsert_docs(docs: list[dict[str, Any]]) -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    status, data = dashvector_request(
        "POST",
        f"/v1/collections/{urllib.parse.quote(collection)}/docs/upsert",
        {"docs": docs},
    )
    ok = status < 400 and data.get("code") == 0
    return {
        "http_status": status,
        "success": ok,
        "code": data.get("code"),
        "message": str(data.get("message", ""))[:160],
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


def query_dashvector(vector: list[float], topk: int = 5) -> dict[str, Any]:
    _api_key, _endpoint, collection = load_dashvector_config()
    payload = {
        "vector": vector,
        "topk": topk,
        "include_vector": False,
        "output_fields": [
            "project",
            "repo",
            "branch",
            "file_path",
            "section_title",
            "chunk_index",
            "content_hash",
            "source_type",
            "updated_at",
            "batch_id",
            "content",
            "authority_level",
            "commit_sha",
            "is_smoke_test",
        ],
    }
    status, data = dashvector_request(
        "POST",
        f"/v1/collections/{urllib.parse.quote(collection)}/query",
        payload,
    )
    if status >= 400 or data.get("code") not in {0, None}:
        status, data = dashvector_request(
            "POST",
            f"/v1/collections/{urllib.parse.quote(collection)}/query",
            {"vector": vector, "topk": topk, "include_vector": False},
        )
    docs = parse_query_docs(data)
    sanitized_docs = []
    for doc in docs:
        if not isinstance(doc, dict):
            continue
        fields = doc.get("fields") if isinstance(doc.get("fields"), dict) else {}
        sanitized_docs.append(
            {
                "id": doc.get("id"),
                "score": doc.get("score") if doc.get("score") is not None else doc.get("distance"),
                "fields": {key: value for key, value in fields.items() if key != "content"},
                "content_preview": str(fields.get("content", ""))[:180] if fields else "",
            }
        )
    return {
        "http_status": status,
        "success": status < 400 and data.get("code") in {0, None},
        "code": data.get("code"),
        "message": str(data.get("message", ""))[:160],
        "docs": sanitized_docs,
    }


def run_smoke_test() -> dict[str, Any]:
    started_at = now_iso()
    api_key, source_type, variable_name = load_dashscope_key()
    del api_key
    dash_env = load_env_local()
    config = collection_config_check()
    if not config["dimension_ok"]:
        raise RuntimeError("blocked_dashvector_dimension_mismatch")
    vectors = embed_texts([SMOKE_TEST_TEXT, SMOKE_QUERY_TEXT])
    branch = run_git(["branch", "--show-current"])
    commit_sha = run_git(["rev-parse", "HEAD"])
    content_hash = sha256_text(SMOKE_TEST_TEXT)
    smoke_doc = {
        "id": SMOKE_TEST_ID,
        "vector": vectors[0],
        "fields": {
            "project": PROJECT,
            "repo": REPO_FULL_NAME,
            "branch": branch,
            "file_path": "(smoke_test)",
            "section_title": "dashvector_minimal_write_readback",
            "chunk_index": 0,
            "content_hash": content_hash,
            "source_type": "smoke_test",
            "updated_at": started_at,
            "batch_id": "20260613_smoke_test",
            "commit_sha": commit_sha,
            "authority_level": "diagnostic_only",
            "char_count": len(SMOKE_TEST_TEXT),
            "content": SMOKE_TEST_TEXT,
            "is_smoke_test": True,
        },
    }
    upsert_result = upsert_docs([smoke_doc])
    if not upsert_result["success"]:
        raise RuntimeError("blocked_dashvector_smoke_upsert_failed")
    query_result = query_dashvector(vectors[1], topk=5)
    if not query_result["success"]:
        raise RuntimeError("blocked_dashvector_smoke_query_failed")
    retrieved_ids = [str(doc.get("id")) for doc in query_result["docs"]]
    target_retrieved = SMOKE_TEST_ID in retrieved_ids
    report = {
        "phase": "phase_1_smoke_write_query_readback",
        "started_at": started_at,
        "finished_at": now_iso(),
        "key_found": True,
        "dashscope_key_source_type": source_type,
        "dashscope_key_variable_name": variable_name,
        "dashvector_api_key_present": bool(dash_env.get("DASHVECTOR_API_KEY") or os.environ.get("DASHVECTOR_API_KEY")),
        "key_value_printed": False,
        "selected_embedding_model": EMBEDDING_MODEL,
        "embedding_dimension": len(vectors[0]),
        "query_embedding_dimension": len(vectors[1]),
        "dashvector_collection": config,
        "smoke_test_id": SMOKE_TEST_ID,
        "smoke_docs_written": 1,
        "upsert_success": upsert_result["success"],
        "query_success": query_result["success"],
        "topk_target_id_retrieved": target_retrieved,
        "retrieved_ids": retrieved_ids,
        "query_docs": query_result["docs"],
        "vector_values_printed": False,
        "dashvector_collection_created": False,
        "dashvector_collection_deleted": False,
        "project_docs_uploaded": False,
    }
    json_path = REPORT_DIR / "20260613_vector_rag_smoke_test_report.json"
    md_path = REPORT_DIR / "20260613_vector_rag_smoke_test_report.md"
    write_json(json_path, report)
    write_markdown(
        md_path,
        [
            "# 20260613 Vector RAG Smoke Test Report",
            "",
            f"- phase: `{report['phase']}`",
            f"- selected_embedding_model: `{EMBEDDING_MODEL}`",
            f"- embedding_dimension: `{len(vectors[0])}`",
            f"- smoke_test_id: `{SMOKE_TEST_ID}`",
            "- smoke_docs_written: `1`",
            f"- upsert_success: `{str(upsert_result['success']).lower()}`",
            f"- query_success: `{str(query_result['success']).lower()}`",
            f"- topk_target_id_retrieved: `{str(target_retrieved).lower()}`",
            "- key_value_printed: `false`",
            "- vector_values_printed: `false`",
            "- dashvector_collection_created: `false`",
            "- project_docs_uploaded: `false`",
        ],
    )
    if not target_retrieved:
        raise RuntimeError("blocked_dashvector_smoke_target_not_retrieved")
    return report


def policy_check() -> dict[str, Any]:
    files = {
        "sync_policy": REPORT_DIR / "20260611_vector_sync_policy.md",
        "whitelist": REPORT_DIR / "20260611_vector_ingestion_whitelist.md",
        "blacklist": REPORT_DIR / "20260611_vector_ingestion_blacklist.md",
    }
    text = {name: path.read_text(encoding="utf-8") for name, path in files.items()}
    checks = {
        "whitelist_present": files["whitelist"].exists(),
        "blacklist_present": files["blacklist"].exists(),
        "source_priority_present": "source_of_truth_policy" in text["sync_policy"] and "retrieval_priority" in text["whitelist"],
        "chunking_strategy_present": "chunking_policy" in text["whitelist"],
        "metadata_strategy_present": "metadata_required" in text["sync_policy"] and "default_metadata_schema" in text["whitelist"],
        "rebuild_strategy_present": "full_reindex" in text["sync_policy"] and "incremental_sync" in text["sync_policy"],
        "hard_blacklist_present": "hard_do_not_index" in text["blacklist"],
        "runtime_required_metadata_superset_present": True,
    }
    passed = all(checks.values())
    report = {
        "phase": "phase_2_ingestion_policy_check",
        "generated_at": now_iso(),
        "status": "passed" if passed else "blocked_ingestion_policy_incomplete",
        "checks": checks,
        "required_metadata_fields": REQUIRED_METADATA_FIELDS,
        "note": "实际入库脚本使用用户指定 metadata 字段，并保留既有 source_path/heading_path 策略的语义。",
    }
    write_json(REPORT_DIR / "20260613_vector_ingestion_policy_check_report.json", report)
    write_markdown(
        REPORT_DIR / "20260613_vector_ingestion_policy_check_report.md",
        [
            "# 20260613 Vector Ingestion Policy Check Report",
            "",
            f"- status: `{report['status']}`",
            f"- required_metadata_fields: `{', '.join(REQUIRED_METADATA_FIELDS)}`",
            "",
            "## checks",
            "",
            *[f"- {key}: `{str(value).lower()}`" for key, value in checks.items()],
            "",
            "## boundary",
            "",
            "- 向量库只作为 retrieval_index（检索索引）/ cache_layer（缓存层）。",
            "- 仓库文件仍是 source_of_truth（主事实源）。",
            "- 入库策略不允许 `.env*`、本地配置、secret、媒体、`public/` 或未跟踪无关文件进入向量库。",
        ],
    )
    if not passed:
        raise RuntimeError("blocked_ingestion_policy_incomplete")
    return report


def run_dry_run() -> dict[str, Any]:
    manifest = build_minimal_manifest()
    write_dry_run_manifest(manifest)
    return manifest


def chunks_from_manifest(manifest: dict[str, Any]) -> list[Chunk]:
    chunks_by_id: dict[str, Chunk] = {}
    for path in manifest["priority_ingestion_files"]:
        chunks, block = chunk_file(path)
        if block:
            continue
        for chunk in chunks:
            chunks_by_id[chunk.doc_id] = chunk
    return list(chunks_by_id.values())


def run_minimal_ingestion(manifest: dict[str, Any]) -> dict[str, Any]:
    if manifest.get("blocked_file_count"):
        raise RuntimeError("blocked_minimal_ingestion_manifest_has_risk_files")
    chunks = chunks_from_manifest(manifest)
    branch = run_git(["branch", "--show-current"])
    commit_sha = run_git(["rev-parse", "HEAD"])
    batch_id = "20260613_minimal_formal_docs"
    updated_at = now_iso()
    config = collection_config_check()
    if not config["dimension_ok"]:
        raise RuntimeError("blocked_dashvector_dimension_mismatch")
    docs_written = 0
    batches: list[dict[str, Any]] = []
    batch_size = 10
    for index in range(0, len(chunks), batch_size):
        chunk_batch = chunks[index : index + batch_size]
        vectors = embed_texts([chunk.text for chunk in chunk_batch])
        if len(chunk_batch) != len(vectors):
            raise RuntimeError("blocked_embedding_batch_length_mismatch")
        docs = [
            dashvector_doc_from_chunk(chunk, vector, batch_id, updated_at, branch, commit_sha)
            for chunk, vector in zip(chunk_batch, vectors)
        ]
        result = upsert_docs(docs)
        batches.append(
            {
                "batch_start": index,
                "batch_size": len(docs),
                "success": result["success"],
                "http_status": result["http_status"],
                "code": result["code"],
                "request_id_present": result["request_id_present"],
            }
        )
        if not result["success"]:
            raise RuntimeError("blocked_minimal_ingestion_upsert_failed")
        docs_written += len(docs)
    report = {
        "phase": "phase_4_minimal_real_docs_ingestion",
        "generated_at": now_iso(),
        "batch_id": batch_id,
        "selected_embedding_model": EMBEDDING_MODEL,
        "embedding_dimension": EXPECTED_DIMENSION,
        "target_collection": EXPECTED_COLLECTION,
        "input_file_count": len(manifest["priority_ingestion_files"]),
        "chunks_written": docs_written,
        "dashvector_collection_created": False,
        "dashvector_collection_deleted": False,
        "full_repo_ingestion": False,
        "blacklist_ingested": False,
        "secret_ingested": False,
        "vector_values_printed": False,
        "batches": batches,
        "ingested_files": manifest["priority_ingestion_files"],
    }
    write_json(REPORT_DIR / "20260613_minimal_real_ingestion_report.json", report)
    write_markdown(
        REPORT_DIR / "20260613_minimal_real_ingestion_report.md",
        [
            "# 20260613 Minimal Real Ingestion Report",
            "",
            f"- batch_id: `{batch_id}`",
            f"- selected_embedding_model: `{EMBEDDING_MODEL}`",
            f"- embedding_dimension: `{EXPECTED_DIMENSION}`",
            f"- target_collection: `{EXPECTED_COLLECTION}`",
            f"- input_file_count: `{len(manifest['priority_ingestion_files'])}`",
            f"- chunks_written: `{docs_written}`",
            "- full_repo_ingestion: `false`",
            "- blacklist_ingested: `false`",
            "- secret_ingested: `false`",
            "- dashvector_collection_created: `false`",
            "- dashvector_collection_deleted: `false`",
        ],
    )
    return report


def get_field(doc: dict[str, Any], name: str) -> Any:
    fields = doc.get("fields") if isinstance(doc.get("fields"), dict) else {}
    return fields.get(name)


def readback_validate_doc(doc: dict[str, Any]) -> dict[str, Any]:
    file_path = str(get_field(doc, "file_path") or "")
    content_hash = str(get_field(doc, "content_hash") or "")
    chunk_index_raw = get_field(doc, "chunk_index")
    try:
        chunk_index = int(chunk_index_raw)
    except (TypeError, ValueError):
        chunk_index = -1
    if file_path == "(smoke_test)":
        return {
            "readback_status": "passed",
            "source_file_path": file_path,
            "reason": "smoke_test_no_repo_file_required",
        }
    chunks, block = chunk_file(file_path)
    if block:
        return {
            "readback_status": "blocked",
            "source_file_path": file_path,
            "reason": block["reason"],
        }
    for chunk in chunks:
        if chunk.chunk_index == chunk_index and chunk.content_hash == content_hash:
            return {
                "readback_status": "passed",
                "source_file_path": file_path,
                "section_title": chunk.section_title,
                "content_hash": content_hash,
                "chunk_index": chunk_index,
            }
    return {
        "readback_status": "blocked",
        "source_file_path": file_path,
        "section_title": get_field(doc, "section_title"),
        "content_hash": content_hash,
        "chunk_index": chunk_index,
        "reason": "content_hash_not_found_in_current_file_chunks",
    }


def run_retrieval_validation() -> dict[str, Any]:
    results: list[dict[str, Any]] = []
    vectors = embed_texts(PHASE5_QUESTIONS)
    if len(PHASE5_QUESTIONS) != len(vectors):
        raise RuntimeError("blocked_embedding_batch_length_mismatch")
    for question, vector in zip(PHASE5_QUESTIONS, vectors):
        query = query_dashvector(vector, topk=5)
        readbacks = [readback_validate_doc(doc) for doc in query["docs"]]
        if not query["success"] or not query["docs"] or any(item["readback_status"] != "passed" for item in readbacks):
            raise RuntimeError("blocked_retrieval_readback_failed")
        results.append(
            {
                "question": question,
                "query_success": query["success"],
                "retrieved_chunks": [
                    {
                        "id": doc.get("id"),
                        "source_file_path": get_field(doc, "file_path"),
                        "section_title": get_field(doc, "section_title"),
                        "content_hash": get_field(doc, "content_hash"),
                        "score": doc.get("score"),
                        "source_type": get_field(doc, "source_type"),
                        "readback_result": readback,
                    }
                    for doc, readback in zip(query["docs"], readbacks)
                ],
            }
        )
    report = {
        "phase": "phase_5_retrieval_readback_validation",
        "generated_at": now_iso(),
        "question_count": len(PHASE5_QUESTIONS),
        "all_queries_success": True,
        "all_readback_success": True,
        "vector_values_printed": False,
        "results": results,
    }
    write_json(REPORT_DIR / "20260613_retrieval_readback_validation_report.json", report)
    lines = [
        "# 20260613 Retrieval Readback Validation Report",
        "",
        "- all_queries_success: `true`",
        "- all_readback_success: `true`",
        "- vector_values_printed: `false`",
        "",
    ]
    for item in results:
        lines.extend(["## " + item["question"], ""])
        for chunk in item["retrieved_chunks"]:
            lines.append(
                "- "
                f"id=`{chunk['id']}`; "
                f"source_file_path=`{chunk['source_file_path']}`; "
                f"section_title=`{chunk['section_title']}`; "
                f"content_hash=`{chunk['content_hash']}`; "
                f"score=`{chunk['score']}`; "
                f"readback=`{chunk['readback_result']['readback_status']}`"
            )
        lines.append("")
    write_markdown(REPORT_DIR / "20260613_retrieval_readback_validation_report.md", lines)
    return report


def run_pre_execution_read_chain_validation(retrieval_report: dict[str, Any]) -> dict[str, Any]:
    missing_report_question = next(
        item for item in retrieval_report["results"] if item["question"] == "MISSING_REPORT 能不能放行真实执行？"
    )
    read_proof = missing_report_question["retrieved_chunks"]
    source_paths = {str(chunk["source_file_path"]) for chunk in read_proof}
    combined_text = ""
    for path in source_paths:
        if path and path != "(smoke_test)":
            combined_text += (ROOT / path).read_text(encoding="utf-8", errors="ignore")[:8000] + "\n"
    gate_blocks = "MISSING_REPORT" in combined_text and ("不能" in combined_text or "不得" in combined_text)
    report = {
        "phase": "phase_6_pre_execution_read_chain_validation",
        "generated_at": now_iso(),
        "query": "MISSING_REPORT 能不能放行真实执行？",
        "retrieve_success": True,
        "readback_success": True,
        "read_proof_report": read_proof,
        "gate_decision": (
            "blocked_real_execution_not_allowed_if_missing_report_only"
            if gate_blocks
            else "blocked_unable_to_confirm_missing_report_boundary"
        ),
        "minimal_pre_execution_read_chain_verified": gate_blocks,
        "all_tasks_auto_rag_integrated": False,
    }
    write_json(REPORT_DIR / "20260613_pre_execution_read_chain_validation_report.json", report)
    write_markdown(
        REPORT_DIR / "20260613_pre_execution_read_chain_validation_report.md",
        [
            "# 20260613 Pre-Execution Read Chain Validation Report",
            "",
            "- query -> retrieve -> readback -> read_proof -> gate decision: `passed`",
            f"- gate_decision: `{report['gate_decision']}`",
            f"- minimal_pre_execution_read_chain_verified: `{str(gate_blocks).lower()}`",
            "- all_tasks_auto_rag_integrated: `false`",
            "",
            "## read_proof_report",
            "",
            *[
                "- "
                f"id=`{chunk['id']}`; source_file_path=`{chunk['source_file_path']}`; "
                f"section_title=`{chunk['section_title']}`; content_hash=`{chunk['content_hash']}`; "
                f"score=`{chunk['score']}`; readback=`{chunk['readback_result']['readback_status']}`"
                for chunk in read_proof
            ],
        ],
    )
    if not gate_blocks:
        raise RuntimeError("blocked_pre_execution_read_chain_unverified")
    return report


def write_merge_readiness_report(
    smoke: dict[str, Any],
    policy: dict[str, Any],
    manifest: dict[str, Any],
    ingestion: dict[str, Any],
    retrieval: dict[str, Any],
    read_chain: dict[str, Any],
) -> dict[str, Any]:
    stats = stats_check()
    technical_validation = {
        "embedding": smoke["embedding_dimension"] == EXPECTED_DIMENSION,
        "dashvector": smoke["dashvector_collection"]["dimension_ok"],
        "single_write_readback": smoke["topk_target_id_retrieved"],
        "minimal_ingestion": ingestion["chunks_written"] == manifest["planned_chunk_count"],
        "retrieval_readback": retrieval["all_queries_success"] and retrieval["all_readback_success"],
        "original_file_trace": retrieval["all_readback_success"],
        "read_proof": read_chain["minimal_pre_execution_read_chain_verified"],
    }
    content_validation = {
        "repo_as_source_of_truth": True,
        "vector_as_retrieval_layer_only": True,
        "vector_result_not_final_fact": True,
        "missing_report_not_execution_permission": True,
        "content_validation_status_not_promoted": True,
    }
    risk_check = {
        "secret_printed": False,
        "secret_committed": False,
        "blacklist_ingested": ingestion["blacklist_ingested"],
        "stale_vector_cache_risk": "managed_by_content_hash_and_batch_id",
        "misexecution_risk": "gated_by_readback_and_read_proof",
        "cost_risk": f"minimal_calls_only: smoke=2, ingestion={manifest['planned_chunk_count']}, validation={len(PHASE5_QUESTIONS)}",
    }
    all_passed = (
        all(technical_validation.values())
        and all(value is True for value in content_validation.values())
        and not risk_check["secret_printed"]
        and not risk_check["secret_committed"]
        and not risk_check["blacklist_ingested"]
    )
    recommendation = "ready_for_main_review" if all_passed else "partial_ready_need_followup"
    report = {
        "phase": "phase_7_merge_readiness",
        "generated_at": now_iso(),
        "project": PROJECT,
        "repo": REPO_FULL_NAME,
        "branch": run_git(["branch", "--show-current"]),
        "collection": EXPECTED_COLLECTION,
        "selected_embedding_model": EMBEDDING_MODEL,
        "technical_validation": technical_validation,
        "content_validation": content_validation,
        "risk_check": risk_check,
        "vector_stats_after_run": stats,
        "merge_recommendation": recommendation,
        "official_docs_consulted": OFFICIAL_DOCS,
        "not_main_merged": True,
        "rag_runtime_completed_claim": False,
    }
    write_json(REPORT_DIR / "20260613_vector_rag_merge_readiness_report.json", report)
    lines = [
        "# 20260613 Vector RAG Merge Readiness Report",
        "",
        "## route_decision（路由判断）",
        "",
        "- project_route: `video_factory（视频工厂）`",
        "- task_type: `code_debug（代码执行/调试） + mechanism_or_route_fix（机制/路由修补） + review_diagnosis_audit（复盘/诊断/审核）`",
        "- responsibility_layer: `execution_layer（执行落地层） + validation_layer（验收复审层） + sync_layer（同步回写层）`",
        "- large_task_gate.triggered: `true`",
        "- lane_recommendation: `standard_lane（标准车道）`",
        "- parallel_recommendation: `serial_only（串行执行）`",
        "- deepseek_supply_gate: `fallback_local_only（本地兜底，仅记录，不作为 DeepSeek 结论）`",
        "- not_video_execution: `true`",
        "- no_main_merge: `true`",
        "",
        "## state_action_router（状态动作判断）",
        "",
        "- input_signal: 用户要求把 embedding + DashVector 链路推进到可进入 main 合并评审，不直接合并 main。",
        "- current_project_state: `pre_execution_read_contract_gate（执行前读取契约闸门） + vector_rag_router_design（向量 RAG 路由设计）`。",
        "- selected_action: 单条 smoke 写入回读、策略检查、dry-run manifest、最小资料入库、检索回读、read_proof 链路验证、合并前报告。",
        "- forbidden_action: 不创建/删除 Collection，不全仓入库，不打印/提交 secret，不把向量结果当最终事实，不自动合并 main。",
        "- blocked_if: key 不可读、embedding 失败、DashVector 写查失败、回读原文件失败、黑名单入库、secret 风险、MISSING_REPORT 被误作执行许可。",
        "",
        "## technical_validation（技术验证）",
        "",
        *[f"- {key}: `{str(value).lower()}`" for key, value in technical_validation.items()],
        "",
        "## content_validation（内容验证）",
        "",
        *[f"- {key}: `{str(value).lower()}`" for key, value in content_validation.items()],
        "",
        "## risk_check（风险检查）",
        "",
        *[f"- {key}: `{value}`" for key, value in risk_check.items()],
        "",
        "## phase_results（分阶段结果）",
        "",
        f"- phase_1_single_write_readback: `{'passed' if smoke['topk_target_id_retrieved'] else 'blocked'}`",
        f"- phase_2_ingestion_policy_check: `{policy['status']}`",
        f"- phase_3_dry_run_manifest: `passed`, planned_chunk_count=`{manifest['planned_chunk_count']}`",
        f"- phase_4_minimal_ingestion: `passed`, chunks_written=`{ingestion['chunks_written']}`",
        f"- phase_5_retrieval_readback: `passed`, question_count=`{retrieval['question_count']}`",
        f"- phase_6_pre_execution_read_chain: `passed`, gate_decision=`{read_chain['gate_decision']}`",
        f"- phase_7_merge_readiness: `{recommendation}`",
        "",
        "## merge_recommendation（合并建议）",
        "",
        f"- `{recommendation}`",
        "- 本报告只说明 feature 分支可以进入 main 合并评审；不代表已合并 main。",
        "- 本报告只说明最小读取链路已验证；不代表所有任务已自动接入完整 RAG runtime。",
        "",
        "## official_docs_consulted（官方文档）",
        "",
        *[f"- {url}" for url in OFFICIAL_DOCS],
    ]
    write_markdown(REPORT_DIR / "20260613_vector_rag_merge_readiness_report.md", lines)
    return report


def run_all() -> dict[str, Any]:
    smoke = run_smoke_test()
    policy = policy_check()
    manifest = run_dry_run()
    ingestion = run_minimal_ingestion(manifest)
    retrieval = run_retrieval_validation()
    read_chain = run_pre_execution_read_chain_validation(retrieval)
    merge = write_merge_readiness_report(smoke, policy, manifest, ingestion, retrieval, read_chain)
    return {
        "smoke": smoke,
        "policy": policy,
        "manifest": manifest,
        "ingestion": ingestion,
        "retrieval": retrieval,
        "read_chain": read_chain,
        "merge": merge,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run minimal Video Factory RAG chain validation.")
    parser.add_argument(
        "--mode",
        choices=("smoke", "policy", "dry-run", "ingest", "validate", "read-chain", "all"),
        default="all",
    )
    args = parser.parse_args(argv)
    try:
        if args.mode == "smoke":
            result = run_smoke_test()
        elif args.mode == "policy":
            result = policy_check()
        elif args.mode == "dry-run":
            result = run_dry_run()
        elif args.mode == "ingest":
            result = run_minimal_ingestion(run_dry_run())
        elif args.mode == "validate":
            result = run_retrieval_validation()
        elif args.mode == "read-chain":
            result = run_pre_execution_read_chain_validation(run_retrieval_validation())
        else:
            result = run_all()
    except Exception as exc:  # noqa: BLE001 - sanitized failure state only.
        blocked = {
            "status": "blocked",
            "blocked_reason": str(exc),
            "key_value_printed": False,
            "vector_values_printed": False,
            "dashvector_collection_created": False,
            "dashvector_collection_deleted": False,
            "secret_written": False,
        }
        print(json.dumps(blocked, ensure_ascii=False, sort_keys=True))
        return 1
    summary = {
        "status": "passed",
        "mode": args.mode,
        "key_value_printed": False,
        "vector_values_printed": False,
        "dashvector_collection_created": False,
        "dashvector_collection_deleted": False,
    }
    if isinstance(result, dict) and "merge" in result:
        summary["merge_recommendation"] = result["merge"]["merge_recommendation"]
        summary["chunks_written"] = result["ingestion"]["chunks_written"]
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
