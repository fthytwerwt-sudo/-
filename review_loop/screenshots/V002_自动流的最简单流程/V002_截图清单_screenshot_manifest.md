# V002 截图清单 screenshot manifest

## 基础信息

- video_id（视频编号）：V002
- video_slug（视频标识）：V002_自动流的最简单流程
- video_title（视频标题）：自动流的最简单流程
- record_dir（记录目录）：`review_loop/records/V002_自动流的最简单流程_douyin_policy_notice/`
- screenshot_root（截图证据目录）：`review_loop/screenshots/V002_自动流的最简单流程/`

## 截图文件状态

| screenshot_type（截图类型） | screenshot_path（截图路径） | source_status（来源状态） | notes（说明） |
| --- | --- | --- | --- |
| douyin_policy_notice（抖音审核通知截图） | missing_user_not_provided | missing_user_not_provided | 用户本轮提供了截图可识别字段文字，但未提供截图原图文件；Codex 不编造路径。 |
| visible_ai_label（AI 标识可见截图） | missing_user_not_provided | missing_user_not_provided | 用户文字说明第二张截图可见“作者声明：内容由 AI 生成”；原图未提供。 |

## 当前目录结构

```text
审核通知_policy_notice/
人工补充数据_manual_metrics/
```

## 写入规则

- 后续若用户提供截图原图，应归档到 `审核通知_policy_notice/`。
- 用户人工补充的播放 / 点赞 / 收藏数据不伪装成截图原图。
- 未提供截图原图时，只记录 `screenshot_file_status = missing_user_not_provided（截图原图未提供给 Codex）`。
- 不得把 V002 截图或数据混入 V001。

