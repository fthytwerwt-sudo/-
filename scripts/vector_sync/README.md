# Vector Sync Dry Run（向量同步空跑）

本目录只放《视频工厂》RAG Router 设计线的本地 dry-run 工具。当前脚本不会调用阿里 / DashScope / DashVector / DeepSeek API，不会生成 embedding，不会创建 collection，也不会写入向量数据库。

## 运行方式

```bash
python3 scripts/vector_sync/向量同步空跑_vector_sync_dry_run.py --base-ref origin/main --head-ref HEAD
```

可选本地对照：

```bash
python3 scripts/vector_sync/向量同步空跑_vector_sync_dry_run.py --base-ref HEAD~1 --head-ref HEAD
```

## 输出文件

- `codex_log/vector_rag_router_design/vector_sync_dry_run/20260611_vector_sync_dry_run_plan.json`
- `codex_log/vector_rag_router_design/vector_sync_dry_run/20260611_vector_sync_dry_run_summary.md`

## 安全边界

- `can_apply=false` 固定为 false。
- `.env`、`.env.local`、`secret`、`token`、`credential`、`authorization.local` 路径只标记 blocked，不读取内容。
- 原始媒体扩展名只标记 skipped，不读取内容。
- feature 分支只映射到 `video_factory_branch_staging`，`allowed_for_real_tasks=false`。
- 输出只包含 chunk metadata，不输出完整 chunk 文本。
