# 阿里内部声音候选听审单

## Round 3 probe 文案

```text
豆包给你出的方案，
你有没有觉得——

能看，但用不了？

最后你还是自己重写了一遍？

这不是豆包的问题。

是你问的方式，
就决定了它
只能给你那种结果。
```

## 候选结果

| 候选 | 模型 | 音色 | 状态 | 目标 |
| --- | --- | --- | --- | --- |
| `C1` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：功能词 / 语气词抬高感 |
| `C2` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：句内快慢层次 / 停顿分布不像真人 |
| `C3` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：情绪微调不对 / 验证 pitch_rate 0.97 是否压过头 |

## 四项核心维度

- `功能词是否还被抬高`：听“就 / 还是 / 但 / 先 / 再 / 所以”是不是仍然被读得太重。
- `停顿是否还落在每个标点后`：听停顿是不是机械卡在逗号句号，而不是落在语义转折前。
- `句内快慢层次是否更像真人`：听铺垫部分是否更顺滑带过，关键判断是否更稳。
- `情绪是否更在场`：听它像不像一个真的在分享发现的人，而不是在念稿。

## 当前分类

- `暂定第一名`：`C2`
- `备选`：`C1`
- `淘汰`：`C3`

## 当前结论

- `推测` 当前轮暂定第一名：`C2`。
- `推测` 当前轮备选：`C1`。
- `推测` 当前轮淘汰：`C3`。
- `待验证` 上述结论仍需人工听审，不得直接写成最终过线。

## Round 3 AB review bundle

- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/01_暂定第一名_C2.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/02_备选_C1.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/03_淘汰_C3.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/00_三候选顺序连听.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round3/试听说明.md`
