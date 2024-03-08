import itertools

import xlsxwriter
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from openpyxl.styles import Alignment, Side, Border

from hipmessageservice.models import Service, Application, StatusShip


# Create your views here.
def index(request):
    services = Service.objects.filter(is_deleted=False).order_by("service_queue")
    applications = Application.objects.filter(is_deleted=False, firm__isnull=False).order_by('-firm')
    status = StatusShip.objects.filter(is_deleted=False)
    return render(request, 'hipmessageservice/index.html',
                  context={'services': services, 'applications': applications, 'status': status})



def read_all() -> list:
    sql = """select d.firm_name_short, c.application_name, a.service_name||'|'||a.service_code as service, status
            from hipmessageservice_service a
            left join hipmessageservice_statusship b on a.id = b.service_id
            left join hipmessageservice_application c on c.id = b.application_id
            left join hipmessageservice_firm d on d.id = b.application_id
            where a.is_deleted = FALSE
            order by a.service_queue asc;
            """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        items = cursor.fetchall()

    return list(items)

def read_cda() -> list:
    sql = """
        select value, comment, c.firm_name_short, 1 status
        from hipmessageservice_cda a
        left join hipmessageservice_cda_firm b on a.id = b.cda_id
        left join hipmessageservice_firm c on b.firm_id = c.id
        where a.is_deleted = false
        order by value asc, b.firm_id asc;
    """

    with connection.cursor() as cursor:
        cursor.execute(sql)
        items = cursor.fetchall()

    return list(items)


def test_data(request):


    import pandas as pd

    items1 = read_all()
    items2 = read_cda()

    df = pd.DataFrame(items1, columns=['firm_name', 'application_name', 'service', "status"])
    df2 = pd.DataFrame(items2, columns=['value','comment', 'firm_name_short', "status"])

    result = df.pivot_table(values="status", index="service", columns=['firm_name', "application_name"])
    result2 = df2.pivot_table(values="status", index=['value', 'comment'], columns=["firm_name_short"])

    writer = pd.ExcelWriter("hipmessageservice/resutls.xlsx")
    result.to_excel(writer, index=True, sheet_name="交互场景")
    result2.to_excel(writer, index=True, sheet_name="分工-CDA")

    # 设置样式
    sheet = writer.sheets['交互场景']
    format = writer.book.add_format({'fg_color': '#D7E4BC', 'bold': True, 'align': 'center', 'valign': 'vcenter',
                                     'border': 2, 'text_wrap': True})
    sheet.set_column('B:AE', 5, cell_format=format)
    sheet.set_column('A:A', 20)

    sheet2 = writer.sheets['分工-CDA']
    sheet2.set_column('A:I', 10, cell_format=format)

    # 关闭并保存到文件
    writer.close()

    return HttpResponse(result, status=200)