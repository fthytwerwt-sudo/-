# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- 当前 Codex 侧桥接机制现在已覆盖：
  - `codex_source/02_current_execution_context.md`
  - `codex_source/03_research_findings_bridge.md`
  - `codex_source/04_completion_and_review_contract.md`
  - `codex_source/05_execution_deviation_and_reality_sync.md`
  - `codex_source/09_dynamic_source_sync_rules.md`

## 最近一次完成了什么

- `02 ~ 05` 这组执行层桥接文件已基本补到位，不是当前主要尾巴。
- 本轮新增了 `codex_source/09_dynamic_source_sync_rules.md`：
  - 用于规定 GPT 项目源、ChatGPT 侧动态资料和外部动态资料，什么时候必须桥接进 Codex。
- 本轮清理了 `codex_source/01_execution_rules.md` 里的残留旧口径：
  - 去掉了“当前第一优先看火山引擎 TTS API”这类旧长期默认事实
  - 把 `EXEC-008` 收口成当前正式主路径
  - 把 `09_dynamic_source_sync_rules.md` 接入了命中读取与动态资料同步规则

## 当前已确认事实

- 只存在于 GPT 项目源或 ChatGPT 侧的内容，默认不视为 Codex 已知。
- 会影响本轮执行的动态资料，必须进入 `codex_source/03_research_findings_bridge.md` 或本轮执行单。
- 会影响长期前提的动态资料，必须同步更新 `codex_source/02_current_execution_context.md`。
- 当前 `EXEC-008` 已统一为当前正式主路径：
  - 文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传

## 当前最关键的下一步

- 后续凡是 GPT 项目源、ChatGPT 侧或外部动态资料发生变化，先按 `codex_source/09_dynamic_source_sync_rules.md` 判断是参考更新、本轮执行更新还是长期前提更新。
- 如果命中执行更新或长期前提更新，再分别同步到 `03` 或 `02`，不要再让动态资料只停在 ChatGPT 侧。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_source/02_current_execution_context.md`
- 若任务涉及外部结论桥接：
  - `codex_source/03_research_findings_bridge.md`
- 若任务涉及完成回报或验收口径：
  - `codex_source/04_completion_and_review_contract.md`
- 若任务涉及执行现实偏差：
  - `codex_source/05_execution_deviation_and_reality_sync.md`
- 若任务涉及 GPT 项目源更新、ChatGPT 侧动态资料变化或动态资料是否影响执行：
  - `codex_source/09_dynamic_source_sync_rules.md`
