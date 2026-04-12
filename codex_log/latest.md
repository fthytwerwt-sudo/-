# Latest

## 当前主结论

- `已确认` 本轮完成的是：**基于新素材 `素材录制/豆包素材.mp4` 的正式样片执行、成片验证与状态回写。**
- `部分成立` 用户给出的固定路径：
  - `/Users/fan/Documents/视频工厂/素材录制/豆包素材`
  实际不存在；本轮真实审计并执行的素材是同级单文件：
  - `/Users/fan/Documents/视频工厂/素材录制/豆包素材.mp4`
- `已确认` 本轮已新建样片目录：
  - `dist/formal_api_demo_doubao_task_clear_20260412/`
- `已确认` 本轮已新建执行输入稿：
  - `cases/formal_api_demo_doubao_task_clear_20260412.md`
- `已确认` 本轮已把 `seg02` 重做为新的 26 秒证据段：
  - `dist/formal_api_demo_doubao_task_clear_20260412/visual/seg02_doubao_evidence_v1.mp4`
  - 当前证据逻辑已改成：
    - `旧状态 别再直接写`
    - `先收 3 件事`
    - `三个判断点`
    - `今天能开工的起手句`
- `已确认` 本轮 generation 成功：
  - `script.txt`
  - `captions.srt`
  - `manifest.json`
  - `route_plan.json`
  - `result_summary.json`
  - `seg01_video.mp4`
  - 手工重做后的 `seg03_image.png`
  已全部落出。
- `已确认` 本轮 cloud assembly 成功：
  - `result_summary.json` 已写入：
    - `overall_status = success`
    - `assembly_status = success`
    - `cloud_assembly_status = success`
  - 对应云端正式输出：
    - `oss://zvip1-video-beijing/video-factory/final/20260412T150420Z/formal_api_demo.mp4`
- `部分成立` 本轮云端正式成片没有自动回拉到本地 `final.mp4`；
  - 但已补出可直接审片的本地 clean review 成片：
    - `dist/formal_api_demo_doubao_task_clear_20260412/local_review/final_review_clean.mp4`
- `已确认` 本轮技术验证通过，依据包括：
  - generation dry-run 通过
  - generation 实跑成功
  - cloud assembly 成功
  - 本地 clean review 成片真实落出
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_mainline_route`
    - `49` tests passed
- `已确认` 本轮内容验证通过，依据是：
  - 开头由 `API 生成真人` 承担问题点破
  - 中段由 `豆包素材.mp4` 承担主体证据
  - `seg02` 已能让观众看到：
    - 别再直接写
    - 先收 3 件事
    - `给谁看 / 最怕哪里翻车 / 手里什么能直接用`
    - 起手句
  - 结尾 steps_card 已把动作出口压实
- `已确认` 当前最新样片判断改为：
  - `technical_validation`：`通过`
  - `content_validation`：`通过`
  - `可发布测试线`：`通过`
- `已确认` 本轮已更新：
  - `cases/formal_api_demo_doubao_task_clear_20260412.md`
  - `codex_log/latest.md`
  - `codex_log/current_publish_target.md`
  - `codex_log/current_publish_target_light_evidence.md`
- `已确认` 本轮已新增 dated log：
  - `codex_log/20260412_豆包素材正式样片执行与过线结论.md`

## 当前默认接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. `codex_log/current_publish_target.md`
5. `codex_log/current_publish_target_light_evidence.md`
6. `codex_log/20260412_豆包素材正式样片执行与过线结论.md`
7. `cases/formal_api_demo_doubao_task_clear_20260412.md`
8. `dist/formal_api_demo_doubao_task_clear_20260412/{manifest.json,route_plan.json,script.txt,captions.srt,result_summary.json}`
