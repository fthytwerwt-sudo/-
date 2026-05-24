# 视觉异常根因判断

## 结论

artifact_origin = `redaction_layer + whiteout_privacy_mask + canvas_or_edge_mask`

已确认：异常不是源素材自带。关键证据是同一时间点下：

- V001 / V003 / V004 源素材正常显示浏览器或表格内容，没有大面积主体洗白。
- `visual_no_audio.mp4` 与 `visual_with_captions.mp4` 在多处仍保留可读主体。
- 最终 `full.mp4` 额外出现白屏 / 洗白主体、右上角黑块、左侧 / 顶部灰边。

## 分层判断

| 异常 | 最可能来源 | 证据 | 是否源素材问题 |
| --- | --- | --- | --- |
| 大面积白屏 / 洗白 | final-stage strengthened privacy redaction / whiteout layer | `privacy_risk_check.json` 明确写 masked or washed out；中间视频可读，final 不可读 | 否 |
| 右上角黑块 | right account/sidebar band privacy mask | `privacy_risk_check.json` 的 masked_areas 包含 right account/sidebar band；多时间码固定出现 | 否 |
| 左侧 / 顶部灰边 | edge privacy masks + canvas/letterbox/padding safe band | masked_areas 包含 top navigation/account band、left edge residue band；成片比源素材多出统一边缘层 | 部分源窗口有边界，但异常遮挡由成片新增 |
| 底部黑带 | subtitle zone / subtitle background | `subtitle_card_overlap_check.json` 写 subtitle_zone = bottom band；它解释底部黑带，不解释中间白屏 | 否 |
| 卡片遮挡 | card overlays | 卡片存在但不覆盖多数主体白屏区域；不是主因 | 否 |

## 为什么不是字幕 / 卡片主因

字幕黑底集中在底部，卡片预算集中在 LG001 / LG008 / LG010 / LG013 / LG015 / LG019 / LG021。白屏洗白却在商品卡区、表格主体区、页面中部持续出现，且与审片包里“字段被 washed out”的隐私策略一致。

## 为什么不是源素材主因

源素材同类时间段只存在正常录屏边界、浏览器空白和表格小字；没有 final 中把商品卡 / 表格主体整体抹白的层。最终异常应归入装配 / 隐私遮挡策略问题。
