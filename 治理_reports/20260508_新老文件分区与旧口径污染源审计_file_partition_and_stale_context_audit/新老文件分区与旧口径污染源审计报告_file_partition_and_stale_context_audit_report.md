# 新老文件分区与旧口径污染源审计报告 file_partition_and_stale_context_audit_report

## 1. 审计定位

- `审计日期`：`2026-05-08 CST`
- `审计范围`：`/Users/fan/Documents/视频工厂`
- `审计方式`：只读审计 + 报告落库
- `已确认` 本轮未删除、未移动、未重命名、未覆盖、未清空、未归档任何既有文件。
- `已确认` 本轮未修改 `dist/latest_review_pack/`、`codex_log/current_publish_target.md`、`content_validation`、`send_ready`、`GPT 数据源/`、`GPT数据源/` 当前 10 份执行包。

## 2. route_decision（路由判断）

```text
route_decision:
  project_route: video_factory
  task_type:
    - local_file_governance
    - review_diagnosis_audit
    - mechanism_or_route_fix
    - project_file_change
  responsibility_layer:
    - entry_routing_layer
    - execution_layer
    - validation_layer
    - sync_layer
    - mechanism_fix_layer
  large_task_gate:
    triggered: true
    reason:
      - 本轮同时涉及一级目录分区、旧口径风险识别、路径索引核查、latest_review_pack 指针核查、治理报告与执行日志落库
      - 本轮检查文件数明显超过 3 个，且同时横跨规则文件、日志文件、报告文件、路径索引文件
      - 本轮慢点在审计判断，不在运行时执行
    lane_recommendation: audit_lane
    lane_reason: 当前目标是查清正式区/历史区/污染源，不是直接清理；必须先分层标记已确认、部分成立、待验证
    lane_invalid_if:
      - 需要直接删改文件才能继续
      - 需要把历史镜像写成当前事实
      - 需要修改冻结目录才能得出结论
    parallel_recommendation: serial_only
    parallel_reason: 这轮需要单点整合同一份审计结论，且后续只允许单点写报告/日志/latest 摘要
    parallel_invalid_if:
      - 多 lane 同时写同一份治理报告或 latest 摘要
      - 子任务对同一批口径文件做并发改写
    write_owner: current_codex_session
    read_only_lanes:
      - workspace_scan
      - pointer_check
      - stale_context_audit
    integration_owner: current_codex_session
  allowed_changes:
    - 治理_reports/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit/
    - codex_log/20260508_新老文件分区与旧口径污染源审计_file_partition_and_stale_context_audit.md
    - codex_log/latest.md（仅允许新增审计完成摘要，不改当前 v3.1 状态）
  forbidden_changes:
    - 任何删除、移动、重命名、覆盖、清空、压缩、归档动作
    - dist/latest_review_pack/
    - codex_log/current_publish_target.md
    - content_validation
    - send_ready
    - GPT 数据源/
    - GPT数据源/ 当前 10 份执行包
    - 新建外部工作区 / fresh clone / audit clone / clean clone / git worktree add
    - git gc / git prune / git repack / git lfs migrate / filter-repo / filter-branch / BFG / force push
  blocked_if:
    - 不在唯一正式工作区
    - 当前分支不是 codex/user-readable-map 且无法安全切换
    - 关键必读文件缺失或无法读取
    - 需要靠删改文件才能完成审计
    - 需要修改冻结目录或 live 状态字段才能得出结论
    - 无法 push 到 codex/user-readable-map
  execution_permission: granted_for_read_only_audit_and_report_writeback
```

## 3. read_status（读取状态）

| path | reason | read_status |
| --- | --- | --- |
| `AGENTS.md` | 仓库入口规则与《视频工厂》路由闸门 | `read_ok` |
| `codex_source/00_codex_readme.md` | Codex 执行层总入口 | `read_ok` |
| `codex_source/01_execution_rules.md` | 执行规则与 route_decision 模板 | `read_ok` |
| `codex_log/latest.md` | 最新摘要与新会话默认事实入口 | `read_ok` |
| `codex_log/current_local_artifact_paths.md` | 当前本地产物路径索引与外部路径降权清单 | `read_ok` |
| `review_loop/00_review_loop_readme.md` | 发布后复盘执行层总说明 | `read_ok` |
| `review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md` | bridge 入口是否已入正确区位 | `read_ok` |
| `review_loop/10_文案结构改版包模板_copy_revision_package_template.md` | bridge 模板是否已入正确区位 | `read_ok` |
| `GPT数据源/00_项目总述.md` | 当前动态事实包总述 | `read_ok` |
| `GPT数据源/03_总索引与阅读顺序.md` | 当前动态事实包读取顺序 | `read_ok` |
| `GPT数据源/08_当前正式事实.md` | 当前正式事实 | `read_ok` |
| `GPT数据源/04_选题与文案规则.md` | 动态文案规则包 | `read_ok` |
| `GPT数据源/05_文案路由规则.md` | 动态文案路由包 | `read_ok` |
| `project_source/14_content_review_and_loop_governance_rules.md` | 复盘治理规则 | `read_ok` |
| `codex_source/13_execution_lane_and_parallel_rules.md` | large_task_gate 触发后的 lane / parallel 规则 | `read_ok` |
| `project_source/20_codex_multi_agent_routing_note_for_gpt_project.md` | large_task_gate 触发后的 GPT 侧并发说明 | `read_ok` |

## 4. workspace_status（工作区状态）

| item | result | status |
| --- | --- | --- |
| `pwd` | `/Users/fan/Documents/视频工厂` | `已确认` |
| `git branch --show-current` | `codex/user-readable-map` | `已确认` |
| `git status --short` | 仅有 `?? GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | `已确认` |
| `git remote -v` | `origin https://github.com/fthytwerwt-sudo/-.git` | `已确认` |
| Documents 顶层 `find /Users/fan/Documents -maxdepth 1 -name '视频工厂*'` | 只剩 `/Users/fan/Documents/视频工厂` | `已确认` |
| 额外外部 worktree 线索 | `/Users/fan/.config/superpowers/worktrees/视频工厂` 仅剩 `.DS_Store` | `部分成立` |
| 工作区体积 | `34G` | `已确认` |
| `.git` 体积 | `21G` | `已确认` |
| `素材录制/` 体积 | `11G` | `已确认` |
| `dist/` 体积 | `1.3G` | `已确认` |
| `review_loop/` 体积 | `164K` | `已确认` |
| `GPT数据源/` 体积 | `100K` | `已确认` |
| `GPT 数据源/` 体积 | `92K` | `已确认` |

## 5. 一级目录分区结论

### 5.1 current_core（当前核心区）

- `AGENTS.md`
- `codex_source/`
- `codex_log/`
- `GPT数据源/`
- `review_loop/`
- `dist/latest_review_pack/`
- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `scripts/`
- `tests/`
- `compose.yaml`
- `config/`
- `工作台模板/`

### 5.2 gpt_project_static_pack（GPT Project 静态协作包）

- `GPT 数据源/`

### 5.3 archive_or_history（归档 / 历史区）

- `归档_archive/`
- `本地归档_local_archive/`
- `project_source/`
- `复审包_review_packs/` 中非当前 v3.1 基线复审包
- `dist/` 中 `voice_trials/`、`reference_packs/`、`_guardrail_probe_*`、`_provider_rotation_*`、`20260424_不放大完整可读_no_zoom_completeness/`

### 5.4 review_and_governance（复盘 / 治理区）

- `review_loop/`
- `治理_reports/`
- `验证_reports/`
- `素材检查_reports/`
- `样片报告_sample_reports/`

### 5.5 raw_assets_or_sensitive（原始素材 / 高风险区）

- `素材录制/`
- `素材库_assets/`

### 5.6 temp_or_cache（临时 / 缓存区）

- `.DS_Store`
- 未来若重建会出现的 `node_modules/`
- `dist/` 下纯 probe / smoke / provider rotation 输出

### 5.7 unclear_or_risky（不清楚 / 有污染风险区）

- `执行日志_codex_log/`
- `README.md`
- `cases/demo.md`
- `generate_demo.py`
- `video_builder.swift`
- `package.json`
- `codex_source/00_current_repo_audit.md`
- `codex_source/02_codex_index.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `project_source/07_current_formal_facts.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_*`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md`
- `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_summary.json`

## 6. partition_map（分区地图）

| directory | category | current_status | should_codex_read_by_default | allowed_use | forbidden_use | cleanup_action_recommendation | evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `AGENTS.md` | `current_core` | 当前仓库总入口 | `yes` | 路由、边界、单工作区规则 | 不能被旧单项目口径覆盖 | `P0_do_not_touch` | `AGENTS.md` |
| `codex_source/` | `current_core` | 当前执行规则层；但内部混有旧导航文件 | `yes_with_file_filter` | 读 `00/01/13/14/15` 等当前规则文件 | 不应默认把 `02_codex_index.md`、`00_current_repo_audit.md`、`07_formal_api_demo_target_plan.md` 当现行入口 | 保留目录；下一轮做“旧执行索引降权任务” | `codex_source/00_codex_readme.md`, `codex_source/01_execution_rules.md` |
| `codex_log/` | `current_core` | 当前日志与指针层；`latest.md` 为默认入口 | `yes_with_top_section_priority` | 读 `latest.md`、`current_*` 指针 | 不应把旧 dated log 当当前事实 | 保留目录；下一轮考虑拆分 append-only 历史层 | `codex_log/latest.md`, `codex_log/current_publish_target.md` |
| `GPT数据源/` | `current_core` | 当前动态事实 / 当前 10 份执行包 | `yes` | 当前事实、项目总述、文案规则、路由 | 禁止改写为静态协作包角色 | `P0_do_not_touch` | `GPT数据源/00_项目总述.md`, `GPT数据源/08_当前正式事实.md` |
| `review_loop/` | `review_and_governance` | 发布后复盘执行层，V001/V002 已分桶 | `yes_when_task_matches` | 灰度复盘、bridge、平台风险检查 | 不应被写成正式事实源头 | `P0_do_not_touch` | `review_loop/00_review_loop_readme.md`, `review_loop/08/09/10` |
| `dist/latest_review_pack/` | `current_core` | 当前正式复审包入口；同时并存旧 v3 与旧 v31 副本 | `yes` | 当前 full/review_manifest/summary/route map 读取 | 不应修改本目录；不应把并排旧副本当当前状态 | 保留目录；下一轮只做“同目录旧副本降权 / 移位方案” | `dist/latest_review_pack/review_manifest.md`, `dist/latest_review_pack/summary.json` |
| `formal_api_demo_core.py` + `formal_api_demo_cloud_assembly.py` + `scripts/` + `tests/` + `compose.yaml` + `config/` + `工作台模板/` | `current_core` | 仍是现行代码 / 工作台执行层，但命名保留 legacy `formal_api_demo` | `yes_for_code_tasks` | 当前主线执行、工作台、测试 | 不应因命名老就直接当可删 | 保留不动；下一轮单独做“代码命名与入口说明审计” | `scripts/generate_formal_api_demo.py`, `scripts/assemble_formal_api_demo.py`, `compose.yaml` |
| `GPT 数据源/` | `gpt_project_static_pack` | GPT Project 静态协作包；含 `_backup_before_update_20260429...` 与冻结文件 `10_样片参考质量规则...` | `no` | 协作包、静态说明、读取规则 | 不得当当前动态事实库；本轮禁止修改 | `P0_do_not_touch` | `GPT 数据源/08_当前事实读取规则.md`, `git status --short` |
| `project_source/` | `archive_or_history` | 历史 / 辅助镜像层，仍保留部分旧事实文件 | `no_by_default` | 辅助判断、对照、治理历史 | 不得高于 `GPT数据源/`、`codex_log/latest.md`、`dist/latest_review_pack/` | 下一轮优先做旧事实文件降权与引用修正 | `AGENTS.md`, `project_source/06_project_index.md`, `project_source/07_current_formal_facts.md` |
| `复审包_review_packs/` | `archive_or_history` | 当前 v3.1 基线复审包 + 历史 reference 包 | `yes_for_local_artifact_validation_only` | 本地路径核实、reference whitelist 读取 | 不得把历史包写成当前状态 | 保留；分“当前基线包 / reference 包 / 历史候选包”三层治理 | `codex_log/current_local_artifact_paths.md` |
| `归档_archive/` | `archive_or_history` | 已归档旧口径，README 明确默认不读 | `no` | 复盘、证据追溯 | 不得回流成当前事实入口 | `P2_safe_to_archive_candidate` 保持原位，禁止默认读取 | `归档_archive/旧口径_old_context_20260502/README_归档说明_archive_readme.md` |
| `本地归档_local_archive/` | `archive_or_history` | 已回收外部工作区；内部仍含嵌套 `.git` 的 fresh clone 存档 | `no` | 只作历史证据保留 | 不得作为执行工作区或默认路径 | 下一轮先做“嵌套 repo 存档去活化策略”评审 | `本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260504/` |
| `治理_reports/` | `review_and_governance` | 治理审计报告集中区 | `yes_when_governance_task_matches` | 治理报告、审计历史 | 不应被当成当前事实总入口 | `P0_do_not_touch` | 目录现状 |
| `验证_reports/` | `review_and_governance` | 技术验证报告区 | `no_by_default` | 技术验证追溯 | 不应被写成内容通过 | `P2_safe_to_archive_candidate` | `验证_reports/20260503_阿里云剪辑复接验证...` |
| `素材检查_reports/` | `review_and_governance` | 素材检查和节奏提取报告 | `no_by_default` | 写稿辅助、素材节奏追溯 | 不应被当成当前发布状态 | `P2_safe_to_archive_candidate` | `素材检查_reports/20260429_文案样本节奏提取...` |
| `素材录制/` | `raw_assets_or_sensitive` | 11G 用户原始录制素材 | `no_by_default` | 素材核实、补录判断、证据来源 | 不能默认清理、外置、删除 | `P1_needs_user_confirmation` | `du -sh 素材录制`, 目录扫描 |
| `素材库_assets/` | `raw_assets_or_sensitive` | 当前固定素材锚点所在目录 | `yes_when_reference_needed` | 固定素材锚点读取 | 不得误删或误归档 | `P0_do_not_touch` | `codex_log/current_local_artifact_paths.md` |
| `dist/` 其余子目录 | `archive_or_history` | 同时含 probe、reference、voice trials、完整成片历史目录 | `no_by_default` | 历史验证、trial 回看 | 不得把 probe / trial 当当前 latest | 下一轮分“archive 候选”和“cache 候选”双清单 | `find dist -maxdepth 2`, `治理_reports/20260504_项目升级前旧资产清库...` |
| `README.md` + `cases/demo.md` + `generate_demo.py` + `video_builder.swift` + `package.json` | `unclear_or_risky` | root 入口仍是最小 demo 叙述；与当前项目主线不一致 | `no_for_project_routing` | 保留为 demo / legacy code entry 说明 | 不应作为新会话默认项目入口 | 下一轮做 root 入口降权或补说明 | `README.md`, `package.json`, `codex_source/00_current_repo_audit.md` |
| `执行日志_codex_log/` | `unclear_or_risky` | 仍保留直播项目旧摘要，且被 AGENTS 默认执行规则提到 | `no` | 仅作多项目历史残留证据 | 不得再被写成《视频工厂》最新摘要 | 下一轮优先修 route-level 引用 | `执行日志_codex_log/最新摘要_latest.md`, `AGENTS.md` |
| `项目资料_docs/` | `unclear_or_risky` | 多项目仓库中的直播项目 sibling 区 | `no_when_video_factory_route` | 仅在命中直播项目时读取 | 不得被《视频工厂》任务默认继承 | 保留不动；通过路由规则隔离 | `AGENTS.md` |

## 7. current_core_files（当前核心区）

### 7.1 当前正式主线与默认入口

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/current_local_artifact_paths.md`
- `GPT数据源/00_项目总述.md`
- `GPT数据源/03_总索引与阅读顺序.md`
- `GPT数据源/08_当前正式事实.md`
- `review_loop/00_review_loop_readme.md`
- `review_loop/08_发布前平台风险检查_pre_publish_platform_risk_check.md`
- `review_loop/09_复盘到文案调整桥接_review_to_copy_revision_bridge.md`
- `review_loop/10_文案结构改版包模板_copy_revision_package_template.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/visual_route_map.json`

### 7.2 当前代码 / 脚本入口（已确认存在）

- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `compose.yaml`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `工作台模板/`
- `tests/test_formal_api_demo_pipeline.py`
- `tests/test_formal_mainline_route.py`

`部分成立` 这些代码 / 脚本入口仍服务当前执行层，但其命名继承了早期 `formal_api_demo` 时代，不应再被当成“root demo = 当前项目入口”。

## 8. archived_or_legacy_files（归档 / 历史区）

- `归档_archive/旧口径_old_context_20260502/*`
- `本地归档_local_archive/外部工作区回收_external_workspace_recovery_20260504/视频工厂_fresh_clone_audit_20260504/`
- `project_source/*` 整体
- `复审包_review_packs/20260430_可爱风格卡片页参考核查_cute_card_reference_audit/`
- `复审包_review_packs/20260430_骚萌卡历史样本复审_sassy_card_reference_review/`
- `dist/_guardrail_probe_20260408/`
- `dist/_provider_rotation_probe/`
- `dist/_provider_rotation_realcheck/`
- `dist/20260424_不放大完整可读_no_zoom_completeness/`
- `dist/reference_packs/`
- `dist/voice_trials/`
- `dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/`

## 9. risky_unclear_files（不清楚 / 有污染风险区）

| path | risk_summary | status |
| --- | --- | --- |
| `执行日志_codex_log/最新摘要_latest.md` | 内容仍写“AI 直播前台验证项目”默认入口；与《视频工厂》当前入口冲突 | `已确认` |
| `AGENTS.md` 中对 `执行日志_codex_log/最新摘要_latest.md` 的默认更新要求 | 会把新会话带向错误摘要文件 | `已确认` |
| `project_source/07_current_formal_facts.md` | 仍写 2026-04-12 历史样片“通过 / 可直接发送”，与当前 v3.1 灰测状态冲突 | `已确认` |
| `project_source/00_project_brief.md`、`01_project_system_prompt.md`、`06_project_index.md` | 仍把 `project_source/07_current_formal_facts.md` 作为正式事实入口 | `已确认` |
| `codex_source/02_codex_index.md`、`00_current_repo_audit.md` | 启动期旧导航，仍把 README/demo 当默认接手入口 | `已确认` |
| `codex_source/07_formal_api_demo_target_plan.md` | legacy 目标态文件，仍在大量旧 dated log 中被引用 | `已确认` |
| `README.md`、`cases/demo.md`、`generate_demo.py`、`video_builder.swift`、`package.json` | root 命名仍突出 demo，容易让无上下文执行器误判仓库身份 | `已确认` |
| `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_*` | 与当前 latest 同目录并存，且仍是 tracked 文件 | `已确认` |
| `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md`、`AI做PPT踩坑_成品候选_v31_summary.json` | 同目录内仍保留灰测前旧候选口径，和 `review_manifest.md` / `summary.json` 不一致 | `已确认` |
| `codex_log/latest.md` 历史段落 | append-only 文件内仍含 `/private/tmp`、旧 worktree、round34 旧状态，可被 grep 命中 | `部分成立` |

## 10. stale_context_risks（旧口径污染风险清单）

| risk_id | stale_source | possible_wrong_behavior | affected_task_type | current_guardrail | missing_guardrail | recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| `R001` | `执行日志_codex_log/最新摘要_latest.md` | 新会话把直播项目旧摘要当《视频工厂》默认摘要 | `mechanism_or_route_fix`, `project_file_change`, `copywriting` | `AGENTS.md` 多项目路由规则已改回《视频工厂》 | `AGENTS.md` 默认执行规则仍引用该旧摘要 | 下一轮先修 `AGENTS.md` 与默认日志写回指向 |
| `R002` | `project_source/07_current_formal_facts.md` | 把 2026-04-12 历史过线样片误读成当前正式状态 | `review_diagnosis_audit`, `video_sample_or_assembly`, `copywriting` | `GPT数据源/08_当前正式事实.md` 已明确 v3.1 灰测状态 | `project_source` 仍保留旧事实文件且被多处索引引用 | 下一轮先降权 / 改名 / 改引用，不直接删 |
| `R003` | `project_source/00/01/06` 对 `07_current_formal_facts.md` 的引用 | 旧镜像链把 stale facts 继续包装成默认项目脑 | `mechanism_or_route_fix`, `external_research_bridge` | `AGENTS.md` 已写 `project_source/` 不高于 `GPT数据源/` | 缺少 project_source 内部“旧事实已降权”显式说明 | 下一轮做 project_source 引用修正包 |
| `R004` | `codex_source/02_codex_index.md`, `00_current_repo_audit.md`, `07_formal_api_demo_target_plan.md` | 把仓库误当“最小 demo / formal_api_demo 仓库”而不是当前《视频工厂》执行层 | `code_debug`, `project_file_change`, `local_file_governance` | `codex_source/00_codex_readme.md` 已建立新入口 | 旧导航文件仍位于同一 current_core 目录且无降权标识 | 下一轮做 codex_source 旧导航降权包 |
| `R005` | `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_*` | 读同目录文件名时误拿 v3 历史候选做当前状态 | `video_sample_or_assembly`, `review_diagnosis_audit` | `review_manifest.md` / `summary.json` 已指向 v3.1 | 同目录并存历史文件，缺少“legacy_copy_do_not_read”层 | 下一轮只做同目录旧副本清单与迁移方案 |
| `R006` | `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md` 与 `_summary.json` | 拿灰测前旧候选口径替代当前 gray test 口径 | `review_diagnosis_audit`, `mechanism_or_route_fix` | `dist/latest_review_pack/review_manifest.md` / `summary.json` 已更新灰测状态 | 同目录双状态文件缺少显式降权说明 | 下一轮先补“current alias vs legacy snapshot”边界 |
| `R007` | `README.md`, `cases/demo.md`, `generate_demo.py`, `video_builder.swift`, `package.json` | 无上下文执行器从 root README 误判仓库仍是 15 秒 demo 项目 | `code_debug`, `local_file_governance`, `external_research_bridge` | `AGENTS.md` 已接管真实项目路由 | root README / package name 仍是 demo 语义 | 下一轮单独评估 root 入口说明修正 |
| `R008` | `codex_log/latest.md` 历史 append 段落 | grep 旧 round34、外部 worktree、`/private/tmp` 路径时产生“旧状态仍在当前”错觉 | `review_diagnosis_audit`, `local_file_governance` | `latest.md` 顶部新摘要已经同步最新治理结论 | 缺少历史段落归档切分或显式“仅历史”分隔层 | 下一轮考虑 latest 历史归档拆分方案 |
| `R009` | `本地归档_local_archive/.../视频工厂_fresh_clone_audit_20260504/.git` | 后续扫描时把 archive 内嵌 repo 当可执行工作区 | `local_file_governance` | `.gitignore` 已忽略 `本地归档_local_archive/` | 缺少 archive 内“不可执行 repo”显式标识 | 下一轮只做 archive 标识和使用边界补丁 |
| `R010` | `GPT 数据源/` 与 `_backup_before_update_20260429...` | 把静态协作包或备份误读成当前动态事实 | `mechanism_or_route_fix`, `copywriting` | `GPT 数据源/08_当前事实读取规则.md` 已写 GitHub 当前文件优先 | 缺少更醒目的“静态协作包 / frozen”头部说明 | 下一轮可补静态包头部防误读提示 |

## 11. cleanup_priority_table（清理优先级表）

### 11.1 `P0_do_not_touch（绝对不动）`

| path_group | reason | status |
| --- | --- | --- |
| `AGENTS.md`, `codex_source/00_codex_readme.md`, `codex_source/01_execution_rules.md` | 当前正式入口与执行闸门 | `已确认` |
| `codex_log/latest.md`, `codex_log/current_publish_target.md`, `codex_log/current_publish_target_light_evidence.md`, `codex_log/current_local_artifact_paths.md` | 当前日志与状态指针 | `已确认` |
| `GPT数据源/` 当前 10 份执行包 | 当前动态事实包 | `已确认` |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | frozen / untracked 静态协作包文件 | `已确认` |
| `review_loop/` | 当前复盘执行层 | `已确认` |
| `dist/latest_review_pack/` | 当前正式复审包入口 | `已确认` |
| `素材录制/`, `素材库_assets/` 当前锚点 | 用户原始素材 / 当前固定素材锚点 | `已确认` |

### 11.2 `P1_needs_user_confirmation（需要用户确认）`

| path_group | reason | status |
| --- | --- | --- |
| `素材录制/` 全量目录 | 11G 原始素材，证据价值未逐项核完 | `已确认` |
| `dist/完整成片_full_videos/` | 大体积成片历史产物，可能仍有证据价值 | `部分成立` |
| `复审包_review_packs/` 中非当前基线但含 reference 的媒体文件 | 既是历史又可能仍被 reference whitelist 依赖 | `部分成立` |
| `本地归档_local_archive/` 内嵌 fresh clone | 已归档但是否继续保留需要用户确认 | `部分成立` |

### 11.3 `P2_safe_to_archive_candidate（可归档候选）`

| path_group | reason | evidence_level |
| --- | --- | --- |
| `project_source/07_current_formal_facts.md` 及其引用链 | 已确认与当前动态事实冲突，但仍被索引引用 | `high` |
| `执行日志_codex_log/` | 已确认为直播项目旧摘要残留 | `high` |
| `codex_source/02_codex_index.md`, `00_current_repo_audit.md`, `07_formal_api_demo_target_plan.md` | 已确认为旧启动期 / demo 入口文档 | `high` |
| `dist/latest_review_pack/AI做PPT踩坑_成品候选_v3_*` | 已确认是历史 v3 副本，和当前 latest 同目录并存 | `high` |
| `dist/latest_review_pack/AI做PPT踩坑_成品候选_v31_review_manifest.md` 与 `_summary.json` | 已确认是灰测前旧候选副本 | `high` |
| `dist/_guardrail_probe_*`, `dist/_provider_rotation_*`, `dist/20260424_不放大完整可读_no_zoom_completeness/`, `dist/reference_packs/`, `dist/voice_trials/` | 当前未发现默认入口引用，但仍可能保留复盘价值 | `medium` |

### 11.4 `P3_safe_to_delete_candidate_after_confirm（确认后可删候选）`

| path_group | reason | evidence_level |
| --- | --- | --- |
| `.DS_Store` | Finder 元数据，可重建 | `high` |
| 未来若重建的 `node_modules/` | 依赖缓存，可重装 | `high` |
| 明确无引用的临时 probe 缓存副产物 | 需在下一轮对照引用后逐项确认 | `low_to_medium` |

## 12. recommended_next_cleanup_tasks（下一轮清理任务建议）

### 任务 A：旧口径文件降权 / 归档入口确认

- 目标：修 `AGENTS.md`、`codex_source/00_codex_readme.md`、`project_source/*`、`执行日志_codex_log/` 的错误默认入口引用。
- 范围：只动路由与说明，不碰视频状态字段。
- 阻断条件：若需要同步修改 `GPT数据源/` 当前 10 份执行包或 `dist/latest_review_pack/` 才能完成，则 blocked。

### 任务 B：旧产物 / 旧 dist 只读清单

- 目标：给 `dist/` 和 `复审包_review_packs/` 做“当前 alias / legacy snapshot / reference whitelist / temp probe”四层清单。
- 范围：只读清单，不移文件。
- 阻断条件：若无法证明某产物属于 legacy snapshot，则不得归档建议升级。

### 任务 C：`素材录制/` 原始素材用户确认

- 目标：把 `素材录制/` 分成 `must_keep / confirm_needed / externalizable_candidate`。
- 范围：只读审计 + 用户确认表。
- 阻断条件：没有用户确认，不得外置、归档或删除。

### 任务 D：缓存 / `node_modules` / `.DS_Store` 清理

- 目标：只处理真正可重建的缓存和 Finder 元数据。
- 范围：`.DS_Store`、未来重建的 `node_modules/`、无引用纯缓存。
- 阻断条件：若命中 tracked 文件或 evidence 文件，立即停止。

### 任务 E：`current_local_artifact_paths.md` 路径索引复核

- 目标：把仍写在历史说明里的外部路径、`/private/tmp` 路径与 archive 路径进一步降权。
- 范围：只修路径索引与说明文字，不改产物本体。
- 阻断条件：若需要恢复已删除历史路径才能解释索引，立即 blocked。

### 任务 F：入口规则最小修正

- 目标：最小修复会误导新会话的 root / route 入口。
- 最优先对象：
  - `AGENTS.md` 中 `执行日志_codex_log/最新摘要_latest.md`
  - `project_source/* -> project_source/07_current_formal_facts.md` 引用链
  - `codex_source/02_codex_index.md` / `00_current_repo_audit.md`
  - `README.md`
- 阻断条件：若修正会触发多项目 live_frontend 入口回退风险，先做双项目路由审计再动。

## 13. 审计结论

### 13.1 已确认

- 当前新旧文件 **没有完全分区清楚**。
- 当前正式主线已经基本收束到：`AGENTS.md + codex_source/00/01 + codex_log/latest.md + codex_log/current_* + GPT数据源/ + review_loop/ + dist/latest_review_pack/`。
- 历史归档区已经存在，但 **旧口径仍通过错误入口引用、同目录双状态文件、legacy 命名 code entry** 持续暴露。
- 风险最高的污染源不是“看起来旧的媒体文件”，而是：
  - 错误默认摘要入口
  - stale facts 仍被索引
  - `latest_review_pack` 同目录并排旧状态副本
  - root demo 入口仍挂在仓库最显眼位置

### 13.2 部分成立

- 单工作区规则在 `/Users/fan/Documents` 顶层已经基本成立，但 `~/.config/superpowers/worktrees/视频工厂` 仍残留 `.DS_Store` 线索。
- 代码执行层已经转向当前主线，但文件名仍保留 demo / `formal_api_demo` 时代惯性，容易让“只看根目录”的执行器误判。

### 13.3 待验证

- `dist/` 其余 probe / reference / voice trial 子目录中，哪些可以从“archive candidate”升级到“delete candidate”。
- `复审包_review_packs/` 中哪些 reference 包还会继续被实际执行依赖。

## 14. forbidden_changes_check（禁止项检查）

- `已确认` 未删除文件。
- `已确认` 未移动文件。
- `已确认` 未重命名文件。
- `已确认` 未清空目录。
- `已确认` 未修改 `dist/latest_review_pack/`。
- `已确认` 未修改 `codex_log/current_publish_target.md`。
- `已确认` 未修改 `content_validation`。
- `已确认` 未修改 `send_ready`。
- `已确认` 未修改 `GPT 数据源/`。
- `已确认` 未修改 `GPT数据源/` 当前 10 份执行包。
- `已确认` 未新建外部工作区。
- `已确认` 未执行 Git 高风险清理命令或 history rewrite。

## 15. 下一个目标

先把“仍会误导新会话默认接手”的入口级污染源降权或改引用，再开始任何真实清理动作；也就是先做 **任务 A + 任务 F**，把错误入口和 stale facts 链条切断，再决定哪些历史产物可以安全归档。
