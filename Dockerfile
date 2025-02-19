# 定义镜像的标签
ARG TAG=3.13-slim

# 阶段 1: 构建镜像
FROM python:${TAG} AS builder

# 设置环境变量
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# 设置环境变量以避免交互式安装提示
ENV DEBIAN_FRONTEND=noninteractive

# pip镜像源
#ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"
ENV PIPURL "https://pypi.org/simple/"

# 更换为阿里云的镜像源以加速 apt 下载
#RUN test -e /etc/apt/sources.list || echo "deb http://mirrors.aliyun.com/debian bookworm main" > /etc/apt/sources.list && \
#    echo "deb http://mirrors.aliyun.com/debian-security bookworm-security main" >> /etc/apt/sources.list && \
#    echo "deb http://mirrors.aliyun.com/debian bookworm-updates main" >> /etc/apt/sources.list

# 安装依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev curl \
    && rm -rf /var/lib/apt/lists/* \

# 添加 Microsoft 包存储库密钥
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# 添加 Microsoft 包存储库
RUN curl https://packages.microsoft.com/mssql-server/debian/prod.list > /etc/apt/sources.list.d/mssql-server.list

# 安装 ODBC 驱动
RUN apt-get update && apt-get install -y \
    msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# 复制 pdm.lock 文件
COPY pyproject.toml .

# 安装 pdm 及项目依赖
RUN pip install --no-cache-dir pdm -i ${PIPURL} --default-timeout=1000 \
    && pdm lock \
    && pdm export -o requirements.txt --without-hashes \
    && pip install --no-cache-dir -r requirements.txt -i ${PIPURL} --default-timeout=1000 \
    && rm -f requirements.txt pdm.lock

# 阶段 2: 运行时镜像
FROM python:${TAG}

# 设置环境变量
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# 设置环境变量以避免交互式安装提示
ENV DEBIAN_FRONTEND=noninteractive

# 更换为阿里云的镜像源以加速 apt 下载
#RUN test -e /etc/apt/sources.list || echo "deb http://mirrors.aliyun.com/debian bookworm main" > /etc/apt/sources.list && \
#    echo "deb http://mirrors.aliyun.com/debian-security bookworm-security main" >> /etc/apt/sources.list && \
#    echo "deb http://mirrors.aliyun.com/debian bookworm-updates main" >> /etc/apt/sources.list

# 安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev curl \
    && rm -rf /var/lib/apt/lists/* \

# 添加 Microsoft 包存储库密钥
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# 添加 Microsoft 包存储库
RUN curl https://packages.microsoft.com/mssql-server/debian/prod.list > /etc/apt/sources.list.d/mssql-server.list

# 安装 ODBC 驱动
RUN apt-get update && apt-get install -y \
    msodbcsql17 \
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
# docker build -t django_hip_service:latest .
# 文件格式问题,请保持unix编码;set ff=unix
