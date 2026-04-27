# 方案 B V3｜阿里 / 百炼 / DashScope 历史生成链路审计

## 审计结论

- `已确认` 历史上项目确实通过阿里百炼 / DashScope 生成过图像和视频，不能简单归因成“用户没配 API”。
- `已确认` 与 V3 最相关的历史成功链路是 `元素娃娃线 round3 / round4 / round5`：`wan2.7-image-pro` 已成功生成主持娃娃图像；round5 进一步跑通 `wan2.2-s2v-detect` 与 `wan2.2-s2v` 最短视频 smoke test。
- `已确认` V3 当前脚本复用了核心 helper `_execute_aliyun_visual_generation_task` 和 DashScope 图像生成 endpoint，但 V3 运行摘要记录的本地配置路径是 `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`，而历史 round3 / round4 / round5 成功摘要指向 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- `已确认` 当前脱敏复查中，`/Users/fan/.config/video-factory/formal_api_demo.local.toml` 存在 `sk-` 形态 DashScope key；`/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml` 存在但当前未呈现为可用 `auth.api_key`。
- `最可能主因` V3 没有沿用历史成功的配置来源 / key 来源，而是跑到了旧仓库内 legacy config 或 stale key source，导致 DashScope 在创建 `wan2.7-image-pro / wan2.7-image` 任务时返回 `HTTP401 / InvalidApiKey`。
- `已确认` 本轮没有重新运行 V3 生成，没有生成新图 / 新视频，没有修改 key，没有修改正式视频状态。

## 读取结果

### 已读必读文件

- `AGENTS.md`
- `codex_source/00_codex_readme.md`
- `codex_source/01_execution_rules.md`
- `codex_log/latest.md`
- `codex_log/20260428_方案B独立反应片段V3排查与预览.md`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/run_summary.json`
- `dist/prototypes/20260428_方案B独立反应片段V3_scheme_b_standalone_reaction_v3/wan_generation_attempts_sanitized.json`
- `scripts/方案B独立反应片段V3_wan_generation.py`
- `formal_api_demo_core.py`
- `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`，只做脱敏读取
- `/Users/fan/.config/video-factory/formal_api_demo.local.toml`，只做脱敏读取

### skills 检查

- `已确认` 当前仓库本地 `skills/` 目录不存在。
- `已确认` 已检查全局 `~/.codex/skills`。
- `已确认` 找到并使用了相关通用 skill：
  - `verification-before-completion`
  - `debugging-strategies`
- `已确认` 未找到阿里百炼 / DashScope / 万相专用 skill。

## 历史成功生成链路

### 链路 A：正式 API demo 通用视觉链路

- `脚本路径`
  - `scripts/generate_formal_api_demo.py`
  - `formal_api_demo_core.py`
- `服务位置`
  - 开头 / 结尾 / 辅助视觉段，不是当前中段 reaction clip。
- `模型`
  - 图像：`wan2.6-image`
  - 视频：`liveportrait` 曾成功；`wan2.7-i2v` 在部分通用计划中作为候选 / general video model。
- `helper`
  - `run_generation_pipeline`
  - `_execute_aliyun_wan_image_generation`
  - `_execute_aliyun_visual_generation_task`
  - `_execute_aliyun_liveportrait_video_generation`
  - `_execute_aliyun_liveportrait_detect`
- `endpoint / base_url`
  - `https://dashscope.aliyuncs.com/api/v1`
  - 图像：`/services/aigc/image-generation/generation`
  - liveportrait detect：`/services/aigc/image2video/face-detect`
  - liveportrait video：`/services/aigc/image2video/video-synthesis/`
- `配置来源`
  - 入口默认使用 `DEFAULT_FORMAL_LOCAL_CONFIG_PATH`。
  - 当前代码环境下该默认值解析为 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- `输出目录 / 成功证据`
  - `dist/formal_api_demo_doubao_task_clear_20260412/visual_generation_plan.json`
    - `seg01 image_task_id = fda8daff-0bf2-49d0-89d2-d14fbaf45261`
    - `seg01 video_task_id = ff765c7b-62c3-4bcb-829c-247fad23a837`
    - `portrait_video_generation.status = success`
    - `portrait_video_generation.request_id = 343ec64a-0ced-962b-b4cc-871c29f0af15`
  - `codex_log/20260404_formal_api_demo_liveportrait_round5_success.md`
    - `liveportrait task_id = ee48c19b-80a0-41c1-88b5-80d4c6744e29`
    - `request_id = b5ba667b-86c1-95b8-a58d-cb0827a3f744`

### 链路 B：formal_api_demo_platform_uniqueness_source 图像链路

- `脚本路径`
  - `scripts/generate_formal_api_demo.py`
  - `formal_api_demo_core.py`
- `服务位置`
  - 开头 / 结尾 / 过程辅助视觉，不是中段 reaction clip。
- `模型`
  - `wan2.6-image`
- `helper`
  - `_execute_aliyun_wan_image_generation`
  - `_execute_aliyun_visual_generation_task`
- `配置来源`
  - `aliyun_bailian` provider；默认本地配置链路。
- `输出目录 / 成功证据`
  - `/Users/fan/Documents/视频工厂/dist/formal_api_demo_platform_uniqueness_source/visual_generation_plan.json`
  - `segment_assets[0].image_task_id = d31d9377-5e4d-4c2a-8ac8-dbfa20352970`
  - `segment_assets[1].image_task_id = acf72057-3723-485d-95e5-a85c62c2af4a`
  - `segment_assets[2].image_task_id = 8cf96368-368d-48c7-8d9f-9eb3bac09323`
  - `visual_generation.status = success`

### 链路 C：元素娃娃 round3 / round4 / round5 万相图像与 s2v 链路

- `脚本路径`
  - `scripts/元素娃娃线_round3_切换wan2.7与s2v闭环.py`
  - `scripts/元素娃娃线_round4_s2v_detect过检优化.py`
  - `scripts/元素娃娃线_round5_s2v_detect过检优化.py`
- `服务位置`
  - 主持壳 / 元素娃娃，不是当前中段 reaction clip。
- `模型`
  - 图像：`wan2.7-image-pro`，fallback `wan2.7-image`
  - 视频检测：`wan2.2-s2v-detect`
  - 视频：`wan2.2-s2v`
- `helper`
  - 图像复用 `formal_api_demo_core._execute_aliyun_visual_generation_task`
  - s2v detect / s2v 由 round 脚本内自定义调用：
    - `_upload_file_to_aliyun_temp_storage`
    - `_urlopen_json_request`
    - `_poll_aliyun_visual_task`
    - `_extract_aliyun_video_result_url`
- `endpoint / base_url`
  - 图像：`https://dashscope.aliyuncs.com/api/v1/services/aigc/image-generation/generation`
  - s2v detect：`https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/face-detect`
  - s2v video：`https://dashscope.aliyuncs.com/api/v1/services/aigc/image2video/video-synthesis/`
- `配置来源`
  - `round3_switch_summary.json` / `round4_detect_summary.json` / `round5_detect_summary.json` 均记录：
    - `provider_snapshot.local_config_path = /Users/fan/.config/video-factory/formal_api_demo.local.toml`
    - `provider_snapshot.provider.name = aliyun_bailian`
- `输出目录 / 成功证据`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round3/audit/round3_switch_summary.json`
    - `wan2.7-image-pro` 成功生成 2 张主持娃娃图。
    - `task_id = ae8dde69-9385-4542-9b61-655322795497`
    - `request_id = 81b6b246-e122-943f-b999-af6713bd262c`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round4/audit/round4_detect_summary.json`
    - `wan2.7-image-pro` 成功生成 4 张主持娃娃图。
    - detect 未过，但不是鉴权失败。
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/audit/round5_detect_summary.json`
    - `wan2.7-image-pro` 成功生成 1 张主持肖像。
    - `wan2.2-s2v-detect.status = success`
    - `wan2.2-s2v.status = success`
    - `s2v task_id = 471601a5-8a5d-40ce-b161-43bb1ab87bb7`
    - `s2v request_id = f1cdfeaf-8b9b-9786-a7e1-c68259bfa5ec`
    - 视频落盘：`dist/20260417_豆包的正确打开方式_vnext/host_motion_asset_gate_round5/s2v_probe/visual/候选A_round5_软脸主持肖像_video.mp4`

## V3 当前失败链路

- `脚本路径`
  - `scripts/方案B独立反应片段V3_wan_generation.py`
- `服务位置`
  - 中段独立 reaction clip 技术预览准备。
- `模型`
  - 图像：`wan2.7-image-pro` -> fallback `wan2.7-image`
  - 图生视频：`wan2.7-i2v`，因图像创建失败未进入。
- `helper`
  - `_execute_aliyun_visual_generation_task`
  - `_extract_aliyun_image_result_url`
  - `_extract_aliyun_video_result_url`
  - `load_formal_config`
- `配置来源`
  - V3 `run_summary.json` 记录：
    - `local_config_path = /Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`
    - `local_config_exists = true`
    - `provider = aliyun_bailian`
  - 当前审计复查中，历史成功链路最可能使用的是 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- `endpoint / region`
  - base_url：`https://dashscope.aliyuncs.com/api/v1`
  - image endpoint：`/services/aigc/image-generation/generation`
  - i2v endpoint：`/services/aigc/video-generation/video-synthesis`
  - config region：`cn-beijing`
- `失败返回`
  - `wan2.7-image-pro`：`HTTP401 / InvalidApiKey`
  - `wan2.7-image`：`HTTP401 / InvalidApiKey`
  - 未获得 `request_id` / `task_id`
  - `wan2.7-i2v` 未执行

## 差异表

| 项目 | 历史成功链路 | V3 当前失败链路 | 结论 |
| --- | --- | --- | --- |
| 配置来源 | round3 / round4 / round5 摘要指向 `/Users/fan/.config/video-factory/formal_api_demo.local.toml` | V3 run_summary 指向 `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml` | `已确认` 配置来源不一致，是最高优先级差异 |
| key 状态 | 当前复查为 `sk-` 形态 DashScope key 存在，长度范围 `20-39` | 当前复查 legacy config 未呈现可用 `auth.api_key`；V3 当时记录字段存在但返回 401 | `部分成立` 可能是旧 config / stale key / 非可用 key |
| 图像 helper | `_execute_aliyun_visual_generation_task` | `_execute_aliyun_visual_generation_task` | helper 主体一致，不是最可能问题 |
| 图像 endpoint | `/services/aigc/image-generation/generation` | `/services/aigc/image-generation/generation` | endpoint 主体一致，不是最可能问题 |
| 图像模型 | round3 / round4 / round5 成功用 `wan2.7-image-pro` | V3 先试 `wan2.7-image-pro` 再试 `wan2.7-image` | 模型名不是最可能问题 |
| 视频模型 | round5 成功的是 `wan2.2-s2v` | V3 计划用 `wan2.7-i2v` | `已确认` 历史视频成功不自动证明 V3 i2v 成立 |
| 使用场景 | 主持壳 / 元素娃娃 / 开头结尾 | 中段独立 reaction clip | `已确认` V3 是新用途，历史链路只能作为配置和调用参考 |

## 密钥状态脱敏摘要

- `环境变量`
  - `DASHSCOPE_API_KEY`：不存在
  - `DASHSCOPE_API_KEY_CN`：不存在
  - `BAILIAN_API_KEY`：不存在
  - `ALIBABA_CLOUD_ACCESS_KEY_ID`：不存在
  - `ALIBABA_CLOUD_ACCESS_KEY_SECRET`：不存在
  - `FORMAL_API_DEMO_LOCAL_CONFIG`：不存在
- `本地配置来源 1`
  - 路径：`/Users/fan/.config/video-factory/formal_api_demo.local.toml`
  - 状态：存在、可读
  - provider：`aliyun_bailian`
  - region：`cn-beijing`
  - `auth.api_key`：存在
  - key 形态：`sk_dashscope_like`
  - key 长度范围：`20-39`
  - `image_generation.model = wan2.6-image`
  - `video_generation.model = wan2.7-i2v`
  - OSS access key：存在
- `本地配置来源 2`
  - 路径：`/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`
  - 状态：存在、可读
  - provider：`aliyun_bailian`
  - region：`cn-beijing`
  - 当前复查 `auth.api_key`：未呈现为可用 DashScope key
  - OSS access key：存在
- `最可能用于历史成功生成的来源`
  - `/Users/fan/.config/video-factory/formal_api_demo.local.toml`
  - 证据：round3 / round4 / round5 的 `provider_snapshot.local_config_path` 均明确指向该路径。
- `安全边界`
  - 本报告未输出任何完整 key。
  - 本报告未输出任何超过 6 位连续 key 片段。
  - 本报告未提交本地私有配置。

## 最可能主因

`已确认 / 高置信` V3 没有复用历史成功的配置来源 / key 来源，而是记录为使用 `/Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml` 这条 legacy config。当前审计中，历史成功链路指向 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`，且该路径存在 `sk-` 形态 DashScope key；legacy config 当前未呈现为可用 `auth.api_key`。因此 V3 在同一类 DashScope 图像 endpoint 上得到 `HTTP401 / InvalidApiKey`，最可能是读取了错误或 stale 的 key source。

证据：

- V3 `run_summary.json`：`local_config_path = /Users/fan/Documents/视频工厂/config/formal_api_demo.local.toml`。
- round3 / round4 / round5 摘要：`provider_snapshot.local_config_path = /Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- 当前 `formal_api_demo_core.DEFAULT_FORMAL_LOCAL_CONFIG_PATH` 解析为 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
- 当前脱敏复查：official config 有 `sk-` 形态 key；legacy config 未呈现为可用 DashScope key。
- V3 对 `wan2.7-image-pro` 和 `wan2.7-image` 均在创建阶段返回 `HTTP401 / InvalidApiKey`，未进入 task 生成。

## 备选原因

1. `部分成立 / 中等证据` V3 运行时 legacy config 曾有一个 key 字段，但该 key 已过期、被撤销或不是 DashScope / 百炼通用 API Key。
   - 证据：V3 日志写过 `auth.api_key` 字段存在，但实际返回 `HTTP401 / InvalidApiKey`。
   - 限制：当前复查 legacy config 时未看到可用 DashScope key，无法确认当时字段值是否已被改动。

2. `部分成立 / 中等证据` 当前 key 权限或账户状态不覆盖 V3 所需 `wan2.7-image-pro / wan2.7-image / wan2.7-i2v`。
   - 证据：V3 直接 401，未取得 task；历史成功不自动等于当前账号 / key 仍有权限。
   - 限制：历史 round3 / round4 / round5 用同类 `wan2.7-image-pro` 成功，所以模型名本身不像主因。

3. `待验证 / 弱证据` V3 的图生视频模型选择与历史成功视频模型不同。
   - 证据：历史真正跑通视频的是 `wan2.2-s2v`；V3 计划使用 `wan2.7-i2v`。
   - 限制：V3 尚未进入视频生成，当前失败点停在图像任务创建 401，因此这不是当前最上游 blocker。

4. `待验证 / 弱证据` endpoint / region 不匹配。
   - 证据：config region 是 `cn-beijing`，DashScope base_url 固定为 `https://dashscope.aliyuncs.com/api/v1`。
   - 限制：历史成功链路使用相同 DashScope base_url；V3 图像 endpoint 也与历史成功图像 endpoint 一致，所以不是最可能主因。

## 本轮未做

- 未修改任何 key。
- 未输出任何完整 key。
- 未重新运行 V3 图像生成。
- 未重新运行 V3 视频生成。
- 未用本地程序画图。
- 未生成低保真替代图。
- 未修改 `full.mp4`。
- 未修改 `dist/latest_review_pack/`。
- 未修改 `content_validation`。
- 未修改 `send_ready`。
- 未确定方案 B 最终口径。

## 下一个目标

如果继续 V3，下一轮应先让 V3 显式复用历史成功配置链路：

1. 确认 `FORMAL_API_DEMO_LOCAL_CONFIG` 或脚本参数指向 `/Users/fan/.config/video-factory/formal_api_demo.local.toml`。
2. 用脱敏 preflight 记录 V3 实际读取的 config path、provider、key 形态，不打印 key。
3. 先只跑 `wan2.7-image-pro` 最小创建检查；若仍 401，则说明 official config 中当前 key 也已不可用。
4. 若 official config 仍不可用，应在阿里百炼 / DashScope 控制台补齐新的通用 API Key，要求同时支持万相图像生成模型与图生视频模型；不需要把 key 发给 Codex，只需配置到本地私有配置。
