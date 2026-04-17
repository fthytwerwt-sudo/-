# 阿里内部声音候选听审单

## Round 4 probe 文案

```text
豆包给你出的方案，你有没有觉得——

能看，但用不了？

最后你还是自己重写了一遍。

这不是豆包的问题。

是你问的方式，决定了它只能给你那种结果。
```

## 候选结果

| 候选 | 模型 | 音色 | 状态 | 目标 |
| --- | --- | --- | --- | --- |
| `E1` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：句尾假上扬；说完就收 |
| `E2` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：功能词 / 连接词被抬高 |
| `E3` | `qwen3-tts-instruct-flash-realtime` | `Serena` | `success` | 主要解决：验证更低 pitch 是否压住局部上扬且不沉闷 |

## 四项核心维度

- `句尾有没有往上挑`：听陈述句尾是不是还往上悬，而不是往下收。
- `功能词有没有被抬高`：听“你 / 就 / 但 / 其实 / 然后 / 所以 / 是”是不是还在抢重音。
- `整体有没有在等你回应的悬置感`：听句尾是不是像还没说完，在等对方接话。
- `pitch 下压后有没有变沉闷`：听音高压低后是不是丢掉了在场感，变得发闷。

## 当前分类

- `已确认` 当前暂定定版：`E1`
- `已确认` 当前备选：`E2`
- `已确认` 当前淘汰：`E3`

## 当前结论

- `已确认` 当前正式 B 线暂定定版：`E1`。
- `已确认` 当前正式备选：`E2`。
- `已确认` 当前正式淘汰：`E3`。
- `已确认` 这表示“B 线当前已收口到 E1”，不代表整条内容或整条样片已过线。

## Round 4 AB review bundle

- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/01_暂定第一名_E1.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/02_备选_E2.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/03_淘汰_E3.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/00_三候选顺序连听.wav`
- `/Users/fan/Documents/视频工厂/dist/20260417_豆包的正确打开方式_vnext/voice_ab_review_bundle_round4/试听说明.md`
