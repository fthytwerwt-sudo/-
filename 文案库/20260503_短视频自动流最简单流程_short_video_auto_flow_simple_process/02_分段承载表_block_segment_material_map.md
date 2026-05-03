# 分段承载表：短视频自动流的最简单流程 full flow quality sample

## 本轮状态

- `已确认` 本轮不是 PR #43 的 145 秒短样片，不复用 PR #43 压缩稿或 timeline。
- `已确认` 本轮 runtime 使用用户最新 `FINAL_SCRIPT_V2` 完整文案。
- `已确认` 用户录制素材承担中段主体推进；卡片 / PPT 只做结构、边界和总结辅助。
- `已确认` Trae 项目骨架只能证明初步项目形状出现，不能证明 app 跑通。
- `已确认` API 画面如无法安全脱敏，使用信息卡 fallback，不使用火山引擎原画面。

## block / segment 承载

| block_id | segment_id | 文案范围 | 主要承载 | 辅助承载 | 证明点 | 不能证明点 |
|---|---|---|---|---|---|---|
| B01 | host_opening_judgement | 一键生成不是自动流 | 主持壳替代卡 / cute_prompt_card_route | 字幕 | 建立主判断 | 不证明工具执行 |
| B02 | doubao_simple_need | 用户给豆包一句需求 | 用户录制素材：豆包素材 00:00:16-00:00:24 | 字幕 | 需求入口很简单 | 不证明 Trae 已执行 |
| B03 | doubao_plan | 豆包拆短视频生产流程 | 用户录制素材：豆包素材 00:01:28-00:02:00 | 信息卡少量提示 | 豆包把需求拆成流程 | 不证明工程跑通 |
| B04 | doubao_prompt | 豆包生成 Trae prompt | 用户录制素材：豆包素材 00:02:40-00:04:08 | cute_info_card_route | 想法转成 Trae 能接的任务说明 | 不证明 prompt 已运行成功 |
| B05 | trae_solo | Trae SOLO 接住 prompt 并 plan | 用户录制素材：trae 素材 00:00:32-00:01:52 | 字幕 | SOLO Coder、Updating Tasks、11 待办 | 不证明所有待办完成 |
| B06 | trae_skeleton | Trae 生成项目骨架 | 用户录制素材：trae 素材 00:02:00-00:02:40 | cute_info_card_route | `vlog_automation_workflow`、目录和基础文件出现 | 不证明 app 跑通 |
| B07 | api_station | API 是外部能力入口 | cute_info_card_route | 字幕 | API 位置和边界 | 不证明 API 已接通 |
| B08 | cloud_station | 云剪是装配台 | cute_info_card_route | 字幕 | 云端总装工位边界 | 不证明云剪正式稳定 |
| B09 | codex_checker | Codex 做执行检查 | 用户录制素材：codex 素材 00:02:56-00:03:08 | 遮挡层、字幕 | 命令、路径、文件、报告检查 | 不证明内容过线 |
| B10 | comparison_and_summary | 即梦对比与收束 | cute_info_card_route / 主持壳替代卡 | 字幕 | 抽素材 vs 搭流程；顺序对了自动化才有落脚点 | 不证明可发布 |
