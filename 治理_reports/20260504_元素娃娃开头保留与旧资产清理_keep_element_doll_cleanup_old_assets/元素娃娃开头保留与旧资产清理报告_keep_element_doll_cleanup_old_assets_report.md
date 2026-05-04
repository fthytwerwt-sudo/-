# 元素娃娃开头保留与旧资产清理报告 keep_element_doll_cleanup_old_assets_report

## 1. 本轮结论

- `current_branch`：`codex/keep-element-doll-clean-old-assets-20260504`
- `reading_branch`：`codex/user-readable-map`
- `result_status`：`cleanup_audit_and_safe_temp_cleanup_completed`
- `v31_element_doll_opening_anchor_added_to_path_index`：`true`
- `v31_element_doll_opening_preview_added_to_path_index`：`true`
- `pr46_status`：`parallel_future_flow_teaching_asset_only_not_current_reference`
- `gpt_project_static_file_status`：`frozen_do_not_touch_this_round`
- `current_publish_target_modified`：`false`
- `video_generated`：`false`
- `video_artifacts_modified`：`false`
- `content_validation_promoted`：`false`
- `send_ready_promoted`：`false`

## 2. v3.1 元素娃娃开头路径索引补充

| artifact_id（产物编号） | 中文名称 | canonical_local_path（首选本地路径） | path_exists（路径是否存在） | verified_at（验证时间） | notes（备注） |
| --- | --- | --- | --- | --- | --- |
| `v31_element_doll_opening_anchor` | v3.1 元素娃娃开头锚点 | `/Users/fan/Documents/视频工厂/素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | `true` | `2026-05-04 CST` | 只保留开头价值；不代表元素娃娃继续做全片主持；不代表元素娃娃替代录屏主体；不代表元素娃娃替代真人判断段。 |
| `v31_element_doll_opening_preview` | v3.1 元素娃娃开头预览 | `/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | `true` | `2026-05-04 CST` | 只保留开头预览价值；不代表元素娃娃继续做全片主持；不代表元素娃娃替代录屏主体；不代表元素娃娃替代真人判断段。 |

## 3. cleanup_audit（清理审计）

### 3.1 keep_must（必须保留）

| 路径 | 中文说明 | 保留原因 |
| --- | --- | --- |
| `素材库_assets/元素娃娃开头锚点_opening_anchor_20260428/005_1496_seg01_no_text_inpaint_opening_anchor.mp4` | v3.1 元素娃娃开头锚点 | 当前唯一固定素材锚点 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/shot00_opening_hello_wave_preview.mp4` | v3.1 开头预览 | 当前复审包开头证据 |
| `dist/latest_review_pack/summary.json` | 当前复审包摘要 | 当前 v3.1 发布后灰度测试状态入口 |
| `dist/latest_review_pack/review_manifest.md` | 当前复审入口 | 当前结构和复审入口 |
| `dist/latest_review_pack/timeline.json` | 当前时间线 | v3.1 shot / segment 结构资产 |
| `dist/latest_review_pack/cut_map.md` | 当前切点图 | v3.1 镜头结构资产 |
| `dist/latest_review_pack/visual_route_map.json` | 视觉路由表 | v3.1 三路视觉路由资产 |
| `dist/latest_review_pack/visual_route_validation_report.json` | 视觉路由验证报告 | route 通过证据 |
| `codex_source/locked_reference_registry.md` | 锁定参考登记表 | reference 正式登记入口 |
| `codex_source/14_locked_reference_inheritance_rules.md` | 锁定参考继承规则 | 后续 reference 继承边界 |
| `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md` | v3.1 视觉路由规则 | 后续升级前置规则 |
| `codex_log/current_local_artifact_paths.md` | 当前本地产物路径索引 | 本轮补充路径的唯一正式索引 |

### 3.2 freeze_do_not_touch（冻结不动）

| 路径 / 对象 | 中文说明 | 冻结原因 |
| --- | --- | --- |
| `PR #46` | `Record blocked formal short-video auto-flow TTS retry` | open / draft / not merged；只保留为未来流程教学类方向资料 |
| `dist/完整成片_full_videos/20260503_短视频自动流最简单流程_full_reference_quality_video/` | PR #46 相关结构资产 | 本轮降权但不删除、不移动、不归档 |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | GPT Project 静态包未追踪文件 | 用户明确要求本轮单独冻结 |
| `GPT 数据源/` | GPT Project 静态协作包目录 | 用户明确要求本轮不动整个有空格目录 |
| `contact_sheet_frames/inputs.txt` | PR #46 contact sheet 输入清单 | 位于 PR #46 冻结范围 |
| `local_fix_20260504_reference_quality_v1/v2/v3` | PR #46 本地修正版 | 可能仍有流程教学对照价值，本轮不动 |
| `blocked_unknown` 全部项目 | 不确定项 | 禁止删除 |

### 3.3 archive_only（只归档不删除）

| 路径 | 中文说明 | 归档原因 |
| --- | --- | --- |
| `归档_archive/旧口径_old_context_20260502/` | 旧口径归档目录 | 仍有复盘价值，但不得默认读取为当前事实 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v3_ai_ppt_pitfall_finished_candidate_v3/` | v3 历史候选复审包 | v3 不再作为后续默认基础 |
| `复审包_review_packs/20260430_AI做PPT踩坑_成品标准候选_v2_ai_ppt_pitfall_finished_candidate_v2/` | PR #15 v2 失败 / 候选历史包 | 已作为 failed reference 反例，保留复盘价值 |
| `本地归档_local_archive/` | 已回收外部路径资料 | 仅作历史来源，不作为执行路径 |
| `本地隔离区_local_quarantine/` | 外部散目录待确认隔离区 | 不确定项，禁止直接删除 |

### 3.4 safe_delete（可安全删除）

| 路径 | 中文说明 | 删除依据 | 二次引用检查结果 |
| --- | --- | --- | --- |
| `selected .DS_Store files` | Finder 临时元数据 | 非业务资产、非 manifest / summary / registry / timeline / cut_map / path index 引用 | `rg` 二次检查未发现当前结构地图或路径索引引用具体删除候选；执行目标原本排除 `.git/`、`.omx/`、`node_modules/`、`GPT 数据源/`、PR #46 目录、`dist/latest_review_pack/`、当前 v3.1 复审包、`素材录制/`、元素娃娃开头锚点目录；但 `find -delete` 的执行行为导致部分受保护目录内 `.DS_Store` 临时元数据也被删除，已在偏差记录中说明。 |

### 3.5 rewrite_needed（需要重写 / 降权）

| 路径 / 对象 | 中文说明 | 处理结果 |
| --- | --- | --- |
| `codex_log/current_local_artifact_paths.md` | 缺 v3.1 元素娃娃开头路径索引 | 已补充 `v31_element_doll_opening_anchor` 与 `v31_element_doll_opening_preview` |
| `PR #46` | 容易被误读为当前主参考 | 已在本报告和路径索引说明中降权为未来流程教学方向资料 |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | 未追踪 GPT Project 静态包文件 | 本轮冻结不动，后续另起任务 |

### 3.6 blocked_unknown（不确定，禁止动）

| 路径 / 对象 | 中文说明 | 阻断原因 |
| --- | --- | --- |
| `no_zoom_1x_review_frames` | 历史 no_zoom 复审图 | 路径索引为 `path_exists=false`，但仍是历史线索 |
| `no_zoom_layout_metrics` | 历史 no_zoom 布局指标 | 路径索引为 `path_exists=false`，但仍是历史线索 |
| `本地隔离区_local_quarantine/` | 外部散目录隔离区 | 需要用户另轮确认是否仍有唯一证据价值 |
| `PR #46 local_fix v1/v2/v3` | 并行分支本地修正版 | 已降权但可能有流程教学对照价值 |

## 4. 实际执行清单

### 4.1 实际删除

| 路径 | 删除原因 | 验证方式 |
| --- | --- | --- |
| `94` 个 `.DS_Store` 文件；另有 `3` 个复核时由本地环境重建后再次清理 | Finder 临时元数据 | 删除前候选清单 + 引用检查；复核发现 `.DS_Store` 可被本地环境重新生成，均不进入 Git 跟踪 |

### 4.1A 执行偏差记录

- `部分成立` 原计划只删除冻结 / 保护范围外的 `.DS_Store`。
- `已确认` 实际执行时，`find -delete` 触发深度遍历行为，导致部分原计划排除目录内的 `.DS_Store` 也被删除。
- `已确认` 被额外影响的对象仅为 `.DS_Store` Finder 临时元数据，不是业务文件、视频、manifest、summary、registry、timeline、cut_map、路径索引、PR #46 核心文件或 `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`。
- `已确认` 删除后复核：`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 仍存在且未被纳入 Git；v3.1 元素娃娃开头锚点与 v3.1 开头预览仍存在。

### 4.2 实际归档 / 降权

| 路径 | 处理方式 | 原因 |
| --- | --- | --- |
| `PR #46` | 降权为 `parallel_future_flow_teaching_asset` | 当前不作为 reference，不进入主读取正式状态 |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | 冻结说明 | 本轮不纳入、不删除、不移动、不改名 |
| 旧 PR / 旧 round / 旧候选资料 | 保留在既有归档 / 历史包 | 有复盘价值但不得默认继承 |

### 4.3 本轮未动但后续可处理

| 路径 / 对象 | 后续建议 | 需要用户确认什么 |
| --- | --- | --- |
| `PR #46 local_fix v1/v2` | 后续可单独判断是否归档或删除 | 是否仍需要作为流程教学对照 |
| `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` | 另起 GPT Project 静态包整理任务 | 是否纳入仓库、移动到正式目录或删除 |
| `本地隔离区_local_quarantine/` | 另起隔离区清理任务 | 是否仍有唯一证据价值 |

## 5. PR #46 状态处理

- `已确认` PR #46 本轮未合并。
- `已确认` PR #46 本轮未关闭。
- `已确认` PR #46 当前不作为参考。
- `已确认` PR #46 只作为未来流程 / 教学 / 操作拆解类视频升级方向资料。
- `已确认` PR #46 local fix v3 不写成内容通过。
- `已确认` PR #46 不写成 `send_ready = true`。

## 6. GPT Project 静态包文件处理

- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 本轮未动。
- `已确认` 本轮不纳入、不删除、不移动、不改名。
- `部分成立` `GPT 数据源/` 目录中的 `.DS_Store` 临时元数据被上述删除偏差影响；业务文件未被修改、移动或删除。
- `下一个目标`：后续另起 GPT Project 静态包整理任务。

## 7. 状态字段保护确认

- `content_validation（内容验证）` 没有被写成 `passed`。
- `send_ready（可发送状态）` 没有被写成 `true`。
- `voice_validation（声音验证）` 没有被写成 `final`。
- 当前 v3.1 发布 / 灰度状态没有被修改。

## 8. 验证记录

- `git diff --check`：`passed`
- 重新读取路径索引：`passed`，`v31_element_doll_opening_anchor` 与 `v31_element_doll_opening_preview` 均存在。
- 删除清单复核：`部分成立`，`.DS_Store` 已执行清理；本地环境会重建少量 `.DS_Store`，该类文件未进入 Git 跟踪。
- keep / freeze / blocked 是否未被删除：`passed`，元素娃娃锚点、v3.1 开头预览、`GPT 数据源/10_...`、当前结构地图文件均存在。
- 当前发布状态是否未变：`passed`，`codex_log/current_publish_target.md` 与 `dist/latest_review_pack/*` 未出现在 diff 中。
