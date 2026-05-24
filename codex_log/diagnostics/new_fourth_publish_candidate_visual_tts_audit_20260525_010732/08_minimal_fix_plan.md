# 最小修复方案

## 修复顺序

先修视觉层，再修 TTS route。

原因：当前 `full.mp4` 的视觉证据已经被白屏 / 灰边 / 黑块破坏，即使声音修对，也仍不能作为可发布候选片。

## visual_fix_first_step

重做隐私遮挡策略：

1. 删除或禁用 final-stage broad whiteout。
2. 把商品名、价格、佣金、月销、账号、路径、Drive 账号等改为局部 blur / 小块 mask。
3. 保留商品卡和表格结构的可读轮廓，让观众看懂“卡 -> 表 -> 复查清单”的证据链。
4. 重新跑 `subtitle_card_overlap_check` 和可读性检查，不能再用“字段被 washed out，由卡片承载机制”作为通过理由。

## tts_fix_first_step

重做 TTS route，而不是只换一个普通 voice：

1. 使用项目 B 语音路线：custom voice candidate `qwen-t...ac19` + `qwen3-tts-vc-realtime-2026-01-15`。
2. 加载 `tts_15s_b_pacing_locked_20260427` 作为节奏参考。
3. 生成 sanitized debug，必须写 `used_b_voice=true/false`、`used_b_pacing=true/false`，但不得写真实 key。
4. 若 B voice runtime 不支持长文案，应先生成 15-30 秒正式样段给用户 / ChatGPT 复审，不能再把普通 Serena 全片当成 B 声音。

## files_likely_to_modify_next

- 生成新第四期 publish candidate 的装配脚本或运行时 wrapper。
- TTS provider / TTS runner 中 voice route 参数传入处。
- privacy redaction / mask / blur / whiteout 生成逻辑。
- review pack validator：增加 `whiteout_visual_fail_gate` 与 `b_voice_route_gate`。

## blocked_if

- B voice custom route 授权不可用。
- 只能继续使用 `Serena` 或普通 realtime voice。
- 隐私遮挡只能靠大面积 whiteout 完成，无法保留证据可读性。
- 修复后仍出现 high severity subtitle/card/证据重叠。
