# Latest

## 当前主结论

- 2026-04-05 已按“质量基线交付”完成 30 秒 `hybrid` 正式母版成片（本地可复审）。
- 成片已落到本地路径：
  - `dist/formal_api_demo_30s_hybrid/final.mp4`
- 已同步输出回审帧：
  - `dist/formal_api_demo_30s_hybrid/review_frames/`
- 本轮成片保持真人承载 + 结构证据混合路线，非样片口径、非纯 PPT。

## 本轮核心判断

- `video_scene`: AI 项目讲解
- `video_route_strategy`: `hybrid`
- `primary_value`: 结构
- `audience_need_first`: 两者都要（先相信 + 先看懂）

## 本轮实际产物（本地）

- `dist/formal_api_demo_30s_hybrid/final.mp4`
- `dist/formal_api_demo_30s_hybrid/review_frames/`
- `dist/formal_api_demo_30s_hybrid/review_record.md`
- `dist/formal_api_demo_30s_hybrid/result_summary.json`

> 以上产物属于 `local_only`，已在 `.gitignore` 中屏蔽，不会上传 GitHub。

## 本轮关键执行事实

- 真人段与结构证据段均真实生成视频资产，已组成 28.57 秒成片。
- 阿里百炼 TTS 与视频生成出现 `Arrearage` 拦截，导致本轮后段无法继续新调接口；
  - 已复用本轮已落地音频与真人小样，避免链路回退成纯 PPT。
- Swift 本地装配在 `process` 页遇到数组越界，已改用 ffmpeg 拼接 + 字幕烧录，成片稳定落地。

## 本轮实际改动（仓库内）

- 新增 30 秒 hybrid 母版输入：
  - `cases/formal_api_demo_30s_hybrid.md`
- 新增/更新正式母版执行脚本与逻辑：
  - `formal_hybrid_master.py`
  - `scripts/render_formal_api_demo_30s_hybrid.py`
- 新增测试覆盖：
  - `tests/test_formal_hybrid_master.py`
- 更新 `.gitignore`：
  - `dist/formal_api_demo_30s_hybrid/` 标记为 `local_only`

## 下一步建议

- 若要把本轮结果作为“仓库正式事实”，需在 `codex/user-readable-map` 回流分支同步。
- 若要继续提升一致性，建议修复 Swift 装配对 `process` 页芯片数量的约束。
