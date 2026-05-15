# DeepSeek 运行时授权说明

## 1. 文件定位

本目录只存放本机 runtime 配置说明和示例文件。

`DeepSeek runtime provider（DeepSeek 运行时供应商）` 的目标是：让《视频工厂》每轮需要 DeepSeek 供料时，都能由项目 runtime 自动加载授权，再只注入 DeepSeek 子进程环境。

## 2. 可用 key 来源

加载顺序固定为：

1. `process_env`
2. `.env.local`
3. `.env`
4. `本地运行配置_local_runtime/deepseek_runtime_authorization.local.json`

允许字段名只有：

```text
DEEPSEEK_API_KEY
```

可选配置字段：

```text
DEEPSEEK_BASE_URL
DEEPSEEK_MODEL
DEEPSEEK_ESCALATION_MODEL
```

## 3. 安全边界

- key 可以放在项目根目录 `.env.local` 或 `.env`。
- key 也可以放在本地未跟踪授权文件：`deepseek_runtime_authorization.local.json`。
- 这些文件必须被 `.gitignore` 忽略。
- 配好一次后，每轮 Codex 任务由 runtime provider 自动读取。
- key 只注入 DeepSeek 子进程环境。
- key 不得进入 prompt。
- key 不得打印到 stdout / stderr。
- key 不得写入日志、供料包、manifest、fixture 或 Git。

## 4. 一次性配置流程

如果 runtime doctor 输出：

```text
runtime_setup_required
```

只需要在上述任一允许位置补一次 `DEEPSEEK_API_KEY`，然后重新运行 runtime doctor。

不得把实际 key 写入本说明文件或 example 文件。
