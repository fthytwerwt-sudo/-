# 20260504_元素娃娃开头保留与旧资产清理_keep_element_doll_cleanup_old_assets

## 1. 本轮定位

- `已确认` 本轮是《视频工厂》参考资产收缩与旧资产清理任务。
- `已确认` 本轮不生成视频，不修改 v3.1 当前发布状态，不修改 `current_publish_target.md` 状态字段。
- `已确认` 当前唯一固定素材锚点收缩为 v3.1 元素娃娃开头。

## 2. 路径索引补充

- `已确认` 已将 `v31_element_doll_opening_anchor` 补入 `codex_log/current_local_artifact_paths.md`。
- `已确认` 已将 `v31_element_doll_opening_preview` 补入 `codex_log/current_local_artifact_paths.md`。
- `已确认` 两个路径均在 `/Users/fan/Documents/视频工厂` 唯一正式工作区内，并已执行 `test -f` 验证存在。
- `边界`：只保留开头价值；不代表元素娃娃继续做全片主持；不代表元素娃娃替代录屏主体；不代表元素娃娃替代真人判断段。

## 3. PR #46 降权

- `已确认` PR #46 当前仍为 `open / draft / not merged`。
- `已确认` PR #46 本轮未合并、未关闭、未删除。
- `已确认` PR #46 暂时不作为当前 reference。
- `已确认` PR #46 仅作为未来流程 / 教学 / 操作拆解类视频升级方向资料。
- `边界`：PR #46 local fix v3 不写成内容通过，不写成 `send_ready = true`。

## 4. GPT Project 静态包冻结

- `已确认` `GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md` 本轮冻结不动。
- `已确认` 本轮不纳入、不删除、不移动、不改名。
- `下一个目标`：后续另起 GPT Project 静态包整理任务。

## 5. 清理执行

- `已确认` 已先写 `cleanup_audit（清理审计）`，再执行删除。
- `已确认` 实际删除对象均为 `.DS_Store` Finder 临时元数据。
- `部分成立` 删除前原计划排除 `.git/`、`.omx/`、`node_modules/`、`GPT 数据源/`、PR #46 目录、`dist/latest_review_pack/`、当前 v3.1 复审包、`素材录制/`、元素娃娃开头锚点目录；但 `find -delete` 的执行行为导致部分受保护目录内 `.DS_Store` 也被删除。
- `已确认` 被额外影响的对象仅为 `.DS_Store`，不是业务文件；`GPT 数据源/10_样片参考质量规则_reference_quality_sample_rule.md`、当前结构地图、PR #46 核心文件、元素娃娃开头锚点和 v3.1 开头预览均未被删除。
- `已确认` 未删除任何核心 reference、当前结构地图文件、v3.1 元素娃娃开头资产或 blocked_unknown。

## 6. 报告

- `治理_reports/20260504_元素娃娃开头保留与旧资产清理_keep_element_doll_cleanup_old_assets/元素娃娃开头保留与旧资产清理报告_keep_element_doll_cleanup_old_assets_report.md`

## 7. 状态保护

- `content_validation` 未写成 `passed`。
- `send_ready` 未写成 `true`。
- `voice_validation` 未写成 `final`。
- 当前 v3.1 发布 / 灰度状态未修改。

## 8. 下一个目标

用户 / ChatGPT 复审本轮 PR，确认元素娃娃开头路径索引补充无误、旧资产清理未误删；通过后再进入项目升级前的机制收口。
