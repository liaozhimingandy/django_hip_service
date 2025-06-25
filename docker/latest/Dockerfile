# 定义镜像的标签
ARG VERSION_PYTHON_TAG=3.13-slim

FROM "liaozhiming/django_hip_service:$VERSION_PYTHON_TAG-base"

LABEL MAINTAINER="andy<contact@liaozhimingandy>"

# 避免交互，设置环境变量
ENV LANG C.UTF-8 \
    LC_ALL C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

# 创建工作目录并复制代码
WORKDIR /app
COPY ../../. /app

# 配置权限并暴露端口
RUN chmod +x /app/config/entrypoint.sh

# 暴露端口
EXPOSE 8000

# 设置入口点
ENTRYPOINT ["/app/config/entrypoint.sh"]
