# 声音路线听审单

## 阶段结论

- `已确认` 本轮没有生成新的 Doubao / Azure 候选音频。
- `已确认` 当前主阻塞不在听感微调，而在执行面：
  - Doubao 2.0：`provider implementation` 未接入
  - Azure：当前仓库无 `provider / route family / SDK / config` 执行面
- `已确认` 阿里 `prosody-only` 只算历史失败线，不回退用于本轮候选生成。

## 统一对比文案

来源：`route_plan.json -> block_01.seg01_hook`

```text
豆包给你出的方案，你有没有觉得——
能看，但用不了？
最后你还是自己重写了一遍？

这不是豆包的问题。
是你问的方式，就决定了它只能给你那种结果。
```

## 路线审计表

| 路线 | 当前状态 | 是否有真实执行面 | 当前结论 |
| --- | --- | --- | --- |
| Doubao 2.0 / `doubao_openspeech_v3` | `blocked` | 否 | 代码只拆出了 route family；probe 前即报 `provider implementation 尚未接入` |
| Azure fallback / `zh-CN-XiaoxiaoNeural` | `blocked` | 否 | 当前仓库没有 Azure provider、SDK、配置字段或 route family |
| 阿里 `prosody-only` 历史线 | `rejected_history` | 是 | 可执行不等于可用；已被 `latest.md` 判为旧线不合格，不纳入本轮 |

## 四项结论

| 维度 | Doubao 2.0 | Azure fallback | 阿里历史线 | 本轮总判断 |
| --- | --- | --- | --- | --- |
| 自然度 | `待验证` | `待验证` | `已确认不合格` | 当前没有新样本，不能给通过结论 |
| 向导感 | `待验证` | `待验证` | `部分成立但未过线` | 当前没有形成“轻陪伴、像游戏向导”的新对比 |
| 停顿与韵律 | `待验证` | `待验证` | `已确认不合格` | 旧线已失败，新线未生成 |
| 播音腔 / AI 感 | `待验证` | `待验证` | `已确认 AI 感明显` | 当前不能把任何新路线写成已达标 |

## 阻塞归因

1. `已确认` Doubao 2.0 不是“缺调参”，而是缺 provider 实现。
2. `已确认` Azure 不是“缺 key”，而是当前仓库没有接入面。
3. `已确认` repo 内 `config/formal_api_demo.local.toml` 当前还缺 `auth.api_key` 与 `tts.voice`，并且主配仍指向阿里。
4. `部分成立` 脚本默认会优先读 `~/.config/video-factory/formal_api_demo.local.toml`；该处存在可执行的阿里配置，但这不改变本轮主路线 blocked 结论。

## 若下一轮解锁，听审必须看

- `自然度`：不能一听就是念稿。
- `向导感`：要像轻陪伴式游戏向导，不像播报员。
- `停顿与韵律`：停顿按语义，不按标点机械切。
- `播音腔 / AI 感`：不能是新闻腔、客服腔、朗读腔。

## 本轮产物状态

- `voice_route_report.json`：已写入
- `voice_listen_sheet.md`：已写入
- `voice_candidates/`：仅写入阻塞说明，不含新候选音频
