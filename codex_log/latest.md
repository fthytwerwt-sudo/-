# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，后续仓库型任务继续默认在功能分支推进，而不是直接改 `main`。
- 当前项目已进入“正式版目标态搭建阶段”：
  - 正式版目标态文件已落入执行层
  - 正式版最小骨架、输入输出契约与 Gate 校验框架已开始落仓库
  - 当前已进入 TTS 真实接通阶段，本轮已用当前本地 Edge Gateway 配置再次重跑真实 non-dry-run
  - 当前已把 TTS probe 拆成显式 route family：Ark / Edge Gateway / Doubao OpenSpeech
  - 本轮只验证 TTS，不代表整条正式视频链路已跑通
  - 但正式版云端链路仍不能视为已跑通
- 当前仓库已明确项目正式口径：
  - 个人内部使用
  - Prompt 驱动
  - Codex 可执行
  - 视频内核优先
  - 前端页面不是当前阶段重点
- 当前仓库仍保留“用户可讨论定位层”，用于帮助非技术用户判断问题落在哪一层，并更准确地向 ChatGPT 描述修改点。
- 原有三层分工保持不变：
  - `project_source/` 负责项目脑
  - `codex_source/` 负责执行层
  - `codex_log/` 负责执行日志
- 当前已确认运行事实仍是本地 demo 链路：
  - `cases/demo.md` → `generate_demo.py` → `say / afconvert / ffmpeg-static` → `video_builder.swift` → `dist/demo/` 四件套
- 当前旧 demo 仍是运行锚点，不是质量样片，不是正式版事实参考
- 当前新落仓库的正式版文件定义的是目标态：
  - 先锁质量标准
  - 再按 bug / 缺口 / 参数 / 编排问题进入修正循环
  - 不得写成“当前云端正式链路已成立”

## 最近一次完成了什么

- 已再次用当前本地 Edge Gateway 配置重跑真实 non-dry-run TTS probe：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
  - 当前最小字段复核通过：
    - `auth.api_key`
    - `tts.api_route_family`
    - `tts.model`
    - `tts.voice`
- 本轮真实结果仍是 `failed`
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`
  - 三份结果文件状态一致
- 当前失败点继续稳定压缩在同一最小层：
  - route family：`edge_gateway_openai_compatible`
  - `base_url = https://ai-gateway.vei.volces.com/v1`
  - `relative_path = /audio/speech`
  - `model_identifier_source = model`
  - `voice_location = payload.voice`
  - HTTP `401`
  - 远端返回：AI Gateway API Key invalid
- 当前没有落出真实音频文件
- 因为没有可用音频资产，本轮 assembly 仍未执行：
  - 这是按阶段收口，不是漏执行
  - 若强行继续，当前只会命中 `generation_assets_not_ready`
- 已把正式版 generation 收窄到“TTS probe”：
  - local 私有配置已支持方舟 API Key、TTS model / endpoint、voice、response_format
  - generation_gate 已改成以 TTS 为主判断 `success / blocked / failed`
  - generation pipeline 已支持在前提齐时发起真实 TTS probe，在前提不足时明确 blocked
- 已在本地创建 `config/formal_api_demo.local.toml` 模板：
  - 该文件只存在本地、不会进入 git
  - 当前默认仍为空值占位，因此本轮真实 probe 结果是 blocked，而不是 success
- 已新增和更新测试：
  - 验证缺 API Key、缺 model / endpoint、failed / success 分支
  - 现有 dry-run 路径保持不被破坏
- 已落正式版最小骨架：
  - `cases/formal_api_demo.md`
  - `config/formal_api_demo.example.toml`
  - `formal_api_demo_core.py`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `tests/test_formal_api_demo_pipeline.py`
- 已把正式版输入解析、manifest / result_summary schema、generation_gate / assembly_gate、dry-run / blocked 路径落成可执行骨架：
  - dry-run 会真实产出结构化 manifest、gate report、assembly plan、result_summary
  - 在无凭证、无 local 配置、无 provider 实现时，只会写 `planned` 或 `blocked`，不会假装 success
  - 明确禁止回退到本地 `say / afconvert / ffmpeg-static / video_builder.swift` 作为正式版 fallback
- 已为 `codex_source/07_formal_api_demo_target_plan.md` 补入“验收节奏 / 验收时机 / 阶段完成标志”：
  - 明确骨架验收、接 API 前验收、首轮样片验收、修正循环验收四个时间点
  - 明确每阶段做到哪算过、什么时候不能继续往下走
  - 明确用户最该在哪些节点介入验收
- 已新增 `codex_source/07_formal_api_demo_target_plan.md`：
  - 把正式版 API demo 目标态、执行 Gate、修正循环、最小回归样本集、机器硬校验与人工复审正式写入仓库
  - 明确区分“当前仓库事实”与“正式版目标态”
- 已同步增补入口文件：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
- 已刷新 `codex_log/latest.md`，让新会话能直接接手正式版目标态主线
- 已新增完整执行日志：
  - `codex_log/20260401_formal_api_demo_target_plan_upgrade.md`

## 当前最关键的下一步

- 若后续继续执行正式版主线，TTS 下一步仍不该先改代码，而应先换成真实有效的 AI Gateway 访问密钥。
- Ark 路由保留用于继续压测当前 404，但不再作为所有 TTS family 的默认兜底。
- Doubao OpenSpeech 当前仅完成 family / gate 拆分；若继续推进，需要先补请求体和返回解析实现。
- 在火山凭证、空间名、资源存储配置、关键接口可用性未补齐前，不得把正式版云端链路写成已跑通。
- 若后续继续做仓库型小闭环，仍按“先更新日志，再 commit / push 当前分支，供 ChatGPT 复审”推进。

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- 若任务偏正式版 API demo / 目标态 / 云端组装 / 修正循环 / 质量达标反推，再补读：
  - `cases/formal_api_demo.md`
  - `config/formal_api_demo.example.toml`
  - `config/formal_api_demo.local.toml`（若本地存在，仅本地读取，不进 git）
  - `formal_api_demo_core.py`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `codex_source/05_runtime_and_artifact_rules.md`
  - `codex_source/01_execution_rules.md`
  - 并优先看 `codex_source/07_formal_api_demo_target_plan.md` 里“验收节奏 / 验收时机 / 阶段完成标志”这一节
- 若任务偏项目定位，再补读 `project_source/00_project_brief.md` 和 `project_source/01_project_system_prompt.md`
- 必须明确：
  - `codex_source/05_runtime_and_artifact_rules.md` 记录当前仓库已确认事实
  - `codex_source/07_formal_api_demo_target_plan.md` 定义正式版目标态
  - 旧 demo 仍是运行锚点，正式版链路仍不是当前已验证跑通事实
