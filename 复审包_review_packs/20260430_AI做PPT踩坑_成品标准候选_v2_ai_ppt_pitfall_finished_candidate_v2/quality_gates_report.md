# quality gates report

| gate | result | evidence |
| --- | --- | --- |
| source gate | pass | 正反录屏、元素娃娃开场、PR #7 A reference、PR #8 规则、round34 参考均可读。 |
| sassy-card gate | pass_for_candidate_review | 三张独立图、prompt、contact sheet、visual-verdict 报告已输出；最终搞笑感待用户复审。 |
| editing-inheritance gate | pass_for_candidate_review | 已输出 round34 剪辑继承对照；没有重走 PR #14 18-shot 教程结构。 |
| runtime gate | pass | full candidate 时长约 81.76s，位于 70-90s 推荐区间内，低于 100s 硬上限。 |
| layout gate | pass_for_candidate_review | 已输出 layout_gate_report；未触发 layout_validation_failed。 |
| evidence chain gate | pass_for_candidate_review | 反面能看出一句糊话 -> 文字方案；正面能看出交付标准 -> PPT 预览；6m31 和 16 页预览入片。 |
| validation-split gate | pass | summary 分开写 technical/content/sassy/editing/layout/send_ready；未把技术成功写成内容成功。 |

## 边界

- `content_validation = pending_user_chatgpt_review`
- `send_ready = false`
- `voice_status = temporary_no_voice_preview`
- `final_voice_validated = false`
