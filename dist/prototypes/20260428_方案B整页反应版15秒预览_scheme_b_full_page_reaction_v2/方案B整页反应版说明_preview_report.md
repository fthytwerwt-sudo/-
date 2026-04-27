# 方案 B 整页反应版 15 秒技术预览 V2 说明

## 1. 本轮定位

- `已确认` 本轮只生成 `方案 B：AI向导崩溃模式` 的整页 reaction 技术预览 V2。
- `已确认` 本轮只验证画面层方向：人物表情、搞笑强度、插入节奏。
- `已确认` 本轮不是最终成片修改，不代表方案 B 最终口径。
- `已确认` 本轮不做 `content_validation（内容验证）` 通过判断，不更新 `send_ready（可发送状态）`。

## 2. 分支与事实源校准

- `已确认` 执行工作区：`/private/tmp/视频工厂_user_readable_map_sync`
- `已确认` 校准起点分支：`codex/user-readable-map`
- `已确认` V2 任务分支：`codex/scheme-b-full-page-reaction-v2-20260428`
- `已确认` `dist/latest_review_pack/summary.json` 指向：`round34_中段双展示提示卡_正反分段提示修复`
- `已确认` `middle_segment_review = 用户暂定通过 / 暂不继续修改中段`
- `已确认` `content_validation = 待用户 / ChatGPT 最终复审`
- `已确认` `send_ready = false`

## 3. 底片来源

- `已确认` 使用底片：`dist/latest_review_pack/middle_preview.mp4`
- `已确认` 该底片来自当前 round34 审片包，不是 round32。
- `已确认` 预览截取范围：从 `middle_preview.mp4` 的 `1.6s` 起截取 `15.0s`。
- `已确认` 这样处理后，预览开头直接进入反面录屏结果，避免只展示 round34 的《反面展示》提示卡。

## 4. 15 秒结构

| 预览时间 | 画面职责 | 说明 |
| --- | --- | --- |
| `0.0s-4.52s` | 反面录屏结果露出 | 先让观众看到普通问法生成的空泛结果。 |
| `4.52s-5.92s` | 整页人物搞笑反应 | 切到整页 AI 向导崩溃 reaction 页，大字为 `方案很满 / 用起来空`。 |
| `5.92s-约9.7s` | 回到录屏主线 | reaction 结束后回到反面录屏证据链。 |
| `约9.7s-15.0s` | 正面转向 | 进入 round34《正面展示》提示卡和正面录屏开头。 |

## 5. 整页 reaction 设计

- `已确认` V2 是整页 reaction 插入，不是角落贴图。
- `已确认` 人物胸口没有 `AI` 标识，身上没有文字 logo。
- `已确认` 人物为原创 Q 版 AI 向导，不使用真实人物、不使用受版权保护角色、不照抄对标视频人物。
- `已确认` 表情包含：X 眼、旋涡眼、大张嘴、崩溃泪、双手抱头、头顶 `!?`、汗滴、手足无措姿势、轻微震动 / bounce。
- `已确认` 背景为黄 / 橙色放射线和速度线，并保留一层模糊暗化的录屏背景作为上下文。
- `已确认` 动效为 0.15s 左右 punch-in、轻微 bounce / 震动、随后快速切回录屏。

## 6. 输出文件

- `方案B整页反应版15秒预览_scheme_b_full_page_reaction_v2.mp4`
- `方案B整页反应页_full_page_reaction.png`
- `方案B整页反应页_透明人物层_character_alpha.png`
- `方案B整页反应版_contact_sheet.jpg`
- `方案B整页反应版_before_after_contact_sheet.jpg`
- `run_summary.json`

## 7. 验证口径

- `已确认` ffmpeg 解码通过。
- `已确认` 输出视频时长为 `15.00s`。
- `已确认` 输出视频分辨率为 `720x1280`。
- `已确认` 整页 reaction 出现窗口为 `4.52s-5.92s`，持续 `1.40s`，未超过 2 秒。
- `已确认` 预览结构为：反面结果露出 -> 整页人物搞笑反应 -> 回到录屏主线 -> 正面做法开头。
- `已确认` 本轮不改 `full.mp4`、不生成正式新 round、不修改 `dist/latest_review_pack/`、不修改 `content_validation`、不修改 `send_ready`。

## 8. 待复审项

- `待验证` 整页 reaction 是否比上一版角落贴图更接近用户想要的搞笑反应插入。
- `待验证` 人物表情强度、画质、形象方向和插入节奏仍需 ChatGPT / 用户复审。
- `待验证` 本轮不判断方案 B 是否进入正式正片。
