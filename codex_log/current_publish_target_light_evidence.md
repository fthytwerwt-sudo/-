# Current Publish Target Light Evidence

## 对应对象

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`round34_中段双展示提示卡_正反分段提示修复`
- 当前完整正片：`dist/latest_review_pack/full.mp4`
- 当前中段预览：`dist/latest_review_pack/middle_preview.mp4`
- 当前审片入口：`dist/latest_review_pack/review_manifest.md`

## 历史对象

- 历史待发对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 历史云端正式输出：`oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`
- 当前解释：该对象只代表 20260412 当时口径下的历史通过样片，不再是当前最新复审 target。

## Git 可追踪轻量证据包

1. `dist/latest_review_pack/review_manifest.md`
   - 当前 ChatGPT / 用户复审入口。
   - 明确复审顺序：先看正反提示卡关键帧，再看 `middle_preview.mp4`、切点联系表和 full。
2. `dist/latest_review_pack/summary.json`
   - 当前 round34 验证状态摘要。
   - 可直接确认：
     - `border_residue_validation = 通过`
     - `jump_cut_validation = 通过`
     - `technical_validation = 通过`
     - `content_validation = 待用户 / ChatGPT 最终复审`
     - `send_ready = false`
3. `dist/latest_review_pack/timeline.json`
   - 当前 segment / shot 时间轴与承载方式。
   - 可直接确认中段顺序：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
4. `dist/latest_review_pack/cut_map.md`
   - 当前逐镜头承载说明。
   - 可直接确认反面 / 正面录屏源时间码保持不变。
5. `dist/latest_review_pack/图二参考图.png`
   - 用户本轮同步的图二参考图副本，尺寸 `908x492`。
6. `dist/latest_review_pack/反面展示提示卡_单帧.png`
   - 反面展示提示卡 9:16 单帧，尺寸 `720x1280`。
7. `dist/latest_review_pack/正面展示提示卡_单帧.png`
   - 正面展示提示卡 9:16 单帧，尺寸 `720x1280`。
8. `dist/latest_review_pack/正反提示卡_并排对比.png`
   - 正反提示卡统一风格对比图。
9. `dist/latest_review_pack/middle_preview.mp4`
   - 中段快速复审视频。
10. `dist/latest_review_pack/full.mp4`
   - round34 完整正片。
11. `dist/latest_review_pack/before_after.mp4`
   - round33 与 round34 中段对比视频。
12. `dist/latest_review_pack/cut_contact_sheet.jpg`
   - round34 全片切点联系表。
13. `dist/latest_review_pack/problem_windows/30_32s.mp4`
   - 当前保留的 30-32 秒问题窗口。
   - 该窗口仍落在正面真实录屏内部。
14. `dist/latest_review_pack/problem_windows/30_32s_frames.jpg`
   - 30-32 秒高频抽帧联系表。
15. `dist/latest_review_pack/audit/full_border_residue_report.md`
   - round34 全片边框残留报告。
16. `dist/latest_review_pack/audit/full_jump_cut_report.md`
   - round34 全片跳切连续性报告。
17. `dist/latest_review_pack/audit/border_residue_contact_sheet.jpg`
   - round34 全片边框残留抽帧联系表。
18. `dist/latest_review_pack/audit/jump_cut_contact_sheet.jpg`
   - round34 全片跳切抽帧联系表。
19. `scripts/元素娃娃线_round34_中段双展示提示卡_正反分段提示修复.py`
   - round34 局部修复生成脚本。
20. `scripts/视频全片边框与跳切审计.py`
   - 本轮继续使用的边框残留与跳切审计脚本。
21. `codex_log/20260425_round34_中段双展示提示卡_正反分段提示修复.md`
   - round34 生成、修复、验证与口径同步日志。

## 这些轻量证据共同证明什么

- 当前最新复审对象是谁：
  - `dist/latest_review_pack/`
- 当前审片包指向哪一轮：
  - `round34_中段双展示提示卡_正反分段提示修复`
- 当前中段结构是什么：
  - 反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡
- 当前技术状态是什么：
  - `technical_validation（技术验证）`：`通过`
  - `border_residue_validation（边框残留验证）`：`通过`
  - `jump_cut_validation（跳切连续性验证）`：`通过`
- 当前内容状态是什么：
  - `content_validation（内容验证）`：`待用户 / ChatGPT 最终复审`
  - `send_ready（可直接发送）`：`no`
- 当前证据链原则是什么：
  - 中段主体仍由用户真实录屏承担。
  - 卡片 / PPT / 图片只允许辅助解释，不允许替代证据。
  - 新增 / 重构提示卡不能替代正面或反面真实录屏。
- 当前不能证明什么：
  - 不能证明 round34 已经可直接发送。
  - 不能证明 `content_validation` 已通过。
  - 不能证明 `云端剪辑` runtime 已稳定跑通。

## 当前本地审片包

- `/Users/fan/Documents/视频工厂/dist/latest_review_pack/`
- `dist/latest_review_pack/`

## 为什么仍保留历史 20260412 证据

- 20260412 是当时口径下的历史通过样片。
- 历史日志不删除，继续用于追溯旧判断。
- 当前复审 target 已切到 round34，不得再用 20260412 冒充当前最新可发样片。

## 当前一句话

- 当前最新复审对象是 `dist/latest_review_pack/`，指向 `round34_中段双展示提示卡_正反分段提示修复`；技术扫描通过不等于内容最终过线，`content_validation = 待用户 / ChatGPT 最终复审`，`send_ready = no`。
