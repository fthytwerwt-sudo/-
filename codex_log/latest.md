# Latest

## 当前主结论

- `已确认` 本轮只完成《视频工厂》全仓清理审计，没有实际删除任何文件。
- `已确认` 当前仓库仍是多项目仓库；本轮按《视频工厂》入口读取，不涉及直播项目业务改动。
- `已确认` 当前正式高风险不可误删主链为：
  - `GPT数据源/*`
  - `codex_source/*`
  - `codex_log/*`
  - `project_source/*`
  - `cases/formal_api_demo_doubao_task_clear_20260412.md`
  - `dist/formal_api_demo_doubao_task_clear_20260412/*`
  - `codex_log/current_publish_target.md`
  - `codex_log/current_publish_target_light_evidence.md`
- `已确认` 第二步最值得先清的一批已经锁定为：
  - `dist/_generation_probe_20260409/`
  - `dist/_portrait_probe_20260409/`
  - `dist/_probe_generation_20260408014710/`
  - `dist/_probe_generation_current_config/`
  - `dist/_probe_generation_home_config/`
  - `dist/.tmp_review_user_footage/`
  - `dist/.seg02_v2_frames/`
  - `dist/seg02_v2_frames/`
  - `dist/seg02_v2_frames_jpg/`
  - `dist/final_after_frames/`
  - `dist/final_seg02_v3_frames/`
  - 全仓非 `.git/` 下 `.DS_Store`
- `已确认` 上述第一批目录与文件不在当前正式入口、当前正式日志、当前待发对象证据链里，合计约 `16.8M`，风险最低。
- `待验证` `codex_log/current_publish_target*.md` 仍引用不存在的 `素材录制/豆包素材.mp4`；当前本地实际存在的是 `素材录制/录制于 2026-04-14 03.50.02.mp4`，因此 `素材录制/*` 暂时不能进删除批次。
- `部分成立` `GPT 数据源/` 与 `GPT数据源/` 当前内容一致，但语义上分别承担本地源事实目录与 GitHub 可读镜像角色；本轮不进入删除候选。

## 本轮产出

1. `codex_log/20260415_全仓清理审计.md`

## 下一步建议

1. 若执行第二步删除，只先删审计报告里那一批 `refs=0` 的 `probe / tmp / frames / .DS_Store`。
2. 不要在未核清 `素材录制/豆包素材.mp4` 路径漂移前处理 `素材录制/*`。
3. 不要把 `GPT 数据源/`、`GPT数据源/`、`project_source/`、`codex_source/`、`codex_log/` 当成普通重复文件区。

## 当前默认接手建议先读

1. `AGENTS.md`
2. `codex_source/00_codex_readme.md`
3. `codex_log/latest.md`
4. 若命中《视频工厂》清理 / 复盘 / 审计，再读 `codex_log/20260415_全仓清理审计.md`
5. 若命中当前样片 / 发布线复核，再读 `codex_log/current_publish_target.md`
6. 若需要轻量证据，再读 `codex_log/current_publish_target_light_evidence.md`
