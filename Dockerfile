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
# ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"
ENV PIPURL "https://pypi.org/simple/"

# 安装依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev freetds-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# 复制 pdm.lock 文件
COPY pyproject.toml uv.lock ./

# 安装 uv CLI：方式一，通过 pip
RUN pip install --no-cache-dir uv -i ${PIPURL} --default-timeout=1000

# （可选）创建虚拟环境并激活：若使用虚拟环境安装依赖
RUN uv venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 配置 pip 镜像源（对于 uv sync 内部调用 pip 也会使用此配置）
RUN pip config set global.index-url ${PIPURL}

# 导出 requirements.txt，然后通过 pip 安装，或直接 uv sync 安装
# 方式 A：uv 同步安装
RUN uv export --no-hashes --format requirements-txt > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt -i ${PIPURL} --default-timeout=1000 \
     && rm requirements.txt


# 阶段 2: 运行时镜像
FROM python:${TAG}

# 设置环境变量
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
# 设置环境变量以避免交互式安装提示
ENV DEBIAN_FRONTEND=noninteractive

# 安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev freetds-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# 复制 builder 阶段的虚拟环境（可选）或 site-packages
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

# 创建工作目录并复制代码
WORKDIR /app
COPY . /app

# 配置权限并暴露端口
RUN chmod +x /app/config/entrypoint.sh
EXPOSE 8000

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 设置入口点
ENTRYPOINT ["/app/config/entrypoint.sh"]
