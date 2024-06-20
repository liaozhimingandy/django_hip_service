from django.contrib.staticfiles import finders
from django.test import TestCase


# Create your tests here.
class SchemaTest(TestCase):
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

    def test_services(self):
        """ 批量校验服务是否符合指定格式 """
        import os
        sample_path = finders.find('hipmessageservice\services\samples\services')

        # 列出所有文件名称
        files = os.listdir(sample_path)

        for file in files:

            if os.path.isfile(os.path.join(sample_path, file)):
                base_name, extension = os.path.splitext(file)  # 拆分文件名和后缀名
                with open(os.path.join(sample_path, file), 'r', encoding="utf-8") as fp:
                    content = fp.read()

                response = self.client.post('/v3/openim/verify/service/',
                                            data={"service_code": base_name, "content": content}, follow=True)
                self.assertEqual(response.status_code, 200, response.content.decode())
                if response.status_code == 200:
                    print(f"{base_name} 校验通过")
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
                response = self.client.post('/v3/openim/verify/cda/',
                                            data={"cda_code": cda_code, "content": content}, follow=True)
                self.assertEqual(response.status_code, 200, response.content.decode())
                if response.status_code == 200:
                    print(f"{base_name} 校验通过")
            print(f'#############测试数量:{len(samples)}#############')