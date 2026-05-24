# 字幕 / 卡片图层审计

## 读取到的审片包记录

`subtitle_card_overlap_check.json`：

- status: `passed_for_human_review`
- high_severity_overlap_detected: false
- subtitle_zone: bottom band
- main_card_zone: upper-left or ending lower-middle

## 诊断

字幕和卡片没有直接造成主体白屏，但存在两个观感问题：

1. 底部字幕黑底较重，让画面下方压暗。
2. 卡片和字幕承担了过多信息转译，因为表格本体被洗白；这会让成片看起来像“卡片解释 + 失真录屏”，不是“真实录屏证据 + 卡片辅助”。

## 结论

字幕 / 卡片层不是首要修复点。应先修 redaction / whiteout，再评估字幕黑底高度和卡片透明度。
