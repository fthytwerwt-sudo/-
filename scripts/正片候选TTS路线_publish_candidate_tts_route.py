#!/usr/bin/env python3
from __future__ import annotations

from typing import Any


DEFAULT_TTS_PROVIDER_FOR_PUBLISH_CANDIDATE = "minimax"
REQUIRED_MINIMAX_MODELS = {"speech-2.8-hd", "MiniMax/speech-2.8-hd"}
MINIMAX_SELECTED_ROUTES = {
    "minimax_official_api",
    "aliyun_bailian_proxy_to_minimax",
    "route_a",
    "route_b",
}
B_VOICE_SCHEME_ROLE = {
    "status": "formal_voice_feel_reference",
    "meaning": "B 方案升级为正式声音听感标准，保留停顿梗感、轻陪伴感和低压向导感",
    "not_allowed": "不再把阿里 B 方案作为正片候选默认 TTS 生成路线",
}
B_VOICE_FEEL_REQUIRED_TAGS = {
    "light_companion",
    "low_pressure",
    "natural_spoken_chinese",
    "b_pacing_feel",
    "subtle_pause_joke_rhythm",
    "game_guide_feeling",
    "not_broadcast",
    "not_sales",
    "not_customer_service",
    "not_childish_cute_voice",
}
B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE = {
    "status": "active",
    "b_voice_scheme_role": "formal_voice_feel_reference",
    "required_generation_route": {
        "provider_family": ["minimax", "aliyun_bailian_proxy_to_minimax"],
        "model": sorted(REQUIRED_MINIMAX_MODELS),
    },
    "required_voice_feel": sorted(B_VOICE_FEEL_REQUIRED_TAGS),
    "forbidden_generation_route": [
        "aliyun_qwen_realtime_websocket_voice_clone_as_publish_candidate",
        "qwen3-tts-vc-realtime-2026-01-15_as_publish_candidate",
        "Serena",
        "macOS_say",
        "local_low_quality_tts",
        "silent_audio",
        "unauthorized_fallback",
    ],
    "required_report": ["tts_route_report.json", "tts_route_report.md"],
    "blocked_if": [
        "actual_model_is_not_minimax_speech_2_8_hd",
        "fallback_used = true",
        "audio_missing = true",
        "non_silent = false",
        "b_voice_feel_not_reflected = true",
    ],
}


def truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "passed", "pass", "1"}
    return bool(value)


def flatten_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(flatten_text(item) for item in value)
    if isinstance(value, dict):
        return "\n".join(f"{key}:{flatten_text(item)}" for key, item in value.items())
    return str(value)


def _nested_payloads(payload: Any) -> list[dict[str, Any]]:
    if not isinstance(payload, dict):
        return []
    candidates = [payload]
    for key in [
        "tts_route_report",
        "tts",
        "voice_route",
        "validation",
        "media_probe",
        "narration",
        "narration_tts_debug_sanitized",
    ]:
        nested = payload.get(key)
        if isinstance(nested, dict):
            candidates.append(nested)
    return candidates


def _first_value(payloads: list[dict[str, Any]], keys: list[str]) -> Any:
    for payload in payloads:
        for key in keys:
            value = payload.get(key)
            if value not in ("", None, []):
                return value
    return None


def _any_truthy(payloads: list[dict[str, Any]], keys: list[str]) -> bool:
    return any(truthy(payload.get(key)) for payload in payloads for key in keys)


def _list_values(payloads: list[dict[str, Any]], keys: list[str]) -> list[str]:
    values: list[str] = []
    for payload in payloads:
        for key in keys:
            value = payload.get(key)
            if isinstance(value, list):
                values.extend(str(item) for item in value)
            elif isinstance(value, str) and value:
                values.append(value)
    return values


def _explicit_route_report_present(tts_map: Any, summary: Any) -> bool:
    return any(
        isinstance(payload, dict) and isinstance(payload.get("tts_route_report"), dict)
        for payload in [tts_map, summary]
    )


def is_internal_diagnostic_only(tts_map: Any, summary: Any) -> bool:
    text = flatten_text([tts_map, summary]).lower()
    publish_ready = any(
        truthy(payload.get("publish_candidate_ready_for_human_review"))
        for payload in [tts_map, summary]
        if isinstance(payload, dict)
    )
    return "internal_diagnostic_only" in text and not publish_ready


def is_publish_candidate_context(tts_map: Any, summary: Any) -> bool:
    if is_internal_diagnostic_only(tts_map, summary):
        return False
    text = flatten_text([tts_map, summary]).lower()
    if "publish_candidate" in text or "ready_for_human_review" in text:
        return True
    return True


def is_minimax_speech_2_8_hd(provider: str, model: str, selected_route: str, explicit_flag: Any = None) -> bool:
    if explicit_flag is not None:
        return truthy(explicit_flag)
    provider_normalized = provider.strip().lower()
    route_normalized = selected_route.strip()
    model_ok = model in REQUIRED_MINIMAX_MODELS
    provider_ok = provider_normalized in {
        "minimax",
        "minimax_official_api",
        "aliyun_bailian_proxy_to_minimax",
    }
    route_ok = route_normalized in MINIMAX_SELECTED_ROUTES
    return model_ok and (provider_ok or route_ok)


def build_tts_route_report(tts_map: Any, summary: Any) -> dict[str, Any]:
    payloads: list[dict[str, Any]] = []
    for source in [tts_map, summary]:
        payloads.extend(_nested_payloads(source))

    actual_provider = str(
        _first_value(payloads, ["actual_tts_provider", "actual_provider", "provider_used", "provider"]) or ""
    )
    actual_model = str(
        _first_value(
            payloads,
            ["actual_tts_model", "actual_model_name", "actual_model", "model_used", "model", "target_model"],
        )
        or ""
    )
    selected_route = str(_first_value(payloads, ["selected_route", "route", "api_route_family"]) or "")
    explicit_minimax_flag = _first_value(payloads, ["is_minimax_speech_2_8_hd", "is_real_minimax_speech_2_8_hd"])
    audio_present = _first_value(payloads, ["audio_present", "audio_generated"])
    non_silent = _first_value(payloads, ["non_silent"])
    if isinstance(_first_value(payloads, ["non_silent_check"]), dict):
        non_silent = _first_value(payloads, ["non_silent_check"]).get("passed")

    fallback_used = _any_truthy(
        payloads,
        [
            "fallback_tts_used",
            "fallback_used",
            "local_tts_fallback_used",
            "local_say_fallback_used",
            "macos_say_used",
            "silent_audio_fallback_used",
        ],
    )
    macos_say_used = _any_truthy(payloads, ["macos_say_used", "local_say_fallback_used"])
    local_low_quality_tts_used = _any_truthy(payloads, ["local_tts_fallback_used", "local_low_quality_tts_used"])
    voice_feel_tags = set(_list_values(payloads, ["voice_feel_tags", "required_voice_feel_used", "b_voice_feel_tags"]))
    explicit_b_voice_feel = _first_value(payloads, ["b_voice_feel_reflected", "used_b_voice_feel", "b_voice_feel_passed"])
    missing_b_voice_tags = sorted(B_VOICE_FEEL_REQUIRED_TAGS - voice_feel_tags)

    report = {
        "actual_tts_provider": actual_provider,
        "actual_tts_model": actual_model,
        "selected_route": selected_route,
        "is_minimax_speech_2_8_hd": is_minimax_speech_2_8_hd(
            actual_provider,
            actual_model,
            selected_route,
            explicit_minimax_flag,
        ),
        "minimax_authorization_source_masked": str(
            _first_value(payloads, ["minimax_authorization_source_masked", "auth_source_masked", "api_key_source", "tts_auth_source"])
            or "none"
        ),
        "api_key_printed": _any_truthy(payloads, ["api_key_printed", "key_printed"]),
        "api_key_written": _any_truthy(payloads, ["api_key_written", "key_written"]),
        "audio_present": truthy(audio_present),
        "non_silent": truthy(non_silent),
        "fallback_tts_used": fallback_used,
        "fallback_reason": str(_first_value(payloads, ["fallback_reason", "blocked_reason"]) or ""),
        "macos_say_used": macos_say_used,
        "local_low_quality_tts_used": local_low_quality_tts_used,
        "tts_route_report_present": _explicit_route_report_present(tts_map, summary),
        "b_voice_scheme_role": B_VOICE_SCHEME_ROLE,
        "b_voice_feel_reflected": truthy(explicit_b_voice_feel) or not missing_b_voice_tags,
        "voice_feel_tags": sorted(voice_feel_tags),
        "missing_b_voice_feel_tags": missing_b_voice_tags,
    }
    return report


def validate_publish_candidate_tts_route(tts_map: Any, summary: Any) -> dict[str, Any]:
    report = build_tts_route_report(tts_map, summary)
    reasons: list[str] = []
    publish_candidate = is_publish_candidate_context(tts_map, summary)

    if is_internal_diagnostic_only(tts_map, summary):
        return {
            **report,
            "publish_candidate_context": False,
            "voice_route_validation": "internal_diagnostic_only",
            "full_video_can_only_be_internal_diagnostic": True,
            "blocked_reasons": [],
        }

    if not report["tts_route_report_present"]:
        reasons.append("tts_route_report_missing")
    if not report["is_minimax_speech_2_8_hd"]:
        reasons.append("failed_non_minimax_voice")
        if report["actual_tts_provider"] and report["actual_tts_provider"] not in {
            "minimax",
            "minimax_official_api",
            "aliyun_bailian_proxy_to_minimax",
        }:
            reasons.append("actual_tts_provider_not_minimax")
        if report["actual_tts_model"] and report["actual_tts_model"] not in REQUIRED_MINIMAX_MODELS:
            reasons.append("actual_tts_model_not_speech_2_8_hd")
    if report["fallback_tts_used"]:
        reasons.append("fallback_tts_used_without_user_explicit_approval")
    if report["macos_say_used"]:
        reasons.append("macos_say_used_for_publish_candidate")
    if report["local_low_quality_tts_used"]:
        reasons.append("local_low_quality_tts_used_for_publish_candidate")
    if not report["audio_present"]:
        reasons.append("audio_not_generated_or_missing")
    if not report["non_silent"]:
        reasons.append("audio_missing_or_silent")
    if report["api_key_printed"] or report["api_key_written"]:
        reasons.append("api_key_printed_or_written")

    unavailable_markers = {"", "none", "unavailable"}
    if (
        report["is_minimax_speech_2_8_hd"]
        and (not report["audio_present"] or report["selected_route"] in unavailable_markers)
    ):
        voice_route_validation = "blocked_minimax_unavailable"
    elif reasons:
        voice_route_validation = "failed_non_minimax_voice"
    else:
        voice_route_validation = "passed_minimax"

    return {
        **report,
        "publish_candidate_context": publish_candidate,
        "voice_route_validation": voice_route_validation,
        "full_video_can_only_be_internal_diagnostic": bool(reasons),
        "blocked_reasons": sorted(set(reasons)),
    }


def validate_b_voice_feel_minimax_route(tts_map: Any, summary: Any) -> dict[str, Any]:
    validation = validate_publish_candidate_tts_route(tts_map, summary)
    reasons = list(validation.get("blocked_reasons", []))

    if validation.get("voice_route_validation") != "internal_diagnostic_only":
        if not validation.get("b_voice_feel_reflected"):
            reasons.append("b_voice_feel_not_reflected")
        if validation.get("missing_b_voice_feel_tags"):
            reasons.append("b_voice_feel_required_tags_missing")

    if reasons:
        voice_route_validation = validation.get("voice_route_validation")
    else:
        voice_route_validation = "passed_minimax_b_voice_feel"

    return {
        **validation,
        "voice_route_validation": voice_route_validation,
        "b_voice_feel_minimax_formal_voice_rule": B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE,
        "blocked_reasons": sorted(set(reasons)),
    }
