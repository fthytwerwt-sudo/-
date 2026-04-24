# latest_review_pack 审片入口

`已确认` 本包指向 `round33_正反展示提示卡补齐与风格统一`。

- 仓库相对路径：`dist/latest_review_pack/`
- 本地绝对路径：`/Users/fan/Documents/视频工厂/dist/latest_review_pack/`
- `codex/user-readable-map` 只同步默认接手口径与轻量 manifest / summary；完整视频产物与图片文件以 `codex/doubao-vnext-direct-fix-20260417` 分支为准。

## 本轮先看顺序

1. 先看 `反面展示提示卡_单帧.png`、`正面展示提示卡_单帧.png`、`正反提示卡_并排对比.png`
   - 判断正反提示卡是否统一为粉色樱花柔和展示牌风格，且为 9:16 竖屏重构。
2. 再看 `middle_preview.mp4`
   - 确认中段结构为：反面展示提示卡 -> 反面真实录屏 -> 正面展示提示卡 -> 正面真实录屏 -> 结果差提示卡。
3. 再看 `problem_windows/30_32s.mp4`
   - 确认 30-32 秒仍在正面真实录屏内部，新增正面提示卡没有替代证据。
4. 再看 `cut_contact_sheet.jpg`
   - 判断正反提示卡前后轻过渡是否降低跳屏感。
5. 最后看 `full.mp4`
   - 判断全片节奏；用户确认前不能写可发。

## 文件清单与中文备注

| 文件 | 中文备注 |
| --- | --- |
| `full.mp4` | round33 最新完整正片。 |
| `middle_preview.mp4` | round33 中段预览，用于快速检查正反提示卡与证据链。 |
| `before_after.mp4` | round32 与 round33 中段对比视频。 |
| `cut_contact_sheet.jpg` | 按镜头切点抽帧，方便判断跳屏、风格断裂、卡片过短。 |
| `反面展示提示卡_单帧.png` | 反面展示提示卡单帧图。 |
| `正面展示提示卡_单帧.png` | 正面展示提示卡单帧图。 |
| `正反提示卡_并排对比.png` | 两张提示卡并排对比图。 |
| `problem_windows/30_32s.mp4` | 30-32 秒问题窗口。 |
| `problem_windows/30_32s_frames.jpg` | 30-32 秒高频抽帧联系表。 |
| `audit/full_border_residue_report.md` | 全片边框残留扫描报告。 |
| `audit/full_jump_cut_report.md` | 全片跳切连续性扫描报告。 |
| `audit/border_residue_contact_sheet.jpg` | 全片边框残留抽帧联系表。 |
| `audit/jump_cut_contact_sheet.jpg` | 全片跳切抽帧联系表。 |
| `timeline.json` | round33 每个 segment / shot 的时间轴、承载方式、文件来源。 |
| `cut_map.md` | round33 逐镜头说明。 |
| `summary.json` | 写明 `technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`。 |
| `review_manifest.md` | 给 ChatGPT 的审片入口。 |

## 不得写成已完成的结论

- `content_validation` 不能因为技术扫描通过就写成通过。
- `send_ready` 必须保持 `no`，除非用户人工最终确认。
- 不得说云端剪辑链路已稳定跑通。
- 不得把提示卡写成中段主体证据；中段主体仍必须是用户真实录屏。

## 当前 validation

- `border_residue_validation`: 通过
- `jump_cut_validation`: 通过
- `technical_validation`: 通过：round33 已生成 full/middle/before_after/problem window，正反提示卡已补齐并完成边框残留与跳切连续性扫描。
- `content_validation`: 待用户 / ChatGPT 最终复审
- `send_ready`: no
