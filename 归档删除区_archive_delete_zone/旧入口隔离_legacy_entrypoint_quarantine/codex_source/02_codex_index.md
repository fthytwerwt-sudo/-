# codex_source 导航

## 当前定位

当前仓库里已经存在 `codex_source/`，但它仍处于启动期。

这个目录现在主要承担两类工作：

- 把当前仓库真实状态说清楚
- 把缺失文件与下一步顺序说清楚

它还没有形成完整的 Codex 执行规则体系。

## 本轮重点文件分别干什么

### `codex_source/00_current_repo_audit.md`

- 用途：记录当前仓库真实存在的关键文件、代码链路、产物和最小闭环
- 适合在想先判断“现在仓库到底到哪一步了”时先看

### `codex_source/01_missing_files_and_next_steps.md`

- 用途：列出当前缺失的 `project_source` / `codex_source` 文件，并给出下一轮最合理的建档顺序
- 适合在想判断“下一轮先补什么”时先看

## 当前仓库里还存在的其他 codex 文件

### `codex_source/01_codex_source_plan.md`

- 这是当前仓库里已经存在的早期规划文件
- 可以作为补充参考
- 但本轮最直接相关的规划文件，已经改为 `01_missing_files_and_next_steps.md`

## 当前还没建哪些关键文件

### 缺失的 project_source 文件

- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/02_scene_mode_templates.md`
- `project_source/03_perplexity_prompt_library.md`
- `project_source/04_review_templates.md`
- `project_source/05_psychology_execution_rules.md`
- `project_source/06_project_index.md`

### 缺失的 codex_source 文件

- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_codex_task_templates.md`
- `codex_source/03_skill_integration_rules.md`
- `codex_source/04_delivery_and_report_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`

## 后续 Codex 应该先看什么，再看什么

### 如果任务是“先理解当前仓库”

建议顺序：

1. `AGENTS.md`
2. `codex_source/02_codex_index.md`
3. `codex_source/00_current_repo_audit.md`
4. `README.md`
5. `cases/demo.md`
6. `generate_demo.py`
7. `video_builder.swift`
8. `tests/test_generate_demo.py`

### 如果任务是“继续补文档层”

建议顺序：

1. `AGENTS.md`
2. `codex_source/02_codex_index.md`
3. `codex_source/01_missing_files_and_next_steps.md`
4. `codex_source/00_current_repo_audit.md`

然后再决定要补的是：

- `project_source/*`
- 还是 `codex_source/*`

### 如果任务是“开始接代码链路”

建议顺序：

1. `AGENTS.md`
2. `codex_source/00_current_repo_audit.md`
3. `README.md`
4. `cases/demo.md`
5. `generate_demo.py`
6. `video_builder.swift`
7. `tests/test_generate_demo.py`

## 当前阶段的短结论

当前 `codex_source/` 已经能回答两件关键事：

1. 这个仓库当前真实有什么
2. 它还缺什么、下一轮该先补什么

但它还不能替代完整的执行规则层。

所以后续最合理的动作不是继续扩散写很多模板，而是先把：

- 项目脑入口
- Codex 入口
- Codex 执行边界

这几层补起来。
