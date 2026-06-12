#!/usr/bin/env python3
"""Probe DashScope embedding vector length without printing secrets.

This script is intentionally narrow:
- reads a Bailian/DashScope key from process env or local runtime config;
- rejects placeholder-looking values before any external call;
- calls only embedding endpoints;
- prints only sanitized JSON metadata and vector lengths.
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
OFFICIAL_LOCAL_CONFIG = pathlib.Path.home() / ".config" / "video-factory" / "formal_api_demo.local.toml"
LEGACY_REPO_LOCAL_CONFIG = ROOT / "config" / "formal_api_demo.local.toml"
DEFAULT_MODEL = "text-embedding-v4"
DEFAULT_DIMENSIONS = 1024
COMPATIBLE_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings"
NATIVE_ENDPOINT = (
    "https://dashscope.aliyuncs.com/api/v1/services/embeddings/"
    "text-embedding/text-embedding"
)
TEST_TEXTS = [
    "视频工厂当前是 OPC 一人公司 AI 闭环验证系统，Codex 是唯一写入执行层。",
    "MISSING_REPORT 只能证明缺失已识别，不能放行真实执行。",
]
ENV_NAMES = (
    "DASHSCOPE_API_KEY",
    "BAILIAN_API_KEY",
    "ALIYUN_BAILIAN_API_KEY",
    "ALIYUN_API_KEY",
)
PLACEHOLDER_RE = re.compile(
    r"(^SET_|PLACEHOLDER|REPLACE|EXAMPLE|YOUR_|填入|填写|^XXX$|<.*>)",
    re.IGNORECASE,
)


def _resolve_default_config() -> pathlib.Path:
    env_override = os.environ.get("FORMAL_API_DEMO_LOCAL_CONFIG", "").strip()
    if env_override:
        return pathlib.Path(env_override).expanduser()
    if OFFICIAL_LOCAL_CONFIG.exists():
        return OFFICIAL_LOCAL_CONFIG
    return LEGACY_REPO_LOCAL_CONFIG


def _base_result(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "connector_created": True,
        "key_found": False,
        "key_source_type": "unknown",
        "key_variable_name": "",
        "key_value_printed": False,
        "selected_embedding_model": args.model,
        "requested_dimensions": args.dimensions,
        "endpoint_attempted": [],
        "api_auth_result": "not_attempted",
        "api_call_success": False,
        "openai_compatible_result": "not_attempted",
        "dashscope_native_result": "not_attempted",
        "vector_length_probe_1": None,
        "vector_length_probe_2": None,
        "dimension_consistent": False,
        "recommended_collection_dimension": None,
        "recommended_metric": "Cosine",
        "recommended_vector_type": "FLOAT",
        "dashvector_collection_created": False,
        "dashvector_written": False,
        "full_vector_printed": False,
        "blocked_status": None,
        "likely_reason": [],
        "next_required_user_action": "",
    }


def _is_placeholder(value: str) -> bool:
    return not value.strip() or bool(PLACEHOLDER_RE.search(value.strip()))


def _read_auth_api_key(config_path: pathlib.Path) -> str:
    if not config_path.exists():
        return ""
    in_auth = False
    for raw_line in config_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if re.match(r"^\[[^\]]+\]$", line):
            in_auth = line == "[auth]"
            continue
        if in_auth:
            match = re.match(r"^api_key\s*=\s*(.*?)\s*(?:#.*)?$", line)
            if match:
                return match.group(1).strip().strip('"').strip("'")
    return ""


def load_key(config_path: pathlib.Path) -> tuple[str, str, str, bool]:
    for env_name in ENV_NAMES:
        value = os.environ.get(env_name, "").strip()
        if value:
            return value, "process_env", env_name, _is_placeholder(value)

    runtime_key = _read_auth_api_key(config_path)
    if runtime_key:
        return runtime_key, "local_runtime_config", "[auth].api_key", _is_placeholder(runtime_key)

    return "", "unknown", "", False


def _safe_error(data: dict[str, Any], status_code: int | None) -> dict[str, Any]:
    error = data.get("error") if isinstance(data.get("error"), dict) else {}
    code = data.get("code") or error.get("code")
    message = data.get("message") or error.get("message")
    error_type = error.get("type") or data.get("code")
    return {
        "http_status": status_code,
        "api_error_code": code,
        "api_error_type": error_type,
        "api_error_message_preview": str(message or "")[:160],
    }


def _post_json(url: str, api_key: str, payload: dict[str, Any]) -> tuple[int | None, dict[str, Any]]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=40) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            data = {"message": body[:160]}
        return exc.code, data
    except Exception as exc:  # noqa: BLE001 - sanitized diagnostic only.
        return None, {"code": type(exc).__name__, "message": type(exc).__name__}


def _extract_compatible_vector(data: dict[str, Any]) -> list[float] | None:
    rows = data.get("data") or []
    if not rows or not isinstance(rows[0], dict):
        return None
    vector = rows[0].get("embedding")
    if isinstance(vector, list) and all(isinstance(item, (int, float)) for item in vector):
        return vector
    return None


def _extract_native_vector(data: dict[str, Any]) -> list[float] | None:
    rows = (data.get("output") or {}).get("embeddings") or []
    if not rows or not isinstance(rows[0], dict):
        return None
    vector = rows[0].get("embedding")
    if isinstance(vector, list) and all(isinstance(item, (int, float)) for item in vector):
        return vector
    return None


def _blocked_from_http(status: int | None, data: dict[str, Any]) -> str:
    code = str(data.get("code") or (data.get("error") or {}).get("code") or "")
    text = json.dumps(data, ensure_ascii=False)
    if status == 401:
        return "blocked_embedding_auth_failed_401"
    if status == 403:
        return "blocked_embedding_forbidden_403"
    if status == 404 or "model" in code.lower() or "model" in text.lower():
        return "blocked_embedding_model_unavailable"
    return "blocked_embedding_connector_missing"


def probe_compatible(api_key: str, model: str, dimensions: int) -> dict[str, Any]:
    lengths: list[int] = []
    for text in TEST_TEXTS:
        status, data = _post_json(
            COMPATIBLE_ENDPOINT,
            api_key,
            {
                "model": model,
                "input": text,
                "encoding_format": "float",
                "dimensions": dimensions,
            },
        )
        if status is None or status >= 400:
            return {
                "ok": False,
                "blocked_status": _blocked_from_http(status, data),
                "safe_error": _safe_error(data, status),
            }
        vector = _extract_compatible_vector(data)
        if vector is None:
            return {
                "ok": False,
                "blocked_status": "blocked_embedding_vector_missing",
                "safe_error": {"http_status": status, "api_error_code": "embedding_vector_missing"},
            }
        lengths.append(len(vector))
    return {"ok": True, "lengths": lengths}


def probe_native(api_key: str, model: str, dimensions: int) -> dict[str, Any]:
    lengths: list[int] = []
    for text in TEST_TEXTS:
        status, data = _post_json(
            NATIVE_ENDPOINT,
            api_key,
            {
                "model": model,
                "input": {"texts": [text]},
                "parameters": {"dimension": dimensions, "output_type": "dense"},
            },
        )
        if status is None or status >= 400:
            return {
                "ok": False,
                "blocked_status": _blocked_from_http(status, data),
                "safe_error": _safe_error(data, status),
            }
        vector = _extract_native_vector(data)
        if vector is None:
            return {
                "ok": False,
                "blocked_status": "blocked_embedding_vector_missing",
                "safe_error": {"http_status": status, "api_error_code": "embedding_vector_missing"},
            }
        lengths.append(len(vector))
    return {"ok": True, "lengths": lengths}


def _auth_failure_reasons() -> list[str]:
    return [
        "旧 MiniMax 代理 key 可能不适用于标准 DashScope embedding。",
        "key 所属地域 / workspace 可能与当前 endpoint 不一致。",
        "key 可能已过期或权限未覆盖 text-embedding-v4。",
        "本地配置可能仍是占位或旧 key，不是当前百炼控制台最新 key。",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Probe DashScope embedding dimensions without leaking secrets."
    )
    parser.add_argument("--model", default=os.environ.get("EMBEDDING_MODEL") or DEFAULT_MODEL)
    parser.add_argument("--dimensions", type=int, default=DEFAULT_DIMENSIONS)
    parser.add_argument("--config", type=pathlib.Path, default=_resolve_default_config())
    parser.add_argument(
        "--endpoint",
        choices=("compatible", "native", "both"),
        default="both",
    )
    args = parser.parse_args()

    result = _base_result(args)
    api_key, source_type, variable_name, placeholder = load_key(args.config)
    result["key_source_type"] = source_type
    result["key_variable_name"] = variable_name

    if not api_key or placeholder:
        result["key_found"] = False
        result["blocked_status"] = "blocked_local_runtime_key_read_failed"
        result["likely_reason"] = [
            "未读取到可用百炼 key，或本地配置字段仍是 SET_ / placeholder 占位值。"
        ]
        result["next_required_user_action"] = (
            "把可调用 DashScope embedding 的百炼 API Key 写入本地 "
            "config/formal_api_demo.local.toml 的 [auth].api_key，"
            "或临时导出 DASHSCOPE_API_KEY。"
        )
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0

    result["key_found"] = True

    endpoint_order = []
    if args.endpoint in ("compatible", "both"):
        endpoint_order.append(("compatible", probe_compatible))
    if args.endpoint in ("native", "both"):
        endpoint_order.append(("native", probe_native))

    last_failure: dict[str, Any] | None = None
    for name, probe in endpoint_order:
        result["endpoint_attempted"].append(name)
        attempt = probe(api_key, args.model, args.dimensions)
        if attempt.get("ok"):
            lengths = attempt["lengths"]
            result["api_auth_result"] = "success"
            result["api_call_success"] = True
            result["vector_length_probe_1"] = lengths[0]
            result["vector_length_probe_2"] = lengths[1]
            result["dimension_consistent"] = lengths[0] == lengths[1]
            result["recommended_collection_dimension"] = (
                lengths[0] if result["dimension_consistent"] else None
            )
            result["blocked_status"] = (
                None if result["dimension_consistent"] else "blocked_dimension_inconsistent"
            )
            endpoint_result = "success"
            if name == "compatible":
                result["openai_compatible_result"] = endpoint_result
            else:
                result["dashscope_native_result"] = endpoint_result
            print(json.dumps(result, ensure_ascii=False, sort_keys=True))
            return 0

        last_failure = attempt
        endpoint_result = attempt.get("blocked_status", "failed")
        if name == "compatible":
            result["openai_compatible_result"] = endpoint_result
        else:
            result["dashscope_native_result"] = endpoint_result

    blocked_status = (
        str(last_failure.get("blocked_status"))
        if last_failure
        else "blocked_embedding_connector_missing"
    )
    result["blocked_status"] = blocked_status
    result["api_call_success"] = False
    result["api_auth_result"] = (
        "401" if blocked_status == "blocked_embedding_auth_failed_401" else "failed"
    )
    if last_failure and isinstance(last_failure.get("safe_error"), dict):
        result["safe_error"] = last_failure["safe_error"]
    if blocked_status in {"blocked_embedding_auth_failed_401", "blocked_embedding_forbidden_403"}:
        result["likely_reason"] = _auth_failure_reasons()
        result["next_required_user_action"] = (
            "需要更新或提供一个确认可调用 text-embedding-v4 的 DashScope/百炼 API Key。"
        )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
