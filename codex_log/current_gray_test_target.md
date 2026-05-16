# 当前灰度测试目标 current_gray_test_target

## legacy compatibility pointer

`已确认` 本文件已在 2026-05-15 从当前 canonical 入口降级为 `legacy_compatibility_pointer（历史兼容指针）`。

当前正式入口已迁移到：

- `codex_log/current_operation_target.md`

当前项目阶段已迁移为：

- `formal_operation_active（正式运营中）`
- `data_driven_operation_iteration（数据驱动运营迭代）`
- `operation_data_intake（运营数据录入）`
- `operation_review（运营复盘）`
- `operation_next_variable_decision（运营下一变量判断）`

## why this file remains

本文件不删除，原因是旧日志、旧记录目录、GPT Project 静态包、`review_loop/` 历史模板仍可能引用 `current_gray_test_target.md`。

从本轮开始：

- `gray_test` 只作为 `legacy_previous_term（历史前置术语）`。
- 旧路径只作为 `historical_path / legacy_alias`。
- 后续新数据截图 / 评论 / 私信 / 咨询默认不再走 `gray_test_data_intake`，而走 `operation_data_intake`。

## legacy summary

```yaml
legacy_current_gray_test_target:
  status: "legacy_compatibility_pointer"
  canonical_replacement: "codex_log/current_operation_target.md"
  previous_term: "gray_test"
  current_project_stage: "formal_operation_active"
  current_operation_target: "V003"
  operation_records_index: "review_loop/operation_records_index.md"
  current_data_goal_anchor: "codex_log/current_data_goal_anchor.md"
```

## operation target summary

| video_id | role_now | legacy_note |
| --- | --- | --- |
| V001 | `historical_operation_record` | 原 v3.1 灰度观察对象，历史字段保留 |
| V002 | `policy_limited_abnormal_operation_sample` | 平台审核减推异常样本，不作为正常分发样本 |
| V003 | `current_operation_target` | 当前最新运营样本，已录入 `interim_36h_snapshot` 与 `interim_65h_snapshot`；仍非 72h final |

## forbidden status boundary

- 正式运营不等于内容成功。
- 正式运营不等于商业验证成立。
- 正式运营不等于当前视频内容通过。
- 正式运营不等于数据飞轮已经跑通。
- 正式运营不等于 multi-agent runtime 长期稳定。
- 正式运营不等于当前数据目标锚点 ready。
- 旧 `gray_test_published / post_publish_gray_test / gray_testing_not_final_passed` 只保留为历史兼容字段，不再作为当前 canonical 状态。

## next target

后续读取本文件时，必须跳转到 `codex_log/current_operation_target.md`；只有在追溯 2026-05-15 以前的历史灰度记录时，才按 legacy 语义读取本文件。
