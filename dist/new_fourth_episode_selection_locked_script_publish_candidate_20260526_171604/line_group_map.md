# line_group_map

本轮按锁稿重新拆分，每个非空自然句/短句为一个 `line_group`，旧 21 组仅作为素材时间码参考。

| line_group_id | narration_text | material | status |
|---|---|---|---|
| `LG001` | 朋友们，你有没有发现，现在做带货，最贵的已经不是拍一条视频了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG002` | 也不是剪辑。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG003` | 也不是买一个样品。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG004` | 最贵的是，你前面测错商品的成本。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG005` | 你刷半天精选联盟，看到的全是商品卡。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG006` | 这个佣金高。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG007` | 那个销量好。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG008` | 这个图片看起来很精致。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG009` | 那个价格好像也挺适合冲动消费。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG010` | 但你翻到最后会发现一个很尴尬的问题： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG011` | 你看了二十个商品，收藏了一堆链接，最后还是不知道，到底哪个值得你继续测。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG012` | 这才是最累的。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG013` | 不是商品不够多。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG014` | 是商品太多了以后，每一个看起来都像机会，每一个又都像坑。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG015` | 有的商品，佣金看起来很高。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG016` | 但客单价太低，你拍一条视频的时间成本，可能都不一定回得来。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG017` | 有的商品，销量看起来不错。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG018` | 但 SKU 太复杂，观众看完根本不知道该买哪一款。 | V003/V004 00:51-01:30 / 00:39-00:51 | `blocked_unresolved_core_evidence_mismatch` |
| `LG019` | 有的商品，图片特别好看。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG020` | 但店铺分和商品分一低，你视频拍得再顺，转化也可能卡住。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG021` | 还有的商品，看起来特别适合做内容。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG022` | 但退货风险一高，后面全是售后坑。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG023` | 所以我现在越来越觉得，选品不是看哪个商品“看起来能卖”。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG024` | 第一步应该是： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG025` | 先判断它值不值得你继续花时间测。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG026` | 以前这一步，我都是自己一个个翻。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG027` | 打开精选联盟。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG028` | 输入一个品类。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG029` | 点开商品卡。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG030` | 看价格。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG031` | 看佣金。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG032` | 看月销。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG033` | 再看店铺分、商品分、评价、退货风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG034` | 看完一个，脑子里记一下。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG035` | 再看下一个。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG036` | 然后看到第十个的时候，前面那个商品到底哪里好，哪里有风险，其实已经忘得差不多了。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG037` | 你以为自己是在筛商品。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG038` | 其实你是在靠记忆硬扛一堆零散信息。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG039` | 所以这次我换了一个做法。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG040` | 我不想再自己一个个翻了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG041` | 我直接让 Codex 操作我的电脑，先帮我跑一轮选品初筛。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG042` | 注意，我不是问它一句： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG043` | “帮我找一个爆品。” | V001 00:15-01:24 | `declared_contextual_match` |
| `LG044` | 这种问题太空了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG045` | 它最后大概率会给你一堆听起来很有道理的建议。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG046` | 比如什么高需求、低竞争、高复购、适合内容化。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG047` | 这些话不能说错。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG048` | 但你看完还是不知道，今天到底先看哪个商品。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG049` | 我这次给 Codex 的任务是很具体的。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG050` | 不是让它替我赌。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG051` | 而是让它先帮我把商品卡里的信息拆出来。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG052` | 你看这里，它不是在聊天框里随便回我一句建议。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG053` | 它是真的开始在我的电脑上操作。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG054` | 先进入选品页面。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG055` | 再输入品类词。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG056` | 然后一张一张翻商品卡。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG057` | 它看的也不是这个商品顺不顺眼。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG058` | 它会先看几个最硬的字段。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG059` | 第一个，客单价。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG060` | 这个价格带，用户到底能不能接受？ | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG061` | 第二个，佣金。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG062` | 不是佣金越高越好，而是要看它能不能覆盖你后面的内容成本和时间成本。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG063` | 第三个，销量信号。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG064` | 有没有人买过？是不是完全冷启动？还是已经卷到红海了？ | V001 00:15-01:24 | `declared_contextual_match` |
| `LG065` | 第四个，店铺分。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG066` | 店铺本身靠不靠谱。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG067` | 第五个，商品分。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG068` | 商品口碑有没有明显问题。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG069` | 第六个，退货和风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG070` | 这个品会不会看起来很好卖，但后面全是售后。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG071` | 第七个，内容可拍性。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG072` | 不是所有商品都适合做短视频。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG073` | 有些商品你看着不错，但你拍出来就是一张商品图加几句废话。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG074` | 这样的品，对我现在的账号来说，未必值得测。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG075` | 你看，这一步其实已经和我自己手动翻不一样了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG076` | 我自己看的时候，是边看边想。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG077` | Codex 做的时候，是边看边记录。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG078` | 它会把这些商品先整理成一张候选表。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG079` | 原来在页面上，它们只是一张张商品卡。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG080` | 到了表格里，就变成了一行一行可以判断的记录。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG081` | 商品名是什么。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG082` | 客单价大概在哪个区间。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG083` | 佣金空间怎么样。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG084` | 有没有销量信号。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG085` | 店铺分怎么样。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG086` | 商品分怎么样。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG087` | 退货风险在哪里。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG088` | 内容能不能拍。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG089` | 为什么留下。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG090` | 为什么不能直接上。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG091` | 下一步还要核什么。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG092` | 这些东西一进表，选品这件事就不再是靠感觉了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG093` | 它变成了一个可以逐项核对的判断过程。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG094` | 我觉得这里最关键。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG095` | Codex 没有直接跟我说： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG096` | “这个商品能爆。” | V001 00:15-01:24 | `declared_contextual_match` |
| `LG097` | 它也没有跟我说： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG098` | “这个商品你马上去拍。” | V001 00:15-01:24 | `declared_contextual_match` |
| `LG099` | 它真正帮我做的是另一件更现实的事： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG100` | 先把一堆看起来都能卖的商品，分成几类。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG101` | 哪些只是看起来热闹。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG102` | 哪些佣金不错，但风险还没核。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG103` | 哪些内容好拍，但价格可能撑不起成本。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG104` | 哪些可以进入下一轮复查。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG105` | 哪些现在先别碰。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG106` | 这比一句“推荐你做这个品”有用多了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG107` | 因为我真正缺的，不是一个拍脑袋的答案。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG108` | 我缺的是一个能帮我减少试错的判断表。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG109` | 比如它会把商品先缩成几个更窄的方向。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG110` | 像高客单杯具。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG111` | 家居香氛。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG112` | 键帽套装。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG113` | 礼物类小物。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG114` | 这些不是最终结果，只是第一轮方向。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG115` | 然后它会继续往下收。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG116` | 从几个方向里，再挑出几个具体商品卡。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG117` | 最后不是让我继续翻二十个商品。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG118` | 而是告诉我： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG119` | 先复查这四个。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG120` | 为什么是这四个？ | V001 00:15-01:24 | `declared_contextual_match` |
| `LG121` | 因为它们在佣金、内容可拍性、价格带和风险之间，至少有继续核验的空间。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG122` | 但每一个都还不能直接拍。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG123` | 因为还要看店铺分。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG124` | 还要看退货风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG125` | 还要看 SKU 会不会太复杂。 | V003/V004 00:51-01:30 / 00:39-00:51 | `blocked_unresolved_core_evidence_mismatch` |
| `LG126` | 还要看商品图和卖点能不能拆成一条短视频。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG127` | 所以最后你看，结果不是一个“爆品答案”。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG128` | 结果是一张复查表。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG129` | 这里面会写清楚： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG130` | 第一个商品，为什么留下。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG131` | 第二个商品，最大的风险是什么。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG132` | 第三个商品，内容能不能拍。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG133` | 第四个商品，下一步要去巨量百应核什么。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG134` | 这才是我觉得 AI 参与电商真正有价值的地方。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG135` | 不是让它替我做一个玄学判断。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG136` | 而是先把原本乱七八糟的商品信息，整理成我能决策的东西。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG137` | 而且它最后不是把一堆截图丢给我。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG138` | 它会把文件和表格整理好。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG139` | 放到云盘里。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG140` | 我打开以后能看到清清楚楚的记录。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG141` | 商品名。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG142` | 客单价。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG143` | 佣金。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG144` | 销量信号。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG145` | 店铺分。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG146` | 商品分。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG147` | 内容可拍性。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG148` | 主要风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG149` | 适不适合我。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG150` | 为什么适合。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG151` | 下一步还要核什么。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG152` | 以前我选品，最痛苦的是信息散在各个页面里。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG153` | 商品页一个信息。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG154` | 聊天框一个判断。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG155` | 截图里一个字段。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG156` | 脑子里还要记着刚才那个商品哪里不错。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG157` | 现在至少第一轮初筛以后，它能变成一个地方能看的表。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG158` | 我不用在一堆标签页里反复横跳。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG159` | 也不用靠记忆硬撑。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG160` | 更重要的是，如果你连表格都不想看，它还可以直接回到聊天框里给我总结。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG161` | 比如它会告诉我： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG162` | 目前最值得先复查的是哪几个商品。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG163` | 为什么留下它。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG164` | 风险在哪里。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG165` | 下一步先核什么。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG166` | 这个品佣金空间可以，但要先核店铺分和退货风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG167` | 那个品内容可拍性不错，但客单价可能不一定支撑成本。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG168` | 还有一个品看起来数据不错，但 SKU 太复杂，观众看完可能不知道该买哪款。 | V003/V004 00:51-01:30 / 00:39-00:51 | `blocked_unresolved_core_evidence_mismatch` |
| `LG169` | 它不会直接让我冲。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG170` | 它会把每个商品的“不确定”也写出来。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG171` | 这点很重要。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG172` | 因为电商里最危险的，不是你不知道哪个商品好。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG173` | 而是一个商品看起来很好，但你不知道它的坑在哪。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG174` | 你觉得佣金高。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG175` | 但没算时间成本。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG176` | 你觉得销量好。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG177` | 但没看竞争。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG178` | 你觉得内容好拍。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG179` | 但没看退货风险。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG180` | 你觉得商品图好看。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG181` | 但没看店铺和商品评分。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG182` | 所以我现在更想让 AI 做的，不是替我选一个看起来很爽的答案。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG183` | 而是先把这些坑帮我摊开。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG184` | 让我知道这个商品到底是： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG185` | 可以继续核。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG186` | 暂时先放着。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG187` | 还是根本不适合我现在去测。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG188` | 这里面还有一个区别。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG189` | 普通 AI，你问它： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG190` | “我适合做什么商品？” | V001 00:15-01:24 | `declared_contextual_match` |
| `LG191` | 它可能很快给你十几个方向。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG192` | 家居百货。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG193` | 小家电。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG194` | 母婴。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG195` | 宠物。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG196` | 数码配件。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG197` | 你看完会觉得都对，但也都没法开始。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG198` | 而 Codex 这种执行型 AI，如果你让它直接操作电脑，它可以把任务往前推一步。 | V001/V003/V004 旧审计仅有商品卡/表格/聊天输出参考，无直接 computer-use 操作证据 | `blocked_unresolved_core_evidence_mismatch` |
| `LG199` | 它不是只回答你。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG200` | 它会去页面里看。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG201` | 去整理。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG202` | 去记录。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG203` | 去归类。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG204` | 再把结果回到你能看懂的表格和聊天框里。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG205` | 这就从“建议”变成了“工作”。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG206` | 当然，这里一定要说清楚。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG207` | 这不代表 Codex 已经帮我选出了爆品。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG208` | 也不代表这些商品一定能卖。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG209` | 更不代表佣金一定能覆盖成本。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG210` | 现在这一步，只能叫选品初筛。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG211` | 它的价值是： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG212` | 先把明显不适合的排掉。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG213` | 把值得复查的留下。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG214` | 把下一步要核的字段写清楚。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG215` | 后面我还要继续看样品、售后、履约、退货风险和内容测试结果。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG216` | 只有这些都过了，才值得进入第一条内容测试。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG217` | 但哪怕只是做到这一步，对我来说已经很有用了。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG218` | 因为我少掉了一轮最乱、最耗眼睛、最容易凭感觉乱选的过程。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG219` | 以前是我在商品页里乱翻。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG220` | 现在是 Codex 先帮我把商品变成判断表。 | V003/V004 V003 00:33-01:30 / V004 00:27-00:51 | `blocked_readability_unresolved` |
| `LG221` | 以前是我看完一堆商品还不知道先测哪个。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG222` | 现在是它先告诉我： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG223` | 这几个值得复查。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG224` | 这个风险最大。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG225` | 这个下一步先核。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG226` | 这个暂时别碰。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG227` | 我觉得这才是 AI 做电商最现实的用法。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG228` | 不是自动赚钱。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG229` | 不是一键爆单。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG230` | 不是替你拍板。 | V004/summary_card 00:39-00:51 + 边界卡 | `declared_match_needs_card_placement_check` |
| `LG231` | 而是先帮你把复杂选择整理成一个清楚的判断过程。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG232` | 你可以不相信 AI 的最终结论。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG233` | 但你可以让它先替你少走一圈弯路。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG234` | 先把二十张商品卡，整理成四个复查对象。 | V004 00:00-00:06 / 00:27-00:51 | `blocked_readability_unresolved` |
| `LG235` | 先把一堆散乱字段，整理成一张表。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG236` | 先把“我觉得好像可以”，变成“我知道下一步该核什么”。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG237` | 所以如果你现在还在一个个手动翻精选联盟。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG238` | 可以先别急着拍视频。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG239` | 也别急着问 AI 哪个品能爆。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG240` | 你先让它做一件事： | V001 00:15-01:24 | `declared_contextual_match` |
| `LG241` | 把商品卡拆成表。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG242` | 把风险写出来。 | V001/V003 V001 00:15-01:24 / V003 00:51-01:30 | `declared_match_needs_readability_guard` |
| `LG243` | 把下一步复查项列清楚。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG244` | 过了这张表，再拍。 | V001 00:15-01:24 | `declared_contextual_match` |
| `LG245` | 没过这张表，就别浪费时间拍视频。 | V001 00:15-01:24 | `declared_contextual_match` |
