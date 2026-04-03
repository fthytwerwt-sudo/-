# Latest

## 当前仓库规则状态

- 2026-04-04 本轮修的是“90 分 / `quality_passed` / 可发布测试线通过后，必须给用户可见样片”的硬规则。
- 当前默认主读取分支仍是：
  - `codex/user-readable-map`

## 本轮新增 / 改写的正式样片交付规则

- 当本轮达到以下任一条件时，必须向用户交付可见样片：
  - 项目内部 90 分水位通过
  - `quality_passed`
  - 通过可发布测试线
- 这里的“可见样片”不能只写一句“已过线”，必须至少给出：
  - 样片文件路径
  - 或可直接打开的样片文件
  - 或固定回审帧集合
  - 或明确的验收样片目录
- 当前默认样片交付物优先写死为：
  - `dist/formal_api_demo/final.mp4`
  - 如需辅助验收，再补：
    - `dist/formal_api_demo/review_frames/`
- 若样片属于 `.gitignore` / `local_only`，必须同时说明：
  - 不会上传到 GitHub
  - 但本地已生成
  - 用户当前应优先看哪一个本地路径
  - 它是否足以完成当前验收

## 当前禁止偷换

- “质量已过线”但不给样片路径
- “已经 90 分了”但用户看不到任何样片
- “本地有成片”但不告诉用户在哪
- “GitHub 上看不到是正常的”却不补交付方式

## 本轮实际修改文件

- [project_source/08_quality_baseline_and_90_score_rules.md](/Users/fan/Documents/视频工厂/project_source/08_quality_baseline_and_90_score_rules.md)
- [project_source/13_stage_and_acceptance_gates.md](/Users/fan/Documents/视频工厂/project_source/13_stage_and_acceptance_gates.md)
- [project_source/14_content_review_and_loop_governance_rules.md](/Users/fan/Documents/视频工厂/project_source/14_content_review_and_loop_governance_rules.md)
- [AGENTS.md](/Users/fan/Documents/视频工厂/AGENTS.md)
- [codex_source/01_execution_rules.md](/Users/fan/Documents/视频工厂/codex_source/01_execution_rules.md)
- [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)

## 当前默认样片交付物

- 主样片：
  - `dist/formal_api_demo/final.mp4`
- 辅助验收：
  - `dist/formal_api_demo/review_frames/`

## 当前最关键下一步

- 后续凡是写 `quality_passed` / 90 分 / 可发布测试线通过，都必须在收尾里同时回报：
  - 样片路径
  - `local_only` 与否
  - 用户应优先看的样片文件
  - 若 GitHub 不可见，则本地路径

## 新会话建议先读

- `AGENTS.md`
- `project_source/08_quality_baseline_and_90_score_rules.md`
- `project_source/13_stage_and_acceptance_gates.md`
- `project_source/14_content_review_and_loop_governance_rules.md`
- `codex_source/01_execution_rules.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
