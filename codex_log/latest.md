# Latest

## 20260425｜round33 正反展示提示卡补齐与风格统一

- `已确认` 当前视频工作分支为 `codex/doubao-vnext-direct-fix-20260417`；该分支当前由 Git worktree `/private/tmp/视频工厂_round28_complete_readability` 持有。
- `已确认` 本轮新开 `round33_正反展示提示卡补齐与风格统一`，只做中段正反展示提示卡局部修复；未重构整条视频。
- `已确认` 已将原中段段首提示卡替换为《反面展示》提示卡，并在反面真实录屏之后、正面真实录屏之前新增《正面展示》提示卡。
- `已确认` 两张提示卡均为 720x1280、9:16 竖屏展示牌，采用粉色樱花、细线边框、蕾丝花边感、圆角展示牌、中心大标题、柔和光感与少量高光粒子。
- `已确认` 两张提示卡时长均为 `1.6s`，中段主要切点使用 `0.16s` 轻 crossfade，结果差卡回主持壳使用 `0.22s` 轻 crossfade。
- `已确认` 反面录屏与正面录屏仍由用户真实录屏承担，源片段未裁短、未替换、未重录；新增正面提示卡不替代正面录屏证据。
- `已确认` 结果差提示卡、主持壳、`judgment_card`、Prompt 引用尾卡均未重做；未调用阿里 API，未重新生成元素娃娃，未修改原始录屏素材。
- `已确认` `latest_review_pack` 已更新指向：
  - `round33_正反展示提示卡补齐与风格统一`
- `已确认` 当前审片包口径：
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 已新增并执行“视频修改必须同步口径规则”：以后凡是修改视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新口径文件；不允许只改视频、不改口径；只要影响新会话默认接手判断，就必须同步到 `codex/user-readable-map`。
- `已确认` 本文件所在默认主读取分支 `codex/user-readable-map` 已同步到 round33 口径；视频完整产物以 `codex/doubao-vnext-direct-fix-20260417` 为准。
- `待验证` round33 内容最终是否过线仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 当前最新审片入口

- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `dist/latest_review_pack/full.mp4`
- `dist/latest_review_pack/middle_preview.mp4`
- `dist/latest_review_pack/before_after.mp4`
- `dist/latest_review_pack/反面展示提示卡_单帧.png`
- `dist/latest_review_pack/正面展示提示卡_单帧.png`
- `dist/latest_review_pack/正反提示卡_并排对比.png`
- `dist/latest_review_pack/problem_windows/30_32s.mp4`
- `dist/latest_review_pack/cut_contact_sheet.jpg`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_round33_正反展示提示卡补齐与风格统一.md`
