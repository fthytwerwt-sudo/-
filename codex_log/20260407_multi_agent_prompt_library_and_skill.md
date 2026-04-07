# 20260407_multi_agent_prompt_library_and_skill

## 本轮目标

- 把 Codex 多 agent 执行模板正式落地为双层结构：
  - 仓库内版本：`codex_source/10_codex_multi_agent_prompt_library.md`
  - 全局版本：`~/.codex/skills/parallel-explorer-integrator/SKILL.md`
- 保证后续可以直接复用 `2 explorers + 1 integrator` 结构发起多 agent 任务
- 不改项目主线、不改 `project_source/*`、不改代码、不改 case、不扩成大而全 agent 框架

## 当前工作分支

- `codex/round1-visual-pass-conservative`

## 执行前已确认事实

- 当前仓库本地 `skills/`：
  - 不存在
- 当前仓库最接近但不等同的执行层文件：
  - `codex_source/06_execution_gate_and_parallel_rules.md`
  - 它讲的是执行闸门与外部多工位并行，不是当前要落的多 agent prompt library
- 当前全局 skills 中无重名项，但有强相关项：
  - `dispatching-parallel-agents`
  - `subagent-driven-development`
  - `parallel-feature-development`
  - `task-coordination-strategies`
  - `team`
- 本轮采用的命名结论：
  - 新建
  - 避免重名
  - 避免与多写手框架重叠
  - 全局 skill 名称使用：`parallel-explorer-integrator`
- 当前工作树存在与本轮无关的既有修改：
  - `project_source/03_perplexity_prompt_library.md`
  - 本轮未触碰该文件

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `codex_source/06_execution_gate_and_parallel_rules.md`
- `codex_source/02_codex_index.md`
- `/Users/fan/.codex/skills/skill-creator/SKILL.md`
- `/Users/fan/.codex/skills/writing-skills/SKILL.md`
- `/Users/fan/.codex/skills/dispatching-parallel-agents/SKILL.md`
- `/Users/fan/.codex/skills/subagent-driven-development/SKILL.md`
- `/Users/fan/.codex/skills/parallel-feature-development/SKILL.md`
- `/Users/fan/.codex/skills/task-coordination-strategies/SKILL.md`
- `/Users/fan/.codex/skills/team/SKILL.md`

## 审计结论

- 仓库内：
  - `已确认` 没有现成的“多 agent prompt library”同类文件
  - `已确认` 最接近的是 `codex_source/06_execution_gate_and_parallel_rules.md`
- 全局 skills：
  - `已确认` 没有重名 skill
  - `已确认` 有多项强相关但不等同的 skill
- 本轮应采用：
  - `已确认` 新建项目内文件
  - `已确认` 新建全局 skill
  - `已确认` 避免做成泛化 team / 多写手框架

## 实际改动

- 新建：
  - `codex_source/10_codex_multi_agent_prompt_library.md`
    - 项目内版本
    - 固定为《视频工厂》实际工作方式
    - 明确 `2 explorers + 1 integrator`
    - 含 4 套可直接复制使用的 prompt 模板
- 新建：
  - `/Users/fan/.codex/skills/parallel-explorer-integrator/SKILL.md`
    - 全局跨项目 skill
    - 明确 explorers 默认只读
    - integrator 独占写权限
    - 提供标准化 prompt skeleton
- 更新：
  - `codex_source/00_codex_readme.md`
    - 仅补 1 处极短导航提示
- 更新：
  - `codex_log/latest.md`
    - 刷新为本轮最新交接摘要
- 新增：
  - `codex_log/20260407_multi_agent_prompt_library_and_skill.md`
    - 完整执行日志

## 实际执行

- 已按审计结果采用：
  - 项目内版本放仓库
  - 全局版本放 `~/.codex/skills/`
- 已明确让两层结构分工不同：
  - 项目内版本偏《视频工厂》实际工作方式
  - 全局 skill 偏跨项目通用路由
- 本轮未修改：
  - `project_source/*`
  - 代码
  - 测试
  - case

## 实际验证

- 已执行：
  - `test -f codex_source/10_codex_multi_agent_prompt_library.md`
  - `test -f /Users/fan/.codex/skills/parallel-explorer-integrator/SKILL.md`
  - `sed -n '1,260p' codex_source/10_codex_multi_agent_prompt_library.md`
  - `sed -n '1,260p' /Users/fan/.codex/skills/parallel-explorer-integrator/SKILL.md`
  - `git diff --check -- codex_source/00_codex_readme.md codex_source/10_codex_multi_agent_prompt_library.md codex_log/latest.md codex_log/20260407_multi_agent_prompt_library_and_skill.md`
  - `git status --short --branch`
- 验证结果：
  - 项目内模板库文件已真实存在
  - 全局 skill 文件已真实存在
  - 导航引用只改了 1 处
  - 本轮 Git 跟踪改动只落在：
    - `codex_source/00_codex_readme.md`
    - `codex_source/10_codex_multi_agent_prompt_library.md`
    - `codex_log/latest.md`
    - `codex_log/20260407_multi_agent_prompt_library_and_skill.md`
  - 全局 skill 位于仓库外：
    - 不会随当前仓库 push 到 GitHub
    - 但本机 Codex 后续可直接调用

## 当前结果

- `已确认完成`
  - 仓库内版本已落文件
  - 全局 skill 已落文件
  - skill 名称与已有 skills 无重名冲突
  - skill 与项目内版本职责分层清楚
- `已确认完成`
  - 项目内模板库已包含：
    - 文件定位
    - 适用场景
    - 为什么适合当前项目
    - 默认结构
    - 角色边界
    - 适用 / 不适用情形
    - 4 套可直接复用模板
    - 使用注意事项
    - 一句话规则
- `已确认完成`
  - 全局 skill 已包含：
    - 启用条件
    - 为什么默认是 `2 explorers + 1 integrator`
    - explorer / integrator 边界
    - 典型任务分类
    - 标准化 prompt skeleton
- `已确认`
  - 全局 skill 属于本机环境结果，不属于当前仓库 Git 跟踪内容

## 下一步建议

- 以后在《视频工厂》里要发起多 agent 任务时：
  - 若任务明显偏项目内执行，优先从 `codex_source/10_codex_multi_agent_prompt_library.md` 复制模板
  - 若任务偏跨项目通用，用全局 skill `parallel-explorer-integrator`
- 当前仓库状态分类：
  - `pr_open_not_merged_to_reading_branch`
- 当前 draft PR 仍是长分支 PR：
  - `https://github.com/fthytwerwt-sudo/-/pull/3`
  - 它不等于“只含本轮文档改动”的净 PR
