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

- `自然度`：`待验证`，需要人工试听确认。
- `向导感`：`待验证`，需要人工试听确认。
- `停顿与韵律`：`待验证`，需要人工试听确认。
- `播音腔 / AI 感`：`待验证`，需要人工试听确认。

## 当前结论

- `推测` 机器侧暂定主路线：`qwen3-tts-instruct-flash-realtime + Serena`。
- `待验证` 该结论仍需人工试听，不得直接写成最终过线。
