import datetime
import json
import os
import shutil
import uuid

from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from django.views.decorators.http import require_POST

from django_hip_service import settings
from .models import MessageFormat, DataElement


# Create your views here.
def home(request):
    """首页"""
    messages = MessageFormat.objects.all()
    return render(request, template_name='esb_standard/index.html',
                  context={'messages': messages, 'APP_VERSION_VERBOSE': settings.APP_VERSION_VERBOSE})


@require_POST
def download(request):
    """下载消息示例"""
    # 提取参数
    query_dict = QueryDict(request.body)
    messages_list = query_dict.getlist("messages")

    assert messages_list is not None, "缺失必要参数"

    # 数据库筛选消息
    messages = MessageFormat.objects.filter(id__in=messages_list)

    dir_name = f"messages-{str(uuid.uuid4()).replace('-', '')}"
    generate_messages_demo(dir_name=dir_name, messages=messages)

    # 使用 Django 响应 ZIP 文件
    with open("tmp-messages.zip", 'rb') as fp:
        response = HttpResponse(fp.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=messages.zip'
        return response


def generate_messages_demo(dir_name: str, messages):
    """生成消息示例"""
    for message in messages:
        # 生成demo样例,打压缩包
        # 递归创建目录
        dir_path = f"tmp/{dir_name}/{message.service.service_name}-{message.service.service_code}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=False)

        data = message.format
        data['id'] = str(uuid.uuid4()).replace('-', '')
        data['creationTime'] = f'{datetime.datetime.now().strftime("%Y%m%dT%H%M%S")}'

        # 递归处理消息节点
        if not message.is_custom:
            data['message'] = iterative_message(data['message'])

        # 请求
        with open(os.path.join(dir_path, f'{message.service.service_name}-请求消息.json'), encoding='utf8',
                  mode='w') as fp:
            fp.write(json.dumps(data, ensure_ascii=False, indent=4))

        # 正向响应
        del data['message']
        data['receiver'], data['sender'] = data['sender'], data['receiver']
        data["ack"] = {
            "ackCode": "AA",
            "targetMessageId": data['id'],
            "ackDetail": "消息处理成功"
        }
        data['id'] = str(uuid.uuid4()).replace('-', '')
        with open(os.path.join(dir_path, f'{message.service.service_name}-响应消息（成功）.json'), encoding='utf8',
                  mode='w') as fp:
            fp.write(json.dumps(data, ensure_ascii=False, indent=4))

        # 反向响应
        data['id'] = str(uuid.uuid4()).replace('-', '')
        data["ack"]["ackCode"] = "AE"
        data["ack"]["ackDetail"] = "消息处理失败，原因：XXX"

        with open(os.path.join(dir_path, f'{message.service.service_name}-响应消息（异常）.json'), encoding='utf8',
                  mode='w') as fp:
            fp.write(json.dumps(data, ensure_ascii=False, indent=4))

    # 压缩文件夹
    if os.path.exists("tmp-messages.zip"):
        os.remove("tmp-messages.zip")
    shutil.make_archive(base_name="tmp-messages", format='zip', root_dir="tmp")

    # 移除文件夹
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')


def iterative_message(items: (dict, list)):
    assert items is not None, "dict is must not None"

    if isinstance(items, (dict,)):
        for key, value in items.items():
            if isinstance(value, (dict, list)) and value:
                items[key] = iterative_message(value)
            else:
                qs = DataElement.objects.filter(data_set__value=key)
                objs = {key: []}
                for q in qs:
                    objs[key].append({
                        "DATA_ELEMENT_ID": q.de_code,
                        "DATA_ELEMENT_NAME": q.de_name,
                        "DATA_ELEMENT_EN_NAME": q.de_en_code,
                        "DATA_ELEMENT_VALUE": ""
                    })
                return objs
    else:
        for item in items:
            if isinstance(item, (dict, list)) and item:
                iterative_message(item)
