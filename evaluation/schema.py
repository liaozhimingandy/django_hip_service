#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： schema.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-10-08 15:22
    @Desc: 互联互通定量数据导出工具
================================================="""
import os
import threading
import time
import uuid

import graphene
import pandas as pd
from django.contrib.staticfiles import finders
from lxml import etree as et

from evaluation.utils import create_examples_zip, generate_cda

# 定义XML命名空间
namespace = {'xmlns': 'urn:hl7-org:v3'}

# 服务文件映射关系
list_file_path = {
        "PatientInfoQuery": "EMR-PL-04-个人信息查询服务",
        "OrganizationInfoQuery": "EMR-PL-07-医疗卫生机构（科室）信息查询服务",
        "ProviderInfoQuery": "EMR-PL-10-医疗卫生人员信息查询服务",
        "TerminologyQuery": "EMR-PL-13-术语查询服务",
        "DocumentAccess": "EMR-PL-15-电子病历文档检索服务",
        "DocumentRetrieve": "EMR-PL-16-电子病历文档调阅服务",
        "EncounterCardInfoQuery": "EMR-PL-19-就诊卡信息查询服务",
        "SourceAndScheduleInfoQuery": "EMR-PL-52-号源排班信息查询服务",
        "OutPatientInfoQuery": "EMR-PL-22-门诊挂号信息查询服务",
        "InPatientInfoQuery": "EMR-PL-25-住院就诊信息查询服务",
        "TransferInfoQuery": "EMR-PL-28-住院转科信息查询服务",
        "DischargeInfoQuery": "EMR-PL-31-出院登记信息查询服务",
        "OrderInfoQuery": "EMR-PL-34-医嘱信息查询服务",
        "ExamAppInfoQuery": "EMR-PL-37-检验申请信息查询服务",
        "CheckAppInfoQuery": "EMR-PL-40-检查申请信息查询服务",
        "PathologyAppInfoQuery": "EMR-PL-43-病理申请信息查询服务",
        "BloodTransAppInfoQuery": "EMR-PL-46-输血申请信息查询服务",
        "OperationAppInfoQuery": "EMR-PL-49-手术申请信息查询服务",
        "OutPatientAppointStatusInfoQuery": "EMR-PL-55-门诊预约状态信息查询服务",
        "CheckAppointStatusInfoQuery": "EMR-PL-58-检查预约状态信息查询服务",
        "OrderFillerStatusInfoQuery": "EMR-PL-60-医嘱执行状态信息查询服务",
        "CheckStatusInfoQuery": "EMR-PL-62-检查状态信息查询服务",
        "ExamStatusInfoQuery": "EMR-PL-64-检验状态信息查询服务",
        "OperationScheduleInfoQuery": "EMR-PL-79-手术排班信息查询服务",
        "OperationStatusInfoQuery": "EMR-PL-81-手术状态信息查询服务"
    }


# 返回的内容
class ResponseMessageOutput(graphene.ObjectType):
    code = graphene.Int(required=True)
    message = graphene.String(required=True)
    data = graphene.String()

class Content(graphene.InputObjectType):
    comment = graphene.String(required=True , description="备注说明")
    eg = graphene.String(required=False , description="示例")
    path = graphene.String(required=True , description="参数取值路径")
    value = graphene.String(required=True , description="取值")
    sql = graphene.String(required=False , description="底层sql查询语句")


class Service(graphene.InputObjectType):
    service_code = graphene.String(required=True , description="服务代码")
    service_name = graphene.String(required=True , description="服务名称")
    rank = graphene.String(required=True , description="互联互通评测等级")
    params = graphene.List(of_type=Content, description="参数列表")


class DataInputType(graphene.InputObjectType):
    """
    入参数据模型
    """
    data = graphene.List(of_type=Service, required=True, description="数据")


def update_demo_param(service, dir_name: str, args: list) -> None:
    """
    更新示例参数

    Args:
        service: 服务代码
        dir_name: 生成的目录
        args: 参数列表,需要更新的xml节点列表

    Returns:
        返回None

    """
    assert len(args) > 0, "No arguments"
    id_msg = str(uuid.uuid4())
    gmt_created = time.strftime('%Y%m%d%H%M%S')

    id_sender, id_receiver = os.getenv('SEND_ID', 'esbid_send'), os.getenv('RECV_ID', 'esbid_receive')

    file_name_t, file_name_f = f"{list_file_path[service]}-T01.xml", f"{list_file_path[service]}-F01.xml"

    for file_name in [file_name_t, file_name_f]:
        doc = et.parse(os.path.join(finders.find("evaluation/services"), file_name))
        root = doc.getroot()

        # 公共基本信息修改
        root.find('xmlns:id', namespace).set('extension', id_msg)
        root.find('xmlns:creationTime', namespace).set('value', gmt_created)
        root.find('xmlns:sender/xmlns:device/xmlns:id/xmlns:item', namespace).set('extension', id_sender)
        root.find('xmlns:receiver/xmlns:device/xmlns:id/xmlns:item', namespace).set('extension', id_receiver)

        for item in args:
            path, node = item.path.strip().split('/@')
            # 如何是正向测试用例则正常赋值,反向测试用例则默认赋值000000
            root.find(path, namespaces=namespace).set(node, item.value
            if file_name_t == file_name else os.getenv("DEFAULT_TEST_VALUE", '000000'))

        # 创建文件夹
        dir_path = f"temp/services/{dir_name}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        result_file = f"{dir_path}/{file_name}"

        # 保存到文件
        doc.write(result_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')


class Query(graphene.ObjectType):
    read_cdas_by_adm_no = graphene.Field(type_=graphene.String, adm_no=graphene.String(required=True),
                                         description='通过就诊流水号获取cda文档')
    examples_services = graphene.Field(type_=graphene.String, data=DataInputType(required=True),
                                       description="生成交互服务测试用例")
    # 或者使用下面这种方式
    # examples_services = graphene.Field(type_=graphene.String,
    #                                             input_data=GenericScalar(required=True),
    #                                    description="生成交互服务测试用例")  # 接收一个json字符串

    def resolve_read_cdas_by_adm_no(self, info, adm_no: str) -> str | None:
        """
        根据就诊流水号导出该条件下符合条件的所有CDA并且生成xml,最后打包成zip文件供下载使用

        Args:
            adm_no: 就诊流水号
            info: 用于添加后台任务;Info

        Returns:
            供下载使用的链接

        """

        dir_path = str(uuid.uuid4())

        # 启动后台线程,从数据库导出CDA
        task_thread = threading.Thread(target=generate_cda, args=(dir_path, adm_no))
        task_thread.daemon = True # 设置为守护线程，Django 退出时会自动终止该线程
        task_thread.start()


        # 生成一个 URL，假设有一个名为 'some_view' 的视图
        # relative_url = reverse('download_zip', kwargs={'temp_dir_path': dir_path, "content_type": "cda"})
        relative_url = f'static/archive-cdas-{dir_path}.zip'
        # 构建完整的绝对 URL
        absolute_url = info.context.build_absolute_uri(relative_url)



        return absolute_url

    def resolve_examples_services(self, info, data):
        """
        生成交互服务测试用例

        Args:
            data: 自定义类型DataInputType
            info: 用于添加后台任务

        Returns:
            返回空字符或None

        """
        # 临时文件路径
        dir_name = str(uuid.uuid4())
        list_params = [('类别名称', '参数名称', '参数值')]

        # 处理数据（这里可以根据需要处理 input_data）
        for item in data['data']:
            update_demo_param(item.service_code, dir_name, item.params)
            list_params.append((f'{list_file_path[item.service_code]}-T01', ','.join(el.comment for el in item.params),
                                ','.join((el.value for el in item.params))))
            list_params.append((f'{list_file_path[item.service_code]}-F01', ','.join(el.comment for el in item.params),
                                os.getenv("DEFAULT_TEST_VALUE", '000000')))

        # 生成一份csv文件交互服务测试参数文件
        file_path = f"temp/services/{dir_name}/services_params.xlsx"

        df = pd.DataFrame(list_params[1:], columns=list_params[0])

        # 保存到 Excel
        df.to_excel(file_path, sheet_name="services", index=False)

        # 启动后台线程,执行对文件打包
        task_thread = threading.Thread(target=create_examples_zip, args=(dir_name, True))
        task_thread.daemon = True  # 设置为守护线程，Django 退出时会自动终止该线程
        task_thread.start()

        relative_url = f'static/archive-services-{dir_name}.zip'

        # 构建完整的绝对 URL
        absolute_url = info.context.build_absolute_uri(relative_url)

        # 返回处理后的数据
        return absolute_url
