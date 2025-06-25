#!/bin/bash

RELEASE_DIR='./docker';
REPO_NAME='liaozhiming/django_hip_service'

for app_ver in $RELEASE_DIR/*; do

    if [ -f "$app_ver/Dockerfile.base" ]; then

        tag=$(echo $app_ver | cut -b 10-);
        echo "Build: $tag";
        set -a
            . "$app_ver/.env"
        set +a

        echo $app_ver
        echo "VERSION_PYTHON_TAG: $VERSION_PYTHON_TAG"

        # 获取最新的标签（假设标签都是按字母顺序排序的，并且最新的标签排在最前面）
        latest_tag=$(git describe --tags --abbrev=0)
        # 去掉标签中的 "v" 前缀（如果存在）
        latest_tag_without_v=$(echo "$latest_tag" | sed 's/^v//')
        echo "最新标签值: $latest_tag_without_v"

        docker build --build-arg VERSION_PYTHON_TAG=$VERSION_PYTHON_TAG -f "$app_ver/Dockerfile" -t "$REPO_NAME:$latest_tag_without_v" "$app_ver"
    fi

done