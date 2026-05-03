# redaction_report

- status：passed
- 火山引擎素材是否使用：false
- 火山引擎 API 管理页特写：因敏感信息脱敏风险，未使用，改用信息卡说明 API 能力入口
- Trae 素材遮挡：seg07 / seg08 已配置底部遮挡框并进入 prepared visuals
- Codex 素材遮挡：seg14 已配置右侧与底部遮挡框并进入 prepared visuals
- 敏感信息最终成片扫描：passed；未使用火山引擎敏感页面特写，报告未写 secret / token / signed URL
- 云剪 timeline 脱敏：passed；`assembly/cloud_timeline.json` 已将 OSS signed URL 查询参数替换为 `<redacted_signature>`
- 是否发现提交 secret：false

敏感信息检查仅覆盖本轮生成报告、manifest 和所选素材路线；内容复审仍保持 pending。
