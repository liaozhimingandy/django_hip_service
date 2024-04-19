#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： signals.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-03-26 17:35
================================================="""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from hipmessageservice.models import Application


@receiver(post_save, sender=Application)
def application_post_save_handler(sender, instance, created, **kwargs):
    # 当新增一个系统时,自动插入到认证表
    # instance 是被保存的模型实例
    # created 是一个布尔值，如果模型是新创建的则为True，否则为False
    if created:
        # todo:在oauth_app表插入数数据
        print(f"A new {sender.__name__} object has been created: {instance}")
    else:
        print(f"An existing {sender.__name__} object has been updated: {instance}")


@receiver(post_delete, sender=Application)
def application_post_delete_handler(sender, instance, args, **kwargs):
    # 当删除一个系统时,自动删除该表对应的数据
    # instance 是被删除的模型实例
    #     todo: 待实现
    print(f"A new {sender.__name__} object has been deleted: {instance}")


if __name__ == "__main__":
    pass
