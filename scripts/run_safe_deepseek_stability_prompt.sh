#!/usr/bin/env bash
set -euo pipefail
set +x

cleanup() {
  unset DEEPSEEK_API_KEY
}
trap cleanup EXIT

cd "/Users/fan/Documents/视频工厂"

printf "请输入 DeepSeek API Key（输入不会显示，不会写入 .env，不会进入日志）：\n"
read -rsp "DEEPSEEK_API_KEY: " DEEPSEEK_API_KEY
printf "\n"

if [ -z "${DEEPSEEK_API_KEY:-}" ]; then
  echo "未输入 DEEPSEEK_API_KEY，已取消。"
  exit 2
fi

export DEEPSEEK_API_KEY
export DEEPSEEK_DISABLE_ENV_FILE=1
export DEEPSEEK_ALLOW_PROCESS_ENV_KEY=1

set +e
python3 scripts/deepseek_supply_controller.py \
  --allow-process-env-api-key \
  --request-file codex_log/supply_requests/20260510_deepseek_stability_check_request.json
status=$?
set -e

unset DEEPSEEK_API_KEY
trap - EXIT

echo
echo "DeepSeek 稳定化测试已结束。"
echo "请回到 Codex 查看最新日志。"

exit "$status"
