# 脱敏计划 redaction_plan

## 1. 火山引擎 API 特写边界

- 允许：只截取 API 管理页可安全展示区域，裁切 / 放大 / 打码后作为“API 能力入口”特写。
- 必须遮挡：手机号、短信验证码、API Key 明文、资源 ID、账号信息、URL 中可能暴露账号或资源的信息、任何密钥 / token / secret / AccessKey / 临时授权 URL。
- 不得证明：API 已全部接通、云端剪辑链路稳定、内容过线。

## 2. 本轮决策

- `已确认` PR #38 已记录火山引擎素材含手机号、验证码、API Key 管理页和资源 ID 痕迹。
- `已确认` 自动裁切无法保证对所有敏感视觉信息零风险。
- `已确认` 本轮执行 fallback：不使用火山引擎原画面，改用 API 信息卡。

## 3. 输出

- `redaction_report.md`：记录 fallback。
- `redaction_contact_sheet.jpg`：显示 API 信息卡 fallback 预览。
