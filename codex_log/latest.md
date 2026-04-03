# Latest

## 当前 motion 排查状态

- 2026-04-04 本轮只排查当前样片“有点卡卡的”来源，并只做最小 assembly 修正。
- 当前结论：
  - `motion_fix_passed`

## 当前主判断

- 当前卡顿感主因：
  - `assembly_side`
- 不是 `seg02_video.mp4` 本身只有低帧率。
- 最直接证据：
  - `dist/formal_api_demo/visual/seg02_video.mp4` 是 `30 fps`、约 `6.004s`、`180` 个视频时间点。
  - 修正前 `dist/formal_api_demo/final.mp4` 的 `seg02` 对应窗（`4.0s-10.0s`）只有 `10 fps`、`60` 个时间点。
  - `config/formal_api_demo.local.toml` 与 `config/formal_api_demo.example.toml` 都已配置 `assembly.fps = 25`，但 [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py) 之前把 preview/final manifest 硬编码成了 `10 fps`。

## 本轮实际改动

- 修改：
  - [formal_api_demo_core.py](/Users/fan/Documents/视频工厂/formal_api_demo_core.py)
  - [tests/test_formal_api_demo_pipeline.py](/Users/fan/Documents/视频工厂/tests/test_formal_api_demo_pipeline.py)
- 新增 / 更新日志：
  - [codex_log/latest.md](/Users/fan/Documents/视频工厂/codex_log/latest.md)
  - [codex_log/20260404_motion_issue_assembly_fps_fix.md](/Users/fan/Documents/视频工厂/codex_log/20260404_motion_issue_assembly_fps_fix.md)

## 当前真实产物

- 当前本地成片：
  - [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)
- 当前局部连续帧证据：
  - 修正前 final `seg02` 连续帧：`dist/formal_api_demo/review_frames/motion_probe/final_seg02_native_*.png`
  - 修正后 final `seg02` 连续帧：`dist/formal_api_demo/review_frames/motion_probe/final_seg02_native_postfix_*.png`
  - 源 `seg02` 连续帧：`dist/formal_api_demo/review_frames/motion_probe/seg02_source_native_*.png`

## 当前修正后结果

- preview/final manifest 现已走 `assembly.fps = 25`。
- 修正后 `dist/formal_api_demo/final.mp4` 为 `25 fps`。
- 修正后 final 中 `seg02` 对应窗为 `150` 个时间点 / `25 fps`，明显高于修正前的 `60` 个时间点 / `10 fps`。
- 本轮没有改文案、结构或画面内容，只修 assembly 帧率入口。

## `.gitignore` 边界

- `dist/formal_api_demo/` 仍属于 `.gitignore` / `local_only`。
- 因此：
  - 新旧成片与连续帧证据都不会上传到 GitHub
  - 但本地已生成，可完成当前验收
  - 当前应优先查看：
    - `dist/formal_api_demo/final.mp4`

## 当前最关键下一步

- 直接复审新的 [dist/formal_api_demo/final.mp4](/Users/fan/Documents/视频工厂/dist/formal_api_demo/final.mp4)。
- 若还觉得 `seg02` 仍有轻微发涩，下一轮唯一优先动作是：
  - 继续做 assembly 侧“源素材直通 / 更接近源帧率采样”，不要回到内容层大修。
