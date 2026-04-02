# Latest

## 当前主读取分支

- 当前默认主读取分支：
  - `codex/user-readable-map`
- 2026-04-03 本轮任务分支：
  - `codex/formal-api-demo-quality-liveportrait-round1`
- 本轮内容：
  - A 线：普通主线质量审核 round1
  - B 线：真人开口分支 `liveportrait-detect -> liveportrait` round1

## 当前 formal_api_demo 真实状态

- TTS API：
  - `success`
- 图片 API：
  - `success`
  - `wan2.6-image` 已有真实 provider implementation
- 通用视频 API：
  - `success`
  - `wan2.6-t2v` 已有真实 provider implementation
- 真人开口分支：
  - `blocked`
  - `liveportrait-detect -> liveportrait` 的 provider implementation round1 已补到代码与测试层
  - 已完成官方契约核对，并补了 detect / liveportrait 的 success / fail / timeout / 本地结果缺失测试
  - 但当前 worktree 没有 `config/formal_api_demo.local.toml`
  - 因此还没做带真实 API Key 的线上实调，不得直接写成 `success`
- local assembly：
  - `success`
  - 正式本地 `final.mp4` 已可落出
- overall：
  - `blocked`
  - 技术主链只剩真人开口分支的真实线上验证
  - 普通主线已进入质量审核，但尚未通过质量收口

## A 线：普通主线质量审核 round1

- 已审核产物：
  - `cases/formal_api_demo.md`
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/visual/*`
  - `dist/formal_api_demo/final.mp4`
  - `dist/formal_api_demo/assembly/preview_manifest.json`
  - `dist/formal_api_demo/visual_generation_plan.json`
- 当前主结论：
  - 普通主线已经具备正式可审产物
  - 但当前只到“可继续复审水位”，还没到“质量过线可交付”
- 一票否决项：
  - 画面 demo / PPT 感仍然过重
  - 15 秒里有 9 秒仍由静态图承载，“散乱 -> SOP”的变化被说到了，但没有被真正看见
- 当前最关键的 2 个质量问题：
  - 中段推进仍偏“方法说明”，不像真实内容推进
  - 结果变化不够可视，观众看到的更像卡片轮播，不像流程被收束
- 下一轮质量修正只收口 2 点：
  - 把 `seg02` 改成更明显的“散乱 -> 结构化 SOP”可视变化
  - 把中段文案从抽象说明书口径压成更具体的推进句

## B 线：真人开口分支 round1

- 本轮已推进：
  - 核对阿里官方 `liveportrait-detect` / `liveportrait` 契约
  - 补齐 upload -> detect -> create task -> poll task -> download -> manifest 写回
  - 补齐 detect reject / detect timeout / task fail / task timeout / local file missing 测试
- 当前最具体 blocker：
  - 缺 `config/formal_api_demo.local.toml`
  - 因而无法在当前 worktree 做带真实 API Key 的 `liveportrait-detect -> liveportrait` 实调

## 当前剩余最高优先级 blocker

- `liveportrait-detect -> liveportrait` 的真实线上验证

## 下一轮最关键一步

- 先补可用的 `config/formal_api_demo.local.toml`
- 用真实 API Key 跑一轮 `liveportrait-detect -> liveportrait` 实调
- 若真人开口分支实调通过，再只改 A 线的 demo 感和中段推进
