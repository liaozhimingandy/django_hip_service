#!/bin/bash

RELEASE_DIR='./docker';
REPO_NAME='liaozhiming/django_hip_service'

# 简易日志函数
log() { echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"; }

for app_ver in $RELEASE_DIR/*; do

    # 如果存在 .env，则仅导入有用变量
    if [[ -f "$app_ver/.env" ]]; then
      log "导入环境变量"
      # 过滤注释，逐行 export
      export $(grep -v '^\s*#' "$app_ver/.env" | xargs)
    fi

    # 进入版本目录，以便正确找到所属 Git 仓库
    pushd "$app_ver" > /dev/null

    # 获取最新标签（示例匹配 v 开头标签）
    latest_tag=$(git describe --tags --abbrev=0 --match 'v*' || echo "")
    if [[ -z "$latest_tag" ]]; then
      log "未找到任何标签，跳过"
      popd > /dev/null
      continue
    fi

    # 去掉 v 前缀
    latest_tag="${latest_tag#v}"
    log "最新标签：$latest_tag"

    popd > /dev/null

    if [ -f "$app_ver/Dockerfile.base" ]; then
        [[ -d "$app_ver" ]] || continue

        # 推送python环境基础到阿里云私人镜像仓库
        full_src="${REPO_NAME}:${VERSION_PYTHON_TAG}-base"
        full_dst="${REGISTRY_ALI}/${REPO_NAME}:${VERSION_PYTHON_TAG}-base"

        log "Tag & push 基础镜像 $full_src → $full_dst"

        docker tag "$full_src" "$full_dst" \
          && docker push "$full_dst" \
          || { log "推送失败：$full_dst"; exit 1; }
    fi

    if [ -f "$app_ver/Dockerfile" ]; then
        # 推送使用生成环境的镜像到阿里云私人镜像仓库
        full_src="${REPO_NAME}:${latest_tag}"
        full_dst="${REGISTRY_ALI}/${REPO_NAME}:${latest_tag}"
        log "Tag & push 正式镜像 $full_src → $full_dst"

        docker tag "$full_src" "$full_dst" \
          && docker push "$full_dst" \
          || { log "推送失败：$full_dst"; exit 1; }
    fi

done
