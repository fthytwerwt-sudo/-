# 2026-04-03 formal_api_demo 主线语义纠偏 / mainline realign

## 本轮目标

- 把 `formal_api_demo` 从当前“配音 API + 视觉计划 + 本地 preview”的旧执行语义拉回正式主线
- 不继续做 preview 画面 round2
- 不继续优化 `seg02` 的视觉表现
- 先把 `generation success / assembly success / provider 接入 / preview 辅助产物` 的语义彻底改正

## 读取结果

- 已读取：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_source/02_current_execution_context.md`
  - `codex_source/05_execution_deviation_and_reality_sync.md`
  - `codex_source/07_formal_api_demo_target_plan.md`
  - `codex_log/latest.md`
  - `codex_log/20260403_formal_api_demo_visual_layer_round1.md`
  - `scripts/generate_formal_api_demo.py`
  - `scripts/assemble_formal_api_demo.py`
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `config/formal_api_demo.example.toml`

## 执行前已确认事实

- 当前正式主线在执行层文档中已明确为：
  - `文本需求 → 脚本 → 配音 API → 图片 / 视频生成 API → 本地 assembly → 本地 mp4 → 人工上传`
- 当前仓库里仍存在旧偏差：
  - `latest` 与上一轮日志还把注意力停在 preview 画面 round1 / round2
  - `formal_api_demo_core.py` 虽然已经开始纠偏，但仍有少量状态文案会把人带回 `cloud assembly` 旧语义
  - 测试层虽然已把大部分 `generation success` 旧口径扳回，但还缺一条“真实 visual assets ready 时，本地 assembly implementation 缺口仍必须被诚实暴露”的回归锁
- 本轮没有发现足够明确的图片 / 视频 provider 上游合同、请求体、返回体和既有实现片段：
  - 仓库里只有模型字段、占位名称和 `provider implementation 尚未接入` 的明确标记
  - 没有足够安全依据去硬接图片 / 视频 provider
- 因此本轮动作收成：
  - 不伪造 visual provider
  - 先完成语义纠偏、测试纠偏、latest / 日志纠偏

## 识别到的跑偏点

### 描述层

- `scripts/generate_formal_api_demo.py`
  - 接手时工作区已经把描述改到较正确方向，但仍需和核心状态语义、日志入口一起收口，避免“脚本描述改了，接手日志还在继续修 preview 画面”

### 状态层

- `formal_api_demo_core.py`
  - `assembly_result_summary.next_action_hint` 在“真实 visual assets 已就绪，但正式本地 assembly implementation 仍缺失”时，仍会把下一步带回 `cloud assembly 当前未配置`
  - `evaluate_assembly_gate` 的部分检查文案仍带“正式组装仍以云端为目标”的旧表述
  - `_tts_probe_known_issues` 里仍残留“cloud visual generation / cloud assembly 是后续增强项”的旧句式，容易弱化图片 / 视频 API 仍在 generation 主链里的事实

### 测试层

- `tests/test_formal_api_demo_pipeline.py`
  - 已有测试能证明：
    - visual provider 未接通时，generation 不再 success
    - preview 成功不再自动等于 assembly 成功
  - 但还缺一条更狠的回归：
    - 当真实 visual assets 被视作 ready 时，如果 `local_assembly_implementation` 仍未接入，`next_action_hint` 也必须优先指向正式本地拼接缺口，而不能退回 cloud / preview 旧语义

### 日志层

- `codex_log/latest.md`
  - 仍把当前最关键下一步写成继续修 `seg02` 画面
- `codex_log/20260403_formal_api_demo_visual_layer_round1.md`
  - 仍是上一轮聚焦画面层的执行日志，不适合作为当前主线接手入口

## 实际改动

### 1. `formal_api_demo_core.py`

- 保留已有的主线纠偏改动，并继续补齐：
  - `generation success` 仍明确要求 `TTS success + visual generation success`
  - visual provider 未实现时继续诚实 `blocked`
  - `visual plan / preview storyboard` 继续保留为辅助产物
- 本轮新增修正：
  - `build_assembly_result_summary` 的 `next_action_hint` 改为优先看 `local_assembly`
  - 当真实 visual assets 已就绪但 `local_assembly_implementation` 仍缺失时，下一步提示必须直指正式本地拼接缺口
  - `evaluate_assembly_gate` 的检查文案和 notes 改回：
    - 当前默认交付是本地 assembly / 本地 mp4
    - cloud assembly 只单列，不覆盖主线
  - `_tts_probe_known_issues` 改成：
    - TTS 已通，但图片 / 视频 API 与正式本地 assembly 仍需继续补齐

### 2. `tests/test_formal_api_demo_pipeline.py`

- 先新增红灯测试：
  - `test_assemble_non_dry_run_surfaces_local_assembly_implementation_gap_even_when_visual_assets_ready`
- 这条测试专门卡住：
  - 即使把 generation manifest 手动调成“真实 visual assets ready”
  - 只要 `local_assembly_implementation` 未接入
  - `assembly_status` 仍必须 `blocked`
  - `next_action_hint` 也必须优先指向“正式本地 assembly implementation 缺口”
- 红灯后再修 core，测试回绿

### 3. `codex_source/02_current_execution_context.md`

- 最小补两条长期接手硬口径：
  - `visual plan / preview` 只能算辅助产物，不得写成 `generation success`
  - `local assembly` 只负责拼接真实生成素材，不得替代图片 / 视频生成本身

### 4. `codex_log/latest.md`

- 从“继续画面层 round2”切回：
  - “本轮已完成主线语义纠偏”
  - “当前最高优先级 blocker 是真实 visual provider 尚未接入”

### 5. 新增本日志

- 新建：
  - `codex_log/20260403_formal_api_demo_mainline_realign.md`

## 实际执行

### 1. 红灯测试

- 执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_surfaces_local_assembly_implementation_gap_even_when_visual_assets_ready`
- 初始结果：
  - `FAIL`
- 失败点：
  - `result["next_action_hint"]` 仍返回：
    - `cloud assembly 当前未配置；当前阶段继续沿用本地 mp4 作为默认交付件。`
- 这正是本轮要修掉的旧语义残留

### 2. 修正 core 后回绿

- 同一命令再次执行
- 结果：
  - `OK`

### 3. 语法校验

- 执行：
  - `python3 -m py_compile formal_api_demo_core.py scripts/generate_formal_api_demo.py scripts/assemble_formal_api_demo.py tests/test_formal_api_demo_pipeline.py`

### 4. 全量单测

- 执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`

## 验证结果

- `py_compile`
  - 本轮已通过
- `unittest`
  - 本轮已通过

## 当前 formal_api_demo 的真实状态

- TTS API：
  - `success`
  - 当前已有真实请求实现与回归测试
- 图片 API：
  - `blocked`
  - 当前仍缺真实 provider implementation
- 视频 API：
  - `blocked`
  - 当前仍缺真实 provider implementation
- local assembly：
  - `blocked`
  - 当前只有辅助 `preview`，正式本地素材拼接 implementation 仍未接入
- overall：
  - `blocked`

## 执行审核结论

- 本轮真实改了：
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`
  - `codex_source/02_current_execution_context.md`
  - `codex_log/latest.md`
  - 本日志
- 本轮没有做：
  - preview 画面 round2
  - `seg02` 视觉表现优化
  - cloud assembly 扩写
  - 视觉 provider 硬接实现
- 当前状态判定：
  - `已完成`

说明：

- 对本轮唯一目标“把 formal_api_demo 拉回正式主线语义”来说，已经完成
- 但 formal_api_demo 整体运行状态仍然是 `blocked`
- 剩余 blocker 不是 preview 画面，而是：
  - 图片 / 视频 provider 真实接入缺口
  - 正式本地 assembly implementation 缺口

## 当前最高优先级 blocker

- 最高优先级 blocker 是：
  - 图片 / 视频 API provider 的真实接口合同与实现仍未接入

## 下一轮唯一最优先改点

- 下一轮如果只做一个点，先补：
  - 真实 visual provider 的上游接口依据与实现
- 在这一步成立前，不要再把“继续修 preview 画面”写成最高优先级

## 仓库事实冲突说明

- 你给的背景里指出：
  - `scripts/generate_formal_api_demo.py` 还在旧描述
  - `tests` 还接受某些旧 success 语义
- 当前仓库事实是：
  - 这两处在接手时已经有一部分未提交纠偏改动
  - 但还没完全收口，尤其 `latest` 和 `assembly next_action_hint` 仍会把人带偏
- 本轮按仓库事实执行，没有回退这些已存在的纠偏，只把它们补齐到一致状态
