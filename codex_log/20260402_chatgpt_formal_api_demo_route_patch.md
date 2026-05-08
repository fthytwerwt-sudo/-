# 2026-04-02 ChatGPT 补充 formal_api_demo 当前执行路线

## 本轮目标

- 直接把用户本轮最新拍板写入仓库
- 避免后续继续沿用“视频 API 暂时不接 / 先纯本地出片”的旧口径
- 明确当前正式路线是：API 继续接，但默认本地 assembly 交付

## 执行前已确认事实

- 当前仓库里已经存在一部分“本地优先交付”的新判断
- 但仍存在旧口径残留，尤其是：
  - 视频 API 暂时不接
  - 先纯本地出片
  - 云端模板工厂 / 云端 assembly 仍像当前前置
- 用户本轮已明确纠正：
  - 自己比较价格不是为了放弃视频 API
  - 当前仍要接入视频 API
  - 只是最终默认走本地拼装

## 实际改动

新增文件：

- `project_source/10_formal_api_demo_current_route_patch_20260402.md`

该文件明确写入：

- 当前继续接 TTS API
- 当前继续接图片 / 视频生成 API
- 当前默认交付路径是本地 assembly
- `storage.space_name` / `assembly.template_id` / 模板工厂 / 云端 assembly 当前降为后续增强项
- 若与旧日志、旧摘要、旧判断冲突，以本轮用户拍板 + 本补丁文件为准

## 当前结果

- 当前最新执行路线已被直接写入仓库
- 后续接手时，不应再把 `formal_api_demo` 理解成“视频 API 暂时不接”

## 下一步建议

- 下一轮由 Codex 继续把这份补丁真正落实到：
  - `codex_log/latest.md`
  - `formal_api_demo_core.py`
  - `tests/test_formal_api_demo_pipeline.py`
- 目标是把“项目脑补丁”进一步变成“代码口径 + 测试口径 + latest 口径”一致
