# 隐私遮挡 / 洗白层审计

## 读取到的审片包记录

`privacy_risk_check.json`：

- status: `passed_for_human_review_after_strengthened_redaction`
- redaction_applied: true
- masked_areas: top navigation/account band, bottom system/path band, right account/sidebar band, left edge residue band
- redaction_strengthened_after_visual_spot_check: true
- notes: product names, prices, commission/monthly sales and table values are masked or washed out; cards/subtitles carry the mechanism.

## 问题判断

`redaction_strengthened_after_visual_spot_check` 很可能把隐私保护做成了大范围 whiteout，而不是局部遮挡敏感字段。这样虽然降低了隐私风险，但破坏了“真实录屏证据”和表格可读性：观众看到的是白屏 / 灰层 / 黑块，而不是商品卡和判断表。

## 具体风险

- 商品卡段：字段、图片、卡片内容被整体抹白，丢失“精选联盟商品卡很多”的证据感。
- V003 / V004 表格段：表格主体被洗白，观众只能看卡片解释，不能验证表格确实存在。
- 右上角黑块：保护账号区域可以成立，但块体过硬、位置过醒目，破坏画面可信度。
- 边缘灰层：看起来像渲染 bug，不像有意遮挡。

## 结论

privacy_redaction 技术上完成，但视觉上失败。下一轮不能复用当前 strengthened redaction 策略作为通过标准。
