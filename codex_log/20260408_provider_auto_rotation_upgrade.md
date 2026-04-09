# 20260408_provider_auto_rotation_upgrade

## 本轮目标

- 读取并审计 `formal_api_demo` 当前正式 config 的真实读取结果
- 审计仓库里现有的 provider / key / voice 自动切换逻辑到底覆盖到哪一层
- 把 `formal_api_demo` 升级成：
  - 单一正式 config 源
  - provider / key / voice 候选池
  - preflight 候选链检查
  - 运行时自动切换
  - 切换日志可追踪
- 必须如实说明：
  - 如果没有备用资源，系统只能报资源池已耗尽，不能伪造新 key

## 当前工作分支

- `codex/provider-auto-rotation`

## 执行前已确认事实

- `已确认`
  - 当前仓库本地 `skills/` 目录不存在
  - 本轮已检查并实际采用的全局 skill：
    - `brainstorming`
    - `systematic-debugging`
    - `test-driven-development`
    - `verification-before-completion`
- `已确认`
  - 当前 formal_api_demo 正式主线仍是：
    - `文本需求 -> 脚本 -> 配音 API -> 图片 / 视频生成 API -> 纯 PPT / 信息卡母版 -> 北京区 OSS + 云剪 -> 导出`
- `已确认`
  - 当前工作树存在与本轮无关的既有修改：
    - `project_source/03_perplexity_prompt_library.md`
  - 本轮未触碰该文件
- `待验证`
  - 当前 formal local config 是否真的已经包含可用主 key / voice / 备用池，必须以代码真实读取结果为准，不能只按口头预期判断

## 实际读取

- `AGENTS.md`
- `codex_log/latest.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_source/02_current_execution_context.md`
- `formal_api_demo_core.py`
- `formal_api_demo_cloud_assembly.py`
- `scripts/generate_formal_api_demo.py`
- `scripts/assemble_formal_api_demo.py`
- `config/formal_api_demo.example.toml`
- `config/formal_api_demo.local.toml`
- `tests/test_formal_api_demo_pipeline.py`
- `tests/test_formal_hybrid_master.py`
- 相关历史日志：
  - `codex_log/20260401_edge_gateway_key_source_block.md`
  - `codex_log/20260401_formal_api_demo_aliyun_tts_success.md`
  - `codex_log/20260406_ppt_cloud_assembly_provider_impl.md`

## 当前 formal config 审计结果

- `已确认`
  - `load_formal_config(...)` 真实返回：
    - `has_local_config = true`
- `已确认`
  - 当前 formal local config 被代码正确读到了，不是“文件根本没读到”
- `已确认`
  - 当前解析出来的候选池数量是：
    - `tts_candidate_total = 1`
    - `tts_candidate_available = 0`
    - `image_candidate_total = 1`
    - `image_candidate_available = 0`
    - `video_candidate_total = 1`
    - `video_candidate_available = 0`
- `已确认`
  - 当前没有任何：
    - `tts_pool.*`
    - `image_generation_pool.*`
    - `video_generation_pool.*`
- `已确认`
  - 当前 primary TTS 候选仍被解析成 placeholder：
    - `auth.api_key`
    - `tts.voice`
- `部分成立`
  - 用户口头预期是“正式 config 已填好”
  - 但当前文件真实读取结果不是这样
  - 执行层必须以当前代码真实读取结果为准

## 现有自动切换逻辑审计

- `已确认`
  - 仓库原有的“自动切换”主要停留在：
    - TTS `route family` 分流
    - TTS style probe 候选
    - 单 provider 的图片 / 视频模型路由
- `已确认`
  - 原有逻辑没有真正覆盖：
    - key 级 fallback
    - voice 级 fallback
    - provider 候选池轮转
    - 候选链 preflight
    - 切换日志回写
- `已确认`
  - 真人分支目前仍未具备真实 provider implementation
  - 所以本轮没有把“真人自动切换”假装成已经落成

## 实际改动

- 更新：
  - `formal_api_demo_core.py`
    - parser 支持 dotted section 资源池结构
    - 新增 TTS 候选池解析与 preflight
    - 新增图片 / 视频候选池解析与 preflight
    - 新增 TTS runtime fallback
    - 新增图片 / 视频 runtime fallback 执行器
    - 新增 fallback event / candidate pool / resource exhausted 回写
  - `config/formal_api_demo.example.toml`
    - 新增 `tts_pool.* / image_generation_pool.* / video_generation_pool.*` 示例结构说明
  - `tests/test_formal_api_demo_pipeline.py`
    - 新增 parser / preflight / TTS fallback / 图片 fallback 测试
- 新增：
  - `codex_log/20260408_provider_auto_rotation_upgrade.md`
- 更新：
  - `codex_log/latest.md`

## 本轮新增 / 修正的 fallback 机制

### 1. 单一正式 config 源

- `已确认`
  - 运行时继续只认：
    - `config/formal_api_demo.local.toml`
  - `example.toml` 仅继续承担默认值与结构示意

### 2. 候选池结构

- `已确认`
  - 新增支持：
    - `[tts_pool.<candidate_id>]`
    - `[image_generation_pool.<candidate_id>]`
    - `[video_generation_pool.<candidate_id>]`
- `已确认`
  - base `[tts] / [image_generation] / [video_generation]` 仍被视为 `primary`
  - 若存在 pool section，会自动并入候选链

### 3. 自动切换条件

- `已确认`
  - TTS 当前会识别并处理：
    - `401 / 403 / invalid key`
    - `429 / quota exhausted`
    - `voice unavailable / unsupported`
    - `timeout / upstream unavailable`
    - `model / endpoint / resource invalid`
- `已确认`
  - 图片 / 视频当前会识别并处理：
    - `401 / 403 / invalid key`
    - `429 / quota exhausted`
    - `timeout / upstream unavailable`
    - `model / route invalid`

### 4. 风格映射

- `已确认`
  - 候选项保留：
    - `style_profile`
  - 当前默认值：
    - `default`
- `部分成立`
  - 本轮已把“不要切完就风格乱掉”的最小承载字段接进去
  - 但还没有扩成更复杂的跨 provider 声音 / 画面风格标准化系统

### 5. preflight 升级

- `已确认`
  - gate 已从“单字段检查”升级成“候选链检查”
  - 现在会返回：
    - 候选总数
    - 可用候选数
    - 备选数
    - 每个候选缺什么

### 6. 日志与状态回写

- `已确认`
  - 自动切换事件已回写到：
    - `manifest.json`
    - `visual_generation_plan.json`
    - `result_summary.json`
  - 记录字段包括：
    - 原候选
    - 原 provider / voice
    - 触发原因分类
    - 切到谁
    - 剩余候补数量

## 实际验证

- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline tests.test_formal_hybrid_master`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo.md --out dist/_provider_rotation_probe --dry-run`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo.md --out dist/_provider_rotation_realcheck`
- 验证结果：
  - `已确认`
    - 单元测试 `41` 项全部通过
  - `已确认`
    - dry-run 结果里已经能直接看到候选池摘要
  - `已确认`
    - non-dry-run 在当前本机没有可用主 key / backup pool 的情况下，会在 preflight 层诚实 blocked
  - `已确认`
    - 当前 blocked 原因被真实压到：
      - `api_key`
      - `tts_voice`
    - 不再误报成 `image_generation_model / video_generation_model`

## 当前结果

- `已确认`
  - 代码层面已经具备：
    - TTS 资源池 + 自动切换
    - 图片资源池 + 自动切换
    - 视频资源池解析 + 自动切换执行器
    - 候选链 preflight
    - fallback 事件日志
- `部分成立`
  - 当前不是 `auto_rotation_ready`
  - 因为本机 formal local config 里没有任何真实 backup pool，且 primary TTS 候选本身也不可用

## 当前状态

- 代码能力状态：
  - `partial_auto_rotation`
- 本机资源状态：
  - `blocked_by_no_backup_resources`

## 下一步建议

- 若想把当前机器真正推进到“平时不需要手动管、额度出问题自动切”的状态，最小动作是：
  - 在 `config/formal_api_demo.local.toml` 中补至少 1 组真实可用备选
- 当前最推荐的最小补法：
  - `tts_pool.backup_*`
  - `image_generation_pool.backup_*`
  - `video_generation_pool.backup_*`
- 若用户只提供单个 key，系统以后能做到的上限是：
  - 自动识别失败
  - 诚实报资源池已耗尽
  - 不能凭空创造新 key
