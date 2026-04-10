# 2026-04-11 当前最新样片发布线复核

## 本轮目标

- 识别“明天要发的那条内容 / 当前最新样片”到底是哪一个仓库对象。
- 判断它是否达到当前仓库的“可发布测试线”。
- 若这轮结论改变 reading branch 默认已知状态，则把真实状态同步回 `codex/user-readable-map`。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/latest.md`
- `project_source/07_current_formal_facts.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/09_target_state_plan.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- `project_source/16_presentation_routing_rules.md`
- `project_source/22_copy_mode_routing_rules.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `cases/formal_api_demo_human_self_footage.md`
- `cases/ai_report_fluff_trap_45s.md`
- `dist/formal_api_demo_user_footage_20260409/{final.mp4,manifest.json,route_plan.json,script.txt,captions.srt,result_summary.json}`
- `dist/formal_api_demo_ai_report_fluff_trap_45s/result_summary.json`
- `dist/formal_api_demo_report_style_pass/result_summary.json`
- `codex_log/20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample.md`
- `codex_log/20260408_formal_mainline_human_self_footage_shift.md`
- `codex_log/20260409_api_human_mainline_unify_blocked_by_tts_quota.md`

## skill 检查

- `已确认` 仓库本地 `skills/`：不存在。
- `已确认` 全局 `~/.codex/skills` 已检查到：
  - `verification-before-completion`
  - `context-driven-development`
- `已确认` 本轮实际采用：
  - `verification-before-completion`：先取机器结果、文件证据、成片抽帧，再下结论。
  - `context-driven-development`：把判断建立在仓库现有正式上下文，而不是聊天印象。

## 候选对象与最终锁定

### 候选 1
- `dist/formal_api_demo_user_footage_20260409/final.mp4`
- 证据：
  - `dist/` 下最新的 `formal_api_demo*` 样片目录
  - 时长 15 秒，直接贴当前正式主线
  - `route_profile = api_human_local_footage_light_ppt_cloud_editing`

### 候选 2
- `dist/formal_api_demo_ai_report_fluff_trap_45s/`
- 证据：
  - 有明确内容题目
  - 已有较早完整样片记录
  - 但不是最新样片，且更像上一轮题材样片

### 候选 3
- `dist/formal_api_demo_report_style_pass/`
- 证据：
  - 机器结果成功
  - 但更早，且不是当前主线下的最新审核对象

### 最终锁定
- `已确认` 本轮主审核对象定为：`dist/formal_api_demo_user_footage_20260409/final.mp4`
- 选择原因：
  1. 它是当前仓库里最新的主线样片目录。
  2. 它直接对应当前唯一正式主线，而不是旧支线或更早样片。
  3. 用户要求优先判“明天要发的那条内容 / 当前最新样片”，在缺少更直接待发表记号时，这个对象的“证据最新 + 与当前主线最直接相关”最成立。

## reading branch 既有写回检查

- `已确认` 本轮前，`AGENTS.md`、`codex_source/*`、`project_source/*`、`codex_log/latest.md` 中没有这条 15 秒样片的正式验收结论。
- `已确认` 搜索不到：
  - `formal_api_demo_user_footage_20260409`
  - `AI 最耗时间的，不是写`
  - 针对该样片的 `technical_validation / content_validation` 结论
- 结论：
  - 本轮前该状态属于 `待复核事实`

## 审核证据

### 1. 机器与产物层

- `已确认` `dist/formal_api_demo_user_footage_20260409/result_summary.json` 写明：
  - `overall_status = success`
  - `generation_status = success`
  - `assembly_status = success`
  - `cloud_assembly_status = success`
  - `machine_gate_result.generation_gate = success`
  - `machine_gate_result.assembly_gate = success`
- `已确认` `final.mp4` 存在，ffmpeg 元信息显示：
  - 时长 `15.00s`
  - 分辨率 `1080x1920`
  - 视频 H.264
  - 音频 AAC

### 2. 结构与路由层

- `已确认` `route_plan.json` 已按主线拆成 3 个 block：
  - `seg01`：`human`
  - `seg02`：`self_footage`
  - `seg03`：`light_ppt`
- `已确认` 这 3 段的职责分配与当前正式规则基本一致：
  - 判断节点给 `API生成真人`
  - 证据节点给 `用户录制素材`
  - 整理节点给 `少量PPT`
- `部分成立` 这说明“规则没路由到位”不是主因；规则层已经把职责分对了。

### 3. 脚本与字幕层

- `已确认` `script.txt` / `captions.srt` 的三段文案分别承担：
  - 开头判断
  - 中段动作建议
  - 结尾结果句
- `部分成立` 文案方向是对的，但中段“证据段”在成片里没有被画面可读性支撑住。

### 4. 成片人工抽帧观察

- `已确认` 开头帧：
  - API 真人画面成立
  - 第一判断句能接住人
- `已确认` 中段帧：
  - 真实桌面录屏被放进竖版后，上下大面积黑边
  - 核心工作区太小
  - 观众难以在 9 秒内看清“到底压清了什么、如何推进”
- `已确认` 结尾帧：
  - 轻量结果卡风格克制
  - 没有明显越权抢主叙事

### 5. 附带证据缺口（非本轮主 blocker）

- `部分成立` `manifest.json` 的 `input_path` 指向：
  - `/Users/fan/Documents/视频工厂/cases/formal_api_demo_user_footage_execution_20260409.md`
- `已确认` 当前仓库里找不到这个输入文件。
- 影响：
  - 这会削弱可追溯性
  - 但它不是本轮“能不能发”的最高优先级 blocker

## 正式审核结论

- `已确认` 三选一正式结论：
  - `technical_validation 通过，content_validation 未通过`

### 为什么不是“可发布测试线通过”

- `已确认` 当前至少没有满足：
  - `用户录制素材` 真的承担中段主体推进
  - 中段有过程感或证据感能被看清
  - 不触发 `demo 感 / 说明书感`
- `已确认` 因此不满足：
  - `project_source/08_quality_baseline_and_90_score_rules.md` 的必须过线项
  - `project_source/14_content_review_and_loop_governance_rules.md` 的“可发布测试线”

### 为什么不是“technical / content 都未通过”

- `已确认` 机器 gate、成片落地、时长、编码、主线路由都已经成立。
- `已确认` 当前不过线的主因不是链路没跑通，而是内容样片层没有过发布线。

## 唯一最高优先级 blocker

- `已确认` 唯一最高优先级 blocker：
  - `seg02` 的用户录屏在竖版里可读性失守，导致本该承担“主体推进 + 过程证据”的段落只剩“有录屏占位”，没有形成观众可读的真实证据。

## 现在最该改的唯一一点

- `已确认` 现在最该改的唯一一点：
  - 只重做 `seg02` 的竖版证据呈现，让观众在 9 秒内看清一个完整动作或一个明确差值。
- 具体收口方向：
  - 优先改录屏裁切、放大、跟随、局部高亮或直接换成更适合 9:16 的真实素材
  - 不先扩规则
  - 不先重写整条片

## 这是规则问题还是内容问题

- `已确认` 当前更像“明天这条内容本身不过线”。
- 理由：
  - 规则已经把判断 / 证据 / 整理分给了对的 carrier。
  - 真正失手的是当前样片里 `seg02` 的视觉执行，没有把规则要求兑现成可读证据。

## 本轮同步意图

- `已确认` 本轮判断改变了 reading branch 默认应知状态：
  - 之前只知道规则已补强
  - 现在新增了“当前最新 15 秒样片技术过、内容不过，主 blocker 是竖版录屏可读性”
- 因此本轮应同步：
  - `codex_log/latest.md`
  - `codex_log/20260411_latest_sample_publish_line_review.md`

## 样片文件上传边界

- `部分成立` `dist/formal_api_demo_user_footage_20260409/` 当前未纳入 Git 跟踪。
- 这意味着：
  - 样片文件本身当前仍是 `local_only`
  - 但它对应的审核结论会通过日志同步进 `codex/user-readable-map`
