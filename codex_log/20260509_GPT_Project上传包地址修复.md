# 20260509｜GPT Project 上传包地址修复

## 1. 本轮定位

- `已确认` 本轮只修复 GPT Project 上传包地址不一致问题。
- `已确认` 本轮不做视频、不改代码、不改发布状态、不接 DeepSeek API、不执行多 agent runtime。

## 2. 地址不对号诊断

- `已确认` 旧地址 `/Users/fan/Documents/视频工厂/GPT 数据源/` 存在，但它是历史静态包，不是本轮 canonical upload package path。
- `已确认` 旧静态包仍包含 `10_样片参考质量规则_reference_quality_sample_rule.md`，且 `08_当前事实读取规则.md` 默认主读取分支仍是旧口径。
- `已确认` 无空格目录 `/Users/fan/Documents/视频工厂/GPT数据源/` 存在，但它是 GitHub 动态事实 / 执行包目录，不是 GPT Project 规范上传目录。
- `已确认` 本轮新生成的规范上传包路径是：
  `/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`
- `已确认` 以后 ChatGPT 不得凭记忆给本地上传地址；必须由 Codex 本地审计或 `current_local_artifact_paths.md` 给出。

## 3. 当前规范上传包

- `已确认` 当前上传包包含 11 个主文件：
  - `00_项目总述.md`
  - `01_项目系统提示词.md`
  - `02_术语定义与状态边界.md`
  - `03_总索引与阅读顺序.md`
  - `04_选题与文案规则.md`
  - `05_文案路由规则.md`
  - `06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
  - `07_AI知识类视频价值规则.md`
  - `08_当前事实读取规则.md`
  - `09_目标态计划.md`
  - `10_OPC一人公司闭环与多AI协作机制.md`
- `已确认` 当前上传包还包含：`上传说明_UPLOAD_MANIFEST.md`
- `已确认` 当前上传包主层级不包含旧 `10_样片参考质量规则_reference_quality_sample_rule.md`

## 4. 路径机制

- `已确认` 已把 canonical upload package path 写入 `codex_log/current_local_artifact_paths.md`
- `已确认` 已在 `AGENTS.md` 和 `codex_source/00_codex_readme.md` 写明：上传地址必须由 Codex 本地审计或路径索引给出。

## 5. 保护项

- `已确认` 本轮未修改视频产物。
- `已确认` 本轮未修改音频 / TTS / voice trial 产物。
- `已确认` 本轮未修改图片 / 卡片 / 素材产物。
- `已确认` 本轮未修改 `dist/latest_review_pack/`。
- `已确认` 本轮未修改 `content_validation`、`send_ready`、`publish_status`、`voice_validation`、`final_voice_validated`、`technical_validation`、`current_video_baseline`、`latest_review_pack` 状态值。

## 6. 下一个目标

用户上传 canonical upload package path 中的文件到 GPT Project；上传后 ChatGPT 再检查 GPT Project 包是否生效。
