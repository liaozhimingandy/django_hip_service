#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： api.py.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-05-17 17:00
    @Desc: 消息校验服务
================================================="""
import uuid
from datetime import datetime
from typing import Optional
from zoneinfo import ZoneInfo

from ninja import Router, Schema
from ninja.responses import codes_2xx, codes_4xx

router = Router(tags=["openim"])


# 消息统一格式
class SendMsgSchema(Schema):
    client_msg_id: str
    server_msg_id: Optional[str] = None
    gmt_create: str
    gmt_send: str
    send_id: str
    recv_id: str
    group_id: Optional[str] = None
    content_type: str


class SendMsgSchemaOut(Schema):
    code: int = 0
    message: str = "ok"
    msg_id: str
    gmt_created: str


def verification(data):
    """
    消息校验
    :param data: 待校验的消息元素,元素格式请参考标准接口文档
    :return:
    """
    content_type = data["content_type"]
    """校验"""
    data = {}
    code, message = 0, "ok"

    match content_type:
        case 'CheckResultAdd':
            message = "ok"
        case _:
            code = 8403
            message = "本消息暂未纳入校验范围!"

    data["code"] = code
    data["message"] = message

    return data


@router.post("/send_msg/", response={codes_2xx: SendMsgSchemaOut, codes_4xx: SendMsgSchemaOut})
def send_msg(request, payload: SendMsgSchema, msg_id: str = str(uuid.uuid4())):
    """补充服务的校验"""

    data = payload.dict(exclude_unset=False)
    result = verification(data=data)
    message = {"code": result["code"], "message": result["message"], "msg_id": msg_id, "gmt_created": datetime.
    now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')}
    response_code = 200 if result['code'] == 0 else (message["code"]-8000)

    return response_code, message


if __name__ == "__main__":
    pass
