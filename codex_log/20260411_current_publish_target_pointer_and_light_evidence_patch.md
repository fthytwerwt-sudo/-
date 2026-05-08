# 2026-04-11 current_publish_target 指针与轻量证据包补丁

## 本轮目标

- 补齐当前待发对象 / 当前审核对象的固定指针。
- 统一执行层入口，减少每轮重新找对象、重新翻译术语、重新追本地样片的热机成本。
- 给当前最新样片补一组 Git 可追踪的轻量证据，不再只剩本地 `final.mp4`。

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/12_codex_known_state_three_layer_rules.md`
- `.gitignore`
- `codex_log/20260411_latest_sample_publish_line_review.md`
- `dist/formal_api_demo_user_footage_20260409/{manifest.json,route_plan.json,script.txt,captions.srt,result_summary.json}`

## skill 检查

- `已确认` 仓库本地 `skills/`：不存在。
- `已确认` 全局 `~/.codex/skills` 已检查并采用：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`

## 实际新增文件

- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260411_current_publish_target_pointer_and_light_evidence_patch.md`
- `cases/formal_api_demo_user_footage_execution_20260409.md`

## 实际修改文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_log/latest.md`

## 轻量证据包处理

- `已确认` 本轮把以下文件纳入 Git 可追踪证据：
  - `dist/formal_api_demo_user_footage_20260409/manifest.json`
  - `dist/formal_api_demo_user_footage_20260409/route_plan.json`
  - `dist/formal_api_demo_user_footage_20260409/script.txt`
  - `dist/formal_api_demo_user_footage_20260409/captions.srt`
  - `dist/formal_api_demo_user_footage_20260409/result_summary.json`
- `部分成立` `final.mp4`、preview、原始录屏素材仍保留为 `local_only`，不进入本轮 Git 跟踪范围。

## 输入稿缺口处理

- `已确认` `manifest.json` 指向的 `cases/formal_api_demo_user_footage_execution_20260409.md` 原先确实缺失。
- `已确认` 当前可用证据足够 grounded 补回：
  - `input_snapshot`
  - `video_spec`
  - `presentation_routing`
  - `segments`
- `已确认` 因此本轮选择补回，而不是伪造“未知历史原稿”。

## 入口层统一点

- 新增固定规则：
  - 命中当前待发对象 / 当前最新样片 / 发布线复核 / 当前唯一 blocker / 只改这一条内容时，在 `latest.md` 之后优先读 `codex_log/current_publish_target.md`
  - 需要快速复核轻量证据时，再读 `codex_log/current_publish_target_light_evidence.md`
- 术语统一为：
  - `用户录制素材`
  - `少量 PPT`
- `图片` 不再和正式主线并列混写，只保留为可选辅助承载理解。

## 当前结果

- `已确认` 后续新聊天要找“当前对象是谁”，不必再先翻多条 dated log。
- `已确认` 后续新聊天要看“当前为什么不过线”，不必先追本地 `final.mp4` 才能知道基本状态。
- `已确认` 执行层入口口径已经和当前正式主线收齐到同一套术语。

## 验证计划

- `git diff --check`
- 重新读取：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
  - `codex_log/current_publish_target.md`
  - `codex_log/current_publish_target_light_evidence.md`
- 使用 `git show codex/user-readable-map:路径` 验证回流后的稳定入口文件
