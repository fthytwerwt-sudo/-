# 20260406_cloud_assembly_permission_blocker_status_sync

## 本轮目标

- 把第一次真实 cloud-only assembly 验证的脱敏结果写回仓库状态文件
- 保留真实失败层、当前主体、最小权限缺口和未重跑原因
- 只更新状态 / 日志类文件，不改 Python 逻辑

## 执行前确认

- 当前目录：`/Users/fan/Documents/视频工厂`
- 当前分支：`codex/round1`
- 当前 HEAD 起点：`75178a35bd4e0d87e3d423f0a9aaaaa7f826f24b`
- 当前主线路由仍是 pure PPT / 信息卡 cloud-only
- 本轮不重跑 generation
- 本轮不修改 `formal_api_demo_core.py`
- 本轮不修改 `formal_api_demo_cloud_assembly.py`

## 本轮真实运行事实

- 已真实执行：
  - `python3 scripts/assemble_formal_api_demo.py --manifest dist/formal_api_demo/manifest.json --local-config config/formal_api_demo.local.toml`
- 真实结果：失败
- 精确失败层：`ListEditingProjects`
- 失败位置归类：云剪工程解析层
- 真实证据：
  - Host：`ice.cn-beijing.aliyuncs.com`
  - Code：`Forbidden`
  - Message：`User not authorized to operate on the specified resource.`
  - RequestId（真实 assembly 运行）：`EDDE072A-BC84-5CDA-A29D-EE883E324AB6`
  - RequestId（最小权限复现）：`5C1B3503-D169-5DF3-8710-EE334C6B93AB`

## 已确认不是这些层

- 不是 OSS 上传层
- 不是 manifest / timeline 输入资产层
- 不是 `UpdateEditingProject`
- 不是 `SubmitMediaProducingJob`
- 不是 `GetMediaProducingJob`
- 不是导出结果解析层

证据：

- `uploaded_assets_count = 6`
- `dist/formal_api_demo/assembly/cloud_timeline.json` 已生成
- `project_id = null`
- `job_id = null`
- `media_id = null`
- `request_ids = {}`

## 当前主体与权限审计

- 当前主体：RAM 用户 `video-factory-oss-1`
- 身份确认方式：真实 STS `GetCallerIdentity`
- 脱敏身份摘要：
  - AccountId：`1301171458131253`
  - PrincipalType：`RAMUser`
  - ARN 摘要：`acs:ram::1301171458131253:user/video-fac...`

## 当前主因

- 当前 RAM 用户缺少最小 ICE / 云剪权限
- 至少还过不了：
  - `ice:ListEditingProjects`

## 建议最小权限

- `ice:ListEditingProjects`
- `ice:UpdateEditingProject`
- `ice:SubmitMediaProducingJob`
- `ice:GetMediaProducingJob`

建议挂载对象：

- `video-factory-oss-1`

最小策略 JSON：

```json
{
  "Version": "1",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ice:ListEditingProjects",
        "ice:UpdateEditingProject",
        "ice:SubmitMediaProducingJob",
        "ice:GetMediaProducingJob"
      ],
      "Resource": "*"
    }
  ]
}
```

## 当前为什么没有重跑

- 本轮已确认主体身份
- 本轮也已确认当前主体连 RAM 只读查询都没有权限
- 因此本轮不能假装“已补权”
- 当前未重跑原因：无法直接补权

## RAM 权限审计证据

- `ram:GetUser`：`403 NoPermission`
  - RequestId：`5148A91E-4292-541B-8BC9-55A3ECC79503`
- `ram:ListUsers`：`403 NoPermission`
  - RequestId：`FD5D619D-913D-570F-BEBB-A54C9D0E7699`
- `ram:ListPoliciesForUser`：`403 NoPermission`
  - RequestId：`A2443A4B-11BC-58A3-9A75-6EA49CDAC886`
  - RequestId：`CAF6407A-141A-5FC9-B68D-832E0D83F3A7`

## 本轮状态结论

- 本轮不是 `no_repo_change`
- 本轮状态应视为：
  - `repo_status_updated`
- 按分支同步规则，本轮若 commit + push 完成，但未同步回 `codex/user-readable-map`，分类应为：
  - `task_branch_only`
