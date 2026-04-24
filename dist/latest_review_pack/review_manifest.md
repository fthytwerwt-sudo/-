# latest_review_pack 审片入口

`已确认` 本包指向 `round32_全片边框残留与跳切连续性修复`。

- 仓库相对路径：`dist/latest_review_pack/`
- 本地绝对路径：`/Users/fan/Documents/视频工厂/dist/latest_review_pack/`

## 本轮先看顺序

1. 先看 `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round32_全片边框残留与跳切连续性修复/audit/full_border_residue_report.md`
   - 判断 round31 绿色边框定位是否完整，round32 复扫是否仍有候选。
2. 再看 `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/round32_全片边框残留与跳切连续性修复/audit/full_jump_cut_report.md`
   - 判断 37-39s 跳屏 / 连续插图感是否已被轻过渡消解。
3. 再看 `problem_windows/30_32s.mp4`
   - 确认原 30-32s 证据链窗口仍落在正面真实录屏内部。
4. 再看 `middle_preview.mp4`
   - 确认中段主体仍由用户录制素材承担，反面 / 正面证据链未被破坏。
5. 最后看 `full.mp4`
   - 判断全片边框残留、跳切连续性和整体节奏；用户确认前不能写可发。

## 文件清单与中文备注

| 文件 | 中文备注 |
| --- | --- |
| `full.mp4` | 最新完整正片。 |
| `middle_preview.mp4` | 最新中段预览，用于快速检查证据链。 |
| `before_after.mp4` | 上一轮和本轮对比视频。 |
| `cut_contact_sheet.jpg` | 按每个镜头切点抽关键帧，方便判断跳屏、风格断裂、卡片过多。 |
| `problem_windows/30_32s.mp4` | 截出用户反馈有跳屏感的 30-32 秒问题窗口。 |
| `problem_windows/30_32s_frames.jpg` | 30-32 秒逐帧 / 高频抽帧联系表，用于判断是否有硬插图、连续贴片、跳屏。 |
| `timeline.json` | 每个 segment / shot 的开始时间、结束时间、承载方式、文件来源。 |
| `cut_map.md` | 逐镜头说明每一段是 API 生成真人、用户录制素材、卡片、总结卡，还是 Prompt 尾卡。 |
| `summary.json` | 写明 `technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`。 |
| `review_manifest.md` | 给 ChatGPT 的审片入口，说明先看哪个文件、重点判断什么、哪些结论不能写成已完成。 |

## 不得写成已完成的结论

- `content_validation` 不能因为技术扫描通过就写成通过。
- `send_ready` 必须保持 `no`，除非用户人工最终确认。
- 不得说云端剪辑链路已稳定跑通。
- 不得把卡片写成中段主体证据；中段主体仍必须是用户真实录屏。

## 当前 validation

- `border_residue_validation`: 通过
- `jump_cut_validation`: 通过
- `technical_validation`: 通过：round32 已生成，full/middle/problem window 已产出，全片边框残留扫描与跳切连续性扫描已完成。
- `content_validation`: 待用户 / ChatGPT 最终复审
- `send_ready`: no
