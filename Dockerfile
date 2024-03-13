# 定义镜像的标签
ARG TAG=3.11.2-slim-buster

FROM python:${TAG} as builder-image

# change apt-get mirror
RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb http://mirrors.aliyun.com/debian-security/ buster/updates main non-free contrib" >> /etc/apt/sources.list \
    && echo "deb-src http://mirrors.aliyun.com/debian-security/ buster/updates main non-free contrib" >> /etc/apt/sources.list

RUN apt-get update && apt-get -y install libpq-dev gcc

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


FROM python:${TAG}

# 如果python大版本有调整,请调整python的路径,示例: 3.11 -> 调整为对应版本
COPY --from=builder-image /usr/local/bin /usr/local/bin
COPY --from=builder-image /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

RUN mkdir /opt/app
WORKDIR /opt/app
COPY . /opt/app

RUN ["chmod", "+x", "/opt/app/config/entrypoint.sh"]

# run entrypoint.sh
ENTRYPOINT ["/opt/app/config/entrypoint.sh"]

# 构建命令
# docker build -t liaozhiming/django_hip:latest .
# 文件格式问题,请保持unix编码;set ff=unix
