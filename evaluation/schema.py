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
import time
import uuid

from django.contrib.staticfiles import finders
from lxml import etree as et

from django.urls import reverse

import graphene
from graphene.types.generic import GenericScalar
from evaluation.utils import CDATool, cda_map, query_to_dict

# 定义XML命名空间
namespace = {'xmlns': 'urn:hl7-org:v3'}


# 返回的内容
class ResponseMessageOutput(graphene.ObjectType):
    code = graphene.Int(required=True)
    message = graphene.String(required=True)
    data = graphene.String()


def update_demo_param(service, dir_name: str, *args):
    """
    更新示例参数
    :return:
    """
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
    assert len(args) > 0, "No arguments"
    id_msg = str(uuid.uuid4())
    gmt_created = time.strftime('%Y%m%d%H%M%S')

    id_sender, id_receiver = 'esbid_1', 'esbid_2'

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
            path, node = item.get('path').strip().split('/@')
            root.find(path, namespaces=namespace).set(node, item.get("value") if file_name_t == file_name else '000000')

        # 创建文件夹
        dir_path = f"temp/service/{dir_name}"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        result_file = f"{dir_path}/{file_name}"

        # 保存到文件
        doc.write(result_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')


class Query(graphene.ObjectType):
    download_cdas_by_adm_no = graphene.Field(ResponseMessageOutput, adm_no=graphene.String(required=True))
    download_examples_services = graphene.Field(ResponseMessageOutput,
                                                input_data=GenericScalar(required=True))  # 接收一个json字符串

    def resolve_download_cdas_by_adm_no(self, info, adm_no):
        """通过就诊流水号导出CDA"""

        sql = ("select [no], PatientName patient_name, DocTypeCode doc_type_code, DocContent content "
               "from(SELECT row_number() over(partition by DocTypeCode order by CreateTime asc) no, [PatientName], DocTypeCode, [DocContent] "
               "from [CDADocument] where Visit_id = ? ) as T where T.[no] < 21")

        cda = CDATool(ip=os.getenv("ip", '172.16.33.179'), user=os.getenv('user', 'caradigm'),
                      password=os.getenv('password', 'Knt2020@lh'), dbname=os.getenv('dbname', 'CDADB'))

        cursor = cda.get_cursor()
        cursor.execute(sql, (adm_no,))

        code = 400

        # 临时文件路径
        dir_path = uuid.uuid4()
        file_dir = f'temp/cda/{dir_path}'

        for row in query_to_dict(cursor):

            if not os.path.exists(file_dir):
                os.makedirs(os.path.join(file_dir, row['patient_name']))
            tmp_file_name = f'EMR-SD-{row["doc_type_code"][-2:]}-{cda_map.get(row["doc_type_code"], "未知")}-{row["patient_name"]}-T01-{str(row["no"]).rjust(3, "0")}.xml'
            with open(file=f'{file_dir}/{row["patient_name"]}/{tmp_file_name}', encoding='utf-8', mode='w',
                      newline='') as f:
                f.writelines(row["content"])

            # 生成一个 URL，假设有一个名为 'some_view' 的视图
            relative_url = reverse('download_zip',
                                   kwargs={'temp_dir_path': dir_path, "content_type": "cda"})
            # 构建完整的绝对 URL
            absolute_url = info.context.build_absolute_uri(relative_url)
            code = 200

        return ResponseMessageOutput(code=code, message=absolute_url if code < 400 else "暂无数据")

    def resolve_download_examples_services(self, info, input_data):
        """下载互联互通测试服务入参"""
        # 临时文件路径
        dir_name = str(uuid.uuid4())

        # 处理数据（这里可以根据需要处理 input_data）
        for item in input_data['data']:
            update_demo_param(item.get('service_code'), dir_name, *item.get(item.get('service_code')))

        # 生成一个 URL，假设有一个名为 'some_view' 的视图
        relative_url = reverse('download_zip',
                               kwargs={'temp_dir_path': dir_name, "content_type": "service"})
        # 构建完整的绝对 URL
        absolute_url = info.context.build_absolute_uri(relative_url)

        # 返回处理后的数据
        return ResponseMessageOutput(code=200, message=absolute_url)
