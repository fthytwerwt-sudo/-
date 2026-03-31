# 20260401 Edge Gateway TTS And Assembly Run

## 本轮目标

- 连续执行 formal_api_demo 的 TTS 子线与下一块 assembly
- 先把 Edge Gateway TTS 推到真实可判断结果
- 若 TTS 成功则立即推进 assembly
- 若遇到真实硬阻塞，则压缩到最小层后收口

## 执行前已确认事实

- formal_api_demo 已完成 TTS route family split
- 当前默认优先路线是 `edge_gateway_openai_compatible`
- Ark 保留为 404 对照路径
- Doubao OpenSpeech 仍是 gate-only，这轮不走
- 上一轮 Edge Gateway 的最小阻塞点是 `tts.model`

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/07_formal_api_demo_target_plan.md`
- `codex_log/latest.md`
- `codex_log/20260401_tts_route_fix.md`
- `codex_log/20260401_tts_route_family_split.md`
- `codex_log/20260401_edge_gateway_tts_probe.md`
- `formal_api_demo_core.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- 本地 `config/formal_api_demo.local.toml`
- 当前 `dist/formal_api_demo/` 下已有结果文件

## 本地最小字段复核结果

### TTS 阶段

- `auth.api_key`：通过
- `tts.api_route_family`：通过
- `tts.model`：初始未通过，已在本地补齐到可执行状态
- `tts.voice`：通过

### Assembly 阶段

- `assembly.mode`：通过
- `assembly.template_id`：未通过
- `storage.space_name`：未通过

## TTS 阶段实际执行

- 本地只修改了私有配置：
  - 继续保留 `tts.api_route_family = "edge_gateway_openai_compatible"`
  - 把现有的可调用标识同步到 `tts.model`
- 执行：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 结果状态核对：
  - `generation_gate.status = success`
  - `manifest.current_status = failed`
  - `manifest.generation.status = failed`
  - `manifest.generation.tts_probe.status = failed`
  - `result_summary.overall_status = failed`

## TTS 阶段结果

- 本轮 TTS 结果：`failed`
- 当前已进入真实远端失败层，不再是 blocked
- 当前失败点已压缩到最小层：
  - route family：`edge_gateway_openai_compatible`
  - HTTP 状态码：`401`
  - 远端错误信息明确指向：AI Gateway API Key invalid
- 当前没有落出真实音频文件

## Assembly 阶段实际执行

- 本轮未进入真实 assembly 执行
- 原因不是 assembly 代码先卡，而是 TTS 阶段未通过，当前没有可用音频资产进入组装
- 因此本轮 assembly 只完成了前提复核，没有继续发起真实 non-dry-run

## Assembly 阶段结果

- 本轮 assembly 结果：未执行
- 若继续强行进入 assembly，当前最先命中的仍会是：
  - `generation_assets_not_ready`
  - 且本地 `template_id / space_name` 也仍未就位

## 当前结果

- 本轮已先把 TTS 推到不能再前推的位置
- 当前最小硬阻塞不是代码 bug，而是：
  - Edge Gateway 访问密钥层
- 在这一步未解决前，继续推进 assembly 没有意义，因为没有可用 TTS 输出可组装

## 下一步建议

- 下一步不建议继续改代码
- 先换成真实有效的 AI Gateway API Key
- 然后继续重跑：
  - `python3 scripts/generate_formal_api_demo.py --out dist/formal_api_demo`
- 只有当真实音频文件落出后，才进入 assembly 的真实执行
