#!/usr/bin/env python3
"""Validate the real-task dry-run preflight fixture pair.

本探测只读取本地 YAML fixture（测试样例），不调用外部 API（外部接口），
不读取真实媒体，不启动 service（服务），不启用 runtime（运行时），不写仓库事实。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"PyYAML required by existing probe environment: {exc}")


REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "codex_source" / "schema_contracts" / "fixtures"

PASSING_FIXTURE = FIXTURE_ROOT / "passing" / "real_task_dry_run_preflight.passing.yaml"
BLOCKED_FIXTURE = FIXTURE_ROOT / "blocked" / "real_task_dry_run_preflight.blocked.yaml"

REQUIRED_TOP_LEVEL_KEYS = (
    "route_decision（路由判断）",
    "state_map_check（状态地图检查）",
    "rag_default_decision（RAG 默认判断）",
    "source_readback_requirement（原文回读要求）",
    "tool_permission_check（工具权限检查）",
    "copy_permission_check（文案权限检查）",
    "card_decision_check（卡片判断检查）",
    "material_evidence_check（素材证据检查）",
    "evaluator_failure_guardrail_check（评估失败护栏检查）",
    "human_decision_gate（人工决策闸门）",
    "allowed_actions（允许动作）",
    "blocked_actions（阻断动作）",
    "next_safe_step（下一步安全动作）",
)

REQUIRED_BLOCKED_REASONS = {
    "missing_project_route",
    "rag_default_without_source_readback",
    "real_rag_call_without_authorization",
    "runtime_requested_without_boundary",
    "copy_semantic_change_without_user_confirmation",
    "card_blocks_core_evidence",
    "media_generation_requested_in_dry_run",
    "technical_validation_claimed_as_content_validation",
}

REQUIRED_STATE_LABELS = {
    "formal（正式）",
    "candidate（候选）",
    "probe_only（仅探测）",
    "documented_only（仅文档）",
    "missing（缺失）",
    "conflict（冲突）",
    "blocked（阻断）",
}


class ProbeFailure(AssertionError):
    """Raised when the dry-run preflight contract is incomplete or unsafe."""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ProbeFailure(f"missing file: {path.relative_to(REPO_ROOT)}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ProbeFailure(f"not a mapping: {path.relative_to(REPO_ROOT)}")
    return data


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise ProbeFailure(message)


def validate_passing_fixture() -> dict[str, Any]:
    fixture = load_yaml(PASSING_FIXTURE)
    expect(fixture.get("case_type（样例类型）") == "passing", "passing fixture type mismatch")
    missing = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in fixture]
    expect(not missing, f"passing fixture missing top-level keys: {missing}")

    route = fixture["route_decision（路由判断）"]
    expect(route.get("project_route（项目路由）") == "video_factory（视频工厂）", "wrong project route")
    expect(
        route.get("workflow_route_decision（工作流归位判断）")
        in {"mechanism_repair_flow（机制修补流）", "preflight_validation_flow（执行前验证流）"},
        "workflow route must be mechanism repair or preflight validation",
    )
    expect(
        route.get("task_type（任务类型）") == "real_task_preflight_simulation（真实任务执行前模拟）",
        "wrong task type",
    )
    expect(route.get("is_video_generation（是否视频生成）") is False, "dry run cannot be video generation")
    expect(route.get("is_formal_copywriting（是否正式文案产出）") is False, "dry run cannot generate formal copy")

    state = fixture["state_map_check（状态地图检查）"]
    labels = set(state.get("allowed_statuses（允许状态）", []))
    expect(REQUIRED_STATE_LABELS.issubset(labels), f"state labels incomplete: {REQUIRED_STATE_LABELS - labels}")
    current = state.get("current_status（当前状态）", {})
    expect(current.get("framework_status（框架状态）") == "probe_only_safe_framework（仅限安全框架探测）", "framework status must remain probe only")
    expect(current.get("runtime_status（运行时状态）") == "not_enabled（未启用）", "runtime status must remain not enabled")
    expect(current.get("rag_runtime_status（RAG 运行时状态）") == "not_enabled（未启用）", "RAG runtime must remain not enabled")
    expect(current.get("media_status（媒体状态）") == "not_generated（未生成）", "media must remain not generated")

    rag = fixture["rag_default_decision（RAG 默认判断）"]
    expect(rag.get("rag_default_entered（RAG 是否进入默认判断链）") is True, "RAG must enter default decision route")
    fields = set(rag.get("required_source_fields（必需来源字段）", []))
    for field in ("source_path（来源路径）", "chunk_id（分块编号）", "readback（原文回读）"):
        expect(field in fields, f"RAG required source field missing: {field}")
    expect(rag.get("real_dashvector_call_allowed（是否允许真实调用 DashVector）") is False, "DashVector real call must remain false")
    expect(rag.get("real_chroma_ingestion_allowed（是否允许 Chroma 入库）") is False, "Chroma ingestion must remain false")
    expect(rag.get("repo_fact_priority（仓库事实优先）") is True, "repo fact priority required")
    expect(rag.get("rag_result_can_override_repo_fact（RAG 结果能否覆盖仓库事实）") is False, "RAG cannot override repo facts")

    readback = fixture["source_readback_requirement（原文回读要求）"]
    expect(readback.get("source_readback_required（是否必须原文回读）") is True, "source readback required")
    minimum = set(readback.get("minimum_source_fields（最小来源字段）", []))
    for field in ("source_path（来源路径）", "chunk_id（分块编号）", "line_range（行号范围，如适用）", "readback（原文回读）"):
        expect(field in minimum, f"source readback field missing: {field}")

    tool = fixture["tool_permission_check（工具权限检查）"]
    for key in (
        "external_tool_call_allowed（是否允许工具外呼）",
        "tool_repo_fact_write_allowed（是否允许工具写仓库事实）",
        "cost_creation_allowed（是否允许产生成本）",
        "private_file_read_allowed（是否允许读取隐私文件）",
    ):
        expect(tool.get(key) is False, f"tool permission must be false: {key}")

    copy = fixture["copy_permission_check（文案权限检查）"]
    expect(copy.get("locked_copy_input_present（是否已有锁定文案输入）") is False, "locked copy should be absent")
    for key in (
        "formal_copy_generation_allowed（是否允许生成正式文案）",
        "semantic_change_allowed（是否允许改语义）",
        "title_change_allowed（是否允许改标题）",
        "core_judgment_change_allowed（是否允许改核心判断）",
    ):
        expect(copy.get(key) is False, f"copy permission must be false: {key}")

    card = fixture["card_decision_check（卡片判断检查）"]
    expect(card.get("card_generation_this_round（本轮是否生成卡片）") is False, "card generation forbidden this round")
    expect(card.get("card_can_block_evidence（卡片能否遮挡证据）") is False, "card cannot block evidence")
    expect(card.get("card_can_add_new_fact（卡片能否新增事实）") is False, "card cannot add facts")

    material = fixture["material_evidence_check（素材证据检查）"]
    expect(material.get("real_media_read_this_round（本轮是否读取真实媒体）") is False, "real media read forbidden")
    future_fields = set(material.get("future_required_fields（后续必需字段）", []))
    for field in ("material_path（素材路径）", "timecode（时间码）", "evidence_strength（证据强度）", "material_gap（素材缺口）"):
        expect(field in future_fields, f"material future field missing: {field}")

    guardrail = fixture["evaluator_failure_guardrail_check（评估失败护栏检查）"]
    expect(
        guardrail.get("technical_validation_can_promote_content_validation（技术验证能否推进内容验证）") is False,
        "technical validation cannot promote content validation",
    )
    expect(
        guardrail.get("dry_run_can_claim_real_output_completed（干跑能否声称真实产出完成）") is False,
        "dry run cannot claim real output",
    )

    human = fixture["human_decision_gate（人工决策闸门）"]
    required_for = set(human.get("required_for（需要人工确认的事项）", []))
    for item in ("real_rag_call（真实 RAG 调用）", "external_api_call（外部 API 调用）", "media_generation（媒体生成）", "runtime_enablement（运行时启用）"):
        expect(item in required_for, f"human gate missing: {item}")
    expect(human.get("auto_pass_allowed_when_required（需要人工时是否允许自动通过）") is False, "human-required gates cannot auto-pass")

    blocked_actions = set(fixture["blocked_actions（阻断动作）"])
    for action in ("generate_video（生成视频）", "real_dashvector_call（真实调用 DashVector）", "runtime_enablement（启用运行时）", "content_validation_promotion（推进内容验证）"):
        expect(action in blocked_actions, f"blocked action missing: {action}")

    return {"status": "passed", "top_level_key_count": len(REQUIRED_TOP_LEVEL_KEYS)}


def validate_blocked_fixture() -> dict[str, Any]:
    fixture = load_yaml(BLOCKED_FIXTURE)
    expect(fixture.get("case_type（样例类型）") == "blocked", "blocked fixture type mismatch")
    expect(fixture.get("blocked（是否阻断）") is True, "blocked fixture must set blocked true")
    reasons = set(fixture.get("blocked_reasons", []))
    expect(REQUIRED_BLOCKED_REASONS.issubset(reasons), f"blocked reasons incomplete: {REQUIRED_BLOCKED_REASONS - reasons}")
    cases = fixture.get("blocked_cases（阻断场景）", {})
    for reason in REQUIRED_BLOCKED_REASONS:
        matching_keys = [key for key in cases if key.startswith(reason)]
        expect(matching_keys, f"blocked case detail missing for {reason}")
    unsafe = fixture.get("unsafe_attempt_summary（不安全尝试摘要）", {})
    expect(unsafe.get("project_route_present（项目路由是否存在）") is False, "blocked case should miss project route")
    expect(unsafe.get("source_readback_required（是否要求原文回读）") is False, "blocked case should miss source readback")
    expect(unsafe.get("real_rag_authorized（真实 RAG 是否授权）") is False, "real RAG should be unauthorized")
    expect(unsafe.get("dry_run_requests_media（干跑是否请求媒体）") is True, "blocked case should request media unsafely")
    return {"status": "blocked_passed", "blocked_reason_count": len(reasons)}


def main() -> int:
    result: dict[str, Any] = {
        "probe_name": "real_task_dry_run_preflight_probe",
        "runtime_enabled": False,
        "service_started": False,
        "external_api_called": False,
        "dashvector_real_call": False,
        "chroma_ingestion_run": False,
        "media_generated": False,
    }
    try:
        result["passing_fixture_result"] = validate_passing_fixture()
        result["blocked_fixture_result"] = validate_blocked_fixture()
        result["final_probe_status"] = "passed"
    except ProbeFailure as exc:
        result["final_probe_status"] = "failed"
        result["failure"] = str(exc)
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
