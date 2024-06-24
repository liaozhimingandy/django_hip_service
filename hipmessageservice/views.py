import base64
import copy
import datetime
import uuid
from http import HTTPStatus
from zoneinfo import ZoneInfo

import lxml
import openpyxl
import pandas as pd
import requests
from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.exceptions import ValidationError
from django.db import connection
from django.db import transaction
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import never_cache
from json2xml import json2xml
from lxml import etree
from openpyxl.styles import Font, Border, Side, Alignment
from openpyxl.styles.fills import PatternFill
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from cdr.models import ExamReport, ExamResultMain, ExamResultDetail, ExamResultDetailAST, CheckReport
from .authentication import AuthBearer
from hipmessageservice.models import Service, Application, StatusShip
from hipmessageservice.serializers import HIPServiceSerializer, HIPCDASerializer, CheckReportSerializer, \
    ExamReportSerializer, ExamResultMainSerializer
from hipmessageservice.utils.database import read_cda
from .utils.encrypt import EncryptUtils


# Create your views here.
@never_cache
@transaction.non_atomic_requests
def index(request):
    services = (Service.objects.filter(is_deleted=False)
                .only('service_id', 'service_name', 'service_code', 'is_v3', "id", "service_queue")).order_by(
        "service_queue")
    status = (
        StatusShip.objects.filter(is_deleted=False, service__is_deleted=False).only("service_id", "application_id",
                                                                                    "status"))
    dict_status = {}
    for obj in status:
        dict_status[f"{obj.service_id}-{obj.application_id}"] = obj.status

    applications = (Application.objects.filter(is_deleted=False, firm__isnull=False).order_by('-firm')
                    .prefetch_related('firm').only("id", 'application_name', "firm_id", 'firm__firm_name_short'))

    return render(request, 'hipmessageservice/index.html',
                  context={'services': services, 'applications': applications, 'status': status,
                           'dict_status': dict_status})


def read_all() -> list:
    sql = """select a.service_code, a.service_name, d.firm_name_short, c.application_name, b.status, a.service_queue
            from hipmessageservice_service a
            right join hipmessageservice_statusship b on a.id = b.service_id and b.is_deleted=False
            right join hipmessageservice_application c on c.id = b.application_id and b.is_deleted=False
            right join hipmessageservice_firm d on d.id = c.firm_id
            where a.is_deleted = False
            order by a.service_queue asc;
            """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        items = cursor.fetchall()

    return list(items)


def generate_cda(df_all):
    """
    生成cda分工sheet
    :return:
    """

    list_cda = read_cda()
    str_sheet_name = '分工-CDA'

    df = (pd.DataFrame(list_cda, columns=['value', 'comment', 'firm__firm_name_short', "count"]))
    result = df.pivot_table(values="count", index=['value', 'comment'], columns=["firm__firm_name_short"])

    # 替换值
    result.replace(1, '√', inplace=True)
    writer = pd.ExcelWriter("temp/results.xlsx", engine="xlsxwriter")

    # 保存交互场景
    df_all.to_excel(writer, sheet_name="交互场景", index=True, index_label=0)

    # 设置样式
    format_sheet = writer.book.add_format({'fg_color': '#D7E4BC', 'bold': True, 'align': 'center', 'valign': 'vcenter',
                                           'border': 2, 'text_wrap': True})
    result.to_excel(writer, index=True, sheet_name=str_sheet_name, index_label=['CDA文档代码', 'CDA文档名称'])
    sheet = writer.sheets[str_sheet_name]
    sheet.set_column('A1:I47', 18, cell_format=format_sheet)

    writer.close()


def cell_style(sheet, cell, style_name, style):
    sheet[cell][style_name] = style


def generate_data():
    map_status = {1: '订阅', 2: "发布", 3: "全部"}
    filename = "temp/results.xlsx"
    statuss = StatusShip.objects.filter(is_deleted=False).only("application__firm__firm_name_short").distinct(
        "application__firm__firm_name_short")

    # 样式
    font = Font(size=16, bold=True, color='FF000000')
    border = Border(left=Side(border_style='thin', color='FF000000'),
                    right=Side(border_style='thin', color='FF000000'),
                    top=Side(border_style='thin', color='FF000000'),
                    bottom=Side(border_style='thin', color='FF000000'))
    orange_fill = PatternFill(fill_type='solid', fgColor="1890ff")
    # 居中所有单元格
    align = Alignment(horizontal='center', vertical='center', wrapText=False)

    for status in statuss:
        if not status.application.firm:
            continue

        book = openpyxl.load_workbook(filename)
        sheet = book.create_sheet(title=f"交互服务分工-{status.application.firm.firm_name_short}")
        index = 1

        items = (StatusShip.objects.filter(application__firm__firm_name_short=status.application.firm.firm_name_short,
                                           service__is_deleted=False).values('service__service_name',
                                                                             'service__service_code', 'status')
                 .distinct('service__service_name', 'service__service_code', 'status'))

        sheet[f'A{index}'] = f"以下为您需要完成的交互服务|统计日期:{datetime.datetime.now().strftime('%Y-%m-%d')}"
        # cell_style(sheet, f'A{index}', "font", font)
        sheet[f'A{index}'].font = font
        sheet[f'A{index}'].border = border
        sheet[f'A{index}'].alignment = align
        sheet.merge_cells('A1:C1')

        index += 1

        sheet[f'A{index}'] = "服务名称"
        sheet[f'B{index}'] = "服务代码"
        sheet[f'C{index}'] = "发布订阅关系"
        sheet[f'A{index}'].font = font
        sheet[f'B{index}'].font = font
        sheet[f'C{index}'].font = font
        sheet[f'A{index}'].border = border
        sheet[f'B{index}'].border = border
        sheet[f'C{index}'].border = border
        sheet[f'A{index}'].fill = orange_fill
        sheet[f'B{index}'].fill = orange_fill
        sheet[f'C{index}'].fill = orange_fill
        sheet[f'A{index}'].alignment = align
        sheet[f'B{index}'].alignment = align
        sheet[f'C{index}'].alignment = align

        for item in items:
            sheet[f'A{index + 1}'] = item['service__service_name']
            sheet[f'B{index + 1}'] = item['service__service_code']
            sheet[f'C{index + 1}'] = map_status.get(item['status'])

            sheet[f'A{index + 1}'].font = font
            sheet[f'B{index + 1}'].font = font
            sheet[f'C{index + 1}'].font = font
            sheet[f'A{index + 1}'].border = border
            sheet[f'B{index + 1}'].border = border
            sheet[f'C{index + 1}'].border = border

            index += 1

        sheet.column_dimensions["A"].width = 60
        sheet.column_dimensions["B"].width = 60
        sheet.column_dimensions["C"].width = 60
        book.save(filename)

        # break


def generate_service_all():
    list_data = read_all()
    df = pd.DataFrame.from_records(list_data, columns=['service_code', 'service_name', 'firm_name_short',
                                                       'application_name', 'status', 'service_queue'])

    result = df.pivot_table(values="status", index=['service_queue', 'service_code', 'service_name'],
                            columns=["firm_name_short", 'application_name'])  # 暂不支持dropna=False

    result.sort_values(by='service_queue', ascending=True)
    result.replace(1, '订阅', inplace=True)
    result.replace(2, '发布', inplace=True)
    result.replace(3, '全部', inplace=True)

    # result.to_excel("temp/results.xlsx", sheet_name='交互场景', index=True)
    return result


def generate_report(request):
    generate_service_all()
    return HttpResponse("ok", content_type='text')


def download(request):
    import os
    if not os.path.exists("temp"):
        os.makedirs("temp")
    if os.path.exists("temp/results.xlsx"):
        os.remove("temp/results.xlsx")

    # 生成消息场景
    df = generate_service_all()
    # 生成cda统计数据
    generate_cda(df)
    # 生成交互服务分工
    generate_data()

    return FileResponse(open('temp/results.xlsx', 'rb'), as_attachment=True,
                        filename=f'医院信息平台交互规范-交互场景-{datetime.datetime.now().strftime("%Y-%m-%d")}.xlsx')


def home(request):
    services = (Service.objects.filter(is_deleted=False)
                .only('service_id', 'service_name', 'service_code', 'is_v3', "id"))
    status = (
        StatusShip.objects.filter(is_deleted=False, service__is_deleted=False).only("service_id", "application_id",
                                                                                    "status"))
    dict_status = {}
    for obj in status:
        dict_status[f"{obj.service_id}-{obj.application_id}"] = obj.status

    applications = (Application.objects.filter(is_deleted=False, firm__isnull=False).order_by('-firm')
                    .prefetch_related('firm').only("id", 'application_name', "firm_id", 'firm__firm_name_short'))

    return render(request, 'hipmessageservice/home.html',
                  context={'services': services, 'applications': applications, 'status': status,
                           'dict_status': dict_status, 'user': request.user})


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
    "ethnic_group_code": "//xmlns:ethnicGroupCode/xmlns:item/xmlns:displayName/@value",
    "ethnic_group_name": "//xmlns:ethnicGroupCode/xmlns:item/@code",
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
    "org_code": "//xmlns:providerOrganization/xmlns:name/xmlns:item/xmlns:part/@value",
    "org_name": "//xmlns:providerOrganization/xmlns:id/xmlns:item/@extension",
    "ins_code": "//xmlns:beneficiary/xmlns:code/@code",
    "ins_name": "//xmlns:beneficiary/xmlns:code/xmlns:displayName/@value",
    "author_id": "//xmlns:author/xmlns:assignedEntity/xmlns:assignedPerson/xmlns:name/xmlns:item/xmlns:part/@value",
    "author": "//xmlns:author/xmlns:assignedEntity/xmlns:id/xmlns:item/@extension",
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
    "CONTACT_ADDRESS": "",
    "ABO_BLOOD_TYPE_CODE": "",
    "ABO_BLOOD_TYPE_NAME": "",
    "RH_BLOOD_TYPE_CODE": "",
    "RH_BLOOD_TYPE_NAME": "",
    "CREATE_BY": "",
    "CREATE_TIME": "",
    "MEDICAL_RECORD_NO": "",
    "OP_MEDICAL_RECORD_NO": "",
    "Passport_GA": "",
    "BEIJING_MEDICAL_CARD_NO": "",
    "VIP_INDICATOR": "",
    "DEATH_INDICATOR": "",
    "DOD": "",
    "HOSPITAL_CARD_NO": "",
    "CATEGORY_CODE": ""
}


def DealPatient(content):
    """处理个人新增注册,更新接口,调取empi注册接口,并且保存到数据库"""
    from lxml import etree
    etree.register_namespace('xmlns', 'urn:hl7-org:v3')
    xml_root = etree.fromstring(content)
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
    payload = f"""
            <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:car="http://www.caradigm.com/">
           <soap:Header/>
           <soap:Body>
              <car:IndexRegisterFunc>
                 <!--Optional:-->
                 <car:xml>
                 <![CDATA[{xml_data.replace('<?xml version="1.0" ?>', '')}]]>
                 </car:xml>
              </car:IndexRegisterFunc>
           </soap:Body>
        </soap:Envelope>
        """
    # 调empi接口进行患者注册
    response = requests.post(settings.EMPI_API_URL, data=payload, headers={'Content-Type': 'text/xml'}, timeout=2)

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

            return True, f"#empi:{empi}#"
        else:
            return False, empi_root.find('.//message').text

    else:
        return False, response.text


class VerificationViewset(viewsets.ViewSet):
    """
    单一服务或CDA校验
    """

    # authentication_classes = [AuthBearer]
    def list(self, request):
        """
        用于生成根路由地址
        :param request:
        :return:
        """
        return Response(data="hello world", status=HTTPStatus.OK)

    @staticmethod
    def _validate(schema_name: str, content: str, is_service: bool = False) -> tuple:
        """schema 校验"""

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

    @staticmethod
    def _check_cda(content: str, **kwargs) -> tuple:
        # 对CDA注册服务部分字段校验
        # 文档流水号, 文档生成日期时间,文档类型代码, 患者类型
        etree.register_namespace('xmlns', 'urn:hl7-org:v3')

        xml_file = etree.fromstring(content.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
        doc_id = xml_file.xpath('xmlns:id/@extension', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        cda_code = xml_file.xpath('xmlns:code/@code', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        cda_name = xml_file.xpath('xmlns:title', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text
        gmt_created = xml_file.xpath('xmlns:effectiveTime/@value', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        patient_name = xml_file.xpath('//xmlns:patient/xmlns:name', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text

        if doc_id == kwargs['doc_id'] and cda_code == kwargs['cda_code'] and cda_name == kwargs[
            'cda_name'] and gmt_created == kwargs['gmt_created'] and patient_name == kwargs['patient_name']:
            return True, 'ok'
        else:
            return False, f"服务和文档内容不一致,详情:{doc_id} ?== {kwargs['doc_id']} and {cda_code} ?== {kwargs['cda_code']} and {cda_name} ?== {kwargs['cda_name']} and {gmt_created} ?== {kwargs['gmt_created']} and {patient_name} ?== {kwargs['patient_name']}"

    @action(methods=['post'], detail=False)
    def service(self, request):
        """
        服务校验,对互联互通标准服务进行校验
        :param request:
        :return:
        """
        # 序列化校验
        serializer = HIPServiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service_name = serializer.validated_data['service_code']
        content = serializer.validated_data['content']
        # 服务schema校验
        valid = self._validate(schema_name=service_name, content=content, is_service=True)

        # 特殊服务校验
        match service_name:
            # 个人信息注册,更新则需要进行empi注册和保存到数据库
            case 'PatientInfoRegister' | 'PatientInfoUpdate':
                created, message = DealPatient(content)
                if created:
                    return Response(data={"message": message}, status=HTTPStatus.OK)
                else:
                    return Response(data={"message": message}, status=HTTPStatus.BAD_REQUEST)
            # 如果是CDA
            case 'DocumentRegister':
                etree.register_namespace('xmlns', 'urn:hl7-org:v3')
                xml_root = etree.fromstring(content)

                cda_code = xml_root.xpath("//*[@codeSystem='2.16.156.10011.2.5.1.23']")[0].get('code')

                cda_content_base64 = xml_root.find('xmlns:controlActProcess/xmlns:subject/xmlns:clinicalDocument/xmlns'
                                                   ':storageCode/xmlns:originalText',
                                                   namespaces={'xmlns': 'urn:hl7-org:v3'}).get('value')
                cda_data = base64.b64decode(cda_content_base64).decode('utf-8')
                valid = self._validate(schema_name=cda_code, content=cda_data, is_service=False)

                # cda服务三重校验
                cda_name = xml_root.xpath("//xmlns:clinicalDocument/xmlns:code/xmlns:displayName/@value",
                                          namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
                doc_id = xml_root.xpath("//xmlns:clinicalDocument/xmlns:id/xmlns:item/@extension",
                                        namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
                gmt_created = xml_root.xpath("//xmlns:effectiveTime/@value", namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
                patient_name = xml_root.xpath(
                    "//xmlns:recordTarget/xmlns:patient/xmlns:patientPerson/xmlns:name/xmlns:item/xmlns:part/@value",
                    namespaces={'xmlns': 'urn:hl7-org:v3'})[0]

                ok, message = self._check_cda(content=cda_data, cda_code=cda_code, cda_name=cda_name, doc_id=doc_id,
                                              gmt_created=gmt_created, patient_name=patient_name)
                if ok:
                    return Response(data={"message": message}, status=HTTPStatus.OK)
                else:
                    return Response(data={"message": message}, status=HTTPStatus.BAD_REQUEST)

        return Response(data={"message": str(valid[0]) if valid[0] else valid[1]},
                        status=HTTPStatus.OK if valid[0] else HTTPStatus.BAD_REQUEST)

    @action(methods=['post'], detail=False)
    def cda(self, request):
        """
        CDA服务进行校验
        :param request:
        :return:
        """
        serializer = HIPCDASerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cda_code = serializer.validated_data['cda_code']
        content = serializer.validated_data['content']

        valid = self._validate(schema_name=cda_code, content=content, is_service=False)

        return Response(data={"message": "ok" if valid[0] else valid[1]}, status=HTTPStatus.OK)

    @action(methods=['post'], detail=False, url_path=r'test_service/(?P<service_name>\w+)')
    def test_service(self, request, service_name):

        schema_file_path = finders.find(f'hipmessageservice\services\schemas\services\{service_name}.xsd')

        # 加载XML Schema文件
        schema_file = etree.parse(schema_file_path)
        schema = etree.XMLSchema(schema_file)

        # 加载待验证的XML文件
        xml_file = etree.parse(request.data)

        # 验证XML文件是否符合Schema
        valid = schema.validate(xml_file)
        if valid:
            print("XML文件验证成功！")
        else:
            print("XML文件验证失败！")
            print(schema.error_log)

        return Response({"message": "Verified"})


class HIPMessageServiceViewSet(viewsets.ViewSet):
    """
    实现消息校验及签名
    """

    def list(self, request):
        return Response({"message": "This is a list view"})

    def _check_cda(self, content: str, **kwargs) -> tuple:
        # 对CDA注册服务部分字段校验
        # 文档流水号, 文档生成日期时间,文档类型代码, 患者类型
        etree.register_namespace('xmlns', 'urn:hl7-org:v3')

        xml_file = etree.fromstring(content.replace('<?xml version="1.0" encoding="UTF-8"?>', ''))
        doc_id = xml_file.xpath('xmlns:id/@extension', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        cda_code = xml_file.xpath('xmlns:code/@code', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        cda_name = xml_file.xpath('xmlns:title', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text
        gmt_created = xml_file.xpath('xmlns:effectiveTime/@value', namespaces={'xmlns': 'urn:hl7-org:v3'})[0]
        patient_name = xml_file.xpath('//xmlns:patient/xmlns:name', namespaces={'xmlns': 'urn:hl7-org:v3'})[0].text

        if doc_id == kwargs['doc_id'] and cda_code == kwargs['cda_code'] and cda_name == kwargs[
            'cda_name'] and gmt_created == kwargs['gmt_created'] and patient_name == kwargs['patient_name']:
            return True, 'ok'
        else:
            return False, f"服务和文档内容不一致,详情:{doc_id} ?== {kwargs['doc_id']} and {cda_code} ?== {kwargs['cda_code']} and {cda_name} ?== {kwargs['cda_name']} and {gmt_created} ?== {kwargs['gmt_created']} and {patient_name} ?== {kwargs['patient_name']}"

    def _verification_hip_detail(self, schema_name: str, content: str, is_service: bool = False) -> tuple:
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

    def _verification_hip(self, data: dict) -> tuple:
        """对互联互通服务校验"""
        content_type = data["content_type"]
        content = base64.b64decode(data[content_type]).decode('utf-8')
        # 服务schema校验
        ok, message = self._verification_hip_detail(schema_name=content_type, content=content, is_service=True)

        if not ok:
            return ok, message

        match content_type:
            # 个人新增注册和更新
            case 'PatientInfoRegister' | 'PatientInfoUpdate':
                return DealPatient(content)

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
                ok, message = self._verification_hip_detail(schema_name=cda_code, content=cda_data, is_service=False)
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

                ok, message = self._check_cda(content=cda_data, cda_code=cda_code, cda_name=cda_name, doc_id=doc_id,
                                              gmt_created=gmt_created, patient_name=patient_name)
                return ok, message
            case _:
                pass

        return ok, message

    def _verification(self, data: dict) -> tuple:
        """
        校验函数,对请求的消息内容进行校验
        :param data:
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
                return self._verification_hip(data)
            # 其他非标准服务
            case 'ExamReportAdd':
                report = copy.deepcopy(data[content_type])
                del report['patient'], report['details']
                # 校验报告
                instance, created = ExamReport.objects.update_or_create(report_id=report.get("report_id", None),
                                                                         defaults=report)
                exam_report_serializer = ExamReportSerializer(data=report, instance=instance)
                if not exam_report_serializer.is_valid():
                    return False, exam_report_serializer.errors
                # 保存到数据库
                if settings.IS_SAVE_TO_DB:
                    exam_report_serializer.save()
                # 校验检验报告模型
                try:
                    # 校验主表
                    for main in data[content_type]['details']:
                        temp_main = copy.deepcopy(main)
                        del main['test_items']
                        exam_main = ExamResultMain(**main)
                        exam_main.exam_report_id = exam_report_serializer.validated_data['report_id']
                        exam_main.full_clean()
                        # 保存到数据库
                        if settings.IS_SAVE_TO_DB:
                            ExamResultMain.objects.filter(exam_report_id=exam_main.exam_report_id,
                                                          apply_id=exam_main.apply_id).delete()
                            exam_main.save()
                        # 校验明细表
                        for detail in temp_main['test_items']:
                            temp_detail = copy.deepcopy(detail)
                            del detail['ast_items']
                            exam_detail = ExamResultDetail(**detail)
                            exam_detail.exam_result_main_id = f"{exam_report_serializer.validated_data['report_id']}_{exam_main.apply_id}"
                            exam_detail.full_clean()
                            # 保存到数据库
                            if settings.IS_SAVE_TO_DB:
                                ExamResultDetail.objects.filter(exam_result_main_id=exam_detail.exam_result_main_id,
                                                                item_code=exam_detail.item_code).delete()
                                exam_detail.save()
                            # 如果有药敏则校验
                            if temp_detail['ast_items'] and len(temp_detail['ast_items']) > 0:
                                for item in temp_detail['ast_items']:
                                    exam_ast = ExamResultDetailAST(**item)
                                    exam_ast.exam_result_detail_id = f"{exam_report_serializer.validated_data['report_id']}_{exam_main.apply_id}_{exam_detail.index}"
                                    exam_ast.full_clean()
                                    # 保存到数据库
                                    if settings.IS_SAVE_TO_DB:
                                        ExamResultDetailAST.objects.filter(
                                            exam_result_detail_id=exam_ast.exam_result_detail_id,
                                            ast_code=exam_ast.ast_code).delete()
                                        exam_ast.save()
                except (ValidationError,) as e:
                    return False, [str(item) for item in e]
                else:
                    return True, 'ok'
            case "ExamReportDelete" | "PathologyReportDelete" | "CheckReportDelete":
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
                                        if ExamResultDetail.objects.filter(exam_result_main_id=f'{exam_main.exam_report_id}_{exam_main.apply_id}').exists():
                                            exam_details = ExamResultDetail.objects.filter(exam_result_main_id=f'{exam_main.exam_report_id}_{exam_main.apply_id}')
                                            for exam_detail in exam_details:
                                                ExamResultDetailAST.objects.filter(exam_result_detail_id=f'{exam_main.exam_report_id}_{exam_main.apply_id}_{exam_detail.index}').delete()
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
                instance, created = CheckReport.objects.update_or_create(report_id=report.get("report_id", None),
                                                                         defaults=report)
                serializer = CheckReportSerializer(data=report, instance=instance)
                # 校验
                if serializer.is_valid():
                    # 保存到数据库
                    if settings.IS_SAVE_TO_DB:
                        serializer.save()
                    return True, "ok"
                else:
                    return False, serializer.errors

            case _:
                return True, "本消息暂未纳入校验范围!"

    @action(detail=False, methods=['post'], url_path=r'verify')
    def send_msg(self, request):
        """
        服务内容校验 <br>
        :param request:<br>
        :return: <br>
        """
        payload = request.data
        try:
            assert all([payload['content_type'], payload.get(payload['content_type'], None),
                        payload['client_msg_id'], payload["gmt_create"], payload['gmt_send'],
                        payload['send_id'], payload['recv_id']]) is True, "请重新检查您的参数,必要参数缺失"
        except (AssertionError,) as e:
            return 400, {"code": 400, "message": str(e), "msg_id": uuid.uuid4(),
                         "gmt_created": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')}
        # 调用检验函数
        ok, message = self._verification(payload)

        response_code = 200 if ok else 400
        result = {"code": response_code, "message": 'ok', "msg_id": uuid.uuid4(),
                  "gmt_created": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds')}
        # 验证失败
        if not ok:
            # msg = ','.join(message) if isinstance(message, list) else message
            detail = message
            result.update(**{"detail": detail, "message": "Please recheck your request parameters!"})

        # 如果是同步接口,当处理正常需要返回提示内容时
        if ok and payload['content_type'] in ("PatientInfoRegister", "PatientInfoUpdate"):
            result.update(**{"msg": message, "data": message})

        return Response(data=result, status=HTTPStatus.OK)

    @action(detail=False, methods=['post'], url_path='sign_and_encrypt')
    def sign_and_encrypt(self, request):
        """省互认需要的签名和加密"""
        hospital_id = settings.HOSPITAL_ID
        key = settings.HOSPITAL_KEY
        encrypt = EncryptUtils(key=key, hospital_id=hospital_id)
        # 数据
        # data = {"name": "测试11", "id_card_no": "111111"}
        data = request.data
        # 签名
        md5_hash, timestamp = encrypt.sign()
        # 加密
        encrypted = encrypt.encrypt(data)

        content = {"sign": md5_hash, "encrypted": encrypted, "timestamp": timestamp}
        return Response(data=content, status=HTTPStatus.OK)
