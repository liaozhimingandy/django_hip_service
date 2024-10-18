#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： schema.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-10-18 14:16
    @Desc: 
================================================="""
import graphene

from cdr.schema import Query as CDRQuery, Mutation as CDRMutation
from evaluation.schema import Query as EvaluationQuery


class Query(EvaluationQuery,  CDRQuery, graphene.ObjectType):
    pass


class Mutation(CDRMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
if __name__ == "__main__":
    pass
