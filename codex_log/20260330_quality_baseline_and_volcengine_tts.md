# 20260330 Quality Baseline And Volcengine Tts

## 1. 本轮目标

- 只补“质量基线”这组缺口，不改项目脑、不改代码、不改测试。
- 把 demo 的真实身份、“抖音 90 分标准”的正式定义、以及火山引擎 TTS API 的当前优先级正式写进 Codex 侧执行文件。

## 2. 执行前已确认事实

- 当前仓库仍是《视频工厂：AI 垂类场景化视频内核》的正式项目仓库。
- 当前仓库已有：
  - `codex_source/06_execution_gate_and_parallel_rules.md`
  - `EXEC-013 顶层收口与并行执行规则`
  - 现成的执行闸门 / 自动补全边界 / 多 Codex 并行规则
- 当前项目正式主线仍是本地视频内核，不以平台 API 为前置依赖。
- 当前允许本地生成 + 人工上传。
- 当前仓库内无本地 `skills/` 目录。
- `project_source/07_collaboration_adaptation_rules.md` 当前不存在，因此本轮只能按“若存在再读取”的仓库事实处理。

## 3. 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/05_runtime_and_artifact_rules.md`
- `codex_source/06_execution_gate_and_parallel_rules.md`
- `project_source/00_project_brief.md`
- `project_source/01_project_system_prompt.md`
- `project_source/06_project_index.md`
- 本地 / 全局 skill 检查

## 4. 本轮新增的质量判断口径

- 当前 demo 只证明本地链路能跑通，不具备质量参考价值。
- 当前 demo 不能继续被当作质量样片或质量基线。
- 当前 demo 的定位是“技术闭环底座 / 运行锚点”，不是“质量参考件”。
- “抖音 90 分标准”不是平台官方规则，而是项目内部质量简称。
- 当前第一优先质量增强路线，是用户现成可用的火山引擎 TTS API。
- 当前先接 TTS，不默认扩到其他 API 或平台化路线。

## 5. 当前“抖音 90 分标准”的正式定义

- 它不是平台官方评分体系。
- 它是本项目内部对“接近抖音知识类 / AI 类 / 无人出镜短视频可推荐门槛”的质量简称。
- 它更接近创作者 / 操盘手行业经验口径，不是官方数字评分。
- 执行层后续不得把它写成“官方标准”或“平台正式 90 分规则”。

## 6. 当前 demo 的真实身份

- demo 当前只证明：
  - `cases/demo.md -> generate_demo.py -> say / afconvert / ffmpeg-static -> video_builder.swift -> dist/demo/`
  这条本地链路可以跑通。
- demo 当前不证明：
  - 质量已经过线
  - 当前音画水位可以作为样片参考
  - 当前配音与画面已经能代表目标短视频质量

## 7. 当前第一优先质量增强路线

- 当前第一优先不是平台发布 API，不是自动化运营，不是图生视频，不是数字人。
- 当前第一优先是用户现成可用的火山引擎 TTS API。
- 当前目标是先解决配音 demo 感 / 系统播报感。
- 当前“走火山引擎一套”只表示供应商统一优先，不表示现在把 ASR、图生视频、平台 API 等能力一次性全部接入。

## 8. 实际改动

- 修改 `codex_source/05_runtime_and_artifact_rules.md`
  - 新增 `## 当前质量基线与增强优先级`
  - 写入 demo 身份、90 分标准定义、火山引擎 TTS 优先级、必须过线项、一票否决项与当前路线停止线
- 修改 `codex_source/01_execution_rules.md`
  - 在 `EXEC-008` 补入当前质量基线判断
  - 在 `EXEC-013` 补入不得把行业经验口径包装成平台官方规则的边界
- 修改 `codex_source/06_execution_gate_and_parallel_rules.md`
  - 在防跑偏护栏处补入“质量增强 API 的当前真实边界”
- 修改 `codex_log/latest.md`
  - 刷新本轮完成事项、下一步和建议补读文件

## 9. 当前结果

- Codex 侧现在已经正式把“demo 不是质量参考件”写入执行层。
- Codex 侧现在已经正式把“90 分标准是内部简称，不是平台官方规则”写入执行层。
- Codex 侧现在已经正式把“当前第一优先质量增强路线是火山引擎 TTS API，且当前只先接 TTS”写入执行层。

## 10. 下一步建议

- 若后续继续推进质量增强，优先围绕火山引擎 TTS API 做配音质量替换，不要自动扩成全套火山能力。
- 若后续再次讨论“90 分标准”，先回到 `codex_source/05_runtime_and_artifact_rules.md`，按内部定义、必须过线项和一票否决项判断。
- 若后续进入真实仓库小闭环，仍按当前仓库规则更新日志、commit 并 push 当前分支，再交 ChatGPT 复审。
