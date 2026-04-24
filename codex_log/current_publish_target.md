# Current Publish Target

## 当前口径

- `已确认` 本文件现在记录《视频工厂》当前复审 / publish target 入口。
- `已确认` 20260412 旧样片只保留为历史通过样片，不再代表当前最新复审对象。
- `已确认` 当前用户最终人工确认前，`send_ready` 必须保持 `no`。

## 历史 target

- 历史待发对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 历史云端输出：`oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`
- 历史状态：
  - `technical_validation`：`通过`
  - `content_validation`：`通过`
  - `user_acceptance`：`通过`
  - `send_ready`：`是`
- 当前解释：上述状态只代表 20260412 当时口径下的历史 target，不代表当前 vNext / round32 可直接发送。

## 当前复审 target

- 当前最新复审对象：`dist/latest_review_pack/`
- 当前 round 指向：`round32_全片边框残留与跳切连续性修复`
- 当前完整正片：`dist/latest_review_pack/full.mp4`
- 当前中段预览：`dist/latest_review_pack/middle_preview.mp4`
- 当前复审入口：`dist/latest_review_pack/review_manifest.md`
- 当前状态摘要：`dist/latest_review_pack/summary.json`

## 当前正式状态

- `technical_validation`：`通过`
- `border_residue_validation`：`通过`
- `jump_cut_validation`：`通过`
- `content_validation`：`待用户 / ChatGPT 最终复审`
- `send_ready`：`no`
- 当前判断：`round32 技术扫描与审片包生成已通过；内容最终过线与可发送状态仍待用户 / ChatGPT 复审`

## 当前唯一最高优先级 blocker

- `用户 / ChatGPT 尚未对 round32 完整正片做最终内容复审`
- 当前不能写：
  - `content_validation = 通过`
  - `send_ready = yes`
  - `云端剪辑已稳定跑通`

## 现在最该看的入口

1. `dist/latest_review_pack/review_manifest.md`
2. `dist/latest_review_pack/summary.json`
3. 若需要继续审片视频本体，再看来源视频工作分支 / 本地审片包 `dist/latest_review_pack/` 下的 `full.mp4`、`middle_preview.mp4`、`problem_windows/30_32s.mp4` 与审计报告。

## 当前主读取分支已追踪轻量证据

- `dist/latest_review_pack/review_manifest.md`
- `dist/latest_review_pack/summary.json`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260425_默认主读取分支口径同步与视频修改同步规则.md`

## 当前来源分支 / 本地审片包证据

- `/Users/fan/Documents/视频工厂/dist/latest_review_pack/`
- `dist/latest_review_pack/`

## `lane_recommendation`

- `serial_review_only`

## `lane_reason`

- 当前对象已收束到 round32 审片包。
- 当前动作不是继续生成视频，而是按 review_manifest 进行最终人工复审。
- 用户最终确认前，不得把技术验证通过升级成内容通过。

## `lane_invalid_if`

- 用户要求新开 round 或继续修视频内容。
- 用户人工确认 round32 内容通过并允许更新 `send_ready`。
- `dist/latest_review_pack/summary.json` 指向发生变化。

## `parallel_recommendation`

- `serial_only`

## `parallel_reason`

- 当前只需要围绕同一套审片包做最终判断。
- 并发写同一状态文件容易造成 `technical_validation` 与 `content_validation` 混写。

## `parallel_invalid_if`

- 下一轮任务拆成互不写同一文件的独立审计项。

## 当前同步状态

- 状态分类：`formal_synced`
- 当前主读取分支：`codex/user-readable-map`
- 当前来源分支：`codex/doubao-vnext-direct-fix-20260417`
- 当前主读目录：`GPT数据源/`
- 当前复审 target：`dist/latest_review_pack/`
- 已同步事项：round32 当前口径、latest_review_pack 指针、轻量证据入口、视频修改必须同步口径规则
- 未同步事项：用户 / ChatGPT 最终内容复审结论尚未产生

## 最后更新时间

- `2026-04-25 CST`

## 对应 dated log 路径

- `codex_log/20260412_豆包素材正式样片执行与过线结论.md`
- `codex_log/20260413_口径压平补丁_过线与升级空间拆层.md`
- `codex_log/20260424_round32_全片边框残留与跳切连续性修复.md`
- `codex_log/20260425_默认主读取分支口径同步与视频修改同步规则.md`
