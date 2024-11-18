# 定义镜像的标签
ARG TAG=3.13-slim-bullseye

FROM python:${TAG} as builder-image

# pip镜像源
ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"
#ENV PIPURL "https://pypi.org/simple/"

# 更换为阿里云的镜像源以加速 apt 下载
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list && \
    apt update

# 安装依赖
RUN apt update && apt install -y libpq-dev gcc unixodbc unixodbc-dev

# 赋值pdm.lock文件
COPY pdm.lock .

# 安装依赖包
RUN pip3 install --no-cache-dir pdm -i ${PIPURL} --default-timeout=1000 \
    && pdm export -o requirements.txt  --without-hashes \
    && pip3 install --no-cache-dir -r requirements.txt -i ${PIPURL} --default-timeout=1000 \
    && pip install psycopg2-binary \
    && rm -f requirements.txt \
    && rm -f pdm.lock


FROM python:${TAG}

# pip镜像源
ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"
#ENV PIPURL "https://pypi.org/simple/"

# 更换为阿里云的镜像源以加速 apt 下载
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak && \
    sed -i 's|http://deb.debian.org/debian|http://mirrors.aliyun.com/debian|g' /etc/apt/sources.list && \
    apt update

# 安装依赖
RUN apt update && apt install -y libpq-dev gcc unixodbc unixodbc-dev

# 如果python大版本有调整,请调整python的路径,示例: 3.13 -> 调整为对应版本
COPY --from=builder-image /usr/local/bin /usr/local/bin
COPY --from=builder-image /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages

RUN mkdir /app
COPY . /app

WORKDIR /app

EXPOSE 8000

RUN ["chmod", "+x", "/app/config/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/app/config/entrypoint.sh"]
# 构建命令
# docker build -t liaozhiming/django_hip:latest .
# 文件格式问题,请保持unix编码;set ff=unix
