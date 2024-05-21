#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： api.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-05-17 17:00
    @Desc: 
================================================="""
from ninja import NinjaAPI

from hipmessageservice.api import router as api_router

api = NinjaAPI(version='1.0.0',
               title='Open API',
               description="内部接口文档",
               auth=None,
               openapi_extra={
                   "info": {
                       "terms Of Service": "https://openapi.esb.alsoapp.com/",
                   }},
               docs_url="/docs/",
               servers=[
                   {"url": "https://openapi-test.esb.alsoapp.com", "description": "测试环境"},
                   {"url": "https://openapi.esb.alsoapp.com", "description": "生产环境"},
               ])

api.add_router("/openim/", api_router)


if __name__ == "__main__":
    pass
