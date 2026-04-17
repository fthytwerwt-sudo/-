# 主持壳动态审计｜《豆包的正确打开方式》vNext

## 1. 审计范围

- `已确认` 本轮只审计并写入以下范围：
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_audit.md`
  - `dist/20260417_豆包的正确打开方式_vnext/host_motion_prototype/`
- `已确认` 本轮未改动共享 JSON、主脚本、主流程代码。

## 2. 已读证据

- `已确认` 已读：
  - `AGENTS.md`
  - `codex_source/00_codex_readme.md`
  - `codex_log/latest.md`
  - `GPT数据源/06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
  - `GPT数据源/07_AI知识类视频价值规则.md`
  - `GPT数据源/08_当前正式事实.md`
  - `dist/20260417_豆包的正确打开方式_vnext/route_plan.json`
  - `dist/20260417_豆包的正确打开方式_vnext/manifest.json`
  - `dist/20260417_豆包的正确打开方式_vnext/result_summary.json`
  - `scripts/生成样片_豆包的正确打开方式_vnext.py`
  - `formal_api_demo_core.py`
  - `codex_log/20260417_豆包样片失败复盘与回炉方案.md`
  - `codex_log/20260404_formal_api_demo_liveportrait_round5_success.md`
  - `codex_log/20260403_formal_api_demo_liveportrait_round3_fast_gate_still_blocked.md`

## 3. 当前主持壳路线判定

### 3.1 当前 vNext 落地路线

- `已确认` 当前开头 / 结尾主持壳在共享产物里都被写成：
  - `provider = static_voxel_panel_loop`
  - `current_implementation = PIL draw -> PNG -> ffmpeg -loop 1`
- `已确认` `scripts/生成样片_豆包的正确打开方式_vnext.py` 中：
  - `seg01_hook` / `seg07_close_shell` 走 `visual_kind = "image"`
  - `render_image_segment(...)` 明确使用 ffmpeg `-loop 1`
- `已确认` 这条路线的本质是：
  - 静态单图成段
  - 不是嘴型驱动
  - 不是分层角色动画
  - 不是主持感动作系统

### 3.2 什么算假动态

- `已确认` 以下都不能记成成功：
  - `PIL` 单图 + ffmpeg `-loop 1`
  - 整张图轻微 bounce
  - 整张图轻微平移
  - 只做相机推拉、角色本体不变
  - 像 `NPC idle` 一样只在原地轻微晃动

### 3.3 本轮过线标准回写

- `已确认` 过线至少要满足：
  - 不是静态图
  - 不是轻微浮动
  - 至少有一个明确进入动作
  - 至少两种动态层同时成立
  - 不能像 `NPC idle`
- `已确认` 当前共享路线不满足上述任何关键项。

## 4. 仓库内“真动态路线”审计

### 4.1 历史真动态链是否存在

- `部分成立` 仓库内存在历史真实动态链：
  - `liveportrait-detect -> liveportrait`
- `已确认` 证据包括：
  - `codex_log/20260404_formal_api_demo_liveportrait_round5_success.md` 记录过真实成功
  - `formal_api_demo_core.py` 中存在：
    - `_execute_aliyun_liveportrait_detect(...)`
    - `_execute_aliyun_liveportrait_video_generation(...)`
- `已确认` 当前本机正式配置里：
  - `portrait_detect.enabled = true`
  - `portrait_video_generation.enabled = true`

### 4.2 这条真动态链对本轮体素娃娃是否可用

- `已确认` 我已基于当前开头壳图和现成口播音频做最小实测：
  - 输入图：`素材/开头人物壳_hook_shell.png`
  - 输入音频：`tts/seg01_hook.wav`
  - 实测结果文件：`host_motion_prototype/liveportrait_probe_result.json`
- `已确认` 实测返回：
  - `status = blocked`
  - `blocked_reason = No human face detected.`
  - `failure_reason = portrait_detect_rejected`
- `已确认` 这说明：
  - `liveportrait` 这条链对“真人脸图”是技术成立的
  - 但对当前 `Minecraft-inspired` 体素娃娃壳，不可直接复用
  - 当前对象不是“参数没调好”，而是“检测前置对象就不适配”

## 5. 最终结论

- `已确认` 当前仓库存在“历史上跑通过”的真动态 provider 路线，但它是**真人开口链**，不是当前体素娃娃主持壳路线。
- `已确认` 对当前 vNext 体素主持壳，现成真动态链的最小实测结果是：
  - `blocked`
  - 原因：`liveportrait-detect` 无法识别当前体素壳为可用人脸
- `已确认` 因此本轮不能把以下任何路线写成成功：
  - 当前共享 `static_voxel_panel_loop`
  - 当前体素壳直接接 `liveportrait`
- `已确认` 本轮主持壳结论应维持：
  - `blocked`

## 6. blocked_reason

```md
当前仓库现有共享主持壳路线仍是 `PIL` 单图 + ffmpeg `-loop 1` 的静态成段，属于假动态；仓库内虽然存在历史真实跑通的 `liveportrait-detect -> liveportrait` 路线，但它是真人开口链，对当前体素娃娃壳最小实测直接返回 `No human face detected.`，因此本轮不存在可直接复用到《豆包的正确打开方式》vNext 的真实动态主持壳路线。
```

## 7. 最小替代路线

- `通用建议` 若下一轮继续推进，最小替代路线应改成“**分层主持娃娃资产**”而不是继续拿整张壳图硬跑。
- `通用建议` 最小可用形态：
  - 透明背景角色资产
  - 至少拆出：头部 / 嘴型层 / 手臂或手势层
  - 允许再加：眨眼层 / 身体微重心层
- `通用建议` 最低动作语法：
  - `进入动作`：0.4s-0.8s 内完成入场和落位
  - `动态层 1`：嘴型或口部开合，不允许全程一张脸
  - `动态层 2`：头部点头 / 手臂指向 / 眨眼 三者至少其一
  - `判断动作`：关键句时有一次明确动作重心变化
  - `收束动作`：结尾不能只是停住，需有收手或回正
- `通用建议` 明确禁止继续提交为“成功”的形式：
  - 全图轻微平移
  - 全图轻微 bounce
  - 只有镜头推拉
  - 没有进入动作的原地站桩循环

## 8. prototype 状态

- `已确认` 本轮**没有成功 prototype** 可交付。
- `已确认` 当前仅保留一份实测证据：
  - `host_motion_prototype/liveportrait_probe_result.json`
- `已确认` 不把失败 probe 冒充成 prototype 成功。

## 9. 建议同步到共享 JSON 的字段更新

- `通用建议` `route_plan.json`
  - `constraints.host_route.status` 继续维持 `blocked`
  - `constraints.host_route.blocked_reason` 改成引用本审计里的最终 `blocked_reason`
  - 可新增 `constraints.host_route.audit_path = ".../host_motion_audit.md"`
  - 可新增 `constraints.host_route.prototype_probe = ".../host_motion_prototype/liveportrait_probe_result.json"`
- `通用建议` `manifest.json`
  - `host_route.status` 继续维持 `blocked`
  - `host_route.blocked_reason` 同步本审计结论
  - 可新增 `host_route.audit_status = "audited_current_round"`
  - 可新增 `host_route.provider_probe_status = "portrait_detect_rejected_for_voxel_shell"`
- `通用建议` `result_summary.json`
  - `content_validation_v1.dynamic_host.status` 继续维持 `blocked`
  - `content_validation_v1.dynamic_host.reason` 同步本审计结论
  - `known_issues` 增加一条：
    - `liveportrait` 最小实测对当前体素壳返回 `No human face detected.`，说明历史真人开口链不能直接复用为本轮主持娃娃动态壳
