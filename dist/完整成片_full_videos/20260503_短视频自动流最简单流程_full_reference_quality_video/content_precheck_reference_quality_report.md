# content_precheck_reference_quality_report

- content_precheck_for_reference_quality：blocked
- content_validation：pending_user_chatgpt_review
- send_ready：false

| 检查项 | 状态 | 说明 |
| --- | --- | --- |
| API 真人真实入片 | blocked | TTS / visual API quota 阻断，liveportrait 未完成 |
| 项目 TTS 真实生成完整音轨 | partial | 用户要求重新提取后，独立 TTS 已成功生成 742.848 秒完整音轨；但正式 generation 的 voiceover 状态仍 failed，未进入 assembly |
| 云剪真实导出 | blocked | generation 未通过，assembly 未启动 |
| 用户录制素材承担中段主体 | partial | 素材已按时间码预处理并登记，但未进入最终云剪 |
| 中段剪辑继承 round34 与中段放大参考 | partial | cut map / contact sheet 已输出，但完整片未生成 |
| 完整文案保真入片 | blocked | 文本已写入，独立 TTS 已完整生成；但正式完整片未生成，不能说已入片 |
| visual route 不混 | partial | case route 已声明，API 卡片/真人生成未完成 |
| 没有敏感信息泄露 | partial | 火山素材未使用；Codex/Trae 遮挡框已进入预处理，但未做最终成片扫描 |
| 不是本地拼装片 | passed | 未使用 local assembly fallback |
| 不是短片 / 降级片 | passed | 未交任何降级视频 |
