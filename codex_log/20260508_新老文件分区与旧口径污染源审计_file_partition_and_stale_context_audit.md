# 20260508｜新老文件分区与旧口径污染源审计

## 本轮定位

- `已确认` 本轮只做《视频工厂》唯一正式工作区的只读审计，不做任何清理动作。
- `已确认` 审计目标是查清：当前正式区、历史区、静态协作包、原始素材区、旧口径污染源、下一轮清理优先级与阻断条件。
- `已确认` 本轮执行车道为 `audit_lane`，并发结构为 `serial_only`；写入范围仅限审计报告、执行日志和 `codex_log/latest.md` 最小摘要。

## route_decision 摘要

- `project_route = video_factory`
- `task_type = local_file_governance + review_diagnosis_audit + mechanism_or_route_fix + project_file_change`
- `large_task_gate.triggered = true`
- `lane_recommendation = audit_lane`
- `parallel_recommendation = serial_only`
- `execution_permission = granted_for_read_only_audit_and_report_writeback`

## 工作区状态

- `已确认` 当前路径：`/Users/fan/Documents/视频工厂`
- `已确认` 当前分支：`codex/user-readable-map`
- `已确认` 当前 `git status --short` 仅有 1 个未跟踪文件：`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`
- `已确认` Documents 顶层只剩唯一正式工作区：`/Users/fan/Documents/视频工厂`
- `部分成立` `~/.config/superpowers/worktrees/视频工厂` 仍残留 `.DS_Store`
- `已确认` 体积：工作区 `34G`，`.git` `21G`，`素材录制/` `11G`，`dist/` `1.3G`

## 关键审计结论

### 已确认的当前核心区

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/current_local_artifact_paths.md`
- `GPT数据源/` 当前 10 份执行包
- `review_loop/`
- `dist/latest_review_pack/`
- 当前代码 / 脚本执行层：`formal_api_demo_core.py`、`formal_api_demo_cloud_assembly.py`、`scripts/`、`tests/`、`compose.yaml`、`config/`、`工作台模板/`

### 已确认的高风险污染源

1. `执行日志_codex_log/最新摘要_latest.md`
   - 内容仍写直播前台项目旧入口，但 `AGENTS.md` 默认执行规则还提到它。
2. `project_source/07_current_formal_facts.md`
   - 仍写 2026-04-12 历史样片“通过 / 可直接发送”，且 `project_source/00/01/06` 还在引用它。
3. `codex_source/02_codex_index.md`、`00_current_repo_audit.md`、`07_formal_api_demo_target_plan.md`
   - 仍保留启动期 / demo 时代导航，容易把仓库误解成最小 demo。
4. `dist/latest_review_pack/` 同目录双状态并存
   - 当前 `review_manifest.md` / `summary.json` 已是 v3.1 灰测口径。
   - 但并排的 `AI做PPT踩坑_成品候选_v31_review_manifest.md` / `_summary.json` 仍是灰测前旧候选口径。
   - 同目录还保留 `AI做PPT踩坑_成品候选_v3_*` 历史副本。
5. root demo 入口仍显眼
   - `README.md`、`cases/demo.md`、`generate_demo.py`、`video_builder.swift`、`package.json` 仍突出 `demo / video-demo` 语义。

### 已确认的区位正确对象

- `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`
- `review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `review_loop/10_文案结构改版包模板_copy_revision_package_template.md`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/`
- `review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/V002_复盘到文案调整桥接_review_to_copy_revision_bridge.md`

## 产出物

- `治理报告`：`治理_reports/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit/新老文件分区与旧口径污染源审计报告_file_partition_and_stale_context_audit_report.md`

## 禁止项回查

- `已确认` 未删除 / 未移动 / 未重命名任何文件。
- `已确认` 未修改 `dist/latest_review_pack/`、`current_publish_target`、`content_validation`、`send_ready`。
- `已确认` 未修改 `GPT 数据源/` 与 `GPT数据源/` 当前 10 份执行包。
- `已确认` 未新建外部工作区。

## 下一个目标

先做“入口级旧口径降权”，把 `执行日志_codex_log/`、`project_source/07_current_formal_facts.md` 引用链、`codex_source` 旧导航、`dist/latest_review_pack/` 同目录双状态文件这些污染源从默认读取路径里切出去，再决定后续归档或删除候选。
