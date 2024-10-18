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


# 新增
class CreateTerminology(graphene.Mutation):
    """
    示例:
    mutation create {
      createTerminology(
        itemName: "女性",
        datasetCode: "SEX",
        datasetName: "123",
        status: false,
        version: "1.0",
        versionNo: 1,
        itemStatus: true,
        itemCode: "7",
        authorId: "123",
        fromSrc: "123",
        author: "test",
      ) {
        terminology {
          tid
        }
      }
    }
    """
    class Arguments:
        dataset_code = graphene.String()
        dataset_name = graphene.String()
        status = graphene.Boolean()
        version_no = graphene.Int(default_value=1)
        version = graphene.String(default_value='1.0')
        item_code = graphene.String()
        item_name = graphene.String()
        item_status = graphene.Boolean()
        author_id = graphene.String()
        author = graphene.String()
        from_src = graphene.String()

    terminology = graphene.Field(TerminologyType)

    def mutate(self, info, **kwargs):
        # 使用输入数据创建新实例
        terminology_data = {key: value for key, value in kwargs.items() if value is not None}
        instance = Terminology.objects.create(**terminology_data)
        return CreateTerminology(terminology=instance)


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
