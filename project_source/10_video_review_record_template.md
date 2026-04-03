# 视频回审记录模板

## 1. 文件定位

本文件用于把单条视频的回审记录正式写成可复盘、可切路由、可继续执行的记录模板。

它必须把“展示路由是否选对”写成正式字段，不能只写内容感受。

## 2. 基本信息

- `review_id`:
- `date`:
- `video_title`:
- `stage`:
- `sample_path`:
- `local_only`:

## 3. 本条视频主路由策略

- `video_scene`:
- `video_goal`:
- `primary_value`:
- `audience_need_first`:
- `video_route_strategy`:
- `why_this_strategy`:

## 4. 本条 block 路由表

| block_id | block_goal | block_need_first | block_carrier | asset_requirement | why_this_carrier |
|---|---|---|---|---|---|
| block_01 |  |  |  |  |  |
| block_02 |  |  |  |  |  |
| block_03 |  |  |  |  |  |

## 5. 当前问题归因

- `main_problem_layer`:
- `is_presentation_route_wrong`:
- `content_issue_or_route_issue`:
- `should_be_ppt_but_used_human`:
- `should_be_human_but_used_ppt`:
- `should_be_hybrid_but_forced_single_route`:
- `highest_priority_fix`:

## 6. 回退与下一轮动作

- `fallback_needed`:
- `fallback_target`:
- `fallback_reason`:
- `next_round_keep_or_switch_route`:
- `next_round_only_change_this_one_thing`:

## 7. 当前一句话记录规则

每条视频回审记录都必须同时写清：主路由策略、block 路由表、当前是否存在展示路由错误、下一轮是继续还是切路由。
