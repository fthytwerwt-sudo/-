# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-02 本轮已完成“配音压时长 + 重跑 preview”：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 本轮真实结果：
  - 整段配音已从上一轮约 `18.22s` 压到本轮约 `14.66s`
  - 本地 preview 已重新生成，时长仍为 `15.0s`
  - 当前不再是“整段配音长于 15 秒时间线并被整体截断”
- 当前 pipeline 仍未整体 success：
  - generation 继续因缺 `image_generation.model` / `video_generation.model` 记 `blocked`
  - 但这不是本轮“时长协同修正”的主问题

## 最近一次真正完成了什么

- 本轮只做了一个目标：
  - 把 `formal_api_demo` 当前本地样片里的“配音时长 > 15 秒时间线”问题压下去
- 本轮真实改动是：
  - 缩短了 `cases/formal_api_demo.md` 的三段配音 / 字幕文案
  - 给 `tests/test_formal_api_demo_pipeline.py` 增加了当前 case 的时间线预算回归测试
  - 重新生成了本地 preview 样片
- 当前可确认：
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  已是本轮新结果

## 质量审核结论

- 当前协同层比上一轮明显更稳：
  - 整段配音已回到 15 秒内
  - 结尾不再存在“因整段超时被硬截断”的主风险
- 当前仍有轻微残余：
  - `seg01` 实际约 `4.10s`，比预算多 `0.10s`
  - `seg02` 实际约 `6.07s`，比预算多 `0.07s`
  - `seg03` 实际约 `4.44s`，已回到预算内
- 当前 very small 质量结论：
  - “整段截断”已解除
  - 协同层主问题已改善
  - 但段内节奏还没完全贴合各自 slot

## 当前最关键下一步

- 不继续扩视觉模型或 cloud assembly。
- 下一轮如果只改一个点，优先改：
  - 继续把第 1 / 第 2 段各再收短一点，彻底消掉段内轻微超预算

## 新会话建议先读

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_timeline_alignment_round2.md`
- `cases/formal_api_demo.md`
- `tests/test_formal_api_demo_pipeline.py`
- `formal_api_demo_core.py`
