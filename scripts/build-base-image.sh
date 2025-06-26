#!/bin/bash

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# 假设项目根是脚本所在目录的上一级
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# RELEASE_DIR 相对于项目根
RELEASE_DIR="$PROJECT_ROOT/docker"

REPO_NAME='liaozhiming/django_hip_service'

# 简易日志函数
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

for app_ver in $RELEASE_DIR/*; do

    if [ -f "$app_ver/Dockerfile.base" ]; then

        tag=$(echo $app_ver | cut -b 10-);
        log "Build: $tag";

        # 如果存在 .env，则仅导入有用变量
        if [[ -f "$app_ver/.env" ]]; then
          log "导入环境变量"
          # 过滤注释，逐行 export
          export $(grep -v '^\s*#' "$app_ver/.env" | xargs)
        fi

        log "目前路径:$app_ver"
        log "VERSION_PYTHON_TAG: $VERSION_PYTHON_TAG"

        # Dockerfile 路径
        DOCKERFILE_PATH="$app_ver/Dockerfile.base"
        # 上下文设为项目根
        CONTEXT_DIR="$PROJECT_ROOT"

        log "Building with Dockerfile: $DOCKERFILE_PATH"
        log "Build context: $CONTEXT_DIR"

        docker build --build-arg VERSION_PYTHON_TAG=$VERSION_PYTHON_TAG -f "$app_ver/Dockerfile.base" \
        -t "$REPO_NAME:$VERSION_PYTHON_TAG-base" "$CONTEXT_DIR"
    fi

done
