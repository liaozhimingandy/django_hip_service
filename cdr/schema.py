#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： schema.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-09-14 14:39
    @Desc: 
================================================="""
import graphene
from django.db import models
from graphene import InputObjectType, UUID as GrapheneUUID
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field

from cdr.models import Terminology


class TerminologyType(DjangoObjectType):
    class Meta:
        model = Terminology


# 查询类
class Query(graphene.ObjectType):
    terminologys = graphene.List(TerminologyType)
    count = graphene.Int()

    def resolve_terminologys(self, info):
        return Terminology.objects.all()

    def resolve_count(self, info):
        """总数"""
        return Terminology.objects.count()


def create_input_type(model, exclude: tuple = ("tid", 'gmt_created')):
    # 动态生成输入类型的字段
    attrs = {}
    for field in model._meta.fields:
        # 跳过自动生成的 ID 字段，或者根据需要可以包含
        if isinstance(field, models.AutoField) or field.name in exclude:
            continue

        if isinstance(field, models.UUIDField):
            field_type = GrapheneUUID
        else:
            field_type = convert_django_field(field)

        attrs[field.name] = field_type

    # 动态创建 GraphQL InputObjectType
    input_type = type(f'{model.__name__}Input', (InputObjectType,), attrs)
    return input_type


TerminologyInput = create_input_type(Terminology)


# 新增
class CreateTerminology(graphene.Mutation):
    class Arguments:
        input = TerminologyInput(required=True)

    terminology = graphene.Field(TerminologyType)

    def mutate(self, info, input):
        # 创建新的 Book 实例
        # 使用输入数据创建新实例
        terminology_data = {key: value for key, value in input.items() if value is not None}
        terminology = Terminology.objects.create(**terminology_data)
        return CreateTerminology(terminology=terminology)


# 修改
class UpdateTerminology(graphene.Mutation):
    class Arguments:
        tid = graphene.ID(required=True)
        input = TerminologyInput()

    terminology = graphene.Field(TerminologyType)

    def mutate(self, info, tid, input):
        terminology = Terminology.objects.get(tid=tid)

        # 动态更新模型字段
        for key, value in input.items():
            setattr(terminology, key, value)

        terminology.save()
        return UpdateTerminology(terminology=terminology)


# 删除
class DeleteTerminology(graphene.Mutation):
    class Arguments:
        tid = graphene.UUID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, tid):
        try:
            terminology = Terminology.objects.get(tid=tid)
            terminology.delete()
            return DeleteTerminology(success=True)
        except Terminology.DoesNotExist:
            return DeleteTerminology(success=False)


# 定义 Mutation 类
class Mutation(graphene.ObjectType):
    create_terminology = CreateTerminology.Field()
    update_terminology = UpdateTerminology.Field()
    delete_terminology = DeleteTerminology.Field()


# 定义 schema
schema = graphene.Schema(query=Query, mutation=Mutation)

if __name__ == "__main__":
    pass
