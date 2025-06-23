# 定义镜像的标签
ARG TAG=3.13-slim

# ---------- 阶段 1: 构建阶段 ----------
# 阶段 1: 构建镜像
FROM python:${TAG} AS builder

# 避免交互，设置环境变量
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
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
RUN uv export --no-hashes --format requirements-txt > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt -i ${PIPURL} --default-timeout=1000 \
     && rm requirements.txt


# ---------- 阶段 2: 运行时阶段 ----------
# 阶段 2: 运行时镜像
FROM python:${TAG}

# 避免交互，设置环境变量
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# 安装运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev gcc unixodbc unixodbc-dev freetds-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# 创建并切换到非 root 用户
# 这里示例 UID 1000，你也可根据 CI/CD 规范或编排需求调整
ARG APP_USER=appuser
ARG APP_UID=1000
RUN useradd -u ${APP_UID} -m ${APP_USER}

# 复制 builder 阶段的虚拟环境（可选）或 site-packages
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# 创建工作目录并复制代码
WORKDIR /app
COPY . /app

# 配置权限并暴露端口
RUN chmod +x /app/config/entrypoint.sh

# 修改 /app 目录及可能写入目录的权限归属到非 root 用户
RUN chown -R ${APP_USER}:${APP_USER} /app

# 切换到非 root 用户
USER ${APP_USER}

# 暴露端口
EXPOSE 8000

# 设置入口点
ENTRYPOINT ["/app/config/entrypoint.sh"]
