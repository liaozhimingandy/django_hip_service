import datetime

import openpyxl
from django.db import connection
from django.http import FileResponse, HttpResponse
from django.shortcuts import render
from openpyxl.styles import Font, Border, Side, Alignment
from openpyxl.styles.fills import PatternFill
import pandas as pd

from hipmessageservice.models import Service, Application, StatusShip
from hipmessageservice.utils.database import read_cda


# Create your views here.
def index(request):
    services = Service.objects.filter(is_deleted=False).order_by("service_queue")
    applications = Application.objects.filter(is_deleted=False, firm__isnull=False).order_by('-firm')
    status = StatusShip.objects.filter(is_deleted=False)
    return render(request, 'hipmessageservice/index.html',
                  context={'services': services, 'applications': applications, 'status': status})


def read_all() -> list:
    sql = """select a.service_code, a.service_name, d.firm_name_short, c.application_name, b.status, a.service_queue
            from hipmessageservice_service a
            right join hipmessageservice_statusship b on a.id = b.service_id and b.is_deleted=False
            right join hipmessageservice_application c on c.id = b.application_id and b.is_deleted=False
            right join hipmessageservice_firm d on d.id = c.firm_id
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
    result.replace(1, '发布', inplace=True)
    result.replace(2, '订阅', inplace=True)
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
