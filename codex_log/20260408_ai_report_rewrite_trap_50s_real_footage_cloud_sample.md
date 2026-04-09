# 20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample

## 本轮目标

- 直接使用用户已切好的 3 段本地真实素材，按固定文案做一条约 50 秒样片。
- 正式 assembly 固定走北京区 `OSS + 云剪 cloud-only`。
- 若需要结果卡，则直接生成并注入。
- 若云端链路失败，则必须明确 blocked 层级；若能本地辅助预览，则不得冒充正式完成态。

## 执行前已确认事实

- 当前仓库默认主线不是 pure PPT / 信息卡全片承载，也不是 AI talking avatar / 数字人口播。
- 当前正式默认主线是：
  - 人物负责信任、进入感、关键判断、收束
  - 用户真实录制素材负责主体推进、过程证据、现场感
  - 少量 PPT / 图片负责关键词显影、结构整理、结尾总结
- 正式 assembly 继续固定为北京区 `OSS + 云剪 cloud-only`。
- 本机正式配置源是：
  - `~/.config/video-factory/formal_api_demo.local.toml`

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `codex_source/03_research_findings_bridge.md`
- `codex_source/04_completion_and_review_contract.md`
- `codex_source/05_execution_deviation_and_reality_sync.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_source/08_branch_sync_and_reading_branch_rules.md`
- `project_source/24_human_self_footage_light_ppt_routing_rules.md`
- `config/formal_api_demo.example.toml`
- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `tests/test_formal_api_demo_pipeline.py`
- `tests/test_formal_hybrid_master.py`
- 本地 `~/.config/video-factory/formal_api_demo.local.toml`（读取时已屏蔽密钥）
- 本地素材目录 `素材录制/`
- 本地仓库 `skills/`：不存在
- 全局 skill：
  - `verification-before-completion`
  - `test-driven-development`
  - `systematic-debugging`
  - `using-superpowers`

## 素材检查

- `已确认` 找到 3 段素材：
  - `/Users/fan/Documents/视频工厂/素材录制/1.mov`
  - `/Users/fan/Documents/视频工厂/素材录制/2.mov`
  - `/Users/fan/Documents/视频工厂/素材录制/3.mov`
- `已确认` 基本元信息：
  - `1.mov`：约 `39.38s`，HEVC + AAC，`3366x2180`
  - `2.mov`：约 `49.28s`，HEVC + AAC，`3366x2180`
  - `3.mov`：约 `38.20s`，HEVC + AAC，`3366x2180`
- `已确认` 已用项目内 `node_modules/ffmpeg-static/ffmpeg` 抽帧检查。
- `部分成立` 三段素材均更像真实屏幕录制 / ChatGPT 工作流录制，不是明显真人半身口播。

## 实际路由

- `hook_human`
  - 路由到：`1.mov`
  - 判断：可作为开头工作流上下文占位，但不是真人出镜，质量层必须标记部分成立。
- `process_self_footage`
  - 路由到：`2.mov`
  - 判断：最长、画面最稳定，最适合承担中段真实过程推进。
- `result_card`
  - 路由到：`dist/formal_api_demo/visual/result_card_ai_report_rewrite_trap_cn.png`
  - 判断：本轮直接生成本地结果卡图片。
- `close_human`
  - 路由到：`3.mov`
  - 判断：可作为收束槽位最低可执行占位，但不是可见真人收束，质量层必须标记部分成立。

## 实际改动

- 新增：
  - `cases/ai_report_rewrite_trap_50s.md`
  - `codex_log/20260408_ai_report_rewrite_trap_50s_real_footage_cloud_sample.md`
- 修改：
  - `formal_api_demo_cloud_assembly.py`
    - 修正云剪 visual clip timeline 生成。
    - 视频 clip 改为 `In = 0.0` + `MaxOut = planned_duration`。
    - 图片 clip 改为 `Duration = planned_duration`。
    - 不再把全局段落时间写入 visual clip 的 `TimelineIn / TimelineOut`。
  - `tests/test_formal_api_demo_pipeline.py`
    - 新增回归测试锁住上述 cloud timeline 行为。
  - `codex_log/latest.md`
    - 刷新本轮正式云端样片、素材层判断、验证结果和接手入口。
- 本地配置：
  - `~/.config/video-factory/formal_api_demo.local.toml`
    - 写入 `[footage_inputs.hook_human]`
    - 写入 `[footage_inputs.process_self_footage]`
    - 写入 `[footage_inputs.result_card]`
    - 写入 `[footage_inputs.close_human]`
    - 将 `[tts].speech_rate` 从 `1.18` 调整为 `1.0`，使 voiceover 从约 `42.4s` 回到约 `48.45s`
  - 该文件包含密钥和本机路径，属于 `local_only`，不得提交。

## 实际执行

- dry-run：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/formal_api_demo --dry-run`
  - 结果：`planned`，无缺失前提。
- generation：
  - `python3 scripts/generate_formal_api_demo.py --input cases/ai_report_rewrite_trap_50s.md --out dist/formal_api_demo`
  - 结果：`success`
  - voiceover：`dist/formal_api_demo/tts/formal_voiceover.mp3`
  - voiceover 时长约：`48.45s`
  - manifest：`dist/formal_api_demo/manifest.json`
- assembly 第一次云端导出：
  - 结果：`success`
  - 回拉后发现成片 `84.20s`
  - 层级：`cloud assembly timeline 层`
  - 真实原因：visual clip 使用了全局 `TimelineIn / TimelineOut`，导致云剪没有按预期裁切第 4 段。
- TDD 修复：
  - 先新增回归测试并确认失败
  - 修复 timeline 生成逻辑
  - 再确认测试通过
- assembly 最终云端导出：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --out dist/formal_api_demo`
  - 结果：`success`
  - 云端输出：
    - `oss://zvip1-video-beijing/video-factory/final/20260408T134055Z/formal_api_demo.mp4`
  - 本地回拉：
    - `dist/formal_api_demo/final.mp4`
  - 云端 ID：
    - `project_id = a139456cf3334509b20192f3203d75bc`
    - `job_id = b7de1350454941e39b27d1e65624bb0a`
    - `media_id = 99fe5be0335071f1aa2be7f7d45b6302`

## 实际验证

- `已确认` 已执行：
  - `node_modules/ffmpeg-static/ffmpeg -hide_banner -i dist/formal_api_demo/final.mp4`
- `已确认` 本地回拉正式成片：
  - 路径：`dist/formal_api_demo/final.mp4`
  - 时长：`50.00s`
  - 分辨率：`1080x1920`
  - 视频编码：H.264
  - 音频：AAC
- `已确认` 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
- `已确认` 单测结果：
  - `44` tests passed
- `已确认` 回审帧目录：
  - `dist/formal_api_demo/review_frames/`

## 当前结果

- `已确认` 技术执行目标已完成：
  - 3 段素材已真实检查
  - 本轮专用 case 已新增
  - 本机正式配置已写入真实素材路径
  - result_card 已真实生成并注入
  - generation 已成功
  - 北京区 `OSS + 云剪 cloud-only` assembly 已成功
  - 成片已回拉本地并验证为 `50.00s`
- `部分成立` 内容质量目标没有完全达标：
  - 1.mov 和 3.mov 没有明显可见真人出镜
  - 因此 `hook_human` / `close_human` 的“人物承担信任 / 判断 / 收束”只完成了槽位执行，不应写成质量达标。

## 当前状态

- 技术链路：
  - `已完成`
- 素材质量：
  - `部分成立`
- 同步状态：
  - `task_branch_only`
- 未同步回：
  - `codex/user-readable-map`

## 下一步建议

- 若下一轮要冲质量水位，优先补真正可见真人开头 / 收束素材，而不是再改云端代码。
- 若只验技术链路，本轮已经足够作为“真实素材注入 + 正式云端导出”证据。
