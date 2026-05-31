#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Installing guided proof video Node dependencies..."
npm install --save-exact react react-dom remotion @remotion/media @remotion/captions @remotion/renderer

echo "Installing guided proof video Python dependencies..."
python3 -m pip install -r requirements-video-toolchain.txt

echo "Rendering Remotion validation still..."
npm run vf:remotion:still

echo "Rendering Remotion validation 5s clip..."
npm run vf:remotion:render5s

echo "Running toolchain self-check..."
npm run vf:toolchain:check
