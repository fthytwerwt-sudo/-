# review_loop 总说明

## 1. 这套文件是干什么的

`review_loop/` 用来承接视频发出之后的复盘执行工作。

它当前只负责四件事：

- 记录单条视频的发布前变量与发布后结果
- 做结构化初检，先把现象、字段、缺失项和疑似问题层压清楚
- 归档每一条视频的复盘记录，避免结论只停在聊天里
- 生成下一轮执行单草稿，方便 Codex 稳定接手下一条

这套文件不是：

- GPT 数据源重写区
- 大而全数据中台
- 自动化采集脚本系统
- 平台运营闭环

当前只做 `v1`，先把“文件化复盘执行层”建稳。

## 2. 它和 `project_source/`、`codex_source/` 的区别

三层分工必须固定：

- `project_source/`
  - 负责稳定判断层
  - 负责项目身份、阶段、边界、主场景、主结构、质量口径、回审模板
- `codex_source/`
  - 负责执行规则层
  - 负责 Codex 默认先读什么、能改什么、怎么验证、怎么汇报、何时必须停下
- `review_loop/`
  - 负责视频发出后的复盘执行层
  - 负责记录、初检、归档、下轮任务草稿

一句话说清：

- `project_source/` 回答“这项目是什么、该怎么判断”
- `codex_source/` 回答“Codex 该怎么执行、怎么如实汇报”
- `review_loop/` 回答“视频发出后，复盘这件事怎么稳定落文件”

## 3. 当前 v1 的边界

当前 `review_loop/` 只服务于《视频工厂：AI 垂类场景化视频内核》的小样本复盘阶段。

当前边界必须写清：

- 只围绕视频复盘，不扩到直播、增长、售卖、商业化
- 不把结果看板写成整个系统主骨架
- 不自动扩到自动化采集
- 不自动扩到脚本化诊断
- 不让 Codex 越权替 ChatGPT 做最终判断拍板

## 4. 当前推荐使用顺序

一条视频发布后，默认按这个顺序使用：

1. 用 `02_video_record_template.md` 建单条记录
2. 用 `03_result_dashboard_template.md` 把结果并到看板
3. 用 `04_diagnosis_template.md` 做初步诊断动作
4. 用 `05_dual_review_handoff_template.md` 交给“Codex 初检 → ChatGPT 质量判断”
5. 用 `06_next_round_task_template.md` 生成下一轮执行单草稿

## 4A. 当前 v3.1 灰度测试使用方式

`已确认` 《我用 AI 做 PPT 踩过的坑》v3.1 已发片，当前进入 `post_publish_gray_test（发布后灰度测试阶段）`。

当前灰度测试不是一套新系统，只是 `review_loop/` 在 v3.1 发布后的当前阶段名称。

本阶段固定使用方式：

1. 单条记录：`review_loop/records/20260502_v31_AI做PPT踩坑_gray_test_record.md`
2. 单条模板：`review_loop/02_video_record_template.md`
3. 结果看板：`review_loop/03_result_dashboard_template.md`
4. 诊断初检：`review_loop/04_diagnosis_template.md`
5. 双层交接：`review_loop/05_dual_review_handoff_template.md`
6. 下一轮草稿：`review_loop/06_next_round_task_template.md`
7. 当前灰度目标：`codex_log/current_gray_test_target.md`

本阶段治理规则吸收 `project_source/14_content_review_and_loop_governance_rules.md`：

- 24h 初检 / 72h 复检
- 一次只改一个变量
- 小样本阶段默认保守，少于 3 条只能做观察
- 异常样本可以记录、可以参考，但不得作为规律沉淀主证据
- 规律沉淀必须满足样本数、时间窗口、边界描述和异常排除门槛

当前禁止：

- 不得把发片写成内容过线
- 不得把灰度测试写成验证成功
- 不得把 `content_validation` 写成 `passed`
- 不得跳过数据直接设定下一条文案
- 不得把 PR #7 A 写成后续执行参考

## 5. 当前归档口径

当前 `v1` 的“归档”不是做自动系统，而是要求每条视频的复盘信息都能落成仓库文件。

归档最低要求包括：

- 单条视频有独立记录
- 结果字段不只停在聊天
- 初检结论能回看
- 下一轮只改一个变量的草稿能留痕

后续如果样本量上来，再决定是否补子目录或脚本；这不属于当前轮范围。

## 6. 当前一句话规则

`review_loop/` 不是项目脑，也不是执行总规则；它是视频发出后给 Codex 用的复盘执行层 v1，只做记录、初检、归档和下轮任务草稿，不替 ChatGPT 做最终拍板；当前 v3.1 灰度测试直接接入这套机制，不另起独立灰度系统。
