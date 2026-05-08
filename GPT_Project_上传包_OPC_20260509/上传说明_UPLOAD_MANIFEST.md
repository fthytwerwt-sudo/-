# 上传说明 UPLOAD MANIFEST

## 1. 文件定位

这是当前唯一推荐上传到 GPT Project 的《视频工厂》资料包说明。

当前唯一推荐上传目录绝对路径：

`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`

## 2. 当前包口径

当前包统一按以下口径构建：

- `OPC 一人公司 AI 闭环验证系统`
- `DeepSeek（只读供料层 / Explorer）`
- `Codex（唯一写入执行层 / Integrator）`
- `reference（参考）`、`locked reference（锁定参考）`、`visual route（视觉路由）` 锁质量机制，不锁死固定流程

## 3. 包内主文件清单

1. `00_项目总述.md`
2. `01_项目系统提示词.md`
3. `02_术语定义与状态边界.md`
4. `03_总索引与阅读顺序.md`
5. `04_选题与文案规则.md`
6. `05_文案路由规则.md`
7. `06_当前主线锚点_API生成真人_用户录制素材_少量PPT_云端剪辑.md`
8. `07_AI知识类视频价值规则.md`
9. `08_当前事实读取规则.md`
10. `09_目标态计划.md`
11. `10_OPC一人公司闭环与多AI协作机制.md`

## 4. 不要上传的目录或文件

不要上传旧目录：

`/Users/fan/Documents/视频工厂/GPT 数据源/`

原因：
- 这是旧 GPT Project 静态包。
- 它仍包含旧的 `10_样片参考质量规则_reference_quality_sample_rule.md`。
- 它的 `08_当前事实读取规则.md` 默认主读取分支仍是旧口径，不再适合作为本轮 canonical upload package。

不要上传无空格动态事实目录：

`/Users/fan/Documents/视频工厂/GPT数据源/`

原因：
- 这是 GitHub 动态事实 / 执行包目录。
- 它不是给 GPT Project 直接上传的规范资料包目录。
- 它缺少专门给 GPT Project 使用的 `08_当前事实读取规则.md` 上传版说明。

不要上传旧文件：

`10_样片参考质量规则_reference_quality_sample_rule.md`

原因：
- 本轮主上传包不再把它作为主读文件。
- 当前主上传包以 OPC 总纲 `10_OPC一人公司闭环与多AI协作机制.md` 为上位机制文件。

## 5. 上传动作规则

- 用户上传时只使用本文件顶部给出的唯一目录。
- ChatGPT 不得凭记忆口头给本地上传地址。
- 需要上传地址时，以 Codex 本地审计结果或 `codex_log/current_local_artifact_paths.md` 为准。

## 6. 一句话规则

上传 GPT Project 时，只上传：

`/Users/fan/Documents/视频工厂/GPT_Project_上传包_OPC_20260509/`
