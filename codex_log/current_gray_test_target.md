# Current Gray Test Target

## 当前对象

- `已确认` 当前主题：`我用 AI 做 PPT 踩过的坑`
- `已确认` 当前视频版本：`v3.1`
- `已确认` 当前视频基线：`v3.1`
- `已确认` 后续升级 / 修改 / 技术优化 / GPT 文案侧回炉默认基于：`v3.1`
- `已确认` 当前阶段：`post_publish_gray_test（发布后灰度测试阶段）`
- `已确认` 发布状态：`gray_test_published（已发片，进入灰度测试）`
- `已确认` 灰度状态：`active（灰度测试中）`
- `已确认` 发布后复盘要求：`post_publish_review_required = true`

## 当前目标

用 v3.1 这条已发布视频跑完 24h / 72h 灰度观察，判断它的主要问题层，并产出下一轮“只改一个变量”的执行方向。

## 观察窗口

- `24h 初检`：等待用户回填发布后 24h 数据。
- `72h 复检`：等待用户回填发布后 72h 数据。

## 优先观察指标

- 播放量
- 完播率
- 收藏率
- 前 3 秒留存
- 平均观看时长
- 点赞率
- 评论数
- 转粉数
- 私信 / 咨询数
- 中段主要流失点

## 诊断层

- 场景层
- 结构层
- 心理机制层
- 画面表现层
- 字幕与配音节奏层
- 转化承接层

## 当前执行机制

- 单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
- 单条模板：`review_loop/02_video_record_template.md`
- 结果看板模板：`review_loop/03_result_dashboard_template.md`
- 诊断模板：`review_loop/04_diagnosis_template.md`
- Codex 初检 / ChatGPT 判断交接：`review_loop/05_dual_review_handoff_template.md`
- 下一轮只改一个变量：`review_loop/06_next_round_task_template.md`

## 当前禁止判断

- 不得写成内容通过。
- 不得写成账号方向已验证。
- 不得写成市场成立。
- 不得写成规律成立。
- 不得跳过数据直接设定下一条文案。
- 不得把已发片写成最终成功。
- 不得把灰度测试写成验证成功。

## 当前保持状态

- `content_validation = gray_testing_not_final_passed`
- `send_ready = false`
- `visual_master_locked = false`
- `voice_validation = pending_user_chatgpt_review`
- `final_voice_validated = false`
- `technical_upgrade_next = true`

## reference 边界

- `已确认` PR #7 B 是后续骚萌卡唯一执行参考。
- `已确认` PR #7 A 只能作为历史 / candidate 对照。
- `已确认` 读不到 PR #7 B 必须 blocked，不得回退 PR #7 A。

## 下一步

1. 等待用户补充发布平台、发布时间、视频链接。
2. 等待用户回填 24h 数据。
3. 24h 数据回填后，Codex 按 `review_loop/04_diagnosis_template.md` 做初检。
4. ChatGPT / 用户基于初检判断主要问题层和下一轮唯一改点。
5. 72h 数据回填后，再做复检，不提前写成规律成立。
