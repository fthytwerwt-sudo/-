# 脱敏报告 redaction_report

## 1. 是否使用火山引擎 API 特写

- 是否使用火山引擎 API 原画面：`false`
- 是否完成遮挡：`not_applicable_for_source_footage`
- 是否 fallback 到信息卡：`true`
- fallback 标记：`redaction_blocked_fallback_to_info_card`

## 2. 决策依据

- `已确认` 素材采集汇报已标记火山引擎素材存在手机号、短信验证码、API Key 管理页和资源 ID 痕迹。
- `已确认` 本轮无法仅靠自动裁切保证所有敏感视觉信息安全。
- `已确认` 因此 API 段使用信息卡解释“外部能力入口”，不使用火山引擎原画面。

## 3. 敏感信息检查结论

- `已确认` 本轮装配清单中没有火山引擎视频片段。
- `已确认` 未提交火山引擎未脱敏截图。
- `待验证` 视觉层最终仍需用户 / ChatGPT 看 `contact_sheet.jpg` 复审；Codex 不把该检查写成内容过线。

## 4. 禁止误读

- API 信息卡不证明 API 已接通。
- 云平台入口不证明云端剪辑稳定。
- 样片 MP4 不证明可发布。
