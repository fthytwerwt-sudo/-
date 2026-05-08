# 20260405_正式母版_30s_hybrid

## 一句话结论

本轮已完成 30 秒 `hybrid` 正式母版成片，真人承载 + 结构证据均真实落地，本地可复审。

## 本轮目标与约束

- 时长：约 30 秒（实际 28.57 秒）
- 路由：`hybrid`
- 必须包含：真人承载段 + 结构证据段
- 质量基线：开头 3 秒有效、非说明书、前后变化可见、结尾有落点、配音/字幕同步

## 路由判断

- `video_scene`: AI 项目讲解
- `video_goal`: 让观众一眼看懂卡点不是 prompt，而是没有可交接 SOP 链路，并给最小行动
- `primary_value`: 结构
- `audience_need_first`: 两者都要
- `video_route_strategy`: `hybrid`

### Block 路由表

| block_id | block_goal | block_need_first | block_carrier | asset_requirement | why_this_carrier |
|---|---|---|---|---|---|
| block_01 | 抓手/判断/进入感 | 代入+相信 | human | 真人承载视频 | 开头先建立判断感与可信度 |
| block_02 | 结构证据/对比 | 看懂 | mixed | 结构证据视频 + 卡片字幕 | 让前后变化肉眼可见 |
| block_03 | 收束/最小行动 | 行动+相信 | human_with_overlay | 真人收束视频 | 结尾给行动与掌控感 |

## 实际执行与产物

### 本地成片

- `dist/formal_api_demo_30s_hybrid/final.mp4`
- `dist/formal_api_demo_30s_hybrid/review_frames/`

### 过程文件

- `dist/formal_api_demo_30s_hybrid/script.txt`
- `dist/formal_api_demo_30s_hybrid/captions.srt`
- `dist/formal_api_demo_30s_hybrid/timeline.json`
- `dist/formal_api_demo_30s_hybrid/result_summary.json`
- `dist/formal_api_demo_30s_hybrid/review_record.md`

## 真实阻断与处理

1. **阿里百炼 TTS / 视频生成 `Arrearage`**
   - TTS 与视频接口出现余额拦截，后续请求无法继续。
   - 已复用本轮已落地的配音与真人小样，避免降级成纯 PPT。
2. **Swift 装配崩溃**
   - `process` 页 chips 数量过多导致 `Index out of range`。
   - 采用 ffmpeg 拼接 + 字幕烧录完成成片交付。

## 重要新增/修改文件

- `cases/formal_api_demo_30s_hybrid.md`
- `formal_hybrid_master.py`
- `scripts/render_formal_api_demo_30s_hybrid.py`
- `tests/test_formal_hybrid_master.py`
- `.gitignore`（新增 `dist/formal_api_demo_30s_hybrid/`）
- `codex_log/latest.md`

## local_only 说明

- `dist/formal_api_demo_30s_hybrid/` 属于 `local_only`，已在 `.gitignore` 中屏蔽，不会上传 GitHub。
- 本地成片与回审帧已生成，可直接复审。

## 后续建议

- 若需把本轮结果作为“仓库正式事实”，需要同步回 `codex/user-readable-map`。
- 若需恢复 Swift 装配链路，建议修复 `process` 页 chips 越界逻辑。
