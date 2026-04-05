# Latest

## 当前主结论

- 2026-04-06 pure PPT / 信息卡主线仍保持 cloud-only：
  - `北京区 OSS + 云剪工程 = 唯一 assembly 主路径`
  - `local assembly / local mp4` 已退出 pure PPT / 信息卡主线，不再作为 fallback / 兜底 / 应急正常交付
- 当前代码层已从“只有 gate / plan / blocked 占位”推进到：
  - `provider_assembly_implementation` 已接入
  - `run_assembly_pipeline()` 在前提齐全时会真实进入 cloud assembly 执行器
  - cloud assembly 执行器当前已补上：
    - OSS 上传
    - 云剪工程解析
    - 时间线生成
    - `UpdateEditingProject`
    - `SubmitMediaProducingJob`
    - `GetMediaProducingJob` 轮询
    - 导出结果解析
- 当前真实边界仍然保持诚实：
  - OSS / IMS / 云剪工程的非密钥参数已写回 repo
  - 本地配置文件已整理好，用户只需手填真实密钥
  - `config/formal_api_demo.local.toml` 属于 `.gitignore` / `local_only`
  - 真实云端导出仍待本地注入真实 AccessKey / Secret 后验证
  - 当前还不能把“已真实导出成功”写成 success

## 本轮关键执行事实

- 本轮实际改动：
  - `formal_api_demo_core.py`
    - 接入 `_execute_cloud_only_assembly`
    - assembly gate 不再把 `provider_assembly_implementation` 视为固定缺失
    - assembly result summary 改按真实 cloud assembly 结果出值
  - `formal_api_demo_cloud_assembly.py`
    - 新增云端 assembly 实现模块
    - 包含 OSS 上传、云剪工程解析、Timeline 构造、OpenAPI 请求签名、导出轮询与结果解析
  - `tests/test_formal_api_demo_pipeline.py`
    - 把“visual assets ready 仍 blocked”旧断言升级为“进入 cloud assembly 并返回 success”
  - `config/formal_api_demo.local.toml`
    - 已重写为 cloud-only 本地占位模板
    - 只保留用户手填字段，不再保留旧 `space_name` / `template_id` / `cloud` 旧口径

## 当前外部已确认状态包

- OSS bucket：`zvip1-video-beijing`
- OSS region：`cn-beijing`
- OSS endpoint：`oss-cn-beijing.aliyuncs.com`
- OSS bucket domain：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- OSS ACL：`private`
- RAM 用户：`video-factory-oss-1`
- IMS / ICE / 智能媒体服务：北京区已就绪
- 功能体验月包有效期：`2026-05-05 05:00:00`
- IMS storage address：`zvip1-video-beijing.oss-cn-beijing.aliyuncs.com`
- 云剪工程：`video-factory-ppt-master-v1`
- 云剪工程状态：草稿
- 编辑器可打开：是

## 本轮实际验证

- 已按读取范围复读命中的规则、项目脑、执行上下文、代码、配置与测试文件。
- 已执行：
  - `python3 -m unittest tests.test_formal_api_demo_pipeline.FormalApiDemoPipelineTests.test_assemble_non_dry_run_executes_cloud_assembly_when_visual_assets_ready`
  - `python3 -m unittest tests.test_formal_api_demo_pipeline`
  - `python3 -m py_compile formal_api_demo_core.py formal_api_demo_cloud_assembly.py scripts/assemble_formal_api_demo.py`
  - `git diff --check`
- 当前验证结果：
  - `30` 个测试通过
  - `py_compile` 通过
  - `git diff --check` 通过

## 当前交接提醒

- 仓库口径仍然是 cloud-only，而且代码已经接到真实云端 assembly 主链。
- 当前还差用户在本地文件里手填：
  - `aliyun_oss.access_key_id`
  - `aliyun_oss.access_key_secret`
- 填完后优先执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- `config/formal_api_demo.local.toml` 是 `.gitignore` / `local_only`：
  - 不会上传到 GitHub
  - 但它已经准备好，用户无需自己设计字段结构
