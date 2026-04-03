# 2026-04-04 90 分过线后样片交付规则固化

## 本轮目标

- 把“达到项目内部 90 分水位 / `quality_passed` / 可发布测试线后，必须给用户一个可见样片”写成仓库正式硬规则。

## 执行前已确认事实

- 当前默认主读取分支固定为：
  - `codex/user-readable-map`
- 当前仓库已经明确：
  - demo 只是运行锚点，不是质量样片
  - “抖音 90 分标准”是项目内部质量简称，不是平台官方评分
  - `dist/formal_api_demo/` 属于 `.gitignore` / `local_only`
- 当前缺口是：
  - 即使仓库里写了 `quality_passed`
  - 用户也不一定能立刻知道该看哪个样片文件

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/13_stage_and_acceptance_gates.md`（缺失）
- `project_source/14_content_review_and_loop_governance_rules.md`（缺失）
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`

## 实际改动

- 修改：
  - [project_source/08_quality_baseline_and_90_score_rules.md](/Users/fan/Documents/视频工厂/project_source/08_quality_baseline_and_90_score_rules.md)
  - [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
  - [codex_source/01_execution_rules.md](/Users/fan/Documents/视频工厂/codex_source/01_execution_rules.md)
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
- 新增：
  - [project_source/13_stage_and_acceptance_gates.md](/Users/fan/Documents/视频工厂/project_source/13_stage_and_acceptance_gates.md)
  - [project_source/14_content_review_and_loop_governance_rules.md](/Users/fan/Documents/视频工厂/project_source/14_content_review_and_loop_governance_rules.md)
  - [codex_log/20260404_quality_pass_sample_delivery_rules.md](/Users/fan/Documents/视频工厂/codex_log/20260404_quality_pass_sample_delivery_rules.md)

## 新增 / 改写的硬规则

- 只要达到以下任一条件，必须交付可见样片：
  - 90 分水位通过
  - `quality_passed`
  - 可发布测试线通过
- 可见样片不能只靠一句“已过线”，必须至少交付：
  - 样片文件路径
  - 或回审帧集合
  - 或验收样片目录
- 当前默认样片交付物优先写死为：
  - `dist/formal_api_demo/final.mp4`
  - 如需辅助验收，再补：
    - `dist/formal_api_demo/review_frames/`
- 若样片属于 `.gitignore` / `local_only`，必须同时说明：
  - 不会上 GitHub
  - 本地已生成
  - 用户应看哪个本地路径
  - 它是否足以完成当前验收
- 明确禁止：
  - “质量已过线”但不给样片路径
  - “已经 90 分了”但用户看不到任何样片
  - “本地有成片”但不告诉用户在哪
  - “GitHub 上看不到是正常的”却不补交付方式

## 实际执行

- 读取并核对：
  - `AGENTS.md`
  - `codex_log/latest.md`
  - `project_source/08_quality_baseline_and_90_score_rules.md`
  - `codex_source/01_execution_rules.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/08_branch_sync_and_reading_branch_rules.md`
- 确认缺失文件：
  - `project_source/13_stage_and_acceptance_gates.md`
  - `project_source/14_content_review_and_loop_governance_rules.md`
- 文本规则校验：
  - `git diff --check ...`

## 当前结果

- 当前仓库里已经存在正式规则：
  - 达到 90 分 / `quality_passed` / 可发布测试线时，必须交付可见样片
- 当前默认样片交付物已写死为：
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/review_frames/`

## 下一步建议

- 后续凡是收尾写 `quality_passed`，都必须连同：
  - 样片路径
  - `local_only`
  - 用户优先查看文件
  一起回报，不能只给结论。
