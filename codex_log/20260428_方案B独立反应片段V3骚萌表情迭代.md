# 20260428｜方案 B 独立反应片段 V3 骚萌表情迭代

## 本轮性质

- `已确认` 本轮只做方案 B V3 独立 reaction clip 的角色表情 / 动作气质迭代。
- `已确认` 本轮不是最终成片修改，不代表方案 B 最终口径。
- `已确认` 本轮不代表 `content_validation` 通过，不代表 `send_ready` 更新。

## 配置预检

- `已确认` 实际读取配置路径：`/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- `已确认` 脱敏 preflight 通过：`provider = aliyun_bailian`，`region = cn-beijing`。
- `已确认` key 存在，形态为 `sk_dashscope_like`，长度范围为 `20-39`。
- `已确认` 本轮未打印、写入或提交完整 key。

## 图像候选

- `已确认` 图像模型：`wan2.7-image-pro`。
- `已确认` 生成 2 张候选，未超过本轮限制。
- A 版：
  - 路径：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌A_static_reaction_page.png`
  - `task_id = 0e572645-7897-412c-a82a-9fdf0dbd13e3`
  - `request_id = fe31cbcb-a834-94b6-b52a-f4a8d17ab335`
  - 视觉特征：挑眉、wink、捂嘴偷笑、得瑟手势。
- B 版：
  - 路径：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌B_static_reaction_page.png`
  - `task_id = 1e0bb603-4978-48cc-8c29-358297faae0b`
  - `request_id = eaa3dec2-b5dc-92de-91fc-76dd0912f6a0`
  - 视觉特征：吐舌、歪头、手势更夸张。
- `已确认` 选中 A 版进入 i2v；理由：A 版更接近“贱萌 / 得瑟 / 小坏笑”，且不低幼、不暧昧、胸口无 `AI`；B 版吐舌更强但略偏低幼 / 暧昧。

## 图生视频与预览

- `已确认` 图生视频模型：`wan2.7-i2v`。
- `已确认` 图生视频任务已创建并完成：
  - `task_id = 00843322-0685-4eb2-a2ca-d9802ddc11b0`
  - `request_id = bb5a7a91-d3f9-9588-8aa6-1c7cd10ab680`
  - 输出：`dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip.mp4`
- `已确认` 15 秒骚萌版预览已生成：
  - `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_scheme_b_standalone_reaction_v3_sassy_cute.mp4`
  - 结构：`round34 录屏片段 A -> 骚萌独立 reaction clip -> round34 录屏片段 B`
  - 不是角落贴图，不是录屏 overlay compositing。

## 技术验证

- `已确认` 预览视频可被 ffmpeg 解码。
- `已确认` reaction clip 可被 ffmpeg 解码。
- `已确认` 预览视频：`15.00s / 720x1280 / silent_preview`。
- `已确认` 独立 reaction clip：`1.52s / 720x1280`。
- `已确认` 当前 round 仍为 `round34_中段双展示提示卡_正反分段提示修复`。
- `已确认` 未修改 `full.mp4`、`dist/latest_review_pack/`、`content_validation`、`send_ready`。

## 输出文件

- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/run_summary.json`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3说明_preview_report.md`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应V3_prompts.json`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/sassy_expression_candidates_result_sanitized.json`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应页_骚萌候选对比_contact_sheet.jpg`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应片段_骚萌_reaction_clip.mp4`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_scheme_b_standalone_reaction_v3_sassy_cute.mp4`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_contact_sheet.jpg`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/方案B独立反应15秒预览_骚萌版_before_after_contact_sheet.jpg`

## 边界

- `已确认` 未泄露 key。
- `已确认` 未提交本地私有配置文件。
- `已确认` 未使用本地 Mac 程序绘制角色。
- `已确认` 未改正式正片。
- `已确认` 未改当前审片包。
- `已确认` 未改 `content_validation`。
- `已确认` 未改 `send_ready`。
- `待验证` 本轮只是 `technical_preview_generated_content_pending`，仍待 ChatGPT / 用户复审“骚萌表情、GIF 感、插入节奏、是否能进入正式方案”。
