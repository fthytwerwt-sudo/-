# 2026-04-09｜repo_sync_fix_and_source_of_truth_writeback

## 本轮目标

一次性修复《视频工厂》当前“GPT 数据源与 Codex 仓库不同步”问题，并把本轮已锁定正式事实写回仓库。

## 执行前已确认事实

- 技术闭环已跑通
- 当前重点是内容质量、结构稳定、可复用、可回审、可持续压质量
- 当前正式默认主线是“人物 + 用户自己的真实录制素材 + 少量 PPT / 图片辅助”
- pure PPT / 信息卡与 AI talking avatar / 数字人口播都不再是默认主线
- 正式 assembly 继续固定为北京区 `OSS + 云剪 cloud-only`
- `local preview` / `local mp4` 只能算辅助
- demo 只是链路锚点，不是质量样片
- GPT 数据源不会自动同步到 Codex 仓库

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- 目标 `project_source/*` 文件存在性与正文
- 本地 `skills/` 与全局 `~/.codex/skills`

## 审计结论

- `project_source/24_human_self_footage_light_ppt_routing_rules.md` 在主读取分支缺失
- `project_source/00_project_brief.md`、`project_source/01_project_system_prompt.md`、`project_source/06_project_index.md` 仍保留旧的 pure PPT / TTS 优先叙事
- `codex_log/latest.md` 仍停留在上一轮价值规则同步结果
- 执行层里虽已有部分新主线片段，但“GPT 数据源不会自动同步到 Codex 仓库”尚未被统一写成当前源事实

## 实际改动

- 重写 `project_source/00_project_brief.md`
- 重写 `project_source/01_project_system_prompt.md`
- 重写 `project_source/06_project_index.md`
- 重写 `project_source/16_presentation_routing_rules.md`
- 新建 `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- 重写 `codex_source/00_codex_readme.md`
- 重写 `codex_source/01_execution_rules.md`
- 重写 `codex_source/02_current_execution_context.md`
- 重写 `codex_source/03_research_findings_bridge.md`
- 重写 `codex_source/11_ai_knowledge_video_value_bridge.md`
- 重写 `codex_source/12_codex_known_state_three_layer_rules.md`
- 重写 `codex_log/latest.md`
- 新建本日志

## 实际执行

- 从 `codex/user-readable-map` 新建工作分支 `codex/repo-sync-fix-20260409`
- 按允许修改范围内文件进行覆盖 / 新建
- 运行 `git diff --check`
- commit 当前工作分支
- push `codex/repo-sync-fix-20260409`
- fast-forward 本地 `codex/user-readable-map`
- 后续只剩：
  - commit 最终 `formal_synced` 日志状态
  - push `codex/user-readable-map`
  - 用 `git show codex/user-readable-map:...` 复核关键文件

## 当前结果

- 当前结果 `已确认` 是：仓库口径同步修复已落文件，且主读取分支已在本地完成 fast-forward
- 当前结果 `待验证` 是：远端 `codex/user-readable-map` push 后的关键文件复核
- 当前不得写成：新主线样片已验证成立
