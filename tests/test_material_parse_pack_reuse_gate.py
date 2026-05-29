from __future__ import annotations

import importlib.util
import json
import pathlib
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "素材解析包复用闸门_material_parse_pack_reuse_gate.py"
FIXTURE_PATH = ROOT / "codex_source" / "fixtures" / "素材解析包复用闸门_material_parse_pack_reuse_gate_cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("material_parse_pack_reuse_gate", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MaterialParsePackReuseGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def write_json(self, path: pathlib.Path, payload: object) -> pathlib.Path:
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
        return path

    def build_case_files(self, tmp_path: pathlib.Path, case: dict) -> dict[str, pathlib.Path | None]:
        source_file = tmp_path / "source_demo.mp4"
        source_file.write_text("demo source placeholder", encoding="utf-8")
        stat = source_file.stat()
        inputs = case["inputs"]
        if inputs.get("material_parse_pack") is None and case["case_id"] == "material_parse_pack_missing_blocks":
            return {
                "material_parse_pack": tmp_path / "missing_parse_pack.json",
                "source_segment_inventory": None,
                "script_to_shot_execution_map": None,
                "material_usage_ledger": None,
            }

        def replace_source(value: object) -> object:
            if isinstance(value, str):
                return str(source_file) if value == "__SOURCE_FILE__" else value
            if isinstance(value, list):
                return [replace_source(item) for item in value]
            if isinstance(value, dict):
                return {key: replace_source(item) for key, item in value.items()}
            return value

        inventory = replace_source(inputs["source_segment_inventory"])
        execution_map = replace_source(inputs["script_to_shot_execution_map"])
        ledger = replace_source(inputs["material_usage_ledger"])
        inventory_path = self.write_json(tmp_path / "source_segment_inventory.json", inventory)
        execution_path = self.write_json(tmp_path / "script_to_shot_execution_map.json", execution_map)
        ledger_path = self.write_json(tmp_path / "material_usage_ledger.json", ledger)
        parse_pack = {
            "parse_pack_id": f"pack_{case['case_id']}",
            "material_root": str(tmp_path),
            "source_files": [
                {
                    "path": str(source_file),
                    "size": stat.st_size,
                    "mtime_ns": stat.st_mtime_ns,
                    "material_id": "material_01",
                }
            ],
            "material_index_path": str(tmp_path / "material_index.json"),
            "material_detail_report_path": str(tmp_path / "material_detail_report.md"),
            "contact_sheet_paths": [str(tmp_path / "contact_sheet.jpg")],
            "source_segment_inventory_path": str(inventory_path),
            "script_to_shot_execution_map_path": str(execution_path),
            "material_usage_ledger_path": str(ledger_path),
            "parse_timestamp": "2026-05-29T00:00:00+08:00",
            "parse_scope": "fixture_only",
            "skill_used": "skills/视频素材解析_video_material_audit/SKILL.md",
            "reuse_policy": "reuse_only",
            "stale_if": [
                "source_file_added_deleted_or_renamed",
                "source_file_size_or_mtime_changed",
                "script_target_changed_and_pack_cannot_support",
                "user_requested_reaudit",
                "missing_key_timecode_or_evidence_fields",
            ],
        }
        parse_pack_path = self.write_json(tmp_path / "material_parse_pack.json", parse_pack)
        return {
            "material_parse_pack": parse_pack_path,
            "source_segment_inventory": inventory_path,
            "script_to_shot_execution_map": execution_path,
            "material_usage_ledger": ledger_path,
        }

    def run_case(self, case_id: str) -> dict:
        case = next(item for item in self.fixture["cases"] if item["case_id"] == case_id)
        with tempfile.TemporaryDirectory() as tmp:
            paths = self.build_case_files(pathlib.Path(tmp), case)
            return self.module.run_material_parse_pack_reuse_gate(
                material_parse_pack=paths["material_parse_pack"],
                source_segment_inventory=paths["source_segment_inventory"],
                script_to_shot_execution_map=paths["script_to_shot_execution_map"],
                material_usage_ledger=paths["material_usage_ledger"],
            )

    def test_fixture_json_parse(self) -> None:
        self.assertEqual(self.fixture["schema"], "material_parse_pack_reuse_gate_cases.v1")
        self.assertEqual(len(self.fixture["cases"]), 4)

    def test_material_parse_pack_missing_blocks(self) -> None:
        result = self.run_case("material_parse_pack_missing_blocks")
        self.assertEqual(result["status"], "blocked")
        self.assertIn("material_parse_pack_missing", result["blocked_reasons"])

    def test_duplicate_segment_without_reuse_reason_blocks(self) -> None:
        result = self.run_case("duplicate_segment_without_reuse_reason_blocks")
        self.assertEqual(result["status"], "blocked")
        self.assertIn("same_segment_reused_without_reuse_reason", result["blocked_reasons"])
        self.assertIn("consecutive_duplicate_segment_used", result["blocked_reasons"])

    def test_cannot_support_material_selected_blocks(self) -> None:
        result = self.run_case("cannot_support_material_selected_blocks")
        self.assertEqual(result["status"], "blocked")
        self.assertIn("cannot_support_material_selected", result["blocked_reasons"])

    def test_theme_only_match_as_direct_evidence_blocks(self) -> None:
        result = self.run_case("theme_only_match_as_direct_evidence_blocks")
        self.assertEqual(result["status"], "blocked")
        self.assertIn("theme_only_match_used_as_direct_evidence", result["blocked_reasons"])


if __name__ == "__main__":
    unittest.main()
