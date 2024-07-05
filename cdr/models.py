from django.core.exceptions import ValidationError
from django.db import models


class AdmCodeChoices(models.IntegerChoices):
    """
    急诊类别代码
    """
    A = (1, '门诊')
    B = (2, '急诊')
    C = (3, '住院')
    D = (4, '体检')
    E = (9, '其他')


class SexCodeChoices(models.IntegerChoices):
    """
    性别代码
    """
    A = (0, '未知的性别')
    B = (1, '男性')
    C = (2, '女性')
    D = (9, '未说明的性别')


class PropertyChoices(models.TextChoices):
    """ 优先（紧急）度代码 """
    A = ('N', 'normal')
    B = ('U', 'urgent')
    C = ('C', 'critical')
    D = ('E', 'endangered')


class FromOrgCodeChoices(models.TextChoices):
    """ 来源机构 """
    A = ('12360000491015900T', '南昌大学附属口腔医院（江西省口腔医院）')


# Create your models here.
class BloodTransAppInfo(models.Model):
    class ABOChoices(models.IntegerChoices):
        A = (1, 'A型')
        B = (2, 'B型')
        C = (3, 'O型')
        D = (4, 'AB型')
        E = (5, '不详')

    class RHChoices(models.IntegerChoices):
        A = (1, '阴性')
        B = (2, '阳性')
        C = (3, '不详')
        D = (4, '未查')

    apply_no = models.CharField(max_length=36, blank=True, null=True, db_comment='申请单号', unique=True,
                                verbose_name='申请单号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单详细信息',
                                  verbose_name='申请单详细信息')
    gmt_apply = models.DateTimeField(blank=True, null=True, db_comment='申请日期时间', verbose_name='申请日期时间')
    property = models.CharField(max_length=1, choices=PropertyChoices, default='N', db_comment='优先（紧急）度代码',
                                verbose_name='优先（紧急）度代码')
    gmt_order = models.DateTimeField(blank=True, null=True, db_comment='开单时间', verbose_name='开单时间')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='开单医生工号',
                              verbose_name='开单医生工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='开单医生姓名',
                                verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请科室编码',
                               verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请科室名称',
                                 verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='审核日期时间', verbose_name='审核日期时间')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='审核者工号',
                                   verbose_name='审核者工号')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='审核者姓名',
                                verbose_name='审核者姓名')
    abo_code = models.PositiveSmallIntegerField(choices=ABOChoices, db_comment='患者ABO血型代码',
                                                verbose_name='患者ABO血型代码')
    rh_code = models.PositiveSmallIntegerField(choices=RHChoices, db_comment='患者RH血型代码',
                                               verbose_name='患者RH血型代码')
    height = models.CharField(max_length=8, blank=True, null=True, db_comment='患者身高', verbose_name='患者身高')
    weight = models.CharField(max_length=8, blank=True, null=True, db_comment='患者体重', verbose_name='患者体重')
    diastolic_pressure = models.CharField(max_length=8, blank=True, null=True, db_comment='患者舒张压',
                                          verbose_name='患者舒张压')
    temperature = models.CharField(max_length=8, blank=True, null=True, db_comment='患者体温', verbose_name='患者体温')
    pulse = models.CharField(max_length=8, blank=True, null=True, db_comment='患者脉搏', verbose_name='患者脉搏')
    abo_code_apply = models.PositiveSmallIntegerField(choices=ABOChoices, db_comment='申请ABO血型代码',
                                                      verbose_name='申请ABO血型代码')
    rh_code_apply = models.PositiveSmallIntegerField(choices=RHChoices, db_comment='申请RH血型代码',
                                                     verbose_name='申请RH血型代码')
    is_collect = models.BooleanField(default=False, db_comment='采血标记', verbose_name='采血标记')
    location = models.CharField(max_length=255, blank=True, null=True, db_comment='输血地点', verbose_name='输血地点')
    purpose = models.CharField(max_length=255, blank=True, null=True, db_comment='输血目的', verbose_name='输血目的')
    nature = models.CharField(max_length=255, blank=True, null=True, db_comment='输血性质', verbose_name='输血性质')
    is_urgent = models.BooleanField(default=False, db_comment='输血紧急标志', verbose_name='输血紧急标志')
    medical = models.CharField(max_length=255, blank=True, null=True, db_comment='病史信息', verbose_name='病史信息')
    transfusion = models.CharField(max_length=255, blank=True, null=True, db_comment='输血史', verbose_name='输血史')
    reaction = models.CharField(max_length=255, blank=True, null=True, db_comment='输血反应史',
                                verbose_name='输血反应史')
    allergy = models.CharField(max_length=255, blank=True, null=True, db_comment='药物过敏史',
                               verbose_name='药物过敏史')
    gravidity = models.PositiveSmallIntegerField(default=0, db_comment='孕次', verbose_name='孕次')
    delivery = models.PositiveSmallIntegerField(default=0, db_comment='产次', verbose_name='产次')
    other = models.CharField(max_length=255, blank=True, null=True, db_comment='其他重要病史',
                             verbose_name='其他重要病史')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='备注', verbose_name='备注')
    blood_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='血量单位', verbose_name='血量单位')
    blood = models.CharField(max_length=8, blank=True, null=True, db_comment='血量', verbose_name='血量')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "输血申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '输血申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class CheckAppInfo(models.Model):
    apply_no = models.CharField(max_length=36, db_comment='检查申请单编号', unique=True, verbose_name='检查申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单详细内容',
                                  verbose_name='申请单详细内容')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='检查申请有效日期时间开始',
                                          verbose_name='检查申请有效日期时间开始')
    gmt_effect_high = models.DateTimeField(blank=True, null=True, db_comment='检查申请有效日期时间结束',
                                           verbose_name='检查申请有效日期时间结束')
    property = models.CharField(max_length=1, choices=PropertyChoices, default='N', db_comment='优先（紧急）度代码',
                                verbose_name='优先（紧急）度代码')
    gmt_apply = models.DateTimeField(blank=True, null=True, db_comment='开单时间', verbose_name='开单时间')
    doc_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单开立者签名',
                                verbose_name='申请单开立者签名')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='开单医生编码',
                              verbose_name='开单医生编码')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='开单医生姓名',
                                verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请科室编码',
                               verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请科室名称',
                                 verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='审核日期时间', verbose_name='审核日期时间')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='审核者编码',
                                   verbose_name='审核者编码')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='审核者姓名',
                                verbose_name='审核者姓名')
    order_id = models.CharField(max_length=36, db_comment='医嘱ID', unique=True, verbose_name='医嘱ID')
    item_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查项目编码',
                                 verbose_name='检查项目编码')
    item_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查项目名称',
                                 verbose_name='检查项目名称')
    method_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查方法编码',
                                   verbose_name='检查方法编码')
    method_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查方法名称',
                                   verbose_name='检查方法名称')
    class_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查类型编码',
                                  verbose_name='检查类型编码')
    class_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查类型名称',
                                  verbose_name='检查类型名称')
    site_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查部位编码',
                                 verbose_name='检查部位编码')
    site_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查部位名称',
                                 verbose_name='检查部位名称')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='执行时间', verbose_name='执行时间')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='申请注意事项',
                            verbose_name='申请注意事项')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    diags = models.JSONField(blank=True, null=True, db_comment='诊断信息', verbose_name='诊断信息',
                             help_text='诊断(检查申请原因)')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "检查申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检查申请信息'

        indexes = [
            models.Index(fields=('order_id',)),
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class CheckAppointStatusInfo(models.Model):
    schedule_id = models.CharField(max_length=36, db_comment='预约单流水号', unique=True, verbose_name='预约单流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_booking = models.DateTimeField(blank=True, null=True, db_comment='预约检查时间', verbose_name='预约检查时间')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    index = models.PositiveSmallIntegerField(db_comment='预约排序号', verbose_name='预约排序号')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='病人科室ID', verbose_name='病人科室ID')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='病人科室名称',
                                 verbose_name='病人科室名称')
    device_id = models.CharField(max_length=36, blank=True, null=True, db_comment='预约设备编码(ID)',
                                 verbose_name='预约设备编码')
    device_name = models.CharField(max_length=64, blank=True, null=True, db_comment='预约设备名称',
                                   verbose_name='预约设备名称')
    booking_id = models.CharField(max_length=36, blank=True, null=True, db_comment='预约员工号',
                                  verbose_name='预约员工号')
    bookinger = models.CharField(max_length=64, blank=True, null=True, db_comment='预约员姓名',
                                 verbose_name='预约员姓名')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码(ID) ',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    apply_no = models.CharField(max_length=36, db_comment='检查申请单编号', verbose_name='检查申请单编号')
    order_id = models.CharField(max_length=36, db_comment='医嘱ID', verbose_name='医嘱ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "检查预约状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检查预约状态信息'

        indexes = [
            models.Index(fields=('order_id',)),
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class CheckReport(models.Model):
    """
    检查报告
    """

    class ExamCategoryChoices(models.TextChoices):
        A = ('ECG', '心电检查')
        B = ('UIS', '超声检查')
        C = ('PIS', '病理检查')
        D = ('RIS', '放射检查')
        E = ('EIS', '内镜检查')

    report_id = models.CharField(help_text="报告ID", max_length=36, db_comment="报告ID", unique=True,
                                 verbose_name='报告ID')
    title = models.CharField(max_length=36, db_comment="报告单名称", verbose_name='报告单名称', help_text='报告单名称')
    exam_no = models.CharField(max_length=36, db_comment="检查号", verbose_name='检查号', help_text='检查号')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')

    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码')
    apply_id = models.CharField(max_length=36, db_comment="申请单id", verbose_name='申请单id', help_text='申请单id')
    gmt_apply = models.DateTimeField(db_comment="申请时间", verbose_name='申请时间', help_text='申请时间')
    apply_dept_code = models.CharField(max_length=36, db_comment="申请科室代码", verbose_name='申请科室代码',
                                       help_text='申请科室代码')
    apply_dept_name = models.CharField(max_length=64, db_comment="申请科室名称", verbose_name='申请科室名称',
                                       help_text='申请科室名称')
    apply_doc_id = models.CharField(max_length=36, db_comment="开单医生id", verbose_name='开单医生id',
                                    help_text='开单医生id')
    apply_doc = models.CharField(max_length=64, db_comment="开单医生姓名", verbose_name='开单医生姓名',
                                 help_text='开单医生姓名')
    item_code = models.CharField(max_length=36, db_comment="项目代码", verbose_name='项目代码',
                                 help_text='项目代码')
    item_name = models.CharField(max_length=64, db_comment="项目名称", verbose_name='项目名称',
                                 help_text='项目名称')
    item_cls_code = models.CharField(max_length=36, db_comment="大类代码", verbose_name='大类代码',
                                     help_text='江西省口腔医院市互认上传使用', null=True, blank=True)
    item_cls_name = models.CharField(max_length=36, db_comment="大类代码", verbose_name='大类代码',
                                     help_text='江西省口腔医院市互认上传使用', null=True, blank=True)
    extend_code = models.CharField(max_length=36, db_comment="外部项目代码", help_text='外部项目代码',
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    extend_name = models.CharField(max_length=64, db_comment="外部项目名称", help_text='外部项目名称',
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    checkpoint_id = models.CharField(max_length=36, db_comment="检查部位代码", verbose_name='检查部位代码',
                                     help_text='检查部位代码', null=True, blank=True)
    checkpoint = models.CharField(max_length=36, db_comment="检查部位", verbose_name='检查部位',
                                  help_text='检查部位', null=True, blank=True)
    content = models.CharField(max_length=255, db_comment="检查所见", verbose_name='检查所见',
                               help_text='检查所见')
    url_report_pdf = models.URLField(db_comment="报告pdf链接", verbose_name='报告pdf链接', help_text='报告pdf链接')
    url_image = models.URLField(db_comment="图像查链接", verbose_name='图像查链接', help_text='图像查链接', null=True,
                                blank=True)
    dept_id = models.CharField(max_length=36, db_comment="报告科室ID", help_text='报告科室ID',
                               verbose_name='报告科室ID')
    dept_name = models.CharField(max_length=64, db_comment="报告科室名称", help_text='报告科室名称',
                                 verbose_name='报告科室名称')
    diags = models.CharField(max_length=128, db_comment="临床诊断", help_text='临床诊断',
                             verbose_name='临床诊断')
    diags_comment = models.CharField(max_length=128, db_comment="诊断意见", help_text='诊断意见',
                                     verbose_name='诊断意见')
    comment = models.CharField(max_length=255, db_comment="备注信息或检查提示", help_text='备注信息或检查提示',
                               verbose_name='备注信息或检查提示', null=True, blank=True)

    exam_category_code = models.CharField(max_length=3, choices=ExamCategoryChoices, db_comment="检查分类代码",
                                          help_text='检查分类代码', verbose_name='检查分类代码')
    executor_id = models.CharField(max_length=36, db_comment="检查医生ID", verbose_name='检查医生ID',
                                   help_text='检查医生ID')
    executor = models.CharField(max_length=64, db_comment="检查医生姓名", verbose_name='检查医生姓名',
                                help_text='检查医生姓名')
    gmt_execute = models.DateTimeField(db_comment="检查时间", verbose_name='检查时间', help_text='检查时间')
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id', help_text='报告人id')
    author = models.CharField(max_length=64, db_comment="报告人", verbose_name='报告人', help_text='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间', help_text='报告日期时间')
    verifier_id = models.CharField(max_length=36, db_comment="审核者ID", verbose_name='审核者ID', help_text='审核者ID')
    verifier = models.CharField(max_length=64, db_comment="审核者姓名", verbose_name='审核者姓名',
                                help_text='审核者姓名')
    gmt_verified = models.DateTimeField(db_comment="审核日期时间", verbose_name='审核日期时间',
                                        help_text='审核日期时间')
    device_id = models.CharField(max_length=36, db_comment="设备唯一id", verbose_name='设备唯一id',
                                 help_text='设备唯一id', null=True, blank=True)
    device_name = models.CharField(max_length=64, db_comment="设备名称", verbose_name='设备名称', help_text='设备名称',
                                   null=True, blank=True)
    extra_infos = models.JSONField(db_comment="补充信息", verbose_name='补充信息', help_text='补充信息', null=True,
                                   blank=True)
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统', help_text='来源系统')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构')

    def __str__(self):
        return f'{self.title} - {self.report_id}'

    class Meta:
        verbose_name = '检查报告'
        verbose_name_plural = '检查报告集合'
        db_table_comment = "检查报告表"

        indexes = [
            models.Index(fields=['patient_id']),
            models.Index(fields=['adm_no'])
        ]

    def clean(self):
        # 先调用父类的clean方法来执行字段级别的验证
        super().clean()
        # 自定义验证逻辑
        if not any((isinstance(self.extra_infos, dict), self.extra_infos is None)):
            raise ValidationError(message="extra_infos中的值: '%(value)s'必须是一个字典类型或者null",
                                  code='extra_infos_error', params={'value': self.extra_infos})


class CheckStatusInfo(models.Model):
    class StatusCodeChoices(models.TextChoices):
        """ 检查状态 """
        A1 = ("SC01", "心电检查登记")
        A2 = ("SC02", "取消心电检查登记")
        A3 = ("SC03", "心电采集图像")
        A4 = ("SC04", "心电书写报告")
        A5 = ("SC05", "心电检查打印报告")
        A6 = ("SC06", "超声检查预约")
        A7 = ("SC07", "取消超声检查预约")
        A8 = ("SC08", "超声检查登记")
        A9 = ("SC09", "取消超声检查登记")
        A10 = ("SC10", "超声检查采集图像")
        A11 = ("SC11", "超声检查书写报告")
        A12 = ("SC12", "超声检查打印报告")
        A13 = ("SC13", "超声检查审核")
        A14 = ("SC14", "超声检查复审")
        A15 = ("SC15", "放射检查预约")
        A16 = ("SC16", "取消放射检查预约")
        A17 = ("SC17", "放射检查登记")
        A18 = ("SC18", "取消放射检查登记")
        A19 = ("SC19", "放射检查采集图像")
        A20 = ("SC20", "放射检查书写报告")
        A21 = ("SC21", "放射检查审核")
        A22 = ("SC22", "放射检查复审")
        A23 = ("SC23", "放射检查打印报告")
        A24 = ("SC24", "内镜检查预约")
        A25 = ("SC25", "取消内镜检查预约")
        A26 = ("SC26", "内镜检查登记")
        A27 = ("SC27", "取消内镜检查登记")
        A28 = ("SC28", "内镜检查采集图像")
        A29 = ("SC29", "内镜检查书写报告")
        A30 = ("SC30", "内镜检查打印报告")
        A31 = ("SC31", "内镜检查审核")
        A32 = ("SC32", "内镜检查复审")
        A33 = ("SC33", "病理检查登记")
        A34 = ("SC34", "取消病理检查登记")
        A35 = ("SC35", "病理检查书写报告")
        A36 = ("SC36", "病理检查审核")
        A37 = ("SC37", "病理检查打印报告")

    apply_no = models.CharField(max_length=36, db_comment='申请单号', verbose_name='申请单号', help_text='申请单号')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='操作日期', verbose_name='操作日期',
                                       help_text='操作日期')
    executor_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作人工号',
                                   verbose_name='操作人工号',
                                   help_text='操作人工号')
    executor = models.CharField(max_length=64, blank=True, null=True, db_comment='操作人姓名',
                                verbose_name='操作人姓名',
                                help_text='操作人姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作科室ID', verbose_name='操作科室ID',
                               help_text='操作科室ID')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='操作科室名称',
                                 verbose_name='操作科室名称',
                                 help_text='操作科室名称')
    status_code = models.CharField(max_length=4, choices=StatusCodeChoices, db_comment='检查状态代码',
                                   help_text="检查状态", verbose_name="检查状态")
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')

    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "检查状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检查状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class ExamAppInfo(models.Model):
    apply_no = models.CharField(max_length=36, db_comment='电子申请单编号', unique=True, verbose_name='电子申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单描述',
                                  verbose_name='申请单描述')
    apply_status = models.CharField(max_length=8, blank=True, null=True, db_comment='申请单状态',
                                    verbose_name='申请单状态')
    gmt_effect_high = models.DateTimeField(blank=True, null=True, db_comment='申请单有效日期时间开始',
                                           verbose_name='申请单有效日期时间开始')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='申请单有效日期时间结束',
                                          verbose_name='申请单有效日期时间结束')
    property = models.CharField(max_length=1, choices=PropertyChoices, default='N', db_comment='优先（紧急）度代码',
                                verbose_name='优先（紧急）度代码')
    bar_code = models.CharField(max_length=36, blank=True, null=True, db_comment='条码号', verbose_name='条码号')
    specimen_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='标本类别代码',
                                         verbose_name='标本类别代码')
    specimen_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='标本类别名称',
                                         verbose_name='标本类别名称')
    gmt_apply = models.DateTimeField(blank=True, null=True, db_comment='开单时间', verbose_name='开单时间')
    doc_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单开立者签名',
                                verbose_name='申请单开立者签名')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='开单医生编码',
                              verbose_name='开单医生编码')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='开单医生姓名',
                                verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请科室编码',
                               verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请科室名称',
                                 verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='审核日期时间', verbose_name='审核日期时间')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='审核者编码',
                                   verbose_name='审核者编码')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='审核者姓名',
                                verbose_name='审核者姓名')
    order_id = models.CharField(max_length=36, db_comment='医嘱ID', unique=True, verbose_name='医嘱ID')
    item_code = models.CharField(max_length=36, db_comment='检验项目编码', verbose_name='检验项目编码')
    item_name = models.CharField(max_length=64, db_comment='检验项目名称', verbose_name='检验项目名称')
    method_code = models.CharField(max_length=8, blank=True, null=True, db_comment='检验方法编码',
                                   verbose_name='检验方法编码')
    method_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检验方法名称',
                                   verbose_name='检验方法名称')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='执行时间', verbose_name='执行时间')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='申请注意事项',
                            verbose_name='申请注意事项')
    diags = models.JSONField(blank=True, null=True, db_comment='诊断信息', verbose_name='诊断信息',
                             help_text='诊断(检验申请原因)')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "检验申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检验申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class ExamReport(models.Model):
    """检验报告"""

    class ExamClsCodeChoices(models.IntegerChoices):
        A = (1, '普通')
        B = (2, '细菌药敏')
        C = (3, '文字描述型结果')

    report_id = models.CharField(help_text="检验报告ID", max_length=36, db_comment="检验报告ID", unique=True,
                                 verbose_name='检验报告ID')
    title = models.CharField(max_length=36, db_comment="报告单名称", verbose_name='报告单名称', help_text='报告单名称')
    bar_code = models.CharField(max_length=18, db_comment="条码号", verbose_name='条码号', help_text='条码号')
    specimen_id = models.CharField(max_length=18, db_comment="标本id", verbose_name='标本id', help_text='标本id',
                                   null=True, blank=True)
    specimen_name = models.CharField(max_length=18, db_comment="标本名称", verbose_name='标本名称',
                                     help_text='标本名称',
                                     null=True, blank=True)
    specimen_cls_code = models.CharField(max_length=18, db_comment="标本类型代码", verbose_name='标本类型代码',
                                         help_text='标本类型代码')
    specimen_cls_name = models.CharField(max_length=18, db_comment="标本类型名称", verbose_name='标本类型名称',
                                         help_text='标本类型名称,eg: 血清,尿液...')
    exam_cls_code = models.PositiveSmallIntegerField(choices=ExamClsCodeChoices, db_comment="检验类型",
                                                     verbose_name='检验类型', help_text='检验类型')
    dept_id = models.CharField(max_length=36, db_comment="报告科室ID", verbose_name='报告科室ID',
                               help_text='报告科室ID')
    dept_name = models.CharField(max_length=18, db_comment="报告科室", verbose_name='报告科室', help_text='报告科室')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码')
    content = models.CharField(max_length=255, db_comment="检验所见", verbose_name='检验所见', help_text='检验所见',
                               null=True, blank=True)
    comment = models.CharField(max_length=255, db_comment="备注内容", verbose_name='备注内容', help_text='备注内容',
                               null=True, blank=True)
    url_report_pdf = models.URLField(db_comment="报告pdf链接", verbose_name='报告pdf链接', help_text='报告pdf链接')
    device_id = models.CharField(max_length=36, db_comment="设备唯一id", verbose_name='设备唯一id',
                                 help_text='设备唯一id',
                                 null=True, blank=True)
    device_name = models.CharField(max_length=64, db_comment="设备名称", verbose_name='设备名称', help_text='设备名称',
                                   null=True, blank=True)
    gmt_collect = models.DateTimeField(db_comment="样本采集时间", verbose_name='样本采集时间', help_text='样本采集时间')
    gmt_receive = models.DateTimeField(db_comment="样本接收时间", verbose_name='样本接收时间', help_text='样本接收时间')
    executor_id = models.CharField(max_length=36, db_comment="执行者ID", verbose_name='执行者ID', help_text='执行者ID')
    executor = models.CharField(max_length=64, db_comment="执行者姓名", verbose_name='执行者姓名',
                                help_text='执行者姓名')
    gmt_execute = models.DateTimeField(db_comment="执行日期", verbose_name='执行日期', help_text='执行日期')
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id', help_text='报告人id')
    author = models.CharField(max_length=64, db_comment="报告人", verbose_name='报告人', help_text='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间', help_text='报告日期时间')
    reviewer_id = models.CharField(max_length=36, db_comment="复核医生", verbose_name='复核医生', help_text='复核医生')
    reviewer = models.CharField(max_length=64, db_comment="复核医生姓名", verbose_name='复核医生姓名',
                                help_text='复核医生姓名')
    gmt_review = models.DateTimeField(db_comment="复核日期时间", verbose_name='复核日期时间', help_text='复核日期时间')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统', help_text='来源系统')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构',
                                help_text='医疗卫生机构')

    class Meta:
        verbose_name = '检验报告信息'
        verbose_name_plural = verbose_name
        db_table_comment = '检验报告表'

        indexes = [
            models.Index(fields=['adm_no', ]),
            models.Index(fields=['patient_id'])
        ]


class ExamResultMain(models.Model):
    """检验结果主表"""
    apply_id = models.CharField(max_length=36, db_comment="申请单id", help_text='申请单id', verbose_name='申请单id')
    order_id = models.CharField(max_length=36, db_comment="医嘱id", help_text='医嘱id', verbose_name='医嘱id')
    doc_id = models.CharField(max_length=36, db_comment="申请单医生工号", help_text='申请单医生工号',
                              verbose_name='申请单医生工号')
    doc_name = models.CharField(max_length=64, db_comment="申请单医生姓名", help_text='申请单医生姓名',
                                verbose_name='申请单医生姓名')
    dept_id = models.CharField(max_length=36, db_comment="申请单开单科室ID", verbose_name='申请单开单科室ID',
                               help_text='申请单开单科室ID')
    dept_name = models.CharField(max_length=18, db_comment="申请单开单科室名称", verbose_name='申请单开单科室名称',
                                 help_text='申请单开单科室名称')
    item_code = models.CharField(max_length=36, db_comment="检验项目代码", help_text='检验项目代码',
                                 verbose_name='检验项目代码')
    item_name = models.CharField(max_length=36, db_comment="检验项目名称", help_text='检验项目名称',
                                 verbose_name='检验项目名称')
    item_cls_code = models.CharField(max_length=36, db_comment="检验项目代码", help_text='检验项目代码',
                                     verbose_name='检验项目代码', null=True, blank=True)
    item_cls_name = models.CharField(max_length=64, db_comment="检验项目名称", help_text='检验项目名称',
                                     verbose_name='检验项目名称', null=True, blank=True)
    exam_report_id = models.CharField(max_length=64, db_comment="检验报告", help_text='检验报告',
                                      verbose_name='检验报告')

    indexes = [
        models.Index(fields=['exam_report_id'])
    ]

    class Meta:
        verbose_name = '检验结果主表'
        verbose_name_plural = '检验结果集合'
        db_table_comment = "检验结果主表"


class ExamResultDetail(models.Model):
    """检验结果明细表"""
    index = models.PositiveIntegerField(db_comment="序号", help_text='序号', verbose_name='序号')
    item_code = models.CharField(max_length=36, db_comment="检测项目代码", help_text='检测项目代码',
                                 verbose_name='检测项目代码')
    item_name = models.CharField(max_length=36, db_comment="检测项目", help_text='检测项目', verbose_name='检测项目')
    abbr = models.CharField(max_length=36, db_comment="检测项目缩写", help_text='检测项目缩写',
                            verbose_name='检测项目缩写')
    value = models.CharField(max_length=255, db_comment="结果内容/细菌结果", help_text='结果内容/细菌结果',
                             verbose_name='结果内容/细菌结果')
    unit = models.CharField(max_length=36, db_comment="单位", help_text='单位', verbose_name='单位', null=True,
                            blank=True)
    comment = models.CharField(max_length=64, db_comment="提示", help_text='提示', verbose_name='提示', null=True,
                               blank=True)
    remarks = models.CharField(max_length=128, db_comment="备注信息", help_text='备注信息', verbose_name='备注信息',
                               null=True,
                               blank=True)
    upper_limit_value = models.CharField(max_length=36, db_comment="参考值上限", help_text='参考值上限',
                                         verbose_name='参考值上限', null=True, blank=True)
    lower_limit_value = models.CharField(max_length=36, db_comment="参考值下限", help_text='参考值下限',
                                         verbose_name='参考值下限', null=True, blank=True)
    limit_desc = models.CharField(max_length=255, db_comment="参考值描述", help_text='参考值描述',
                                  verbose_name='参考值描述')
    abnormal_flag_code = models.CharField(max_length=16, db_comment="结果值标志代码", help_text='结果值标志代码',
                                          verbose_name='结果值标志代码')
    abnormal_flag_name = models.CharField(max_length=16, db_comment="结果值标志名称", help_text='结果值标志名称',
                                          verbose_name='结果值标志名称')
    is_warn = models.BooleanField(default=False, db_comment="危急值标识", help_text='危急值标识',
                                  verbose_name='危急值标识')
    test_method_code = models.CharField(max_length=36, db_comment="检测方法代码", help_text='检测方法代码',
                                        verbose_name='检测方法代码', null=True, blank=True)
    test_method_name = models.CharField(max_length=36, db_comment="检测方法名称", help_text='检测方法名称',
                                        verbose_name='检测方法名称', null=True, blank=True)
    is_germ = models.BooleanField(default=False, db_comment="是否为微生物", help_text='是否为微生物',
                                  verbose_name='是否为微生物')
    bacterium_id = models.CharField(max_length=36, db_comment="细菌id", help_text='细菌id', verbose_name='细菌id',
                                    null=True, blank=True)
    bacterium_code = models.CharField(max_length=36, db_comment="细菌代码（用于耐药性和细菌培养）",
                                      help_text='细菌代码（用于耐药性和细菌培养）',
                                      verbose_name='细菌代码（用于耐药性和细菌培养）',
                                      null=True, blank=True)
    bacterium_name = models.CharField(max_length=36, db_comment="细菌名称", help_text='细菌名称',
                                      verbose_name='细菌名称', null=True, blank=True)
    bacterium_abbr = models.CharField(max_length=128, db_comment="细菌名称_英文", help_text='细菌名称_英文',
                                      verbose_name='细菌名称_英文', null=True, blank=True)
    bacterium_type_code = models.CharField(max_length=36, db_comment="菌种类型代码", help_text='菌种类型代码',
                                           verbose_name='菌种类型代码', null=True, blank=True)
    bacterium_type_name = models.CharField(max_length=64, db_comment="菌种类型名称", help_text='菌种类型名称',
                                           verbose_name='菌种类型名称', null=True, blank=True)
    extend_code = models.CharField(max_length=36, db_comment="外部项目代码", help_text='外部项目代码',
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    extend_name = models.CharField(max_length=64, db_comment="外部项目名称", help_text='外部项目名称',
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    exam_result_main_id = models.CharField(max_length=64, db_comment="检验结果主表", help_text='检验结果主表',
                                           verbose_name='检验结果主表')

    indexes = [
        models.Index(fields=['exam_result_main_id'])
    ]

    class Meta:
        verbose_name = '检验结果明细表'
        verbose_name_plural = '检验结果明细集合'
        db_table_comment = "检验结果明细表"


class ExamResultDetailAST(models.Model):
    """检验结果药敏结果"""
    index = models.PositiveIntegerField(db_comment="序号", help_text='序号', verbose_name='序号')
    ast_code = models.CharField(max_length=36, db_comment="药敏代码", help_text='药敏代码',
                                verbose_name='药敏代码')
    ast_name = models.CharField(max_length=36, db_comment="药敏名称", help_text='药敏名称', verbose_name='药敏名称')
    ast_abbr = models.CharField(max_length=36, db_comment="药敏名称缩写", help_text='药敏名称缩写',
                                verbose_name='药敏名称缩写', null=True, blank=True)
    value_qualitative = models.CharField(max_length=64, db_comment="药敏定性结果", help_text='药敏定性结果',
                                         verbose_name='药敏定性结果')
    value_qualitative_desc = models.CharField(max_length=64, db_comment="药敏定性结果", help_text='药敏定性结果',
                                              verbose_name='药敏定性结果')
    value_qualitative_disk = models.CharField(max_length=16, db_comment="药物敏感度", help_text='药物敏感度',
                                              verbose_name='药物敏感度', null=True, blank=True)
    value_ration = models.CharField(max_length=16, db_comment="药敏定量结果", help_text='药敏定量结果',
                                    verbose_name='药敏定量结果', null=True, blank=True)
    mic = models.CharField(max_length=16, db_comment="最小抑菌浓度", help_text='最小抑菌浓度',
                           verbose_name='最小抑菌浓度', null=True, blank=True)
    exam_result_detail_id = models.CharField(max_length=128, db_comment="检验结果明细表",
                                             help_text='检验结果明细表', verbose_name='检验结果明细表')

    class Meta:
        verbose_name = '检验结果药敏结果'
        verbose_name_plural = '检验结果药敏结果集合'
        db_table_comment = "检验结果药敏结果表"

        indexes = [
            models.Index(fields=['exam_result_detail_id'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['exam_result_detail_id', 'ast_code'],
                                    name='unique_exam_result_detail_id_ast_code'),
        ]


class ExamStatusInfo(models.Model):
    class StatusCodeChoices(models.TextChoices):
        """ 检验状态 """
        A1 = ('SE01', '条码打印')
        A2 = ('SE02', '取消打印')
        A3 = ('SE03', '标本采集')
        A4 = ('SE04', '取消采集')
        A5 = ('SE05', '标本送检')
        A6 = ('SE06', '标本送达')
        A7 = ('SE07', '标本接收')
        A8 = ('SE08', '标本拒收')
        A9 = ('SE09', '标本检测')
        A10 = ('SE10', '已出报告')
        A11 = ('SE11', '报告已打印')

    apply_no = models.CharField(max_length=36, db_comment='电子申请单编号', verbose_name='电子申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单描述',
                                  verbose_name='申请单描述')
    apply_status = models.CharField(max_length=8, blank=True, null=True, db_comment='申请单状态',
                                    verbose_name='申请单状态')
    bar_code = models.CharField(max_length=36, db_comment='条码号', verbose_name='条码号')
    specimen_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='标本类别代码',
                                         verbose_name='标本类别代码')
    specimen_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='标本类别名称',
                                         verbose_name='标本类别名称')
    gmt_execute = models.DateTimeField(db_comment='操作日期时间', verbose_name='操作日期时间', help_text='操作日期时间')
    status_code = models.CharField(max_length=4, choices=StatusCodeChoices, db_comment='检验状态',
                                   verbose_name='检验状态')
    reason = models.CharField(max_length=128, blank=True, null=True, db_comment='操作描述（如标本拒绝原因）',
                              verbose_name='操作描述', help_text='如标本拒绝原因')
    executor_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作者代码',
                                   verbose_name='操作者代码')
    executor = models.CharField(max_length=64, blank=True, null=True, db_comment='操作者姓名',
                                verbose_name='操作者姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作科室ID', verbose_name='操作科室ID')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='操作科室名称',
                                 verbose_name='操作科室名称')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "检验状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检验状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class InPatientDischargeInfo(models.Model):
    inpatient_id = models.CharField(max_length=36, db_comment='住院号标识', verbose_name='住院号标识')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    adm_no = models.CharField(max_length=36, db_comment='就诊流水号', verbose_name='就诊流水号', unique=True)
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='入院日期时间', verbose_name='入院日期时间')
    reason = models.CharField(max_length=255, blank=True, null=True, db_comment='就诊原因描述',
                              verbose_name='就诊原因描述')
    ins_code = models.CharField(max_length=4, db_comment='医疗保险类别代码', verbose_name='医疗保险类别代码')
    in_times = models.PositiveSmallIntegerField(db_comment='住院次数', verbose_name='住院次数')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='责任医生的职工号',
                              verbose_name='责任医生的职工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='责任医师姓名',
                                verbose_name='责任医师姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='科室id', verbose_name='科室id')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='科室名称', verbose_name='科室名称')
    ward_id = models.CharField(max_length=36, blank=True, null=True, db_comment='病区id', verbose_name='病区id')
    ward_name = models.CharField(max_length=64, blank=True, null=True, db_comment='病区名称', verbose_name='病区名称')
    room_id = models.CharField(max_length=36, blank=True, null=True, db_comment='病房id', verbose_name='病房id')
    room_name = models.CharField(max_length=64, blank=True, null=True, db_comment='病房名称', verbose_name='病房名称')
    bed_id = models.CharField(max_length=36, blank=True, null=True, db_comment='床号ID', verbose_name='床号ID')
    bed_name = models.CharField(max_length=64, blank=True, null=True, db_comment='床号', verbose_name='床号')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment='服务机构', verbose_name='服务机构')
    is_pre_discharge = models.BooleanField(default=False, db_comment='出院登记标识', verbose_name='出院登记标识')
    gmt_discharge = models.DateTimeField(blank=True, null=True, db_comment='出院登记时间', verbose_name='出院登记时间')
    diags_a = models.JSONField(blank=True, null=True, db_comment='西医诊断', verbose_name='西医诊断')
    diags_b = models.JSONField(blank=True, null=True, db_comment='中医诊断', verbose_name='中医诊断')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "住院就诊信息出院登记信息"
        verbose_name_plural = verbose_name
        db_table_comment = '住院就诊信息出院登记信息'

        indexes = [
            models.Index(fields=('patient_id',)),
        ]


class OperationAppInfo(models.Model):
    class PropertyChoices(models.IntegerChoices):
        A = (1, '择期')
        B = (2, '围期')

    apply_no = models.CharField(max_length=36, db_comment='申请单号', verbose_name="申请单号", unique=True)
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='描述/说明',
                                  verbose_name="描述/说明")
    gmt_apply = models.DateTimeField(blank=True, null=True, db_comment='申请日期', verbose_name='申请日期')
    anesthesia_code = models.CharField(max_length=8, blank=True, null=True, db_comment='麻醉方式编码',
                                       verbose_name='麻醉方式编码')
    anesthesia_name = models.CharField(max_length=64, blank=True, null=True, db_comment='麻醉方式名称',
                                       verbose_name='麻醉方式名称')
    property_code = models.PositiveSmallIntegerField(choices=PropertyChoices, db_comment='手术性质编码（择期，围期)',
                                                     verbose_name='手术性质编码')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请医师工号',
                              verbose_name='申请医师工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请医师姓名',
                                verbose_name='申请医师姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请科室编码',
                               verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请科室名称',
                                 verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='审核日期', verbose_name='审核日期')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='审核医师工号',
                                   verbose_name='审核医师工号')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='审核人姓名',
                                verbose_name='审核人姓名')
    surgical_code = models.CharField(max_length=8, blank=True, null=True, db_comment='手术名称编码',
                                     verbose_name='手术名称编码')
    surgical_name = models.CharField(max_length=64, blank=True, null=True, db_comment='手术名称',
                                     verbose_name='手术名称')
    grade_code = models.CharField(max_length=1, blank=True, null=True, db_comment='手术等级编码',
                                  verbose_name='手术等级编码')
    grade_name = models.CharField(max_length=16, blank=True, null=True, db_comment='手术等级名称',
                                  verbose_name='手术等级名称')
    gmt_booking = models.DateTimeField(blank=True, null=True, db_comment='预订手术时间', verbose_name='预订手术时间')
    execute_doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='手术医师工号',
                                      verbose_name='手术医师工号')
    execute_doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='手术医师姓名',
                                        verbose_name='手术医师姓名')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='注意事项', verbose_name='注意事项')
    diags = models.JSONField(blank=True, null=True, db_comment='诊断信息', verbose_name='诊断信息',
                             help_text='诊断(手术申请原因)')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "手术申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OperationScheduleInfo(models.Model):
    booking_id = models.CharField(max_length=36, db_comment='手术排班号', verbose_name='手术排班号', unique=True)
    gmt_booking = models.DateTimeField(db_comment='预约手术时间', verbose_name='预约手术时间')
    duration = models.PositiveSmallIntegerField(db_comment='预计手术时长', verbose_name='预计手术时长')
    duration_unit = models.CharField(max_length=8, blank=True, null=True, db_comment='预计手术时长单位',
                                     verbose_name='预计手术时长单位')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    device_id = models.CharField(max_length=36, blank=True, null=True, db_comment='预约设备编码',
                                 verbose_name='预约设备编码')
    device_name = models.CharField(max_length=64, blank=True, null=True, db_comment='预约设备名称',
                                   verbose_name='预约设备名称')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='主刀医生工号',
                              verbose_name='主刀医生工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='主刀医生名称',
                                verbose_name='主刀医生名称')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                               verbose_name='执行科室编码')
    dept_name = models.CharField(max_length=255, blank=True, null=True, db_comment='执行科室名称',
                                 verbose_name='执行科室名称')
    room = models.CharField(max_length=36, blank=True, null=True, db_comment='手术间', verbose_name='手术间')
    apply_no = models.CharField(max_length=36, db_comment='手术申请单号', verbose_name='手术申请单号', unique=True)
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    assistants = models.JSONField(blank=True, null=True, db_comment='助手信息', verbose_name='助手信息')

    class Meta:
        verbose_name = "手术排班信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术排班信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OperationStatusInfo(models.Model):
    apply_no = models.CharField(max_length=36, db_comment='申请单号', verbose_name='手术申请单号')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='操作日期', verbose_name='操作日期')
    executor_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作人工号',
                                   verbose_name='操作人工号')
    executor = models.CharField(max_length=64, blank=True, null=True, db_comment='操作人姓名',
                                verbose_name='操作人姓名')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    status_code = models.CharField(max_length=8, blank=True, null=True, db_comment='手术状态编码',
                                   verbose_name='手术状态编码')
    status_name = models.CharField(max_length=36, blank=True, null=True, db_comment='手术状态名称',
                                   verbose_name='手术状态名称')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "手术状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OrderFillerStatusInfo(models.Model):
    """ 医嘱执行状态 """
    order_id = models.CharField(max_length=36, db_comment='医嘱ID', verbose_name='医嘱ID')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='操作日期', verbose_name='操作日期')
    executor_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作人工号',
                                   verbose_name='操作人工号')
    executor = models.CharField(max_length=64, blank=True, null=True, db_comment='操作人姓名',
                                verbose_name='操作人姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                               verbose_name='执行科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                 verbose_name='执行科室名称')
    apply_no = models.CharField(max_length=36, blank=True, null=True, db_comment='申请单号', verbose_name='申请单号')
    item_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医嘱类别编码',
                                     verbose_name='医嘱类别编码')
    item_cls_name = models.CharField(max_length=64, blank=True, null=True, db_comment='医嘱类别名称',
                                     verbose_name='医嘱类别名称')
    bar_code = models.CharField(max_length=36, blank=True, null=True, db_comment='标本条码号',
                                verbose_name='标本条码号')
    gmt_collect = models.DateTimeField(blank=True, null=True, db_comment='采集日期', verbose_name='采集日期')
    collector_id = models.CharField(max_length=36, blank=True, null=True, db_comment='采集人Id',
                                    verbose_name='采集人Id')
    collector_name = models.CharField(max_length=64, blank=True, null=True, db_comment='采集人姓名',
                                      verbose_name='采集人姓名')
    reason = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱撤消原因',
                              verbose_name='医嘱撤消原因')
    execute_status_code = models.CharField(max_length=36, db_comment='医嘱执行状态', verbose_name='医嘱执行状态')
    execute_status_name = models.CharField(max_length=64, db_comment='医嘱执行状态名称',
                                           verbose_name='医嘱执行状态名称')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "医嘱执行状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医嘱执行状态信息'

        indexes = [
            models.Index(fields=('order_id',)),
            models.Index(fields=('patient_id',)),
            models.Index(fields=('patient_id', 'times')),
        ]


class OrderInfo(models.Model):
    gmt_order = models.DateTimeField(blank=True, null=True, db_comment='医嘱开立日期时间',
                                     verbose_name='医嘱开立日期时间')
    doc_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱开立者签名',
                                verbose_name='医嘱开立者签名')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='医务人员工号',
                              verbose_name='医务人员工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='医嘱开立者',
                                verbose_name='医嘱开立者')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='医疗卫生机构（科室）ID',
                               verbose_name='医疗卫生机构（科室）ID')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='医嘱开立科室',
                                 verbose_name='医嘱开立科室')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='医嘱审核日期时间',
                                      verbose_name='医嘱审核日期时间')
    reviewer_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱审核者签名',
                                     verbose_name='医嘱审核者签名')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='医嘱审核者工号',
                                   verbose_name='医嘱审核者工号')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='医嘱审核者',
                                verbose_name='医嘱审核者')
    index = models.PositiveIntegerField(db_comment='医嘱序号', verbose_name='医嘱序号')
    order_id = models.CharField(db_comment='医嘱ID', verbose_name='医嘱ID', unique=True, max_length=36)
    item_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医嘱项目类型代码',
                                     verbose_name='医嘱项目类型代码')
    item_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='医嘱项目类型名称',
                                     verbose_name='医嘱项目类型名称')
    content = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱项目内容',
                               verbose_name='医嘱项目内容')
    gmt_effect_high = models.DateTimeField(blank=True, null=True, db_comment='医嘱开始日期时间',
                                           verbose_name='医嘱开始日期时间')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='医嘱结束日期时间 ',
                                          verbose_name='医嘱结束日期时间')
    rate_execute_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医嘱执行频率编码',
                                         verbose_name='医嘱执行频率编码')
    rate_execute_name = models.CharField(max_length=36, blank=True, null=True, db_comment='医嘱执行频率名称',
                                         verbose_name='医嘱执行频率名称')
    route_code = models.CharField(max_length=8, blank=True, null=True, db_comment='用药途径代码',
                                  verbose_name='用药途径代码')
    route_name = models.CharField(max_length=36, blank=True, null=True, db_comment='用药途径名称',
                                  verbose_name='用药途径名称')
    dose = models.CharField(max_length=36, blank=True, null=True, db_comment='用药剂量-单次',
                            verbose_name='用药剂量-单次')
    dose_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='用药剂量-单次-单位',
                                 verbose_name='用药剂量-单次-单位')
    dose_total = models.CharField(max_length=64, blank=True, null=True, db_comment='药物使用总剂量',
                                  verbose_name='药物使用总剂量')
    dose_total_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='药物使用总剂量-单位',
                                       verbose_name='医嘱开立日期时间')
    dose_total_day = models.PositiveSmallIntegerField(db_default=1, db_comment='药物使用总剂量-天数',
                                                      verbose_name='药物使用总剂量-天数')
    dosage_admin_code = models.CharField(max_length=8, blank=True, null=True, db_comment='药物剂型代码',
                                         verbose_name='药物剂型代码')
    dosage_admin_name = models.CharField(max_length=36, blank=True, null=True, db_comment='药物剂型名称',
                                         verbose_name='药物剂型名称')
    package_index = models.PositiveSmallIntegerField(db_default=1, db_comment='包装序号',
                                                     verbose_name='医嘱开立日期时间')
    product_code = models.CharField(max_length=36, blank=True, null=True, db_comment='药物编码',
                                    verbose_name='药物编码')
    product_name = models.CharField(max_length=64, blank=True, null=True, db_comment='药物名称',
                                    verbose_name='药物名称')
    product_capacity = models.CharField(max_length=255, blank=True, null=True, db_comment='药物规格',
                                        verbose_name='药物规格')
    product_capacity_unit = models.CharField(max_length=255, blank=True, null=True, db_comment='药物规格单位',
                                             verbose_name='药物规格单位')
    product_ins_code = models.CharField(max_length=36, blank=True, null=True, db_comment='药物医保类别编码',
                                        verbose_name='药物医保类别编码')
    product_ins_name = models.CharField(max_length=64, blank=True, null=True, db_comment='药物医保类别名称',
                                        verbose_name='药物医保类别名称')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    pre_order_id = models.CharField(max_length=64, blank=True, null=True,
                                    db_comment='父医嘱ID(没有父医嘱可以没有此occurrenceOf节点)',
                                    verbose_name='父医嘱ID',
                                    help_text='没有父医嘱可以没有此occurrenceOf节点')
    order_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医嘱类别编码',
                                      verbose_name='医嘱类别编码')
    order_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='医嘱类别名称',
                                      verbose_name='医嘱类别名称')
    amount = models.PositiveSmallIntegerField(default=1, db_comment='领量(给药量)', verbose_name='领量(给药量)')
    amount_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='领量(给药量)-单位',
                                   verbose_name='领量(给药量)-单位')
    gmt_start = models.DateTimeField(blank=True, null=True, db_comment='开始时间', verbose_name='开始时间')
    gmt_end = models.DateTimeField(blank=True, null=True, db_comment='停止时间', verbose_name='停止时间')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱备注信息',
                            verbose_name='医嘱备注信息')
    note_status = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱备注信息状态',
                                   verbose_name='医嘱备注信息状态')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "医嘱信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医嘱信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OrganizationInfo(models.Model):
    dept_id = models.CharField(max_length=36, db_comment='医疗卫生机构（科室）标识-科室ID', unique=True,
                               verbose_name="医疗卫生机构（科室）标识-科室ID")
    dept_name = models.CharField(max_length=64, db_comment='医疗卫生机构（科室）实体名称',
                                 verbose_name="医疗卫生机构（科室）实体名称")
    dept_cls_code = models.CharField(max_length=16, db_comment='医疗卫生机构（科室）类别-科室代码',
                                     verbose_name="医疗卫生机构（科室）类别-科室代码")
    dept_cls_name = models.CharField(max_length=64, db_comment='医疗卫生机构（科室）类别-科室',
                                     verbose_name="医疗卫生机构（科室）类别-科室")
    dept_role = models.CharField(max_length=64, blank=True, null=True, db_comment='医疗卫生机构（科室）角色名称',
                                 verbose_name="医疗卫生机构（科室）角色名称")
    dept_addr = models.CharField(max_length=255, blank=True, null=True, db_comment='工作地址', verbose_name="工作地址")
    dept_tel = models.CharField(max_length=36, blank=True, null=True, db_comment='工作联系方式：电话、邮箱地址等',
                                verbose_name="工作联系方式：电话、邮箱地址等")
    gmt_effect_high = models.DateTimeField(db_comment='角色有效期间开始', verbose_name="角色有效期间开始")
    gmt_effect_low = models.DateTimeField(db_comment='角色有效期间结束', verbose_name="角色有效期间结束")
    pre_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='上级医疗卫生机构（科室）号标识',
                                   verbose_name="上级医疗卫生机构（科室）号标识")
    pre_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='上级医疗卫生机构（科室）号名称',
                                     verbose_name="级医疗卫生机构（科室）号名称")
    author_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请者医务人员ID',
                                 verbose_name="申请者医务人员ID")
    author = models.CharField(max_length=36, blank=True, null=True, db_comment='申请者医务人员姓名',
                              verbose_name="申请者医务人员姓名")
    author_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请者医务人员科室号标识',
                                      verbose_name="申请者医务人员科室号标识")
    author_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请者医务人员科室名称',
                                        verbose_name="申请者医务人员科室名称")
    author_dept_contact = models.CharField(max_length=64, blank=True, null=True, db_comment='申请者医务人员科室联系人',
                                           verbose_name="申请者医务人员科室联系人")
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name="来源系统")
    gmt_created = models.DateTimeField(db_comment='申请时间', verbose_name="申请时间")

    class Meta:
        verbose_name = "医疗机构信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医疗机构信息'


class OutpatientAppointStatusInfo(models.Model):
    booking_id = models.CharField(max_length=36, db_comment='预约ID', unique=True, verbose_name="预约ID")
    gmt_schedule = models.DateTimeField(db_comment='预约日期时间', verbose_name="预约日期时间")
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    id_no = models.CharField(max_length=36, db_comment='身份证号', verbose_name="身份证号")
    patient_name = models.CharField(max_length=64, db_comment='姓名', verbose_name="姓名")
    gmt_booking = models.DateTimeField(db_comment='系统预约日期时间', verbose_name="系统预约日期时间")
    from_src = models.CharField(max_length=36, db_comment='系统id', verbose_name="系统id")
    booking_code = models.CharField(max_length=36, db_comment='预约状态代码', verbose_name="预约状态代码")
    booking_name = models.CharField(max_length=64, db_comment='预约状态名称', verbose_name="预约状态名称")
    gmt_operate = models.DateTimeField(db_comment='医务人员预约日期时间', verbose_name="医务人员预约日期时间")
    operator_id = models.CharField(max_length=36, db_comment='医务人员工号', verbose_name="医务人员工号")
    schedule_id = models.CharField(max_length=36, db_comment='资源ID', verbose_name="资源ID")
    gmt_effect_high = models.DateTimeField(db_comment='资源时段开始时间', verbose_name="资源时段开始时间")
    gmt_effect_low = models.DateTimeField(db_comment='资源时段结束时间', verbose_name="资源时段结束时间")
    extra = models.JSONField(db_comment='补充信息', verbose_name="补充信息")

    class Meta:
        verbose_name = "门诊预约状态"
        verbose_name_plural = verbose_name
        db_table_comment = '门诊预约状态'

        indexes = [
            models.Index(fields=('patient_id',)),
        ]


class OutPatientInfo(models.Model):
    gmt_reg = models.DateTimeField(db_comment='挂号时间', verbose_name='挂号时间')
    adm_no = models.CharField(max_length=36, blank=True, null=True, db_comment='就诊流水号', verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_adm = models.DateTimeField(blank=True, null=True, db_comment='就诊日期时间', verbose_name='就诊日期时间')
    reason = models.CharField(max_length=128, blank=True, null=True, db_comment='就诊原因描述',
                              verbose_name='就诊原因描述')
    ins_cls_code = models.CharField(max_length=2, db_comment='医疗保险类别代码', verbose_name='医疗保险类别代码')
    ins_cls_name = models.CharField(max_length=16, db_comment='医疗保险类别名称', verbose_name='医疗保险类别名称')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    doc_id = models.CharField(max_length=36, db_comment='医生的职工号', verbose_name='医生的职工号')
    doc_name = models.CharField(max_length=16, db_comment='责任医师姓名', verbose_name='责任医师姓名')
    dept_id = models.CharField(max_length=36, db_comment='服务场所科室标识', verbose_name='服务场所科室标识')
    dept_name = models.CharField(max_length=64, db_comment='服务场所科室', verbose_name='服务场所科室')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment='服务机构标识', verbose_name='服务机构标识')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    extra = models.JSONField(db_comment='补充信息', verbose_name='补充信息')

    class Meta:
        verbose_name = "门诊挂号信息"
        verbose_name_plural = verbose_name
        db_table_comment = '门诊挂号信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class PathologyAppInfo(models.Model):
    apply_no = models.CharField(max_length=36, db_comment='检查申请单编号', unique=True, verbose_name='检查申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单详细内容',
                                  verbose_name='申请单详细内容')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='检查申请日期', verbose_name='检查申请日期')
    class_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查类型编码',
                                  verbose_name='检查类型编码')
    class_name = models.CharField(max_length=255, blank=True, null=True, db_comment='检查类型名称',
                                  verbose_name='检查类型名称')
    send_part = models.CharField(max_length=255, blank=True, null=True, db_comment='送检组织部位',
                                 verbose_name='送检组织部位')
    send_part_amount = models.PositiveSmallIntegerField(db_comment='送检组织数量', db_default=1,
                                                        verbose_name='检查申请单编号')
    send_part_amount_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='送检组织数量单位',
                                             verbose_name='送检组织数量单位')
    bar_code = models.CharField(max_length=36, blank=True, null=True, db_comment='样本条码号',
                                verbose_name='取材组织数量')
    collect_part = models.CharField(max_length=64, blank=True, null=True, db_comment='取材组织部位',
                                    verbose_name='取材组织部位')
    collect_part_amount = models.PositiveSmallIntegerField(db_default=1, db_comment='取材组织数量',
                                                           verbose_name='取材组织数量')
    collect_part_amount_unit = models.CharField(max_length=36, blank=True, null=True, db_comment='取材组织数量单位',
                                                verbose_name='取材组织数量单位')
    fixation = models.CharField(max_length=64, blank=True, null=True, db_comment='固定液', verbose_name='固定液')
    gmt_collect = models.DateTimeField(blank=True, null=True, db_comment='采集日期', verbose_name='采集日期')
    send_doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='送检医师Id',
                                   verbose_name='送检医师Id')
    send_doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='送检医师姓名',
                                     verbose_name='送检医师姓名')
    gmt_apply = models.DateTimeField(blank=True, null=True, db_comment='开单时间', verbose_name='开单时间')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='开单医生工号',
                              verbose_name='开单医生工号')
    doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='开单医生姓名',
                                verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='申请科室编码',
                               verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='申请科室名称',
                                 verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='确认时间', verbose_name='确认时间')
    reviewer_id = models.CharField(max_length=36, blank=True, null=True, db_comment='确认医生工号',
                                   verbose_name='确认医生工号')
    reviewer = models.CharField(max_length=64, blank=True, null=True, db_comment='确认人姓名',
                                verbose_name='确认人姓名')
    record = models.CharField(max_length=255, blank=True, null=True, db_comment='病历摘要及手术所见',
                              verbose_name='病历摘要及手术所见')
    item_code = models.CharField(max_length=36, db_comment='检查项目编码', verbose_name='检查项目编码')
    item_name = models.CharField(max_length=64, db_comment='检查项目名称', verbose_name='检查项目名称')
    method_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查方式编码',
                                   verbose_name='检查方式编码')
    method_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查方式名称',
                                   verbose_name='检查方式名称')
    site_code = models.CharField(max_length=36, blank=True, null=True, db_comment='检查部位编码',
                                 verbose_name='检查部位编码')
    site_name = models.CharField(max_length=64, blank=True, null=True, db_comment='检查部位名称',
                                 verbose_name='检查部位名称')
    gmt_execute = models.DateTimeField(blank=True, null=True, db_comment='执行时间', verbose_name='执行时间')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    note = models.CharField(max_length=255, blank=True, null=True, db_comment='申请注意事项',
                            verbose_name='申请注意事项')
    diags = models.JSONField(blank=True, null=True, db_comment='诊断信息', verbose_name='诊断信息',
                             help_text='诊断(检查申请原因)')
    adm_no = models.CharField(max_length=36, blank=True, null=True, db_comment='就诊流水号', verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "病理申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '病理申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class PatientInfo(models.Model):
    """患者信息"""
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID',
                                  unique=True)
    gmt_reg = models.DateTimeField(db_comment="患者登记时间", help_text="患者登记时间", verbose_name='患者登记时间')
    id_no = models.CharField(max_length=36, db_comment="证件号码", verbose_name='证件号码')
    id_code = models.CharField(max_length=2, db_comment="证件类型代码", verbose_name='证件类型代码')
    patient_name = models.CharField(max_length=36, db_comment="患者姓名", verbose_name='患者姓名')
    tel_no = models.CharField(max_length=36, db_comment="联系电话", verbose_name='联系电话')
    sex_code = models.PositiveSmallIntegerField(choices=SexCodeChoices, db_comment="性别代码", verbose_name='性别代码',
                                                help_text="性别")
    gmt_birth = models.DateField(db_comment="出生日期", verbose_name='出生日期')
    addr_sal = models.CharField(max_length=128, db_comment="完整地址描述", verbose_name='完整地址描述')
    addr_sta = models.CharField(max_length=36, db_comment="自治区、直辖市", verbose_name='自治区、直辖市', null=True,
                                blank=True)
    addr_cty = models.CharField(max_length=36, db_comment="地址-市（地区）", verbose_name='地址-市（地区）', null=True,
                                blank=True)
    addr_cnt = models.CharField(max_length=36, db_comment="地址-县（区）", verbose_name='地址-县（区）', null=True,
                                blank=True)
    addr_stb = models.CharField(max_length=36, db_comment="地址-乡（镇、街道办事处）",
                                verbose_name='地址-乡（镇、街道办事处）',
                                null=True, blank=True)
    addr_str = models.CharField(max_length=36, db_comment="地址-村（街、路、弄等）", verbose_name='地址-村（街、路、弄等）',
                                null=True, blank=True)
    addr_bnr = models.CharField(max_length=36, db_comment="地址-门牌号码", verbose_name='地址-门牌号码', null=True,
                                blank=True)
    addr_zip = models.CharField(max_length=36, db_comment="邮政编码", verbose_name='邮政编码', null=True, blank=True)
    marital_status_code = models.CharField(max_length=36, db_comment="婚姻状况代码", verbose_name='婚姻状况代码')
    ethnic_group_code = models.CharField(max_length=36, db_comment="民族代码", verbose_name='民族代码')
    occupation_code = models.CharField(max_length=36, db_comment="职业类别代码", verbose_name='职业类别代码')
    work_org = models.CharField(max_length=36, db_comment="工作单位", verbose_name='工作单位', null=True, blank=True)
    work_org_tel = models.CharField(max_length=36, db_comment="工作单位联系电话", verbose_name='工作单位联系电话',
                                    null=True,
                                    blank=True)
    hcard_no = models.CharField(max_length=36, db_comment="健康卡号", verbose_name='健康卡号', null=True, blank=True)
    hcard_org_code = models.CharField(max_length=36, db_comment="健康卡发放机构代码", verbose_name='健康卡发放机构代码',
                                      choices=FromOrgCodeChoices)
    gcard_no = models.CharField(max_length=36, db_comment="城乡居民健康档案编号", verbose_name='城乡居民健康档案编号',
                                null=True, blank=True)
    gcard_org_code = models.CharField(max_length=36, db_comment="建档医疗机构组织机构代码",
                                      verbose_name='建档医疗机构组织机构代码', choices=FromOrgCodeChoices)
    contact_code = models.CharField(max_length=36, db_comment="联系人关系代码", verbose_name='联系人关系代码')
    contact_tel = models.CharField(max_length=36, db_comment="联系人电话", verbose_name='联系人电话')
    contact_cname = models.CharField(max_length=36, db_comment="联系人姓名", verbose_name='联系人姓名')
    org_code = models.CharField(max_length=36, choices=FromOrgCodeChoices, db_comment="组织机构代码", verbose_name='组织机构代码')
    org_name = models.CharField(max_length=36, db_comment="组织机构名称", verbose_name='组织机构名称')
    ins_code = models.CharField(max_length=36, db_comment="医疗保险类别代码", verbose_name='医疗保险类别代码')
    author_id = models.CharField(max_length=36, db_comment="登记人ID", verbose_name='登记人ID')
    author = models.CharField(max_length=36, db_comment="登记人", verbose_name='登记人')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    empi_id = models.CharField(max_length=36, db_comment="EMPI号", verbose_name='EMPI号', null=True, blank=True)
    gmt_updated = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='最后更新时间')
    outpatient_id = models.CharField(max_length=36, db_comment="门急诊号标识ID", verbose_name='门急诊号标识ID',
                                     help_text="门急诊号标识,对于门诊住院患者不同表情况下使用", null=True, blank=True)
    inpatient_id = models.CharField(max_length=36, db_comment="住院号", verbose_name='住院号',
                                    help_text='住院号标识,对于门诊住院患者不同表情况下使用', null=True, blank=True)

    def __str__(self):
        return f"{self.patient_name}-{self.patient_id}"

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name
        db_table_comment = '个人信息'


class ProviderInfo(models.Model):
    emp_id = models.CharField(max_length=36, db_comment='医务人员ID', unique=True, verbose_name='医务人员ID')
    emp_name = models.CharField(max_length=64, db_comment='姓名', verbose_name='姓名')
    job_code = models.CharField(max_length=10, db_comment='专业技术职务代码', verbose_name='专业技术职务代码')
    job_name = models.CharField(max_length=64, db_comment='专业技术职务名称', verbose_name='专业技术职务名称')
    gmt_effect_high = models.DateTimeField(db_comment='角色有效期间开始', verbose_name='角色有效期间开始')
    gmt_effect_low = models.DateTimeField(db_comment='角色有效期间结束', verbose_name='角色有效期间结束')
    id_no = models.CharField(max_length=32, db_comment='身份证号', verbose_name='身份证号')
    id_code = models.CharField(max_length=2, db_comment='证件号代码', verbose_name='证件号代码')
    id_name = models.CharField(max_length=16, db_comment='证件号名称', verbose_name='证件号名称')
    sex_code = models.PositiveSmallIntegerField(choices=SexCodeChoices, db_comment="性别代码", verbose_name='性别代码')
    addr_birth = models.CharField(max_length=255, blank=True, null=True, db_comment='出生地', verbose_name='出生地')
    gmt_birth = models.DateField(db_comment='出生日期', verbose_name='出生日期')
    dept_id = models.CharField(max_length=32, db_comment='科室号标识', verbose_name='科室号标识')
    dept_name = models.CharField(max_length=64, db_comment='科室号名称', verbose_name='科室号名称')
    author_id = models.CharField(max_length=36, db_comment='申请者医务人员ID', verbose_name='申请者医务人员ID')
    author = models.CharField(max_length=64, db_comment='申请者医务人员名称', verbose_name='申请者医务人员名称')
    author_dept_id = models.CharField(max_length=36, db_comment='申请者科室ID', verbose_name='申请者科室ID')
    author_dept_name = models.CharField(max_length=64, db_comment='申请者科室名称', verbose_name='申请者科室名称')
    author_dept_contact = models.CharField(max_length=64, blank=True, null=True, db_comment='申请者科室联系人名称',
                                           verbose_name='申请者科室联系人名称')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    gmt_created = models.DateTimeField(db_comment='申请时间', verbose_name='申请时间')

    class Meta:
        verbose_name = "医疗卫生人员信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医疗卫生人员信息'


class SourceAndScheduleInfo(models.Model):
    schedule_id = models.CharField(max_length=36, db_comment='排班标识', unique=True, verbose_name='排班标识')
    roster_id = models.CharField(max_length=36, blank=True, null=True, db_comment='操作者ID', verbose_name='操作者ID')
    roster = models.CharField(max_length=64, blank=True, null=True, db_comment='操作者', verbose_name='操作者')
    gmt_rostered = models.DateTimeField(blank=True, null=True, db_comment='操作时间', verbose_name='操作时间')
    dept_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医疗卫生机构业务科室分类代码',
                                     verbose_name='医疗卫生机构业务科室分类代码')
    dept_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='医疗卫生机构业务科室分类名称',
                                     verbose_name='医疗卫生机构业务科室分类名称')
    total = models.PositiveIntegerField(db_comment='资源总数', verbose_name='资源总数')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='科室标识', verbose_name='科室标识')
    res_rank_code = models.CharField(max_length=8, blank=True, null=True, db_comment='资源级别代码',
                                     verbose_name='资源级别代码')
    res_rank_name = models.CharField(max_length=36, blank=True, null=True, db_comment='资源级别名称',
                                     verbose_name='资源级别名称')
    doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='出诊医生ID', verbose_name='出诊医生ID')
    doc_name = models.CharField(max_length=36, blank=True, null=True, db_comment='出诊医生姓名',
                                verbose_name='出诊医生姓名')
    job_code = models.CharField(max_length=36, blank=True, null=True, db_comment='专业技术职务类别代码',
                                verbose_name='专业技术职务类别代码')
    job_name = models.CharField(max_length=36, blank=True, null=True, db_comment='专业技术职务类别名称',
                                verbose_name='专业技术职务类别名称')
    id_no = models.CharField(max_length=36, blank=True, null=True, db_comment='身份证号', verbose_name='身份证号')
    res_code = models.CharField(max_length=36, blank=True, null=True, db_comment='排班资源类型代码',
                                verbose_name='排班资源类型代码')
    res_name = models.CharField(max_length=64, blank=True, null=True, db_comment='排班资源类型名称',
                                verbose_name='排班资源类型名称')
    amount = models.PositiveSmallIntegerField(db_comment='分时段资源总数', verbose_name='分时段资源总数')
    gmt_effect_high = models.DateTimeField(blank=True, null=True, db_comment='排班开始日期时间',
                                           verbose_name='排班开始日期时间')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='排班结束日期时间',
                                          verbose_name='排班结束日期时间')
    remain = models.PositiveSmallIntegerField(db_comment='剩余号数', verbose_name='剩余号数')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "号源排班信息"
        verbose_name_plural = verbose_name
        db_table_comment = '号源排班信息'


class Terminology(models.Model):
    dataset_code = models.CharField(max_length=36, db_comment='值集标识符', verbose_name='值集标识符')
    dataset_name = models.CharField(max_length=64, db_comment='值集描述', verbose_name='值集描述')
    status = models.BooleanField(default=True, db_comment='值集状态代码; 1: 启用，0：未启用',
                                 verbose_name='值集状态启用代码')
    version_no = models.PositiveSmallIntegerField(db_comment='版本号', verbose_name='版本号', default=1, db_default=1)
    version = models.CharField(max_length=36, db_comment='值集版本信息', verbose_name='值集版本信息')
    item_code = models.CharField(max_length=36, db_comment='项目代码', verbose_name='项目代码')
    item_name = models.CharField(max_length=64, db_comment='项目描述', verbose_name='项目描述')
    item_status = models.BooleanField(default=True, db_comment='项目状态; 1: 启用，0：未启用',
                                      verbose_name='项目启用状态')
    author_id = models.CharField(max_length=36, db_comment='值集注册者信息注册人ID',
                                 verbose_name='值集注册者信息注册人ID')
    author = models.CharField(max_length=64, db_comment='值集注册者信息注册人姓名',
                              verbose_name='值集注册者信息注册人姓名')
    gmt_author = models.DateTimeField(db_comment='值集注册者时间', verbose_name='值集注册者时间')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "术语信息"
        verbose_name_plural = verbose_name
        db_table_comment = '术语信息'

        indexes = [
            models.Index(fields=('dataset_code',))
        ]


class TransferInfo(models.Model):
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    gmt_in = models.DateTimeField(db_comment='转入日期时间', verbose_name='转入日期时间')
    in_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转入科室id',
                                  verbose_name='转入科室id')
    in_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转入科室名称',
                                    verbose_name='转入科室名称')
    in_ward_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转入病区id',
                                  verbose_name='转入病区id')
    in_ward_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转入病区名称',
                                    verbose_name='转入病区名称')
    in_room_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转入病房id',
                                  verbose_name='转入病房id')
    in_room_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转入病房名称',
                                    verbose_name='转入病房名称')
    in_bed_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转入床号ID',
                                 verbose_name='转入床号ID')
    in_bed_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转入床号', verbose_name='转入床号')
    gmt_out = models.DateTimeField(db_comment='转出日期时间', verbose_name='转出日期时间')
    out_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转出科室id',
                                   verbose_name='转出科室id')
    out_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转出科室名称',
                                     verbose_name='转出科室名称')
    out_ward_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转出病区id',
                                   verbose_name='转出病区id')
    out_ward_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转出病区名称',
                                     verbose_name='转出病区名称')
    out_room_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转出病房id',
                                   verbose_name='转出病房id')
    out_room_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转出病房名称',
                                     verbose_name='转出病房名称')
    out_bed_id = models.CharField(max_length=36, blank=True, null=True, db_comment='转出床号ID',
                                  verbose_name='转出床号ID')
    out_bed_name = models.CharField(max_length=64, blank=True, null=True, db_comment='转出床号',
                                    verbose_name='转出床号')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')

    class Meta:
        verbose_name = "住院转科信息"
        verbose_name_plural = verbose_name
        db_table_comment = '住院转科信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]
