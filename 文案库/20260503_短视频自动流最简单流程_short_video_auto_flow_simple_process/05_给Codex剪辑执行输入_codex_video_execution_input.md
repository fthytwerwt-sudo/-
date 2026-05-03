# 给 Codex 剪辑执行输入：短视频自动流的最简单流程 V2

## 1. 标题

《短视频自动流的最简单流程》

## 2. 文案文件路径

- 完整口播稿：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/01_完整口播稿_full_script.md`
- 分段承载表：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/02_分段承载表_block_segment_material_map.md`
- 卡片文案：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/03_卡片文案_card_copy.md`
- 执行注意事项：`/Users/fan/Documents/视频工厂/文案库/20260503_短视频自动流最简单流程_short_video_auto_flow_simple_process/04_执行注意事项_execution_notes.md`

## 3. 推荐素材路径与时间码

| 用途 | 素材路径 | 推荐时间码 | 说明 |
|---|---|---|---|
| 一句需求输入 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:00:16-00:00:24 | 用户只输入一句简单需求。 |
| 豆包拆方案 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:01:28-00:02:00 | 豆包输出轻量版到无人值守版方案。 |
| 用户要求 Trae prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:02:40-00:02:56 | 用户要求豆包生成给 Trae 的 prompt。 |
| 豆包输出 Trae SOLO prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:03:52-00:04:08 | 可见 Trae Vlog 自动流核心搭建 prompt 和模块清单。 |
| 进入 Trae SOLO Coder | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:00:32-00:01:04 | 可见 SOLO Coder 和 `/plan`、`/spec` 能力提示。 |
| prompt 进入 Trae 并 plan | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:01:20-00:01:52 | prompt 模块文字、`Updating Tasks...`、`11 待办`。 |
| Trae 生成项目骨架 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:02:00-00:02:40 | `vlog_automation_workflow`、目录、`settings.py`、`base_module.py`。 |
| API 特写 | 火山引擎素材仅可脱敏使用 | 条件使用 | 本轮无法自动确认安全脱敏，fallback 到信息卡。 |
| 阿里云剪辑 / ICE / 云剪 | 信息卡 | 信息卡 | 说明云端总装候选位置，不证明正式稳定。 |
| Codex 执行检查 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:02:56-00:03:08 | `ffprobe`、命令执行、文件变更、Git 操作和报告文件。 |
| HyperFrames 技术处理 B-roll | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:03:36-00:03:44 | 只作候选，不作为 Codex 检查主证据。 |

## 4. 卡片清单

1. 流程总览卡：自动流不是一键生成。
2. 豆包到 Trae prompt 卡：把想法翻译成执行器能接的任务说明。
3. Trae 骨架卡：看不懂代码没关系，先看 app / 项目有没有初步形状。
4. API 解释卡：API 是把外部工具接成系统可调用能力。
5. 阿里云剪辑总装卡：它是装配台，不是总控脑。
6. Codex 检查卡：技术检查不等于内容过线。
7. 即梦对比卡：即梦像抽素材，自动流像搭流程。
8. 最后总结卡：顺序对了，自动化才有地方落脚。

## 5. 禁用 / 条件素材

- 火山引擎素材：未完成安全脱敏前不得使用原画面；本轮 fallback 到信息卡。
- 创建文件夹素材：只可弱 B-roll。
- 2026-04-30 长录屏：默认不进入本条视频。

## 6. 输出状态边界

- `technical_validation` 必须由 ffprobe / decode 结果决定。
- `content_validation = pending_user_chatgpt_review`。
- `send_ready = false`。
- `audio_validation = temporary_preview` 或 `silence_placeholder`，不得写最终声音通过。
