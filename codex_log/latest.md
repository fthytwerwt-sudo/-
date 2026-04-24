# Latest

## 20260425｜默认主读取分支口径同步与视频修改同步规则

- `已确认` 本轮只做《视频工厂》项目口径、执行口径、路由口径、状态同步口径修补；未生成视频、未修改视频内容、未删除历史日志、未删除旧 round 产物。
- `已确认` 默认主读取分支 `codex/user-readable-map` 已同步到当前 round32 口径。
- `已确认` 当前《视频工厂》正式来源顺序为：
  1. `GPT数据源/` 当前 10 份执行包
  2. `codex_log/latest.md`
  3. `dist/latest_review_pack/summary.json`
  4. `dist/latest_review_pack/review_manifest.md`
  5. `codex_source/00_codex_readme.md`
- `已确认` `project_source/` 只作为历史 / 辅助主题化镜像，不得默认高于 `GPT数据源/` 当前 10 份执行包或 `latest_review_pack`。
- `已确认` `current_publish_target.md` 与 `current_publish_target_light_evidence.md` 已将 20260412 旧样片降级为历史 target；当前复审 target 改为 `dist/latest_review_pack/`。
- `已确认` 当前 `latest_review_pack` 指向：
  - `round32_全片边框残留与跳切连续性修复`
- `已确认` 当前审片包口径：
  - `border_residue_validation = 通过`
  - `jump_cut_validation = 通过`
  - `technical_validation = 通过`
  - `content_validation = 待用户 / ChatGPT 最终复审`
  - `send_ready = no`
- `已确认` 历史 20260412 样片仍保留为历史通过样片，不再代表当前最新可发对象。
- `已确认` 当前正式主线仍是：`API 生成真人 + 用户录制素材 + 少量 PPT + 云端剪辑`。
- `已确认` 当前中段证据原则仍是：用户录制素材必须承担中段主体证据；卡片 / PPT / 图片只允许辅助解释，不能替代证据。
- `已确认` 已新增“视频修改必须同步口径规则”：凡是修改视频产物、样片轮次、`round`、`latest_review_pack`、`current_publish_target`、审片状态、`technical_validation`、`content_validation`、`send_ready`、`remaining_blockers`，都必须同步更新相关口径文件，并同步到 `codex/user-readable-map`。
- `待验证` round32 内容是否达到最终发送标准，仍需用户 / ChatGPT 人工复审。
- `禁止误写` 不得把技术扫描通过写成内容最终通过；不得写 `send_ready = yes`；不得把云端剪辑写成稳定跑通。

## 视频修改后默认必须同步检查

1. `codex_log/latest.md`
2. `codex_log/current_publish_target.md`
3. `codex_log/current_publish_target_light_evidence.md`
4. `GPT数据源/08_当前正式事实.md`
5. `dist/latest_review_pack/summary.json`
6. `dist/latest_review_pack/review_manifest.md`
7. 如改变入口 / 分支 / 读取顺序，还必须同步 `AGENTS.md` 和 `codex_source/00_codex_readme.md`

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `GPT数据源/08_当前正式事实.md`
- `codex_log/current_publish_target.md`
- `codex_log/current_publish_target_light_evidence.md`
- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/20260425_默认主读取分支口径同步与视频修改同步规则.md`
