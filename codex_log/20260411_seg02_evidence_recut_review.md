# 2026-04-11 seg02 证据段重剪复核

## 本轮目标

- 只改当前待发样片的 `seg02`
- 不改 `seg01`
- 不改 `seg03`
- 不扩规则
- 至少完成一次新的生成 / 组装 / 导出，并重新做内容复核

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_log/latest.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260411_latest_sample_publish_line_review.md`
- `cases/formal_api_demo_user_footage_execution_20260409.md`
- `dist/formal_api_demo_user_footage_20260409/{manifest.json,route_plan.json,script.txt,captions.srt,result_summary.json}`
- 本地重证据：
  - `dist/formal_api_demo_user_footage_20260409/final.mp4`
  - `dist/formal_api_demo_user_footage_20260409/assembly/formal_api_demo_preview.mp4`
  - `素材录制/1.mov`

## skill 检查

- `已确认` 仓库本地 `skills/`：不存在。
- `已确认` 全局 `~/.codex/skills` 已检查并实际采用：
  - `using-superpowers`
  - `context-driven-development`
  - `verification-before-completion`
- `部分成立` `visual-verdict` 已检查，但本轮没有可用 reference image，不能按它的标准 JSON 回路作为权威判定；因此改用关键帧 + OCR + manifest/assembly_plan 实读做复核。

## 当前问题诊断

- `已确认` 原始 `1.mov` 是 3366x2180 宽录屏。
- `已确认` 旧版 `seg02` 直接把宽录屏缩进 9:16，导致：
  - 上下黑边过大
  - 有效信息面积过小
  - 观众只能知道“这里有录屏”，看不清“你在压清什么”
- `已确认` 当前拖后腿的不是路线，而是 `seg02` 证据镜头没有被证据化。

## 本轮实际改动

### 1. 输入稿与轻量证据更新

- 更新 `cases/formal_api_demo_user_footage_execution_20260409.md`
  - 把 `seg02` 的画面意图改成已锁定的 Beat A / B / C 结构。
- 更新 `dist/formal_api_demo_user_footage_20260409/route_plan.json`
  - 让 `seg02` 的 `visual_intent` 与 Beat A / B / C 对齐。
- 更新 `dist/formal_api_demo_user_footage_20260409/manifest.json`
  - `seg02` 的 `visual_uri` 与 `video_asset_path` 改为本轮新 clip。

### 2. 本轮新生成的 `seg02` 证据版 clip

- 新本地 clip：
  - `dist/formal_api_demo_user_footage_20260409/visual/seg02_evidence_focus_v3.mp4`
- 处理方式只围绕 `seg02`：
  - 竖裁
  - 放大
  - 分拍拼接
  - 轻量标签
- 实际 beat 结构：
  - Beat A：先给“没压清前”
  - Beat B：把 `目标 / 边界 / 验收` 分拍显影
  - Beat C：收在“压清后再交给 AI”

### 3. 新的组装 / 导出

- 已重新执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo_user_footage_20260409/manifest.json --out dist/formal_api_demo_user_footage_20260409`
- 本轮新的云端输出：
  - `oss://zvip1-video-beijing/video-factory/final/20260410T202608Z/formal_api_demo.mp4`
- 当前本地成片路径仍是：
  - `dist/formal_api_demo_user_footage_20260409/final.mp4`

## 新证据

- `已确认` `assembly_plan.json` 已明确使用：
  - `dist/formal_api_demo_user_footage_20260409/visual/seg02_evidence_focus_v3.mp4`
- `已确认` 新 clip 元信息：
  - 时长 `9.28s`
  - 分辨率 `1080x1920`
- `已确认` 新成片元信息：
  - 时长 `15.00s`
  - 分辨率 `1080x1920`
  - `generation_status = success`
  - `assembly_status = success`
  - `cloud_assembly_status = success`
- `已确认` 对新 clip 关键帧做 OCR 时，已经能稳定读到：
  - `process_self_footage`
  - `formal_api_demo.local.toml`
  - `gpt_chat_screen_recording.mp4`
  - `result_card.png`
  说明当前证据段已经不再只是“录屏占位”，而是能看出你在整理固定交接槽位与本地配置边界。

## 正式复核结论

### `technical_validation`

- `已确认` 通过

理由：
- 新的 `seg02` 证据 clip 已真实生成
- 新 manifest 已真实改写
- 新的 assembly / export 已完成
- 本地 `final.mp4` 仍成功落地

### `content_validation`

- `已确认` 未通过

理由：
- 旧问题“黑边过大、信息太小、录屏只是占位”已经明显改善
- 但当前 `seg02` 仍主要是把已有同一份聊天录屏做成更可读的证据段
- 现有 `1.mov` 本体没有足够强的“同一任务从混乱到清单化”的原生前后差值
- 因此观众现在更容易看懂“你在压清”，但还没强到“一眼就懂这同一任务已经从不能直接交给 AI，变成可直接交接”

## 当前唯一最高优先级 blocker

- `已确认` 当前唯一最高优先级 blocker：
  - 现有 `1.mov` 缺足够强的同任务前后差值，`seg02` 已摆脱黑边占位，但还需要更硬的“旧状态 -> 压清动作 -> 可直接交接状态”原始录屏素材，才能真正冲过发布线。

## `seg02` 现在具体改善了什么

1. 不再是整屏小录屏加大黑边，主体内容已经明显放大。
2. 不再只是“有录屏”，而是已经通过分拍和标签把 `目标 / 边界 / 验收` 拆出来。
3. 已经能在关键帧里看清 `process_self_footage`、`formal_api_demo.local.toml`、素材文件名这些具体交接信息。
4. 已经更接近“证据段”，不再只是“录屏占位”。

## 当前样片路径

- 当前本地样片：
  - `dist/formal_api_demo_user_footage_20260409/final.mp4`
- 当前本地 `seg02` 证据版 clip：
  - `dist/formal_api_demo_user_footage_20260409/visual/seg02_evidence_focus_v3.mp4`

## 同步说明

- `current_publish_target.md`：已刷新
- `current_publish_target_light_evidence.md`：已刷新
- `latest.md`：已刷新
- 本日志：已新增

## 当前状态分类

- `formal_synced`
