# 给 Codex 剪辑执行输入：短视频自动流的最简单流程

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
| 一句需求输入 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:00:16-00:00:24 | 用户输入 `我想用 Trae 做一个短视频自动流`。 |
| 豆包拆方案 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:01:28-00:02:00 | 标题和核心流程可见。 |
| 用户要 Trae prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:02:40-00:02:56 | 用户明确要求豆包生成给 Trae 的 prompt。 |
| 豆包输出 Trae SOLO prompt | `/Users/fan/Documents/视频工厂/素材录制/最新素材/豆包素材.mp4` | 00:03:52-00:04:08 | 可见直接复制到 Trae SOLO 的核心搭建 prompt 和模块。 |
| 进入 Trae SOLO Coder | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:00:32-00:01:04 | 可见 SOLO Coder 和 `/plan`、`/spec` 能力提示。 |
| prompt 进入 Trae 并 plan | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:01:20-00:01:52 | prompt 模块文字、`Updating Tasks...`、`11 待办`。 |
| Trae 生成项目骨架 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/trae 素材.mp4` | 00:02:00-00:02:40 | `vlog_automation_workflow`、目录、`settings.py`、`base_module.py`。 |
| Codex 执行检查 | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:02:56-00:03:08 | `ffprobe`、命令执行、文件变更、Git 操作和报告文件。 |
| HyperFrames 技术处理 B-roll | `/Users/fan/Documents/视频工厂/素材录制/最新素材/codex 素材.mp4` | 00:03:36-00:03:44 | 只作候选，不作为 Codex 检查主证据。 |

## 4. 卡片清单

1. 流程总览卡：短视频自动流，不是一键生成。
2. 豆包 -> Trae prompt 卡：豆包把想法翻译成 Trae 能接住的任务说明。
3. API 解释卡：API 是把工具变成系统可调用能力。
4. 阿里云剪辑总装卡：阿里云剪辑不是总控脑，更像装配台。
5. Codex / Claude / Trae 执行层卡：流程在，工具可以换。
6. 即梦 vs 自动流对比卡：即梦像抽素材，自动流像搭流程。
7. 最后总结卡：别一上来追求一键生成，先把顺序理出来。

## 5. 禁用素材

- `/Users/fan/Documents/视频工厂/素材录制/最新素材/火山引擎素材.mp4`
  - 禁用原因：未打码前含手机号、短信验证码、API Key 管理页和资源 ID 痕迹。
  - 替代方式：API 相关口播使用信息卡。
- `/Users/fan/Documents/视频工厂/素材录制/最新素材/录屏2026-04-30 03.25.28.mov`
  - 禁用原因：历史长录屏，不默认进入本条视频。

## 6. 弱素材

- `/Users/fan/Documents/视频工厂/素材录制/最新素材/创建文件夹.mp4`
  - 只可作为弱 B-roll，不作为主线素材。

## 7. 风险遮挡项

- 豆包：历史会话侧栏、昵称、小字截断处。
- Trae：本地路径、文件夹名、项目列表、环境提示 / 失败提示不得被剪掉后误导成全成功。
- Codex：右侧分支详情、底部路径、文件名、巨大 diff 数字、本地任务信息。
- 火山引擎：未打码前整段禁用。

## 8. 状态边界

- `已确认` 本包只生成文案执行包，未生成视频 / 音频 / 图片。
- `已确认` 豆包输出方案不等于工程跑通。
- `已确认` Trae 生成项目骨架不等于代码运行成功。
- `待验证` 阿里云剪辑只是云端总装方向 / 技术验证候选，不是正式稳定链路。
- `已确认` Codex 检查不等于内容过线。
- `待验证` 后续执行前必须由 ChatGPT 复审本包。

## 9. 后续执行前置条件

后续 Codex 视频执行任务必须先读取：

1. 本文件。
2. `01_完整口播稿_full_script.md`
3. `02_分段承载表_block_segment_material_map.md`
4. `03_卡片文案_card_copy.md`
5. `04_执行注意事项_execution_notes.md`

`待验证` ChatGPT 复审通过后，才进入剪辑执行。
