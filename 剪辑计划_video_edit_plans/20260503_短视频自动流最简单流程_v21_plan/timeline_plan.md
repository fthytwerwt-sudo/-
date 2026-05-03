# timeline_plan｜短视频自动流的最简单流程 V2.1

## 1. 总体目标

- `total_runtime_target_seconds`：`105`
- `plan_status`：`review_ready_not_render_ready`
- `content_validation`：`pending_user_chatgpt_review`
- `send_ready`：`false`
- `render_allowed_now`：`false`

本时间线只用于 ChatGPT / 用户审核。下一轮 render 前必须复读本计划包，不得回退 PR #41 的长说明片结构。

## 2. 12 段时间线

| segment | 类型 | 目标时长 | 素材 / 画面 | 剪辑重点 | 证明 | 不能证明 |
|---|---|---:|---|---|---|---|
| 01 开头判断 | `card` | 3s | 信息卡 | “自动流不是一键生成” | 建立判断 | 不证明任何工具跑通 |
| 02 豆包一句需求 | `real_footage` | 7s | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` 00:00:16-00:00:24 | 放大输入“我想用 Trae 做一个短视频自动流” | 需求入口简单 | 不证明 Trae 已执行 |
| 03 豆包拆流程 | `real_footage` | 13s | `豆包素材.mp4` 00:01:28-00:02:00 | 截最清楚的标题和核心链路，不长时间滚动整页 | 豆包把需求拆成流程 | 不证明工程跑通 |
| 04 豆包生成 Trae prompt | `real_footage` | 18s | `豆包素材.mp4` 00:02:40-00:04:08 | 两段快切：用户要求 prompt；豆包输出 prompt 标题和模块 | 豆包生成 Trae 能接的任务说明 | 不证明 prompt 已运行成功 |
| 05 进入 Trae SOLO | `real_footage` | 8s | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` 00:00:32-00:01:04 | 裁切本地路径，保留 SOLO Coder、`/plan`、`/spec` | 用户进入执行器 | 不证明执行完成 |
| 06 Prompt 进入 Trae 并 plan | `real_footage` | 14s | `trae 素材.mp4` 00:01:20-00:01:52 | 必须保留 prompt 模块文字、Updating Tasks、11 待办 | Trae 接住 prompt 并拆任务 | 不证明所有待办完成 |
| 07 Trae 项目骨架 | `real_footage` | 18s | `trae 素材.mp4` 00:02:00-00:02:40 | 放大文件树和文件名，遮挡本地路径 | 从聊天方案变成项目骨架 | 不证明 app 已跑通 |
| 08 API 工位 | `card` | 4s | API 信息卡 fallback | 不使用火山原画面 | API 是外部能力入口 | 不证明 API 已接通 |
| 09 云端剪辑工位 | `card` | 4s | 信息卡 | 云剪是装配台，不是总控脑 | 说明总装位置 | 不证明正式稳定链路 |
| 10 Codex 检查 | `real_footage` | 8s | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` 00:02:56-00:03:08 | 遮挡右侧分支详情、底部路径、文件名、巨大 diff 数字、本地任务信息 | Codex 检查路径、文件、命令、报告 | 不证明内容过线 |
| 11 即梦对比 | `card` | 4s | 信息卡 | 抽素材 vs 搭流程 | 说明工具定位差异 | 不证明即梦不可用 |
| 12 总结 | `card` | 4s | 信息卡 | 顺序对了，自动化才有地方落脚 | 收住主判断 | 不证明可发布 |

## 3. 节奏约束

- `已确认` 真实录屏总时长：`86s`。
- `已确认` 卡片总时长：`19s`。
- `已确认` 卡片最长时长：`4s`。
- `已确认` 卡片只做提示和转场，不承担主叙事。
- `已确认` 主体流程推进由豆包 / Trae / Codex 真实录屏承担。
- `已确认` 本计划不是 PR #41 的 731 秒长说明片。
