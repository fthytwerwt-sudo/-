# 20260402 Formal API Demo TTS Style Round2

## 本轮目标

- 基于用户最新反馈“旧 A 更对，但还不完全对”，继续把 `formal_api_demo` 的阿里 TTS 子线往下压实
- 只围绕旧 A 做第二轮更窄微调
- 把声音目标和执行标准沉淀进文件
- 不推进视频生成，不推进 assembly，不重开大路线

## 执行前已确认事实

- 阿里百炼 TTS 已接通并落出真实音频
- 旧 A / B / C 三版已生成
- 用户明确反馈：
  - 旧 A 更对
  - 但还不完全对
  - 说明当前主问题不是路线错，而是 A 方向已对，但 instruction / 节奏 / 参数还要继续压
- 当前默认技术路线保持不变：
  - `provider.name = aliyun_bailian`
  - `tts.api_route_family = aliyun_bailian_cosyvoice`
  - `tts.model = cosyvoice-v3-flash`
  - `tts.voice = longanyang`

## 实际读取

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `formal_api_demo_core.py`
- `config/formal_api_demo.example.toml`
- `project_source/06_project_index.md`
- 本地 `config/formal_api_demo.local.toml`（只读，不回显真实值）

## 实际改动

- 修改了 `formal_api_demo_core.py`
  - 新增 round2 入口：
    - `run_aliyun_tts_style_probe_round2(...)`
  - 新增 A1 / A2 / A3 / A4 四个 round2 变体
  - 新增 round2 汇总文件输出：
    - `dist/formal_api_demo/tts_style_probe_round2.json`
  - 汇总结果现在会显式写出：
    - 每版 `instruction`
    - 每版 `speech_rate`
    - 每版 `pitch_rate`
    - 每版 `volume`
    - `recommended_variant_id`
    - `recommended_variant_label`
    - `recommendation_reason`
- 修改了 `config/formal_api_demo.example.toml`
  - 新增 round2 配置块：
    - `[tts_style_probe_round2]`
    - `[tts_style_probe_round2_variant_A1]`
    - `[tts_style_probe_round2_variant_A2]`
    - `[tts_style_probe_round2_variant_A3]`
    - `[tts_style_probe_round2_variant_A4]`
- 修改了 `tests/test_formal_api_demo_pipeline.py`
  - 新增 round2 单测
  - 校验四版文件名、summary 结构和推荐候选字段
- 新增项目脑文件：
  - `project_source/09_tts_voice_target_v1.md`
- 新增执行脑文件：
  - `codex_source/08_tts_style_execution_rules.md`

## 本轮真实尝试了什么

### 第一轮 round2 instruction 写法

- 先尝试自由中文风格稿：
  - 更稳、更冷静
  - 更干、更利落
  - 判断感更强一点
  - 去客服感 / 播音感

结果：

- 四版全部真实发出请求
- 全部被远端返回：
  - `InvalidParameter`
  - `engine 428`

### 第二轮 round2 instruction 写法

- 为了不回退到纯情绪词，又尽量贴近旧成功句式，再尝试更窄的结构化中文：
  - “你现在扮演……，你的情感是……”
- 仍全部被：
  - `InvalidParameter`
  - `engine 428`

### 第三轮 round2 instruction 写法

- 再继续收紧到更接近旧成功句式：
  - “你说话的角色是……，你说话的情感是……”
  - “你说话的场景是……，你说话的情感是……”

结果：

- 四版再次全部真实发出请求
- 仍全部被：
  - `InvalidParameter`
  - `engine 428`

## 实际执行

- 单测：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_run_aliyun_tts_style_probe_round2_writes_four_named_audio_files_and_summary`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
- 语法检查：
  - `python3 -m py_compile formal_api_demo_core.py tests/test_formal_api_demo_pipeline.py`
- 真实 non-dry-run：
  - 通过 `python3` 内联脚本调用 `run_aliyun_tts_style_probe_round2(...)`
  - 输出目录：
    - `dist/formal_api_demo`

## 当前结果

- 代码与测试层：
  - 单测通过
  - 语法检查通过
  - 项目脑与执行脑文件已新增
- 真实执行层：
  - `dist/formal_api_demo/tts_style_probe_round2.json` 已生成
  - `style_draft_in_request = true`
  - 四版都是真实发出了请求
  - 四版都没有落出新音频文件
- 当前 round2 汇总中的设计推荐仍是：
  - `recommended_variant_id = A2`
  - `recommended_variant_label = 更干、更利落`
  - 但这只是当前设计推荐，不是已试听候选

## 最小失败层级

- 当前失败不是：
  - assembly
  - 视频生成
  - 代码桥接缺失
  - API key 缺失
  - model / voice 缺失
- 当前最小失败层已经压到：
  - 当前 `aliyun_bailian_cosyvoice + cosyvoice-v3-flash + longanyang` 的 instruction 合同限制
- 证据：
  - instruction 已真实进请求体
  - request_debug 已显示 `style_draft_in_request = true`
  - 但 richer 中文 instruction 连续三轮都被远端以 `InvalidParameter / engine 428` 拦下

## 当前最值的结论

- 当前路线没有错
- 旧 A 仍是当前可用基线
- 本轮最值的新事实不是“又多调了几个声音”，而是：
  - richer 中文 instruction 目前不能直接在这条 route / model / voice 上承载
- 这意味着明天不需要重新定义方向，只需要在已验证成功的最窄 instruction 句式上继续收口

## 下一步建议

- 明天最省事的下一步：
  - 保留旧 A 为可用基线
  - 不再继续盲写 richer 中文 prose instruction
  - 用已验证成功的最窄 instruction 句式，只做更小的 `speech_rate / pitch_rate / volume` 微调
- 若下一轮仍不够，再继续按既定顺序分叉：
  - 先判断 `longanyang` 是否不合适
  - 最后才考虑换模型族
