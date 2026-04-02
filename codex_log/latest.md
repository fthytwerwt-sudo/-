# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-02 本轮已完成 `seg01 / seg02` 单段时间线对齐 round3：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 本轮真实结果：
  - `seg01` 已压到约 `3.94s`，回到 `4.0s` slot 内
  - `seg02` 已压到约 `5.64s`，回到 `6.0s` slot 内
  - `seg03` 约 `4.44s`，仍在 `5.0s` slot 内
  - 整段配音约 `14.06s`
  - 本地 preview 已重新生成，时长仍为 `15.0s`
- 当前已不再存在“单段轻微超预算”的协同尾巴。
- 当前 pipeline 仍未整体 success：
  - generation 继续因缺 `image_generation.model` / `video_generation.model` 记 `blocked`
  - 但这不是本轮 `seg01 / seg02` 时间线修正的剩余问题

## 最近一次真正完成了什么

- 本轮只做了一个 very small fix：
  - 继续把 `formal_api_demo` 的第 1 / 第 2 段配音再收短一点，让每段都完全回到各自 slot 内
- 本轮真实改动是：
  - 再次微缩了 `cases/formal_api_demo.md` 的 `seg01 / seg02` 文案
  - 把 `tests/test_formal_api_demo_pipeline.py` 的当前 case 预算测试继续收紧到 `seg01=22`、`seg02=29`
  - 重新生成了本地 preview 样片
- 当前可确认：
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  已是本轮新结果

## 质量审核结论

- 本轮只审“协同层尾巴”。
- 当前主结论：
  - `seg01 / seg02` 的单段超预算尾巴已经清干净
  - 字幕 / 配音 / slot 的贴合度比上一轮更稳
  - 当前不再存在“段内轻微超预算”导致的节奏尾巴

## 当前最关键下一步

- 不继续扩视觉模型或 cloud assembly。
- 协同层尾巴清掉后，下一轮如果只改一个点，优先切到：
  - 画面层，先降低当前本地 preview 的 demo / 静态卡片感，尤其是第 1 段 hook 的画面表达

## 新会话建议先读

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_timeline_alignment_round3.md`
- `cases/formal_api_demo.md`
- `tests/test_formal_api_demo_pipeline.py`
- `formal_api_demo_core.py`
