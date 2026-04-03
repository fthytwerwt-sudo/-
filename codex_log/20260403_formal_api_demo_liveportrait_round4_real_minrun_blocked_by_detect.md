# 2026-04-03 formal_api_demo 真人开口 round4：真实最小闭环已执行，detect 阻塞

## 本轮目标

- 直接使用当前 worktree 的 `config/formal_api_demo.local.toml`
- 用正式入口跑最小 `liveportrait-detect -> liveportrait` 真实闭环
- 把失败压到 detect / create / poll / download 的具体层级

## 实际运行命令

- 第 1 次：
  - `python3 scripts/generate_formal_api_demo.py --local-config config/formal_api_demo.local.toml --out dist/formal_api_demo_liveportrait_minrun`
- 第 2 次：
  - `python3 scripts/generate_formal_api_demo.py --local-config config/formal_api_demo.local.toml --out dist/formal_api_demo_liveportrait_minrun_retry_tts`

## 第 1 次真实运行结果

- `detect`：
  - 已真实执行
- `liveportrait`：
  - 未开始创建任务
- 当前结果：
  - `failed`
- 最具体原因：
  - 当前 worktree 的 TTS 配置先返回：
    - `AccessDenied`
    - `model Access denied.`
  - 同时 `liveportrait-detect` 对当前 `seg02` 图返回：
    - `No human face detected.`
- 本地落地：
  - 有脚本 / 字幕 / 部分图片
  - 无真人开口视频文件

## 第 2 次真实运行结果

- 处理动作：
  - 仅修正当前 worktree 本地 TTS 取值到主工作区那组真实值
  - 未改业务代码
- `detect`：
  - 已真实执行
  - 已拿到 `request_id`
  - 结果：
    - `blocked`
    - `failure_reason = portrait_detect_rejected`
    - `blocked_reason = No human face detected.`
- `liveportrait`：
  - 未开始创建任务
  - `task_id = null`
  - `request_id = null`
  - `asset_path = null`
- `tts_probe`：
  - `success`
- `voiceover`：
  - `success`
- 当前结果：
  - `blocked`

## 最具体 blocker

- 当前 `seg02` 输入图不包含可检测真人脸
- 所以：
  - `liveportrait-detect` 真实 reject
  - `liveportrait` 根本没有进入 create task / poll / download

## 本地结果文件

- 第 2 次运行输出目录：
  - `dist/formal_api_demo_liveportrait_minrun_retry_tts/`
- 已落地：
  - `tts/voice_probe.mp3`
  - `tts/formal_voiceover.mp3`
  - `tts/segment_seg01.mp3`
  - `tts/segment_seg02.mp3`
  - `tts/segment_seg03.mp3`
  - `visual/seg01_image.png`
  - `visual/seg02_image.png`
  - `manifest.json`
  - `result_summary.json`
- 未落地：
  - 真人开口视频文件

## 当前状态改标

- 真人开口分支：
  - `blocked`
- overall：
  - `blocked`

## 下一轮唯一最关键一步

1. 把 `seg02` 输入改成有清晰真人正脸的人像底图
2. 保持当前已可用的 TTS 配置
3. 重新跑最小 `liveportrait-detect -> liveportrait`
