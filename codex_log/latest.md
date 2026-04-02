# Latest

## 当前 formal_api_demo 执行状态

- 2026-04-02 本轮已真实重跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
- 当前结果不是“主链没跑起来”，而是：
  - generation 真实落出了脚本、字幕、整段配音
  - local assembly 真实落出了本地 preview mp4
  - 但 `image_generation.model` / `video_generation.model` 仍缺，generation 继续记为 `blocked`
  - cloud assembly 仍是后续增强项，不是这轮本地样片落地的主阻塞
- 当前产物状态：
  - `dist/formal_api_demo/script.txt`
  - `dist/formal_api_demo/captions.srt`
  - `dist/formal_api_demo/tts/formal_voiceover.mp3`
  - `dist/formal_api_demo/assembly/formal_api_demo_preview.mp4`
  均已真实存在，可作为首轮质量审核输入

## 最近一次真正完成了什么

- 本轮没有继续补机制文件，也没有继续改 `project_source/`。
- 本轮真实完成的是：
  - 重跑了 `formal_api_demo` 本地主链
  - 重新落出一版本地可审样片
  - 做了一轮执行审核 + 质量审核
- 执行审核结论：
  - 当前属于“部分完成”
  - 本地可审样片已重新生成
  - 整体状态仍 blocked，最小执行阻塞已压清到：
    - `image_generation.model`
    - `video_generation.model`

## 质量审核结论

- 当前样片还没有达到“可发布测试”水位。
- 当前最大问题层不在 cloud assembly，而在：
  - 字幕 / 配音 / 画面协同层
- 本轮已确认的最关键质量事实：
  - `formal_voiceover.mp3` 实际时长约 `18.22s`
  - `formal_api_demo_preview.mp4` 实际时长是 `15.0s`
  - 三段配音都超出各自时间预算，当前 preview 合成会按较短时长截断音频
- 同时仍存在明显 demo 感：
  - 本地 preview 仍是静态卡片轮播
  - 画面里仍显式保留 `PPT Demo` / `formal_api_demo / 本地预览` 标识

## 当前最关键下一步

- 不再回头补机制文件。
- 下一轮如果只改一个点，优先改：
  - 把整段配音和 15 秒时间线压齐，先解决字幕 / 配音 / 画面协同失真问题
- 补齐视觉模型配置仍是执行层最小阻塞，但按质量收益排序，不是下一轮唯一最值改点。

## 新会话建议先读

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_log/20260402_formal_api_demo_dual_review_round1.md`
- `formal_api_demo_core.py`
- `video_builder.swift`
- `cases/formal_api_demo.md`
