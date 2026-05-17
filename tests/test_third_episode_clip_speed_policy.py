import importlib.util
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = next((ROOT / "scripts").glob("*third_episode_real_review_scene_candidate.py"))


def load_candidate_module():
    spec = importlib.util.spec_from_file_location("third_episode_candidate", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class ThirdEpisodeClipSpeedPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_candidate_module()

    def test_locked_evidence_window_is_not_compressed_to_tts_duration(self) -> None:
        policy = self.module.resolve_clip_speed_policy(
            {
                "source_material": "material_03",
                "evidence_strength": "high",
                "evidence_window_lock": True,
            },
            source_duration=36.0,
            target_duration=4.78,
        )

        self.assertEqual(policy["speed_factor"], 1.0)
        self.assertEqual(policy["setpts_factor"], 1.0)
        self.assertEqual(policy["render_duration"], 36.0)
        self.assertTrue(policy["allow_timeline_extension"])
        self.assertTrue(policy["do_not_compress_to_tts_duration"])

    def test_locked_evidence_window_defaults_to_one_x_without_max_speed_field(self) -> None:
        policy = self.module.resolve_clip_speed_policy(
            {
                "source_material": "material_03",
                "evidence_strength": "high",
            },
            source_duration=24.0,
            target_duration=6.0,
        )

        self.assertEqual(policy["speed_factor"], 1.0)
        self.assertEqual(policy["max_allowed_speedup"], 1.0)

    def test_weak_evidence_or_context_is_capped_to_light_speedup(self) -> None:
        policy = self.module.resolve_clip_speed_policy(
            {
                "source_material": "material_01",
                "evidence_strength": "medium",
                "source_text_must_be_readable": False,
            },
            source_duration=30.0,
            target_duration=7.16,
        )

        self.assertEqual(policy["speed_factor"], 1.25)
        self.assertLessEqual(policy["speed_factor"], 1.25)
        self.assertTrue(policy["allow_timeline_extension"])

    def test_waiting_blank_or_repeated_action_can_exceed_one_point_five_only_when_explicit(self) -> None:
        policy = self.module.resolve_clip_speed_policy(
            {
                "source_material": "material_03",
                "segment_role": "waiting_or_blank_or_repeated_action",
                "evidence_window_lock": False,
                "source_text_must_be_readable": False,
            },
            source_duration=30.0,
            target_duration=7.5,
        )

        self.assertGreater(policy["speed_factor"], 1.5)
        self.assertFalse(policy["evidence_window_lock"])

    def test_missing_fields_on_user_recording_default_to_no_speedup(self) -> None:
        policy = self.module.resolve_clip_speed_policy(
            {
                "source_material": "material_03",
            },
            source_duration=24.0,
            target_duration=6.0,
        )

        self.assertEqual(policy["speed_factor"], 1.0)
        self.assertTrue(policy["evidence_window_lock"])


if __name__ == "__main__":
    unittest.main()
