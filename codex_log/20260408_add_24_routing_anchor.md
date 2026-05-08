# 2026-04-08 add_24_routing_anchor

## 本轮目标

- 只补一个缺口：
  - 新增 `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- 让 Codex 侧已统一引用的 `24_*` 锚点文件不再撞空

## 执行前已确认事实

- `AGENTS.md`、`codex_source/00_codex_readme.md`、`codex_source/02_current_execution_context.md`、`codex_source/03_research_findings_bridge.md`
  已开始引用：
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- 当前仓库里真实仍只有：
  - `project_source/19_human_self_footage_hybrid_mainline_rules.md`
- 因此当前冲突不是主线没收口，而是：
  - 入口层已收口
  - 但真实锚点文件缺失

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- 本地 skill 检查：无
- 全局 skill 检查：
  - `using-superpowers`
  - `verification-before-completion`

## 实际改动

- 新增：
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- 刷新：
  - `codex_log/latest.md`
    - 去掉“24 文件还不存在 / 部分成立”的旧状态
    - 改成“24 文件已真实落库”

## 实际执行

- 按用户给定正文原样落库 `24_*`
- 没有改代码
- 没有改 case
- 没有改 config
- 没有改 tests
- 没有删除旧 `19_*` 文件

## 验证

- `已确认`
  - `project_source/24_human_self_footage_light_ppt_routing_rules.md` 已真实存在
- `已确认`
  - Codex 侧已引用 `24_*` 的入口文件不再撞空
- `已确认`
  - `codex_log/latest.md` 不再保留“24 文件不存在”的旧状态

## 当前结果

- 当前仓库已同时存在：
  - 旧 `19_*` 锚点文件
  - 新 `24_*` 锚点文件
- 本轮只完成“补缺失锚点”这一个最小动作
- 没有把任务分支结果误写成已同步回 `codex/user-readable-map`

## 下一步建议

1. 若后续要彻底去重，再单独处理 `19_*` 和 `24_*` 的关系
2. 当前新会话按 Codex 侧入口接手时，已经不会再因为 `24_*` 缺失而撞空
