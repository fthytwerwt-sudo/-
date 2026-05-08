# 20260503 HyperFrames 卡片动效边界与阿里云剪辑审计

## 1. 本轮范围

- `已确认` 当前工作区：`/Users/fan/Documents/视频工厂`。
- `已确认` 当前分支：`codex/hyperframes-card-routing-and-aliyun-edit-audit-20260503`。
- `已确认` 本轮只做 HyperFrames 卡片动效接入规则设计与阿里云剪辑只读审计。
- `已确认` 未生成视频、音频、图片。
- `已确认` 未写新文案，未处理 HyperFrames 中段录屏接入，未修改 v3.1 正片，未修改 `dist/latest_review_pack/` 既有产物。
- `已确认` `content_validation` 保持当前灰度测试口径。
- `已确认` `send_ready` 保持 `false`。

## 2. 读取依据

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `dist/latest_review_pack/visual_route_map.json`
- `dist/latest_review_pack/visual_route_validation_report.json`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_local_artifact_paths.md`
- `package.json`
- `package-lock.json`
- `README.md`

## 3. HyperFrames route mapping

| HyperFrames motion | 现有 route | 允许 segment | 状态 |
| --- | --- | --- | --- |
| 数据卡 / 结果差卡动效 | `cute_info_card_route` | `shot15_result_diff_card`；未来灰度数据卡只能作为同 route 扩展 | `已确认` |
| Prompt 引用尾卡动效 | `cute_info_card_route` | `shot16_low_pressure_ending` | `已确认` |
| 骚萌卡动效版 | `sassy_reaction_card_route` | `shot03_problem_hook_sassy_card`、`shot05_negative_reversal_sassy_card`、`shot14_positive_reversal_sassy_card` | `已确认` |

`已确认` HyperFrames 当前只是 `card_motion_layer（卡片动效层）`，不是新视觉路由，不替代云端剪辑，不替代真实录屏证据。

当前明确禁止 HyperFrames 接入：

- 用户录制素材中段
- 反面录屏
- 正面录屏
- 录屏证据段
- 录屏动态标注
- 录屏包装框
- 录屏叠层
- 整条视频生成
- API 生成真人段
- 云端剪辑总装

## 4. 阿里云剪辑审计结论

- `部分成立` 仓库当前仍保留阿里云 ICE / OSS 云端 assembly 代码路径和配置字段。
- `已确认` 历史日志中存在 20260405-20260408 的云剪 / ICE 验证与导出样本。
- `未发现当前实际调用证据` 当前 v3.1 `dist/latest_review_pack/` 未发现阿里云剪辑 / ICE assembly 调用记录；命中的阿里百炼内容属于 TTS / voice clone，不等于剪辑服务。
- `待验证` 后续是否继续将阿里云剪辑作为 vNext 实际总装运行链路，需要单独执行云端导出或读取新的执行记录。

## 5. 修改文件

- `codex_source/15_v31视觉路由规则_v31_visual_routing_rules.md`
- `GPT数据源/05_文案路由规则.md`
- `GPT数据源/07_AI知识类视频价值规则.md`
- `codex_log/latest.md`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/HyperFrames卡片边界写入报告_hyperframes_card_boundary_report.md`
- `治理_reports/20260503_HyperFrames卡片边界与阿里云剪辑审计_hyperframes_card_boundary_aliyun_audit/阿里云剪辑使用审计报告_aliyun_edit_usage_audit.md`

## 6. 下一个目标

- ChatGPT 复审本轮 PR 是否可合并。
- 如果需要继续判断阿里云剪辑保留 / 替换 / 降级，另起单独执行链路决策任务。
