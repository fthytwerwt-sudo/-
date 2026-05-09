# reference 质量机制锁最小测试

## 1. 本轮定位

- `项目`: 《视频工厂》
- `测试目标`: 验证 DeepSeek 供料参与一次最小 `reference（参考）` 质量机制锁修正是否可执行
- `执行边界`: 只做最小规则收口，不做完整机制重构，不做视频、不改发布状态

## 2. 本轮供料来源

- `deepseek_generation_status`: `failed`
- `context_pack_validation`: `fallback_local_only`
- `pipeline_status`: `usable_with_fallback`
- `说明`: 本轮资料包来自 local fallback，不是 DeepSeek 真实任务稳定生成通过

本轮资料包给出的主要线索：

- `codex_source/00_codex_readme.md` 中仍有 `fixed_material_anchor（固定素材锚点）` 与强执行闸门语义，单独阅读时可能被误解成固定 SOP
- `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md`、`GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` 与 `GPT数据源/05_文案路由规则.md` 本身已经是反 SOP 口径，但仍值得再补一层“优先解释规则”

## 3. 本轮最小修正

- `已确认` 在 `GPT数据源/10_OPC一人公司闭环与多AI协作机制.md` 增加“优先按质量机制锁解释”的说明
- `已确认` 在 `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md` 增加“历史 reference 不得预先写死人物段次数 / 卡片数量 / 尾卡结构”的说明
- `已确认` 在 `GPT数据源/05_文案路由规则.md` 增加“block / segment 承载表是职责地图，不是固定镜头 SOP”的说明

## 4. 本轮确认结果

- `已确认` 本轮规则比之前更明确表达：锁质量，不锁流程
- `已确认` 本轮规则比之前更明确表达：文案驱动实时路由
- `已确认` 本轮规则比之前更明确表达：`reference` 不是镜头流程模板
- `已确认` 本轮规则比之前更明确表达：`locked reference` 不是每条内容必须照搬
- `已确认` 本轮规则比之前更明确表达：`visual route` 是展示结构区分，不是死流程

## 5. 边界检查

- `已确认` 本轮没有把 fallback 写成 DeepSeek 结论
- `已确认` 本轮没有把 DeepSeek 写成稳定供料通过
- `已确认` 本轮没有把 multi-agent runtime 写成已跑通
- `已确认` 本轮没有修改视频产物
- `已确认` 本轮没有修改 `dist/latest_review_pack/`
- `已确认` 本轮没有修改 `content_validation`
- `已确认` 本轮没有修改 `send_ready`
- `已确认` 本轮没有修改 `publish_status`
- `已确认` 本轮没有修改 `voice_validation`
- `已确认` 本轮没有修改 `final_voice_validated`

## 6. 一句话结论

本轮证明的是：即使 DeepSeek 真实任务仍依赖 `fallback_local_only`，Codex 也已经可以利用这份资料包完成一次最小、诚实、可验证的 `reference` 质量机制锁修正；这不代表 DeepSeek 真实生成稳定通过，也不代表完整 agent 协作闭环已跑通。

## 7. 下一个目标

基于这次最小测试结果，继续推进 `reference` 质量机制锁修正的下一轮收口。
