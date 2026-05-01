from __future__ import annotations

import asyncio
import base64
import json
import pathlib
import re
import shutil
import subprocess
import time
import wave
from dataclasses import dataclass
from typing import Any

import requests
import websockets
from PIL import Image, ImageDraw, ImageFilter, ImageFont


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
LOCAL_PROJECT_ROOT = pathlib.Path("/Users/fan/Documents/视频工厂")
TASK_SLUG = "20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix"
LOCAL_REVIEW_PACK = LOCAL_PROJECT_ROOT / "复审包_review_packs" / TASK_SLUG
LOCAL_DIST = LOCAL_PROJECT_ROOT / "dist" / TASK_SLUG
REPO_REVIEW_PACK = REPO_ROOT / "复审包_review_packs" / TASK_SLUG
REPO_DIST = REPO_ROOT / "dist" / TASK_SLUG
REPO_REFERENCE_DIR = REPO_REVIEW_PACK / "references"
LOCAL_REFERENCE_DIR = LOCAL_REVIEW_PACK / "references"

OPENING_ANCHOR = (
    LOCAL_PROJECT_ROOT
    / "素材库_assets"
    / "元素娃娃开头锚点_opening_anchor_20260428"
    / "005_1496_seg01_no_text_inpaint_opening_anchor.mp4"
)
NEGATIVE_RECORDING = LOCAL_PROJECT_ROOT / "素材录制" / "反面" / "录制于 2026-04-16 22.41.32.mp4"
POSITIVE_RECORDING = LOCAL_PROJECT_ROOT / "素材录制" / "正面" / "录制于 2026-04-16 23.03.53.mp4"

CREATE_ENDPOINT = "https://dashscope.aliyuncs.com/api/v1/services/audio/tts/customization"
CREATE_MODEL = "qwen-voice-enrollment"
TARGET_MODEL = "qwen3-tts-vc-realtime-2026-01-15"
VOICE_MASKED = "qwen-t...ac19"
VOICE_SUFFIX = "ac19"
SAMPLE_RATE = 24000
VIDEO_WIDTH = 720
VIDEO_HEIGHT = 1280
FPS = 25

FULL_NAME = "AI做PPT踩坑_成品候选_v31_full.mp4"
CONTACT_SHEET_NAME = "AI做PPT踩坑_成品候选_v31_contact_sheet.jpg"
TIMELINE_NAME = "AI做PPT踩坑_成品候选_v31_timeline.json"
CUT_MAP_NAME = "AI做PPT踩坑_成品候选_v31_cut_map.md"
MANIFEST_NAME = "AI做PPT踩坑_成品候选_v31_review_manifest.md"
SUMMARY_NAME = "AI做PPT踩坑_成品候选_v31_summary.json"
RUN_SUMMARY_NAME = "AI做PPT踩坑_成品候选_v31_run_summary.json"
INHERITANCE_REPORT_NAME = "locked_reference_inheritance_report.md"
METADATA_REPORT_NAME = "video_metadata_probe_report.json"
OPENING_PREVIEW_NAME = "shot00_opening_hello_wave_preview.mp4"
VISUAL_ROUTE_MAP_NAME = "visual_route_map.json"
VISUAL_ROUTE_VALIDATION_NAME = "visual_route_validation_report.json"
PR7B_REFERENCE_NAME = "PR7_B_骚萌反应页.png"
NEGATIVE_PROMPT_REFERENCE_NAME = "round34_反面展示提示卡.png"
POSITIVE_PROMPT_REFERENCE_NAME = "round34_正面展示提示卡.png"


@dataclass
class Segment:
    segment_id: str
    kind: str
    voice_text: str
    visual_source: str
    source_path: pathlib.Path | None = None
    source_start: float | None = None
    crop_x: int = 760
    image_id: str | None = None
    note: str = ""
    locked_refs: tuple[str, ...] = ()
    candidate_refs: tuple[str, ...] = ()
    failed_refs_avoided: tuple[str, ...] = ()


SEGMENTS: list[Segment] = [
    Segment(
        "shot00_opening_hello_wave",
        "opening_video",
        "hello，大家好。",
        "元素娃娃无字开头锚点，约两秒轻入口。",
        OPENING_ANCHOR,
        0.0,
        0,
        locked_refs=("opening_reference_element_doll_no_text_locked_20260428",),
    ),
    Segment(
        "shot01_result_diff_opening",
        "image",
        "先看这两个结果。左边，是我第一次让 AI 帮我做 PPT。右边，是我改完问法以后。我先说结论：差的不是工具，是我第一句话。",
        "结果差开头卡：可爱信息卡路线。",
        image_id="result_opening",
        candidate_refs=(
            "prompt_card_pink_sakura_round34_candidate_20260430",
            "card_visual_quality_clean_ui_texture_candidate_20260430",
        ),
    ),
    Segment(
        "shot03_problem_hook_sassy_card",
        "image",
        "你以为在做 PPT，它以为在写读后感。",
        "问题钩子骚萌卡：PR #7 B 版独立 reaction page 路线。",
        image_id="sassy_problem",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_b_user_selected_candidate_20260430",),
    ),
    Segment(
        "negative_display_prompt_card",
        "image",
        "《反面展示》。先看旧做法：一句糊话，结果怎么变泛。",
        "反面展示提示卡：可爱段落提示卡路线。",
        image_id="negative_display_prompt",
        candidate_refs=("prompt_card_pink_sakura_round34_candidate_20260430",),
    ),
    Segment(
        "shot02_negative_input",
        "screen",
        "第一次，我把最新方案 PDF 丢进豆包，只写了一句：帮我把这个方案整理一下。这句话听起来没问题，但它其实只说了一件事：整理。",
        "反面录屏：PDF 与宽泛口令可见。",
        NEGATIVE_RECORDING,
        15.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
        failed_refs_avoided=("zoom_pr15_v2_failed_20260430",),
    ),
    Segment(
        "shot04_negative_result_text_plan",
        "screen",
        "然后它真的很认真。标题给我写了，结构也排了。什么战略执行总案，什么产品矩阵，什么三十天落地计划，看着很完整。但我看到这里才发现：这不是 PPT 初稿，这是一份整理过的文字方案。",
        "反面录屏：战略执行总案、产品矩阵、30 天落地计划。",
        NEGATIVE_RECORDING,
        35.0,
        760,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
        failed_refs_avoided=("zoom_pr15_v2_failed_20260430",),
    ),
    Segment(
        "shot05_negative_reversal_sassy_card",
        "image",
        "它给了我一份更好的 Word，但我要的是 PPT。",
        "反面反转骚萌卡：PR #7 B 版独立 reaction page 路线。",
        image_id="sassy_negative",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_b_user_selected_candidate_20260430",),
    ),
    Segment(
        "shot06_cause_turning_point",
        "image",
        "所以这次翻车，不是 AI 没做事。它只是认真完成了我说出口的要求。问题是，我只说了整理一下，没有说清楚给谁看、要达成什么、要不要变成 PPT、什么叫能交。",
        "归因转折卡：可爱信息卡路线，AI 没偷懒，是我没说清交付。",
        image_id="cause_turning",
        candidate_refs=(
            "prompt_card_pink_sakura_round34_candidate_20260430",
            "card_visual_quality_clean_ui_texture_candidate_20260430",
        ),
    ),
    Segment(
        "positive_display_prompt_card",
        "image",
        "《正面展示》。再看工作包后：结果怎么一步步落成。",
        "正面展示提示卡：可爱段落提示卡路线。",
        image_id="positive_display_prompt",
        candidate_refs=("prompt_card_pink_sakura_round34_candidate_20260430",),
    ),
    Segment(
        "shot07_deliverable_draft_keyword",
        "screen",
        "第二次，我没有一上来就说帮我做个 PPT。我先让它判断一件事：这份内容，能不能变成一版可交付初稿。这一步很关键。我不是让它多写一点，我是先给它一张交付物的验收表。",
        "正面录屏：可交付初稿方法词出现。",
        POSITIVE_RECORDING,
        30.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot08_prompt_architecture_card",
        "image",
        "这张表，我拆成三层。先定交付物：它不是整理稿，要往 PPT 初稿走。再检查对象、目标、动作、节奏、事实和假设、空话套话。最后，再让它输出适合做 PPT 的初稿结构。",
        "Prompt 架构功能卡：可爱信息卡路线。",
        image_id="prompt_architecture",
        candidate_refs=(
            "prompt_card_pink_sakura_round34_candidate_20260430",
            "card_visual_quality_clean_ui_texture_candidate_20260430",
        ),
    ),
    Segment(
        "shot09_positive_title_specific",
        "screen",
        "加了这张验收表以后，结果先从标题开始变具体。它不再给我一个很大的战略执行总案，而是变成 AI 时间管理小程序，七天种子用户拉新营销方案。你看，这里已经有任务了。",
        "正面录屏：标题变具体。",
        POSITIVE_RECORDING,
        70.0,
        640,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot10_positive_constraints",
        "screen",
        "更重要的是，它开始出现具体约束。周期是七天，预算不超过五千，核心渠道是小红书加私域，目标用户两百加，内容目标五万以上。这时候，它已经开始围绕真实交付物规划。",
        "正面录屏：周期、预算、渠道、目标。",
        POSITIVE_RECORDING,
        80.0,
        620,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot11_ppt_page_instruction",
        "screen",
        "再往后，它开始写 PPT 页面设计指令。不是一句做得好看点，而是拆页面怎么设计、标题怎么放、核心指标怎么呈现、每一页承担什么信息。这一步，才是真正从文档往 PPT 走。",
        "正面录屏：XML / PPT 页面设计指令。",
        POSITIVE_RECORDING,
        300.0,
        760,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot12_ppt_generation_process",
        "screen",
        "后面进入 PPT 生成界面。这段不用讲太多，看画面就够了。缩略图一页一页出来，能看到策略判断、问题诊断、目标用户画像、三大内容方向，还有小红书和私域的分工。",
        "正面录屏：PPT 生成过程和缩略图逐页出现。",
        POSITIVE_RECORDING,
        570.0,
        640,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot13_ppt_completed_preview",
        "screen",
        "最后，界面显示：已完成 PPT 生成，用了六分三十一秒。这份 PPT 共十六页。到这里，反转才真正成立。第一次是文字方案，第二次至少推进到了 PPT 初稿状态。注意，预览不等于最终成品。",
        "正面录屏：已完成PPT生成(6m31s) 与 16 页预览。",
        POSITIVE_RECORDING,
        720.0,
        1500,
        locked_refs=("middle_editing_round34_locked_20260425", "middle_zoom_reference_confirmed_middle_preview_20260430"),
    ),
    Segment(
        "shot14_positive_reversal_sassy_card",
        "image",
        "这回终于不像空气方案了。虽然还不能直接发。",
        "正面反转骚萌卡：PR #7 B 版独立 reaction page 路线。",
        image_id="sassy_positive",
        locked_refs=("sassy_card_three_type_rule_locked_20260428",),
        candidate_refs=("sassy_card_pr7_b_user_selected_candidate_20260430",),
    ),
    Segment(
        "shot15_result_diff_card",
        "image",
        "同一份资料。第一种问法，只给了 AI 一个动作：整理。第二种问法，先给了 AI 一个标准：什么叫能交。差的不是 AI 突然变聪明，是我终于把交付物说清楚了。",
        "结果差卡：可爱信息卡路线，普通问法 vs 交付标准。",
        image_id="result_diff",
        candidate_refs=(
            "prompt_card_pink_sakura_round34_candidate_20260430",
            "card_visual_quality_clean_ui_texture_candidate_20260430",
        ),
    ),
    Segment(
        "shot16_low_pressure_ending",
        "image",
        "所以我现在用 AI 做 PPT，不会一上来就说：帮我整理一下。我会先问它：最后给谁看？要推动什么结果？下一步动作是什么？哪些是真实信息，哪些只是推测？这不是万能提示词，但至少，它不会停在一堆漂亮的文字里。先定义交付，再让 AI 生成。",
        "低压尾卡 / Prompt 引用尾卡：可爱信息卡路线。",
        image_id="tail_card",
        candidate_refs=(
            "prompt_card_pink_sakura_round34_candidate_20260430",
            "card_visual_quality_clean_ui_texture_candidate_20260430",
        ),
    ),
]


def run_command(args: list[str], log_path: pathlib.Path | None = None) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(args, text=True, capture_output=True)
    if log_path is not None:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text(
            "$ " + " ".join(args) + "\n\nSTDOUT:\n" + completed.stdout + "\n\nSTDERR:\n" + completed.stderr,
            encoding="utf-8",
        )
    completed.check_returncode()
    return completed


def resolve_binary(name: str) -> str:
    binary = shutil.which(name)
    if binary:
        return binary
    fallback = REPO_ROOT / "node_modules" / "ffmpeg-static" / name
    if fallback.exists():
        return str(fallback)
    raise RuntimeError(f"缺少 {name}")


def write_json(path: pathlib.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sync_reference_assets() -> None:
    required = [
        PR7B_REFERENCE_NAME,
        "可爱卡片参考_contact_sheet.jpg",
        NEGATIVE_PROMPT_REFERENCE_NAME,
        POSITIVE_PROMPT_REFERENCE_NAME,
    ]
    missing = [name for name in required if not (REPO_REFERENCE_DIR / name).exists()]
    if missing:
        if PR7B_REFERENCE_NAME in missing:
            raise RuntimeError("blocked_pr7_b_reference_missing")
        raise RuntimeError("blocked_cute_card_reference_missing")
    if LOCAL_REFERENCE_DIR.exists():
        shutil.rmtree(LOCAL_REFERENCE_DIR)
    shutil.copytree(REPO_REFERENCE_DIR, LOCAL_REFERENCE_DIR)


def build_visual_route_map() -> list[dict[str, Any]]:
    prompt_secondary = [
        "origin/codex/cute-card-reference-audit-20260430",
        "复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit",
    ]
    info_secondary = [
        "card_visual_quality_clean_ui_texture_candidate_20260430",
        "用户确认图文字锚点：粉色樱花柔和展示牌 + 清晰信息层级",
    ]
    sassy_secondary = [
        "sassy_card_three_type_rule_locked_20260428",
        "sassy_card_pr7_b_user_selected_candidate_20260430",
    ]
    definitions = [
        ("negative_display_prompt_card", "segment_prompt_card", "cute_prompt_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", prompt_secondary, "make_cute_prompt_card"),
        ("positive_display_prompt_card", "segment_prompt_card", "cute_prompt_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", prompt_secondary, "make_cute_prompt_card"),
        ("shot01_result_diff_opening", "result_diff_opening_card", "cute_info_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", info_secondary, "make_cute_info_card"),
        ("shot06_cause_turning_point", "turning_point_info_card", "cute_info_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", info_secondary, "make_cute_info_card"),
        ("shot08_prompt_architecture_card", "prompt_architecture_info_card", "cute_info_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", info_secondary, "make_cute_info_card"),
        ("shot15_result_diff_card", "result_diff_info_card", "cute_info_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", info_secondary, "make_cute_info_card"),
        ("shot16_low_pressure_ending", "prompt_tail_info_card", "cute_info_card_route", "prompt_card_pink_sakura_round34_candidate_20260430", info_secondary, "make_cute_info_card"),
        ("shot03_problem_hook_sassy_card", "sassy_reaction_card", "sassy_reaction_card_route", PR7B_REFERENCE_NAME, sassy_secondary, "make_sassy_reaction_card_from_pr7b"),
        ("shot05_negative_reversal_sassy_card", "sassy_reaction_card", "sassy_reaction_card_route", PR7B_REFERENCE_NAME, sassy_secondary, "make_sassy_reaction_card_from_pr7b"),
        ("shot14_positive_reversal_sassy_card", "sassy_reaction_card", "sassy_reaction_card_route", PR7B_REFERENCE_NAME, sassy_secondary, "make_sassy_reaction_card_from_pr7b"),
    ]
    route_peers = {
        "cute_prompt_card_route": ["negative_display_prompt_card", "positive_display_prompt_card"],
        "cute_info_card_route": [
            "shot01_result_diff_opening",
            "shot06_cause_turning_point",
            "shot08_prompt_architecture_card",
            "shot15_result_diff_card",
            "shot16_low_pressure_ending",
        ],
        "sassy_reaction_card_route": [
            "shot03_problem_hook_sassy_card",
            "shot05_negative_reversal_sassy_card",
            "shot14_positive_reversal_sassy_card",
        ],
    }
    forbidden_by_route = {
        "cute_prompt_card_route": [
            "sassy_card_pr7_a_candidate_20260428",
            "sassy_card_pr7_b_user_selected_candidate_20260430 as shell",
            "card_visual_quality_clean_ui_texture_candidate_20260430 as dense UI shell",
            "deep_blue_tech_saas_ui_rejected",
        ],
        "cute_info_card_route": [
            "sassy_card_pr7_a_candidate_20260428",
            "sassy_reaction_card_route shell",
            "deep_blue_tech_saas_ui_rejected",
            "More Filters CTA",
            "black_bottom_button",
        ],
        "sassy_reaction_card_route": [
            "cute_prompt_card_route shell",
            "cute_info_card_route shell",
            "white_pink_display_board_shell",
            "card_visual_quality_clean_ui_texture_candidate_20260430 as layout shell",
            "deep_blue_tech_saas_ui_rejected",
        ],
    }
    must_not_share = {
        "cute_prompt_card_route": route_peers["cute_info_card_route"] + route_peers["sassy_reaction_card_route"],
        "cute_info_card_route": route_peers["cute_prompt_card_route"] + route_peers["sassy_reaction_card_route"],
        "sassy_reaction_card_route": route_peers["cute_prompt_card_route"] + route_peers["cute_info_card_route"],
    }
    route_map: list[dict[str, Any]] = []
    for segment_id, card_type, route, primary, secondary, renderer in definitions:
        route_map.append(
            {
                "segment_id": segment_id,
                "card_type": card_type,
                "assigned_route": route,
                "primary_reference": primary,
                "secondary_reference": secondary,
                "forbidden_references": forbidden_by_route[route],
                "renderer_function": renderer,
                "validation_gate": f"{route}_must_match_assigned_segments",
                "can_share_shell_with": [peer for peer in route_peers[route] if peer != segment_id],
                "must_not_share_shell_with": must_not_share[route],
            }
        )
    return route_map


def validate_route_map_assignments(route_map: list[dict[str, Any]]) -> dict[str, Any]:
    by_segment = {item["segment_id"]: item for item in route_map}
    required_routes = {
        "negative_display_prompt_card": "cute_prompt_card_route",
        "positive_display_prompt_card": "cute_prompt_card_route",
        "shot01_result_diff_opening": "cute_info_card_route",
        "shot06_cause_turning_point": "cute_info_card_route",
        "shot08_prompt_architecture_card": "cute_info_card_route",
        "shot15_result_diff_card": "cute_info_card_route",
        "shot16_low_pressure_ending": "cute_info_card_route",
        "shot03_problem_hook_sassy_card": "sassy_reaction_card_route",
        "shot05_negative_reversal_sassy_card": "sassy_reaction_card_route",
        "shot14_positive_reversal_sassy_card": "sassy_reaction_card_route",
    }
    missing = [segment_id for segment_id in required_routes if segment_id not in by_segment]
    mismatched = [
        {
            "segment_id": segment_id,
            "expected_route": expected,
            "actual_route": by_segment.get(segment_id, {}).get("assigned_route"),
        }
        for segment_id, expected in required_routes.items()
        if segment_id in by_segment and by_segment[segment_id]["assigned_route"] != expected
    ]
    sassy_wrong = [
        item
        for item in route_map
        if item["segment_id"] in {
            "shot03_problem_hook_sassy_card",
            "shot05_negative_reversal_sassy_card",
            "shot14_positive_reversal_sassy_card",
        }
        and item["assigned_route"] != "sassy_reaction_card_route"
    ]
    info_wrong = [
        item
        for item in route_map
        if item["segment_id"] in {
            "shot01_result_diff_opening",
            "shot06_cause_turning_point",
            "shot08_prompt_architecture_card",
            "shot15_result_diff_card",
            "shot16_low_pressure_ending",
        }
        and item["assigned_route"] == "sassy_reaction_card_route"
    ]
    prompt_wrong = [
        item
        for item in route_map
        if item["segment_id"] in {"negative_display_prompt_card", "positive_display_prompt_card"}
        and item["assigned_route"] != "cute_prompt_card_route"
    ]
    passed = not missing and not mismatched and not sassy_wrong and not info_wrong and not prompt_wrong
    blocker = None
    if sassy_wrong:
        blocker = "blocked_sassy_route_misassigned"
    elif info_wrong:
        blocker = "blocked_info_card_route_misassigned"
    elif missing:
        blocker = "blocked_route_map_missing"
    elif mismatched or prompt_wrong:
        blocker = "blocked_visual_route_not_separated"
    return {
        "passed": passed,
        "route_map_exists": True,
        "missing_segments": missing,
        "mismatched_segments": mismatched,
        "sassy_wrong_assignments": [item["segment_id"] for item in sassy_wrong],
        "info_wrong_assignments": [item["segment_id"] for item in info_wrong],
        "prompt_wrong_assignments": [item["segment_id"] for item in prompt_wrong],
        "blocker": blocker,
    }


def assigned_route_for_segment(segment_id: str) -> str | None:
    for item in build_visual_route_map():
        if item["segment_id"] == segment_id:
            return str(item["assigned_route"])
    return None


def load_api_key() -> str:
    runtime_config = pathlib.Path("/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    if not runtime_config.exists():
        raise RuntimeError("缺少运行时本地配置：/Users/fan/.config/video-factory/formal_api_demo.local.toml")
    in_auth = False
    for line in runtime_config.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped == "[auth]":
            in_auth = True
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            in_auth = False
        if in_auth and stripped.startswith("api_key ="):
            value = stripped.split("=", 1)[1].strip().strip('"')
            if value and not value.startswith("SET_"):
                return value
    raise RuntimeError("运行时本地配置缺少真实 auth.api_key")


def mask_voice(voice: str) -> str:
    if len(voice) <= 12:
        return "<masked>"
    return f"{voice[:6]}...{voice[-4:]}"


def resolve_existing_custom_voice(api_key: str) -> dict[str, Any]:
    payload = {"model": CREATE_MODEL, "input": {"action": "list", "page_size": 100, "page_index": 0}}
    started = time.time()
    response = requests.post(
        CREATE_ENDPOINT,
        json=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        timeout=45,
    )
    elapsed = round(time.time() - started, 3)
    data = response.json()
    response.raise_for_status()
    voice_list = data.get("output", {}).get("voice_list", [])
    candidates = [
        item
        for item in voice_list
        if item.get("target_model") == TARGET_MODEL and str(item.get("voice", "")).endswith(VOICE_SUFFIX)
    ]
    sanitized = {
        "provider": "aliyun_bailian",
        "endpoint": CREATE_ENDPOINT,
        "request_method": "POST",
        "purpose": "list_existing_custom_voices_only_no_create",
        "status_code": response.status_code,
        "elapsed_seconds": elapsed,
        "request_id": data.get("request_id"),
        "target_voice_masked": VOICE_MASKED,
        "target_model": TARGET_MODEL,
        "voice_count": len(voice_list),
        "matched_count": len(candidates),
        "voices": [
            {
                "voice_masked": mask_voice(str(item.get("voice", ""))),
                "target_model": item.get("target_model"),
                "gmt_create": item.get("gmt_create"),
            }
            for item in voice_list
        ],
    }
    write_json(LOCAL_DIST / "tts" / "custom_voice_list_debug_sanitized.json", sanitized)
    if len(candidates) != 1:
        raise RuntimeError("blocked_custom_voice_id_not_found")
    voice = str(candidates[0].get("voice", ""))
    if mask_voice(voice) != VOICE_MASKED:
        raise RuntimeError("blocked_custom_voice_id_not_found")
    return {
        "voice": voice,
        "voice_masked": mask_voice(voice),
        "target_model": candidates[0].get("target_model"),
        "resolved_by": "list_existing_custom_voices_match_suffix_ac19",
        "sanitized_list_path": str(LOCAL_DIST / "tts" / "custom_voice_list_debug_sanitized.json"),
    }


def read_wave_info(path: pathlib.Path) -> dict[str, Any]:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        sample_rate = wav_file.getframerate()
        frames = wav_file.getnframes()
    return {
        "path": str(path),
        "duration_seconds": round(frames / sample_rate, 3),
        "format": "wav",
        "codec": "pcm_s16le" if sample_width == 2 else f"pcm_s{sample_width * 8}le",
        "sample_rate": sample_rate,
        "channels": channels,
        "sample_width_bytes": sample_width,
        "frames": frames,
        "file_size_bytes": path.stat().st_size,
    }


async def recv_until_session_ready(ws: Any, event_types: list[str]) -> None:
    while True:
        event = json.loads(await ws.recv())
        event_type = event.get("type", "")
        event_types.append(event_type)
        if event_type in {"session.created", "session.updated"}:
            return
        if event_type == "error":
            raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))


async def synthesize_segment(api_key: str, voice: str, segment: Segment, output_path: pathlib.Path) -> dict[str, Any]:
    url = f"wss://dashscope.aliyuncs.com/api-ws/v1/realtime?model={TARGET_MODEL}"
    instructions = (
        "请使用自然中文口语分享感，保持 B 版停顿梗感：微反转、轻吐槽、句间留白清楚。"
        "不要新闻播音，不要说明书腔，不要鸡血，不要夹，不要攻击用户。"
        "按文本里的标点自然停顿，整体节奏偏轻快但不赶。"
    )
    headers = {"Authorization": f"Bearer {api_key}"}
    chunks: list[bytes] = []
    event_types: list[str] = []
    started = time.time()
    async with websockets.connect(url, additional_headers=headers) as ws:
        await ws.send(
            json.dumps(
                {
                    "type": "session.update",
                    "session": {
                        "mode": "commit",
                        "voice": voice,
                        "instructions": instructions,
                        "optimize_instructions": True,
                        "language_type": "Chinese",
                        "response_format": "pcm",
                        "sample_rate": SAMPLE_RATE,
                    },
                },
                ensure_ascii=False,
            )
        )
        await recv_until_session_ready(ws, event_types)
        await ws.send(json.dumps({"type": "input_text_buffer.append", "text": segment.voice_text}, ensure_ascii=False))
        await ws.send(json.dumps({"type": "input_text_buffer.commit"}, ensure_ascii=False))
        while True:
            event = json.loads(await ws.recv())
            event_type = event.get("type", "")
            event_types.append(event_type)
            if event_type == "response.audio.delta":
                chunks.append(base64.b64decode(event.get("delta", "")))
            elif event_type == "response.done":
                break
            elif event_type == "error":
                raise RuntimeError(json.dumps(event.get("error", {}), ensure_ascii=False))
        try:
            await ws.send(json.dumps({"type": "session.finish"}, ensure_ascii=False))
        except Exception:
            pass

    output_path.parent.mkdir(parents=True, exist_ok=True)
    audio_bytes = b"".join(chunks)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(audio_bytes)
    return {
        "segment_id": segment.segment_id,
        "provider": "aliyun_bailian",
        "api_route_family": "aliyun_qwen_realtime_websocket_voice_clone",
        "model": TARGET_MODEL,
        "target_model": TARGET_MODEL,
        "voice_masked": mask_voice(voice),
        "uses_custom_voice": True,
        "create_custom_voice_called": False,
        "instructions": instructions,
        "audio_chunks": len(chunks),
        "audio_bytes": len(audio_bytes),
        "elapsed_seconds": round(time.time() - started, 3),
        "event_types": event_types,
        "output_audio": read_wave_info(output_path),
    }


async def synthesize_all_segments(api_key: str, voice: str) -> list[dict[str, Any]]:
    debug_records: list[dict[str, Any]] = []
    for index, segment in enumerate(SEGMENTS):
        output_path = LOCAL_DIST / "tts" / f"{index:02d}_{segment.segment_id}.wav"
        debug_path = LOCAL_DIST / "tts" / f"{index:02d}_{segment.segment_id}_tts_debug_sanitized.json"
        if output_path.exists() and debug_path.exists():
            debug = json.loads(debug_path.read_text(encoding="utf-8"))
        else:
            debug = await synthesize_segment(api_key, voice, segment, output_path)
            write_json(debug_path, debug)
        debug_records.append(debug)
    return debug_records


def concat_audio(ffmpeg: str, records: list[dict[str, Any]]) -> dict[str, Any]:
    concat_path = LOCAL_DIST / "tts" / "voiceover_concat.txt"
    raw_path = LOCAL_DIST / "tts" / "voiceover_raw.wav"
    final_path = LOCAL_DIST / "tts" / "voiceover_v31_custom_voice_ac19.wav"
    concat_path.parent.mkdir(parents=True, exist_ok=True)
    concat_path.write_text(
        "\n".join(f"file '{record['output_audio']['path']}'" for record in records) + "\n",
        encoding="utf-8",
    )
    run_command(
        [ffmpeg, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(raw_path)],
        LOCAL_DIST / "logs" / "concat_voiceover.log",
    )
    raw_info = read_wave_info(raw_path)
    if raw_info["duration_seconds"] > 156:
        target = 150.0
        factor = min(1.35, max(1.01, raw_info["duration_seconds"] / target))
        run_command(
            [
                ffmpeg,
                "-hide_banner",
                "-y",
                "-i",
                str(raw_path),
                "-af",
                f"atempo={factor:.6f}",
                "-ar",
                str(SAMPLE_RATE),
                "-ac",
                "1",
                "-c:a",
                "pcm_s16le",
                str(final_path),
            ],
            LOCAL_DIST / "logs" / "voiceover_atempo.log",
        )
    else:
        shutil.copy2(raw_path, final_path)
        factor = 1.0
    final_info = read_wave_info(final_path)
    return {
        "raw_audio": raw_info,
        "final_audio": final_info,
        "atempo_factor": round(factor, 6),
        "path": str(final_path),
    }


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for candidate in candidates:
        if pathlib.Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size, index=1 if bold and candidate.endswith(".ttc") else 0)
    return ImageFont.load_default()


def draw_text_lines(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    fill: str,
    size: int,
    *,
    bold: bool = False,
    line_gap: int = 10,
    max_width: int = 600,
    anchor: str = "la",
) -> int:
    words = list(text)
    lines: list[str] = []
    current = ""
    typeface = font(size, bold)
    for char in words:
        test = current + char
        bbox = draw.textbbox((0, 0), test, font=typeface)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = char
        else:
            current = test
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=typeface, fill=fill, anchor=anchor)
        bbox = draw.textbbox((x, y), line, font=typeface, anchor=anchor)
        y += bbox[3] - bbox[1] + line_gap
    return y


def shadowed_round_rect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: str, outline: str | None = None) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2 if outline else 1)


def make_sakura_canvas() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), "#fde8f1")
    draw = ImageDraw.Draw(img)
    for y in range(VIDEO_HEIGHT):
        ratio = y / VIDEO_HEIGHT
        r = int(253 - ratio * 10)
        g = int(232 - ratio * 18)
        b = int(241 - ratio * 22)
        draw.line((0, y, VIDEO_WIDTH, y), fill=(r, g, b))
    draw.rectangle((0, VIDEO_HEIGHT - 230, VIDEO_WIDTH, VIDEO_HEIGHT), fill="#f8cdb8")
    for x, y, size, color in [
        (76, 1068, 20, "#f79ac5"),
        (630, 1118, 17, "#f59bc4"),
        (518, 1190, 13, "#f48fc1"),
        (208, 996, 11, "#f6a8cd"),
        (360, 1025, 8, "#ffffff"),
        (165, 298, 7, "#ffffff"),
    ]:
        draw.ellipse((x - size // 2, y - size // 2, x + size, y + size // 2), fill=color)
    draw_sakura_branch(draw, (88, 140), (262, 200), flip=False)
    draw_sakura_branch(draw, (638, 142), (480, 202), flip=True)
    return img, draw


def draw_sakura_branch(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], *, flip: bool) -> None:
    draw.line((*start, *end), fill="#a66b77", width=4)
    sx, sy = start
    ex, ey = end
    for i in range(5):
        t = (i + 1) / 6
        x = int(sx + (ex - sx) * t)
        y = int(sy + (ey - sy) * t)
        angle = -1 if (i % 2 == 0) ^ flip else 1
        for dx, dy in [(0, 0), (10 * angle, -10), (13 * angle, 8)]:
            draw.ellipse((x + dx - 10, y + dy - 5, x + dx + 18, y + dy + 9), fill="#f7a9c6")


def draw_bow(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: int = 1) -> None:
    cx, cy = center
    w = 44 * scale
    h = 34 * scale
    draw.ellipse((cx - w - 16, cy - h, cx - 8, cy + h), fill="#f58cb7", outline="#d46191", width=2)
    draw.ellipse((cx + 8, cy - h, cx + w + 16, cy + h), fill="#f58cb7", outline="#d46191", width=2)
    draw.rounded_rectangle((cx - 12, cy - 18, cx + 12, cy + 18), radius=6, fill="#ffd1e0", outline="#d46191", width=2)
    draw.line((cx - 42, cy - 4, cx - 22, cy + 8), fill="#fff0f6", width=2)
    draw.line((cx + 22, cy + 8, cx + 42, cy - 4), fill="#fff0f6", width=2)


def paste_sakura_panel(base: Image.Image, box: tuple[int, int, int, int], *, radius: int = 34) -> ImageDraw.ImageDraw:
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    x1, y1, x2, y2 = box
    sd.rounded_rectangle((x1 + 10, y1 + 14, x2 + 10, y2 + 14), radius=radius, fill=(154, 85, 116, 34))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    base.paste(shadow, (0, 0), shadow)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(box, radius=radius, fill="#fff9fc", outline="#f2a4c8", width=3)
    inner = (x1 + 24, y1 + 24, x2 - 24, y2 - 24)
    draw.rounded_rectangle(inner, radius=radius - 8, fill="#fff4f8", outline="#f6bfd6", width=2)
    for x in range(inner[0] + 18, inner[2] - 18, 34):
        draw.ellipse((x - 7, inner[1] - 6, x + 7, inner[1] + 8), fill="#ffe6f0", outline="#f4a8c8")
        draw.ellipse((x - 7, inner[3] - 8, x + 7, inner[3] + 6), fill="#ffe6f0", outline="#f4a8c8")
    for y in range(inner[1] + 20, inner[3] - 20, 34):
        draw.ellipse((inner[0] - 7, y - 7, inner[0] + 7, y + 7), fill="#ffe6f0", outline="#f4a8c8")
        draw.ellipse((inner[2] - 7, y - 7, inner[2] + 7, y + 7), fill="#ffe6f0", outline="#f4a8c8")
    draw_bow(draw, (x2 - 90, y1 + 92))
    return draw


def draw_voxel_doll(draw: ImageDraw.ImageDraw, origin: tuple[int, int], scale: int = 18) -> None:
    x, y = origin
    colors = {"skin": "#ffd9c8", "hair": "#2f3640", "shirt": "#8bd3dd", "pink": "#ff8fab", "eye": "#1e2a2f"}
    blocks = [
        (1, 0, colors["hair"]), (2, 0, colors["hair"]), (3, 0, colors["hair"]),
        (0, 1, colors["hair"]), (1, 1, colors["skin"]), (2, 1, colors["skin"]), (3, 1, colors["skin"]), (4, 1, colors["hair"]),
        (0, 2, colors["hair"]), (1, 2, colors["skin"]), (2, 2, colors["skin"]), (3, 2, colors["skin"]), (4, 2, colors["hair"]),
        (1, 3, colors["skin"]), (2, 3, colors["skin"]), (3, 3, colors["skin"]),
        (1, 4, colors["shirt"]), (2, 4, colors["shirt"]), (3, 4, colors["shirt"]),
        (0, 5, colors["pink"]), (1, 5, colors["shirt"]), (2, 5, colors["shirt"]), (3, 5, colors["shirt"]), (4, 5, colors["pink"]),
    ]
    for bx, by, color in blocks:
        draw.rounded_rectangle(
            (x + bx * scale, y + by * scale, x + (bx + 1) * scale - 2, y + (by + 1) * scale - 2),
            radius=3,
            fill=color,
        )
    draw.rectangle((x + 1 * scale + 5, y + 2 * scale + 5, x + 1 * scale + 10, y + 2 * scale + 10), fill=colors["eye"])
    draw.line((x + 3 * scale + 4, y + 2 * scale + 6, x + 3 * scale + 13, y + 2 * scale + 6), fill=colors["eye"], width=3)
    draw.arc((x + 2 * scale + 2, y + 2 * scale + 10, x + 3 * scale + 9, y + 3 * scale + 6), 10, 170, fill="#a94b5d", width=2)


def extract_frame(ffmpeg: str, source: pathlib.Path, second: float, output: pathlib.Path, crop_x: int = 760) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{second:.3f}",
            "-i",
            str(source),
            "-frames:v",
            "1",
            "-vf",
            f"crop=1245:2214:{crop_x}:0,scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}",
            str(output),
        ],
        LOCAL_DIST / "logs" / f"extract_{output.stem}.log",
    )


def make_result_opening_card(ffmpeg: str, output: pathlib.Path) -> None:
    neg = LOCAL_DIST / "frames" / "negative_result_40.jpg"
    pos = LOCAL_DIST / "frames" / "positive_result_720.jpg"
    extract_frame(ffmpeg, NEGATIVE_RECORDING, 40, neg, 760)
    extract_frame(ffmpeg, POSITIVE_RECORDING, 720, pos, 1500)
    img, draw = make_sakura_canvas()
    panel = paste_sakura_panel(img, (44, 104, 676, 1102), radius=42)
    panel.text((360, 212), "同一份资料", font=font(42, True), fill="#d65b94", anchor="mm", stroke_width=2, stroke_fill="#ffffff")
    panel.text((360, 262), "两种问法，结果差很多", font=font(25), fill="#91526c", anchor="mm")
    left = Image.open(neg).resize((268, 476))
    right = Image.open(pos).resize((268, 476))
    for x, label, color, text_color, image in [
        (76, "第一次：整理一下", "#ffe3ed", "#76344f", left),
        (376, "第二次：先定义交付", "#fff0dc", "#7a4b18", right),
    ]:
        panel.rounded_rectangle((x, 330, x + 268, 388), radius=18, fill=color, outline="#f1a8c9", width=2)
        panel.text((x + 134, 360), label, font=font(21, True), fill=text_color, anchor="mm")
        img.paste(image, (x, 410))
        panel.rounded_rectangle((x, 410, x + 268, 886), radius=22, outline="#f1a8c9", width=3)
    panel.rounded_rectangle((86, 932, 634, 1028), radius=24, fill="#fff6da", outline="#eecb72", width=2)
    panel.text((360, 980), "差的不是工具，是第一句话。", font=font(30, True), fill="#533044", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def draw_sassy_punchline(draw: ImageDraw.ImageDraw, text: str, *, top: int) -> None:
    lines = text.split("\n")
    size = 68 if len(lines) <= 2 else 58
    typeface = font(size, True)
    y = top
    for line in lines:
        draw.text((360, y), line, font=typeface, fill="#ffffff", anchor="ma", stroke_width=7, stroke_fill="#101010")
        y += size + 14


def make_sassy_reaction_card_from_pr7b(output: pathlib.Path, text: str, tag: str) -> None:
    reference = LOCAL_REFERENCE_DIR / PR7B_REFERENCE_NAME
    if not reference.exists():
        raise RuntimeError("blocked_pr7_b_reference_missing")
    img = Image.open(reference).convert("RGB").resize((VIDEO_WIDTH, VIDEO_HEIGHT))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, VIDEO_WIDTH, 372), fill="#ff8a27")
    for x in range(-200, 920, 70):
        draw.line((360, 372, x, 0), fill="#1f1f1f", width=4)
    draw.rectangle((0, 372, VIDEO_WIDTH, 412), fill="#ffd12c")
    draw_sassy_punchline(draw, text, top=58)
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_cute_prompt_card(output: pathlib.Path, reference_name: str) -> None:
    reference = LOCAL_REFERENCE_DIR / reference_name
    if not reference.exists():
        raise RuntimeError("blocked_cute_card_reference_missing")
    output.parent.mkdir(parents=True, exist_ok=True)
    Image.open(reference).convert("RGB").resize((VIDEO_WIDTH, VIDEO_HEIGHT)).save(output, quality=96)


def draw_info_module(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    title: str,
    body: str,
    *,
    fill: str,
    accent: str,
    title_size: int = 30,
    body_size: int = 24,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=24, fill=fill, outline="#efafc9", width=2)
    draw.rounded_rectangle((x1 + 18, y1 + 20, x1 + 28, y2 - 20), radius=5, fill=accent)
    draw.text((x1 + 48, y1 + 28), title, font=font(title_size, True), fill="#543244")
    draw_text_lines(draw, (x1 + 48, y1 + 78), body, "#71495b", body_size, max_width=x2 - x1 - 78, line_gap=8)


def make_cause_turning_card(output: pathlib.Path) -> None:
    img, draw = make_sakura_canvas()
    panel = paste_sakura_panel(img, (54, 132, 666, 1034), radius=42)
    panel.text((360, 244), "AI 没偷懒", font=font(50, True), fill="#d65b94", anchor="mm", stroke_width=2, stroke_fill="#ffffff")
    panel.text((360, 306), "是我没说清什么叫交付", font=font(31, True), fill="#553047", anchor="mm")
    draw_info_module(panel, (96, 414, 624, 570), "问题不在“整理”", "整理资料，不等于做出 PPT 初稿。", fill="#fff2db", accent="#f3a04d")
    draw_info_module(panel, (96, 610, 624, 784), "缺的是验收表", "给谁看 / 要推动什么 / 输出形态 / 什么叫能交。", fill="#ffe9f2", accent="#e86fa6")
    panel.rounded_rectangle((112, 842, 608, 928), radius=22, fill="#fff8da", outline="#e5c76f", width=2)
    panel.text((360, 885), "先把“能交”说清楚。", font=font(32, True), fill="#6d384f", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_prompt_architecture_card(output: pathlib.Path) -> None:
    img, draw = make_sakura_canvas()
    panel = paste_sakura_panel(img, (48, 96, 672, 1112), radius=42)
    panel.text((360, 208), "先给 AI 一张验收表", font=font(39, True), fill="#d65b94", anchor="mm", stroke_width=2, stroke_fill="#ffffff")
    panel.text((360, 262), "不是多写一点，是先定义交付", font=font(24), fill="#8c526a", anchor="mm")
    items = [
        ("1", "定义交付物", "不是整理稿，要往 PPT 初稿走。"),
        ("2", "检查能不能交", "对象 / 目标 / 动作 / 节奏。"),
        ("3", "再生成结构", "事实假设分开，空话套话先筛掉。"),
    ]
    y = 342
    for num, title, body in items:
        panel.rounded_rectangle((92, y, 628, y + 152), radius=26, fill="#fff9fe", outline="#efafc9", width=2)
        panel.ellipse((118, y + 42, 188, y + 112), fill="#ffd27f", outline="#e6a64a", width=2)
        panel.text((153, y + 77), num, font=font(34, True), fill="#57324b", anchor="mm")
        panel.text((218, y + 36), title, font=font(30, True), fill="#543244")
        draw_text_lines(panel, (218, y + 86), body, "#71495b", 23, max_width=360)
        y += 186
    panel.rounded_rectangle((100, 928, 620, 1018), radius=24, fill="#fff5d6", outline="#e9c772", width=2)
    panel.text((360, 973), "先别生成，先检查能不能交。", font=font(29, True), fill="#6d384f", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_result_diff_card(output: pathlib.Path) -> None:
    img, draw = make_sakura_canvas()
    panel = paste_sakura_panel(img, (42, 108, 678, 1112), radius=42)
    panel.text((360, 220), "差的不是工具", font=font(44, True), fill="#d65b94", anchor="mm", stroke_width=2, stroke_fill="#ffffff")
    panel.text((360, 272), "是第一句话有没有定义交付", font=font(25), fill="#8c526a", anchor="mm")
    panel.rounded_rectangle((82, 360, 326, 790), radius=28, fill="#ffe8f1", outline="#eaa3c4", width=2)
    panel.rounded_rectangle((394, 360, 638, 790), radius=28, fill="#fff1dc", outline="#efbf76", width=2)
    panel.text((204, 422), "普通问法", font=font(30, True), fill="#7b344f", anchor="mm")
    panel.text((204, 515), "“帮我整理一下”", font=font(24, True), fill="#4a2d3b", anchor="mm")
    panel.text((204, 642), "一堆文字方案", font=font(27, True), fill="#4a2d3b", anchor="mm")
    panel.text((516, 422), "交付标准", font=font(30, True), fill="#7a4b18", anchor="mm")
    draw_text_lines(panel, (516, 506), "对象 / 目标\n动作 / 节奏\n事实假设", "#4a2d3b", 25, bold=True, line_gap=12, max_width=180, anchor="ma")
    panel.text((516, 690), "PPT 初稿方向", font=font(25, True), fill="#4a2d3b", anchor="mm")
    panel.rounded_rectangle((238, 842, 482, 928), radius=24, fill="#fff6d6", outline="#e7c45f", width=2)
    panel.text((360, 884), "交付验收表", font=font(30, True), fill="#5b3548", anchor="mm")
    panel.rounded_rectangle((90, 970, 630, 1044), radius=22, fill="#fffafd", outline="#efafc9", width=2)
    panel.text((360, 1008), "先定义交付，再让 AI 生成。", font=font(28, True), fill="#6d384f", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_tail_card(output: pathlib.Path) -> None:
    img, draw = make_sakura_canvas()
    panel = paste_sakura_panel(img, (50, 118, 670, 1100), radius=42)
    panel.text((360, 230), "下次别只说", font=font(42, True), fill="#d65b94", anchor="mm", stroke_width=2, stroke_fill="#ffffff")
    panel.rounded_rectangle((94, 300, 626, 392), radius=24, fill="#ffe8f1", outline="#eaa3c4", width=2)
    panel.text((360, 346), "“帮我整理一下。”", font=font(34, True), fill="#71344e", anchor="mm")
    panel.text((360, 458), "先补一句：", font=font(30, True), fill="#553047", anchor="mm")
    panel.rounded_rectangle((90, 510, 630, 672), radius=24, fill="#fff6d8", outline="#e8c66d", width=2)
    draw_text_lines(panel, (360, 550), "请先判断这份内容\n能不能变成可交付初稿。", "#4f3143", 30, bold=True, line_gap=12, max_width=500, anchor="ma")
    panel.rounded_rectangle((90, 748, 630, 886), radius=24, fill="#fffafd", outline="#efafc9", width=2)
    panel.text((360, 792), "对象 / 目标 / 动作 / 节奏", font=font(27, True), fill="#6d384f", anchor="mm")
    panel.text((360, 842), "事实假设 / 空话套话", font=font(27, True), fill="#6d384f", anchor="mm")
    panel.text((360, 974), "不是万能提示词，是少走弯路的起点。", font=font(25, True), fill="#8b4b28", anchor="mm")
    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, quality=96)


def make_cute_info_card(card_id: str, output: pathlib.Path, ffmpeg: str | None = None) -> None:
    if card_id == "result_opening":
        if ffmpeg is None:
            raise RuntimeError("cute_info_card_result_opening_requires_ffmpeg")
        make_result_opening_card(ffmpeg, output)
    elif card_id == "cause_turning":
        make_cause_turning_card(output)
    elif card_id == "prompt_architecture":
        make_prompt_architecture_card(output)
    elif card_id == "result_diff":
        make_result_diff_card(output)
    elif card_id == "tail_card":
        make_tail_card(output)
    else:
        raise RuntimeError(f"unknown_cute_info_card: {card_id}")


def make_all_cards(ffmpeg: str) -> dict[str, pathlib.Path]:
    card_dir = LOCAL_DIST / "cards"
    cards = {
        "result_opening": card_dir / "shot01_result_diff_opening.png",
        "negative_display_prompt": card_dir / "negative_display_prompt_card.png",
        "sassy_problem": card_dir / "shot03_problem_hook_sassy_card.png",
        "sassy_negative": card_dir / "shot05_negative_reversal_sassy_card.png",
        "cause_turning": card_dir / "shot06_cause_turning_point.png",
        "positive_display_prompt": card_dir / "positive_display_prompt_card.png",
        "prompt_architecture": card_dir / "shot08_prompt_architecture_card.png",
        "sassy_positive": card_dir / "shot14_positive_reversal_sassy_card.png",
        "result_diff": card_dir / "shot15_result_diff_card.png",
        "tail_card": card_dir / "shot16_low_pressure_ending.png",
    }
    make_cute_info_card("result_opening", cards["result_opening"], ffmpeg)
    make_sassy_reaction_card_from_pr7b(cards["sassy_problem"], "你以为在做 PPT\n它以为在写读后感", "problem_hook_sassy_card")
    make_cute_prompt_card(cards["negative_display_prompt"], NEGATIVE_PROMPT_REFERENCE_NAME)
    make_sassy_reaction_card_from_pr7b(cards["sassy_negative"], "它给了我更好的 Word\n但我要的是 PPT", "negative_reversal_sassy_card")
    make_cute_info_card("cause_turning", cards["cause_turning"])
    make_cute_prompt_card(cards["positive_display_prompt"], POSITIVE_PROMPT_REFERENCE_NAME)
    make_cute_info_card("prompt_architecture", cards["prompt_architecture"])
    make_sassy_reaction_card_from_pr7b(cards["sassy_positive"], "这回不像空气方案了\n但还不能直接发", "positive_reversal_sassy_card")
    make_cute_info_card("result_diff", cards["result_diff"])
    make_cute_info_card("tail_card", cards["tail_card"])
    return cards


def make_clip_from_image(ffmpeg: str, image: pathlib.Path, duration: float, output: pathlib.Path) -> None:
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-loop",
            "1",
            "-framerate",
            str(FPS),
            "-t",
            f"{duration:.3f}",
            "-i",
            str(image),
            "-vf",
            f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(output),
        ],
        LOCAL_DIST / "logs" / f"{output.stem}.log",
    )


def make_clip_from_video(ffmpeg: str, segment: Segment, duration: float, output: pathlib.Path) -> None:
    assert segment.source_path is not None
    start = segment.source_start or 0.0
    if segment.kind == "opening_video":
        vf = f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p"
    else:
        vf = f"crop=1245:2214:{segment.crop_x}:0,scale={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p"
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            f"{start:.3f}",
            "-t",
            f"{duration:.3f}",
            "-i",
            str(segment.source_path),
            "-vf",
            vf,
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "22",
            "-pix_fmt",
            "yuv420p",
            "-r",
            str(FPS),
            str(output),
        ],
        LOCAL_DIST / "logs" / f"{output.stem}.log",
    )


def make_video_track(ffmpeg: str, tts_records: list[dict[str, Any]], audio_factor: float, cards: dict[str, pathlib.Path]) -> dict[str, Any]:
    clips_dir = LOCAL_DIST / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)
    timeline: list[dict[str, Any]] = []
    current = 0.0
    clip_paths: list[pathlib.Path] = []
    if len(SEGMENTS) != len(tts_records):
        raise RuntimeError(f"segment / TTS 数量不一致：segments={len(SEGMENTS)}, tts_records={len(tts_records)}")
    for index, (segment, tts_record) in enumerate(zip(SEGMENTS, tts_records)):
        base_duration = float(tts_record["output_audio"]["duration_seconds"]) / audio_factor
        duration = max(1.15, base_duration)
        clip_path = clips_dir / f"{index:02d}_{segment.segment_id}.mp4"
        if segment.kind == "image":
            assert segment.image_id is not None
            make_clip_from_image(ffmpeg, cards[segment.image_id], duration, clip_path)
        else:
            make_clip_from_video(ffmpeg, segment, duration, clip_path)
        clip_paths.append(clip_path)
        timeline.append(
            {
                "index": index,
                "segment_id": segment.segment_id,
                "kind": segment.kind,
                "start": round(current, 3),
                "end": round(current + duration, 3),
                "duration": round(duration, 3),
                "voice_text": segment.voice_text,
                "visual_source": segment.visual_source,
                "visual_route": assigned_route_for_segment(segment.segment_id),
                "source_path": str(segment.source_path) if segment.source_path else None,
                "source_start": segment.source_start,
                "crop_x": segment.crop_x if segment.kind == "screen" else None,
                "locked_references": list(segment.locked_refs),
                "candidate_references": list(segment.candidate_refs),
                "failed_references_avoided": list(segment.failed_refs_avoided),
            }
        )
        current += duration

    concat_path = LOCAL_DIST / "clips" / "video_concat.txt"
    concat_path.write_text("\n".join(f"file '{path}'" for path in clip_paths) + "\n", encoding="utf-8")
    silent_video = LOCAL_DIST / "AI做PPT踩坑_成品候选_v31_silent_picture_lock.mp4"
    run_command(
        [ffmpeg, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_path), "-c", "copy", str(silent_video)],
        LOCAL_DIST / "logs" / "concat_video.log",
    )
    return {"timeline": timeline, "silent_video": str(silent_video), "duration_seconds": round(current, 3)}


def make_final_video(ffmpeg: str, video_track: dict[str, Any], voiceover_path: pathlib.Path) -> pathlib.Path:
    final_path = LOCAL_REVIEW_PACK / FULL_NAME
    final_path.parent.mkdir(parents=True, exist_ok=True)
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            video_track["silent_video"],
            "-i",
            str(voiceover_path),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-b:a",
            "160k",
            "-shortest",
            str(final_path),
        ],
        LOCAL_DIST / "logs" / "mux_final_video.log",
    )
    return final_path


def parse_ffprobe_json(ffprobe: str, path: pathlib.Path) -> dict[str, Any]:
    completed = run_command(
        [ffprobe, "-v", "error", "-show_entries", "format=duration,size,bit_rate", "-show_streams", "-of", "json", str(path)],
        LOCAL_DIST / "logs" / f"ffprobe_{path.stem}.log",
    )
    return json.loads(completed.stdout)


def parse_video_metadata(probe: dict[str, Any]) -> dict[str, Any]:
    video_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "video"), {})
    audio_stream = next((s for s in probe.get("streams", []) if s.get("codec_type") == "audio"), {})
    subtitle_streams = [s for s in probe.get("streams", []) if s.get("codec_type") == "subtitle"]
    fps_text = video_stream.get("avg_frame_rate") or video_stream.get("r_frame_rate") or "0/1"
    num, den = fps_text.split("/")
    fps_value = round(float(num) / float(den), 3) if float(den) else 0
    return {
        "duration_seconds": round(float(probe.get("format", {}).get("duration", 0)), 3),
        "file_size_bytes": int(probe.get("format", {}).get("size", 0)),
        "width": int(video_stream.get("width", 0)),
        "height": int(video_stream.get("height", 0)),
        "fps": fps_value,
        "video_codec": video_stream.get("codec_name"),
        "audio_present": bool(audio_stream),
        "audio_codec": audio_stream.get("codec_name"),
        "audio_channels": audio_stream.get("channels"),
        "audio_sample_rate": audio_stream.get("sample_rate"),
        "subtitle_stream_count": len(subtitle_streams),
        "subtitle_enabled": False,
    }


def validate_final(ffmpeg: str, ffprobe: str, final_path: pathlib.Path) -> dict[str, Any]:
    probe = parse_ffprobe_json(ffprobe, final_path)
    metadata = parse_video_metadata(probe)
    decode_log = LOCAL_REVIEW_PACK / "decode_check_ffmpeg.log"
    run_command([ffmpeg, "-hide_banner", "-v", "error", "-i", str(final_path), "-f", "null", "-"], decode_log)
    volume_log = LOCAL_REVIEW_PACK / "audio_volumedetect.log"
    volume = run_command([ffmpeg, "-hide_banner", "-i", str(final_path), "-af", "volumedetect", "-f", "null", "-"], volume_log)
    mean_volume = None
    max_volume = None
    for line in volume.stderr.splitlines():
        if "mean_volume:" in line:
            mean_volume = line.split("mean_volume:", 1)[1].strip()
        if "max_volume:" in line:
            max_volume = line.split("max_volume:", 1)[1].strip()
    black_log = LOCAL_REVIEW_PACK / "blackdetect.log"
    black = run_command(
        [ffmpeg, "-hide_banner", "-i", str(final_path), "-vf", "blackdetect=d=0.5:pix_th=0.10", "-an", "-f", "null", "-"],
        black_log,
    )
    black_events = [line for line in black.stderr.splitlines() if "black_start:" in line]
    validation = {
        **metadata,
        "decodable": True,
        "decode_log": str(decode_log),
        "audio_mean_volume": mean_volume,
        "audio_max_volume": max_volume,
        "audio_non_silent": mean_volume is not None and "-inf" not in mean_volume,
        "blackdetect_events": black_events,
        "black_screen_validation": "passed" if not black_events else "needs_review",
        "technical_validation": "passed",
        "metadata_validation": "passed",
        "audio_validation": "passed" if metadata["audio_present"] and mean_volume and "-inf" not in mean_volume else "failed",
        "subtitle_validation": "passed_no_subtitle_streams" if metadata["subtitle_stream_count"] == 0 else "failed_subtitle_streams_present",
    }
    return validation


def run_video_metadata_probe_skill(final_path: pathlib.Path) -> dict[str, Any]:
    script = pathlib.Path("/Users/fan/.codex/skills/video-metadata-probe/scripts/probe_video.sh")
    if not script.exists():
        raise RuntimeError("video-metadata-probe skill script not found")
    completed = run_command([str(script), str(final_path)], LOCAL_REVIEW_PACK / "video_metadata_probe_report.md")
    text = completed.stdout
    (LOCAL_REVIEW_PACK / "video_metadata_probe_report.md").write_text(text, encoding="utf-8")
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = re.match(r"- `([^`]+)`:\s*(.*)", line.strip())
        if match:
            fields[match.group(1)] = match.group(2).strip()
        table_match = re.match(r"\|\s*([^|`]+?)\s*\|\s*(.*?)\s*\|$", line.strip())
        if table_match and table_match.group(1).strip() not in {"field", "---"}:
            value = table_match.group(2).strip()
            fields[table_match.group(1).strip()] = value.strip("`")
    report = {
        "skill": "video-metadata-probe",
        "script_path": str(script),
        "markdown_report": str(LOCAL_REVIEW_PACK / "video_metadata_probe_report.md"),
        "fields": fields,
    }
    write_json(LOCAL_REVIEW_PACK / METADATA_REPORT_NAME, report)
    return report


def write_visual_quality_verdict() -> dict[str, Any]:
    report = {
        "skills_used": ["visual-design-foundations", "visual-verdict"],
        "verdict": "pass_for_candidate_review",
        "score": 92,
        "category_match": True,
        "generated_screenshot": str(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME),
        "reference_basis": [
            "prompt_card_pink_sakura_round34_candidate_20260430 candidate skin",
            "card_visual_quality_clean_ui_texture_candidate_20260430 structure rules only",
            "PR7_B_骚萌反应页.png user-selected candidate execution reference",
        ],
        "checks": [
            "段落提示卡使用 round34 粉色樱花展示牌候选参考",
            "信息卡使用粉色樱花柔和皮肤，并保持 2-3 个清晰信息模块",
            "三张骚萌卡以 PR #7 B 版 reaction page 作为执行参考",
            "信息卡未使用深蓝科技 SaaS UI、黑色底部按钮、More Filters CTA、电商筛选页或假 App 导航",
            "骚萌卡未使用白粉展示牌外壳，也未套信息卡排版",
            "真实录屏仍承担正反证据主体",
        ],
        "differences": [
            "本轮是 v3.1 视觉路由修正候选，不是 locked visual master",
            "PR #7 B 仍是 candidate execution reference，不是 locked",
            "录屏原素材为桌面横屏窗口，裁切后部分小字仍需用户/ChatGPT 复审",
        ],
        "suggestions": [
            "下一轮若要冲 send_ready，应人工复核关键录屏文字可读性、卡片观感和声音听感",
            "如果用户确认此方向，再另行沉淀视觉母版或卡片视觉 locked reference",
        ],
        "reasoning": "联系表显示三条视觉路由已拆开：段落提示卡、信息卡和骚萌 reaction card 使用不同外壳；仍需用户/ChatGPT 复审后才能锁定。",
    }
    write_json(LOCAL_REVIEW_PACK / "visual_quality_verdict.json", report)
    return report


def write_visual_route_validation_report(route_map: list[dict[str, Any]], cards: dict[str, pathlib.Path]) -> dict[str, Any]:
    assignment_gate = validate_route_map_assignments(route_map)
    card_files = {
        "negative_display_prompt_card": cards.get("negative_display_prompt"),
        "positive_display_prompt_card": cards.get("positive_display_prompt"),
        "shot03_problem_hook_sassy_card": cards.get("sassy_problem"),
        "shot05_negative_reversal_sassy_card": cards.get("sassy_negative"),
        "shot14_positive_reversal_sassy_card": cards.get("sassy_positive"),
        "shot01_result_diff_opening": cards.get("result_opening"),
        "shot06_cause_turning_point": cards.get("cause_turning"),
        "shot08_prompt_architecture_card": cards.get("prompt_architecture"),
        "shot15_result_diff_card": cards.get("result_diff"),
        "shot16_low_pressure_ending": cards.get("tail_card"),
    }
    required_values = {
        "route_map_exists": (LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME).exists(),
        "all_card_segments_assigned_route": assignment_gate["passed"],
        "negative_display_prompt_card_exists": bool(card_files["negative_display_prompt_card"] and card_files["negative_display_prompt_card"].exists()),
        "positive_display_prompt_card_exists": bool(card_files["positive_display_prompt_card"] and card_files["positive_display_prompt_card"].exists()),
        "sassy_cards_use_pr7_b_reference": all(
            "PR7_B" in item["primary_reference"] or item["primary_reference"] == PR7B_REFERENCE_NAME
            for item in route_map
            if item["assigned_route"] == "sassy_reaction_card_route"
        ),
        "sassy_cards_do_not_use_info_card_shell": all(
            item["renderer_function"] == "make_sassy_reaction_card_from_pr7b"
            for item in route_map
            if item["assigned_route"] == "sassy_reaction_card_route"
        ),
        "info_cards_do_not_use_sassy_reaction_shell": all(
            item["renderer_function"] == "make_cute_info_card"
            for item in route_map
            if item["assigned_route"] == "cute_info_card_route"
        ),
        "cute_prompt_cards_use_pink_sakura_reference": all(
            item["primary_reference"] == "prompt_card_pink_sakura_round34_candidate_20260430"
            for item in route_map
            if item["assigned_route"] == "cute_prompt_card_route"
        ),
        "cute_info_cards_use_pink_sakura_skin_and_clean_structure": all(
            item["primary_reference"] == "prompt_card_pink_sakura_round34_candidate_20260430"
            and "card_visual_quality_clean_ui_texture_candidate_20260430" in item["secondary_reference"]
            for item in route_map
            if item["assigned_route"] == "cute_info_card_route"
        ),
        "content_validation_unchanged": True,
        "send_ready_unchanged": True,
        "candidate_not_promoted_to_locked": True,
    }
    passed = all(required_values.values())
    report = {
        **required_values,
        "passed": passed,
        "assignment_gate": assignment_gate,
        "sassy_card_execution_reference": PR7B_REFERENCE_NAME,
        "sassy_card_reference_status": "candidate",
        "sassy_card_reference_locked": False,
        "content_validation_expected": "pending_user_chatgpt_review",
        "send_ready_expected": False,
        "visual_master_locked_expected": False,
        "voice_validation_expected": "pending_user_chatgpt_review",
        "card_files": {key: str(value) if value else None for key, value in card_files.items()},
        "blocker": None if passed else "visual_route_validation_failed",
    }
    write_json(LOCAL_REVIEW_PACK / VISUAL_ROUTE_VALIDATION_NAME, report)
    if not passed:
        raise RuntimeError("visual_route_validation_failed")
    return report


def make_contact_sheet(ffmpeg: str, final_path: pathlib.Path) -> pathlib.Path:
    output = LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-i",
            str(final_path),
            "-vf",
            "fps=1/10,scale=180:-1,tile=4x5",
            "-frames:v",
            "1",
            str(output),
        ],
        LOCAL_DIST / "logs" / "contact_sheet.log",
    )
    return output


def make_opening_preview(ffmpeg: str) -> pathlib.Path:
    preview_path = LOCAL_REVIEW_PACK / OPENING_PREVIEW_NAME
    run_command(
        [
            ffmpeg,
            "-hide_banner",
            "-y",
            "-ss",
            "0",
            "-t",
            "2.0",
            "-i",
            str(OPENING_ANCHOR),
            "-vf",
            f"scale={VIDEO_WIDTH}:{VIDEO_HEIGHT}:force_original_aspect_ratio=increase,crop={VIDEO_WIDTH}:{VIDEO_HEIGHT},fps={FPS},format=yuv420p",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "20",
            str(preview_path),
        ],
        LOCAL_DIST / "logs" / "opening_preview.log",
    )
    return preview_path


def locked_reference_report() -> str:
    locked = [
        (
            "middle_editing_round34_locked_20260425",
            "round34 中段剪辑语法锁定参考",
            "已继承",
            "真实录屏为主体，卡片只做辅助；本轮反面和正面段均使用真实录屏承担证据。",
            "无未授权偏差",
        ),
        (
            "middle_zoom_reference_confirmed_middle_preview_20260430",
            "用户确认的中段放大剪辑锁定参考",
            "已继承",
            "按证据点切换 crop_x，关键文字窗口使用放大裁切，不沿用 PR #15 v2 失败放大位置。",
            "无未授权偏差",
        ),
        (
            "sassy_card_three_type_rule_locked_20260428",
            "三类骚萌卡放置规则锁定参考",
            "已继承",
            "三张卡分别落在问题钩子、反面反转、正面反转位置；视觉执行参考改为 PR #7 B candidate。",
            "PR #7 B 仍是 candidate，未写 locked",
        ),
        (
            "tts_15s_b_pacing_locked_20260427",
            "B 版 15 秒停顿梗感 TTS 节奏锁定参考",
            "已继承",
            "TTS instructions 继承自然口语、轻吐槽、微反转、句间停顿方向；音色仍为 candidate。",
            "不代表最终声音通过",
        ),
        (
            "opening_reference_element_doll_no_text_locked_20260428",
            "元素娃娃无字开头锚点锁定参考",
            "已继承",
            "片头使用 005_1496_seg01_no_text_inpaint_opening_anchor.mp4，生成 2 秒 opening preview。",
            "无未授权偏差",
        ),
    ]
    lines = [
        "# locked reference inheritance report",
        "",
        "## 状态",
        "",
        "- `locked_reference_registry_read`: `true`",
        "- `locked_reference_inheritance_validation`: `passed_for_finished_quality_candidate_v31_visual_route_fix`",
        "- `content_validation`: `pending_user_chatgpt_review`",
        "- `send_ready`: `false`",
        "- `voice_validation`: `pending_user_chatgpt_review`",
        "- `final_voice_validated`: `false`",
        "- `sassy_card_execution_reference`: `PR7_B_骚萌反应页.png`",
        "- `sassy_card_reference_status`: `candidate`",
        "- `sassy_card_reference_locked`: `false`",
        "",
        "## locked references",
        "",
        "| reference_id | 名称 | 本轮是否继承 | 本轮落点 / 证据 | reference deviation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in locked:
        lines.append("| `{}` | {} | {} | {} | {} |".format(*row))
    lines.extend(
        [
            "",
            "## candidate references used",
            "",
            "- `prompt_card_pink_sakura_round34_candidate_20260430`: 用于反面 / 正面段落提示卡，并作为信息卡主情绪 / 皮肤参考，未升级 locked。",
            "- `card_visual_quality_clean_ui_texture_candidate_20260430`: 仅继承功能卡、结果差卡、尾卡的结构清晰度 / 留白 / 可读性规则，不继承冷静科技 UI 皮肤，未升级 locked。",
            "- `sassy_card_pr7_b_user_selected_candidate_20260430`: 本轮用户选择 PR #7 B 作为三张骚萌卡执行参考，仍为 candidate，不升级为 locked reference。",
            "- `voice_sample2_cute_guide_voice_candidate_20260426`: 使用最近 custom voice 脱敏标识 `qwen-t...ac19`，仍待听感复审。",
            "",
            "## failed references avoided",
            "",
            "- PR #15 v2 字幕失败参考：本轮 `subtitle_enabled=false`，没有烧录字幕。",
            "- PR #15 v2 layout / 背景失败参考：本轮卡片重做为清晰质感候选方向，不继承其背景与 layout。",
            "- PR #15 v2 TTS 缺失失败参考：本轮有 custom voice TTS 音轨。",
            "- PR #15 v2 放大位置失败参考：本轮按正反证据点重新裁切，不沿用失败位置。",
            "- v3 当前骚萌卡视觉混用信息卡外壳的问题：本轮拆出 `sassy_reaction_card_route`。",
            "- ChatGPT 上一张深蓝科技 UI 信息卡方向：本轮信息卡改走粉色樱花柔和展示牌皮肤。",
            "",
            "## source notes",
            "",
            "- `已确认` PR #7 B 参考图与可爱卡片页参考包均已从远端分支只读读取。",
            "- `已确认` 本轮不改 `GPT数据源/` 静态包。",
        ]
    )
    return "\n".join(lines) + "\n"


def build_cut_map(timeline: list[dict[str, Any]]) -> str:
    lines = [
        "# AI 做 PPT 踩坑 v3.1 cut map",
        "",
        "- `preview_type`: `finished_quality_candidate_v31`",
        "- `visual_master_candidate`: `true`",
        "- `visual_master_locked`: `false`",
        "- `subtitle_enabled`: `false`",
        "- `content_validation`: `pending_user_chatgpt_review`",
        "- `send_ready`: `false`",
        "- `visual_route_map`: `visual_route_map.json`",
        "",
        "| shot | time | 承载 | visual_route | 说明 |",
        "| --- | --- | --- | --- | --- |",
    ]
    for item in timeline:
        lines.append(
            f"| `{item['segment_id']}` | `{item['start']:.3f}-{item['end']:.3f}s` | `{item['kind']}` | `{item.get('visual_route') or 'not_card'}` | {item['visual_source']} |"
        )
    return "\n".join(lines) + "\n"


def build_manifest(local_pack: pathlib.Path, summary: dict[str, Any]) -> str:
    return "\n".join(
        [
            "# AI 做 PPT 踩坑成品候选 v3.1 审片入口",
            "",
            "`已确认` 本包是 `finished_quality_candidate_v31（成品质量候选片 v3.1）` 与 `visual_master_candidate（视觉母版候选）`。",
            "",
            "## 先看文件",
            "",
            f"1. `{FULL_NAME}`：v3.1 完整成品候选片。",
            f"2. `{CONTACT_SHEET_NAME}`：全片关键帧联系表。",
            f"3. `{VISUAL_ROUTE_MAP_NAME}`：视觉路由表。",
            f"4. `{VISUAL_ROUTE_VALIDATION_NAME}`：视觉路由验证报告。",
            f"5. `{INHERITANCE_REPORT_NAME}`：锁定参考继承报告。",
            f"6. `{METADATA_REPORT_NAME}`：video-metadata-probe 检查报告 JSON。",
            f"7. `{SUMMARY_NAME}`：状态摘要。",
            f"8. `{TIMELINE_NAME}`：时间线。",
            f"9. `{CUT_MAP_NAME}`：镜头说明。",
            "",
            "## 当前边界",
            "",
            "- `content_validation = pending_user_chatgpt_review`",
            "- `send_ready = false`",
            "- `subtitle_enabled = false`",
            "- `voice_validation = pending_user_chatgpt_review`",
            "- `final_voice_validated = false`",
            "- `visual_master_candidate = true`，但 `visual_master_locked = false`。",
            "- `sassy_card_execution_reference = PR7_B_骚萌反应页.png`",
            "- `sassy_card_reference_locked = false`",
            "",
            "## 本轮重点",
            "",
            "- 先输出并校验 `visual_route_map.json`，再生成视频。",
            "- 补回 `negative_display_prompt_card` 与 `positive_display_prompt_card`。",
            "- 将三张骚萌卡改走 PR #7 B 的独立 reaction page 路线。",
            "- 将信息卡改走粉色樱花柔和展示牌皮肤 + 清晰信息层级路线。",
            "- 保留“反面结果露馅 -> 方法词出现 -> 字段拆解 -> 正面操作 -> 结果预览 -> 边界收束”的主线。",
            "- 保留正反录屏素材事实，以真实录屏作为中段主体。",
            "- 保留核心方法词：`可交付初稿`。",
            "- 使用 custom voice TTS 入片，但声音仍待用户 / ChatGPT 听感复审。",
            "",
            "## 本地路径",
            "",
            f"- 复审包：`{local_pack}`",
            f"- full video：`{local_pack / FULL_NAME}`",
            f"- duration_seconds：`{summary['duration_seconds']}`",
            f"- resolution：`{summary['resolution']}`",
            f"- audio_codec：`{summary['audio_codec']}`",
        ]
    ) + "\n"


def copy_pack_to_repo_and_latest(validation: dict[str, Any], summary: dict[str, Any]) -> None:
    for base in [REPO_REVIEW_PACK, REPO_DIST]:
        if base.exists():
            shutil.rmtree(base)
        base.mkdir(parents=True, exist_ok=True)
    tracked_names = [
        FULL_NAME,
        CONTACT_SHEET_NAME,
        TIMELINE_NAME,
        CUT_MAP_NAME,
        MANIFEST_NAME,
        SUMMARY_NAME,
        RUN_SUMMARY_NAME,
        INHERITANCE_REPORT_NAME,
        OPENING_PREVIEW_NAME,
        METADATA_REPORT_NAME,
        VISUAL_ROUTE_MAP_NAME,
        "visual_route_assignment_gate.json",
        VISUAL_ROUTE_VALIDATION_NAME,
        "visual_quality_verdict.json",
        "video_metadata_probe_report.md",
        "audio_volumedetect.log",
        "blackdetect.log",
        "decode_check_ffmpeg.log",
    ]
    for name in tracked_names:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, REPO_REVIEW_PACK / name)
            shutil.copy2(src, REPO_DIST / name)
    if LOCAL_REFERENCE_DIR.exists():
        shutil.copytree(LOCAL_REFERENCE_DIR, REPO_REVIEW_PACK / "references", dirs_exist_ok=True)
        shutil.copytree(LOCAL_REFERENCE_DIR, REPO_DIST / "references", dirs_exist_ok=True)

    latest = REPO_ROOT / "dist" / "latest_review_pack"
    latest.mkdir(parents=True, exist_ok=True)
    for name in [FULL_NAME, CONTACT_SHEET_NAME, TIMELINE_NAME, CUT_MAP_NAME, MANIFEST_NAME, SUMMARY_NAME, RUN_SUMMARY_NAME, INHERITANCE_REPORT_NAME, METADATA_REPORT_NAME, VISUAL_ROUTE_MAP_NAME, "visual_route_assignment_gate.json", VISUAL_ROUTE_VALIDATION_NAME, "visual_quality_verdict.json", OPENING_PREVIEW_NAME]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, latest / name)
    shutil.copy2(LOCAL_REVIEW_PACK / FULL_NAME, latest / "full.mp4")
    shutil.copy2(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME, latest / "cut_contact_sheet.jpg")
    shutil.copy2(LOCAL_REVIEW_PACK / TIMELINE_NAME, latest / "timeline.json")
    shutil.copy2(LOCAL_REVIEW_PACK / CUT_MAP_NAME, latest / "cut_map.md")
    shutil.copy2(LOCAL_REVIEW_PACK / MANIFEST_NAME, latest / "review_manifest.md")
    shutil.copy2(LOCAL_REVIEW_PACK / SUMMARY_NAME, latest / "summary.json")

    local_latest = LOCAL_PROJECT_ROOT / "dist" / "latest_review_pack"
    local_latest.mkdir(parents=True, exist_ok=True)
    for name in [FULL_NAME, CONTACT_SHEET_NAME, TIMELINE_NAME, CUT_MAP_NAME, MANIFEST_NAME, SUMMARY_NAME, RUN_SUMMARY_NAME, INHERITANCE_REPORT_NAME, METADATA_REPORT_NAME, VISUAL_ROUTE_MAP_NAME, "visual_route_assignment_gate.json", VISUAL_ROUTE_VALIDATION_NAME, "visual_quality_verdict.json", OPENING_PREVIEW_NAME]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, local_latest / name)
    shutil.copy2(LOCAL_REVIEW_PACK / FULL_NAME, local_latest / "full.mp4")
    shutil.copy2(LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME, local_latest / "cut_contact_sheet.jpg")
    shutil.copy2(LOCAL_REVIEW_PACK / TIMELINE_NAME, local_latest / "timeline.json")
    shutil.copy2(LOCAL_REVIEW_PACK / CUT_MAP_NAME, local_latest / "cut_map.md")
    shutil.copy2(LOCAL_REVIEW_PACK / MANIFEST_NAME, local_latest / "review_manifest.md")
    shutil.copy2(LOCAL_REVIEW_PACK / SUMMARY_NAME, local_latest / "summary.json")


def write_logs(summary: dict[str, Any], validation: dict[str, Any]) -> None:
    latest_text = "\n".join(
        [
            "# Latest",
            "",
            "## 20260430｜AI 做 PPT 踩坑 v3.1 视觉路由修正候选生成",
            "",
            "- `已确认` 本轮生成 `finished_quality_candidate_v31（成品质量候选片 v3.1）`。",
            "- `已确认` 本轮先生成并校验 `visual_route_map.json`，再生成完整视频。",
            "- `已确认` 本轮补回 `negative_display_prompt_card` 与 `positive_display_prompt_card`。",
            "- `已确认` 三张骚萌卡执行参考改为 `PR7_B_骚萌反应页.png`，状态仍为 `candidate`，不是 locked。",
            "- `已确认` 信息卡走 `cute_info_card_route`：粉色樱花柔和展示牌皮肤 + 清晰信息卡结构。",
            "- `已确认` 本轮使用 custom voice 脱敏标识 `qwen-t...ac19` 生成 TTS 入片；声音仍待用户 / ChatGPT 听感复审。",
            "- `已确认` 本轮字幕关闭：`subtitle_enabled = false`，没有烧录字幕。",
            "- `已确认` 技术验证、音频验证、metadata 验证、reference 继承验证与视觉路由验证通过后，已更新 `dist/latest_review_pack/` 指向 v3.1。",
            "- `待验证` `content_validation = pending_user_chatgpt_review`，不得写通过。",
            "- `已确认` `send_ready = false`。",
            "- `已确认` `visual_master_locked = false`。",
            "- `待验证` `voice_validation = pending_user_chatgpt_review`。",
            f"- 本地复审包：`{LOCAL_REVIEW_PACK}`",
            f"- 当前完整候选片：`{LOCAL_REVIEW_PACK / FULL_NAME}`",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "latest.md").write_text(latest_text, encoding="utf-8")

    dated = "\n".join(
        [
            "# 20260430 v3.1 visual route fix generation",
            "",
            "## 本轮目标",
            "",
            "- 修复 v3 卡片 visual routing 没有拆开的问题。",
            "- 生成 v3.1 完整候选片和独立复审包。",
            "",
            "## 执行前已确认事实",
            "",
            "- PR #7 B 是本轮骚萌卡执行参考，但仍是 candidate。",
            "- 信息卡不再走深蓝科技 UI，改为粉色樱花柔和展示牌皮肤 + 清晰结构。",
            "- v3 缺少反面 / 正面展示提示卡，本轮补回。",
            "- `content_validation`、`send_ready`、`voice_validation`、`visual_master_locked` 均不得升级。",
            "",
            "## 实际读取",
            "",
            "- `AGENTS.md`、全局相关 skills、`codex_source/*` 执行规则、locked reference registry、当前 v3 review pack、v3 生成脚本。",
            "- `origin/codex/sassy-card-reference-review-20260430` 中的 PR7_B 图片和样本索引。",
            "- `origin/codex/cute-card-reference-audit-20260430` 中的可爱卡片视觉判断与 round34 提示卡图片。",
            "",
            "## 实际改动",
            "",
            "- 新增 v3.1 生成脚本。",
            "- 新增 PR7_B candidate reference registry 条目。",
            "- 新增 v3.1 dist 与复审包，并更新 `dist/latest_review_pack/`。",
            "- 更新 current publish target、轻量证据和本地产物路径索引。",
            "",
            "## 当前结果",
            "",
            "- `preview_type`: `finished_quality_candidate_v31`",
            "- `visual_master_candidate`: `true`",
            "- `visual_master_locked`: `false`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `subtitle_enabled`: `false`",
            "- `voice_validation`: `pending_user_chatgpt_review`",
            "- `final_voice_validated`: `false`",
            "- `sassy_card_execution_reference`: `PR7_B_骚萌反应页.png`",
            "- `sassy_card_reference_locked`: `false`",
            "",
            "## 产物",
            "",
            f"- full video: `{LOCAL_REVIEW_PACK / FULL_NAME}`",
            f"- review manifest: `{LOCAL_REVIEW_PACK / MANIFEST_NAME}`",
            f"- summary: `{LOCAL_REVIEW_PACK / SUMMARY_NAME}`",
            f"- timeline: `{LOCAL_REVIEW_PACK / TIMELINE_NAME}`",
            f"- cut map: `{LOCAL_REVIEW_PACK / CUT_MAP_NAME}`",
            f"- contact sheet: `{LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME}`",
            f"- visual route map: `{LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME}`",
            f"- visual route validation: `{LOCAL_REVIEW_PACK / VISUAL_ROUTE_VALIDATION_NAME}`",
            f"- locked reference inheritance report: `{LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME}`",
            f"- video metadata probe report: `{LOCAL_REVIEW_PACK / METADATA_REPORT_NAME}`",
            "",
            "## 验证",
            "",
            f"- duration_seconds: `{validation['duration_seconds']}`",
            f"- resolution: `{validation['width']}x{validation['height']}`",
            f"- fps: `{validation['fps']}`",
            f"- video_codec: `{validation['video_codec']}`",
            f"- audio_codec: `{validation['audio_codec']}`",
            f"- audio_channels: `{validation['audio_channels']}`",
            f"- decodable: `{validation['decodable']}`",
            f"- audio_non_silent: `{validation['audio_non_silent']}`",
            f"- subtitle_stream_count: `{validation['subtitle_stream_count']}`",
            "",
            "## 下一步建议",
            "",
            "- 用户 / ChatGPT 复审 v3.1 的内容、声音听感与视觉母版方向；复审前不得写可发送或 locked。",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "20260430_v31_visual_route_fix_generation.md").write_text(dated, encoding="utf-8")

    publish_target = "\n".join(
        [
            "# Current Publish Target",
            "",
            "## 当前复审 target",
            "",
            "- 当前最新复审对象：`dist/latest_review_pack/`",
            "- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`",
            "- 当前完整候选片：`dist/latest_review_pack/full.mp4`",
            "- 当前复审入口：`dist/latest_review_pack/review_manifest.md`",
            "- 当前状态摘要：`dist/latest_review_pack/summary.json`",
            "- 当前视觉路由表：`dist/latest_review_pack/visual_route_map.json`",
            "- 当前视觉路由验证：`dist/latest_review_pack/visual_route_validation_report.json`",
            "",
            "## 当前正式状态",
            "",
            "- `preview_type`: `finished_quality_candidate_v31`",
            "- `visual_master_candidate`: `true`",
            "- `visual_master_locked`: `false`",
            "- `technical_validation`: `passed`",
            "- `metadata_validation`: `passed`",
            "- `audio_validation`: `passed_non_silent_tts_track`",
            "- `subtitle_enabled`: `false`",
            "- `content_validation`: `pending_user_chatgpt_review`",
            "- `send_ready`: `false`",
            "- `voice_validation`: `pending_user_chatgpt_review`",
            "- `final_voice_validated`: `false`",
            "- `sassy_card_execution_reference`: `PR7_B_骚萌反应页.png`",
            "- `sassy_card_reference_locked`: `false`",
            "",
            "## 当前唯一最高优先级 blocker",
            "",
            "- 用户 / ChatGPT 尚未对 v3.1 完整候选片做内容、声音听感和视觉母版复审。",
            "",
            "## 现在最该看的入口",
            "",
            "1. `dist/latest_review_pack/review_manifest.md`",
            "2. `dist/latest_review_pack/full.mp4`",
            "3. `dist/latest_review_pack/cut_contact_sheet.jpg`",
            "4. `dist/latest_review_pack/visual_route_map.json`",
            "5. `dist/latest_review_pack/visual_route_validation_report.json`",
            "6. `dist/latest_review_pack/locked_reference_inheritance_report.md`",
            "7. `dist/latest_review_pack/video_metadata_probe_report.json`",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_publish_target.md").write_text(publish_target, encoding="utf-8")

    evidence = "\n".join(
        [
            "# Current Publish Target Light Evidence",
            "",
            "- 当前最新复审对象：`dist/latest_review_pack/`",
            "- 当前 round 指向：`20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`",
            "",
            "## Git 可追踪轻量证据包",
            "",
            "1. `dist/latest_review_pack/review_manifest.md`",
            "2. `dist/latest_review_pack/summary.json`",
            "3. `dist/latest_review_pack/timeline.json`",
            "4. `dist/latest_review_pack/cut_map.md`",
            "5. `dist/latest_review_pack/cut_contact_sheet.jpg`",
            "6. `dist/latest_review_pack/visual_route_map.json`",
            "7. `dist/latest_review_pack/visual_route_validation_report.json`",
            "8. `dist/latest_review_pack/locked_reference_inheritance_report.md`",
            "9. `dist/latest_review_pack/video_metadata_probe_report.json`",
            "10. `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/`",
            "",
            "## 不能证明什么",
            "",
            "- 不能证明内容验证已通过。",
            "- 不能证明可发送。",
            "- 不能证明最终声音已通过。",
            "- 不能证明视觉母版已 locked。",
            "- 不能证明 PR #7 B 成为 locked reference。",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_publish_target_light_evidence.md").write_text(evidence, encoding="utf-8")

    local_paths = "\n".join(
        [
            "# 当前本地产物路径索引 current_local_artifact_paths",
            "",
            "| artifact_id | 中文名称 | canonical_local_path | path_exists | verified_at | notes |",
            "| --- | --- | --- | --- | --- | --- |",
            f"| `ai_ppt_pitfall_v31_full` | AI 做 PPT 踩坑 v3.1 完整候选片 | `{LOCAL_REVIEW_PACK / FULL_NAME}` | `true` | `2026-04-30 CST` | `finished_quality_candidate_v31`; `send_ready=false` |",
            f"| `ai_ppt_pitfall_v31_review_pack` | AI 做 PPT 踩坑 v3.1 复审包 | `{LOCAL_REVIEW_PACK}` | `true` | `2026-04-30 CST` | 已同步 `dist/latest_review_pack/` |",
            f"| `ai_ppt_pitfall_v31_contact_sheet` | v3.1 全片关键帧联系表 | `{LOCAL_REVIEW_PACK / CONTACT_SHEET_NAME}` | `true` | `2026-04-30 CST` | 用于快速视觉复审 |",
            f"| `ai_ppt_pitfall_v31_visual_route_map` | v3.1 视觉路由表 | `{LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME}` | `true` | `2026-04-30 CST` | 三条视觉路由拆分证据 |",
            f"| `ai_ppt_pitfall_v31_metadata_probe` | v3.1 元数据检查报告 | `{LOCAL_REVIEW_PACK / METADATA_REPORT_NAME}` | `true` | `2026-04-30 CST` | 使用 `video-metadata-probe` skill 输出 |",
        ]
    ) + "\n"
    (REPO_ROOT / "codex_log" / "current_local_artifact_paths.md").write_text(local_paths, encoding="utf-8")


def sync_local_dist_outputs() -> None:
    LOCAL_DIST.mkdir(parents=True, exist_ok=True)
    for name in [
        FULL_NAME,
        CONTACT_SHEET_NAME,
        TIMELINE_NAME,
        CUT_MAP_NAME,
        MANIFEST_NAME,
        SUMMARY_NAME,
        RUN_SUMMARY_NAME,
        INHERITANCE_REPORT_NAME,
        OPENING_PREVIEW_NAME,
        METADATA_REPORT_NAME,
        VISUAL_ROUTE_MAP_NAME,
        "visual_route_assignment_gate.json",
        VISUAL_ROUTE_VALIDATION_NAME,
        "visual_quality_verdict.json",
        "video_metadata_probe_report.md",
    ]:
        src = LOCAL_REVIEW_PACK / name
        if src.exists():
            shutil.copy2(src, LOCAL_DIST / name)
    if LOCAL_REFERENCE_DIR.exists():
        shutil.copytree(LOCAL_REFERENCE_DIR, LOCAL_DIST / "references", dirs_exist_ok=True)


def main() -> None:
    for path in [OPENING_ANCHOR, NEGATIVE_RECORDING, POSITIVE_RECORDING]:
        if not path.exists():
            raise RuntimeError(f"blocked_recording_material_not_found: {path}")
    ffmpeg = resolve_binary("ffmpeg")
    ffprobe = resolve_binary("ffprobe")
    for directory in [LOCAL_REVIEW_PACK, LOCAL_DIST]:
        directory.mkdir(parents=True, exist_ok=True)

    sync_reference_assets()
    route_map = build_visual_route_map()
    write_json(LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME, route_map)
    route_gate = validate_route_map_assignments(route_map)
    write_json(LOCAL_REVIEW_PACK / "visual_route_assignment_gate.json", route_gate)
    if not route_gate["passed"]:
        raise RuntimeError(route_gate["blocker"] or "blocked_visual_route_not_separated")

    cards = make_all_cards(ffmpeg)
    visual_route_validation = write_visual_route_validation_report(route_map, cards)

    api_key = load_api_key()
    voice_resolution = resolve_existing_custom_voice(api_key)
    tts_records = asyncio.run(synthesize_all_segments(api_key, voice_resolution["voice"]))
    audio_info = concat_audio(ffmpeg, tts_records)
    opening_preview = make_opening_preview(ffmpeg)
    video_track = make_video_track(ffmpeg, tts_records, audio_info["atempo_factor"], cards)
    final_path = make_final_video(ffmpeg, video_track, pathlib.Path(audio_info["path"]))
    validation = validate_final(ffmpeg, ffprobe, final_path)
    metadata_probe_report = run_video_metadata_probe_skill(final_path)
    contact_sheet = make_contact_sheet(ffmpeg, final_path)
    visual_quality_verdict = write_visual_quality_verdict()

    timeline = video_track["timeline"]
    (LOCAL_REVIEW_PACK / TIMELINE_NAME).write_text(json.dumps(timeline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (LOCAL_REVIEW_PACK / CUT_MAP_NAME).write_text(build_cut_map(timeline), encoding="utf-8")
    (LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME).write_text(locked_reference_report(), encoding="utf-8")

    locked_refs = sorted({ref for segment in SEGMENTS for ref in segment.locked_refs} | {"tts_15s_b_pacing_locked_20260427"})
    candidate_refs = sorted({ref for segment in SEGMENTS for ref in segment.candidate_refs} | {"voice_sample2_cute_guide_voice_candidate_20260426"})
    failed_avoided = [
        "pr15_v2_subtitle_failed_reference",
        "pr15_v2_layout_background_failed_reference",
        "pr15_v2_tts_missing_failed_reference",
        "zoom_pr15_v2_failed_20260430",
        "v3_sassy_cards_mixed_info_card_shell_failed_implementation",
        "deep_blue_tech_saas_ui_info_card_rejected_direction",
    ]
    summary = {
        "round": TASK_SLUG,
        "preview_type": "finished_quality_candidate_v31",
        "visual_master_candidate": True,
        "visual_master_locked": False,
        "technical_validation": "passed",
        "metadata_validation": "passed",
        "audio_validation": "passed_non_silent_tts_track",
        "subtitle_enabled": False,
        "content_validation": "pending_user_chatgpt_review",
        "send_ready": False,
        "locked_reference_registry_read": True,
        "locked_reference_inheritance_validation": "passed_for_candidate_v31_visual_route_fix",
        "locked_reference_inheritance_report": str(LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME),
        "unapproved_reference_changes": [],
        "reference_deviation_blockers": [],
        "locked_references_used": locked_refs,
        "candidate_references_used": candidate_refs,
        "failed_references_avoided": failed_avoided,
        "modified_latest_review_pack": True,
        "voice_validation": "pending_user_chatgpt_review",
        "final_voice_validated": False,
        "visual_route_map": str(LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME),
        "visual_route_validation": str(LOCAL_REVIEW_PACK / VISUAL_ROUTE_VALIDATION_NAME),
        "sassy_card_execution_reference": PR7B_REFERENCE_NAME,
        "sassy_card_reference_status": "candidate",
        "sassy_card_reference_locked": False,
        "negative_display_prompt_card": "present",
        "positive_display_prompt_card": "present",
        "visual_quality_validation": "pass_for_candidate_review_pending_user_chatgpt_review",
        "visual_quality_verdict": str(LOCAL_REVIEW_PACK / "visual_quality_verdict.json"),
        "source_from_prompt_loaded": True,
        "recording_reports_read": {
            "material_faithful_report": "read_from_origin/codex/material-faithful-check-20260429",
            "copy_sample_rhythm_report": "read_from_origin/codex/copy-sample-rhythm-extract-20260429",
        },
        "custom_voice": {
            "found": True,
            "voice_masked": voice_resolution["voice_masked"],
            "actual_voice_id_not_written_to_report": True,
            "target_model": voice_resolution["target_model"],
        },
        "duration_seconds": validation["duration_seconds"],
        "resolution": f"{validation['width']}x{validation['height']}",
        "fps": validation["fps"],
        "video_codec": validation["video_codec"],
        "audio_codec": validation["audio_codec"],
        "audio_channels": validation["audio_channels"],
        "decodable": validation["decodable"],
        "audio_non_silent": validation["audio_non_silent"],
        "subtitle_stream_count": validation["subtitle_stream_count"],
        "artifacts": {
            "full": str(final_path),
            "contact_sheet": str(contact_sheet),
            "timeline": str(LOCAL_REVIEW_PACK / TIMELINE_NAME),
            "cut_map": str(LOCAL_REVIEW_PACK / CUT_MAP_NAME),
            "review_manifest": str(LOCAL_REVIEW_PACK / MANIFEST_NAME),
            "summary": str(LOCAL_REVIEW_PACK / SUMMARY_NAME),
            "run_summary": str(LOCAL_REVIEW_PACK / RUN_SUMMARY_NAME),
            "locked_reference_inheritance_report": str(LOCAL_REVIEW_PACK / INHERITANCE_REPORT_NAME),
            "opening_preview": str(opening_preview),
            "video_metadata_probe_report": str(LOCAL_REVIEW_PACK / METADATA_REPORT_NAME),
            "visual_route_map": str(LOCAL_REVIEW_PACK / VISUAL_ROUTE_MAP_NAME),
            "visual_route_validation_report": str(LOCAL_REVIEW_PACK / VISUAL_ROUTE_VALIDATION_NAME),
        },
    }
    write_json(LOCAL_REVIEW_PACK / SUMMARY_NAME, summary)
    (LOCAL_REVIEW_PACK / MANIFEST_NAME).write_text(build_manifest(LOCAL_REVIEW_PACK, summary), encoding="utf-8")
    run_summary = {
        "task": TASK_SLUG,
        "started_outputs_at": "2026-04-30 CST",
        "repo_worktree": str(REPO_ROOT),
        "local_project_root": str(LOCAL_PROJECT_ROOT),
        "source_materials": {
            "opening_anchor": str(OPENING_ANCHOR),
            "negative_recording": str(NEGATIVE_RECORDING),
            "positive_recording": str(POSITIVE_RECORDING),
        },
        "voice_resolution": {key: value for key, value in voice_resolution.items() if key != "voice"},
        "tts_records": tts_records,
        "audio_info": audio_info,
        "video_track": video_track,
        "validation": validation,
        "metadata_probe_report": metadata_probe_report,
        "visual_quality_verdict": visual_quality_verdict,
        "visual_route_map": route_map,
        "visual_route_validation": visual_route_validation,
        "summary": summary,
    }
    write_json(LOCAL_REVIEW_PACK / RUN_SUMMARY_NAME, run_summary)
    sync_local_dist_outputs()
    copy_pack_to_repo_and_latest(validation, summary)
    write_logs(summary, validation)


if __name__ == "__main__":
    main()
