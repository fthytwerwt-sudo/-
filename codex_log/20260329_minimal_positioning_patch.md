# 20260329 Minimal Positioning Patch

## 1. 本轮目标

- 在不重写项目脑的前提下，再做一轮最小口径补丁。
- 把项目更明确地收口为“个人内部使用的、Prompt 驱动的、Codex 可执行的视频内核”。

## 2. 执行前已确认事实

- 当前分支上，大方向口径已经基本正确。
- 本轮不是大翻修，也不是补前端方案。
- 用户本轮只允许优先修改：
  - `project_source/00_project_brief.md`
  - `project_source/01_project_system_prompt.md`
  - 如确有必要，再小改 `project_source/06_project_index.md`

## 3. 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/06_project_index.md`
- 本地 / 全局 skill 检查
- `git status --short --branch`
- `git log --oneline -3`

## 4. 实际改动

- 修改 `project_source/00_project_brief.md`
  - 在“目前最值得持续优化的主线”里，补明当前先要压稳的是：
    - `Prompt 驱动 -> ChatGPT 收束 -> Codex 执行 -> 出片 -> 回审`
- 修改 `project_source/01_project_system_prompt.md`
  - 在停止线中补明：
    - 不把项目误写成面向外部客户的产品
- 刷新 `codex_log/latest.md`
  - 明确本轮是“最小口径补丁”，不是新一轮大改

## 5. 实际执行

- 先重读限定范围内的入口文件和三份项目脑文件，确认当前分支已经有一轮较大的定位统一。
- 基于“最小补丁”边界，不去重改 `project_source/03_perplexity_prompt_library.md`、`project_source/06_project_index.md` 或执行层文件。
- 只补两句当前仍值得更明确的核心口径。

## 6. 当前结果

- `project_source/00_project_brief.md` 现在更明确地把“Prompt 驱动 -> ChatGPT 收束 -> Codex 执行 -> 出片 -> 回审”写成当前内部主线。
- `project_source/01_project_system_prompt.md` 现在更明确地防止项目再次被误写成外部客户产品。
- 本轮没有把项目脑扩写成新版本，也没有扩出前端、页面、产品化方案。

## 7. 下一步建议

- 若后续还要继续谈定位，只建议围绕“Prompt 驱动闭环怎么更稳”继续收束，不再重复扩改大段项目脑。
- 若未来真的要进入前端页面阶段，应单独开新任务，而不是继续拿当前默认口径延展。
