# Latest

## 当前项目执行状态

- 当前仓库已完成 GitHub baseline，仓库型任务继续走功能分支，不直接改 `main`。
- `formal_api_demo` 当前仍只推进到阿里 TTS 子线：
  - 阿里百炼 TTS 已接通
  - 旧 A / B / C 三版真实音频已存在
  - 本轮没有推进视频生成，也没有推进 assembly
- 当前默认技术路线仍保持：
  - `provider.name = aliyun_bailian`
  - `tts.api_route_family = aliyun_bailian_cosyvoice`
  - `tts.model = cosyvoice-v3-flash`
  - `tts.voice = longanyang`

## 最近一次完成了什么

- 已围绕“旧 A 更对，但还不完全对”做第二轮窄调准备：
  - 新增 `project_source/09_tts_voice_target_v1.md`
  - 新增 `codex_source/08_tts_style_execution_rules.md`
  - 新增 round2 的 A1 / A2 / A3 / A4 配置与执行入口
  - 新增 `dist/formal_api_demo/tts_style_probe_round2.json`
- 已用同一段固定测试文案，对 A1 / A2 / A3 / A4 做真实 non-dry-run。
- 已确认新的关键事实：
  - richer 中文 instruction 已真实进请求体
  - 但当前 `aliyun_bailian_cosyvoice + cosyvoice-v3-flash + longanyang` 会把这类 richer instruction 以 `InvalidParameter / engine 428` 拦下
  - 因此本轮没有落出新的 `voice_probe_A1.mp3` / `A2` / `A3` / `A4`

## 当前结论边界

- 现在可以明确写：
  - 旧 A 仍是当前可用基线
  - 本轮最小失败层已经压到 instruction 合同限制，不是 assembly，不是视频生成，不是代码桥接缺失
- 现在还不能写：
  - “A1 / A2 / A3 / A4 已经形成新的可试听候选”
  - 因为四版都被远端参数校验拦下，没有生成新音频

## 当前最关键的下一步

- 明天最省事的动作不是重新定义方向，而是：
  - 保留旧 A 为可用基线
  - 不再盲写 richer 中文 prose instruction
  - 在已验证成功的最窄 instruction 句式上，只做更小的 rate / pitch / volume 微调
- 若下一轮仍明显不够，再进入：
  - 先判断 `longanyang` 是否不合适
  - 最后才考虑换模型族

## 新会话接手建议先读

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/08_tts_style_execution_rules.md`
- `project_source/09_tts_voice_target_v1.md`
- `codex_log/latest.md`
- 若继续推进阿里 TTS 风格复审：
  - `formal_api_demo_core.py`
  - `config/formal_api_demo.example.toml`
  - `tests/test_formal_api_demo_pipeline.py`
  - `dist/formal_api_demo/tts_style_probe_round2.json`
