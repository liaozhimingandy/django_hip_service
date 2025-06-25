#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=================================================
    @Project: django_hip_service
    @File： utils.py
    @Author：liaozhimingandy
    @Email: liaozhimingandy@gmail.com
    @Date：2024-10-09 9:23
    @Desc: cda导出工具类
=================================================
"""
import os
import shutil
import zipfile

from typing import Annotated
from typing_extensions import Doc
import pandas as pd
import pymssql

cda_map = {
    'C0001': '病历概要',
    'C0002': '门（急）诊病历',
    'C0003': '急诊留观病历',
    'C0004': '西药处方',
    'C0005': '中药处方',
    'C0006': '检查报告',
    'C0007': '检验报告',
    'C0008': '治疗记录',
    'C0009': '一般手术记录',
    'C0010': '麻醉术前访视记录',
    'C0011': '麻醉记录',
    'C0012': '麻醉术后访视记录',
    'C0013': '输血记录',
    'C0014': '待产记录',
    'C0015': '阴道分娩记录',
    'C0016': '剖宫产记录',
    'C0017': '一般护理记录',
    'C0018': '病重（病危）护理记录',
    'C0019': '手术护理记录',
    'C0020': '生命体征测量记录',
    'C0021': '出入量记录',
    'C0022': '高值耗材使用记录',
    'C0023': '入院评估',
    'C0024': '护理计划',
    'C0025': '出院评估与指导',
    'C0026': '手术知情同意书',
    'C0027': '麻醉知情同意书',
    'C0028': '输血治疗同意书',
    'C0029': '特殊检查及特殊治疗同意书',
    'C0030': '病危（重）通知书',
    'C0031': '其他知情告知同意书',
    'C0032': '住院病案首页',
    'C0033': '中医住院病案首页',
    'C0034': '入院记录',
    'C0035': '24小时内入出院记录',
    'C0036': '24小时内入院死亡记录',
    'C0037': '首次病程记录',
    'C0038': '日常病程记录',
    'C0039': '上级医师查房记录',
    'C0040': '疑难病例讨论记录',
    'C0041': '交接班记录',
    'C0042': '转科记录',
    'C0043': '阶段小结',
    'C0044': '抢救记录',
    'C0045': '会诊记录',
    'C0046': '术前小结',
    'C0047': '术前讨论',
    'C0048': '术后首次病程记录',
    'C0049': '出院记录',
    'C0050': '死亡记录',
    'C0051': '死亡病例讨论记录',
    'C0052': '住院医嘱',
    'C0053': '出院小结'
}


class CDATool:

    def __init__(self, ip='localhost', dbname='CDADB', user='caradigm', password='Knt2020@lh', port="1433"):
        self.ip = ip
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn = None

    def get_cursor(self):
        try:
            self.conn = pymssql.connect(server=self.ip, user=self.user, password=self.password, database=self.dbname, tds_version='7.0')
        except(Exception,) as e:
            return None
        else:
            return self.conn.cursor()

    def __del__(self):
        if self.conn:
            self.conn.close()

    @classmethod
    def collect_data_to_csv(cls, data: dict, file_name='') -> None:
        list_cda_collect_data = []
        for item in cda_map.items():
            list_cda_collect_data.append((item[0], item[1], data.get(item[0], 0)))

        name = ['文档类型代码', '文档类型名称', '文档数量']
        df = pd.DataFrame(columns=name, data=list_cda_collect_data)

        df.to_excel(f'统计数据-{file_name}.xlsx')


def create_examples_zip(dir_name: Annotated[str, Doc("目录名称")], is_service: bool = True) -> str:
    """
    根据指定的目录名称,将该目录打包生成zip文件,并且返回压缩文件名称

    Args:
        dir_name: 打包的目录名
        is_service: 打包的目录是否是交互服务;填false则为CDA

    Returns:
        压缩文件名称

    """
    dir_path = f"temp/{'services' if is_service else 'cdas'}/{dir_name}"
    # 创建一个 Zip 文件
    zip_filepath = f'temp/archive-{'services' if is_service else 'cdas'}-{dir_name}.zip'

    with zipfile.ZipFile(zip_filepath, 'w') as zipf:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                # 将文件添加到 ZIP 文件中
                zipf.write(file_path, os.path.relpath(file_path, dir_path))

    # 删除原始文件夹
    shutil.rmtree(dir_path)

    return zip_filepath


def query_to_dict(cursor):
    """将查询结果转换为字典"""
    columns = [column[0] for column in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def generate_cda(dir_path: str, adm_no: str) -> None:
    """
    生成CDA文件

    Args:
        dir_path: 临时目录路径
        adm_no: 就诊流水号

    Returns:
        None
    """
    sql = ("select [no], PatientName patient_name, DocTypeCode doc_type_code, DocContent content "
           "from(SELECT row_number() over(partition by DocTypeCode order by CreateTime asc) no, [PatientName], DocTypeCode, [DocContent] "
           "from [CDADocument] where Visit_id = %s ) as T where T.[no] < %s")

    cda = CDATool(ip=os.getenv("ip", '172.16.33.179'), user=os.getenv('user', 'sa'),
                  password=os.getenv('password', 'Knt2020@lh'), dbname=os.getenv('dbname', 'CDADB'))

    cursor = cda.get_cursor()
    assert cursor is not None, '数据库连接失败'
    cursor.execute(sql, (adm_no, int(os.getenv('MAX_CDA_NUM', 20))))

    # 临时文件路径
    file_dir = f'temp/cdas/{dir_path}'

    for row in query_to_dict(cursor):

        if not os.path.exists(file_dir):
            os.makedirs(os.path.join(file_dir, row['patient_name']))

        tmp_file_name = f'EMR-SD-{row["doc_type_code"][-2:]}-{cda_map.get(row["doc_type_code"], "未知")}-{row["patient_name"]}-T01-{row["no"]:0>3}.xml'
        with open(file=os.path.join(file_dir, row["patient_name"], tmp_file_name), encoding='utf-8', mode='w',
                  newline='') as f:
            f.writelines(row["content"])

    # 执行对文件打包
    create_examples_zip(dir_path, False)


if __name__ == "__main__":
    pass
