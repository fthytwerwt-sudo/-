# 阿里内部声音候选听审单

## 统一测试文案

```text
豆包给你出的方案，你有没有觉得——
能看，但用不了？
最后你还是自己重写了一遍？

这不是豆包的问题。
是你问的方式，就决定了它只能给你那种结果。
```

## 候选结果

| 候选 | 路线 | 模型 | 音色 | 状态 | 备注 |
| --- | --- | --- | --- | --- | --- |
| `A1_qwen3_serena_light` | `primary` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 已落盘，待人工试听 |
| `A2_qwen3_serena_steady` | `primary` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 已落盘，待人工试听 |
| `A3_qwen3_cherry_hint` | `primary` | `qwen3-tts-instruct-flash-realtime` | `Cherry` | `success` | 已落盘，待人工试听 |
| `B1_cosy_plus_longanling` | `fallback` | `cosyvoice-v3-plus` | `longanling_v3` | `failed` | {"request_id":"93cac5b8-463e-90bb-a464-0a5bdf178212","code":"InvalidParameter","message":"[cosyvoice:]Engine return error code: 418"} |
| `B2_cosy_flash_longanqin` | `fallback` | `cosyvoice-v3-flash` | `longanqin_v3` | `failed` | {"code":"AllocationQuota.FreeTierOnly","message":"The free tier of the model has been exhausted. If you wish to continue access the model on a paid basis, please disable the \"use free tier only\" mode in the management console.","request_id":"59b25dfb-208e-969c-9519-59fd803416c3"} |
| `B3_cosy_flash_longanwen` | `fallback` | `cosyvoice-v3-flash` | `longanwen_v3` | `failed` | {"code":"AllocationQuota.FreeTierOnly","message":"The free tier of the model has been exhausted. If you wish to continue access the model on a paid basis, please disable the \"use free tier only\" mode in the management console.","request_id":"270b788e-4650-9eaf-9e4a-1c5c09f84633"} |

## 四项核心维度

- `自然度`：听它是不是像“先理解再说”，而不是字字一样重的机器念稿。
- `向导感`：听它是不是像在旁边带你过一遍，而不是在上课、播报或推销。
- `停顿与韵律`：听停顿是不是跟语义走，而不是机械地按标点切片。
- `播音腔 / AI 感`：听有没有新闻腔、客服腔、朗读腔，还是更像真实的人在说话。

## 当前分类

- `暂定第一名`：`A1_qwen3_serena_light`
- `备选`：`A2_qwen3_serena_steady`
- `淘汰`：`A3_qwen3_cherry_hint`

## 当前结论

- `推测` 当前轮暂定第一名：`qwen3-tts-instruct-flash-realtime + Serena`（`A1_qwen3_serena_light`）。
- `推测` 当前轮备选：`qwen3-tts-instruct-flash-realtime + Serena`（`A2_qwen3_serena_steady`）。
- `推测` 当前轮淘汰：`qwen3-tts-instruct-flash-realtime + Cherry`（`A3_qwen3_cherry_hint`）。
- `已确认` 选 `A1` 的原因：
  - 更贴近“轻陪伴 / 游戏向导”的主目标
  - 不像 `A2` 那样过于收紧
  - 也不像 `A3` 那样偏轻提醒
- `已确认` 不选 `A2` 做第一名的原因：
  - 更克制、更稳，适合作为备选，但主目标的人味和陪伴感可能更弱
- `已确认` 淘汰 `A3` 的原因：
  - 提醒感更强，不是当前轮要的主导感觉
- `待验证` 上述结论仍需人工试听，不得直接写成最终过线。

## AB review bundle

- `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/01_暂定第一名_A1_qwen3_serena_light.wav`
- `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/02_备选_A2_qwen3_serena_steady.wav`
- `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/03_淘汰_A3_qwen3_cherry_hint.wav`
- `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/00_三候选顺序连听.wav`
- `dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle/试听说明.md`
