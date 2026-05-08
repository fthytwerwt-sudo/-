# AI 做 PPT 踩坑成品候选 v3.1 审片入口

`已确认` 本包是 `finished_quality_candidate_v31（成品质量候选片 v3.1）` 与当前视频基线；后续升级、修改、技术优化、GPT 文案侧回炉默认基于 v3.1。

`已确认` 本包已作为 v3.1 当前基线发片，当前进入 `post_publish_gray_test（发布后灰度测试阶段）`。

`已确认` 本包不是可发送版本，不代表内容验证通过，不代表视觉母版 locked；灰度测试不等于验证成功。

## 先看文件

1. `AI做PPT踩坑_成品候选_v31_full.mp4`：v3.1 完整成品候选片。
2. `AI做PPT踩坑_成品候选_v31_contact_sheet.jpg`：全片关键帧联系表。
3. `visual_route_map.json`：视觉路由表。
4. `visual_route_validation_report.json`：视觉路由验证报告。
5. `locked_reference_inheritance_report.md`：锁定参考继承报告。
6. `video_metadata_probe_report.json`：video-metadata-probe 检查报告 JSON。
7. `AI做PPT踩坑_成品候选_v31_summary.json`：状态摘要。
8. `AI做PPT踩坑_成品候选_v31_timeline.json`：时间线。
9. `AI做PPT踩坑_成品候选_v31_cut_map.md`：镜头说明。

## 当前边界

- `current_phase = post_publish_gray_test`
- `publish_status = gray_test_published`
- `gray_test_status = active`
- `post_publish_review_required = true`
- `content_validation = gray_testing_not_final_passed`
- `send_ready = false`
- `subtitle_enabled = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `visual_master_candidate = true`，但 `visual_master_locked = false`。
- `sassy_card_execution_reference = PR7_B_骚萌反应页.png`
- `sassy_card_reference_locked = true`

## 发布后灰度测试

- 当前灰度目标：`codex_log/current_gray_test_target.md`
- 截图录入规则：`review_loop/01_截图数据录入规则_screenshot_data_intake_rules.md`
- 单条主记录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/V001_gray_test_record.md`
- 当前记录目录：`review_loop/records/V001_v31_AI做PPT踩坑_gray_test/`
- 兼容旧记录入口：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- 截图证据目录：`review_loop/screenshots/V001_v31_AI做PPT踩坑/`
- 指标体系 V1：`review_loop/07_v31灰度测试指标体系_v31_gray_test_metrics_v1.md`
- 复盘执行层：`review_loop/`
- 观察窗口：`24h 初检`、`72h 复检`、`7d 封账`
- 7 天播放量基础测试流量门槛：`6000`
- 指标体系定位：不是运营数据大表，而是下一轮改动定位器
- 截图录入定位：用户可直接给截图，Codex 按视频 / 时间窗 / 数据类型归档并提取字段，不要求用户手填完整数据表
- 分桶规则：不同视频分开；`24h / 72h / 7d` 分开；平台数据 / 评论 / 私信 / 咨询分开
- 结果字段：播放量、完播率、收藏率、前 3 秒留存、平均观看时长、点赞率、评论数、转粉数、私信 / 咨询数、中段主要流失点
- 四层指标：流量层、内容层、账号增长层、私域 / 客户转化层
- 字段分级：核心必填字段、辅助观察字段、商业线索出现时才填字段
- 四个复盘问题：
  1. 这条有没有达到 6000 播放基础门槛？
  2. 当前最短板在哪一层：流量 / 内容 / 账号 / 转化？
  3. 下一轮只改哪一个变量？
  4. 为什么先改它，改完看哪个指标？
- 下一步：等待用户回填发布平台、发布时间、视频链接和 24h / 72h / 7 天数据；Codex 做初检，ChatGPT / 用户判断下一轮只改一个变量

当前禁止判断：

- 不得写成内容通过
- 不得写成账号方向已验证
- 不得写成市场成立
- 不得写成规律成立
- 不得跳过数据直接设定下一条文案
- 不得把不同视频、不同时间窗或不同截图类型混写
- 不得把截图识别不清的字段硬猜成确定值

## 本轮重点

- 先输出并校验 `visual_route_map.json`，再生成视频。
- 补回 `negative_display_prompt_card` 与 `positive_display_prompt_card`。
- 将三张骚萌卡改走 PR #7 B 的独立 reaction page 路线。
- 将信息卡改走粉色樱花柔和展示牌皮肤 + 清晰信息层级路线。
- 保留“反面结果露馅 -> 方法词出现 -> 字段拆解 -> 正面操作 -> 结果预览 -> 边界收束”的主线。
- 保留正反录屏素材事实，以真实录屏作为中段主体。
- 保留核心方法词：`可交付初稿`。
- 使用 custom voice TTS 入片，但声音仍待用户 / ChatGPT 听感复审。
- v3 只保留为历史候选 / 对照，不再作为后续默认修改基础。
- PR #7 A 只能作为历史 / candidate 对照，不能作为后续骚萌卡执行参考。
- 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。

## 本地路径

- 复审包：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix`
- full video：`/Users/fan/Documents/视频工厂/复审包_review_packs/20260430_AI做PPT踩坑_成品候选_v31_visual_route_fix/AI做PPT踩坑_成品候选_v31_full.mp4`
- duration_seconds：`149.993`
- resolution：`720x1280`
- audio_codec：`aac`
