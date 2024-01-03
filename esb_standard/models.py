from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseInfo(models.Model):
    """
    通用基础模型
    """
    creator = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, default=1, verbose_name="创建人", db_comment="创建人",
                                related_name="%(app_label)s_%(class)s_related_creator",
                                related_query_name="%(app_label)s_%(class)ss")
    gmt_created = models.DateTimeField("创建时间", auto_now_add=True, db_comment="创建时间")
    is_deleted = models.BooleanField("删除标记", db_comment="删除标记", default=False)
    updater = models.ForeignKey(User, on_delete=models.PROTECT, editable=False, default=1, verbose_name="修改者", db_comment="修改者",
                                related_name="%(app_label)s_%(class)s_related_updater",
                                related_query_name="%(app_label)s_%(class)ss")
    gmt_updated = models.DateTimeField("最后更新时间", auto_now=True, db_comment="最后更新时间")

    class Meta:
        abstract = True


class DictMain(BaseInfo):
    value = models.CharField("值", max_length=64, db_comment="值")
    comment = models.CharField("值含义", max_length=128, db_comment="值含义")

    def __str__(self):
        return f"{self.comment}({self.value})"

    class Meta:
        verbose_name = "字典主表"
        verbose_name_plural = verbose_name


class Dict(BaseInfo):
    """
    标准字典
    """
    value = models.CharField("值", max_length=64, db_comment="值")
    comment = models.CharField("值含义", max_length=128, db_comment="值含义")
    value_dict = models.ForeignKey(DictMain, on_delete=models.PROTECT, null=True, verbose_name="所属字典",
                                   db_comment="所属字典", related_name="value_dict")

    def __str__(self):
        return f"{self.comment}({self.value})"

    class Meta:
        verbose_name = "字典表"
        verbose_name_plural = verbose_name


class DataSet(BaseInfo):
    value = models.CharField("数据集英文名称", max_length=64, db_comment="数据集英文名称")
    comment = models.CharField("数据集中文名称", max_length=128, db_comment="数据集中文名称")

    class Meta:
        verbose_name = "数据集主表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.comment}-{self.value}"


class DataElement(BaseInfo):
    """
    数据元基本信息
    """

    # 数据类型
    data_type_choice = (
        ("BY", "二进制"),
        ("T", "时间型"),
        ("DT", "日期时间型"),
        ("D", "日期型"),
        ("N", "数值型"),
        ("L", "布尔型"),
        ("S1", "字符型-值域代码表"),
        ("S2", "字符型-值域范围"),
        ("S3", "字符型"),
    )

    hd_code = models.CharField("内部数据元标识符", max_length=11, db_comment="内部数据元标识符")
    de_code = models.CharField("标准数据元标识符", max_length=14, db_comment="标准数据元标识符", null=True, blank=True)
    de_en_code = models.CharField("数据元英文名", max_length=32, db_comment="数据元英文名")
    de_name = models.CharField("数据元名称", max_length=32, db_comment="数据元名称")
    definition = models.CharField("定义", max_length=128, null=True, blank=True, db_comment="定义")
    data_type = models.CharField("数据元值的数据类型", max_length=2, choices=data_type_choice, db_comment="数据元值的数据类型")
    expression = models.CharField("表示格式", max_length=8, null=True, blank=True, db_comment="表示格式")
    allowable_value = models.CharField("数据元允许值", max_length=32, null=True, blank=True, db_comment="数据元允许值")
    length = models.PositiveSmallIntegerField("长度", null=True, blank=True, db_comment="长度")
    value = models.CharField("默认值",  max_length=64, blank=True, null='', db_comment="默认值")
    data_set = models.ForeignKey(DataSet, on_delete=models.PROTECT, null=True, verbose_name="所属数据集",
                                 db_comment="所属数据集")

    def __str__(self):
        return f"{self.de_name}({self.de_en_code})"

    class Meta:
        verbose_name = "数据集表"
        verbose_name_plural = verbose_name


class Service(BaseInfo):
    """
    服务信息
    """
    service_code = models.CharField("事件代码",  max_length=6, db_comment="事件代码", help_text="事件代码")
    service_name = models.CharField("事件名称", max_length=32, db_comment="事件名称", help_text="事件名称")

    def __str__(self):
        return f'{self.service_name}-{self.service_code}'

    class Meta:
        verbose_name = "消息事件"
        verbose_name_plural = verbose_name


class MessageFormat(BaseInfo):
    """
    消息格式,用于后续自动生成并导出消息样例,
    关联模型: 用户相关:`auth.User` 和 服务相关: `esb_standard.Service`
    """
    service = models.ForeignKey(Service, on_delete=models.PROTECT, verbose_name="事件", db_comment="对应事件",
                                help_text="对应事件")
    format = models.JSONField("消息格式",  db_comment="消息格式", help_text="消息格式")

    def __str__(self):
        return f'{self.service}'

    class Meta:
        verbose_name = "消息格式"
        verbose_name_plural = verbose_name
