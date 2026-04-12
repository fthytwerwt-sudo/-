# Current Publish Target Light Evidence

## 对应对象

- 当前待发对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 当前审核对象：`dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 云端正式输出：`oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`

## Git 可追踪轻量证据包

1. `cases/formal_api_demo_doubao_task_clear_20260412.md`
   - 本轮正式样片执行输入稿。
   - 明确写死：
     - `54s`
     - `seg01 = human`
     - `seg02 = self_footage`
     - `seg03 = light_ppt`
2. `dist/formal_api_demo_doubao_task_clear_20260412/manifest.json`
   - 本轮完整执行快照。
   - 可直接看到：
     - 总时长 `54s`
     - `seg02` 绑定到 `seg02_doubao_evidence_v1.mp4`
3. `dist/formal_api_demo_doubao_task_clear_20260412/route_plan.json`
   - 本轮 carrier 分发结果。
   - 可直接确认：
     - `seg01 = human`
     - `seg02 = self_footage`
     - `seg03 = light_ppt`
4. `dist/formal_api_demo_doubao_task_clear_20260412/script.txt`
   - 当前样片最短脚本摘要。
   - 可快速确认本轮已从旧 15 秒对象升级到“问题 → 动作 → 结果”结构。
5. `dist/formal_api_demo_doubao_task_clear_20260412/captions.srt`
   - 当前样片字幕与时间切分。
   - 可快速确认时长为：
     - `10s / 26s / 18s`
6. `dist/formal_api_demo_doubao_task_clear_20260412/result_summary.json`
   - 机器侧结果摘要。
   - 可直接确认：
     - `overall_status = success`
     - `assembly_status = success`
     - `cloud_assembly_status = success`
7. `codex_log/20260412_豆包素材正式样片执行与过线结论.md`
   - 本轮素材路径偏差、执行命令、技术验证、内容验证与过线结论。
8. `codex_log/current_publish_target.md`
   - 当前仓库正式指针。
   - 可直接确认：
     - 当前待发对象已切到 `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
     - 旧 `formal_api_demo_user_footage_20260409` 不再是当前对象

## 这些轻量证据共同证明什么

- 当前最新样片是谁：
  - `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- 当前样片 4 层状态是什么：
  - `technical_validation（技术验证）`：`通过`
  - `content_validation（内容验证）`：`通过`
  - `user_acceptance（用户验收）`：`通过`
  - `send_ready（可直接发送）`：`是`
- 当前样片结构是什么：
  - `API 生成真人 -> 豆包真实录屏 -> 单屏 steps_card`
- 当前样片技术状态是什么：
  - generation 成功
  - assembly 成功
  - cloud assembly 成功
- 当前样片为什么已过线：
  - `seg02` 已不再只是抽象说明
  - 已能看见：
    - `别再直接写`
    - `先收 3 件事`
    - `三个判断点`
    - `今天能开工的起手句`
- 当前应该怎么理解后续动作：
  - 当前样片已可直接发送
  - 后续若继续推进，属于发布包装与系统升级空间，不再属于“继续救片”
- 当前路径偏差是什么：
  - 用户给的是不存在的目录
  - 本轮实际执行的是同级单文件：
    - `素材录制/豆包素材.mp4`

## 当前 `local_only` 重证据

- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
  - 当前可直接打开的本地审片件。
- `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review.mp4`
  - 带字幕 burn-in 的辅助版。
- `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg02_doubao_evidence_v1.mp4`
  - 本轮新的 `seg02` 证据 clip。
- `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg03_image.png`
  - 本轮手工重做的单屏 `steps_card`。
- `素材录制/豆包素材.mp4`
  - 本轮真实素材源文件。

## 为什么这轮仍不追踪二进制

- 当前仓库继续优先追踪：
  - `case`
  - `manifest`
  - `route_plan`
  - `script`
  - `captions`
  - `result_summary`
  - dated log
- 二进制样片和原始录屏仍保持 `local_only`
- 这样新聊天能先靠 Git 轻量证据锁定：
  - 对象
  - 结构
  - 状态
  - 过线结论

## 当前一句话

- 旧 `seg02` 的“差值不够硬”问题已经被 `豆包素材.mp4` 里的同任务收清链路替换掉；当前最新样片已经完成技术通过、内容通过与可发布测试线通过，且本地可审对象已切到：
  - `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
  - 且当前状态已扩展为：`user_acceptance 通过`、`send_ready = 是`
