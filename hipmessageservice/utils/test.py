#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""=================================================
    @Project: django_hip_service
    @File： test.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-04-23 16:06
    @Desc: 
================================================="""
import json

def get_services_info():
    """
    获取服务信息
    :return:
    """
    import sqlite3
    # 连接到SQLite数据库
    conn = sqlite3.connect(r'D:\Projects\django_hip_service\cdr.db')
    cur = conn.cursor()

    sql_send = """
    select b.is_mock, d.firm_name_short, b.application_category, b.application_name, GROUP_CONCAT(distinct  c.service_name) AS list_send
    from hipmessageservice_mock a
    left join hipmessageservice_application b on a.send_id = b.application_id
    left join hipmessageservice_service c on a.service_id = c.service_code
    left join hipmessageservice_firm d on b.firm_id = d.id
    where b.is_deleted = 0
    group by b.is_mock,d.firm_name_short, b.application_category, b.application_name;
    """

    cur.execute(sql_send)
    items = cur.fetchall()

    dict_send = {}
    for item in items:
        dict_send[item[3]] = {"short_name": item[1], "app_name": item[3], "category": item[2], "services_send": item[4], "is_mock": item[0]}


    sql_receive = """
    select b.is_mock,d.firm_name_short, b.application_category, b.application_name, GROUP_CONCAT(distinct c.service_name) AS list_recv
    from hipmessageservice_mock a
    left join hipmessageservice_application b on a.receive_id = b.application_id
    left join hipmessageservice_service c on a.service_id = c.service_code
    left join hipmessageservice_firm d on b.firm_id = d.id
    where b.is_deleted = 0
    group by b.is_mock, d.firm_name_short,b.application_category, b.application_name;
    """

    cur.execute(sql_receive)
    items = cur.fetchall()
    for item in items:
        if item[3] in dict_send:
        # dict_send[item[3]] = {"short_name": item[1], "category": item[2], "services": item[4], "is_mock": item[0]}
            dict_send[item[3]]["services_recv"] = item[4]
        else:
            dict_send[item[3]] = {"short_name": item[1], "app_name": item[3], "category": item[2], "services_recv": item[4], "is_mock": item[0]}

    list_services_info = list(dict_send.values())
    list_services_info.sort(key=lambda x: x["category"])

    for item in list_services_info:
        print(item)

    #     导出到csv文件
    import csv
    with open('services_info.csv', 'w', newline='', encoding='gbk') as f:
        fieldnames = ['short_name', 'app_name', 'category', 'services_send', 'services_recv', 'is_mock']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'short_name':'系统体系', 'app_name':  '业务系统', 'category':'分类', 'services_send':'推送服务',
                        'services_recv':'接收服务', 'is_mock': '联通情况'})
        writer.writerows(list_services_info)


def test1():
    # https://the-x.cn/zh-cn/cryptography/Sm4.aspx
    app_id = '19d8dca4b4c247f0bcd1c646bce94a10'
    app_key = '041cac65e6fecaeb59e352341baaf56823e1aa0ea36acf57c086c7f2371de51518e82edbfe5680f98cfe1f2e718fcec9f5bec1c64b015a7b052a3d89c8eee72f9f'
    app_secret = '423414dd8e04dfaaa1d82a115b017547022e9491c40ce9a818d2cde81bac0745'

    from gmssl import sm4
    from gmssl.sm4 import CryptSM4

    # 创建一个SM4加密器
    sm4_crypt = CryptSM4()
    # 设置密钥
    sm4_crypt.set_key(app_id.encode(), sm4.SM4_ENCRYPT)
    # 加密
    new_key_str = sm4_crypt.crypt_ecb(app_secret.encode()).hex().upper()
    print(new_key_str[:32])

    data = {"name": "John Doe", "age": 10, "description": "This is a test object"}
    content = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
    print(content)

    sm4_crypt.set_key(new_key_str[:32].encode(), sm4.SM4_ENCRYPT)
    result = sm4_crypt.crypt_ecb(content.encode()).hex().upper()

    print(result)


if __name__ == "__main__":
    get_services_info()
