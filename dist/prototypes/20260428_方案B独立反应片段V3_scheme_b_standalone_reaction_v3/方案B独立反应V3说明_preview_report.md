# 方案 B 独立反应片段 V3 说明

## 本轮状态

- `已确认` 本轮目标是把 V2 的本地绘图 + overlay 路线改为高质量模型生成 + 独立 reaction clip 路线。
- `已确认` 本轮已完成分支、round34、V2 问题和阿里模型能力排查。
- `已确认` 本轮未生成 V3 视频，因为 DashScope 图像生成创建任务返回 `HTTP401 / InvalidApiKey`。
- `已确认` 本轮状态为：`blocked`。

## 已尝试模型

- `wan2.7-image-pro`：失败，`HTTP401 / InvalidApiKey`
- `wan2.7-image`：失败，`HTTP401 / InvalidApiKey`
- `wan2.7-i2v`：未执行，因为静态反应图生成阶段已失败

## 本轮已输出文件

- `问题诊断_report.md`
- `run_summary.json`
- `wan_generation_attempts_sanitized.json`
- `方案B独立反应V3说明_preview_report.md`

## 本轮未输出文件

- `方案B独立反应页_static_reaction_page.png`
- `方案B独立反应片段_reaction_clip.mp4`
- `方案B独立反应15秒预览_scheme_b_standalone_reaction_v3.mp4`
- `方案B独立反应15秒预览_contact_sheet.jpg`

## 状态边界

- `已确认` 是否改 full：否
- `已确认` 是否改 `dist/latest_review_pack/`：否
- `已确认` 是否改 `content_validation`：否
- `已确认` 是否改 `send_ready`：否
- `已确认` 是否确定最终口径：否

## 下一步

- `待验证` 重新配置可用 DashScope / 百炼 key 后，再执行 V3 生成。
- `待验证` 生成成功后，再交给 ChatGPT / 用户复审画质、表情和独立插入节奏。
