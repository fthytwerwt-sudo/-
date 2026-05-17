#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent

COPY_DIR = Path("review_loop/copy_iteration")
V002_DIR = COPY_DIR / "V002"
V003_DIR = COPY_DIR / "V003"
V004_DIR = COPY_DIR / "V004"

COPY_REGISTRY_PATH = COPY_DIR / "copy_registry.json"
LATEST_REPORT_JSON = COPY_DIR / "latest_copy_iteration_report.json"
LATEST_REPORT_MD = COPY_DIR / "latest_copy_iteration_report.md"

V002_RAW_PATH = V002_DIR / "V002_copy_v1_raw.md"
V002_RECORD_PATH = V002_DIR / "V002_copy_v1_record.json"
V002_STRUCTURE_PATH = V002_DIR / "V002_copy_structure_map.json"
V002_DECISION_PATH = V002_DIR / "V002_copy_iteration_decision.json"
V002_BRIEF_PATH = V002_DIR / "V002_next_copy_revision_brief.md"

V003_RAW_PATH = V003_DIR / "V003_copy_v1_raw.md"
V003_RECORD_PATH = V003_DIR / "V003_copy_v1_record.json"
V003_STRUCTURE_PATH = V003_DIR / "V003_copy_structure_map.json"
V003_DECISION_PATH = V003_DIR / "V003_copy_iteration_decision.json"
V003_BRIEF_PATH = V003_DIR / "V003_next_copy_revision_brief.md"

V004_RAW_PATH = V004_DIR / "V004_copy_v1_raw.md"
V004_RECORD_PATH = V004_DIR / "V004_copy_v1_record.json"
V004_STRUCTURE_PATH = V004_DIR / "V004_copy_structure_map.json"
V004_DECISION_PATH = V004_DIR / "V004_copy_iteration_decision.json"
V004_BRIEF_PATH = V004_DIR / "V004_next_copy_revision_brief.md"

V002_OPERATION_RECORD_PATH = Path(
    "review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/"
    "V002_发布后复盘记录_post_publish_review_record.md"
)

OPERATION_REPORT_PATH = Path("review_loop/decision_engine/latest_operation_decision_report.json")
FINAL_USER_OPERATION_RESULT_PATH = Path("review_loop/decision_engine/final_user_operation_result.md")
V003_OPERATION_RECORD_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_发布后灰度数据记录_post_publish_gray_test_record.md"
)
V003_DATA_SNAPSHOT_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_post_72h_pre_7d_snapshot.json"
)
V003_OPERATION_DECISION_PATH = Path(
    "review_loop/records/V003_本地文件优化实用分享_latest_practical_video_20260514/"
    "V003_operation_decision_result.md"
)
V004_OPERATION_RECORD_PATH = Path(
    "review_loop/records/V004_全自动制作方式_public_ai_video_20260517/"
    "V004_发布后运营数据记录_post_publish_operation_record.md"
)
V004_DATA_SNAPSHOT_PATH = Path(
    "review_loop/records/V004_全自动制作方式_public_ai_video_20260517/"
    "V004_interim_17h_snapshot.json"
)

SCRIPT_PATH = Path("scripts/文案迭代决策系统_copy_iteration_decision_system.py")
CURRENT_DATA_WINDOW = "post_72h_pre_7d_snapshot"

RAW_COPY = """第三期
别再让ai给你定kpi了。播放多少、点赞多少、克资多少，看着很完整，但大多数时候没用，因为这些数字不会告诉你下一条到底该改标题，还是改开头，还是改中段结构。我一开始也这样问，帮视频工厂定个目标，最好有播放、点赞和克资。第一版确实很全，北极星目标、阶段目标、指标数、刻字定义都有，但我看完觉得不对，他还是在回答我要追哪些数字。我真正需要的是数据回来以后，下一轮该改哪里。所以我又追问，让ai设计一套目标驱动的数据飞轮，每期发布后，根据播放、留存、收藏、评论、私信和克兹，判断下一期只改哪个变量，这次结果才像个判断系统。播放和留存是触达，点赞和收藏是认可，评论和追问是互动。但私信也不能全算克资，要看他有没有说清楚任务场景和想要的结果。所以，目标不是kpi表，真正有用的目标是逼你回答三件事哪一层出了问题，下一条只改哪个变量，改完看哪个指标。没有这套判断，你每轮都在动，却不知道哪一步起作用。播放是入口，收藏是认可，私信要评分，每条只改一个主变量，目标清楚了，动作才不会乱，复盘清楚了，下一步才会浮出来。

"""

V002_RAW_COPY = """大家好，短视频自动流的最简单流程。这次做的第一步其实特别简单，先打开豆包，只输入了一句话：我想用吹做一个短视频自动流。就这么一句，没有什么复杂提示词，也没有一上来写一大堆技术要求。这一步的重点不是让豆包直接帮我做视频，它的作用是先帮我把顺序理出来。
豆包先给了我一版方案，他把这个需求拆成了用tree搭建短视频自动流，从零基础清量版到无人值守全自动化版。这个标题其实就很关键，不是说给你生成一条视频，是在说这件事可以先做清量版，也可以继续升级成无人值守版。
换句话说，自动流不是一下子憋出一个大系统，可以先从一个很小的流程开始。豆包拆出来的核心链路大概是选择题、策划、脚本、生成、分镜、制作视频、生成或者剪辑、配音、字幕、封面、标题、自动发布。
这里已经不是在讲某个单点工具了，是在把短视频生产拆成一排工位，哪个环节负责想选举，每个环节负责写脚本，每个环节负责分镜，每个环节负责素材，每个环节负责后期，每个环节负责发布，这才是自动流的第一层。
所以接着问他，主要是想做一个vlog的视频自动流，先给我一个prompt，让tree帮我把架构搭建出来。后面豆包就给了我一份try vlog自动流核心搭建prompt，而且标题里直接写着直接复制粘贴到try solo即可一键生成完整架构加可运行脚本。
当然这句话不能理解成整个系统已经跑通了，它只是说明这份prompt的目标是让翠先把架构搭出来。这里面还拆了几个模块，比如局人设锚定模块、vlog小题与虚实线生成模块、vlog分镜与标准化脚本生成模块、素材智能匹配与调度模块、vlog专属自动化后期模块、成片与运营物料导出模块、总控调度与异常处理模块。
这些名字听起来有点长，但翻成人话就是先固定账号风格，再决定拍什么，再写脚本，再拆镜头，再匹配素材，再做后期，最后导出成片和发布物料。到这里流程已经从一句话想法变成了一份能交给tree。
这里用的是tree的solo coder，可以把它理解成一个会自己规划任务，自己生成项目结构的ai编码工具。这里有一个细节很关键，不是把豆包的回答截图保存一下就结束了，而是把它生成的这份prompt真的放进了tree的solo coder。画面里能看到这些模块文字已经进入tree的输入区，tree没有只回一句建议怎么做。
先说让我先规划一下任务，然后逐步实现。接着画面里出现了updating tasks，还有十一个代办。这一步其实就是自动流开始辨识的地方，因为已经不是聊天里的一个想法了，开始被拆成tree自己能执行的任务列表。再往后tree开始创建项目结构，画面里能看到一个项目目录vlog automation workflow。
下面有：modules、templates、workflows、config、assets、friend and logs，还出现了logs，还出现了settings到p y base module到p y，这些代码文件普通人其实看不懂也没关系，这一步最重要的不是你能不能看懂每一行代码，而是看tree有没有真的把这个东西执行出一个初步形状，有没有项目目录。
"""

V002_LATEST_USER_METRICS = {
    "play_count": 56,
    "like_count": 6,
    "favorite_count": 9,
    "like_rate": "10.71%",
    "favorite_rate": "16.07%",
    "like_plus_favorite_action_rate": "26.79%",
    "source_status": "user_provided_in_chat / no_screenshot_yet",
}

V004_RAW_COPY = """AI 时代，真正拉开差距的不是数据，是复盘能力。

我这条视频只有 141 播放，2 秒跳出接近 50%。

如果只看播放，这条很差。

但如果认真复盘，它反而告诉我：
下一条最该先改的，不是方向，而是开头。

很多人现在用 AI 做内容，最大的问题不是不会生成。

而是数据回来以后，还是只会问一句：
这条是不是废了？

播放低，就怀疑选题。
点赞少，就怀疑表达。
没人私信，就怀疑方向。

但这样复盘，其实没用。

因为数据本身不会告诉你答案。
真正有用的是，你能不能从数据里拆出问题层级。

比如我这条视频，推荐页其实给过一点入口。
但 2 秒跳出接近 50%，5 秒完播也不高。

这说明什么？

它不一定说明方向错了。
更可能说明，用户第一眼还没明白这条视频跟他有什么关系，就已经划走了。

所以我下一条不该先换方向。
也不该先换人群。
更不该整条推翻重写。

我只先改一个变量：
开头 5 秒。

这就是我现在对 AI 最大的理解。

AI 不是帮你列一堆 KPI 的。
什么播放量、点赞率、收藏率、完播率，看着很完整。

但如果这些数字最后不能告诉你下一步该改哪里，那它们只是一个好看的表。

真正有用的复盘，应该逼你回答三个问题：

第一，哪一层出了问题？
是标题、开头、中段结构，还是结尾承接？

第二，下一条只改哪个变量？
不要一条数据不好，就标题、选题、结构、人群全都改。

第三，改完以后看哪个指标？
改开头，就看 2 秒跳出、3 秒留存、5 秒完播。
改中段，就看平均观看和完播。
改承接，就看收藏、评论、私信和主页访问。

这条视频虽然播放低，但它还有 3 个收藏。

这说明内容不一定完全没价值。
更像是价值出现得太晚，用户前面没被接住。

所以我下一条最该做的，不是证明我这个方向有多对。

而是先把开头改到用户愿意留下来看。

播放是入口。
收藏是认可。
私信要评分。

但真正拉开差距的，不是你有没有数据。

而是数据差的时候，你能不能看出问题在哪。

如果每条内容发完，你都能知道下一条只改哪一个变量。

那你就不是在碰运气。

你是在迭代。
"""

V004_INTERIM_METRICS = {
    "play_count": 55,
    "like_count": 1,
    "comment_count": 0,
    "share_count": 0,
    "favorite_count": 0,
    "completion_rate": "4.76%",
    "two_second_bounce_rate": "41.18%",
    "average_watch_time": "14秒",
    "five_second_completion_rate": "30.88%",
    "average_play_ratio": "9.42%",
    "recommendation_page": "95.2%",
    "profile_page": "4.8%",
    "like_rate": "1.82%",
    "favorite_rate": "0.00%",
    "source_status": "screenshot_archived_to_repo_and_user_provided_visual_read",
}

PROBLEM_LAYERS = [
    "opening_packaging",
    "bridge_3_8s",
    "middle_structure",
    "evidence_expression",
    "tone_and_language",
    "topic_angle",
    "target_audience",
]

FORBIDDEN_STATUS_PATTERNS = {
    "content_validation_advanced": ["content_validation = passed", "content_validation: passed"],
    "send_ready_advanced": ["send_ready = true", "send_ready: true"],
    "current_data_goal_anchor_ready": ["current_data_goal_anchor ready", "anchor_instance_status: \"ready\""],
    "next_formal_video_execution_prompt_generated": [
        "正式下一条视频执行 prompt 已生成",
        "next_formal_video_execution_prompt_generated: true",
    ],
    "target_audience_changed": ["allow_target_audience_change\": true"],
    "topic_direction_changed": ["allow_topic_direction_change\": true", "core_topic_direction changed"],
}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(root: Path, path: Path) -> str:
    return (root / path).read_text(encoding="utf-8")


def write_text(root: Path, path: Path, content: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def load_json(root: Path, path: Path) -> dict[str, Any]:
    return json.loads(read_text(root, path))


def write_json(root: Path, path: Path, payload: dict[str, Any]) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def metric_value(operation_report: dict[str, Any], metric_name: str) -> Any:
    v003 = next(record for record in operation_report["records_processed"] if record["video_id"] == "V003")
    metric = v003.get("normalized_metrics", {}).get(metric_name, {})
    return metric.get("value")


def metric_number(operation_report: dict[str, Any], metric_name: str) -> float | None:
    v003 = next(record for record in operation_report["records_processed"] if record["video_id"] == "V003")
    metric = v003.get("normalized_metrics", {}).get(metric_name, {})
    value = metric.get("percent_value")
    if value is None:
        value = metric.get("numeric_value")
    return float(value) if isinstance(value, (int, float)) else None


def record_metric_value(operation_report: dict[str, Any], video_id: str, metric_name: str, fallback: Any = None) -> Any:
    record = next((item for item in operation_report.get("records_processed", []) if item["video_id"] == video_id), None)
    if not record:
        return fallback
    metric = record.get("normalized_metrics", {}).get(metric_name, {})
    return metric.get("value", fallback)


def ensure_v002_raw_copy(root: Path) -> None:
    raw_path = root / V002_RAW_PATH
    if raw_path.exists():
        existing = raw_path.read_text(encoding="utf-8")
        if existing != V002_RAW_COPY:
            if existing.rstrip("\n") == V002_RAW_COPY.rstrip("\n"):
                raw_path.write_text(V002_RAW_COPY, encoding="utf-8")
                return
            raise RuntimeError("V002 raw copy exists but does not match locked user-provided source text")
        return
    write_text(root, V002_RAW_PATH, V002_RAW_COPY)


def ensure_v004_raw_copy(root: Path) -> None:
    raw_path = root / V004_RAW_PATH
    if raw_path.exists():
        existing = raw_path.read_text(encoding="utf-8")
        if existing != V004_RAW_COPY:
            if existing.rstrip("\n") == V004_RAW_COPY.rstrip("\n"):
                raw_path.write_text(V004_RAW_COPY, encoding="utf-8")
                return
            raise RuntimeError("V004 raw copy exists but does not match locked user-provided source text")
        return
    write_text(root, V004_RAW_PATH, V004_RAW_COPY)


def ensure_raw_copy(root: Path) -> None:
    raw_path = root / V003_RAW_PATH
    if raw_path.exists():
        existing = raw_path.read_text(encoding="utf-8")
        if existing != RAW_COPY:
            if existing.rstrip("\n") == RAW_COPY.rstrip("\n"):
                raw_path.write_text(RAW_COPY, encoding="utf-8")
                return
            raise RuntimeError("V003 raw copy exists but does not match locked source text")
        return
    write_text(root, V003_RAW_PATH, RAW_COPY)


def build_v002_copy_record() -> dict[str, Any]:
    return {
        "video_id": "V002",
        "copy_id": "V002_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V002_RAW_PATH),
        "linked_operation_record": rel(V002_OPERATION_RECORD_PATH),
        "abnormal_sample_status": "policy_limited_abnormal_operation_sample",
        "sample_interpretation_label": "policy_limited_but_interest_signal_strong",
        "policy_notice": {
            "review_result": "减少作品推荐",
            "violation_reason": "引导至风险不可控渠道",
            "reason_surface": "画面",
            "distribution_status": "policy_distribution_limited",
        },
        "latest_user_reported_metrics": V002_LATEST_USER_METRICS,
        "historical_recorded_metrics_preserved": {
            "play_count": 39,
            "like_count": 5,
            "favorite_count": 8,
            "source_status": "historical_user_provided_record_preserved",
        },
        "copy_quality_notes": [
            "原文展示了从一句话需求到自动流项目结构的过程，可作为强兴趣异常样本的内容证据。",
            "文案中包含自动流、自动发布、工具名、可运行脚本等表达，需保持平台风险边界。",
            "V002 数据被平台减推污染，不能作为自然分发归因样本。",
        ],
        "suspected_typos": [
            {
                "original_text": "吹",
                "suspected_normalized_text": "工具名或语音转写待确认",
                "action": "mark_only_do_not_modify_raw",
            },
            {
                "original_text": "清量版",
                "suspected_normalized_text": "轻量版",
                "action": "mark_only_do_not_modify_raw",
            },
            {
                "original_text": "想选举",
                "suspected_normalized_text": "想选题",
                "action": "mark_only_do_not_modify_raw",
            },
            {
                "original_text": "翠",
                "suspected_normalized_text": "tree",
                "action": "mark_only_do_not_modify_raw",
            },
        ],
        "raw_copy_modified": False,
        "raw_copy_sha256": sha256_text(V002_RAW_COPY),
        "status_boundary": {
            "normal_distribution_sample": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "direction_established": False,
        },
    }


def build_copy_record() -> dict[str, Any]:
    suspected_typos = [
        {
            "original_text": "克资",
            "suspected_normalized_text": "客资",
            "note": "疑似“客资”误写；raw 原文保留，不在 raw 中改写。",
            "action": "mark_only_do_not_modify_raw",
        },
        {
            "original_text": "刻字定义",
            "suspected_normalized_text": "客资定义",
            "note": "结合上下文疑似“客资定义”误写；raw 原文保留。",
            "action": "mark_only_do_not_modify_raw",
        },
        {
            "original_text": "克兹",
            "suspected_normalized_text": "客资",
            "note": "疑似“客资”误写；raw 原文保留。",
            "action": "mark_only_do_not_modify_raw",
        },
    ]
    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V003_RAW_PATH),
        "linked_operation_record": rel(V003_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V003_DATA_SNAPSHOT_PATH),
        "linked_operation_decision_report": rel(V003_OPERATION_DECISION_PATH),
        "copy_quality_notes": [
            "开头直接进入 KPI 概念，真实数据冲突出现得不够早。",
            "前 3-8 秒承接没有先交代观众为什么要继续看。",
            "数据飞轮、KPI、北极星目标等项目内部语言密度偏高。",
            "核心判断可保留，但应先用真实数据证据承接。",
        ],
        "suspected_typos": suspected_typos,
        "normalized_notes": [
            "客资相关词只在备注中规范化；raw 文案不改。",
            "下一版只允许低置信度准备 opening_0_3s 和 bridge_3_8s。",
        ],
        "current_data_window": CURRENT_DATA_WINDOW,
        "data_confidence": "low",
        "formal_revision_allowed": False,
        "formal_copy_revision_allowed": False,
        "low_confidence_prepare_allowed": True,
        "raw_copy_sha256": sha256_text(RAW_COPY),
        "status_boundary": {
            "raw_copy_modified": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
        },
    }


def build_v004_copy_record() -> dict[str, Any]:
    return {
        "video_id": "V004",
        "copy_id": "V004_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V004_RAW_PATH),
        "linked_operation_record": rel(V004_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V004_DATA_SNAPSHOT_PATH),
        "operation_record_status": "latest_operation_sample_pre_24h",
        "data_window": "pre_24h / interim_17h_snapshot",
        "latest_interim_metrics": V004_INTERIM_METRICS,
        "copy_quality_notes": [
            "raw copy 明确把复盘能力作为核心观点。",
            "文案引用 V003 的 141 播放、接近 50% 2s 跳出和 3 个收藏，用于说明上一条数据复盘，不等于 V004 自身数据。",
            "V004 当前自身收藏量为 0，必须与文案引用的上一条案例收藏数 3 分开记录。",
            "当前只是 pre_24h 早期快照，不允许生成正式下一条视频执行 prompt。",
        ],
        "raw_copy_mentions_previous_case": {
            "previous_video_id": "V003",
            "play_count": 141,
            "favorite_count": 3,
            "two_second_bounce_rate_approx": "接近 50%",
            "boundary": "copy_reference_only_not_V004_actual_metrics",
        },
        "actual_metrics_boundary": {
            "V004_actual_favorite_count": 0,
            "raw_copy_mentions_previous_case_favorite_count": 3,
        },
        "raw_copy_modified": False,
        "raw_copy_sha256": sha256_text(V004_RAW_COPY),
        "status_boundary": {
            "current_operation_target_switched": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "direction_failure_concluded": False,
            "content_value_absent_concluded": False,
        },
    }


def build_copy_registry() -> dict[str, Any]:
    v002_entry = {
        "video_id": "V002",
        "copy_id": "V002_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V002_RAW_PATH),
        "record_path": rel(V002_RECORD_PATH),
        "structure_map_path": rel(V002_STRUCTURE_PATH),
        "decision_path": rel(V002_DECISION_PATH),
        "next_copy_revision_brief_path": rel(V002_BRIEF_PATH),
        "linked_operation_record": rel(V002_OPERATION_RECORD_PATH),
        "publish_status": "published_then_policy_distribution_limited",
        "operation_record_status": "policy_limited_abnormal_operation_sample",
        "sample_interpretation_label": "policy_limited_but_interest_signal_strong",
        "data_window": "user_latest_reported_metrics_no_screenshot_yet",
        "current_revision_status": "recorded_abnormal_sample_reference_only",
    }
    v003_entry = {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V003_RAW_PATH),
        "record_path": rel(V003_RECORD_PATH),
        "structure_map_path": rel(V003_STRUCTURE_PATH),
        "decision_path": rel(V003_DECISION_PATH),
        "next_copy_revision_brief_path": rel(V003_BRIEF_PATH),
        "linked_operation_record": rel(V003_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V003_DATA_SNAPSHOT_PATH),
        "linked_decision_report": rel(V003_OPERATION_DECISION_PATH),
        "publish_status": "published_in_formal_operation",
        "data_window": CURRENT_DATA_WINDOW,
        "current_revision_status": "low_confidence_prepare_only",
    }
    v004_entry = {
        "video_id": "V004",
        "copy_id": "V004_copy_v1",
        "version": "v1_raw",
        "source_type": "user_provided_in_chat",
        "source_status": "raw_source_locked",
        "raw_copy_path": rel(V004_RAW_PATH),
        "record_path": rel(V004_RECORD_PATH),
        "structure_map_path": rel(V004_STRUCTURE_PATH),
        "decision_path": rel(V004_DECISION_PATH),
        "next_copy_revision_brief_path": rel(V004_BRIEF_PATH),
        "linked_operation_record": rel(V004_OPERATION_RECORD_PATH),
        "linked_data_snapshot": rel(V004_DATA_SNAPSHOT_PATH),
        "publish_status": "published_in_formal_operation",
        "operation_record_status": "latest_operation_sample_pre_24h",
        "data_window": "pre_24h / interim_17h_snapshot",
        "current_revision_status": "recorded_latest_sample_pre_24h_only",
    }
    return {
        "registry_version": "copy_iteration_registry_v1",
        "system_name": "copy_iteration_decision_system",
        "updated_at_utc": datetime.now(timezone.utc).isoformat(),
        "records": [v002_entry, v003_entry, v004_entry],
        "status_boundary": {
            "formal_copy_revision_allowed": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
        },
    }


def segment(
    segment_id: str,
    original_text: str,
    copy_function: str,
    viewer_question_answered: str,
    data_feedback_target: list[str],
    likely_issue_if_metric_bad: str,
    can_modify_if_problem_layer: list[str],
    must_keep: list[str],
    forbidden_change: list[str],
) -> dict[str, Any]:
    return {
        "segment_id": segment_id,
        "original_text": original_text,
        "copy_function": copy_function,
        "viewer_question_answered": viewer_question_answered,
        "data_feedback_target": data_feedback_target,
        "likely_issue_if_metric_bad": likely_issue_if_metric_bad,
        "can_modify_if_problem_layer": can_modify_if_problem_layer,
        "must_keep": must_keep,
        "forbidden_change": forbidden_change,
    }


def build_structure_map() -> dict[str, Any]:
    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "source_path": rel(V003_RAW_PATH),
        "structure_version": "copy_structure_map_v1",
        "current_assessment": {
            "opening_too_conceptual": True,
            "enters_kpi_and_data_flywheel_too_fast": True,
            "missing_real_data_conflict": True,
            "has_internal_project_language": True,
            "viewer_scene_insufficient": True,
            "core_claim_keepable": True,
            "assessment_confidence": "low",
            "assessment_boundary": "只能用于准备开头和 3-8 秒承接，不能判定选题方向或目标人群失败。",
        },
        "segments": [
            segment(
                "opening_0_3s",
                "第三期\n别再让ai给你定kpi了。播放多少、点赞多少、克资多少，看着很完整，但大多数时候没用，",
                "抛出反常识判断，试图阻断观众继续用 KPI 表思考。",
                "为什么我不该只看 KPI？",
                ["2s_bounce", "3s_retention"],
                "2s 跳出高时，说明开头像概念判断，缺少真实冲突和观众代入。",
                ["opening_packaging"],
                ["不要再让 AI 只给 KPI 表", "目标要服务下一步动作"],
                ["不得改成换人群", "不得改核心方向", "不得加入素材没有的数据承诺"],
            ),
            segment(
                "bridge_3_8s",
                "因为这些数字不会告诉你下一条到底该改标题，还是改开头，还是改中段结构。",
                "解释开头判断和下一步行动之间的关系。",
                "这些数据为什么没法指导下一条？",
                ["5s_completion", "average_watch_time"],
                "5s 完播弱时，说明承接没有快速把问题落到观众具体困境。",
                ["bridge_3_8s", "opening_packaging"],
                ["下一条只改哪个变量的核心问题"],
                ["不得扩写成全文重写", "不得改变 offer / 承接口径"],
            ),
            segment(
                "problem_setup",
                "我一开始也这样问，帮视频工厂定个目标，最好有播放、点赞和克资。",
                "建立作者旧做法和观众常见误区。",
                "作者之前是怎么错用 AI 的？",
                ["average_watch_time", "comment_count"],
                "如果中段观看弱，可能是旧做法交代太抽象。",
                ["middle_structure", "tone_and_language"],
                ["我一开始也这样问的自曝视角"],
                ["不得把作者经验改成外部权威说教"],
            ),
            segment(
                "negative_example",
                "第一版确实很全，北极星目标、阶段目标、指标数、刻字定义都有，但我看完觉得不对，他还是在回答我要追哪些数字。",
                "展示旧系统的完整但无用。",
                "第一版为什么看起来完整但仍不对？",
                ["average_watch_time", "favorite_rate"],
                "如果收藏弱，可能是反面示例缺少可复用结构。",
                ["middle_structure", "evidence_expression", "tone_and_language"],
                ["看起来完整但不能指导下一步的反差"],
                ["不得删除反面示例", "不得把疑似错字写进 normalized raw"],
            ),
            segment(
                "turning_point",
                "我真正需要的是数据回来以后，下一轮该改哪里。所以我又追问，",
                "从追数字转向追判断系统。",
                "真正的问题到底是什么？",
                ["5s_completion", "average_watch_time"],
                "承接弱时，转折点可能来得太晚或力度不足。",
                ["bridge_3_8s", "middle_structure"],
                ["数据回来以后下一轮该改哪里"],
                ["不得改成商业承诺", "不得改成新人群判断"],
            ),
            segment(
                "positive_system",
                "让ai设计一套目标驱动的数据飞轮，每期发布后，根据播放、留存、收藏、评论、私信和克兹，判断下一期只改哪个变量，这次结果才像个判断系统。",
                "给出新系统的正解形态。",
                "什么样的 AI 目标系统才有用？",
                ["favorite_rate", "average_watch_time"],
                "如果收藏有信号但观看弱，可能要提前压缩为更易懂的结果预览。",
                ["middle_structure", "evidence_expression"],
                ["目标驱动数据飞轮", "每期只改一个变量"],
                ["不得写成系统已经验证成功", "不得生成下一条正式执行 prompt"],
            ),
            segment(
                "metric_explanation",
                "播放和留存是触达，点赞和收藏是认可，评论和追问是互动。",
                "把指标分层解释给观众。",
                "每类指标分别说明什么？",
                ["favorite_rate", "comment_count"],
                "如果互动弱，可能是指标解释仍偏概念，没有引出观众提问。",
                ["evidence_expression", "tone_and_language"],
                ["播放/留存/收藏/评论的层级关系"],
                ["不得把点赞等同于客资", "不得把收藏直接写成商业成立"],
            ),
            segment(
                "lead_quality_boundary",
                "但私信也不能全算克资，要看他有没有说清楚任务场景和想要的结果。",
                "划清客资质量边界。",
                "什么样的私信才有需求质量？",
                ["dm_count", "effective_dm_count", "effective_consult_count"],
                "需求侧字段缺失时，只能保留规则，不得判定商业验证。",
                ["evidence_expression"],
                ["私信要看任务场景和结果"],
                ["不得把所有私信都算客资", "不得在缺数据时写有效咨询成立"],
            ),
            segment(
                "core_claim",
                "所以，目标不是kpi表，真正有用的目标是逼你回答三件事哪一层出了问题，下一条只改哪个变量，改完看哪个指标。",
                "输出整条文案的核心判断。",
                "真正有用的目标要逼我回答什么？",
                ["favorite_rate", "average_watch_time"],
                "如果收藏弱且多样本重复，才考虑核心表达或选题角度问题。",
                ["evidence_expression", "tone_and_language", "topic_angle"],
                ["哪一层出问题", "只改哪个变量", "改完看哪个指标"],
                ["不得在 V003 早期数据下判方向失败", "不得全文重写"],
            ),
            segment(
                "summary_rules",
                "没有这套判断，你每轮都在动，却不知道哪一步起作用。播放是入口，收藏是认可，私信要评分，每条只改一个主变量，",
                "把行动规则压缩成可记住的总结。",
                "我应该记住哪些复盘规则？",
                ["favorite_rate", "comment_count", "average_watch_time"],
                "如果尾段弱，可能是规则密度高，需要更口语化。",
                ["tone_and_language", "middle_structure"],
                ["播放是入口", "收藏是认可", "私信要评分", "每条只改一个主变量"],
                ["不得改成多变量同时测试", "不得改动核心规则"],
            ),
            segment(
                "ending_takeaway",
                "目标清楚了，动作才不会乱，复盘清楚了，下一步才会浮出来。",
                "以一句人话收束价值。",
                "这套判断最终带来什么？",
                ["completion_rate", "average_watch_time"],
                "如果结尾完播弱，可能是前文承接不足，结尾本身不优先大改。",
                ["tone_and_language"],
                ["目标清楚动作不乱", "复盘清楚下一步浮出来"],
                ["不得加重销售承接", "不得生成正式下一条执行 prompt"],
            ),
        ],
    }


def build_v002_structure_map() -> dict[str, Any]:
    return {
        "video_id": "V002",
        "copy_id": "V002_copy_v1",
        "source_path": rel(V002_RAW_PATH),
        "structure_version": "copy_structure_map_v1",
        "sample_boundary": {
            "abnormal_sample_status": "policy_limited_abnormal_operation_sample",
            "sample_interpretation_label": "policy_limited_but_interest_signal_strong",
            "normal_distribution_attribution_allowed": False,
            "content_validation_passed": False,
            "direction_established": False,
        },
        "current_assessment": {
            "core_value_signal": "strong_interest_signal_inside_policy_limited_sample",
            "platform_policy_risk": "high",
            "risk_source": "画面触发“引导至风险不可控渠道”",
            "assessment_confidence": "medium_for_recording_only",
            "assessment_boundary": "只能作为异常样本文案结构和平台风险参考，不能作为正常自然流量表现。",
        },
        "segments": [
            segment(
                "opening_simple_flow",
                "大家好，短视频自动流的最简单流程。",
                "直接给出选题和流程承诺。",
                "这条讲什么？",
                ["2s_bounce", "3s_retention"],
                "平台减推污染下不能用自然留存归因，只能记录开头表达风险。",
                ["platform_risk_packaging", "opening_packaging"],
                ["短视频自动流的最简单流程"],
                ["不得改 raw 文案", "不得写内容通过"],
            ),
            segment(
                "one_sentence_prompt",
                "先打开豆包，只输入了一句话：我想用吹做一个短视频自动流。",
                "展示从一句话需求开始。",
                "这个流程怎么启动？",
                ["favorite_rate", "like_rate"],
                "强收藏可能来自“一句话开始”的实用感，但样本被减推污染。",
                ["evidence_expression"],
                ["一句话 prompt 起步"],
                ["不得把 56/6/9 写成截图确认", "不得扩展成工具引流"],
            ),
            segment(
                "plan_versions",
                "用tree搭建短视频自动流，从零基础清量版到无人值守全自动化版。",
                "把需求拆成可升级层级。",
                "自动流是不是可以从小流程开始？",
                ["favorite_rate"],
                "该段实用性强，但自动化/无人值守表达有平台风险。",
                ["platform_risk_packaging", "tone_and_language"],
                ["从小流程到升级版的层级"],
                ["不得弱化平台风险记录"],
            ),
            segment(
                "workflow_chain",
                "选择题、策划、脚本、生成、分镜、制作视频、生成或者剪辑、配音、字幕、封面、标题、自动发布。",
                "展示完整工位链路。",
                "短视频生产能拆成哪些工位？",
                ["favorite_rate", "like_plus_favorite_action_rate"],
                "高收藏可能来自流程清单，但自动发布等词不能直接复用进安全版。",
                ["middle_structure", "risk_word_replacement"],
                ["流程工位拆解"],
                ["不得把自动发布写成发布引导"],
            ),
            segment(
                "tree_prompt",
                "主要是想做一个vlog的视频自动流，先给我一个prompt，让tree帮我把架构搭建出来。",
                "从需求转为架构 prompt。",
                "怎么把想法变成架构输入？",
                ["average_watch_time"],
                "工具名和架构搭建可作为兴趣点，但需要安全表达。",
                ["evidence_expression", "platform_risk_packaging"],
                ["prompt -> 架构搭建"],
                ["不得新增下载入口或工具包承诺"],
            ),
            segment(
                "module_translation",
                "先固定账号风格，再决定拍什么，再写脚本，再拆镜头，再匹配素材，再做后期，最后导出成片和发布物料。",
                "把复杂模块翻成人话。",
                "这些模块对应人话里的哪些步骤？",
                ["favorite_rate", "comment_count"],
                "这是 V002 最可复用的结构表达。",
                ["middle_structure", "tone_and_language"],
                ["把复杂模块翻成人话"],
                ["不得写成系统已跑通"],
            ),
            segment(
                "solo_coder_execution",
                "把它生成的这份prompt真的放进了tree的solo coder。",
                "证明不是只截图保存，而是进入执行工具。",
                "有没有真的开始执行？",
                ["like_rate", "favorite_rate"],
                "真实执行感是兴趣信号来源之一，但也可能触发平台工具风险。",
                ["evidence_expression", "platform_risk_packaging"],
                ["真的放进 solo coder"],
                ["不得写成工具引导"],
            ),
            segment(
                "task_list",
                "updating tasks，还有十一个代办。",
                "展示任务拆解成可执行列表。",
                "AI 有没有拆成任务？",
                ["favorite_rate"],
                "任务列表能增强可复用价值。",
                ["evidence_expression"],
                ["十一个代办"],
                ["不得改 raw 文案"],
            ),
            segment(
                "project_structure",
                "项目目录vlog automation workflow。下面有：modules、templates、workflows、config、assets、friend and logs。",
                "以目录结构证明初步形状。",
                "有没有项目目录？",
                ["favorite_rate", "completion_rate"],
                "目录证据强，但画面里的英文路径/工具结构需做安全遮挡和表达降风险。",
                ["evidence_expression", "platform_risk_packaging"],
                ["有没有项目目录"],
                ["不得把它写成完整系统已跑通"],
            ),
        ],
    }


def build_v004_structure_map() -> dict[str, Any]:
    return {
        "video_id": "V004",
        "copy_id": "V004_copy_v1",
        "source_path": rel(V004_RAW_PATH),
        "structure_version": "copy_structure_map_v1",
        "sample_boundary": {
            "operation_record_status": "latest_operation_sample_pre_24h",
            "review_window": "pre_24h",
            "snapshot_label": "interim_17h_snapshot",
            "formal_copy_revision_allowed": False,
            "current_operation_target_switched": False,
        },
        "current_assessment": {
            "core_claim": "真正拉开差距的不是数据，是复盘能力。",
            "actual_metrics_favorite_count": 0,
            "raw_copy_mentions_previous_case_favorite_count": 3,
            "assessment_confidence": "low_for_diagnosis / high_for_recording",
            "assessment_boundary": "只能记录 V004 早期样本和文案结构，不能判断方向失败、内容通过或正式下一条变量。",
        },
        "segments": [
            segment(
                "opening_claim",
                "AI 时代，真正拉开差距的不是数据，是复盘能力。",
                "用反常识观点开场，把讨论从数据数量转向复盘能力。",
                "为什么有数据还不够？",
                ["2s_bounce", "3s_retention"],
                "如果早期 2s 跳出仍高，可能说明抽象判断仍需要更早落到观众痛点。",
                ["opening_packaging"],
                ["不是数据，是复盘能力"],
                ["不得改 raw 文案", "不得写方向失败"],
            ),
            segment(
                "previous_case_conflict",
                "我这条视频只有 141 播放，2 秒跳出接近 50%。",
                "引用 V003 真实数据冲突，说明低播放也能提供复盘线索。",
                "上一条到底差在哪里？",
                ["2s_bounce", "5s_completion"],
                "这是前一条案例引用，不得混作 V004 自身数据。",
                ["evidence_expression", "opening_packaging"],
                ["141 播放", "2 秒跳出接近 50%"],
                ["不得写 V004 favorite_count = 3"],
            ),
            segment(
                "problem_reframe",
                "下一条最该先改的，不是方向，而是开头。",
                "给出单变量复盘结论。",
                "低播放后应该先改什么？",
                ["5s_completion", "average_watch_time"],
                "当前 V004 自身只是 pre_24h，不能把该判断升级成最终结论。",
                ["bridge_3_8s", "opening_packaging"],
                ["不是方向，而是开头"],
                ["不得生成正式下一条视频执行 prompt"],
            ),
            segment(
                "bad_review_pattern",
                "播放低，就怀疑选题。点赞少，就怀疑表达。没人私信，就怀疑方向。",
                "指出常见错误复盘方式。",
                "为什么很多人的复盘没用？",
                ["average_watch_time", "comment_count"],
                "如果中段弱，可能要压缩反面例子，让观众更快看到正解。",
                ["middle_structure", "tone_and_language"],
                ["播放低/点赞少/没人私信的误判链"],
                ["不得把 V004 55 播放写成选题失败"],
            ),
            segment(
                "problem_layering",
                "真正有用的是，你能不能从数据里拆出问题层级。",
                "把复盘方法落到问题分层。",
                "数据该怎样变成下一步动作？",
                ["favorite_rate", "average_watch_time"],
                "V004 favorite_rate 为 0%，但 pre_24h 不能判内容无价值。",
                ["evidence_expression", "middle_structure"],
                ["问题层级"],
                ["不得把 0 收藏写成价值不存在"],
            ),
            segment(
                "single_variable_rule",
                "我只先改一个变量：开头 5 秒。",
                "明确单变量迭代原则。",
                "下一条只改哪里？",
                ["2s_bounce", "3s_retention", "5s_completion"],
                "这是文案中的复盘原则，不是本轮正式执行指令。",
                ["opening_packaging"],
                ["只先改一个变量", "开头 5 秒"],
                ["不得升级成正式执行 prompt"],
            ),
            segment(
                "metric_to_action_system",
                "真正有用的复盘，应该逼你回答三个问题：",
                "把指标转成三问结构。",
                "什么样的复盘才有用？",
                ["average_watch_time", "completion_rate"],
                "如果尾段弱，三问结构可能需要更早出现。",
                ["middle_structure", "evidence_expression"],
                ["哪一层出了问题", "下一条只改哪个变量", "改完看哪个指标"],
                ["不得改成 KPI 表"],
            ),
            segment(
                "previous_value_signal",
                "这条视频虽然播放低，但它还有 3 个收藏。",
                "引用 V003 的小正信号，说明价值可能出现得太晚。",
                "低播放是不是完全没价值？",
                ["favorite_rate"],
                "这是 V003 案例引用；V004 actual favorite_count = 0。",
                ["evidence_expression"],
                ["3 个收藏是上一条案例"],
                ["不得混写 V004 actual_metrics"],
            ),
            segment(
                "ending_iteration",
                "那你就不是在碰运气。你是在迭代。",
                "把数据复盘收束为迭代方法。",
                "这套方法最终改变什么？",
                ["completion_rate", "average_watch_time"],
                "结尾能否成立需要等待更完整数据。",
                ["tone_and_language"],
                ["不是碰运气，是迭代"],
                ["不得写商业验证成立"],
            ),
        ],
    }


def ensure_base_records(root: Path) -> None:
    ensure_v002_raw_copy(root)
    ensure_raw_copy(root)
    ensure_v004_raw_copy(root)
    write_json(root, V002_RECORD_PATH, build_v002_copy_record())
    write_json(root, V002_STRUCTURE_PATH, build_v002_structure_map())
    write_json(root, V003_RECORD_PATH, build_copy_record())
    write_json(root, V003_STRUCTURE_PATH, build_structure_map())
    write_json(root, V004_RECORD_PATH, build_v004_copy_record())
    write_json(root, V004_STRUCTURE_PATH, build_v004_structure_map())
    write_json(root, COPY_REGISTRY_PATH, build_copy_registry())


def infer_copy_decision(operation_report: dict[str, Any]) -> dict[str, Any]:
    operation_state = operation_report.get("current_project_state", {})
    next_decision = operation_report.get("next_episode_decision", {})
    partial_data = operation_state.get("current_data_goal_anchor_status") == "partial_data_recorded"
    two_second_bounce = metric_number(operation_report, "two_second_bounce_rate")
    five_second_completion = metric_number(operation_report, "five_second_completion_rate")
    favorite_rate = metric_number(operation_report, "favorite_rate")
    recommendation_page = metric_number(operation_report, "traffic_source_recommendation_page")
    average_watch_time = metric_value(operation_report, "average_watch_time")

    if partial_data:
        formal_copy_revision_allowed = False
        low_confidence_prepare_allowed = True
    else:
        formal_copy_revision_allowed = bool(next_decision.get("can_enter_next_episode_execution"))
        low_confidence_prepare_allowed = not formal_copy_revision_allowed

    problem_layer = "opening_packaging"
    supporting_problem_layers = ["bridge_3_8s"]
    rule_trace = [
        "current_operation_report says V003 is partial_data_recorded -> formal_copy_revision = blocked",
        "recommendation_page is high and 2s_bounce is high -> prioritize opening_packaging",
        "5s_completion is weak -> allow low-confidence bridge_3_8s preparation",
        "favorite_rate has a small positive signal -> do not jump to topic_angle failure",
    ]

    return {
        "video_id": "V003",
        "copy_id": "V003_copy_v1",
        "decision_version": "copy_iteration_decision_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_paths": {
            "operation_report": rel(OPERATION_REPORT_PATH),
            "final_user_operation_result": rel(FINAL_USER_OPERATION_RESULT_PATH),
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "copy_record": rel(V003_RECORD_PATH),
            "structure_map": rel(V003_STRUCTURE_PATH),
        },
        "data_window": CURRENT_DATA_WINDOW,
        "data_confidence": "low",
        "operation_decision_status": next_decision.get("decision_status"),
        "problem_layer": problem_layer,
        "problem_layer_candidates": PROBLEM_LAYERS,
        "supporting_problem_layers": supporting_problem_layers,
        "confidence": "low",
        "formal_copy_revision_allowed": formal_copy_revision_allowed,
        "low_confidence_prepare_allowed": low_confidence_prepare_allowed,
        "revision_scope": ["opening_0_3s", "bridge_3_8s"],
        "forbidden_changes": [
            "target_user",
            "topic_direction",
            "offer",
            "whole_script_rewrite",
            "formal_next_video_execution_prompt",
        ],
        "validation_metric": [
            "2s_bounce",
            "3s_retention",
            "5s_completion",
            "average_watch_time",
        ],
        "next_action": "prepare_candidate_opening_revision_brief_only",
        "allow_topic_direction_change": False,
        "allow_target_audience_change": False,
        "require_multiple_samples_for_topic_angle": True,
        "require_7_to_10_failed_samples_for_target_audience_change": True,
        "data_triggers": {
            "play_count": metric_value(operation_report, "play_count"),
            "recommendation_page": metric_value(operation_report, "traffic_source_recommendation_page"),
            "two_second_bounce_rate": metric_value(operation_report, "two_second_bounce_rate"),
            "five_second_completion_rate": metric_value(operation_report, "five_second_completion_rate"),
            "completion_rate": metric_value(operation_report, "completion_rate"),
            "average_watch_time": average_watch_time,
            "favorite_count": metric_value(operation_report, "favorite_count"),
            "favorite_rate": metric_value(operation_report, "favorite_rate"),
            "missing_fields": next_decision.get("missing_data", []),
        },
        "numeric_trace": {
            "recommendation_page_percent": recommendation_page,
            "two_second_bounce_percent": two_second_bounce,
            "five_second_completion_percent": five_second_completion,
            "favorite_rate_percent": favorite_rate,
        },
        "rule_trace": rule_trace,
        "must_not_output": [
            "target_audience_error",
            "topic_direction_failure",
            "whole_script_rewrite",
            "formal_next_video_execution",
            "formal_copy_revision_ready",
        ],
        "status_boundary": {
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "target_audience_changed": False,
            "topic_direction_changed": False,
        },
    }


def build_v002_copy_iteration_decision(operation_report: dict[str, Any]) -> dict[str, Any]:
    play_count = record_metric_value(operation_report, "V002", "play_count", V002_LATEST_USER_METRICS["play_count"])
    like_count = record_metric_value(operation_report, "V002", "like_count", V002_LATEST_USER_METRICS["like_count"])
    favorite_count = record_metric_value(
        operation_report, "V002", "favorite_count", V002_LATEST_USER_METRICS["favorite_count"]
    )
    like_rate = record_metric_value(operation_report, "V002", "like_rate", V002_LATEST_USER_METRICS["like_rate"])
    favorite_rate = record_metric_value(
        operation_report, "V002", "favorite_rate", V002_LATEST_USER_METRICS["favorite_rate"]
    )
    action_rate = record_metric_value(
        operation_report,
        "V002",
        "like_plus_favorite_action_rate",
        V002_LATEST_USER_METRICS["like_plus_favorite_action_rate"],
    )
    return {
        "video_id": "V002",
        "copy_id": "V002_copy_v1",
        "decision_version": "copy_iteration_decision_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_paths": {
            "operation_report": rel(OPERATION_REPORT_PATH),
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "copy_record": rel(V002_RECORD_PATH),
            "structure_map": rel(V002_STRUCTURE_PATH),
            "linked_operation_record": rel(V002_OPERATION_RECORD_PATH),
        },
        "sample_role": "policy_limited_abnormal_operation_sample",
        "abnormal_sample_status": "policy_limited_abnormal_operation_sample",
        "sample_interpretation_label": "policy_limited_but_interest_signal_strong",
        "data_window": "user_latest_reported_metrics_no_screenshot_yet",
        "source_status": V002_LATEST_USER_METRICS["source_status"],
        "latest_user_reported_metrics": {
            "play_count": play_count,
            "like_count": like_count,
            "favorite_count": favorite_count,
            "like_rate": like_rate,
            "favorite_rate": favorite_rate,
            "like_plus_favorite_action_rate": action_rate,
        },
        "historical_metrics_preserved": {
            "play_count": 39,
            "like_count": 5,
            "favorite_count": 8,
            "like_rate": "12.82%",
            "favorite_rate": "20.51%",
            "like_plus_favorite_action_rate": "33.33%",
        },
        "problem_layer": "platform_risk_packaging",
        "supporting_problem_layers": ["copy_structure", "footage_carrier", "risk_word_replacement"],
        "confidence": "medium_for_abnormal_sample_recording_only",
        "formal_copy_revision_allowed": False,
        "low_confidence_prepare_allowed": False,
        "revision_scope": ["record_only", "abnormal_sample_reference_only"],
        "allowed_use": [
            "保留 V002 原始文案，作为异常高意图样本文案证据。",
            "供 ChatGPT 后续做平台风险规避和安全表达桥接时参考。",
            "用于解释 V002 高点赞 / 高收藏只是在减推污染样本中的兴趣信号。",
        ],
        "forbidden_changes": [
            "modify_raw_copy",
            "normal_distribution_attribution",
            "content_validation_passed",
            "direction_established",
            "commercial_validation_established",
            "formal_next_video_execution_prompt",
            "write_user_metrics_as_screenshot_verified",
        ],
        "next_action": "record_only_no_formal_revision",
        "rule_trace": [
            "V002 is policy_limited_abnormal_operation_sample -> exclude from normal distribution attribution",
            "56/6/9 source_status is user_provided_in_chat / no_screenshot_yet -> record as latest user report only",
            "high like/favorite rates -> interest signal strong inside abnormal sample, not content passed",
        ],
        "status_boundary": {
            "normal_distribution_sample": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "direction_established": False,
            "raw_copy_modified": False,
        },
    }


def build_v004_copy_iteration_decision(operation_report: dict[str, Any]) -> dict[str, Any]:
    play_count = record_metric_value(operation_report, "V004", "play_count", V004_INTERIM_METRICS["play_count"])
    favorite_count = record_metric_value(
        operation_report, "V004", "favorite_count", V004_INTERIM_METRICS["favorite_count"]
    )
    two_second_bounce = record_metric_value(
        operation_report, "V004", "two_second_bounce_rate", V004_INTERIM_METRICS["two_second_bounce_rate"]
    )
    five_second_completion = record_metric_value(
        operation_report,
        "V004",
        "five_second_completion_rate",
        V004_INTERIM_METRICS["five_second_completion_rate"],
    )
    recommendation_page = record_metric_value(
        operation_report,
        "V004",
        "traffic_source_recommendation_page",
        V004_INTERIM_METRICS["recommendation_page"],
    )
    return {
        "video_id": "V004",
        "copy_id": "V004_copy_v1",
        "decision_version": "copy_iteration_decision_v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "input_paths": {
            "operation_report": rel(OPERATION_REPORT_PATH),
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "copy_record": rel(V004_RECORD_PATH),
            "structure_map": rel(V004_STRUCTURE_PATH),
            "linked_operation_record": rel(V004_OPERATION_RECORD_PATH),
            "linked_data_snapshot": rel(V004_DATA_SNAPSHOT_PATH),
        },
        "sample_role": "latest_operation_sample_pre_24h",
        "data_window": "pre_24h / interim_17h_snapshot",
        "source_status": V004_INTERIM_METRICS["source_status"],
        "latest_interim_metrics": {
            "play_count": play_count,
            "favorite_count": favorite_count,
            "two_second_bounce_rate": two_second_bounce,
            "five_second_completion_rate": five_second_completion,
            "recommendation_page": recommendation_page,
        },
        "actual_metrics_boundary": {
            "V004_actual_favorite_count": favorite_count,
            "raw_copy_mentions_previous_case_favorite_count": 3,
            "must_not_mix": True,
        },
        "problem_layer": "pre_24h_observation_only",
        "supporting_problem_layers": ["opening_packaging", "evidence_expression"],
        "confidence": "low_for_diagnosis",
        "formal_copy_revision_allowed": False,
        "low_confidence_prepare_allowed": False,
        "revision_scope": ["record_only", "wait_24h_72h_7d"],
        "allowed_use": [
            "保留 V004 原始文案和早期数据，作为最新运营样本。",
            "后续等待 24h / 72h / 7d 数据后再判断是否切换 current_operation_target。",
            "记录 raw copy 中 V003 案例引用与 V004 自身数据的边界。",
        ],
        "forbidden_changes": [
            "modify_raw_copy",
            "direction_failure_concluded",
            "content_validation_passed",
            "content_value_absent_concluded",
            "platform_full_validation_concluded",
            "current_operation_target_switch_without_human_confirmation",
            "formal_next_video_execution_prompt",
        ],
        "next_action": "record_only_wait_for_24h_72h_7d_and_human_confirmation",
        "rule_trace": [
            "V004 is interim_17h_snapshot -> not 24h final, not 72h final, not 7d final",
            "V004 actual favorite_count = 0 but raw copy mentions previous case favorite_count = 3",
            "V003 remains current_operation_target until explicit human / ChatGPT confirmation",
        ],
        "status_boundary": {
            "current_operation_target_switched": False,
            "content_validation_advanced": False,
            "send_ready_advanced": False,
            "current_data_goal_anchor_ready": False,
            "next_formal_video_execution_prompt_generated": False,
            "direction_failure_concluded": False,
            "content_value_absent_concluded": False,
            "raw_copy_modified": False,
        },
    }


def render_v002_brief(decision: dict[str, Any]) -> str:
    metrics = decision["latest_user_reported_metrics"]
    return "\n".join(
        [
            "# V002 文案记录与异常样本复盘简报",
            "",
            "> 本简报只用于记录和后续平台风险规避参考；不是正式下一条视频执行 prompt。",
            "",
            "## 1. 样本身份",
            "- `video_id`: `V002`",
            "- `abnormal_sample_status`: `policy_limited_abnormal_operation_sample`",
            "- `sample_interpretation_label`: `policy_limited_but_interest_signal_strong`",
            "- 平台通知：减少作品推荐；原因：引导至风险不可控渠道；触发位置：画面。",
            "",
            "## 2. 最新用户补充数据",
            f"- 播放量：{metrics['play_count']}",
            f"- 点赞量：{metrics['like_count']} / 点赞率 {metrics['like_rate']}",
            f"- 收藏量：{metrics['favorite_count']} / 收藏率 {metrics['favorite_rate']}",
            f"- 点赞 + 收藏动作率：{metrics['like_plus_favorite_action_rate']}",
            "- `source_status`: `user_provided_in_chat / no_screenshot_yet`",
            "",
            "## 3. 可用判断",
            "- V002 是平台减推污染样本，但兴趣信号强。",
            "- 原始文案可用于分析为什么“流程拆解 + 真实执行证据”有吸引力。",
            "- 后续安全版只能参考结构，不能照搬高风险表达。",
            "",
            "## 4. 禁止判断",
            "- 不得写 V002 是正常自然流量样本。",
            "- 不得写 V002 内容通过、方向成立或商业验证成立。",
            "- 不得把 56/6/9 写成截图确认数据。",
            "- 不得生成正式下一条视频执行 prompt。",
            "",
        ]
    )


def render_v004_brief(decision: dict[str, Any]) -> str:
    metrics = decision["latest_interim_metrics"]
    return "\n".join(
        [
            "# V004 文案记录与 interim_17h 数据简报",
            "",
            "> 本简报只用于记录 V004 早期数据和 raw copy；不是正式下一条视频执行 prompt。",
            "",
            "## 1. 样本身份",
            "- `video_id`: `V004`",
            "- `operation_record_status`: `latest_operation_sample_pre_24h`",
            "- `snapshot_label`: `interim_17h_snapshot`",
            "- 当前不切换 `current_operation_target`，V003 仍是当前运营目标。",
            "",
            "## 2. V004 早期数据",
            f"- 播放量：{metrics['play_count']}",
            f"- 收藏量：{metrics['favorite_count']}（V004 自身数据）",
            f"- 2s 跳出：{metrics['two_second_bounce_rate']}",
            f"- 5s 完播：{metrics['five_second_completion_rate']}",
            f"- 推荐页来源：{metrics['recommendation_page']}",
            "- `source_status`: `screenshot_archived_to_repo_and_user_provided_visual_read`",
            "",
            "## 3. 文案引用边界",
            "- raw copy 中“3 个收藏”引用的是 V003 复盘案例，不是 V004 自身数据。",
            "- V004 actual_metrics.favorite_count = 0。",
            "",
            "## 4. 禁止判断",
            "- 不得写 V004 方向失败。",
            "- 不得写 0 收藏证明内容无价值。",
            "- 不得写推荐页 95.2% 证明平台已充分验证。",
            "- 不得生成正式下一条视频执行 prompt。",
            "",
        ]
    )


def render_next_brief(decision: dict[str, Any]) -> str:
    triggers = decision["data_triggers"]
    missing = triggers.get("missing_fields", [])
    return "\n".join(
        [
            "# V003 下一版文案修改简报",
            "",
            "> 本简报给 ChatGPT 读取；它不是正式下一条视频执行 prompt，也不是 Codex 最终定稿。",
            "",
            "## 1. 当前判断",
            "当前不是换方向，也不是换人群，而是低置信度准备开头 0-3 秒和 3-8 秒承接。",
            "",
            "## 2. 数据触发原因",
            f"- 2s 跳出：{triggers.get('two_second_bounce_rate')}",
            "- 3s 留存：missing",
            f"- 5s 完播：{triggers.get('five_second_completion_rate')}",
            f"- 完播率：{triggers.get('completion_rate')}",
            f"- 平均观看：{triggers.get('average_watch_time')}",
            f"- 收藏：{triggers.get('favorite_count')} / 收藏率 {triggers.get('favorite_rate')}",
            "- 缺失数据：" + "、".join(missing),
            "",
            "## 3. 这版文案好的地方",
            "- 核心观点成立：目标不是 KPI 表，而是逼出下一步动作。",
            "- “播放是入口，收藏是认可，私信要评分”可保留。",
            "- “每条只改一个主变量”可保留。",
            "- “哪一层出了问题，下一条只改哪个变量，改完看哪个指标”是本条最有价值的判断。",
            "",
            "## 4. 这版文案不好的地方",
            "- 开头太像概念判断，观众还没看到真实冲突就进入 KPI 讨论。",
            "- 太快进入 KPI / 数据飞轮 / 北极星目标等内部语言。",
            "- 缺少 V003 真实数据冲突作为开场证据。",
            "- 观众代入不足，没有先说“为什么你看了数据还是不知道下一条改哪”。",
            "- 客资相关词疑似有错字：`克资`、`刻字定义`、`克兹`，只在备注修正，不改 raw 原文。",
            "",
            "## 5. 下一版只改哪里",
            "- 开头 0-3 秒",
            "- 3-8 秒承接",
            "",
            "## 6. 哪些不能动",
            "- 不改目标用户。",
            "- 不改核心选题方向。",
            "- 不改中段核心判断。",
            "- 不改承接 / offer。",
            "- 不做全文重写。",
            "",
            "## 7. 给 ChatGPT 的改稿指令",
            f"下一版先把开头从“别再让 AI 给你定 KPI”改成真实数据冲突切入，优先用 V003 的 {triggers.get('play_count')} 播放、2s 跳出 {triggers.get('two_second_bounce_rate')}、收藏 {triggers.get('favorite_count')} 作为开场证据，再转入“AI 真正有用的是判断下一条先改哪”。不要重写全片，只重写开头和 3-8 秒承接。",
            "",
            "## 8. 改完看什么指标",
            "- 2s bounce",
            "- 3s retention",
            "- 5s completion",
            "- average_watch_time",
            "",
        ]
    )


def build_latest_report(decision: dict[str, Any]) -> dict[str, Any]:
    return {
        "system_name": "copy_iteration_decision_system",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "current_copy_version": "V003_copy_v1 / v1_raw",
        "current_data_window": CURRENT_DATA_WINDOW,
        "current_problem_layer": decision["problem_layer"],
        "confidence": decision["confidence"],
        "formal_copy_revision_allowed": decision["formal_copy_revision_allowed"],
        "low_confidence_prepare_allowed": decision["low_confidence_prepare_allowed"],
        "revision_scope_allowed": decision["revision_scope"],
        "registered_copy_records": [
            {
                "video_id": "V002",
                "copy_id": "V002_copy_v1",
                "sample_role": "policy_limited_abnormal_operation_sample",
                "record_status": "recorded_abnormal_sample_reference_only",
                "raw_copy_path": rel(V002_RAW_PATH),
                "decision_path": rel(V002_DECISION_PATH),
            },
            {
                "video_id": "V003",
                "copy_id": "V003_copy_v1",
                "sample_role": "current_operation_target",
                "record_status": "low_confidence_prepare_only",
                "raw_copy_path": rel(V003_RAW_PATH),
                "decision_path": rel(V003_DECISION_PATH),
            },
            {
                "video_id": "V004",
                "copy_id": "V004_copy_v1",
                "sample_role": "latest_operation_sample_pre_24h",
                "record_status": "recorded_latest_sample_pre_24h_only",
                "raw_copy_path": rel(V004_RAW_PATH),
                "decision_path": rel(V004_DECISION_PATH),
            },
        ],
        "keep_items": [
            "核心观点：目标不是 KPI 表，而是下一步动作判断系统。",
            "播放是入口，收藏是认可，私信要评分。",
            "每条只改一个主变量。",
        ],
        "forbidden_items": decision["forbidden_changes"],
        "when_continue_copy_revision": "补齐 7d 或下一轮同类样本后，若 2s/3s/5s 仍弱，继续调 opening_packaging 和 bridge_3_8s。",
        "when_adjust_topic_angle": "只有多个正常分发样本在开头、结构、语气测试后仍收藏/评论/需求信号持续弱，才进入 topic_angle 判断。",
        "when_allow_new_target_audience": "必须 7-10 个正常样本经过开头、结构、语气测试仍失败后，才允许讨论 target_audience 变化。",
        "chatgpt_read_first": rel(V003_BRIEF_PATH),
        "paths": {
            "copy_registry": rel(COPY_REGISTRY_PATH),
            "v002_raw_copy": rel(V002_RAW_PATH),
            "v002_copy_record": rel(V002_RECORD_PATH),
            "v002_structure_map": rel(V002_STRUCTURE_PATH),
            "v002_copy_iteration_decision": rel(V002_DECISION_PATH),
            "v002_next_copy_revision_brief": rel(V002_BRIEF_PATH),
            "v003_raw_copy": rel(V003_RAW_PATH),
            "v003_copy_record": rel(V003_RECORD_PATH),
            "v003_structure_map": rel(V003_STRUCTURE_PATH),
            "v003_copy_iteration_decision": rel(V003_DECISION_PATH),
            "v003_next_copy_revision_brief": rel(V003_BRIEF_PATH),
            "v004_raw_copy": rel(V004_RAW_PATH),
            "v004_copy_record": rel(V004_RECORD_PATH),
            "v004_structure_map": rel(V004_STRUCTURE_PATH),
            "v004_copy_iteration_decision": rel(V004_DECISION_PATH),
            "v004_next_copy_revision_brief": rel(V004_BRIEF_PATH),
            "latest_copy_iteration_report_md": rel(LATEST_REPORT_MD),
            "script_path": rel(SCRIPT_PATH),
        },
        "status_boundary": decision["status_boundary"],
    }


def render_latest_report_md(report: dict[str, Any]) -> str:
    lines = [
        "# 最新文案迭代报告",
        "",
        "## 当前结论",
        f"- 当前文案版本：`{report['current_copy_version']}`",
        f"- 当前数据窗口：`{report['current_data_window']}`",
        f"- 当前问题层级：`{report['current_problem_layer']}`",
        f"- 置信度：`{report['confidence']}`",
        "- 本轮只允许改：`opening_0_3s + bridge_3_8s`",
        "- 当前不允许：全文重写、换选题方向、换目标人群、生成正式下一条视频执行 prompt。",
        "",
        "## 已登记文案记录",
    ]
    for item in report.get("registered_copy_records", []):
        lines.append(
            f"- `{item['video_id']}` / `{item['copy_id']}`：`{item['sample_role']}`，`{item['record_status']}`"
        )
    lines.extend(
        [
            "",
            "## 保留项",
        ]
    )
    lines.extend(f"- {item}" for item in report["keep_items"])
    lines.extend(["", "## 禁止项"])
    lines.extend(f"- `{item}`" for item in report["forbidden_items"])
    lines.extend(
        [
            "",
            "## 什么时候继续调文案",
            report["when_continue_copy_revision"],
            "",
            "## 什么时候调选题方向",
            report["when_adjust_topic_angle"],
            "",
            "## 什么时候允许打新人群",
            report["when_allow_new_target_audience"],
            "",
            "## ChatGPT 下一步读取",
            f"- `{report['chatgpt_read_first']}`",
            "",
            "## 状态边界",
        ]
    )
    for key, value in report["status_boundary"].items():
        lines.append(f"- {key}: `{str(value).lower()}`")
    lines.append("")
    return "\n".join(lines)


def build_and_write(root: Path) -> dict[str, Any]:
    operation_report = load_json(root, OPERATION_REPORT_PATH)
    read_text(root, FINAL_USER_OPERATION_RESULT_PATH)
    ensure_base_records(root)

    copy_record = load_json(root, V003_RECORD_PATH)
    structure_map = load_json(root, V003_STRUCTURE_PATH)
    registry = load_json(root, COPY_REGISTRY_PATH)
    decision = infer_copy_decision(operation_report)
    v002_decision = build_v002_copy_iteration_decision(operation_report)
    v004_decision = build_v004_copy_iteration_decision(operation_report)

    write_json(root, V002_DECISION_PATH, v002_decision)
    write_text(root, V002_BRIEF_PATH, render_v002_brief(v002_decision))
    write_json(root, V003_DECISION_PATH, decision)
    write_text(root, V003_BRIEF_PATH, render_next_brief(decision))
    write_json(root, V004_DECISION_PATH, v004_decision)
    write_text(root, V004_BRIEF_PATH, render_v004_brief(v004_decision))
    latest_report = build_latest_report(decision)
    write_json(root, LATEST_REPORT_JSON, latest_report)
    write_text(root, LATEST_REPORT_MD, render_latest_report_md(latest_report))

    validation = validate_outputs(root)
    validation["records_loaded"] = {
        "copy_record": copy_record["copy_id"],
        "structure_segments": len(structure_map["segments"]),
        "registry_records": len(registry["records"]),
    }
    return validation


def validate_outputs(root: Path) -> dict[str, Any]:
    output_paths = [
        COPY_REGISTRY_PATH,
        V002_RAW_PATH,
        V002_RECORD_PATH,
        V002_STRUCTURE_PATH,
        V002_DECISION_PATH,
        V002_BRIEF_PATH,
        V003_RAW_PATH,
        V003_RECORD_PATH,
        V003_STRUCTURE_PATH,
        V003_DECISION_PATH,
        V003_BRIEF_PATH,
        V004_RAW_PATH,
        V004_RECORD_PATH,
        V004_STRUCTURE_PATH,
        V004_DECISION_PATH,
        V004_BRIEF_PATH,
        LATEST_REPORT_JSON,
        LATEST_REPORT_MD,
    ]
    missing = [rel(path) for path in output_paths if not (root / path).exists()]
    if missing:
        raise RuntimeError("Missing copy iteration outputs: " + ", ".join(missing))

    v002_raw = read_text(root, V002_RAW_PATH)
    if v002_raw != V002_RAW_COPY:
        raise RuntimeError("V002 raw copy was modified")

    raw = read_text(root, V003_RAW_PATH)
    if raw != RAW_COPY:
        raise RuntimeError("V003 raw copy was modified")

    v004_raw = read_text(root, V004_RAW_PATH)
    if v004_raw != V004_RAW_COPY:
        raise RuntimeError("V004 raw copy was modified")

    parsed_json = []
    for path in [
        COPY_REGISTRY_PATH,
        V002_RECORD_PATH,
        V002_STRUCTURE_PATH,
        V002_DECISION_PATH,
        V003_RECORD_PATH,
        V003_STRUCTURE_PATH,
        V003_DECISION_PATH,
        V004_RECORD_PATH,
        V004_STRUCTURE_PATH,
        V004_DECISION_PATH,
        LATEST_REPORT_JSON,
    ]:
        load_json(root, path)
        parsed_json.append(rel(path))

    registry = load_json(root, COPY_REGISTRY_PATH)
    v002_record = load_json(root, V002_RECORD_PATH)
    v002_decision = load_json(root, V002_DECISION_PATH)
    record = load_json(root, V003_RECORD_PATH)
    structure = load_json(root, V003_STRUCTURE_PATH)
    decision = load_json(root, V003_DECISION_PATH)
    v004_record = load_json(root, V004_RECORD_PATH)
    v004_decision = load_json(root, V004_DECISION_PATH)
    latest = load_json(root, LATEST_REPORT_JSON)

    registry_ids = {item["video_id"] for item in registry.get("records", [])}
    if "V002" not in registry_ids:
        raise RuntimeError("V002 copy registry entry missing")
    if "V004" not in registry_ids:
        raise RuntimeError("V004 copy registry entry missing")
    if v002_record["raw_copy_modified"]:
        raise RuntimeError("V002 raw copy must remain unmodified")
    if v002_record["abnormal_sample_status"] != "policy_limited_abnormal_operation_sample":
        raise RuntimeError("V002 abnormal sample status missing")
    if v002_decision["sample_interpretation_label"] != "policy_limited_but_interest_signal_strong":
        raise RuntimeError("V002 interest signal label missing")
    if v002_decision["formal_copy_revision_allowed"]:
        raise RuntimeError("V002 must not allow formal copy revision")
    if v002_decision["status_boundary"]["normal_distribution_sample"]:
        raise RuntimeError("V002 must not become a normal distribution sample")
    if v004_record["actual_metrics_boundary"]["V004_actual_favorite_count"] != 0:
        raise RuntimeError("V004 actual favorite count must remain 0")
    if v004_record["actual_metrics_boundary"]["raw_copy_mentions_previous_case_favorite_count"] != 3:
        raise RuntimeError("V004 previous-case favorite count mention must remain 3")
    if v004_decision["formal_copy_revision_allowed"]:
        raise RuntimeError("V004 must not allow formal copy revision from pre-24h data")
    if v004_decision["status_boundary"]["current_operation_target_switched"]:
        raise RuntimeError("V004 must not switch current operation target in copy iteration system")

    required_segments = {
        "opening_0_3s",
        "bridge_3_8s",
        "problem_setup",
        "negative_example",
        "turning_point",
        "positive_system",
        "metric_explanation",
        "lead_quality_boundary",
        "core_claim",
        "summary_rules",
        "ending_takeaway",
    }
    actual_segments = {item["segment_id"] for item in structure["segments"]}
    missing_segments = sorted(required_segments - actual_segments)
    if missing_segments:
        raise RuntimeError("Missing structure segments: " + ", ".join(missing_segments))

    if not record["suspected_typos"]:
        raise RuntimeError("suspected typos were not recorded")
    if decision["problem_layer"] != "opening_packaging":
        raise RuntimeError("V003 problem_layer must remain opening_packaging")
    if decision["confidence"] != "low":
        raise RuntimeError("V003 confidence must remain low")
    if decision["formal_copy_revision_allowed"]:
        raise RuntimeError("formal copy revision must be blocked for V003 interim data")
    if not decision["low_confidence_prepare_allowed"]:
        raise RuntimeError("low confidence preparation must be allowed")
    if decision["allow_target_audience_change"] or decision["allow_topic_direction_change"]:
        raise RuntimeError("target audience or topic direction change was incorrectly allowed")
    if latest["status_boundary"]["next_formal_video_execution_prompt_generated"]:
        raise RuntimeError("formal next video execution prompt must not be generated")

    scan_texts = "\n".join(
        read_text(root, path)
        for path in [
            V002_DECISION_PATH,
            V002_BRIEF_PATH,
            V003_DECISION_PATH,
            V003_BRIEF_PATH,
            V004_DECISION_PATH,
            V004_BRIEF_PATH,
            LATEST_REPORT_JSON,
            LATEST_REPORT_MD,
        ]
        if (root / path).exists()
    ).lower()
    forbidden_scan = {
        key: any(pattern.lower() in scan_texts for pattern in patterns)
        for key, patterns in FORBIDDEN_STATUS_PATTERNS.items()
    }
    if any(forbidden_scan.values()):
        raise RuntimeError(f"Forbidden status phrase found: {forbidden_scan}")

    return {
        "outputs_exist": [rel(path) for path in output_paths],
        "json_parse_passed": parsed_json,
        "v002_raw_copy_sha256": sha256_text(v002_raw),
        "v002_raw_copy_matches_locked_source": True,
        "v002_registered": True,
        "v002_abnormal_sample_status": v002_record["abnormal_sample_status"],
        "v002_sample_interpretation_label": v002_decision["sample_interpretation_label"],
        "v004_raw_copy_sha256": sha256_text(v004_raw),
        "v004_raw_copy_matches_locked_source": True,
        "v004_registered": True,
        "v004_operation_record_status": v004_record["operation_record_status"],
        "v004_actual_favorite_count": v004_record["actual_metrics_boundary"]["V004_actual_favorite_count"],
        "v004_raw_copy_mentions_previous_case_favorite_count": v004_record["actual_metrics_boundary"]["raw_copy_mentions_previous_case_favorite_count"],
        "raw_copy_sha256": sha256_text(raw),
        "raw_copy_matches_locked_source": True,
        "suspected_typos_count": len(record["suspected_typos"]),
        "structure_segment_count": len(structure["segments"]),
        "problem_layer": decision["problem_layer"],
        "confidence": decision["confidence"],
        "formal_copy_revision_allowed": decision["formal_copy_revision_allowed"],
        "low_confidence_prepare_allowed": decision["low_confidence_prepare_allowed"],
        "revision_scope": decision["revision_scope"],
        "forbidden_status_scan": forbidden_scan,
        "forbidden_status_advanced": False,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build copy iteration decision outputs from operation data.")
    parser.add_argument("--root", default=str(ROOT), help="Repository root")
    parser.add_argument("--validate-only", action="store_true", help="Validate existing outputs without rewriting")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.validate_only:
        validation = validate_outputs(root)
    else:
        validation = build_and_write(root)
    print(json.dumps(validation, ensure_ascii=False, indent=2))
    return 0 if not validation["forbidden_status_advanced"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
