# Current Publish Target

## 当前待发对象

- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`

## 当前审核对象

- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`

## 当前云端正式输出

- `oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`

## 当前正式状态

- `technical_validation`：`通过`
- `content_validation`：`通过`
- 当前判断：`可发布测试线通过（以本地 clean review 审片件 + cloud assembly 成功结果为准；云端正式成片未自动回拉本地）`

## 当前唯一最高优先级 blocker

- `无内容 blocker`
- 当前仅剩操作层提示：
  - 云端正式成片本地回拉文件尚未自动落地
  - 但不影响本轮内容过线与当前审片

## 现在最该改的唯一一点

- `无`
- 当前更值当动作已从“继续救 seg02”切换为：
  - 保留本轮样片为当前最新尝试
  - 进入发布前最后复看与分发包装

## 当前已追踪证据

- `cases/formal_api_demo_doubao_task_clear_20260412.md`
- `dist/formal_api_demo_doubao_task_clear_20260412/manifest.json`
- `dist/formal_api_demo_doubao_task_clear_20260412/route_plan.json`
- `dist/formal_api_demo_doubao_task_clear_20260412/script.txt`
- `dist/formal_api_demo_doubao_task_clear_20260412/captions.srt`
- `dist/formal_api_demo_doubao_task_clear_20260412/result_summary.json`
- `codex_log/current_publish_target_light_evidence.md`
- `codex_log/20260412_豆包素材正式样片执行与过线结论.md`

## 当前 `local_only` 证据

- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review.mp4`
- `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg02_doubao_evidence_v1.mp4`
- `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg01_video.mp4`
- `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg03_image.png`
- `素材录制/豆包素材.mp4`

## `lane_recommendation`

- `standard_lane`

## `lane_reason`

- 当前对象、当前状态和当前结论已经锁定
- 本轮最新样片已形成可审对象，不再慢在“素材够不够硬”的审计
- 若下一轮继续动这条样片，更可能是局部 polish、发布包装或云端回拉补齐

## `lane_invalid_if`

- 用户对当前样片提出新的最高优先级内容异议
- 本地 clean review 与云端正式输出出现实质内容偏差
- 当前任务重新回到选题或价值层重判

## `parallel_recommendation`

- `serial_only`

## `parallel_reason`

- 当前对象已经收束到同一条样片
- 后续若再改，只会继续写同一路径和同一结论
- 并发写入这条样片没有收益，反而容易破坏当前稳定状态

## `parallel_invalid_if`

- 下一轮只做纯读取 / 纯审计
- 或拆成互不写同一对象的独立任务

## 当前同步状态

- 状态分类：`formal_synced`
- 主读取分支：`codex/user-readable-map`
- 已同步内容：当前待发对象、当前状态、当前结论、轻量证据包索引
- 未同步内容：二进制审片件、原始豆包素材与 `seg02` clip 仍属 `local_only`

## 最后更新时间

- `2026-04-12 23:20:17 CST`

## 对应 dated log 路径

- `codex_log/20260412_豆包素材正式样片执行与过线结论.md`
