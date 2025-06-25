#!/bin/bash

RELEASE_DIR='./docker';
REPO_NAME='liaozhiming/django_hip_service'

for app_ver in $RELEASE_DIR/*; do

    #  导入环境变量
    set -a
        . "$app_ver/.env"
    set +a

     # 获取最新的标签（假设标签都是按字母顺序排序的，并且最新的标签排在最前面）
    latest_tag=$(git describe --tags --abbrev=0)
    # 去掉标签中的 "v" 前缀（如果存在）
    latest_tag_without_v=$(echo "$latest_tag" | sed 's/^v//')
    echo "最新标签值: $latest_tag_without_v"

    if [ -f "$app_ver/Dockerfile.base" ]; then
        # 推送python环境基础
        docker push $REPO_NAME:$VERSION_PYTHON_TAG-base
    fi

    if [ -f "$app_ver/Dockerfile" ]; then
        # 推送使用生成环境的镜像
        docker push $REPO_NAME:$latest_tag_without_v
    fi

done
