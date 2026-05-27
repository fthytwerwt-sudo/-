from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "正片候选TTS路线_publish_candidate_tts_route.py"
SPEC = importlib.util.spec_from_file_location("publish_candidate_tts_route", MODULE_PATH)
assert SPEC and SPEC.loader
route_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(route_module)


def _summary(status: str = "publish_candidate_ready_for_human_review") -> dict:
    return {
        "status": status,
        "publish_candidate_ready_for_human_review": status == "publish_candidate_ready_for_human_review",
    }


class PublishCandidateVoiceGateTests(unittest.TestCase):
    def test_publish_candidate_with_minimax_speech_2_8_hd_passes(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "is_minimax_speech_2_8_hd": True,
                    "audio_present": True,
                    "non_silent": True,
                    "fallback_tts_used": False,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "passed_minimax")
        self.assertEqual(result["blocked_reasons"], [])

    def test_publish_candidate_with_aliyun_qwen_tts_fails(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "selected_route": "aliyun_qwen_realtime_websocket_voice_clone",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "failed_non_minimax_voice")
        self.assertIn("failed_non_minimax_voice", result["blocked_reasons"])

    def test_publish_candidate_with_macos_say_fails(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "macos_say",
                    "actual_tts_model": "say",
                    "selected_route": "local",
                    "audio_present": True,
                    "non_silent": True,
                    "macos_say_used": True,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "failed_non_minimax_voice")
        self.assertIn("macos_say_used_for_publish_candidate", result["blocked_reasons"])

    def test_minimax_route_unavailable_blocks_publish_candidate(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "is_minimax_speech_2_8_hd": True,
                    "audio_present": False,
                    "non_silent": False,
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "blocked_minimax_unavailable")
        self.assertIn("audio_not_generated_or_missing", result["blocked_reasons"])

    def test_internal_diagnostic_can_use_non_minimax_only_if_not_publish_candidate(self) -> None:
        result = route_module.validate_publish_candidate_tts_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            {
                "status": "internal_diagnostic_only",
                "publish_candidate_ready_for_human_review": False,
            },
        )
        self.assertEqual(result["voice_route_validation"], "internal_diagnostic_only")
        self.assertIs(result["full_video_can_only_be_internal_diagnostic"], True)
        self.assertEqual(result["blocked_reasons"], [])

    def test_b_voice_feel_minimax_formal_voice_rule_passes_with_minimax_and_feel(self) -> None:
        result = route_module.validate_b_voice_feel_minimax_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "is_minimax_speech_2_8_hd": True,
                    "audio_present": True,
                    "non_silent": True,
                    "fallback_tts_used": False,
                    "b_voice_feel_reflected": True,
                    "actual_voice_id": "male-qn-qingse",
                    "actual_gender_direction": "male_or_male_leaning",
                    "actual_voice_setting": {
                        "voice_id": "male-qn-qingse",
                        "speed": 1.08,
                        "pitch": 0,
                        "emotion": "calm",
                        "vol": 1,
                    },
                    "b_voice_identity_lock": {
                        "status": "user_confirmed",
                        "expected_b_minimax_voice_id": "male-qn-qingse",
                        "required_gender_direction": "male_or_male_leaning",
                        "locked_voice_setting": {
                            "voice_id": "male-qn-qingse",
                            "speed": 1.08,
                            "pitch": 0,
                            "emotion": "calm",
                            "vol": 1,
                        },
                        "timbre_change_allowed": False,
                        "human_voice_review_required": True,
                        "human_voice_review_status": "user_confirmed",
                    },
                    "voice_feel_tags": [
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
                    ],
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "passed_minimax_b_voice_identity_lock")
        self.assertEqual(result["blocked_reasons"], [])
        self.assertEqual(
            result["b_voice_feel_minimax_formal_voice_rule"]["b_voice_scheme_role"],
            "formal_voice_feel_reference",
        )

    def test_old_qwen_b_voice_route_blocked_for_publish_candidate(self) -> None:
        result = route_module.validate_b_voice_feel_minimax_route(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "selected_route": "aliyun_qwen_realtime_websocket_voice_clone",
                    "audio_present": True,
                    "non_silent": True,
                    "b_voice_feel_reflected": True,
                    "voice_feel_tags": ["light_companion", "b_pacing_feel"],
                }
            },
            _summary(),
        )
        self.assertEqual(result["voice_route_validation"], "failed_non_minimax_voice")
        self.assertIn("actual_tts_provider_not_minimax", result["blocked_reasons"])

    def test_old_aliyun_qwen_b_voice_route_is_detected_but_requires_runtime_smoke(self) -> None:
        result = route_module.validate_old_b_voice_replacement_rule(
            {
                "tts_route_report": {
                    "actual_tts_provider": "aliyun_bailian",
                    "actual_tts_model": "qwen3-tts-vc-realtime-2026-01-15",
                    "selected_route": "aliyun_qwen_realtime_websocket_voice_clone",
                    "custom_voice_masked_id": "qwen-t...ac19",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            _summary(),
        )
        self.assertTrue(result["old_b_route_detected"])
        self.assertEqual(
            result["old_b_voice_replacement_validation"],
            "old_b_route_detected_pending_runtime_smoke",
        )
        self.assertEqual(result["next_route"], "route_a_restore_old_qwen_b")

    def test_minimax_system_voice_cannot_replace_old_aliyun_b_even_if_male(self) -> None:
        result = route_module.validate_old_b_voice_replacement_rule(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "actual_voice_id": "male-qn-qingse",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            _summary(),
        )
        self.assertEqual(
            result["old_b_voice_replacement_validation"],
            "blocked_system_voice_replacement_for_old_b",
        )
        self.assertIn("system_voice_candidate_cannot_replace_old_b", result["blocked_reasons"])
        self.assertIn("minimax_voice_id_cannot_equal_old_aliyun_b", result["blocked_reasons"])

    def test_qwen_masked_voice_id_cannot_be_used_as_minimax_voice_id(self) -> None:
        result = route_module.validate_old_b_voice_replacement_rule(
            {
                "tts_route_report": {
                    "actual_tts_provider": "minimax",
                    "actual_tts_model": "speech-2.8-hd",
                    "selected_route": "minimax_official_api",
                    "actual_voice_id": "qwen-t...ac19",
                    "audio_present": True,
                    "non_silent": True,
                }
            },
            _summary(),
        )
        self.assertEqual(result["old_b_voice_replacement_validation"], "blocked_old_b_route_not_detected")
        self.assertIn("qwen_t_ac19_cannot_be_minimax_voice_id", result["blocked_reasons"])


if __name__ == "__main__":
    unittest.main()
