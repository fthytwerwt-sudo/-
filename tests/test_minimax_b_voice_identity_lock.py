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


def _summary() -> dict:
    return {
        "status": "publish_candidate_ready_for_human_review",
        "publish_candidate_ready_for_human_review": True,
    }


def _base_tts_report(**extra: object) -> dict:
    payload = {
        "tts_route_report": {
            "actual_tts_provider": "minimax",
            "actual_tts_model": "speech-2.8-hd",
            "selected_route": "aliyun_bailian_proxy_to_minimax",
            "is_minimax_speech_2_8_hd": True,
            "audio_present": True,
            "non_silent": True,
            "fallback_tts_used": False,
            "b_voice_feel_reflected": True,
            "voice_feel_tags": sorted(route_module.B_VOICE_FEEL_REQUIRED_TAGS),
        }
    }
    payload["tts_route_report"].update(extra)
    return payload


class MinimaxBVoiceIdentityLockTests(unittest.TestCase):
    def test_feel_tags_only_do_not_pass_identity_lock(self) -> None:
        result = route_module.validate_b_voice_feel_minimax_route(_base_tts_report(), _summary())

        self.assertEqual(result["voice_route_validation"], "blocked_b_voice_identity_lock")
        self.assertIn("expected_b_minimax_voice_id_missing", result["blocked_reasons"])
        self.assertIn("human_voice_review_status_not_user_confirmed", result["blocked_reasons"])

    def test_female_tianmei_blocks_without_user_confirmation(self) -> None:
        result = route_module.validate_b_voice_feel_minimax_route(
            _base_tts_report(
                actual_voice_id="female-tianmei",
                actual_gender_direction="female_system_voice",
                b_voice_identity_lock={
                    "status": "pending_user_review",
                    "expected_b_minimax_voice_id": "female-tianmei",
                    "required_gender_direction": "male_or_male_leaning",
                    "human_voice_review_status": "pending_user_review",
                    "timbre_change_allowed": False,
                },
            ),
            _summary(),
        )

        self.assertIn("female_tianmei_used_without_user_confirmation", result["blocked_reasons"])
        self.assertIn("actual_voice_id_in_forbidden_voice_ids", result["blocked_reasons"])
        self.assertIn("actual_gender_direction_mismatch_required_gender_direction", result["blocked_reasons"])
        self.assertIn("voice_identity_lock_status_not_user_confirmed", result["blocked_reasons"])

    def test_previous_rejected_female_candidates_block_even_if_user_confirmed_payload_claims_passed(self) -> None:
        for voice_id in ["female-shaonv", "female-shaonv-jingpin", "female-yujie"]:
            with self.subTest(voice_id=voice_id):
                result = route_module.validate_minimax_b_voice_identity_lock(
                    _base_tts_report(
                        actual_voice_id=voice_id,
                        actual_gender_direction="female_system_voice",
                        b_voice_identity_lock={
                            "status": "user_confirmed",
                            "expected_b_minimax_voice_id": voice_id,
                            "required_gender_direction": "male_or_male_leaning",
                            "human_voice_review_status": "user_confirmed",
                            "timbre_change_allowed": False,
                        },
                    ),
                    _summary(),
                )

                self.assertEqual(result["voice_identity_gate_validation"], "blocked_b_voice_identity_lock")
                self.assertIn("actual_voice_id_in_forbidden_voice_ids", result["blocked_reasons"])
                self.assertIn("actual_gender_direction_mismatch_required_gender_direction", result["blocked_reasons"])

    def test_voice_id_mismatch_blocks(self) -> None:
        result = route_module.validate_minimax_b_voice_identity_lock(
            _base_tts_report(
                actual_voice_id="female-shaonv",
                actual_gender_direction="female_system_voice",
                b_voice_identity_lock={
                    "status": "user_confirmed",
                    "expected_b_minimax_voice_id": "female-yujie",
                    "required_gender_direction": "male_or_male_leaning",
                    "human_voice_review_status": "user_confirmed",
                    "timbre_change_allowed": False,
                },
            ),
            _summary(),
        )

        self.assertEqual(result["voice_identity_gate_validation"], "blocked_b_voice_identity_lock")
        self.assertIn("actual_voice_id_mismatch_expected_b_minimax_voice_id", result["blocked_reasons"])

    def test_user_confirmed_cloned_voice_id_passes_identity_lock(self) -> None:
        result = route_module.validate_b_voice_feel_minimax_route(
            _base_tts_report(
                actual_voice_id="bClone20260527Ac19V1",
                actual_gender_direction="male_or_male_leaning",
                actual_voice_setting={
                    "voice_id": "bClone20260527Ac19V1",
                    "speed": 1.08,
                    "pitch": 0,
                    "emotion": "calm",
                    "vol": 1,
                },
                b_voice_identity_lock={
                    "status": "user_confirmed",
                    "expected_b_minimax_voice_id": "bClone20260527Ac19V1",
                    "required_gender_direction": "male_or_male_leaning",
                    "locked_voice_setting": {
                        "voice_id": "bClone20260527Ac19V1",
                        "speed": 1.08,
                        "pitch": 0,
                        "emotion": "calm",
                        "vol": 1,
                    },
                    "human_voice_review_status": "user_confirmed",
                    "human_voice_review_required": True,
                    "timbre_change_allowed": False,
                },
            ),
            _summary(),
        )

        self.assertEqual(result["voice_route_validation"], "passed_minimax_b_voice_identity_lock")
        self.assertEqual(result["blocked_reasons"], [])

    def test_confirmed_old_b_minimax_v2_sample_passes_identity_lock(self) -> None:
        confirmed_voice_id = "oldBMinimax20260528010200"
        confirmed_sample_path = (
            "codex_log/diagnostics/old_b_to_minimax_bailian_20260528_010200/"
            "samples/V2_prosody_optimized.mp3"
        )
        result = route_module.validate_b_voice_feel_minimax_route(
            _base_tts_report(
                actual_voice_id=confirmed_voice_id,
                actual_gender_direction="male_or_male_leaning",
                actual_voice_setting={
                    "voice_id": confirmed_voice_id,
                    "speed": 1.02,
                    "pitch": 0,
                    "emotion": "neutral",
                    "vol": 1,
                },
                generated_minimax_voice_id=confirmed_voice_id,
                b_voice_identity_lock={
                    "status": "user_confirmed",
                    "expected_b_minimax_voice_id": confirmed_voice_id,
                    "selected_sample_version": "V2_prosody_optimized",
                    "selected_sample_path": confirmed_sample_path,
                    "required_gender_direction": "male_or_male_leaning",
                    "locked_voice_setting": {
                        "voice_id": confirmed_voice_id,
                        "speed": 1.02,
                        "pitch": 0,
                        "emotion": "neutral",
                        "vol": 1,
                    },
                    "human_voice_review_status": "user_confirmed",
                    "human_voice_review_required": True,
                    "timbre_change_allowed": False,
                },
            ),
            _summary(),
        )

        self.assertEqual(result["voice_route_validation"], "passed_minimax_b_voice_identity_lock")
        self.assertEqual(result["blocked_reasons"], [])
        self.assertEqual(
            route_module.B_VOICE_IDENTITY_LOCK_RULE["selected_sample_path"],
            confirmed_sample_path,
        )
        self.assertEqual(
            route_module.B_VOICE_IDENTITY_LOCK_RULE["selected_sample_scope"],
            "confirmed_exact_codex_generated_v2_sample_not_generic_v2",
        )

    def test_user_confirmed_male_system_voice_still_blocks_identity_lock(self) -> None:
        result = route_module.validate_minimax_b_voice_identity_lock(
            _base_tts_report(
                actual_voice_id="male-qn-qingse",
                actual_gender_direction="male_or_male_leaning",
                b_voice_identity_lock={
                    "status": "user_confirmed",
                    "expected_b_minimax_voice_id": "male-qn-qingse",
                    "required_gender_direction": "male_or_male_leaning",
                    "human_voice_review_status": "user_confirmed",
                    "timbre_change_allowed": False,
                },
            ),
            _summary(),
        )

        self.assertEqual(result["voice_identity_gate_validation"], "blocked_b_voice_identity_lock")
        self.assertIn("actual_voice_id_in_forbidden_voice_ids", result["blocked_reasons"])

    def test_male_minimax_candidate_still_cannot_replace_old_aliyun_b(self) -> None:
        result = route_module.validate_old_b_voice_replacement_rule(
            _base_tts_report(
                actual_voice_id="Chinese (Mandarin)_Gentleman",
                actual_gender_direction="male_or_male_leaning",
            ),
            _summary(),
        )

        self.assertEqual(
            result["old_b_voice_replacement_validation"],
            "blocked_system_voice_replacement_for_old_b",
        )
        self.assertIn("system_voice_candidate_cannot_replace_old_b", result["blocked_reasons"])


if __name__ == "__main__":
    unittest.main()
