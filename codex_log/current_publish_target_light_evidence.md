# Current Publish Target Light Evidence

## 对应对象

- 当前待发对象：`dist/formal_api_demo_user_footage_20260409/final.mp4`
- 当前审核对象：`dist/formal_api_demo_user_footage_20260409/final.mp4`

## Git 可追踪轻量证据包

1. `cases/formal_api_demo_user_footage_execution_20260409.md`
   - 当前样片执行输入稿。
   - 本轮根据 `manifest.json` 与现有样片证据 grounded 补回。
2. `dist/formal_api_demo_user_footage_20260409/manifest.json`
   - 完整执行快照。
   - 可直接看到输入快照、主线口径、段落职责、素材来源、segment timeline。
3. `dist/formal_api_demo_user_footage_20260409/route_plan.json`
   - 当前样片的 carrier 分发结果。
   - 可直接确认 `seg01 = human`、`seg02 = self_footage`、`seg03 = light_ppt`。
4. `dist/formal_api_demo_user_footage_20260409/script.txt`
   - 当前样片最短脚本摘要。
   - 可快速确认 3 段文案结构。
5. `dist/formal_api_demo_user_footage_20260409/captions.srt`
   - 当前样片字幕与时长切分。
   - 可快速确认 `3s / 9s / 3s` 节奏。
6. `dist/formal_api_demo_user_footage_20260409/result_summary.json`
   - 机器侧结果摘要。
   - 可直接确认 `overall_status = success` 与 `cloud_assembly_status = success`。
7. `codex_log/20260411_latest_sample_publish_line_review.md`
   - 当前正式发布线复核结论。
   - 可直接确认：`technical_validation 通过，content_validation 未通过`。
8. `codex_log/20260411_seg02_evidence_recut_review.md`
   - 当前 `seg02` 局部改片后的复核结论。
   - 可直接确认：本轮已发生真实改动、已重新组装导出，但 `content_validation` 仍未通过。

## 这些轻量证据共同证明什么

- 当前样片是谁：
  - `dist/formal_api_demo_user_footage_20260409/final.mp4`
- 当前样片结构是什么：
  - `API 生成真人 -> 用户录制素材 -> 少量 PPT`
- 当前样片技术状态是什么：
  - generation / assembly / cloud assembly 均成功
- 当前样片为什么没过发布线：
  - 不是路由没分对
  - 而是 `seg02` 的竖版证据呈现没让观众看清真实过程

## 当前 `local_only` 重证据

- `dist/formal_api_demo_user_footage_20260409/final.mp4`
  - 当前最新样片成片。
- `dist/formal_api_demo_user_footage_20260409/assembly/formal_api_demo_preview.mp4`
  - 本地预览成片。
- `dist/formal_api_demo_user_footage_20260409/visual/seg02_evidence_focus_v3.mp4`
  - 本轮 `seg02` 重剪后的证据版 clip。
- `素材录制/1.mov`
  - 当前 `seg02` 证据段直接引用的原始录屏素材。

## 为什么这轮不追踪更多二进制

- `final.mp4` 和原始录屏素材都属于重二进制。
- 当前目标是让新聊天先靠 Git 可追踪轻量证据快速锁定对象、结构、状态和 blocker，而不是把整条片子的二进制同步进仓库。

## 输入稿缺口处理

- `manifest.json` 原始指向：
  - `cases/formal_api_demo_user_footage_execution_20260409.md`
- 本轮处理：
  - 已按 `manifest.json` 的 `input_snapshot`、`video_spec`、`presentation_routing` 与 `segments` grounded 补回该输入稿。
- 若后续发现与历史原稿不一致：
  - 以当前已追踪的 `manifest.json` 和 dated log 为准，继续做证据级修正，不回头伪造“原始历史文件”。

## 本轮 `seg02` 实际改片落点

- 当前 manifest / assembly_plan 已改为使用：
  - `dist/formal_api_demo_user_footage_20260409/visual/seg02_evidence_focus_v3.mp4`
- 这个 clip 的实际处理只围绕 `seg02`：
  - 竖裁
  - 放大
  - 分拍拼接
  - 轻量标签
- 没有新增人物段
- 没有改 `seg01`
- 没有改 `seg03`
