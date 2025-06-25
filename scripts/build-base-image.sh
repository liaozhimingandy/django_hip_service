#!/bin/bash

RELEASE_DIR='./docker';
REPO_NAME='liaozhiming/django_hip_service'

for app_ver in $RELEASE_DIR/*; do

    if [ -f "$app_ver/Dockerfile.base" ]; then

        tag=$(echo $app_ver | cut -b 10-);
        echo "Build: $tag";

        #  导入环境变量
        set -a
            . "$app_ver/.env"
        set +a

        echo $app_ver
        echo "VERSION_PYTHON_TAG: $VERSION_PYTHON_TAG"

        docker build --build-arg VERSION_PYTHON_TAG=$VERSION_PYTHON_TAG -f "$app_ver/Dockerfile.base" -t "$REPO_NAME:$VERSION_PYTHON_TAG-base" "$app_ver"
    fi

done
