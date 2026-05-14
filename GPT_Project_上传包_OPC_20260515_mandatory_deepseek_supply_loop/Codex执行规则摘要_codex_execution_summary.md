# Codex 执行规则摘要 codex_execution_summary

## 本包定位

本包用于把《视频工厂》的 DeepSeek 协作机制同步给 GPT Project。

`已确认` 本包只同步机制规则、脚本字段、schema、fixture、日志和路径索引，不包含视频、音频、图片或 `dist/latest_review_pack/`。

## 当前强制链路

```text
Codex route_decision（路由判断）
-> deepseek_supply_gate（DeepSeek 供料闸门）
-> create_supply_request（创建供料请求任务卡）
-> run_deepseek_pre_supply（执行前 DeepSeek 供料）
-> Codex read / audit / execute（Codex 读取 / 审计 / 执行）
-> Codex vertical_completion（Codex 二次补全）
-> run_deepseek_post_risk_review（执行后 DeepSeek 风险复核）
-> Codex validation / sync（Codex 验证 / 同步）
```

## 状态边界

- `DeepSeek` 每轮默认只读供料，不写文件、不 commit、不 push、不拍板项目事实。
- `Codex` 是唯一写入执行层，必须补齐影响文件、字段、脚本、schema、fixture、日志、路径索引和上传包。
- `fallback_local_only（本地兜底）` 不等于 DeepSeek 结论。
- token 未观察到减少时，不得写 DeepSeek 已深度参与。
- 本包生成不代表用户已上传 GPT Project UI。
- 本包生成不代表 `multi-agent runtime（多 agent 运行时）` 已稳定跑通。
