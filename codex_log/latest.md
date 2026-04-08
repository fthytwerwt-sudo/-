# Latest

## 当前主结论

- 2026-04-08 当前仓库已把《视频工厂》正式默认主线收口为：
  - `人物`
  - `用户自己的真实录制素材`
  - `少量 PPT / 图片辅助`
- 正式 assembly 继续固定为：
  - `北京区 OSS + 云剪 cloud-only`
- `local assembly` 没有被写回默认主路径。
- `AI talking avatar / 数字人口播` 已在项目脑、执行层与 formal_api_demo 入口口径里正式降级：
  - 不再作为默认主承载
  - 保留为可选 / 待验证支线

## formal_api_demo 当前执行口径

- `已确认`
  - `scripts/generate_formal_api_demo.py` 默认 case 已切到：
    - `cases/formal_api_demo_human_self_footage.md`
- `已确认`
  - `formal_api_demo_core.py` 当前已支持：
    - 读取 `展示主线 / 段载体 / 素材键 / 素材来源`
    - 从本地 config 的 `[footage_inputs.*]` 注入真人、自录录屏和结果卡素材
    - 把这些素材直接写进 `manifest.json` / `route_plan.json`
    - 在真实素材齐全时，以 `user_provided_local_assets` 进入正式 generation 结果
- `已确认`
  - `config/formal_api_demo.example.toml` 已补：
    - `hook_human`
    - `process_self_footage`
    - `result_card`
    - `close_human`
    这 4 个 `footage_inputs` 示例占位
- `已确认`
  - `cases/formal_api_demo.md` 现已显式标记为：
    - pure PPT / 信息卡次级支路样例
    - 不再是正式默认主线

## 当前验证结果

- `已确认`
  - `python3 -m unittest` 通过 5 条回归：
    - old pure PPT case 解析
    - old API visual generation lane
    - cloud-only assembly dry-run gate
    - new formal mainline case route 解析
    - new formal mainline user footage reuse
- `已确认`
  - `python3 scripts/generate_formal_api_demo.py --input cases/formal_api_demo_human_self_footage.md --dry-run`
    已能落出：
    - `route_profile = human_self_footage_light_ppt`
    - `video_route_strategy = hybrid`
    - carriers = `human / self_footage / light_ppt / human`

## 当前仍未验证项

- `待验证`
  - 当前仓库只验证到了：
    - route/schema/config/case/code 层已接通
    - dry-run 与单测通过
- `待验证`
  - 真实人物素材、自录素材和结果卡是否已经在当前机器完整注入，并完成一次正式云端导出：
    - 仍待本地继续验证

## 当前下一步

- 若下一轮要真正验证新主线成片，只需要：
  - 在正式 local config 里补齐 `[footage_inputs.*].local_path`
  - 用真实人物 / 录屏 / 结果卡素材跑一轮 generation + cloud assembly
- 若下一轮要继续保留 pure PPT，只能按：
  - 次级支路
  - 非默认路线
  理解，不得再写回默认主承载

## 当前工作分支与状态

- 当前工作分支：
  - `codex/provider-auto-rotation`
- 当前状态标签：
  - `task_branch_only`
- 当前必须继续明确：
  - 本轮结果尚未同步回 `codex/user-readable-map`
  - 仓库正式状态仍未更新到主读取分支
