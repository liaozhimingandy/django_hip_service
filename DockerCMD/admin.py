import re
from collections import OrderedDict
from datetime import datetime

import yaml
from django.contrib import admin
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _

from django.http import HttpResponse
from django_json_widget.widgets import JSONEditorWidget

from DockerCMD.models import App, Service

# 自定义排序顺序
STANDARD_ORDER = [
    'version',
    'services',
    'networks',
    'volumes',
    'configs',
    'secrets'
]

SERVICE_FIELDS_ORDER = [
    'labels',
    'image',
    'build',
    'command',
    'container_name',
    'restart',
    'ports',
    'volumes',
    'environment',
    'networks',
    'depends_on',
    'healthcheck',
    'extra_hosts',
    'user'
]


# 自定义 Dumper 类来处理列表缩进
class MyDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow=False, indentless=False)


# 自定义一个方式避免 PyYAML 对 OrderedDict 输出类型标识
def ordered_dict_representer(dumper, data):
    return dumper.represent_dict(data.items())

# 提取数据卷名称，判断卷的格式
def extract_volume_name(volume):
    # 如果是类似 '卷名:/path/to/dir' 格式，提取卷名
    match = re.match(r'([a-zA-Z0-9-_]+):', volume)
    if match:
        return match.group(1)  # 提取卷名
    return None  # 如果是路径格式则返回 None

# 注册我们自定义的 representer
yaml.add_representer(OrderedDict, ordered_dict_representer)


# Register your models here.
@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ("app_name", "desc", "url", "comment")
    list_display_links = ("app_name",)

    search_fields = ('app_name', "desc")

    @admin.action(description="导出为docker-compose.yaml文件")
    def download_app_docker_compose(self, request, queryset):
        # 确保只选择了一项
        if queryset.count() != 1:
            self.message_user(request, "请选择且仅选择一项记录进行操作", level='error')
            return

        for app in queryset:
            services = Service.objects.filter(App_id=app.app_id)

            # 使用 OrderedDict 来确保字典顺序
            compose_data = OrderedDict({
                'version': '3.8',
                'services': OrderedDict(),
                'volumes': OrderedDict()
            })

            # 需要考虑的字段列表
            fields = SERVICE_FIELDS_ORDER
            # 遍历所有服务，生成对应的配置
            for service in services:
                # 使用字典推导动态过滤空字段
                service_config = OrderedDict({
                    field: getattr(service, field) for field in fields if getattr(service, field, None)
                })

                # 重新设置健康检查
                if service.healthcheck:
                    service_config["healthcheck"] = {
                        "test": service.healthcheck,
                        "interval": "10s",
                        "timeout": "3s",
                        "retries": 10
                    }

                # 设置labels
                labels = {
                    "com.alsoapp.description": service.desc,
                    "com.alsoapp.creator": "liaozhimingandy@qq.com",
                    "com.alsoapp.product": service.service_name_en,
                    "com.alsoapp.copyright": "©liaozhiming",
                    "com.alsoapp.license": "Apache-2.0"
                }

                # 添加一个新元素到第一个位置
                service_config.update({"labels": labels})
                service_config.move_to_end("labels", last=False)

                # 如果有有效的字段，则添加到 compose_data 中
                if service_config:
                    compose_data['services'][service.service_name_en] = service_config

                # 检查并处理 volumes 部分
                if 'volumes' in service_config:
                    for volume in service_config['volumes']:
                        volume_name = extract_volume_name(volume)  # 提取卷名
                        if volume_name:  # 如果提取到卷名，则将卷添加到 volumes 部分
                            compose_data['volumes'][volume_name] = {}

            # 手动调整字典结构，确保 version 字段始终在最前面
            sorted_compose_data = OrderedDict({
                'version': compose_data.get('version'),
                'services': compose_data.get('services'),
                'volumes': compose_data.get('volumes')
            })

            # 其他部分按顺序添加
            for key in STANDARD_ORDER:
                if key != 'version' and key != 'services' and key in compose_data:
                    sorted_compose_data[key] = compose_data[key]
            # 转成yaml格式的数据
            result = yaml.dump(sorted_compose_data, Dumper=MyDumper, default_flow_style=False, allow_unicode=True,
                               indent=2)
            # 添加注释到文件开头
            comment = "# 此文件由系统自动生成,请不要手工编辑 \n# 生成时间: {} \n\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"))
            # 将注释和 YAML 内容合并
            content = comment + result
            # 返回文件内容，作为下载
            response = HttpResponse(content, content_type="text/yaml")
            response['Content-Disposition'] = 'attachment; filename="docker-compose.yaml"'
            return response

    actions = ["download_app_docker_compose"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ("id", "App", "service_name_en", "desc", "image", "container_name", "comment")
    list_display_links = ("service_name_en",)
    list_filter = ("App",)
    search_fields = ("service_name_en", "comment", "image", "container_name")

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
