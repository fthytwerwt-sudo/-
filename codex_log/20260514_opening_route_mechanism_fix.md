# 20260514_opening_route_mechanism_fix

## 1. 本轮目标

本轮只做《视频工厂｜OPC 一人公司 AI 闭环验证系统》的开头路由机制补全：

- 元素娃娃开头保留为合法 `opening route（开头路线）`。
- 元素娃娃不再作为所有内容唯一默认开头。
- 新增 `opening_route_decision（开头路由判断）`，先判断开头路线，再执行开头。
- 梗图 GIF 开场只作为条件优先路线，不成为新默认死流程。
- 本轮不生成视频、不修改媒体、不推进任何视频动态状态。

## 2. route_decision

```text
route_decision:
  project_route: video_factory
  task_type:
    - project_file_change
    - mechanism_or_route_fix
    - copywriting_route_fix
  responsibility_layer:
    - project_judgment_layer
    - mechanism_fix_layer
    - execution_layer
    - validation_layer
    - sync_layer
  large_task_gate:
    triggered: true
    reason: 本轮涉及开头路由机制、文案路由、主线锚点、执行规则和日志同步，多文件机制修补
    lane_recommendation: audit_lane -> standard_lane after impact check passed
    parallel_recommendation: serial_only
  completion_relay_gate:
    triggered: true
    reason: 多文件影响面扫描、规则写入、日志回流和剩余工作反查
  execution_permission: allowed_after_must_read_passed
```

## 3. state_action_router

```text
state_action_router:
  input_signal: 用户明确纠偏：不是删除元素娃娃，而是让 Codex 自己判断哪种开头更适合；搞笑 GIF 更适合超过 3 秒且需要抓眼 / 起情绪的开头
  current_project_state:
    - mechanism_repair_needed
    - content_route_needed
    - reference_contract_needed
  fact_source_arbitration:
    primary_source: 当前用户明确指令 + 本地 main 当前机制文件
    conflict_detected:
      - 旧口径可能把元素娃娃写成默认开头
    conflict_resolution:
      - 元素娃娃保留为合法 opening route，但不再是所有内容唯一默认开头
  inferred_state:
    - opening_route_should_be_decided_per_content
    - element_doll_opening_retained_as_optional_route
    - meme_gif_opening_preferred_when_opening_longer_than_3s_and_emotional_hook_needed
  confidence: high
  trigger_mechanism:
    - content_route_inference_function
    - Reference-to-Execution Contract
    - Completion Relay Gate
  selected_action:
    - 新增开头路由判断字段
    - 修正元素娃娃默认开头旧口径
    - 同步 Codex 执行侧判断
  forbidden_action:
    - 不删除元素娃娃路线
    - 不把梗图 GIF 写成新唯一默认
    - 不推进视频动态状态
    - 不生成媒体
```

## 4. reference_to_execution_contract

```text
reference_anchor:
  reference_id: 用户本轮上传的抖音截图示例；本地来源路径 /Users/fan/Downloads/IMG_1264.jpg
  reference_type:
    - visual_reference
    - opening_hook_reference
    - raw_feeling_reference
  source_layer: user_provided
  exact_reference_available: true_for_mechanism_observation_only
  must_preserve:
    - 抓眼
    - 起情绪
    - 快速抛问题
    - 开头存在感强
  must_not_copy:
    - 不复刻原图人物 / 头像 / 字体 / 构图
    - 不复用第三方可识别资产
    - 不制造搬运或侵权风险
effect_targets:
  viewer_feeling: 先停一下，被问题抓住，愿意进入后续证据
  information_hierarchy: 开头只负责情绪钩子和核心问题；中段真实录屏仍负责证明
  evidence_clarity: 参考图不承担证据；强证据仍来自用户录屏、前后对比、结果截图或平台数据
function_fields:
  selected_action: 将梗图 GIF 开头写为条件优先 route，并同步四种 opening route 判断
  validation_rule: 规则文件中必须出现 route 条件、职责、禁止项、fallback 和证据边界
blocked_if:
  - 需要精确复刻参考图
  - 需要生成媒体
  - 需要推进动态状态
```

## 5. actual_read_files

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `GPT数据源/12_参考到执行落地契约_reference_to_execution_contract.md`
- `codex_source/20_reference_to_execution_contract.md`
- `codex_source/13_execution_lane_and_parallel_rules.md`
- `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md`
- `/Users/fan/Downloads/IMG_1264.jpg`：只读确认 reference 来源，不复制、不修改。

## 6. impact_check

- `需要修改`：`GPT数据源/05_文案路由规则.md` 缺 `opening_route_decision`。
- `需要修改`：`GPT数据源/04_选题与文案规则.md` 仍有“开头人物壳与结尾总结壳默认统一”旧口径。
- `需要修改`：`GPT数据源/06_当前主线锚点...md` 仍写“开头人物壳默认统一”。
- `需要修改`：`GPT数据源/07_AI知识类视频价值规则.md` 缺“梗图 GIF 开头不算强证据”边界。
- `需要修改`：`GPT数据源/08_当前正式事实.md` 仍把开头人物壳写成 vNext 默认统一事实。
- `需要修改`：`GPT数据源/01_项目系统提示词.md` 属于新会话系统提示入口，仍有“开头人物壳默认统一”旧句，需最小同步。
- `需要修改`：`GPT数据源/00_项目总述.md` 属于新会话默认读取入口，需最小同步，避免旧默认继续误导。
- `需要修改`：`GPT数据源/11_项目状态动作总控器_机制推理层.md` 与 `codex_source/19_project_state_action_router.md` 需补 `content_route_inference_function` / Codex 执行侧规则。
- `需要修改`：`codex_source/01_execution_rules.md` 需补开头执行硬规则。
- `保留现状`：`AGENTS.md`、`codex_source/00_codex_readme.md` 记录的是 v3.1 固定素材锚点，并已写“不是唯一 reference”，未发现把元素娃娃写成所有内容唯一默认开头的入口误导，本轮不改。
- `保留现状`：`project_source/*` 只作历史 / 辅助镜像，不高于 `GPT数据源/` 当前正式机制文件；本轮不扩大修改。
- `保留现状`：`codex_source/locked_reference_registry.md` 只登记后续需要元素娃娃开头时的继承锚点，不等于所有内容默认使用元素娃娃。

## 7. changed_files

- `GPT数据源/00_项目总述.md`
- `GPT数据源/01_项目系统提示词.md`
- `GPT数据源/04_选题与文案规则.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `GPT数据源/08_当前正式事实.md`
- `GPT数据源/11_项目状态动作总控器_机制推理层.md`
- `codex_source/19_project_state_action_router.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260514_opening_route_mechanism_fix.md`

## 8. key_rule_changes

- 新增 `opening_route_decision（开头路由判断）`。
- 四种 opening route 写入：
  - `element_doll_opening（元素娃娃开头）`
  - `meme_gif_opening_hook（梗图 GIF 开场钩子）`
  - `direct_question_title_card（直接问题标题卡）`
  - `screen_first_opening（录屏现场先行开头）`
- 元素娃娃保留，但不再是唯一默认。
- 梗图 GIF 开头是条件优先路线，不是新默认死流程。
- 开头 GIF 只负责抓眼、起情绪、抛问题，不负责证明。
- 用户参考图只继承机制，不复刻资产。

## 9. forbidden_status_check

- `dist/latest_review_pack/`: not_modified
- media files: not_modified
- `content_validation`: not_promoted
- `send_ready`: not_promoted
- `publish_status`: not_promoted
- `voice_validation`: not_promoted
- `final_voice_validated`: not_promoted
- `visual_master_locked`: not_promoted
- `.env / .env.swp / secret`: not_read
- external API: not_called

## 10. validation_result

- `keyword_check`: passed，已检出 `opening_route_decision`、`element_doll_opening`、`meme_gif_opening_hook`、`direct_question_title_card`、`screen_first_opening`、`opening_duration`、`topic_emotion_level`、`controversy_level`、`evidence_start_strength`、`brand_consistency_need`。
- `old_default_phrase_check`: passed，当前正式入口文件中未再出现“开头人物壳默认统一为”或“开头人物壳与结尾总结壳默认统一”的旧开头默认句。
- `reference_boundary_check`: passed，已写入不复刻人物、头像、字体、构图或第三方可识别资产。
- `git_diff_check`: passed，`git diff --check` 无输出。
- `worktree_note`: 既有未跟踪 `.env.swp` 保持未读取、未修改、未纳入本轮改动。

## 11. remaining_work_check

- `must_fix_remaining`: none
- `not_done_by_design`: 未生成视频、未修改媒体、未验证真实视频开头长期效果。
- `true_video_effect_status`: `待验证`

## 12. sync_back_check

当前同步项：

- 机制文件：已写入并通过关键词回读确认。
- `latest.md`：已更新。
- dated log：已新增。
- 入口文件：`GPT数据源/00_项目总述.md`、`GPT数据源/01_项目系统提示词.md` 与 `GPT数据源/08_当前正式事实.md` 已最小同步；`AGENTS.md` 与 `codex_source/00_codex_readme.md` 未发现必须修改的误导口径。

## 13. next_target

下一条真实内容执行前，用 `opening_route_decision（开头路由判断）` 验证 Codex / ChatGPT 能否根据内容目标、开头时长、话题情绪、争议程度、证据强度和品牌一致性需求选择开头路线；真实视频效果仍为 `待验证`。
