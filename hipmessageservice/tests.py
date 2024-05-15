from django.contrib.staticfiles import finders
from django.test import TestCase


# Create your tests here.
class SchemaTest(TestCase):

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
                print(f'正在测试...{base_name}')
                response = self.client.post('/services/verify/service/',
                                            data={"service_code": base_name, "content": content}, follow=True)

                self.assertEqual(response.status_code, 200, response.content.decode())
                if response.status_code == 200:
                    print(f"{base_name} 校验通过")
        print(f'#############测试数量:{len(files)}#############')


