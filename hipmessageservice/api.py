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
import base64
import copy
import json
import re
import uuid
import datetime
from enum import Enum
from typing import Optional
from zoneinfo import ZoneInfo
import lxml
import requests

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django.db import connection
from django.utils import timezone

from json2xml import json2xml
from lxml import etree
from ninja import Router, Schema, Field
from ninja.responses import codes_2xx, codes_4xx
from requests.exceptions import ConnectTimeout

from cdr.models import ExamReport, ExamResultMain, ExamResultDetail, ExamResultDetailAST, CheckReport, Visit, Diagnosis, \
    PathologyReport, CriticalValue, CallPatient, PatientInfoCollector
from hipmessageservice.utils.encrypt import EncryptUtils


router = Router(tags=["openim"])

data_mapping = {
    "patient_id": "//xmlns:patient/xmlns:id/xmlns:item/@extension",
    "gmt_reg": "//xmlns:patient/xmlns:effectiveTime/xmlns:any/@value",
    "id_no": "//xmlns:patientPerson/xmlns:id/xmlns:item/@extension",
    "id_code": "//xmlns:patientPerson/xmlns:idCategory/@code",
    "id_name": "//xmlns:patientPerson/xmlns:idCategory/xmlns:displayName/@value",
    "patient_name": "//xmlns:patientPerson/xmlns:name/xmlns:item/xmlns:part/@value",
    "tel_no": "//xmlns:patientPerson/xmlns:telecom/xmlns:item/@value",
    "sex_code": "//xmlns:administrativeGenderCode/@code",
    "sex_name": "//xmlns:administrativeGenderCode/xmlns:displayName/@value",
    "gmt_birth": "//xmlns:birthTime/@value",
    "addr_sal": "//xmlns:addr/xmlns:item/xmlns:part[@type='SAL']/@value",
    "addr_sta": "//xmlns:addr/xmlns:item/xmlns:part[@type='STA']/@value",
    "addr_cty": "//xmlns:addr/xmlns:item/xmlns:part[@type='CTY']/@value",
    "addr_cnt": "//xmlns:addr/xmlns:item/xmlns:part[@type='CNT']/@value",
    "addr_stb": "//xmlns:addr/xmlns:item/xmlns:part[@type='STB']/@value",
    "addr_str": "//xmlns:addr/xmlns:item/xmlns:part[@type='STR']/@value",
    "addr_bnr": "//xmlns:addr/xmlns:item/xmlns:part[@type='BNR']/@value",
    "addr_zip": "//xmlns:addr/xmlns:item/xmlns:part[@type='ZIP']/@value",
    "marital_status_code": "//xmlns:maritalStatusCode/@code",
    "marital_status_name": "//xmlns:maritalStatusCode/xmlns:displayName/@value",
    "occupation_code": "//xmlns:occupationCode/@code",
    "occupation_name": "//xmlns:occupationCode/xmlns:displayName/@value",
    "ethnic_group_code": "//xmlns:ethnicGroupCode/xmlns:item/@code",
    "ethnic_group_name": "//xmlns:ethnicGroupCode/xmlns:item/xmlns:displayName/@value",
    "work_org": "//xmlns:employerOrganization/xmlns:name/xmlns:item/xmlns:part/@value",
    "work_org_tel": "//xmlns:employerOrganization/xmlns:contactParty/xmlns:telecom/xmlns:item/@value",
    "hcard_no": "//xmlns:asOtherIDs/xmlns:id/xmlns:item[@root='2.16.156.10011.1.19']/@extension",
    "hcard_org_code": "//xmlns:asOtherIDs/xmlns:id/xmlns:item["
                      "@root='2.16.156.10011.1.19']/parent::*/following-sibling::*/xmlns:id/xmlns:item/@extension",
    "gcard_no": "//xmlns:asOtherIDs/xmlns:id/xmlns:item[@root='2.16.156.10011.1.2']/@extension",
    "gcard_org_code": "//xmlns:asOtherIDs/xmlns:id/xmlns:item["
                      "@root='2.16.156.10011.1.2']/parent::*/following-sibling::*/xmlns:id/xmlns:item/@extension",
    "contact_code": "//xmlns:personalRelationship/xmlns:code/@code",
    "contact_name": "//xmlns:personalRelationship/xmlns:code/xmlns:displayName/@value",
    "contact_cname": "//xmlns:relationshipHolder1/xmlns:name/xmlns:item/xmlns:part/@value",
    "contact_tel": "//xmlns:personalRelationship/xmlns:telecom/xmlns:item/@value",
    "org_code": "//xmlns:providerOrganization/xmlns:id/xmlns:item/@extension",
    "org_name": "//xmlns:providerOrganization/xmlns:name/xmlns:item/xmlns:part/@value",
    "ins_code": "//xmlns:beneficiary/xmlns:code/@code",
    "ins_name": "//xmlns:beneficiary/xmlns:code/xmlns:displayName/@value",
    "author_id": "//xmlns:author/xmlns:assignedEntity/xmlns:id/xmlns:item/@extension",
    "author": "//xmlns:author/xmlns:assignedEntity/xmlns:assignedPerson/xmlns:name/xmlns:item/xmlns:part/@value",
    "from_src": "//xmlns:sender/xmlns:device/xmlns:id/xmlns:item/@extension"
}

dict_empi_mapping = {
    "SYS_REC_ID": "patient_id",
    "LAST_UPDATE_TIME": "gmt_reg",
    "ID_NO": "id_no",
    "ID_TYPE_CODE": "id_code",
    "ID_TYPE_NAME": "id_name",
    "NAME": "patient_name",
    "PHONE_NO": "tel_no",
    "GENDER_CODE": "sex_code",
    "GENDER_NAME": "sex_name",
    "DOB": "gmt_birth",
    "PRESENT_ADDRESS_PROVINCE": "addr_sta",
    "PRESENT_ADDRESS_CITY": "addr_cty",
    "PRESENT_ADDRESS_COUNTY": "addr_cnt",
    "PRESENT_ADDRES_COUNTRY": "addr_stb",
    "PRESENT_ADDRES_VILLAGE": "addr_str",
    "PRESENT_ADDRES_HOUSE_NO": "addr_bnr",
    "PRESENT_ADDRES_POSTAL_CODE": "addr_zip",
    "MARITAL_STATUS_CODE": "marital_status_code",
    "MARITAL_STATUS_NAME": "marital_status_name",
    "ETHNIC_GROUP_CODE": "ethnic_group_code",
    "ETHNIC_GROUP_NAME": "ethnic_group_name",
    "OCCUPATION_CODE": "occupation_code",
    "OCCUPATION_NAME": "occupation_name",
    "EMPLOYER_NAME": "work_org",
    "EMPLOYER_PHONE_NO": "work_org_tel",
    "HEALTH_CARD_NO": "hcard_no",
    "HEALTH_RECORD_NO": "gcard_no",
    "CONTACT_RELATIONSHIP_CODE": "contact_code",
    "CONTACT_RELATIONSHIP_NAME": "contact_name",
    "CONTACT_PHONE_NO": "contact_tel",
    "CONTACT_NAME": "contact_cname",
    "ORG_CODE": "org_code",
    "MEDICAL_INSURANCE_TYPE_CODE": "ins_code",
    "MEDICAL_INSURANCE_TYPE_NAME": "ins_name",
    "LAST_UPDATE_BY": "author_id",
    "SYS_CODE": "from_src",
    "MEDICAL_INSURANCE_CARD_NO": "",
    "CITIZENSHIP_CODE": "",
    "CITIZENSHIP_NAME": "",
    "EDUCATION_LEVEL_CODE": "",
    "EDUCATION_LEVEL_NAME": "",
    "POB_PROVINCE": "",
    "POB_CITY": "",
    "POB_COUNTY": "",
    "NATIVE_PLACE_PROVINCE": "",
    "NATIVE_PLACE_CITY": "",
    "EMPLOYER_PROVINCE": "",
    "EMPLOYER_CITY": "",
    "EMPLOYER_COUNTY": "",
    "EMPLOYER_POSTAL_CODE": "",
    "CONTACT_ADDRESS": "addr_sal",
    "ABO_BLOOD_TYPE_CODE": "",
    "ABO_BLOOD_TYPE_NAME": "",
    "RH_BLOOD_TYPE_CODE": "",
    "RH_BLOOD_TYPE_NAME": "",
    "CREATE_BY": "author",
    "CREATE_TIME": "gmt_reg",
    "MEDICAL_RECORD_NO": "",
    "OP_MEDICAL_RECORD_NO": "",
    "Passport_GA": "",
    "BEIJING_MEDICAL_CARD_NO": "",
    "VIP_INDICATOR": "",
    "DEATH_INDICATOR": "",
    "DOD": "",
    "HOSPITAL_CARD_NO": "patient_id",
    "CATEGORY_CODE": ""
}


# 定义枚举类型
class ContentTypeEnum(str, Enum):
    PatientInfoRegister = "PatientInfoRegister"
    PatientInfoUpdate = "PatientInfoUpdate"
    PatientInfoMerge = "PatientInfoMerge"
    PatientInfoQuery = "PatientInfoQuery"
    OrganizationInfoRegister = "OrganizationInfoRegister"
    OrganizationInfoUpdate = "OrganizationInfoUpdate"
    OrganizationInfoQuery = "OrganizationInfoQuery"
    ProviderInfoRegister = "ProviderInfoRegister"
    ProviderInfoUpdate = "ProviderInfoUpdate"
    ProviderInfoQuery = "ProviderInfoQuery"
    TerminologyRegister = "TerminologyRegister"
    TerminologyUpdate = "TerminologyUpdate"
    TerminologyQuery = "TerminologyQuery"
    DocumentRegister = "DocumentRegister"
    DocumentAccess = "DocumentAccess"
    DocumentRetrieve = "DocumentRetrieve"
    EncounterCardInfoAdd = "EncounterCardInfoAdd"
    EncounterCardInfoUpdate = "EncounterCardInfoUpdate"
    EncounterCardInfoQuery = "EncounterCardInfoQuery"
    OutPatientInfoAdd = "OutPatientInfoAdd"
    OutPatientInfoUpdate = "OutPatientInfoUpdate"
    OutPatientInfoQuery = "OutPatientInfoQuery"
    InPatientInfoAdd = "InPatientInfoAdd"
    InPatientInfoUpdate = "InPatientInfoUpdate"
    InPatientInfoQuery = "InPatientInfoQuery"
    TransferInfoAdd = "TransferInfoAdd"
    TransferInfoUpdate = "TransferInfoUpdate"
    TransferInfoQuery = "TransferInfoQuery"
    DischargeInfoAdd = "DischargeInfoAdd"
    DischargeInfoUpdate = "DischargeInfoUpdate"
    DischargeInfoQuery = "DischargeInfoQuery"
    OrderInfoAdd = "OrderInfoAdd"
    OrderInfoUpdate = "OrderInfoUpdate"
    OrderInfoQuery = "OrderInfoQuery"
    ExamAppInfoAdd = "ExamAppInfoAdd"
    ExamAppInfoUpdate = "ExamAppInfoUpdate"
    ExamAppInfoQuery = "ExamAppInfoQuery"
    CheckAppInfoAdd = "CheckAppInfoAdd"
    CheckAppInfoUpdate = "CheckAppInfoUpdate"
    CheckAppInfoQuery = "CheckAppInfoQuery"
    PathologyAppInfoAdd = "PathologyAppInfoAdd"
    PathologyAppInfoUpdate = "PathologyAppInfoUpdate"
    PathologyAppInfoQuery = "PathologyAppInfoQuery"
    BloodTransAppInfoAdd = "BloodTransAppInfoAdd"
    BloodTransAppInfoUpdate = "BloodTransAppInfoUpdate"
    BloodTransAppInfoQuery = "BloodTransAppInfoQuery"
    OperationAppInfoAdd = "OperationAppInfoAdd"
    OperationAppInfoUpdate = "OperationAppInfoUpdate"
    OperationAppInfoQuery = "OperationAppInfoQuery"
    SourceAndScheduleInfoAdd = "SourceAndScheduleInfoAdd"
    SourceAndScheduleInfoUpdate = "SourceAndScheduleInfoUpdate"
    SourceAndScheduleInfoQuery = "SourceAndScheduleInfoQuery"
    OutPatientAppointStatusInfoAdd = "OutPatientAppointStatusInfoAdd"
    OutPatientAppointStatusInfoUpdate = "OutPatientAppointStatusInfoUpdate"
    OutPatientAppointStatusInfoQuery = "OutPatientAppointStatusInfoQuery"
    CheckAppointStatusInfoAdd = "CheckAppointStatusInfoAdd"
    CheckAppointStatusInfoUpdate = "CheckAppointStatusInfoUpdate"
    CheckAppointStatusInfoQuery = "CheckAppointStatusInfoQuery"
    OrderFillerStatusInfoUpdate = "OrderFillerStatusInfoUpdate"
    OrderFillerStatusInfoQuery = "OrderFillerStatusInfoQuery"
    CheckStatusInfoUpdate = "CheckStatusInfoUpdate"
    CheckStatusInfoQuery = "CheckStatusInfoQuery"
    ExamStatusInfoUpdate = "ExamStatusInfoUpdate"
    ExamStatusInfoQuery = "ExamStatusInfoQuery"
    OperationScheduleInfoAdd = "OperationScheduleInfoAdd"
    OperationScheduleInfoUpdate = "OperationScheduleInfoUpdate"
    OperationScheduleInfoQuery = "OperationScheduleInfoQuery"
    OperationStatusInfoUpdate = "OperationStatusInfoUpdate"
    OperationStatusInfoQuery = "OperationStatusInfoQuery"
    ExamReportAdd = "ExamReportAdd"
    ExamReportDelete = "ExamReportDelete"
    DrugExamResultDelete = "DrugExamResultDelete"
    CheckReportAdd = "CheckReportAdd"
    CheckReportDelete = "CheckReportDelete"
    PathologyReportAdd = "PathologyReportAdd"
    PathologyReportDelete = "PathologyReportDelete"
    VitalSignsAdd = "VitalSignsAdd"
    VitalSignsDelete = "VitalSignsDelete"
    DiagIssuedAdd = "DiagIssuedAdd"
    DiagIssuedUpdate = "DiagIssuedUpdate"
    DiagIssuedDelete = "DiagIssuedDelete"
    CriticalValueAdd = "CriticalValueAdd"
    CriticalValueDelete = "CriticalValueDelete"
    CriticalValueDeal = "CriticalValueDeal"
    getExamReports = "getExamReports"
    getCheckReports = "getCheckReports"
    VisitInfoUpdate = "VisitInfoUpdate"
    getExamReportPrintInfos = "getExamReportPrintInfos"
    callPatient = 'CallPatient'
    PatientInfoCollector = "PatientInfoCollector"

# 消息统一格式
class SendMsgSchema(Schema):
    client_msg_id: str
    server_msg_id: Optional[str] = None
    gmt_create: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[\+\-]\d{2}:\d{2})",
                            description="消息创建时间")
    gmt_send: str = Field(..., pattern=r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(Z|[\+\-]\d{2}:\d{2})",
                          description="消息发送时间")
    send_id: str
    recv_id: str
    group_id: Optional[str] = None
    content_type: ContentTypeEnum = Field(..., description="消息类型")


class SendMsgSchemaOut(Schema):
    code: int = 0
    message: str = "ok"
    msg_id: str
    gmt_created: str
    data: Optional[str | list] = None
    detail: Optional[str | list] = None


def deal_patient_empi_reg(content):
    """ 处理个人新增注册,更新接口,调取empi注册接口,并且保存到数据库 """
    from lxml import etree
    etree.register_namespace('xmlns', 'urn:hl7-org:v3')
    # 添加带<?xml的情况
    try:
        xml_root = etree.fromstring(content)
    except ValueError:
        xml_root = etree.fromstring(content.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
    except (lxml.etree.XMLSyntaxError,) as e:
        return False, str(e)

    dict_data = data_mapping.copy()

    # 解析平台患者个人信息数据集所需要的数据
    for key in data_mapping.keys():
        data = xml_root.xpath(data_mapping[key], namespaces={'xmlns': 'urn:hl7-org:v3'})
        dict_data[key] = data[0]

    # 日期处理
    dict_data['gmt_reg'] = timezone.make_aware(datetime.datetime.strptime(dict_data['gmt_reg'], '%Y%m%d%H%M%S'),
                                               timezone.get_current_timezone())
    dict_data['gmt_birth'] = timezone.make_aware(datetime.datetime.strptime(dict_data['gmt_birth'], '%Y%m%d'),
                                                 timezone.get_current_timezone())
    dict_data_empi = {}

    # 调empi接口
    for key in dict_empi_mapping.keys():
        if dict_empi_mapping[key]:
            dict_data_empi[key] = dict_data[dict_empi_mapping[key]]

    xml_data = json2xml.Json2xml(dict_data_empi, pretty=True, wrapper="EMPI_PERSON").to_xml()

    # 定义正则表达式模式（注意：这里不需要为大小写差异进行特殊处理）
    pattern = r'<\?xml\s+version=["\']1\.0["\']\s*(?:encoding=["\']UTF-8["\'])?\?>'

    # 标志re.I表示忽略大小写
    patient_data = re.sub(pattern, '', xml_data, flags=re.I)

    payload = f"""
           <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:car="http://www.caradigm.com/">
           <soap:Header/>
           <soap:Body>
              <car:IndexRegisterFunc>
                 <!--Optional:-->
                 <car:xml>
                 <![CDATA[{patient_data}]]>
                 </car:xml>
              </car:IndexRegisterFunc>
           </soap:Body>
        </soap:Envelope>
        """
    # 调empi接口进行患者注册
    try:
        response = requests.post(settings.EMPI_API_URL, data=payload, headers={'Content-Type': 'text/xml;charset=UTF-8'}, timeout=2)
    except ConnectTimeout as e:
        # print(str(e))
        return False, "Connection timed out, please try again later or contact our administrator"
    if response.status_code == 200:
        # 匹配empi号
        # empi = (re.search('empi_id&gt;\d+&lt;/empi_id', response.text).group().replace('empi_id&gt;', '')
        #         .replace('&lt;/empi_id', ''))
        root = etree.fromstring(response.content)
        xml_empi = root.find('.//xmlns:IndexRegisterFuncResult', namespaces={"xmlns": "http://www.caradigm.com/"}).text
        empi_root = etree.fromstring(xml_empi)

        if empi_root.find('.//state').text == 'success':
            empi = empi_root.find('.//empi_id').text
            dict_data.update(**{"empi": empi})
            # 保存到数据库
            # 移除不需要的key
            # list_to_remove = ['id_name', 'sex_name', 'marital_status_name', 'occupation_name', 'ethnic_group_name',
            #                   'contact_name', 'ins_name']
            #
            # for key in list_to_remove:
            #     dict_data.pop(key, None)

            # 保存到数据库, 耗时比较长
            # Patient.objects.update_or_create(patient_id=dict_data['patient_id'], defaults=dict_data)

            return True, f"#empi_id:{empi}#"
        else:
            return False, empi_root.find('.//message').text

    else:
        return False, response.text


def check_cda(content: str, **kwargs) -> tuple:
    # 对CDA注册服务部分字段校验
    # 文档流水号, 文档生成日期时间,文档类型代码, 患者类型
    etree.register_namespace('xmlns', 'urn:hl7-org:v3')

    xml_file = etree.fromstring(content.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
    doc_id = xml_file.xpath('xmlns:id/@extension', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
    cda_code = xml_file.xpath('xmlns:code/@code', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
    cda_name = xml_file.xpath('xmlns:title', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text
    gmt_created = xml_file.xpath('xmlns:effectiveTime/@value', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
    patient_name = xml_file.xpath('//xmlns:patient/xmlns:name', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text

    if (doc_id == kwargs['doc_id'] and cda_code == kwargs['cda_code'] and cda_name == kwargs['cda_name']
            and gmt_created == kwargs['gmt_created'] and patient_name == kwargs['patient_name']):
        return True, 'ok'
    else:
        return False, f"服务和文档内容不一致,详情:{doc_id} ?== {kwargs['doc_id']} and {cda_code} ?== {kwargs['cda_code']} and {cda_name} ?== {kwargs['cda_name']} and {gmt_created} ?== {kwargs['gmt_created']} and {patient_name} ?== {kwargs['patient_name']}"


def verification_hip_detail(schema_name: str, content: str, is_service: bool = False) -> tuple:
    """互联互通服务 schema 校验"""
    schema_file_path = finders.find(
        f'hipmessageservice/services/schemas/{"services" if is_service else "cdas"}/{schema_name}.xsd')

    # 加载XML Schema文件
    schema_file = etree.parse(schema_file_path)
    schema = etree.XMLSchema(schema_file)

    # 加载待验证的XML字符串
    try:
        xml_file = etree.fromstring(content)
    except ValueError:
        xml_file = etree.fromstring(content.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
    except (lxml.etree.XMLSyntaxError,) as e:
        return False, str(e)

    # 验证XML文件是否符合Schema
    valid = schema.validate(xml_file)
    return valid, (str(item) for item in schema.error_log)


def verification_hip(data: dict) -> tuple:
    """互联互通服务校验"""
    content_type = data["content_type"]
    content = base64.b64decode(data[content_type]).decode('utf-8')
    # 服务schema校验
    ok, message = verification_hip_detail(schema_name=content_type, content=content, is_service=True)

    if not ok:
        return ok, message

    match content_type:
        # 个人新增注册和更新
        case 'PatientInfoRegister' | 'PatientInfoUpdate':
            return deal_patient_empi_reg(content)

        # 如果是CDA
        case 'DocumentRegister':
            etree.register_namespace('xmlns', 'urn:hl7-org:v3')
            xml_root = etree.fromstring(content)
            cda_code = xml_root.xpath("//*[@codeSystem='2.16.156.10011.2.5.1.23']")[0].get('code')

            cda_content_base64 = xml_root.find('xmlns:controlActProcess/xmlns:subject/xmlns:clinicalDocument/xmlns'
                                               ':storageCode/xmlns:originalText',
                                               namespaces={'xmlns': 'urn:hl7-org:v3'}).get('value')
            cda_data = base64.b64decode(cda_content_base64).decode('utf-8')

            # cda schema校验
            ok, message = verification_hip_detail(schema_name=cda_code, content=cda_data, is_service=False)

            if not ok:
                return ok, message

            # cda服务三重校验
            cda_name = xml_root.xpath("//xmlns:clinicalDocument/xmlns:code/xmlns:displayName/@value",
                                      namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
            doc_id = xml_root.xpath("//xmlns:clinicalDocument/xmlns:id/xmlns:item/@extension",
                                    namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
            gmt_created = xml_root.xpath("//xmlns:effectiveTime/@value", namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
            patient_name = xml_root.xpath(
                "//xmlns:recordTarget/xmlns:patient/xmlns:patientPerson/xmlns:name/xmlns:item/xmlns:part/@value",
                namespaces={'xmlns': 'urn:hl7-org:v3'})[0]

            ok, message = check_cda(content=cda_data, cda_code=cda_code, cda_name=cda_name, doc_id=doc_id,
                                    gmt_created=gmt_created, patient_name=patient_name)
            return ok, message
        case _:
            pass

    return ok, message


def verification(data: dict) -> tuple:
    """
    消息校验
    :param data: 待校验的消息元素,元素格式请参考标准接口文档
    :return:
    """
    content_type = data["content_type"]
    """校验"""
    match content_type:
        # 互联互通标准服务
        case "PatientInfoRegister" | "PatientInfoUpdate" | "PatientInfoMerge" | "PatientInfoQuery" \
             | "OrganizationInfoRegister" | "OrganizationInfoUpdate" | "OrganizationInfoQuery" | "ProviderInfoRegister" \
             | "ProviderInfoUpdate" | "ProviderInfoQuery" | "TerminologyRegister" | "TerminologyUpdate" \
             | "TerminologyQuery" | "DocumentRegister" | "DocumentAccess" | "DocumentRetrieve" | "EncounterCardInfoAdd" \
             | "EncounterCardInfoUpdate" | "EncounterCardInfoQuery" | "SourceAndScheduleInfoAdd" \
             | "SourceAndScheduleInfoUpdate" | "SourceAndScheduleInfoQuery" | "OutPatientInfoAdd" \
             | "OutPatientInfoUpdate" | "OutPatientInfoQuery" | "InPatientInfoAdd" | "InPatientInfoUpdate" \
             | "InPatientInfoQuery" | "TransferInfoAdd" | "TransferInfoUpdate" | "TransferInfoQuery" \
             | "DischargeInfoAdd" | "DischargeInfoUpdate" | "DischargeInfoQuery" | "OrderInfoAdd" \
             | "OrderInfoUpdate" | "OrderInfoQuery" | "ExamAppInfoAdd" | "ExamAppInfoUpdate" | "ExamAppInfoQuery" \
             | "CheckAppInfoAdd" | "CheckAppInfoUpdate" | "CheckAppInfoQuery" | "PathologyAppInfoAdd" \
             | "PathologyAppInfoUpdate" | "PathologyAppInfoQuery" | "BloodTransAppInfoAdd" | "BloodTransAppInfoUpdate" \
             | "BloodTransAppInfoQuery" | "OperationAppInfoAdd" | "OperationAppInfoUpdate" | "OperationAppInfoQuery" \
             | "OutPatientAppointStatusInfoAdd" | "OutPatientAppointStatusInfoUpdate" \
             | "OutPatientAppointStatusInfoQuery" | "CheckAppointStatusInfoAdd" | "CheckAppointStatusInfoUpdate" \
             | "CheckAppointStatusInfoQuery" | "OrderFillerStatusInfoUpdate" | "OrderFillerStatusInfoQuery" \
             | "CheckStatusInfoUpdate" | "CheckStatusInfoQuery" | "ExamStatusInfoUpdate" | "ExamStatusInfoQuery" \
             | "OperationScheduleInfoAdd" | "OperationScheduleInfoUpdate" | "OperationScheduleInfoQuery" \
             | "OperationStatusInfoUpdate" | "OperationStatusInfoQuery":
            return verification_hip(data)

        # 其他非标准服务
        case 'ExamReportAdd':
            """校验并保存校验报告信息"""
            report = copy.deepcopy(data[content_type])
            del report['patient'], report['details']
            exam_report = ExamReport(**report)
            exam_report.patient_id = data[content_type]['patient']['patient_id']
            # 校验检验报告模型
            try:
                # 校验
                exam_report.full_clean(exclude=('report_id', 'patient'))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    ExamReport.objects.filter(report_id=report.get("report_id", None)).delete()
                    exam_report.save()
                # 校验结果主表
                for main in data[content_type]['details']:
                    temp_main = copy.deepcopy(main)
                    del main['test_items']
                    exam_main = ExamResultMain(**main)
                    exam_main.exam_report_id = exam_report.report_id
                    # 校验
                    exam_main.full_clean(exclude=('exam_report_id', 'order_id'))
                    # 保存到数据库
                    if settings.IS_SAVE_TO_DB:
                        ExamResultMain.objects.filter(exam_report_id=exam_main.exam_report_id,
                                                      order_id=exam_main.order_id).delete()
                        exam_main.save()
                    # 校验结果明细表
                    for detail in temp_main['test_items']:
                        temp_detail = copy.deepcopy(detail)
                        del detail['ast_items']
                        exam_detail = ExamResultDetail(**detail)
                        exam_detail.exam_result_main_id = f"{exam_report.report_id}_{exam_main.order_id}"
                        # 校验
                        exam_detail.full_clean(exclude=('exam_result_main_id', 'item_code'))
                        # 保存到数据库
                        if settings.IS_SAVE_TO_DB:
                            ExamResultDetail.objects.filter(exam_result_main_id=exam_detail.exam_result_main_id,
                                                            item_code=exam_detail.item_code).delete()
                            exam_detail.save()
                        # 如果有药敏则校验
                        if temp_detail['ast_items'] and len(temp_detail['ast_items']) > 0:
                            for item in temp_detail['ast_items']:
                                exam_ast = ExamResultDetailAST(**item)
                                exam_ast.exam_result_detail_id = f"{exam_report.report_id}_{exam_main.order_id}_{exam_detail.item_code}"
                                # 校验
                                exam_ast.full_clean(exclude=('exam_result_detail_id', 'ast_code'))
                                # 保存到数据库
                                if settings.IS_SAVE_TO_DB:
                                    ExamResultDetailAST.objects.filter(
                                        exam_result_detail_id=exam_ast.exam_result_detail_id,
                                        ast_code=exam_ast.ast_code).delete()
                                    exam_ast.save()

            except (ValidationError,) as e:
                return False, [str(item) for item in e]
            else:
                return True, "ok"

        case "ExamReportDelete" | "PathologyReportDelete" | "CheckReportDelete":
            """检查检验报告删除逻辑"""
            report = copy.deepcopy(data[content_type])
            try:
                assert len(report.get('report_id', '')) > 0, "report_id length must be greater than 0"
                assert report.get('org_code', '') == settings.HOSPITAL_CODE, ("Please recheck your request "
                                                                              "parameters org_code!")
                # 数据库操作
                if settings.IS_SAVE_TO_DB:
                    if content_type == "CheckReportDelete":
                        # 检查报告
                        CheckReport.objects.filter(report_id=report.get('report_id', '')).delete()

                    if content_type == "ExamReportDelete":
                        # 检验报告
                        if ExamReport.objects.filter(report_id=report.get('report_id', '')).exists():
                            exam_report = ExamReport.objects.get(report_id=report.get('report_id', ''))
                            if ExamResultMain.objects.filter(exam_report_id=exam_report.report_id).exists():
                                exam_mains = ExamResultMain.objects.filter(exam_report_id=exam_report.report_id)
                                for exam_main in exam_mains:
                                    if ExamResultDetail.objects.filter(
                                            exam_result_main_id=f'{exam_main.exam_report_id}_{exam_main.order_id}').exists():
                                        exam_details = ExamResultDetail.objects.filter(
                                            exam_result_main_id=f'{exam_main.exam_report_id}_{exam_main.order_id}')
                                        for exam_detail in exam_details:
                                            ExamResultDetailAST.objects.filter(
                                                exam_result_detail_id=f'{exam_main.exam_report_id}_{exam_main.order_id}_{exam_detail.index}').delete()
                                        exam_details.delete()
                                exam_mains.delete()
                            exam_report.delete()
            except AssertionError as e:
                return False, str(e)
            else:
                return True, "ok"

        # 检查报告
        case 'CheckReportAdd':
            report = copy.deepcopy(data[content_type])
            del report['patient']
            check_report = CheckReport(**report)
            check_report.patient_id = data[content_type]['patient']['patient_id']
            try:
                # 校验
                check_report.full_clean(exclude=('patient', ))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    # CheckReport.objects.update_or_create(report_id=check_report.report_id, defaults=report)
                    check_report.save()
            except (ValidationError,) as e:
                return False, [str(item) for item in e]
            else:
                return True, 'ok'

        # 门急诊就诊信息更新
        case 'VisitInfoUpdate':
            visit = copy.deepcopy(data[content_type])
            fields = set([field.name for field in Visit._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            filtered_data = {key: value for key, value in visit.items() if key in fields}
            filtered_data.update(**{"from_src": data['send_id'], "patient_id": visit["patient_id"]})
            visit_info = Visit(**filtered_data)
            try:
                # 校验
                visit_info.full_clean(exclude=['patient', 'adm_no'])
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    Visit.objects.update_or_create(adm_no=visit_info.adm_no,  visit_status=visit_info.visit_status,
                                                   doctor_id=visit_info.doctor_id, defaults=filtered_data)
            except (ValidationError,) as e:
                return False, [str(item) for item in e]
            else:
                return True, 'ok'

        case 'getExamReportPrintInfos':
            """ 获取检验报告打印信息 """
            patient_id = data[content_type].get('patient_id', None)
            # 取最近的就诊流水号对应记录
            # 过滤当前时间最近90天的数据
            offset_days_ago = timezone.now() - datetime.timedelta(days=93)
            report = ExamReport.objects.filter(patient_id=patient_id, gmt_created__gte=offset_days_ago).order_by('-bar_code').only('gmt_created').first()
            if report is None:
                return False, 'Not Found'
            report_infos = []
            with connection.cursor() as cursor:
                sql = """
                    select report_id, patient_id, adm_no, url_report_pdf, item_code, item_name
                    from cdr_examreport a
                    inner join cdr_examresultmain b on a.report_id = b.exam_report_id
                    where a.adm_no = %s;
                """
                cursor.execute(sql, [report.adm_no, ])
                for row in cursor.fetchall():
                    report_infos.append({"report_id": row[0], "patient_id": row[1], "adm_no": row[2],
                                         "url_report_pdf": row[3], "item_code": row[4], 'item_name': row[5]})

            return True, report_infos

        case 'DiagIssuedAdd' | 'DiagIssuedUpdate':
            """ 诊断信息新增或更新逻辑 """
            diagnosiss = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in Diagnosis._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            for diagnosis in diagnosiss:
                filtered_data = {key: value for key, value in diagnosis.items() if key in fields}
                diagnosis_info = Diagnosis(**copy.deepcopy(filtered_data))
                filtered_data.update(**{"patient_id": diagnosis["patient_id"]})
                # 校验
                try:
                    diagnosis_info.full_clean(exclude=('diagnosis_id', 'patient'))
                    # 保存到数据库
                    if settings.IS_SAVE_TO_DB:
                        Diagnosis.objects.update_or_create(diagnosis_id=diagnosis_info.diagnosis_id, defaults=filtered_data)
                except ValidationError as e:
                    return False, [str(item) for item in e]
            return True, 'ok'

        case 'DiagIssuedDelete':
            """ 诊断信息撤回 """
            diagnosiss = data[content_type]
            for diagnosis in diagnosiss:
                Diagnosis.objects.filter(diagnosis_id=diagnosis.get('diagnosis_id', None)).delete()
            return True, 'ok'

        case 'PathologyReportAdd':
            """病理结果新增,更新"""
            report = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in PathologyReport._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            filtered_data = {key: value for key, value in report.items() if key in fields}
            filtered_data.update(**{"patient_id": report['patient']['patient_id']})
            report_info = PathologyReport(**copy.deepcopy(filtered_data))
            # 校验
            try:
                report_info.full_clean(exclude=('patient', 'report_id'))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    PathologyReport.objects.update_or_create(report_id=report_info.report_id, defaults=filtered_data)
            except ValidationError as e:
                return False, [str(item) for item in e]

            return True, 'ok'

        case 'PathologyReportDelete':
            """ 病理结果撤回 """
            report = data[content_type]
            PathologyReport.objects.filter(report_id=report.get('report_id', None)).delete()

            return True, 'ok'

        case 'CriticalValueAdd':
            """ 危急值新增"""
            critical = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in CriticalValue._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            filtered_data = {key: value for key, value in critical.items() if key in fields}
            filtered_data.update(**{"patient_id": critical['patient']['patient_id']})

            report_info = CriticalValue(**copy.deepcopy(filtered_data))
            # 校验
            try:
                report_info.full_clean(exclude=('patient', ))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    CriticalValue.objects.update_or_create(critical_id=report_info.critical_id, defaults=filtered_data)

            except ValidationError as e:
                return False, [str(item) for item in e]

            return True, 'ok'

        case 'CriticalValueDelete':
            """ 危急值撤回 """

            critical = data[content_type]
            CriticalValue.objects.filter(critical_id=critical.get('critical_id', None)).delete()

            return True, 'ok'

        case 'CriticalValueDeal':
            """ 危急值处理 """
            critical = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in CriticalValue._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            filtered_data = {key: value for key, value in critical.items() if key in fields}

            try:
                obj = CriticalValue.objects.get(critical_id=filtered_data['critical_id'])
                obj.gmt_recv = filtered_data['gmt_recv']
                obj.recv_dept_id = filtered_data['recv_dept_id']
                obj.recv_dept_name = filtered_data['recv_dept_name']
                obj.recv_opera_id = filtered_data['recv_opera_id']
                obj.recv_opera_name = filtered_data['recv_opera_name']
                obj.process_result = filtered_data['process_result']
                obj.status = 3

                obj.save()
            except CriticalValue.DoesNotExist as e:
                return False, f"{filtered_data['critical_id']}数据不存在"

            return True, 'ok'

        # 叫号服务
        case 'CallPatient':
            """ 叫号服务 """
            call_patient = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in CallPatient._meta.local_fields]) - {'id', 'gmt_created', 'patient'}
            filtered_data = {key: value for key, value in call_patient.items() if key in fields}
            filtered_data.update(**{"patient_id": call_patient['patient_id']})

            call_info = CallPatient(**copy.deepcopy(filtered_data))
            # 校验
            try:
                call_info.full_clean(exclude=('patient',))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    CallPatient.objects.update_or_create(adm_no=call_info.adm_no, gmt_call=call_info.gmt_call, defaults=filtered_data)

            except ValidationError as e:
                return False, [str(item) for item in e]

            return True, 'ok'

        # 患者信息采集
        case 'PatientInfoCollector':
            data = data[content_type]
            # 获取需要保存的数据模型字段列表
            fields = set([field.name for field in PatientInfoCollector._meta.local_fields]) - {'id', 'gmt_created', 'gmt_updated'}
            filtered_data = {key: value for key, value in data.items() if key in fields}

            info = PatientInfoCollector(**copy.deepcopy(filtered_data))
            # 校验
            try:
                info.full_clean(exclude=('id_no', 'debit_card_no'))
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    PatientInfoCollector.objects.update_or_create(id_no=info.id_no, debit_card_no=info.debit_card_no,
                                                         defaults=filtered_data)

            except ValidationError as e:
                return False, [str(item) for item in e]

            return True, 'ok'

        case _:
            return True, "本消息暂未纳入校验范围!"


@router.post("/service/verify/", response={codes_2xx: SendMsgSchemaOut, codes_4xx: SendMsgSchemaOut})
def send_msg(request, payload: SendMsgSchema):
    """服务校验"""
    # dict_payload = payload.dict()
    dict_payload = json.loads(request.body)
    try:
        assert all([dict_payload['content_type'], dict_payload.get(dict_payload['content_type'], None),
                    dict_payload['client_msg_id'], dict_payload["gmt_create"], dict_payload['gmt_send'],
                    dict_payload['send_id'], dict_payload['recv_id']]) is True, \
            "Please recheck your request parameters!"
    except (AssertionError,) as e:
        return 400, {"code": 400, "message": str(e), "msg_id": str(uuid.uuid4()),
                     "gmt_created": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')}
    # 调用校验函数
    ok, message = verification(dict_payload)

    response_code = 200 if ok else 400
    result = {"code": response_code, "message": "ok", "msg_id": str(uuid.uuid4()),
              "gmt_created": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),
              }
    # 验证失败
    if not ok:
        # msg = ','.join(message) if isinstance(message, list) else message
        result.update(**{"detail": message, "message": "Please recheck your request parameters!"})

    # 如果是同步接口,当处理正常需要返回提示内容时
    if ok and dict_payload['content_type'] in ("PatientInfoRegister", "PatientInfoUpdate", "getExamReportPrintInfos"):
        result.update(**{"data": message})

    return response_code, result


@router.post("/service/sign_and_encrypt/")
def sign_and_encrypt(request):
    """加密和签名"""
    hospital_id = settings.HOSPITAL_ID
    key = settings.HOSPITAL_KEY
    encrypt = EncryptUtils(key=key, hospital_id=hospital_id)
    # 数据
    # data = {"name": "测试11", "id_card_no": "111111"}
    data = json.loads(request.body.decode('utf-8'))
    # 签名
    md5_hash, timestamp = encrypt.sign()
    # 加密
    encrypted = encrypt.encrypt(data)

    content = {"sign": md5_hash, "encrypted": encrypted, "timestamp": timestamp}
    return content


if __name__ == "__main__":
    pass
