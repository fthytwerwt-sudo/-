from __future__ import annotations

import importlib.util
import json
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "运营学习台账系统_operation_learning_ledger_system.py"
LEDGER_DIR = ROOT / "review_loop" / "learning_ledger"


def load_module():
    spec = importlib.util.spec_from_file_location("operation_learning_ledger_system", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def load_events() -> list[dict]:
    path = LEDGER_DIR / "metric_event_log.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def events_for(video_id: str) -> list[dict]:
    return [event for event in load_events() if event["video_id"] == video_id]


class OperationLearningLedgerSystemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def test_v005_enters_metric_event_log(self) -> None:
        v005_events = events_for("V005")
        self.assertGreaterEqual(len(v005_events), 17)
        metric_names = {event["metric_name"] for event in v005_events}
        self.assertIn("play_count", metric_names)
        self.assertIn("two_second_bounce_rate", metric_names)
        self.assertIn("clear_need_customer_count", metric_names)

    def test_v005_good_and_bad_signals_both_exist(self) -> None:
        v005_events = events_for("V005")
        directions = {event["signal_direction"] for event in v005_events}
        self.assertIn("good", directions)
        self.assertIn("bad", directions)
        self.assertIn("weak", directions)
        self.assertIn("missing", directions)
        self.assertIn("uncertain", directions)

    def test_v005_enters_episode_variable_registry(self) -> None:
        registry = json.loads((LEDGER_DIR / "episode_variable_registry.json").read_text(encoding="utf-8"))
        by_id = {episode["video_id"]: episode for episode in registry["episodes"]}
        self.assertEqual(by_id["V005"]["copy_id"], "V005_copy_v1")
        self.assertEqual(by_id["V005"]["primary_variable_guess"], "topic_eye_and_packaging")
        self.assertIn("用户自己的选题", by_id["V005"]["human_contribution_note"])

    def test_bet_card_and_handoff_are_generated(self) -> None:
        bet_card = LEDGER_DIR / "next_episode_bet_card.md"
        handoff = LEDGER_DIR / "current_copy_revision_handoff.md"
        self.assertTrue(bet_card.exists())
        self.assertTrue(handoff.exists())
        self.assertIn("Codex 怎么降低剪辑成本", bet_card.read_text(encoding="utf-8"))
        self.assertIn("ChatGPT 写下一版文案时必须做到", handoff.read_text(encoding="utf-8"))

    def test_v002_excluded_from_normal_distribution_attribution(self) -> None:
        registry = json.loads((LEDGER_DIR / "episode_variable_registry.json").read_text(encoding="utf-8"))
        v002 = next(episode for episode in registry["episodes"] if episode["video_id"] == "V002")
        self.assertFalse(v002["normal_attribution_eligible"])
        self.assertEqual(v002["normal_attribution_excluded_reason"], "policy_limited_abnormal_sample")
        v002_events = events_for("V002")
        self.assertEqual(v002_events[0]["metric_name"], "normal_distribution_attribution")
        self.assertEqual(v002_events[0]["metric_value"], "excluded")

    def test_v001_does_not_generate_fake_metrics_from_markdown(self) -> None:
        registry = json.loads((LEDGER_DIR / "episode_variable_registry.json").read_text(encoding="utf-8"))
        v001 = next(episode for episode in registry["episodes"] if episode["video_id"] == "V001")
        self.assertFalse(v001["markdown_metric_extract_allowed"])
        for event in events_for("V001"):
            self.assertIsNone(event["metric_value"])
            self.assertNotEqual(event["source_status"], "user_provided_or_markdown_extract")

    def test_missing_fields_stay_missing_not_zero(self) -> None:
        by_metric = {event["metric_name"]: event for event in events_for("V005")}
        for metric_name in [
            "3s_retention",
            "profile_visit_count",
            "dm_count",
            "effective_dm_count",
            "effective_consult_count",
            "clear_need_customer_count",
        ]:
            self.assertIsNone(by_metric[metric_name]["metric_value"])
            self.assertEqual(by_metric[metric_name]["source_status"], "missing")

    def test_missing_bet_card_blocks_completion_claim(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_root = pathlib.Path(tmp)
            status = self.module.closed_loop_completion_status(tmp_root)
            self.assertFalse(status["completed_allowed"])
            self.assertIn("review_loop/learning_ledger/next_episode_bet_card.md", status["missing_required_outputs"])

    def test_chatgpt_copy_entry_can_find_handoff_files(self) -> None:
        manifest = json.loads((LEDGER_DIR / "learning_ledger_manifest.json").read_text(encoding="utf-8"))
        required = set(manifest["required_next_copy_inputs"])
        self.assertIn("review_loop/learning_ledger/current_copy_revision_handoff.md", required)
        self.assertIn("review_loop/learning_ledger/next_episode_bet_card.md", required)
        self.assertIn("review_loop/copy_iteration/V005/V005_copy_structure_map.json", required)

    def test_latest_report_preserves_forbidden_boundaries(self) -> None:
        report = json.loads((LEDGER_DIR / "latest_operation_learning_report.json").read_text(encoding="utf-8"))
        not_allowed = set(report["V005_learning_result"]["not_allowed_conclusions"])
        self.assertIn("不能写内容通过", not_allowed)
        self.assertIn("不能写方向成立", not_allowed)
        self.assertIn("不能写商业验证成立", not_allowed)
        self.assertEqual(report["ChatGPT_creative_judgment_responsibility"]["must_not_output_only"], "泛泛建议或纯数据解释")


if __name__ == "__main__":
    unittest.main()
