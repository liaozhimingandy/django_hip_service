import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


def id_default():
    return uuid.uuid4().hex[:7]


# Create your models here.
class BaseInfo(models.Model):
    """
    通用基础模型
    """
    creator = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, default=1,
                                verbose_name="创建人", db_comment="创建人",
                                related_name="%(app_label)s_%(class)s_related_creator",
                                related_query_name="%(app_label)s_%(class)ss",
                                db_constraint = settings.IS_DB_CONSTRAINT
                                )
    gmt_created = models.DateTimeField("创建时间", auto_now_add=True, db_comment="创建时间")
    is_deleted = models.BooleanField("删除标记", db_comment="删除标记", default=False)
    updater = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, default=1, verbose_name="修改者", db_comment="修改者",
                                related_name="%(app_label)s_%(class)s_related_updater",
                                related_query_name="%(app_label)s_%(class)ss", db_constraint=settings.IS_DB_CONSTRAINT)
    gmt_updated = models.DateTimeField("最后更新时间", auto_now=True, db_comment="最后更新时间")

    class Meta:
        abstract = True


class Firm(BaseInfo):
    """
    厂商信息
    """
    firm_id = models.CharField(max_length=7, verbose_name="厂商唯一标识", db_comment="唯一标识", default=id_default,
                               unique=True, editable=False)
    firm_name = models.CharField(verbose_name="厂商名称", max_length=64, db_comment="厂商名称", unique=True)
    firm_name_en = models.CharField(verbose_name="厂商英文名称", max_length=64, db_comment="厂商英文名称", blank=True, null=True)
    firm_name_short = models.CharField(verbose_name="厂商名称简称", max_length=64, db_comment="厂商名称简称", blank=True, null=True)
    api_url = models.URLField(verbose_name="api地址", db_comment="api地址", blank=True, null=True)

    def __str__(self):
        return self.firm_name

    class Meta:
        verbose_name = "厂商信息"
        verbose_name_plural = verbose_name


class Application(BaseInfo):
    """
    系统相关
    """
    application_id = models.CharField(max_length=7, verbose_name="系统唯一标识", db_comment="系统唯一标识",
                                      default=id_default, unique=True, editable=False)
    application_code = models.CharField(max_length=32, verbose_name="系统代码", db_comment="系统代码", blank=True, null=True)
    application_name = models.CharField(max_length=32, verbose_name="系统名称", db_comment="系统名称", unique=True)
    application_category = models.CharField(max_length=32, verbose_name="系统分类", db_comment="系统分类", blank=True, null=True)
    description = models.CharField(max_length=32, verbose_name="系统描述", db_comment="系统描述", blank=True, null=True)
    firm = models.ForeignKey(Firm, on_delete=models.PROTECT, null=True, blank=True, verbose_name="厂商名称",
                             db_comment="厂商名称", db_constraint=settings.IS_DB_CONSTRAINT)
    is_customer = models.BooleanField(default=True, verbose_name="是否为国家标准外", db_comment="是否为国家标准外", db_default=False)

    def __str__(self):
        return f"{self.application_name} - {self.application_id}"

    # 表信息声明
    class Meta:
        # 设置数据库中表名
        verbose_name = "系统名称"
        verbose_name_plural = verbose_name


class Service(BaseInfo):
    """服务信息"""

    service_id = models.UUIDField(verbose_name="服务id", db_comment="服务唯一标识", default=uuid.uuid4, unique=True)
    service_code = models.CharField(max_length=32, verbose_name="服务代码", db_comment="服务代码", unique=True)
    service_name = models.CharField(max_length=32, verbose_name="服务名称", db_comment="服务名称")
    service_category = models.CharField(max_length=32, verbose_name="服务分类", db_comment="服务分类", blank=True, null=True)
    service_description = models.CharField(max_length=128, verbose_name="服务描述", db_comment="服务描述", blank=True, null=True)
    service_queue = models.SmallIntegerField(verbose_name="序号", db_comment="序号", unique=True, default=1)
    service_status = models.BooleanField(db_default=False, verbose_name="服务完成状态", db_comment="服务状态")
    service_rank = models.CharField(max_length=8, verbose_name="服务等级", db_comment="服务等级", blank=True, null=True)
    is_v3 = models.BooleanField(db_default=False, verbose_name="是否是国家标准", db_comment="是否是国家标准")
    is_lookup = models.BooleanField(db_default=False, verbose_name="是否为查询类接口", db_comment="是否为查询类接口",
                                    blank=True, null=True, default=False)
    applications = models.ManyToManyField(Application, verbose_name="系统", related_name="系统", through="StatusShip")

    def __str__(self):
        return f"{self.service_name} - {self.service_code}"

    # 表信息声明
    class Meta:
        # 设置数据库中表名
        verbose_name = "服务"
        verbose_name_plural = verbose_name


class StatusShip(BaseInfo):
    """
    服务相关
    """
    class StatusChoice(models.IntegerChoices):
        RCV = (1, "订阅")
        SEND = (2, "发布")
        BOTH = (3, "全部")

    status = models.SmallIntegerField(choices=StatusChoice, default=StatusChoice.SEND, db_comment="发布订阅状态",
                                      verbose_name="发布订阅状态")
    application = models.ForeignKey(Application, verbose_name="系统", db_comment="系统", on_delete=models.PROTECT,
                                    db_constraint=settings.IS_DB_CONSTRAINT)
    service = models.ForeignKey(Service, verbose_name="服务", db_comment="服务", on_delete=models.PROTECT,
                                db_constraint=settings.IS_DB_CONSTRAINT)
    is_online = models.BooleanField(default=False, db_default=False, db_comment="上线状态", verbose_name="上线状态")

    def __str__(self):
        return f"{self.application.application_name} - {self.service.service_name} - {self.status}"

    class Meta:
        verbose_name = "发布订阅关系"
        verbose_name_plural = verbose_name
        unique_together = ("application", "service")


class CDA(BaseInfo):
    value = models.CharField(max_length=5, db_comment="文档代码", verbose_name="文档代码", unique=True)
    comment = models.CharField(max_length=20, db_comment="文档名称", verbose_name="文档名称")
    notes = models.TextField(verbose_name="备注说明", db_comment="备注说明", null=True, blank=True)
    firm = models.ManyToManyField(Firm, related_name="系统", verbose_name="系统", db_constraint=settings.IS_DB_CONSTRAINT)

    def __str__(self):
        return f"{self.comment} - {self.value}"

    class Meta:
        verbose_name = "CDA文档"
        verbose_name_plural = verbose_name


class Mock(BaseInfo):
    """
    数据模拟
    监控恺恩泰的消息追踪接收响应表,然后根据此映射表用于生成互联互通测评接收方的数据
    """
    send = models.ForeignKey(Application, on_delete=models.PROTECT, db_comment="发送方", verbose_name="发送方",
                             db_constraint=settings.IS_DB_CONSTRAINT, related_name="mock_send",
                             to_field="application_id")
    service = models.ForeignKey(Service, on_delete=models.PROTECT, db_comment="服务名称", verbose_name="服务名称",
                                db_constraint=settings.IS_DB_CONSTRAINT, to_field="service_code")
    receive = models.ForeignKey(Application, on_delete=models.PROTECT, db_comment="发送方", verbose_name="发送方",
                                db_constraint=settings.IS_DB_CONSTRAINT, related_name="mock_receive",
                                to_field="application_id")

    class Meta:
        verbose_name = "Mock"
        verbose_name_plural = verbose_name
        constraints = [
            models.UniqueConstraint(fields=("send", "service", "receive"), name="send_service_receive_unique"),
        ]

    def __str__(self):
        return f"{self.send.application_name} - {self.service.service_name} - {self.receive.application_name}"


