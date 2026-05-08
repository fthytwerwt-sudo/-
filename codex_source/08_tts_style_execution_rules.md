# TTS 风格执行规则

## 1. 当前这条子线的执行目标

当前 `formal_api_demo` 的 TTS 子线执行目标是：

- 在阿里 CosyVoice 已接通前提下
- 把声音目标稿稳定落进真实请求体
- 用固定测试文案做可复审的多版本对照
- 把“当前最推荐候选版”压缩到足够小的范围

当前不做的事：

- 不推进 assembly
- 不推进视频生成
- 不扩项目边界
- 不把“更接近”写成“已定稿”

## 2. 当前默认模型与 voice

当前默认技术路线固定为：

- `provider.name = aliyun_bailian`
- `tts.api_route_family = aliyun_bailian_cosyvoice`
- `tts.model = cosyvoice-v3-flash`
- `tts.voice = longanyang`

默认顺序：

1. 先在这条路线内调 instruction
2. 再调 `speech_rate / pitch_rate / volume`
3. 再考虑换 voice
4. 最后才考虑换模型族

## 3. instruction 应该怎么写

instruction 当前不应再只写粗粒度单一情绪词。

当前推荐写法：

- 先用最短可执行句式表达角色或场景
- 再补情绪词
- 保持短、硬、可执行，不写散文化长段说明
- 优先贴近已验证成功的句式，不要一上来写自由长 prose

当前推荐包含的要素：

- 年轻中文男声 / 中低音
- 冷静克制 / 利落 / 判断感
- 短句推进
- 重点判断词前轻微停顿
- 句尾收干净，不上扬，不拖音
- 不要客服感 / 播音感 / 广告感 / 演讲感

当前不推荐的写法：

- 只写 `neutral` / `disgusted` 之类单情绪词
- 完全自由的长中文 prose 风格稿
- “你现在扮演……”这类未验证固定句式的长描述
- 把多个完全不同人设混进一个 instruction
- 为了“更强”直接推到激昂或演讲感

当前已验证到的限制：

- 在 `aliyun_bailian_cosyvoice + cosyvoice-v3-flash + longanyang` 这条线上
- 自由中文风格稿会被远端以 `InvalidParameter / engine 428` 拦下
- “你现在扮演……”式的结构化中文也会被同样错误拦下
- 因此当前 instruction 的可承载空间比预想更窄

## 4. 当前执行标准

每一轮都应遵守：

- 使用同一段固定测试文案
- 所有版本都必须是真实 non-dry-run
- request debug 里必须能确认风格稿真实进请求体
- 输出文件命名必须稳定，便于复审对比
- 每轮都要有结构化汇总文件

当前汇总文件至少应写清：

- 每版 `instruction`
- 每版 `speech_rate`
- 每版 `pitch_rate`
- 每版 `volume`
- 当前最推荐候选版
- 为什么推荐它
- 这份推荐是否仍待人工试听确认

## 5. 本轮验收标准

当前轮次不按“有没有声音”验收，而按以下标准验收：

- 至少一版要明显比旧 A 更接近目标
- 不能像客服播报
- 不能像新闻播音
- 不能像广告配音
- 至少明显成立两项：
  - 冷静
  - 利落
  - 判断感

补充边界：

- 若没有人工试听，不得把“当前推荐候选”写成“最终已定稿”
- 当前推荐只能写成“最值得优先复审的版本”

## 6. 失败后的分叉顺序

若结果仍不够，当前固定分叉顺序是：

1. 先改 instruction
2. 再改 `speech_rate / pitch_rate / volume`
3. 再考虑换 voice
4. 最后才考虑换模型族

只有在以下情况时才进入下一层：

- instruction 已经具体、稳定、仍明显不对味
- rate / pitch / volume 的可用空间已基本压实
- 真实试听已证明当前 `longanyang` 不适合承载目标
- 再往下才允许判断 `cosyvoice-v3-flash` 本身承载不足

## 7. 当前最小失败层判定

若一轮结束后仍不够，必须把问题压到最小层，不能模糊汇报。

当前允许的最小失败层只有：

- instruction 仍太粗
- 当前 voice 不合适
- 当前 model 承载不足
- 代码桥接限制

不允许直接跳结论说“阿里路线不行”，除非已经逐层排掉以上更小层级。

当前新增的经验结论：

- 若 richer instruction 已真实进请求体，但四版全部被远端 `InvalidParameter / 428` 拦下
- 最小失败层优先记为：
  - 当前 route/model/voice 的 instruction 合同限制
- 这时不要误判成：
  - rate / pitch / volume 失效
  - assembly 问题
  - 视频生成问题
