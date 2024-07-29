import base64
import datetime
import uuid
from zoneinfo import ZoneInfo

from django.contrib.staticfiles import finders
from django.test import TestCase

from hipmessageservice.api import verification_hip_detail


# 统一请求消息格式
message = {
    "client_msg_id": str(uuid.uuid4()),
    "server_msg_id": "",
    "gmt_create": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),
    "gmt_send": datetime.datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(timespec='seconds'),
    "send_id": "esbid_15ef316",
    "recv_id": "esbid_15ef316",
    "group_id": "",
    "content_type": "ExamResultAdd"
}


# Create your tests here.
class SchemaTest(TestCase):
    """ 标准交互服务和CDA测试 """
    CDA_MAPPING = {
        '病历概要': 'C0001',
        '门急诊病历': 'C0002',
        '急诊留观病历': 'C0003',
        '西药处方': 'C0004',
        '中药处方': 'C0005',
        '检查报告': 'C0006',
        '检验报告': 'C0007',
        '治疗记录': 'C0008',
        '一般手术记录': 'C0009',
        '麻醉术前访视记录': 'C0010',
        '麻醉记录': 'C0011',
        '麻醉术后访视记录': 'C0012',
        '输血记录': 'C0013',
        '待产记录': 'C0014',
        '阴道分娩记录': 'C0015',
        '剖宫产记录': 'C0016',
        '一般护理记录': 'C0017',
        '病重病危护理记录': 'C0018',
        '手术护理记录': 'C0019',
        '生命体征测量记录': 'C0020',
        '出入量记录': 'C0021',
        '高值耗材使用记录': 'C0022',
        '入院评估': 'C0023',
        '护理计划': 'C0024',
        '出院评估与指导': 'C0025',
        '手术知情同意书': 'C0026',
        '麻醉知情同意书': 'C0027',
        '输血治疗同意书': 'C0028',
        '特殊检查及特殊治疗同意书': 'C0029',
        '病危重通知书': 'C0030',
        '其他知情告知同意书': 'C0031',
        '住院病案首页': 'C0032',
        '中医住院病案首页': 'C0033',
        '入院记录': 'C0034',
        '24小时内入出院记录': 'C0035',
        '24小时内入院死亡记录': 'C0036',
        '首次病程记录': 'C0037',
        '日常病程记录': 'C0038',
        '上级医师查房记录': 'C0039',
        '疑难病例讨论记录': 'C0040',
        '交接班记录': 'C0041',
        '转科记录': 'C0042',
        '阶段小结': 'C0043',
        '抢救记录': 'C0044',
        '会诊记录': 'C0045',
        '术前小结': 'C0046',
        '术前讨论': 'C0047',
        '术后首次病程记录': 'C0048',
        '出院记录': 'C0049',
        '死亡记录': 'C0050',
        '死亡病例讨论记录': 'C0051',
        '住院医嘱': 'C0052',
        '出院小结': 'C0053'
    }

    def test_hip_services(self):
        """ 批量校验服务是否符合指定格式 """
        import os
        sample_path = finders.find('hipmessageservice\services\samples\services')

        # 列出所有文件名称
        files = os.listdir(sample_path)
        files.sort()

        for file in files:

            if os.path.isfile(os.path.join(sample_path, file)):
                base_name, extension = os.path.splitext(file)  # 拆分文件名和后缀名

                # 排除需要调外部接口的服务
                if base_name in ('PatientInfoRegister', 'PatientInfoUpdate'):
                    continue
                print(f"#############{base_name} 正在测试 #############")
                with open(os.path.join(sample_path, file), 'r', encoding="utf-8") as fp:
                    content = fp.read()
                message['content_type'] = base_name
                message[base_name] = base64.b64encode(content.encode("UTF-8")).decode('UTF-8')
                response = self.client.post('/v3/openim/service/verify/',
                                            data=message, follow=True, content_type='application/json')

                self.assertEqual(response.status_code, 200, response.content.decode())

                if response.status_code == 200:
                    print(f"#############{base_name} 测试通过 #############")
        print(f'#############测试数量:{len(files)}#############')

    def test_cdas(self):
        """
        批量测试CDA文档是否服务schema文件定义
        :return:
        """
        import os
        sample_path = finders.find('hipmessageservice\services\samples\cdas')

        # 列出所有文件名称
        samples = os.listdir(sample_path)
        for sample in samples:
            if os.path.isfile(os.path.join(sample_path, sample)):
                base_name, extension = os.path.splitext(sample)  # 拆分文件名和后缀名
                cda_code = self.CDA_MAPPING[base_name.split('：')[1].replace('住院病程记录 ', '')]
                with open(os.path.join(sample_path, sample), 'r', encoding="utf-8") as fp:
                    content = fp.read()

                ok, message = verification_hip_detail(schema_name=cda_code, content=content, is_service=False)
                print(ok, message)
                if ok:
                    print(f"#############{base_name} 测试通过 #############")
                else:
                    print(f'#############{base_name} 测试失败 #############')
                self.assertTrue(ok, ','.join(message))

        print(f'#############测试数量:{len(samples)}#############')


class getExamReportPrintInfosTest(TestCase):
    """ 获取检验报告打印信息测试用例 """
    def setUp(self):
        """ 创建数据用于测试 """
        # 报告数据
        report = """{
               "client_msg_id": "5F61FbB4-CcAF-D34e-F3Ca-beDFf10FeBAf",
               "server_msg_id": "15dFee40-e324-Df16-2Ac7-bc794A82CD93",
               "gmt_create": "2024-07-26T11:49:17+08:00",
               "gmt_send": "2024-07-26T11:49:17+08:00",
               "send_id": "e16d87d8-160F-8b3f-D142-beB308a21D67",
               "recv_id": "2Cbc818f-CAEA-8832-6517-1bc3C4c27d8F",
               "group_id": "BE6EeDEF-C1fB-b5B5-2B48-E1EaE54975f4",
               "content_type": "ExamReportAdd",
               "ExamReportAdd": {
                   "report_id": "610000199206237666",
                   "title": "院水本局传离",
                   "bar_code": "-1811415269102608",
                   "specimen_id": "95",
                   "specimen_name": "动管信酸",
                   "specimen_cls_code": "1",
                   "specimen_cls_name": "血清",
                   "exam_cls_code": 2,
                   "dept_id": "650000199008034478",
                   "dept_name": "单大管积",
                   "patient": {
                       "empi_id": "6189753550896830",
                       "patient_id": "2999834436969188",
                       "outpatient_id": "209542861720304",
                       "inpatient_id": "2437240487466918",
                       "id_no": "82052718610110834X",
                       "patient_name": "朱刚",
                       "sex_code": 2,
                       "gmt_birth": "2003-07-31T17:37:15.0Z",
                       "hrecord_no": "1341408090534334",
                       "sin_no": "94743718110716671x"
                   },
                   "adm_no": "4437756567079436",
                   "adm_code": 2,
                   "content": "特行酸片社又命型任交求些布江毛。反被党信王市治电金做今证求音我。南他运除七须能时管发品飞族且年。老件花重直验六相间点今点话平风。老此类办约则片始亲清由转那农。西常根石道什教题空两眼断并理。",
                   "comment": "国号照维资并里住入压一到值实布应提起。且几速使门族工易资调能切长。什节公张养院权和龙白表后温。约农计然格于设也立义系调号革带力完来。况见制增影圆社例第革力较。",
                   "url_report_pdf": "http://fthclenrof.ao/qpsjsphcd",
                   "details": [
                       {
                           "apply_id": "4758097835143175",
                           "order_id": "5674467411157838",
                           "doc_id": "420000197008131129",
                           "doc_name": "彭秀兰",
                           "dept_id": "A0001",
                           "dept_name": "产科",
                           "item_code": "89",
                           "item_name": "产规上学观",
                           "item_cls_code": "96",
                           "item_cls_name": "属代斯收团片",
                           "test_items": [
                               {
                                   "index": 22,
                                   "item_code": "76",
                                   "item_name": "白里员消",
                                   "abbr": "do culpa est",
                                   "value": "laborum voluptate",
                                   "unit": "ng/mL",
                                   "comment": "↑",
                                   "remarks": "irure sint ad tempor sed",
                                   "upper_limit_value": "20",
                                   "lower_limit_value": "10",
                                   "limit_desc": "ullamco",
                                   "abnormal_flag_code": "37",
                                   "abnormal_flag_name": "放深争真",
                                   "is_warn": false,
                                   "test_method_code": "9",
                                   "test_method_name": "改十人件带名精",
                                   "is_germ": false,
                                   "bacterium_id": "68",
                                   "bacterium_code": "50",
                                   "bacterium_name": "子世书气工",
                                   "bacterium_abbr": "culpa non velit",
                                   "bacterium_type_code": "17",
                                   "bacterium_type_name": "和子名达题",
                                   "extend_code": "12",
                                   "extend_name": "龙织百响头那状",
                                   "ast_items": [
                                       {
                                           "index": 32,
                                           "ast_code": "68",
                                           "ast_name": "值局细适指易",
                                           "ast_abbr": "minim nulla cupidatat proident culpa",
                                           "value_qualitative": "adipisicing qui consequat magna",
                                           "value_qualitative_desc": "dolore proident in aliquip",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       },
                                       {
                                           "index": 16,
                                           "ast_code": "67",
                                           "ast_name": "深党起龙叫",
                                           "ast_abbr": "minim voluptate pariatur Duis",
                                           "value_qualitative": "Excepteur occaecat pariatur deserunt proident",
                                           "value_qualitative_desc": "Duis dolore",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       },
                                       {
                                           "index": 30,
                                           "ast_code": "7",
                                           "ast_name": "度建力",
                                           "ast_abbr": "sunt officia qui",
                                           "value_qualitative": "dolore ut fugiat elit",
                                           "value_qualitative_desc": "consequat",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       }
                                   ]
                               },
                               {
                                   "index": 79,
                                   "item_code": "67",
                                   "item_name": "类成及维容己领",
                                   "abbr": "enim ex consequat commodo nostrud",
                                   "value": "et cillum Ut aliqua",
                                   "unit": "ng/mL",
                                   "comment": "↑",
                                   "remarks": "anim magna in",
                                   "upper_limit_value": "20",
                                   "lower_limit_value": "10",
                                   "limit_desc": "id tempor",
                                   "abnormal_flag_code": "97",
                                   "abnormal_flag_name": "习本见当层",
                                   "is_warn": false,
                                   "test_method_code": "55",
                                   "test_method_name": "红除经持",
                                   "is_germ": false,
                                   "bacterium_id": "47",
                                   "bacterium_code": "69",
                                   "bacterium_name": "打部机间内",
                                   "bacterium_abbr": "aliqua ut eiusmod sunt",
                                   "bacterium_type_code": "73",
                                   "bacterium_type_name": "造年价观铁",
                                   "extend_code": "50",
                                   "extend_name": "查严百选派队",
                                   "ast_items": [
                                       {
                                           "index": 74,
                                           "ast_code": "55",
                                           "ast_name": "术正和提证",
                                           "ast_abbr": "laboris ad deserunt",
                                           "value_qualitative": "eu non",
                                           "value_qualitative_desc": "quis",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       },
                                       {
                                           "index": 29,
                                           "ast_code": "61",
                                           "ast_name": "龙才六调",
                                           "ast_abbr": "anim eiusmod cupidatat aliquip",
                                           "value_qualitative": "labore Ut aliqua ea",
                                           "value_qualitative_desc": "et minim",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       }
                                   ]
                               },
                               {
                                   "index": 45,
                                   "item_code": "46",
                                   "item_name": "往到质理么明",
                                   "abbr": "nulla consequat enim minim eu",
                                   "value": "laborum amet in laboris",
                                   "unit": "ng/mL",
                                   "comment": "↑",
                                   "remarks": "eiusmod ipsum pariatur",
                                   "upper_limit_value": "20",
                                   "lower_limit_value": "10",
                                   "limit_desc": "eiusmod",
                                   "abnormal_flag_code": "1",
                                   "abnormal_flag_name": "已何把么",
                                   "is_warn": false,
                                   "test_method_code": "36",
                                   "test_method_name": "采期入术先容断",
                                   "is_germ": false,
                                   "bacterium_id": "23",
                                   "bacterium_code": "87",
                                   "bacterium_name": "易细长品至派听",
                                   "bacterium_abbr": "est exercitation do dolor",
                                   "bacterium_type_code": "34",
                                   "bacterium_type_name": "管京场例",
                                   "extend_code": "88",
                                   "extend_name": "体系后气务组高",
                                   "ast_items": [
                                       {
                                           "index": 20,
                                           "ast_code": "22",
                                           "ast_name": "引应东",
                                           "ast_abbr": "tempor dolore",
                                           "value_qualitative": "in non irure sed in",
                                           "value_qualitative_desc": "pariatur occaecat deserunt",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       },
                                       {
                                           "index": 22,
                                           "ast_code": "10",
                                           "ast_name": "图机日划",
                                           "ast_abbr": "aliqua et sunt",
                                           "value_qualitative": "Lorem elit Ut",
                                           "value_qualitative_desc": "Duis",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       },
                                       {
                                           "index": 95,
                                           "ast_code": "36",
                                           "ast_name": "决并花律",
                                           "ast_abbr": "eu",
                                           "value_qualitative": "reprehenderit et",
                                           "value_qualitative_desc": "minim culpa",
                                           "value_qualitative_disk": "/",
                                           "value_ration": "/",
                                           "mic": "10μL"
                                       }
                                   ]
                               }
                           ]
                       }
                   ],
                   "device_id": "510000201609012548",
                   "device_name": "意",
                   "gmt_collect": "2024-07-26T11:49:17+08:00",
                   "gmt_receive": "2024-07-26T11:49:17+08:00",
                   "executor_id": "350000200803046923",
                   "executor": "刘磊",
                   "gmt_execute": "2024-07-26T11:49:17+08:00",
                   "author_id": "340000199708300674",
                   "author": "萧霞",
                   "gmt_author": "2024-07-26T11:49:17+08:00",
                   "reviewer_id": "120000200603042108",
                   "reviewer": "顾磊",
                   "gmt_review": "2024-07-26T11:49:17+08:00",
                   "from_src": "DD37eFD3-0fbf-AdC1-24b3-8FB4dC290c4A",
                   "org_code": "12360000491015900T",
                   "org_name": "南昌大学附属口腔医院（江西省口腔医院）"
               }
           }
           """

        # 调接口写入报告信息
        response = self.client.post('/v3/openim/service/verify/',
                                    data=report, follow=True, content_type='application/json')
        self.assertEqual(response.status_code, 200, response.content.decode())

    def test_forward_getExamReportPrintInfos(self):
        """测试获取检验报告打印信息"""
        message['content_type'] = 'getExamReportPrintInfos'
        message['getExamReportPrintInfos'] = {
            "patient_id": "2999834436969188",
            "org_code": "12360000491015900T"
          }

        # 获取报告打印链接
        response = self.client.post('/v3/openim/service/verify/', data=message, follow=True, content_type='application/json')
        self.assertEqual(response.status_code, 200, response.content.decode())
        if response.status_code == 200:
            print(f"内容为: {response.content}")

    def test_reverse_getExamReportPrintInfos(self):
        """ 测试反向关系 """
        message['content_type'] = 'getExamReportPrintInfos'
        message['getExamReportPrintInfos'] = {
            "patient_id": "88888888",
            "org_code": "12360000491015900T"
        }

        # 获取报告打印链接
        response = self.client.post('/v3/openim/service/verify/', data=message, follow=True,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400, response.content.decode())
        if response.status_code == 400:
            print(f"内容为: {response.content}")