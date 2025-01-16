import uuid

from django.db import models

# Create your models here.
class App(models.Model):
    """
    应用信息
    """
    app_id = models.UUIDField("应用唯一ID", db_comment="应用唯一ID", default=uuid.uuid4, unique=True)
    app_name = models.CharField("应用名称", db_comment="应用名称", max_length=64, unique=True)
    desc = models.CharField("应用描述", db_comment="应用描述", max_length=128, blank=True, null=True)
    url = models.URLField("访问地址", db_comment="访问地址", blank=True, null=True)
    comment = models.CharField("备注信息", db_comment="备注信息", max_length=128, blank=True, null=True)
    gmt_created = models.DateTimeField("创建时间", db_comment="创建时间", auto_now=True)

    def __str__(self):
        return self.app_name

    class Meta:
        verbose_name = "应用信息"
        verbose_name_plural = verbose_name
        db_table_comment = '应用信息'


class Service(models.Model):
    """
    app下的服务应用
    """

    class ReStartChoices(models.TextChoices):
        A = ("no", "在任何情况下都不会重启容器")
        B = ("always", "容器总是重新启动")
        C = ("on-failure", "如果退出代码指示失败错误，则重新启动容器")
        D = ("unless-stopped", "总是重新启动容器，除非手动容器停止")


    service_id = models.UUIDField("服务唯一ID", db_comment="服务唯一ID", default=uuid.uuid4, unique=True)
    service_name_en = models.CharField("服务名", db_comment="服务名", help_text="英文名,示例: db, web", default="app",
                                       max_length=64,)
    desc = models.CharField("服务描述", db_comment="服务描述", max_length=128, blank=True, null=True)
    url = models.URLField("访问地址", db_comment="访问地址", blank=True, null=True)
    comment = models.CharField("备注信息", db_comment="备注信息", max_length=128, blank=True, null=True)
    # labels = models.TextField("标签信息", db_comment="标签信息", ); 系统内置
    image = models.CharField("镜像名称", db_comment="镜像名称", max_length=64)
    container_name = models.CharField("容器名称", max_length=64, db_comment="容器名称", null=True, blank=True)
    restart = models.CharField("重启策略", db_comment="重启策略", max_length=64, choices=ReStartChoices,
                               default="unless-stopped")
    ports = models.JSONField("映射端口", db_comment="映射端口", blank=True, null=True,
                              help_text="示例: ['8080:8080', '8443:8443']")
    volumes = models.JSONField("数据卷信息", db_comment="数据卷信息", blank=True, null=True)
    hostname = models.CharField("容器内主机名称", db_comment="容器内主机名称", max_length=64, blank=True, null=True)
    dns = models.JSONField("DNS服务器", db_comment="DNS服务器", blank=True, null=True,
                           help_text="添加项目实际DNS服务地址")
    extra_hosts = models.JSONField("容器内hosts文件", db_comment="容器内hosts文件", blank=True, null=True)
    environment = models.JSONField("环境变量", db_comment="环境变量", blank=True, null=True,
                                   help_text="示例: TZ=Asia/Shanghai")
    healthcheck = models.JSONField("健康检查命令", db_comment="健康检查命令", max_length=64, blank=True, null=True,
                                   help_text='示例: ["CMD-SHELL", "curl -sS localhost:8444/api/info || exit 1"]')
    user = models.CharField("运行用户", db_comment="运行用户", max_length=64, blank=True, null=True, help_text="示例: root")
    command = models.CharField("启动命令", db_comment="启动命令", max_length=64, blank=True, null=True,
                               help_text="示例: ['/bin/bash', '-c', 'echo hello']")
    App = models.ForeignKey(App, on_delete=models.CASCADE, db_constraint=True, to_field="app_id")
    gmt_created = models.DateTimeField("创建时间", db_comment="创建时间", auto_now=True)

    def __str__(self):
        return self.service_name_en

    class Meta:
        verbose_name = "服务信息"
        verbose_name_plural = verbose_name
        db_table_comment = '服务信息'



