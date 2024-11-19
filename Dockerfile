# 定义镜像的标签
ARG TAG=3.13-slim-bullseye

# 阶段 1: 构建镜像
FROM python:${TAG} AS builder

# pip镜像源
ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"

# 更换为阿里云的镜像源以加速 apt 下载
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list

# 更换为阿里云的 APT 源并安装依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# 复制 pdm.lock 文件
COPY pdm.lock .

# 安装 pdm 及项目依赖
RUN pip install --no-cache-dir pdm -i ${PIPURL} --default-timeout=1000 \
    && pdm export -o requirements.txt --without-hashes \
    && pip install --no-cache-dir -r requirements.txt -i ${PIPURL} --default-timeout=1000 \
    && pip install psycopg2-binary \
    && rm -f requirements.txt pdm.lock

# 阶段 2: 运行时镜像
FROM python:${TAG}

# pip镜像源
ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"

# 更换为阿里云的镜像源以加速 apt 下载
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list

# 更换为阿里云的 APT 源并安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev unixodbc \
    && rm -rf /var/lib/apt/lists/*

# 复制构建产物
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 创建工作目录并复制代码
WORKDIR /app
COPY . /app

# 配置权限并暴露端口
RUN chmod +x /app/config/entrypoint.sh
EXPOSE 8000

# 设置入口点
ENTRYPOINT ["/app/config/entrypoint.sh"]

# 构建命令
# docker build -t liaozhiming/django_hip:latest .
# 文件格式问题,请保持unix编码;set ff=unix