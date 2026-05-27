#!/usr/bin/env python3
from __future__ import annotations

from typing import Any


DEFAULT_TTS_PROVIDER_FOR_PUBLISH_CANDIDATE = "minimax"
REQUIRED_MINIMAX_MODELS = {"speech-2.8-hd", "MiniMax/speech-2.8-hd"}
OLD_ALIYUN_QWEN_B_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
OLD_ALIYUN_QWEN_B_ROUTE = "aliyun_qwen_realtime_websocket_voice_clone"
OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID = "qwen-t...ac19"
MINIMAX_B_TARGET_MODEL = "MiniMax/speech-2.8-hd"
MINIMAX_SELECTED_ROUTES = {
    "minimax_official_api",
    "aliyun_bailian_proxy_to_minimax",
    "route_a",
    "route_b",
}
B_VOICE_SCHEME_ROLE = {
    "status": "old_b_to_minimax_migration_pending_minimax_official_auth",
    "meaning": "旧阿里 / Qwen B 只作为 reference anchor；正式目标供应商为 MiniMax reference audio / voice clone 生成的声音身份",
    "not_allowed": "不得恢复旧 Qwen 为正式默认路线，不得用 MiniMax 系统 voice_id、voice_feel_tags 或男声候选冒充旧 B",
    "next_route": "route_b_migrate_old_b_to_minimax_after_minimax_official_auth",
}
REQUIRED_B_VOICE_GENDER_DIRECTION = "male_or_male_leaning"
FORBIDDEN_B_VOICE_IDS = {
    "female-tianmei",
    "female-shaonv",
    "female-shaonv-jingpin",
    "female-yujie",
}
FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS = {
    *FORBIDDEN_B_VOICE_IDS,
    "male-qn-qingse",
    "male-qn-daxuesheng",
    "Chinese (Mandarin)_Gentleman",
    "Chinese (Mandarin)_Gentle_Youth",
    "Chinese (Mandarin)_Sincere_Adult",
}
OLD_ALIYUN_QWEN_B_VOICE_ROUTE = {
    "status": "reference_anchor_only_for_minimax_migration",
    "role": "reference_anchor_only",
    "provider": "aliyun_bailian",
    "api_route_family": OLD_ALIYUN_QWEN_B_ROUTE,
    "request_method": "WEBSOCKET",
    "model": OLD_ALIYUN_QWEN_B_MODEL,
    "target_model": OLD_ALIYUN_QWEN_B_MODEL,
    "voice_identity_kind": "aliyun_qwen_custom_voice_masked",
    "custom_voice_masked_id": OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID,
    "voice_resolution": "list_existing_custom_voices_match_suffix_ac19",
    "create_model": "qwen-voice-enrollment",
    "create_custom_voice_called_in_20260427_trial": False,
    "reference_audio_paths": [
        "dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav",
        "dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav",
    ],
    "evidence_paths": [
        "codex_log/20260427_十五秒文案语速停顿试配.md",
        "dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/run_summary.json",
        "dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_voice_clone_tts_request_debug_sanitized.json",
        "dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/custom_voice_list_debug_sanitized.json",
        "scripts/语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis.py",
        "scripts/生成新第四期选品初筛源比例无遮挡B语音修复候选片_generate_new_fourth_selection_source_ratio_no_mask_b_voice_fix_candidate.py",
    ],
    "publish_candidate_completion_status": "not_selected_as_formal_route_user_current_instruction",
    "formal_route_selected": False,
}
OLD_B_FORBIDDEN_REPLACEMENT_RULE = {
    "status": "active",
    "system_voice_candidates_cannot_replace_old_b": True,
    "old_b_voice_route": OLD_ALIYUN_QWEN_B_VOICE_ROUTE,
    "forbidden_voice_ids": sorted(FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS),
    "forbidden_replacement_rule": [
        "female-tianmei cannot replace old B",
        "female-shaonv cannot replace old B",
        "female-shaonv-jingpin cannot replace old B",
        "female-yujie cannot replace old B",
        "MiniMax male or neutral system voice candidates cannot directly replace old B",
        "Only a MiniMax voice cloned or generated from the old-B reference audio and confirmed by user can become new B",
    ],
}
OLD_B_REFERENCE_AUDIO_PATHS = [
    "dist/voice_trials/20260427_十五秒文案语速停顿试配_15s_copy_pacing_trial/B_15秒文案_停顿梗感.wav",
    "dist/voice_trials/20260426_语音样本2复刻与文案风格解析_voice_sample2_clone_style_analysis/语音样本2_声音复刻试听_15秒.wav",
]
OLD_B_TO_MINIMAX_MIGRATION_ROUTE = {
    "status": "pending_minimax_official_auth",
    "selected_route": "route_b_migrate_old_b_to_minimax",
    "old_qwen_role": "reference_anchor_only",
    "minimax_role": "final_generation_provider",
    "target_provider": "minimax",
    "target_model": MINIMAX_B_TARGET_MODEL,
    "system_voice_candidates_allowed": False,
    "old_qwen_formal_route_allowed": False,
    "requires_reference_audio_access": True,
    "current_bailian_proxy_requires_audio_url": True,
    "official_minimax_supports_file_upload_for_voice_clone": True,
    "official_minimax_file_upload_required_for_clone": True,
    "oss_audio_url_not_sufficient_for_official_clone": True,
    "reference_audio_upload_authorization_received": True,
    "reference_audio_upload_requires_user_authorization": False,
    "blocked_if": [
        "minimax_official_api_key_missing",
        "minimax_file_id_missing",
        "generated_minimax_voice_id_missing",
        "system_voice_candidate_used_as_old_b",
        "old_qwen_route_selected_as_formal_route",
        "human_voice_review_status_not_user_confirmed",
    ],
}
OLD_B_TO_MINIMAX_VOICE_LOCK_RULE = {
    "status": "pending_minimax_official_auth",
    "old_b_reference_audio_path": OLD_B_REFERENCE_AUDIO_PATHS,
    "old_b_reference_voice_masked_id": OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID,
    "target_provider": "minimax",
    "target_model": MINIMAX_B_TARGET_MODEL,
    "generated_minimax_voice_id": None,
    "timbre_similarity_required": True,
    "prosody_optimization_allowed": True,
    "emotion_optimization_allowed": True,
    "timbre_change_allowed": False,
    "system_voice_substitution_allowed": False,
    "human_voice_review_required": True,
    "human_voice_review_status": "pending_minimax_official_auth",
}
FORBIDDEN_B_VOICE_DIRECTIONS = [
    "female_system_voice",
    "childish_cute_voice",
    "broadcast_voice",
    "sales_voice",
]
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
B_VOICE_IDENTITY_LOCK_RULE = {
    "status": "pending_user_review",
    "required_provider": "minimax",
    "required_model": "speech-2.8-hd",
    "lock_status_values": ["pending_user_review", "user_confirmed"],
    "expected_b_minimax_voice_id": None,
    "required_gender_direction": REQUIRED_B_VOICE_GENDER_DIRECTION,
    "expected_b_voice_reference_audio_path": OLD_B_REFERENCE_AUDIO_PATHS,
    "timbre_change_allowed": False,
    "emotion_optimization_allowed": True,
    "prosody_optimization_allowed": True,
    "human_voice_review_required": True,
    "human_voice_review_status": "pending_user_review",
    "forbidden_voice_ids": sorted(FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS),
    "forbidden_voice_direction": FORBIDDEN_B_VOICE_DIRECTIONS,
    "blocked_if": [
        "expected_b_minimax_voice_id_missing",
        "actual_voice_id_mismatch_expected_b_minimax_voice_id",
        "actual_voice_id_in_forbidden_voice_ids",
        "actual_gender_direction_missing",
        "actual_gender_direction_mismatch_required_gender_direction",
        "human_voice_review_status_not_user_confirmed",
        "timbre_change_allowed_true",
    ],
}
USER_CONFIRMED_VOICE_STATUS = "user_confirmed"
PENDING_USER_REVIEW_STATUS = "pending_user_review"
PENDING_REFERENCE_AUDIO_URL_STATUS = "pending_reference_audio_url"
PENDING_MINIMAX_OFFICIAL_AUTH_STATUS = "pending_minimax_official_auth"
FORBIDDEN_DEFAULT_B_VOICE_IDS = set(FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS)


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
    candidates: list[dict[str, Any]] = []
    seen: set[int] = set()

    def collect(node: dict[str, Any]) -> None:
        node_id = id(node)
        if node_id in seen:
            return
        seen.add(node_id)
        candidates.append(node)
        for key in [
            "tts_route_report",
            "tts",
            "voice_route",
            "validation",
            "media_probe",
            "narration",
            "narration_tts_debug_sanitized",
            "voice_setting",
            "actual_voice_setting",
            "b_voice_identity_lock",
            "voice_identity_gate",
            "locked_voice_setting",
            "old_b_to_minimax_voice_lock",
            "minimax_reference_clone_capability",
            "route_arbitration",
        ]:
            nested = node.get(key)
            if isinstance(nested, dict):
                collect(nested)

    collect(payload)
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


def _set_values(payloads: list[dict[str, Any]], keys: list[str], default: set[str] | None = None) -> set[str]:
    values = set(default or set())
    values.update(_list_values(payloads, keys))
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
        "old_aliyun_qwen_b_voice_route": OLD_ALIYUN_QWEN_B_VOICE_ROUTE,
        "old_b_forbidden_replacement_rule": OLD_B_FORBIDDEN_REPLACEMENT_RULE,
        "old_b_to_minimax_migration_route": OLD_B_TO_MINIMAX_MIGRATION_ROUTE,
    }
    return report


def _voice_identity_from_payloads(payloads: list[dict[str, Any]]) -> str:
    actual_voice_setting = _first_value(payloads, ["actual_voice_setting", "voice_setting"]) or {}
    voice_value = _first_value(
        payloads,
        [
            "actual_voice_id",
            "actual_b_voice_id",
            "custom_voice_masked_id",
            "custom_voice_masked",
            "voice_masked",
            "voice_id_masked",
            "voice_id",
        ],
    )
    if not voice_value and isinstance(actual_voice_setting, dict):
        voice_value = actual_voice_setting.get("voice_id")
    return str(voice_value or "")


def _is_old_aliyun_qwen_b_voice_identity(value: str) -> bool:
    normalized = value.strip()
    return normalized == OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID or normalized.endswith("ac19")


def build_old_aliyun_b_voice_restoration_report(tts_map: Any, summary: Any) -> dict[str, Any]:
    payloads: list[dict[str, Any]] = []
    for source in [tts_map, summary]:
        payloads.extend(_nested_payloads(source))

    route_report = build_tts_route_report(tts_map, summary)
    voice_identity = _voice_identity_from_payloads(payloads)
    provider_ok = route_report["actual_tts_provider"] == "aliyun_bailian"
    model_ok = route_report["actual_tts_model"] == OLD_ALIYUN_QWEN_B_MODEL
    route_ok = route_report["selected_route"] == OLD_ALIYUN_QWEN_B_ROUTE
    voice_ok = _is_old_aliyun_qwen_b_voice_identity(voice_identity)
    old_b_route_detected = provider_ok and model_ok and route_ok and voice_ok

    return {
        "old_b_voice_route": OLD_ALIYUN_QWEN_B_VOICE_ROUTE,
        "old_b_voice_exists": True,
        "old_b_voice_model": OLD_ALIYUN_QWEN_B_MODEL,
        "old_b_voice_masked_id": OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID,
        "actual_provider": route_report["actual_tts_provider"],
        "actual_model": route_report["actual_tts_model"],
        "actual_route": route_report["selected_route"],
        "actual_voice_identity": voice_identity,
        "provider_matches_old_b": provider_ok,
        "model_matches_old_b": model_ok,
        "route_matches_old_b": route_ok,
        "voice_identity_matches_old_b": voice_ok,
        "old_b_route_detected": old_b_route_detected,
        "can_old_b_voice_run_on_minimax_directly": False,
        "old_qwen_role": "reference_anchor_only",
        "minimax_role": "final_generation_provider",
        "can_qwen_old_b_route_be_restored_for_publish_candidate": "not_selected_user_current_instruction_reference_only",
        "publish_candidate_completion_status": "not_selected_as_formal_route_user_current_instruction",
        "next_route": "route_b_migrate_old_b_to_minimax",
        "system_voice_candidates_cannot_replace_old_b": True,
        "forbidden_voice_ids": sorted(FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS),
    }


def validate_old_b_voice_replacement_rule(tts_map: Any, summary: Any) -> dict[str, Any]:
    report = build_old_aliyun_b_voice_restoration_report(tts_map, summary)
    reasons: list[str] = []
    actual_voice_identity = str(report["actual_voice_identity"])

    if actual_voice_identity in FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS:
        reasons.append("system_voice_candidate_cannot_replace_old_b")
    if report["actual_provider"] in {"minimax", "minimax_official_api", "aliyun_bailian_proxy_to_minimax"}:
        if actual_voice_identity and actual_voice_identity != OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID:
            reasons.append("minimax_voice_id_cannot_equal_old_aliyun_b")
        if _is_old_aliyun_qwen_b_voice_identity(actual_voice_identity):
            reasons.append("qwen_t_ac19_cannot_be_minimax_voice_id")
    if not report["old_b_route_detected"]:
        reasons.append("old_aliyun_qwen_b_route_not_detected")

    if report["old_b_route_detected"] and not reasons:
        validation = "old_b_reference_anchor_detected_not_formal_route"
    elif "system_voice_candidate_cannot_replace_old_b" in reasons:
        validation = "blocked_system_voice_replacement_for_old_b"
    else:
        validation = "blocked_old_b_route_not_detected"

    return {
        **report,
        "old_b_voice_replacement_validation": validation,
        "blocked_reasons": sorted(set(reasons)),
    }


def build_old_b_to_minimax_voice_lock_report(tts_map: Any, summary: Any) -> dict[str, Any]:
    payloads: list[dict[str, Any]] = []
    for source in [tts_map, summary]:
        payloads.extend(_nested_payloads(source))

    route_report = build_tts_route_report(tts_map, summary)
    actual_voice_id = _voice_identity_from_payloads(payloads)
    target_provider = str(_first_value(payloads, ["target_provider"]) or "minimax")
    target_model = str(_first_value(payloads, ["target_model"]) or MINIMAX_B_TARGET_MODEL)
    generated_minimax_voice_id = str(
        _first_value(payloads, ["generated_minimax_voice_id", "target_minimax_voice_id"]) or ""
    )
    old_b_reference_voice_masked_id = str(
        _first_value(payloads, ["old_b_reference_voice_masked_id", "old_b_voice_masked_id"])
        or OLD_ALIYUN_QWEN_B_MASKED_VOICE_ID
    )
    requires_audio_url_value = _first_value(payloads, ["requires_audio_url", "need_public_accessible_url"])
    requires_audio_url = True if requires_audio_url_value is None else truthy(requires_audio_url_value)
    requires_file_id_value = _first_value(payloads, ["requires_file_id", "official_minimax_file_upload_required_for_clone"])
    requires_file_id = True if requires_file_id_value is None else truthy(requires_file_id_value)
    current_audio_url_available = _any_truthy(
        payloads,
        ["current_audio_url_available", "reference_audio_url_available", "audio_url_available"],
    )
    current_file_id_available = _any_truthy(
        payloads,
        ["current_file_id_available", "reference_audio_file_id_available", "file_id_created", "minimax_file_id_available"],
    )
    reference_audio_upload_authorized = _any_truthy(
        payloads,
        ["reference_audio_upload_authorized", "user_authorized_reference_audio_upload", "upload_authorized"],
    )
    official_minimax_api_key_value = _first_value(
        payloads,
        ["official_minimax_api_key_available", "minimax_official_api_key_available", "minimax_api_key_available"],
    )
    official_minimax_api_key_available = (
        None if official_minimax_api_key_value is None else truthy(official_minimax_api_key_value)
    )
    accepts_local_file_directly_value = _first_value(payloads, ["accepts_local_file_directly"])
    accepts_local_file_directly = False if accepts_local_file_directly_value is None else truthy(accepts_local_file_directly_value)
    human_review_required_value = _first_value(payloads, ["human_voice_review_required"])
    human_review_required = True if human_review_required_value is None else truthy(human_review_required_value)
    human_review_status = _normalized_status(
        _first_value(payloads, ["human_voice_review_status"]),
        PENDING_REFERENCE_AUDIO_URL_STATUS,
    )
    lock_status = _normalized_status(_first_value(payloads, ["old_b_to_minimax_voice_lock_status", "status"]), PENDING_REFERENCE_AUDIO_URL_STATUS)
    timbre_change_allowed_value = _first_value(payloads, ["timbre_change_allowed"])
    timbre_change_allowed = False if timbre_change_allowed_value is None else truthy(timbre_change_allowed_value)
    system_voice_substitution_allowed_value = _first_value(payloads, ["system_voice_substitution_allowed"])
    system_voice_substitution_allowed = (
        False if system_voice_substitution_allowed_value is None else truthy(system_voice_substitution_allowed_value)
    )
    old_qwen_formal_route_allowed_value = _first_value(payloads, ["old_qwen_formal_route_allowed"])
    old_qwen_formal_route_allowed = (
        False if old_qwen_formal_route_allowed_value is None else truthy(old_qwen_formal_route_allowed_value)
    )

    return {
        "old_b_to_minimax_migration_route": OLD_B_TO_MINIMAX_MIGRATION_ROUTE,
        "old_b_to_minimax_voice_lock_rule": OLD_B_TO_MINIMAX_VOICE_LOCK_RULE,
        "status": lock_status,
        "old_qwen_role": "reference_anchor_only",
        "minimax_role": "final_generation_provider",
        "target_provider": target_provider,
        "target_model": target_model,
        "actual_tts_provider": route_report["actual_tts_provider"],
        "actual_tts_model": route_report["actual_tts_model"],
        "actual_voice_id": actual_voice_id,
        "generated_minimax_voice_id": generated_minimax_voice_id,
        "old_b_reference_audio_path": OLD_B_REFERENCE_AUDIO_PATHS,
        "old_b_reference_voice_masked_id": old_b_reference_voice_masked_id,
        "requires_audio_url": requires_audio_url,
        "requires_file_id": requires_file_id,
        "accepts_local_file_directly": accepts_local_file_directly,
        "current_audio_url_available": current_audio_url_available,
        "current_file_id_available": current_file_id_available,
        "official_minimax_api_key_available": official_minimax_api_key_available,
        "reference_audio_upload_authorized": reference_audio_upload_authorized,
        "timbre_similarity_required": True,
        "prosody_optimization_allowed": True,
        "emotion_optimization_allowed": True,
        "timbre_change_allowed": timbre_change_allowed,
        "system_voice_substitution_allowed": system_voice_substitution_allowed,
        "old_qwen_formal_route_allowed": old_qwen_formal_route_allowed,
        "human_voice_review_required": human_review_required,
        "human_voice_review_status": human_review_status,
        "forbidden_voice_ids": sorted(FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS),
    }


def validate_old_b_to_minimax_voice_lock(tts_map: Any, summary: Any) -> dict[str, Any]:
    report = build_old_b_to_minimax_voice_lock_report(tts_map, summary)
    reasons: list[str] = []

    actual_voice_id = str(report["actual_voice_id"])
    generated_minimax_voice_id = str(report["generated_minimax_voice_id"])
    target_provider = str(report["target_provider"]).strip().lower()
    target_model = str(report["target_model"])
    human_review_status = str(report["human_voice_review_status"])

    if target_provider != "minimax":
        reasons.append("target_provider_not_minimax")
    if target_model not in REQUIRED_MINIMAX_MODELS:
        reasons.append("target_model_not_minimax_speech_2_8_hd")
    if not generated_minimax_voice_id:
        reasons.append("generated_minimax_voice_id_missing")
    if generated_minimax_voice_id in FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS:
        reasons.append("system_voice_candidate_cannot_replace_old_b")
    if actual_voice_id in FORBIDDEN_OLD_B_REPLACEMENT_VOICE_IDS:
        reasons.append("system_voice_candidate_cannot_replace_old_b")
    if generated_minimax_voice_id and _is_old_aliyun_qwen_b_voice_identity(generated_minimax_voice_id):
        reasons.append("qwen_t_ac19_cannot_be_minimax_voice_id")
    if report["system_voice_substitution_allowed"]:
        reasons.append("system_voice_substitution_allowed_true")
    if report["old_qwen_formal_route_allowed"]:
        reasons.append("old_qwen_formal_route_selected")
    if report["timbre_change_allowed"]:
        reasons.append("timbre_change_allowed_true")
    if report["requires_audio_url"] and not (
        report["current_audio_url_available"] or report["reference_audio_upload_authorized"]
    ):
        reasons.append("reference_audio_url_or_upload_authorization_missing")
    if (
        report["requires_file_id"]
        and not report["current_file_id_available"]
        and not generated_minimax_voice_id
        and report["reference_audio_upload_authorized"]
    ):
        reasons.append("minimax_file_id_missing")
    if (
        report["official_minimax_api_key_available"] is False
        and not generated_minimax_voice_id
        and report["reference_audio_upload_authorized"]
    ):
        reasons.append("minimax_official_api_key_missing")
    if report["human_voice_review_required"] and human_review_status != USER_CONFIRMED_VOICE_STATUS:
        reasons.append("human_voice_review_status_not_user_confirmed")

    if "reference_audio_url_or_upload_authorization_missing" in reasons:
        validation = "blocked_need_reference_audio_url"
    elif "minimax_official_api_key_missing" in reasons:
        validation = "blocked_need_minimax_official_auth"
    elif reasons:
        validation = "blocked_old_b_to_minimax_voice_lock"
    else:
        validation = "passed_old_b_to_minimax_voice_lock"

    return {
        **report,
        "old_b_to_minimax_voice_lock_validation": validation,
        "blocked_reasons": sorted(set(reasons)),
    }


def _normalized_status(value: Any, default: str = PENDING_USER_REVIEW_STATUS) -> str:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return default


def build_b_voice_identity_lock_report(tts_map: Any, summary: Any) -> dict[str, Any]:
    payloads: list[dict[str, Any]] = []
    for source in [tts_map, summary]:
        payloads.extend(_nested_payloads(source))

    actual_voice_setting = _first_value(payloads, ["actual_voice_setting", "voice_setting"]) or {}
    actual_voice_id_value = _first_value(payloads, ["actual_voice_id", "actual_b_voice_id", "voice_id_masked"])
    if not actual_voice_id_value and isinstance(actual_voice_setting, dict):
        actual_voice_id_value = actual_voice_setting.get("voice_id")
    actual_voice_id = str(actual_voice_id_value or "")
    expected_voice_id = str(_first_value(payloads, ["expected_b_minimax_voice_id"]) or "")
    actual_gender_direction = str(
        _first_value(payloads, ["actual_gender_direction", "actual_voice_gender_direction", "gender_direction", "gender_label"])
        or ""
    )
    required_gender_direction = str(
        _first_value(payloads, ["required_gender_direction"]) or REQUIRED_B_VOICE_GENDER_DIRECTION
    )
    forbidden_voice_ids = _set_values(payloads, ["forbidden_voice_ids"], FORBIDDEN_DEFAULT_B_VOICE_IDS)
    lock_status_value = _first_value(payloads, ["voice_identity_lock_status", "b_voice_identity_lock_status"])
    if lock_status_value is None:
        for payload in payloads:
            if (
                "expected_b_minimax_voice_id" in payload
                and "human_voice_review_status" in payload
                and "status" in payload
            ):
                lock_status_value = payload.get("status")
                break
    lock_status = _normalized_status(lock_status_value)
    human_review_required_value = _first_value(payloads, ["human_voice_review_required"])
    human_review_required = True if human_review_required_value is None else truthy(human_review_required_value)
    human_review_status = _normalized_status(_first_value(payloads, ["human_voice_review_status"]))
    timbre_change_allowed_value = _first_value(payloads, ["timbre_change_allowed"])
    timbre_change_allowed = False if timbre_change_allowed_value is None else truthy(timbre_change_allowed_value)

    return {
        "b_voice_identity_lock_rule": B_VOICE_IDENTITY_LOCK_RULE,
        "voice_identity_lock_status": lock_status,
        "expected_b_minimax_voice_id": expected_voice_id,
        "actual_voice_id": actual_voice_id,
        "actual_gender_direction": actual_gender_direction,
        "required_gender_direction": required_gender_direction,
        "actual_voice_setting": actual_voice_setting,
        "human_voice_review_required": human_review_required,
        "human_voice_review_status": human_review_status,
        "timbre_change_allowed": timbre_change_allowed,
        "emotion_optimization_allowed": True,
        "prosody_optimization_allowed": True,
        "forbidden_voice_ids": sorted(forbidden_voice_ids),
        "forbidden_default_voice_ids_without_user_confirmation": sorted(FORBIDDEN_DEFAULT_B_VOICE_IDS),
    }


def validate_minimax_b_voice_identity_lock(tts_map: Any, summary: Any) -> dict[str, Any]:
    report = build_b_voice_identity_lock_report(tts_map, summary)
    reasons: list[str] = []

    if is_internal_diagnostic_only(tts_map, summary):
        return {
            **report,
            "voice_identity_gate_validation": "internal_diagnostic_only",
            "blocked_reasons": [],
        }

    actual_voice_id = str(report["actual_voice_id"])
    expected_voice_id = str(report["expected_b_minimax_voice_id"])
    actual_gender_direction = str(report["actual_gender_direction"])
    required_gender_direction = str(report["required_gender_direction"])
    forbidden_voice_ids = set(report["forbidden_voice_ids"])
    human_review_status = str(report["human_voice_review_status"])
    lock_status = str(report["voice_identity_lock_status"])

    if not expected_voice_id:
        reasons.append("expected_b_minimax_voice_id_missing")
    if not actual_voice_id:
        reasons.append("actual_voice_id_missing")
    if actual_voice_id in forbidden_voice_ids:
        reasons.append("actual_voice_id_in_forbidden_voice_ids")
    if actual_voice_id == "female-tianmei" and human_review_status != USER_CONFIRMED_VOICE_STATUS:
        reasons.append("female_tianmei_used_without_user_confirmation")
    if expected_voice_id and actual_voice_id and actual_voice_id != expected_voice_id:
        reasons.append("actual_voice_id_mismatch_expected_b_minimax_voice_id")
    if required_gender_direction:
        if not actual_gender_direction:
            reasons.append("actual_gender_direction_missing")
        elif actual_gender_direction != required_gender_direction:
            reasons.append("actual_gender_direction_mismatch_required_gender_direction")
    if report["timbre_change_allowed"]:
        reasons.append("timbre_change_allowed_true")
    if report["human_voice_review_required"] and human_review_status != USER_CONFIRMED_VOICE_STATUS:
        reasons.append("human_voice_review_status_not_user_confirmed")
    if lock_status != USER_CONFIRMED_VOICE_STATUS:
        reasons.append("voice_identity_lock_status_not_user_confirmed")

    return {
        **report,
        "voice_identity_gate_validation": "passed_b_voice_identity_lock" if not reasons else "blocked_b_voice_identity_lock",
        "blocked_reasons": sorted(set(reasons)),
    }


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
    identity_validation = validate_minimax_b_voice_identity_lock(tts_map, summary)
    reasons = list(validation.get("blocked_reasons", []))

    if validation.get("voice_route_validation") != "internal_diagnostic_only":
        if not validation.get("b_voice_feel_reflected"):
            reasons.append("b_voice_feel_not_reflected")
        if validation.get("missing_b_voice_feel_tags"):
            reasons.append("b_voice_feel_required_tags_missing")
        if identity_validation.get("voice_identity_gate_validation") != "passed_b_voice_identity_lock":
            reasons.extend(str(reason) for reason in identity_validation.get("blocked_reasons", []))

    if reasons:
        if (
            validation.get("voice_route_validation") == "passed_minimax"
            and identity_validation.get("voice_identity_gate_validation") == "blocked_b_voice_identity_lock"
        ):
            voice_route_validation = "blocked_b_voice_identity_lock"
        else:
            voice_route_validation = validation.get("voice_route_validation")
    else:
        voice_route_validation = "passed_minimax_b_voice_identity_lock"

    return {
        **validation,
        "b_voice_identity_lock": identity_validation,
        "voice_route_validation": voice_route_validation,
        "b_voice_feel_minimax_formal_voice_rule": B_VOICE_FEEL_MINIMAX_FORMAL_VOICE_RULE,
        "blocked_reasons": sorted(set(reasons)),
    }
