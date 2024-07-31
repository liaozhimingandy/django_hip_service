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


class MaritalStatusCodeChoices(models.TextChoices):
    A = ('10', '未婚')
    B = ('20', '已婚')
    C = ('21', '初婚')
    D = ('22', '再婚')
    E = ('23', '复婚')
    F = ('30', '丧偶')
    G = ('40', '离婚')
    H = ('90', '未说明的婚姻状况')


class PropertyChoices(models.TextChoices):
    """ 优先（紧急）度代码 """
    A = ('N', 'normal')
    B = ('U', 'urgent')
    C = ('C', 'critical')
    D = ('E', 'endangered')


class FromOrgCodeChoices(models.TextChoices):
    """ 来源机构 """
    A = ('12360000491015900T', '南昌大学附属口腔医院（江西省口腔医院）')


class IdCodeChoices(models.TextChoices):
    """ 身份证件类别代码表 """
    A = ('01', '居民身份证')
    B = ('02', '居民户口簿')
    C = ('03', '护照')
    D = ('04', '军官证')
    E = ('05', '驾驶证')
    F = ('06', '港澳居民来往内地通行证')
    G = ('07', '台湾居民来往内地通行证')
    H = ('99', '其他法定有效证件')


class InsCodeChoices(models.TextChoices):
    """ 医疗保险类别代码表 """
    A = ('01', '城镇职工基本医疗保险')
    B = ('02', '城镇居民基本医疗保险')
    C = ('03', '新型农村合作医疗')
    D = ('04', '公务员医疗补助')
    E = ('05', '企业补充医疗保险')
    F = ('06', '大额补充医疗保险')
    G = ('07', '商业医疗保险')
    H = ('99', '其他')


class OrderClsCode(models.TextChoices):
    """ 医嘱类别代码表 """
    A = (1, '长期医嘱')
    B = (2, '临时医嘱')
    C = (9, '其他')


class CheckCategoryChoices(models.TextChoices):
    """
    检查分类,检查类型
    """
    A = ('ECG', '心电检查')
    B = ('UIS', '超声检查')
    C = ('PIS', '病理检查')
    D = ('RIS', '放射检查')
    E = ('EIS', '内镜检查')


# Create your models here.
class BloodTrans(models.Model):
    """
    输血申请信息
    """

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
    blood = models.PositiveSmallIntegerField(blank=True, null=True, db_comment='血量', verbose_name='血量')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "输血申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '输血申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Check(models.Model):
    """
    检查申请信息
    """
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
    class_code = models.CharField(max_length=3, choices=CheckCategoryChoices, db_comment='检查类型编码',
                                  verbose_name='检查类型编码')
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
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

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


class CheckAppointStatus(models.Model):
    """
    检查预约状态信息
    """
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
    booking_id = models.CharField(max_length=36, db_comment='预约员工号', verbose_name='预约员工号')
    bookinger = models.CharField(max_length=64, db_comment='预约员姓名', verbose_name='预约员姓名')
    execute_dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='执行科室编码(ID) ',
                                       verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='执行科室名称',
                                         verbose_name='执行科室名称')
    apply_no = models.CharField(max_length=36, db_comment='检查申请单编号', verbose_name='检查申请单编号')
    order_id = models.CharField(max_length=36, db_comment='医嘱ID', verbose_name='医嘱ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

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

    report_id = models.CharField(max_length=36, db_comment="报告ID", unique=True, verbose_name='报告ID')
    title = models.CharField(max_length=36, db_comment="报告单名称", verbose_name='报告单名称')
    exam_no = models.CharField(max_length=36, db_comment="检查号", verbose_name='检查号')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码')
    apply_id = models.CharField(max_length=36, db_comment="申请单id", verbose_name='申请单id')
    gmt_apply = models.DateTimeField(db_comment="申请时间", verbose_name='申请时间')
    apply_dept_code = models.CharField(max_length=36, db_comment="申请科室代码", verbose_name='申请科室代码')
    apply_dept_name = models.CharField(max_length=64, db_comment="申请科室名称", verbose_name='申请科室名称')
    apply_doc_id = models.CharField(max_length=36, db_comment="开单医生id", verbose_name='开单医生id')
    apply_doc = models.CharField(max_length=64, db_comment="开单医生姓名", verbose_name='开单医生姓名')
    item_code = models.CharField(max_length=36, db_comment="项目代码", verbose_name='项目代码')
    item_name = models.CharField(max_length=64, db_comment="项目名称", verbose_name='项目名称')
    item_cls_code = models.CharField(max_length=36, db_comment="大类代码", verbose_name='大类代码',
                                     help_text='江西省口腔医院市互认上传使用', null=True, blank=True)
    item_cls_name = models.CharField(max_length=36, db_comment="大类代码", verbose_name='大类代码',
                                     help_text='江西省口腔医院市互认上传使用', null=True, blank=True)
    extend_code = models.CharField(max_length=36, db_comment="外部项目代码", null=True, blank=True,
                                   verbose_name='江西省口腔医院市互认上传使用')
    extend_name = models.CharField(max_length=64, db_comment="外部项目名称", null=True, blank=True,
                                   verbose_name='江西省口腔医院市互认上传使用')
    checkpoint_id = models.CharField(max_length=36, db_comment="检查部位代码", verbose_name='检查部位代码', null=True,
                                     blank=True)
    checkpoint = models.CharField(max_length=36, db_comment="检查部位", verbose_name='检查部位', null=True, blank=True)
    content = models.CharField(max_length=255, db_comment="检查所见", verbose_name='检查所见')
    url_report_pdf = models.URLField(db_comment="报告pdf链接", verbose_name='报告pdf链接')
    url_image = models.URLField(db_comment="图像查链接", verbose_name='图像查链接', null=True, blank=True)
    dept_id = models.CharField(max_length=36, db_comment="报告科室ID", verbose_name='报告科室ID')
    dept_name = models.CharField(max_length=64, db_comment="报告科室名称", verbose_name='报告科室名称')
    diags = models.CharField(max_length=128, db_comment="临床诊断", verbose_name='临床诊断')
    diags_comment = models.CharField(max_length=128, db_comment="诊断意见", verbose_name='诊断意见')
    comment = models.CharField(max_length=255, db_comment="备注信息或检查提示", verbose_name='备注信息或检查提示',
                               null=True, blank=True)
    exam_category_code = models.CharField(max_length=3, choices=CheckCategoryChoices, db_comment="检查分类代码",
                                          verbose_name='检查分类代码')
    executor_id = models.CharField(max_length=36, db_comment="检查医生ID", verbose_name='检查医生ID')
    executor = models.CharField(max_length=64, db_comment="检查医生姓名", verbose_name='检查医生姓名')
    gmt_execute = models.DateTimeField(db_comment="检查时间", verbose_name='检查时间')
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id')
    author = models.CharField(max_length=64, db_comment="报告人", verbose_name='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间')
    verifier_id = models.CharField(max_length=36, db_comment="审核者ID", verbose_name='审核者ID')
    verifier = models.CharField(max_length=64, db_comment="审核者姓名", verbose_name='审核者姓名')
    gmt_verified = models.DateTimeField(db_comment="审核日期时间", verbose_name='审核日期时间')
    device_id = models.CharField(max_length=36, db_comment="设备唯一id", verbose_name='设备唯一id',
                                 null=True, blank=True)
    device_name = models.CharField(max_length=64, db_comment="设备名称", verbose_name='设备名称', null=True, blank=True)
    extra_infos = models.JSONField(db_comment="补充信息", verbose_name='补充信息', null=True, blank=True)
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

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
        try:
            assert self.gmt_verified >= self.gmt_author, "报告审核日期时间 不能小于 报告日期时间"
            assert self.gmt_author > self.gmt_apply, "报告日期时间 不能小于 申请时间"
            assert all([self.gmt_execute > self.gmt_apply, self.gmt_execute < self.gmt_author]), \
                "检查时间 必须 位于申请时间和报告日期时间之间"
        except AssertionError as e:
            raise ValidationError(message=str(e))


class CheckStatus(models.Model):
    """
    检查状态信息
    """

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

    apply_no = models.CharField(max_length=36, db_comment='申请单号', verbose_name='申请单号')
    gmt_execute = models.DateTimeField(db_comment='操作日期', verbose_name='操作日期')
    executor_id = models.CharField(max_length=36, db_comment='操作人工号', verbose_name='操作人工号')
    executor = models.CharField(max_length=64, db_comment='操作人姓名', verbose_name='操作人姓名')
    dept_id = models.CharField(max_length=36, db_comment='操作科室ID', verbose_name='操作科室ID')
    dept_name = models.CharField(max_length=64, db_comment='操作科室名称', verbose_name='操作科室名称')
    status_code = models.CharField(max_length=4, choices=StatusCodeChoices, db_comment='检查状态代码',
                                   verbose_name="检查状态")
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "检查状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检查状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Discharge(models.Model):
    """
    出院登记信息
    """
    inpatient_id = models.CharField(max_length=36, db_comment='住院号标识', verbose_name='住院号标识')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    adm_no = models.CharField(max_length=36, db_comment='就诊流水号', verbose_name='就诊流水号', unique=True)
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_discharge = models.DateTimeField(blank=True, null=True, db_comment='出院日期时间', verbose_name='出院日期时间')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    discharge_doc_id = models.CharField(max_length=36, blank=True, null=True, db_comment='出院登记的职工号',
                                        verbose_name='出院登记职工号')
    discharge_doc_name = models.CharField(max_length=64, blank=True, null=True, db_comment='出院登记职工姓名',
                                          verbose_name='出院登记职工姓名')
    dept_id = models.CharField(max_length=36, blank=True, null=True, db_comment='出院科室id', verbose_name='出院科室id')
    dept_name = models.CharField(max_length=64, blank=True, null=True, db_comment='出院科室名称',
                                 verbose_name='出院科室名称')
    ward_id = models.CharField(max_length=36, blank=True, null=True, db_comment='出院病区id', verbose_name='出院病区id')
    ward_name = models.CharField(max_length=64, blank=True, null=True, db_comment='出院病区名称',
                                 verbose_name='出院病区名称')

    diags_a = models.JSONField(blank=True, null=True, db_comment='西医诊断', verbose_name='西医诊断')
    diags_b = models.JSONField(blank=True, null=True, db_comment='中医诊断', verbose_name='中医诊断')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "出院登记信息"
        verbose_name_plural = verbose_name
        db_table_comment = '出院登记信息'

        indexes = [
            models.Index(fields=('patient_id',)),
            models.Index(fields=('adm_no',))
        ]


class Exam(models.Model):
    """
    检验申请信息
    """
    apply_no = models.CharField(max_length=36, db_comment='电子申请单编号', unique=True, verbose_name='电子申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单描述',
                                  verbose_name='申请单描述')
    apply_status = models.CharField(max_length=8, blank=True, null=True, db_comment='申请单状态',
                                    verbose_name='申请单状态')
    gmt_effect_high = models.DateTimeField(db_comment='申请单有效日期时间开始', verbose_name='申请单有效日期时间开始')
    gmt_effect_low = models.DateTimeField(db_comment='申请单有效日期时间结束', verbose_name='申请单有效日期时间结束')
    property = models.CharField(max_length=1, choices=PropertyChoices, default='N', db_comment='优先（紧急）度代码',
                                verbose_name='优先（紧急）度代码')
    bar_code = models.CharField(max_length=36, blank=True, null=True, db_comment='条码号', verbose_name='条码号')
    specimen_cls_code = models.CharField(max_length=8, blank=True, null=True, db_comment='标本类别代码',
                                         verbose_name='标本类别代码')
    specimen_cls_name = models.CharField(max_length=36, blank=True, null=True, db_comment='标本类别名称',
                                         verbose_name='标本类别名称')
    gmt_apply = models.DateTimeField(db_comment='开单时间', verbose_name='开单时间')
    doc_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单开立者签名',
                                verbose_name='申请单开立者签名')
    doc_id = models.CharField(max_length=36, db_comment='开单医生编码', verbose_name='开单医生编码')
    doc_name = models.CharField(max_length=64, db_comment='开单医生姓名', verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, db_comment='申请科室编码', verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, db_comment='申请科室名称', verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(db_comment='审核日期时间', verbose_name='审核日期时间')
    reviewer_id = models.CharField(max_length=36, db_comment='审核者编码', verbose_name='审核者编码')
    reviewer = models.CharField(max_length=64, db_comment='审核者姓名', verbose_name='审核者姓名')
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
                             help_text='检验申请原因')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "检验申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检验申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class EncounterCard(models.Model):
    """ 就诊卡信息 """

    class StatusChoices(models.IntegerChoices):
        A = (1, '激活')
        B = (2, '作废')
        C = (3, '退卡')

    card_no = models.CharField(max_length=36, db_comment="就诊卡号", verbose_name='就诊卡号', unique=True)
    gmt_reg = models.DateTimeField(db_comment="患者登记时间", verbose_name='患者登记时间')
    status = models.PositiveSmallIntegerField(choices=StatusChoices, db_comment="就诊卡状态", verbose_name='就诊卡状态',
                                              help_text='1-active-激活;2-作废-diable;3-退卡-retired')
    id_no = models.CharField(max_length=36, db_comment="证件号码", verbose_name='证件号码')
    patient_name = models.CharField(max_length=36, db_comment="患者姓名", verbose_name='患者姓名')
    tel_no = models.CharField(max_length=36, db_comment="联系电话", verbose_name='联系电话')
    sex_code = models.PositiveSmallIntegerField(choices=SexCodeChoices, db_comment="性别代码", verbose_name='性别代码')
    gmt_birth = models.DateField(db_comment="出生日期", verbose_name='出生日期')
    addr_sal = models.CharField(max_length=128, db_comment="完整地址描述", verbose_name='完整地址描述')
    addr_sta = models.CharField(max_length=36, db_comment="自治区、直辖市", verbose_name='自治区、直辖市', null=True,
                                blank=True)
    addr_cty = models.CharField(max_length=36, db_comment="地址-市（地区）", verbose_name='地址-市（地区）', null=True,
                                blank=True)
    addr_cnt = models.CharField(max_length=36, db_comment="地址-县（区）", verbose_name='地址-县（区）', null=True,
                                blank=True)
    addr_stb = models.CharField(max_length=36, db_comment="地址-乡（镇、街道办事处）",
                                verbose_name='地址-乡（镇、街道办事处）', null=True, blank=True)
    addr_str = models.CharField(max_length=36, db_comment="地址-村（街、路、弄等）", verbose_name='地址-村（街、路、弄等）',
                                null=True, blank=True)
    addr_bnr = models.CharField(max_length=36, db_comment="地址-门牌号码", verbose_name='地址-门牌号码', null=True,
                                blank=True)
    addr_zip = models.CharField(max_length=36, db_comment="邮政编码", verbose_name='邮政编码', null=True, blank=True)
    marital_status_code = models.CharField(max_length=2, choices=MaritalStatusCodeChoices, db_comment="婚姻状况代码",
                                           verbose_name='婚姻状况代码')
    ethnic_group_code = models.CharField(max_length=36, db_comment="民族代码", verbose_name='民族代码')
    occupation_code = models.CharField(max_length=36, db_comment="职业类别代码", verbose_name='职业类别代码')
    work_org = models.CharField(max_length=36, db_comment="工作单位", verbose_name='工作单位', null=True, blank=True)
    work_org_tel = models.CharField(max_length=36, db_comment="工作单位联系电话", verbose_name='工作单位联系电话',
                                    null=True, blank=True)
    contact_code = models.CharField(max_length=36, db_comment="联系人关系代码", verbose_name='联系人关系代码')
    contact_tel = models.CharField(max_length=36, db_comment="联系人电话", verbose_name='联系人电话')
    contact_cname = models.CharField(max_length=36, db_comment="联系人姓名", verbose_name='联系人姓名')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="组织机构代码",
                                verbose_name='组织机构代码')
    ins_code = models.CharField(max_length=2, choices=InsCodeChoices, db_comment="医疗保险类别代码",
                                verbose_name='医疗保险类别代码')
    author_id = models.CharField(max_length=36, db_comment="登记人ID", verbose_name='登记人ID')
    author = models.CharField(max_length=64, db_comment="登记人", verbose_name='登记人')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    def __str__(self):
        return f"{self.patient_name}-{self.card_no}"

    class Meta:
        verbose_name = "就诊卡信息"
        verbose_name_plural = verbose_name
        db_table_comment = '就诊卡信息'

        indexes = (
            models.Index(fields=['card_no'], ),
            models.Index(fields=['id_no'], ),
            models.Index(fields=['tel_no'], ),
        )


class ExamReport(models.Model):
    """检验报告"""

    class ExamClsCodeChoices(models.IntegerChoices):
        A = (1, '普通')
        B = (2, '细菌药敏')
        C = (3, '文字描述型结果')

    report_id = models.CharField(max_length=36, db_comment="检验报告ID", unique=True,
                                 verbose_name='检验报告ID')
    title = models.CharField(max_length=36, db_comment="报告单名称", verbose_name='报告单名称')
    bar_code = models.CharField(max_length=18, db_comment="条码号", verbose_name='条码号')
    specimen_id = models.CharField(max_length=18, db_comment="标本id", verbose_name='标本id', null=True, blank=True)
    specimen_name = models.CharField(max_length=18, db_comment="标本名称", verbose_name='标本名称', null=True,
                                     blank=True)
    specimen_cls_code = models.CharField(max_length=18, db_comment="标本类型代码", verbose_name='标本类型代码')
    specimen_cls_name = models.CharField(max_length=18, db_comment="标本类型名称", verbose_name='标本类型名称',
                                         help_text='标本类型名称,eg: 血清,尿液...')
    exam_cls_code = models.PositiveSmallIntegerField(choices=ExamClsCodeChoices, db_comment="检验类型",
                                                     verbose_name='检验类型')
    dept_id = models.CharField(max_length=36, db_comment="报告科室ID", verbose_name='报告科室ID')
    dept_name = models.CharField(max_length=18, db_comment="报告科室", verbose_name='报告科室')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码')
    content = models.CharField(max_length=255, db_comment="检验所见", verbose_name='检验所见', null=True, blank=True)
    comment = models.CharField(max_length=255, db_comment="备注内容", verbose_name='备注内容', null=True, blank=True)
    url_report_pdf = models.URLField(db_comment="报告pdf链接", verbose_name='报告pdf链接')
    device_id = models.CharField(max_length=36, db_comment="设备唯一id", verbose_name='设备唯一id', null=True,
                                 blank=True)
    device_name = models.CharField(max_length=64, db_comment="设备名称", verbose_name='设备名称', null=True, blank=True)
    gmt_collect = models.DateTimeField(db_comment="样本采集时间", verbose_name='样本采集时间')
    gmt_receive = models.DateTimeField(db_comment="样本接收时间", verbose_name='样本接收时间')
    executor_id = models.CharField(max_length=36, db_comment="执行者ID", verbose_name='执行者ID')
    executor = models.CharField(max_length=64, db_comment="执行者姓名", verbose_name='执行者姓名')
    gmt_execute = models.DateTimeField(db_comment="执行日期", verbose_name='执行日期')
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id')
    author = models.CharField(max_length=64, db_comment="报告人", verbose_name='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间')
    reviewer_id = models.CharField(max_length=36, db_comment="复核医生", verbose_name='复核医生')
    reviewer = models.CharField(max_length=64, db_comment="复核医生姓名", verbose_name='复核医生姓名')
    gmt_review = models.DateTimeField(db_comment="复核日期时间", verbose_name='复核日期时间')
    is_other = models.BooleanField(db_comment="第三方检测机构标识", verbose_name='第三方检测机构标识', default=False)
    other_name = models.CharField(max_length=64, db_comment="第三方检测机构名称", verbose_name='第三方检测机构名称',
                                  null=True, blank=True)
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

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
    apply_id = models.CharField(max_length=36, db_comment="申请单id", verbose_name='申请单id')
    order_id = models.CharField(max_length=36, db_comment="医嘱id", verbose_name='医嘱id')
    doc_id = models.CharField(max_length=36, db_comment="申请单医生工号", verbose_name='申请单医生工号')
    doc_name = models.CharField(max_length=64, db_comment="申请单医生姓名", verbose_name='申请单医生姓名')
    dept_id = models.CharField(max_length=36, db_comment="申请单开单科室ID", verbose_name='申请单开单科室ID')
    dept_name = models.CharField(max_length=18, db_comment="申请单开单科室名称", verbose_name='申请单开单科室名称')
    item_code = models.CharField(max_length=36, db_comment="检验项目代码", verbose_name='检验项目代码')
    item_name = models.CharField(max_length=36, db_comment="检验项目名称", verbose_name='检验项目名称')
    item_cls_code = models.CharField(max_length=36, db_comment="检验项目代码", verbose_name='检验项目代码', null=True,
                                     blank=True, help_text='江西省口腔医院市互认上传使用')
    item_cls_name = models.CharField(max_length=64, db_comment="检验项目名称", verbose_name='检验项目名称', null=True,
                                     blank=True, help_text='江西省口腔医院市互认上传使用')
    exam_report_id = models.CharField(max_length=64, db_comment="检验报告", verbose_name='检验报告')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = '检验结果主表'
        verbose_name_plural = '检验结果集合'
        db_table_comment = "检验结果主表"

        indexes = [
            models.Index(fields=['exam_report_id'])
        ]


class ExamResultDetail(models.Model):
    """检验结果明细表"""
    index = models.PositiveIntegerField(db_comment="序号", verbose_name='序号')
    item_code = models.CharField(max_length=36, db_comment="检测项目代码", verbose_name='检测项目代码')
    item_name = models.CharField(max_length=36, db_comment="检测项目", verbose_name='检测项目')
    abbr = models.CharField(max_length=36, db_comment="检测项目缩写", verbose_name='检测项目缩写')
    value = models.CharField(max_length=255, db_comment="结果内容/细菌结果", verbose_name='结果内容/细菌结果')
    unit = models.CharField(max_length=36, db_comment="单位", verbose_name='单位', null=True, blank=True)
    comment = models.CharField(max_length=64, db_comment="提示", verbose_name='提示', null=True, blank=True)
    remarks = models.CharField(max_length=128, db_comment="备注信息", verbose_name='备注信息', null=True, blank=True)
    upper_limit_value = models.CharField(max_length=36, db_comment="参考值上限", verbose_name='参考值上限', null=True,
                                         blank=True)
    lower_limit_value = models.CharField(max_length=36, db_comment="参考值下限", verbose_name='参考值下限', null=True,
                                         blank=True)
    limit_desc = models.CharField(max_length=255, db_comment="参考值描述", verbose_name='参考值描述')
    abnormal_flag_code = models.CharField(max_length=16, db_comment="结果值标志代码", verbose_name='结果值标志代码')
    abnormal_flag_name = models.CharField(max_length=16, db_comment="结果值标志名称", verbose_name='结果值标志名称')
    is_warn = models.BooleanField(default=False, db_comment="危急值标识", verbose_name='危急值标识')
    test_method_code = models.CharField(max_length=36, db_comment="检测方法代码", verbose_name='检测方法代码',
                                        null=True, blank=True)
    test_method_name = models.CharField(max_length=36, db_comment="检测方法名称", verbose_name='检测方法名称',
                                        null=True, blank=True)
    is_germ = models.BooleanField(default=False, db_comment="是否为微生物", verbose_name='是否为微生物')
    bacterium_id = models.CharField(max_length=36, db_comment="细菌id", verbose_name='细菌id', null=True, blank=True)
    bacterium_code = models.CharField(max_length=36, db_comment="细菌代码（用于耐药性和细菌培养）",
                                      verbose_name='细菌代码（用于耐药性和细菌培养）', null=True, blank=True)
    bacterium_name = models.CharField(max_length=36, db_comment="细菌名称", verbose_name='细菌名称', null=True,
                                      blank=True)
    bacterium_abbr = models.CharField(max_length=128, db_comment="细菌名称_英文", verbose_name='细菌名称_英文',
                                      null=True, blank=True)
    bacterium_type_code = models.CharField(max_length=36, db_comment="菌种类型代码", verbose_name='菌种类型代码',
                                           null=True, blank=True)
    bacterium_type_name = models.CharField(max_length=64, db_comment="菌种类型名称", verbose_name='菌种类型名称',
                                           null=True, blank=True)
    extend_code = models.CharField(max_length=36, db_comment="外部项目代码",
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    extend_name = models.CharField(max_length=64, db_comment="外部项目名称",
                                   verbose_name='江西省口腔医院市互认上传使用', null=True, blank=True)
    exam_result_main_id = models.CharField(max_length=64, db_comment="检验结果主表", verbose_name='检验结果主表')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = '检验结果明细表'
        verbose_name_plural = '检验结果明细集合'
        db_table_comment = "检验结果明细表"

        indexes = [
            models.Index(fields=['exam_result_main_id'])
        ]

        constraints = [
            models.UniqueConstraint(fields=['exam_result_main_id', 'index'],
                                    name='unique_exam_result_main_id_index'),
        ]


class ExamResultDetailAST(models.Model):
    """检验结果药敏结果"""
    index = models.PositiveIntegerField(db_comment="序号", verbose_name='序号')
    ast_code = models.CharField(max_length=36, db_comment="药敏代码", verbose_name='药敏代码')
    ast_name = models.CharField(max_length=36, db_comment="药敏名称", verbose_name='药敏名称')
    ast_abbr = models.CharField(max_length=36, db_comment="药敏名称缩写", verbose_name='药敏名称缩写', null=True,
                                blank=True)
    value_qualitative = models.CharField(max_length=64, db_comment="药敏定性结果", verbose_name='药敏定性结果')
    value_qualitative_desc = models.CharField(max_length=64, db_comment="药敏定性结果描述",
                                              verbose_name='药敏定性结果描述')
    value_qualitative_disk = models.CharField(max_length=16, db_comment="药物敏感度", verbose_name='药物敏感度',
                                              null=True,
                                              blank=True)
    value_ration = models.CharField(max_length=16, db_comment="药敏定量结果", verbose_name='药敏定量结果', null=True,
                                    blank=True)
    mic = models.CharField(max_length=16, db_comment="最小抑菌浓度", verbose_name='最小抑菌浓度', null=True, blank=True)
    exam_result_detail_id = models.CharField(max_length=128, db_comment="检验结果明细表", verbose_name='检验结果明细表')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = '检验结果药敏结果'
        verbose_name_plural = '检验结果药敏结果集合'
        db_table_comment = "检验结果药敏结果表"

        indexes = [
            models.Index(fields=['exam_result_detail_id'])
        ]
        constraints = [
            models.UniqueConstraint(fields=['exam_result_detail_id', 'index'],
                                    name='unique_exam_result_detail_id_index'),
        ]


class ExamStatus(models.Model):
    """
    检验状态信息
    """

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
    gmt_execute = models.DateTimeField(db_comment='操作日期时间', verbose_name='操作日期时间')
    status_code = models.CharField(max_length=4, choices=StatusCodeChoices, db_comment='检验状态',
                                   verbose_name='检验状态')
    reason = models.CharField(max_length=128, blank=True, null=True, db_comment='操作描述（如标本拒绝原因）',
                              verbose_name='操作描述', help_text='如标本拒绝原因')
    executor_id = models.CharField(max_length=36, db_comment='操作者代码', verbose_name='操作者代码')
    executor = models.CharField(max_length=64, db_comment='操作者姓名', verbose_name='操作者姓名')
    dept_id = models.CharField(max_length=36, db_comment='操作科室ID', verbose_name='操作科室ID')
    dept_name = models.CharField(max_length=64, db_comment='操作科室名称', verbose_name='操作科室名称')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "检验状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '检验状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class InPatient(models.Model):
    """
    住院就诊信息
    """
    inpatient_id = models.CharField(max_length=36, db_comment='住院号标识', verbose_name='住院号标识')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    adm_no = models.CharField(max_length=36, db_comment='就诊流水号', verbose_name='就诊流水号', unique=True)
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_effect_low = models.DateTimeField(blank=True, null=True, db_comment='入院日期时间', verbose_name='入院日期时间')
    reason = models.CharField(max_length=255, blank=True, null=True, db_comment='就诊原因描述',
                              verbose_name='就诊原因描述')
    ins_code = models.CharField(max_length=2, choices=InsCodeChoices, db_comment='医疗保险类别代码',
                                verbose_name='医疗保险类别代码')
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
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment='服务机构',
                                verbose_name='服务机构')
    diags_a = models.JSONField(blank=True, null=True, db_comment='西医诊断', verbose_name='西医诊断')
    diags_b = models.JSONField(blank=True, null=True, db_comment='中医诊断', verbose_name='中医诊断')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "住院就诊信息"
        verbose_name_plural = verbose_name
        db_table_comment = '住院就诊信息'

        indexes = [
            models.Index(fields=('patient_id',)),
            models.Index(fields=('adm_no',))
        ]


class Operation(models.Model):
    """
    手术申请信息
    """

    class PropertyChoices(models.IntegerChoices):
        A = (1, '择期')
        B = (2, '围期')

    class GradeCodeChoices(models.IntegerChoices):
        A = (1, '一级手术')
        B = (2, '二级手术')
        C = (3, '三级手术')
        D = (4, '四级手术')

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
    grade_code = models.PositiveSmallIntegerField(choices=GradeCodeChoices, db_comment='手术等级编码',
                                                  verbose_name='手术等级编码')
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
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "手术申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OperationSchedule(models.Model):
    """
    手术排班信息
    """
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
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')
    assistants = models.JSONField(blank=True, null=True, db_comment='助手信息', verbose_name='助手信息')

    class Meta:
        verbose_name = "手术排班信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术排班信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OperationStatus(models.Model):
    """
    手术状态信息
    """

    class StatusCodeChoices(models.TextChoices):
        """手术状态"""
        A = (1, '入手术间')
        B = (2, '开始麻醉')
        C = (3, '开始手术')
        D = (4, '结束手术')
        E = (5, '结束麻醉')
        F = (6, '出手术间')
        G = (7, '入复苏室')
        H = (8, '出复苏室')

    apply_no = models.CharField(max_length=36, db_comment='申请单号', verbose_name='手术申请单号')
    gmt_execute = models.DateTimeField(db_comment='操作日期', verbose_name='操作日期')
    executor_id = models.CharField(max_length=36, db_comment='操作人工号', verbose_name='操作人工号')
    executor = models.CharField(max_length=64, db_comment='操作人姓名', verbose_name='操作人姓名')
    execute_dept_id = models.CharField(max_length=36, db_comment='执行科室编码', verbose_name='执行科室编码')
    execute_dept_name = models.CharField(max_length=64, db_comment='执行科室名称', verbose_name='执行科室名称')
    status_code = models.PositiveSmallIntegerField(choices=StatusCodeChoices, db_comment='手术状态编码',
                                                   verbose_name='手术状态编码')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "手术状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '手术状态信息'

        indexes = [
            models.Index(fields=('apply_no',)),
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class OrderFillerStatus(models.Model):
    """ 医嘱执行状态 """

    class ExecuteStatusCodeChoice(models.IntegerChoices):
        """状态"""
        A = (1, '生成医嘱执行档')
        B = (2, '医嘱执行')
        C = (9, '撤消执行')

    order_id = models.CharField(max_length=36, db_comment='医嘱ID', verbose_name='医嘱ID')
    gmt_execute = models.DateTimeField(db_comment='操作日期', verbose_name='操作日期')
    executor_id = models.CharField(max_length=36, db_comment='操作人工号', verbose_name='操作人工号')
    executor = models.CharField(max_length=64, db_comment='操作人姓名', verbose_name='操作人姓名')
    dept_id = models.CharField(max_length=36, db_comment='执行科室编码', verbose_name='执行科室编码')
    dept_name = models.CharField(max_length=64, db_comment='执行科室名称', verbose_name='执行科室名称')
    apply_no = models.CharField(max_length=36, blank=True, null=True, db_comment='申请单号', verbose_name='申请单号')
    item_cls_code = models.PositiveSmallIntegerField(choices=OrderClsCode, db_comment='医嘱类别编码',
                                                     verbose_name='医嘱类别编码')
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
    execute_status_name = models.PositiveSmallIntegerField(choices=ExecuteStatusCodeChoice,
                                                           db_comment='医嘱执行状态名称',
                                                           verbose_name='医嘱执行状态名称')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号',
                              help_text="部分HIS厂商通过patient_id+time确定就诊流水号")
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    @property
    def get_adm_no(self):
        """
        就诊流水号:部分HIS厂商通过patient_id+time确定就诊流水号
        """
        return f"{self.patient_id}_{self.times}"

    class Meta:
        verbose_name = "医嘱执行状态信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医嘱执行状态信息'

        indexes = [
            models.Index(fields=('order_id',)),
            models.Index(fields=('patient_id',)),
            models.Index(fields=('patient_id', 'times')),
        ]


class Order(models.Model):
    """
    医嘱信息
    """

    class ItemClsCode(models.TextChoices):
        """ 医嘱项目类型代码 """
        A = ('01', '药品类医嘱')
        B = ('02', '检查类医嘱')
        C = ('03', '检验类医嘱')
        D = ('04', '手术类医嘱')
        E = ('05', '处置类医嘱')
        F = ('06', '材料类医嘱')
        G = ('07', '嘱托医嘱')
        H = ('08', '输血类医嘱')
        I = ('99', '其他医嘱')

    gmt_order = models.DateTimeField(db_comment='医嘱开立日期时间', verbose_name='医嘱开立日期时间')
    doc_sign = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱开立者签名',
                                verbose_name='医嘱开立者签名')
    doc_id = models.CharField(max_length=36, db_comment='医务人员工号', verbose_name='医务人员工号')
    doc_name = models.CharField(max_length=64, db_comment='医嘱开立者', verbose_name='医嘱开立者')
    dept_id = models.CharField(max_length=36, db_comment='医疗卫生机构（科室）ID', verbose_name='医疗卫生机构（科室）ID')
    dept_name = models.CharField(max_length=64, db_comment='医嘱开立科室', verbose_name='医嘱开立科室')
    gmt_review = models.DateTimeField(db_comment='医嘱审核日期时间', verbose_name='医嘱审核日期时间')
    reviewer_sign = models.CharField(max_length=255, db_comment='医嘱审核者签名', verbose_name='医嘱审核者签名')
    reviewer_id = models.CharField(max_length=36, db_comment='医嘱审核者工号', verbose_name='医嘱审核者工号')
    reviewer = models.CharField(max_length=64, db_comment='医嘱审核者', verbose_name='医嘱审核者')
    index = models.PositiveIntegerField(db_comment='医嘱序号', verbose_name='医嘱序号')
    order_id = models.CharField(db_comment='医嘱ID', verbose_name='医嘱ID', unique=True, max_length=36)
    item_cls_code = models.CharField(max_length=2, choices=ItemClsCode, db_comment='医嘱项目类型代码',
                                     verbose_name='医嘱项目类型代码')
    content = models.CharField(max_length=255, blank=True, null=True, db_comment='医嘱项目内容',
                               verbose_name='医嘱项目内容')
    gmt_effect_high = models.DateTimeField(db_comment='医嘱开始日期时间', verbose_name='医嘱开始日期时间')
    gmt_effect_low = models.DateTimeField(db_comment='医嘱结束日期时间', verbose_name='医嘱结束日期时间')
    rate_execute_code = models.CharField(max_length=8, blank=True, null=True, db_comment='医嘱执行频率编码',
                                         verbose_name='医嘱执行频率编码')
    rate_execute_name = models.CharField(max_length=36, blank=True, null=True, db_comment='医嘱执行频率名称',
                                         verbose_name='医嘱执行频率名称')
    route_code = models.CharField(max_length=3, db_comment='用药途径代码', verbose_name='用药途径代码')
    route_name = models.CharField(max_length=36, db_comment='用药途径名称', verbose_name='用药途径名称')
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
    pre_order_id = models.CharField(max_length=64, blank=True, null=True, db_comment='父医嘱ID',
                                    verbose_name='父医嘱ID', help_text='没有父医嘱可以没有此occurrenceOf节点')
    order_cls_code = models.PositiveSmallIntegerField(choices=OrderClsCode, db_comment='医嘱类别编码',
                                                      verbose_name='医嘱类别编码')
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
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "医嘱信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医嘱信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Organization(models.Model):
    """
    医疗机构信息
    """
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
    author_id = models.CharField(max_length=36, db_comment='申请者医务人员ID', verbose_name="申请者医务人员ID")
    author = models.CharField(max_length=36, db_comment='申请者医务人员姓名', verbose_name="申请者医务人员姓名")
    author_dept_id = models.CharField(max_length=36, db_comment='申请者医务人员科室号标识',
                                      verbose_name="申请者医务人员科室号标识")
    author_dept_name = models.CharField(max_length=64, db_comment='申请者医务人员科室名称',
                                        verbose_name="申请者医务人员科室名称")
    author_dept_contact = models.CharField(max_length=64, db_comment='申请者医务人员科室联系人',
                                           verbose_name="申请者医务人员科室联系人")
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name="来源系统")
    gmt_created = models.DateTimeField(db_comment='申请时间', verbose_name="申请时间")

    class Meta:
        verbose_name = "医疗机构信息"
        verbose_name_plural = verbose_name
        db_table_comment = '医疗机构信息'


class OutpatientAppointStatus(models.Model):
    """
    门诊预约状态
    """

    class BookingCodeChoices(models.TextChoices):
        """预约状态"""
        A = (1, "患者预约")
        B = (9, "取消预约")

    booking_id = models.CharField(max_length=36, db_comment='预约ID', unique=True, verbose_name="预约ID")
    gmt_schedule = models.DateTimeField(db_comment='预约日期时间', verbose_name="预约日期时间")
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    id_no = models.CharField(max_length=36, db_comment='身份证号', verbose_name="身份证号")
    patient_name = models.CharField(max_length=64, db_comment='姓名', verbose_name="姓名")
    gmt_booking = models.DateTimeField(db_comment='系统预约日期时间', verbose_name="系统预约日期时间")
    from_src = models.CharField(max_length=36, db_comment='系统id', verbose_name="系统id")
    booking_code = models.PositiveSmallIntegerField(choices=BookingCodeChoices, db_comment='预约状态代码',
                                                    verbose_name="预约状态代码")
    gmt_operate = models.DateTimeField(db_comment='医务人员预约日期时间', verbose_name="医务人员预约日期时间")
    operator_id = models.CharField(max_length=36, db_comment='医务人员工号', verbose_name="医务人员工号")
    schedule_id = models.CharField(max_length=36, db_comment='资源ID', verbose_name="资源ID")
    gmt_effect_high = models.DateTimeField(db_comment='资源时段开始时间', verbose_name="资源时段开始时间")
    gmt_effect_low = models.DateTimeField(db_comment='资源时段结束时间', verbose_name="资源时段结束时间")
    extra = models.JSONField(db_comment='补充信息', verbose_name="补充信息")
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "门诊预约状态"
        verbose_name_plural = verbose_name
        db_table_comment = '门诊预约状态'

        indexes = [
            models.Index(fields=('patient_id',)),
        ]

    def clean(self):
        try:
            assert self.gmt_effect_high < self.gmt_effect_low, "资源时段开始时间必须小于资源时段结束时间"
        except AssertionError as e:
            raise ValidationError(message=str(e))


class OutPatient(models.Model):
    """
    门诊挂号信息
    """
    gmt_reg = models.DateTimeField(db_comment='挂号时间', verbose_name='挂号时间')
    adm_no = models.CharField(max_length=36, blank=True, null=True, db_comment='就诊流水号', verbose_name='就诊流水号')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    gmt_adm = models.DateTimeField(blank=True, null=True, db_comment='就诊日期时间', verbose_name='就诊日期时间')
    reason = models.CharField(max_length=128, blank=True, null=True, db_comment='就诊原因描述',
                              verbose_name='就诊原因描述')
    ins_cls_code = models.CharField(max_length=2, choices=InsCodeChoices, db_comment='医疗保险类别代码',
                                    verbose_name='医疗保险类别代码')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    doc_id = models.CharField(max_length=36, db_comment='医生的职工号', verbose_name='医生的职工号')
    doc_name = models.CharField(max_length=16, db_comment='责任医师姓名', verbose_name='责任医师姓名')
    dept_id = models.CharField(max_length=36, db_comment='服务场所科室标识', verbose_name='服务场所科室标识')
    dept_name = models.CharField(max_length=64, db_comment='服务场所科室', verbose_name='服务场所科室')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment='服务机构标识',
                                verbose_name='服务机构标识')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')
    extra = models.JSONField(db_comment='补充信息', verbose_name='补充信息')

    class Meta:
        verbose_name = "门诊挂号信息"
        verbose_name_plural = verbose_name
        db_table_comment = '门诊挂号信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Pathology(models.Model):
    """
    病理申请信息
    """
    apply_no = models.CharField(max_length=36, db_comment='检查申请单编号', unique=True, verbose_name='检查申请单编号')
    apply_desc = models.CharField(max_length=255, blank=True, null=True, db_comment='申请单详细内容',
                                  verbose_name='申请单详细内容')
    gmt_effect_low = models.DateTimeField(db_comment='检查申请日期', verbose_name='检查申请日期')
    class_code = models.CharField(max_length=3, choices=CheckCategoryChoices, db_comment='检查类型编码',
                                  verbose_name='检查类型编码')
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
    gmt_apply = models.DateTimeField(db_comment='开单时间', verbose_name='开单时间')
    doc_id = models.CharField(max_length=36, db_comment='开单医生工号', verbose_name='开单医生工号')
    doc_name = models.CharField(max_length=64, db_comment='开单医生姓名', verbose_name='开单医生姓名')
    dept_id = models.CharField(max_length=36, db_comment='申请科室编码', verbose_name='申请科室编码')
    dept_name = models.CharField(max_length=64, db_comment='申请科室名称', verbose_name='申请科室名称')
    gmt_review = models.DateTimeField(blank=True, null=True, db_comment='确认时间', verbose_name='确认时间')
    reviewer_id = models.CharField(max_length=36, db_comment='确认医生工号', verbose_name='确认医生工号')
    reviewer = models.CharField(max_length=64, db_comment='确认人姓名', verbose_name='确认人姓名')
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
    adm_no = models.CharField(max_length=36, db_comment='就诊流水号', verbose_name='就诊流水号')
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "病理申请信息"
        verbose_name_plural = verbose_name
        db_table_comment = '病理申请信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Patient(models.Model):
    """
    患者信息
    """

    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID',
                                  unique=True)
    gmt_reg = models.DateTimeField(db_comment="患者登记时间", verbose_name='患者登记时间')
    id_no = models.CharField(max_length=36, db_comment="证件号码", verbose_name='证件号码')
    id_code = models.CharField(max_length=2, choices=IdCodeChoices, db_comment="证件类型代码",
                               verbose_name='证件类型代码', help_text='来源:身份证件类别代码表(CV02.01.101)')
    patient_name = models.CharField(max_length=36, db_comment="患者姓名", verbose_name='患者姓名')
    tel_no = models.CharField(max_length=36, db_comment="联系电话", verbose_name='联系电话')
    sex_code = models.PositiveSmallIntegerField(choices=SexCodeChoices, db_comment="性别代码", verbose_name='性别代码')
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
    marital_status_code = models.CharField(max_length=2, choices=MaritalStatusCodeChoices, db_comment="婚姻状况代码",
                                           verbose_name='婚姻状况代码')
    ethnic_group_code = models.CharField(max_length=36, db_comment="民族代码", verbose_name='民族代码')
    occupation_code = models.CharField(max_length=36, db_comment="职业类别代码", verbose_name='职业类别代码')
    work_org = models.CharField(max_length=36, db_comment="工作单位", verbose_name='工作单位', null=True, blank=True)
    work_org_tel = models.CharField(max_length=36, db_comment="工作单位联系电话", verbose_name='工作单位联系电话',
                                    null=True, blank=True)
    hcard_no = models.CharField(max_length=36, db_comment="健康卡号", verbose_name='健康卡号', null=True, blank=True)
    hcard_org_code = models.CharField(max_length=18, db_comment="健康卡发放机构代码", verbose_name='健康卡发放机构代码',
                                      choices=FromOrgCodeChoices, null=True, blank=True)
    gcard_no = models.CharField(max_length=36, db_comment="城乡居民健康档案编号", verbose_name='城乡居民健康档案编号',
                                null=True, blank=True)
    gcard_org_code = models.CharField(max_length=36, db_comment="建档医疗机构组织机构代码", choices=FromOrgCodeChoices,
                                      verbose_name='建档医疗机构组织机构代码', null=True, blank=True)
    contact_code = models.CharField(max_length=36, db_comment="联系人关系代码", verbose_name='联系人关系代码')
    contact_tel = models.CharField(max_length=36, db_comment="联系人电话", verbose_name='联系人电话')
    contact_cname = models.CharField(max_length=36, db_comment="联系人姓名", verbose_name='联系人姓名')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="组织机构代码",
                                verbose_name='组织机构代码')
    ins_code = models.CharField(max_length=2, choices=InsCodeChoices, db_comment="医疗保险类别代码",
                                verbose_name='医疗保险类别代码')
    author_id = models.CharField(max_length=36, db_comment="登记人ID", verbose_name='登记人ID')
    author = models.CharField(max_length=64, db_comment="登记人", verbose_name='登记人')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    # empi_id = models.CharField(max_length=36, db_comment="EMPI号", verbose_name='EMPI号', null=True, blank=True)
    # outpatient_id = models.CharField(max_length=36, db_comment="门急诊号标识ID", verbose_name='门急诊号标识ID',
    #                                  help_text="门急诊号标识,对于门诊住院患者不同表情况下使用", null=True, blank=True)
    # inpatient_id = models.CharField(max_length=36, db_comment="住院号", verbose_name='住院号',
    #                                 help_text='住院号标识,对于门诊住院患者不同表情况下使用', null=True, blank=True)
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')
    extra = models.JSONField(db_comment="补充信息", verbose_name='补充信息',
                             help_text="empi_id, outpatient_id, inpatient_id; 如有需要请自行在对应数据库建立索引")

    def __str__(self):
        return f"{self.patient_name}-{self.patient_id}"

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = verbose_name
        db_table_comment = '个人信息'

        indexes = (
            models.Index(fields=['patient_id'], ),
            models.Index(fields=['id_no'], ),
            models.Index(fields=['tel_no'], ),
        )


class Provider(models.Model):
    """
    医疗卫生人员信息
    """
    emp_id = models.CharField(max_length=36, db_comment='医务人员ID', unique=True, verbose_name='医务人员ID')
    emp_name = models.CharField(max_length=64, db_comment='姓名', verbose_name='姓名')
    job_code = models.CharField(max_length=10, db_comment='专业技术职务代码', verbose_name='专业技术职务代码')
    job_name = models.CharField(max_length=64, db_comment='专业技术职务名称', verbose_name='专业技术职务名称')
    gmt_effect_high = models.DateTimeField(db_comment='角色有效期间开始时间', verbose_name='角色有效期间开始时间')
    gmt_effect_low = models.DateTimeField(db_comment='角色有效期间结束时间', verbose_name='角色有效期间结束时间')
    id_no = models.CharField(max_length=32, db_comment='身份证号', verbose_name='身份证号')
    id_code = models.CharField(max_length=2, choices=IdCodeChoices, db_comment='证件代码', verbose_name='证件代码')
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

    def clean(self):
        try:
            assert self.gmt_effect_high < self.gmt_effect_low, "角色有效期间开始必须小于角色有效期间结束时间"
        except AssertionError as e:
            raise ValidationError(message=str(e))


class SourceAndSchedule(models.Model):
    """
    号源排班信息
    """

    class ResourceType(models.IntegerChoices):
        """ 排班资源类型 """
        A = (1, '窗口号源')
        B = (2, '自助机号源')
        C = (3, '互联网号源')
        D = (9, '通用号源')

    schedule_id = models.CharField(max_length=36, db_comment='排班标识', unique=True, verbose_name='排班标识')
    roster_id = models.CharField(max_length=36, db_comment='操作者ID', verbose_name='操作者ID')
    roster = models.CharField(max_length=64, db_comment='操作者', verbose_name='操作者')
    gmt_rostered = models.DateTimeField(db_comment='操作时间', verbose_name='操作时间')
    dept_cls_code = models.CharField(max_length=8, db_comment='医疗卫生机构业务科室分类代码',
                                     verbose_name='医疗卫生机构业务科室分类代码')
    dept_cls_name = models.CharField(max_length=36, db_comment='医疗卫生机构业务科室分类名称',
                                     verbose_name='医疗卫生机构业务科室分类名称')
    total = models.PositiveIntegerField(db_comment='资源总数', verbose_name='资源总数')
    dept_id = models.CharField(max_length=36, db_comment='科室标识', verbose_name='科室标识')
    res_rank_code = models.CharField(max_length=8, db_comment='资源级别代码', verbose_name='资源级别代码')
    res_rank_name = models.CharField(max_length=36, db_comment='资源级别名称', verbose_name='资源级别名称')
    doc_id = models.CharField(max_length=36, db_comment='出诊医生ID', verbose_name='出诊医生ID')
    doc_name = models.CharField(max_length=36, db_comment='出诊医生姓名', verbose_name='出诊医生姓名')
    job_code = models.CharField(max_length=36, db_comment='专业技术职务类别代码', verbose_name='专业技术职务类别代码')
    job_name = models.CharField(max_length=36, db_comment='专业技术职务类别名称', verbose_name='专业技术职务类别名称')
    id_no = models.CharField(max_length=36, db_comment='身份证号', verbose_name='身份证号')
    res_code = models.PositiveSmallIntegerField(choices=ResourceType, db_comment='排班资源类型代码',
                                                verbose_name='排班资源类型代码')
    amount = models.PositiveSmallIntegerField(db_comment='分时段资源总数', verbose_name='分时段资源总数')
    gmt_effect_high = models.DateTimeField(db_comment='排班开始日期时间', verbose_name='排班开始日期时间')
    gmt_effect_low = models.DateTimeField(db_comment='排班结束日期时间', verbose_name='排班结束日期时间')
    remain = models.PositiveSmallIntegerField(db_comment='剩余号数', verbose_name='剩余号数')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "号源排班信息"
        verbose_name_plural = verbose_name
        db_table_comment = '号源排班信息'

    def clean(self):
        try:
            assert self.gmt_effect_high < self.gmt_effect_low, "排班开始日期时间必须小于排班结束日期时间"
        except AssertionError as e:
            raise ValidationError(message=str(e))


class Terminology(models.Model):
    """
    术语信息
    """
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
    extra = models.JSONField(db_comment='补充信息', verbose_name="补充信息", null=True, blank=True)
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "术语信息"
        verbose_name_plural = verbose_name
        db_table_comment = '术语信息'

        indexes = [
            models.Index(fields=('dataset_code',)),
            models.Index(fields=('item_code',)),
        ]

        # 唯一约束
        constraints = [
            models.UniqueConstraint(fields=('dataset_code', 'item_code'), name='unique_dataset_code_item_code'),
        ]


class Transfer(models.Model):
    """
    住院转科信息
    """
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号',
                              help_text="部分厂商为patient_id+times组合成就诊流水号")
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    gmt_in = models.DateTimeField(db_comment='转入日期时间', verbose_name='转入日期时间')
    in_dept_id = models.CharField(max_length=36, db_comment='转入科室id', verbose_name='转入科室id')
    in_dept_name = models.CharField(max_length=64, db_comment='转入科室名称', verbose_name='转入科室名称')
    in_ward_id = models.CharField(max_length=36, db_comment='转入病区id', verbose_name='转入病区id')
    in_ward_name = models.CharField(max_length=64, db_comment='转入病区名称', verbose_name='转入病区名称')
    in_room_id = models.CharField(max_length=36, db_comment='转入病房id', verbose_name='转入病房id')
    in_room_name = models.CharField(max_length=64, db_comment='转入病房名称', verbose_name='转入病房名称')
    in_bed_id = models.CharField(max_length=36, db_comment='转入床号ID', verbose_name='转入床号ID')
    in_bed_name = models.CharField(max_length=64, db_comment='转入床号', verbose_name='转入床号')
    gmt_out = models.DateTimeField(db_comment='转出日期时间', verbose_name='转出日期时间')
    out_dept_id = models.CharField(max_length=36, db_comment='转出科室id', verbose_name='转出科室id')
    out_dept_name = models.CharField(max_length=64, db_comment='转出科室名称', verbose_name='转出科室名称')
    out_ward_id = models.CharField(max_length=36, db_comment='转出病区id', verbose_name='转出病区id')
    out_ward_name = models.CharField(max_length=64, db_comment='转出病区名称', verbose_name='转出病区名称')
    out_room_id = models.CharField(max_length=36, db_comment='转出病房id', verbose_name='转出病房id')
    out_room_name = models.CharField(max_length=64, db_comment='转出病房名称', verbose_name='转出病房名称')
    out_bed_id = models.CharField(max_length=36, db_comment='转出床号ID', verbose_name='转出床号ID')
    out_bed_name = models.CharField(max_length=64, db_comment='转出床号', verbose_name='转出床号')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    class Meta:
        verbose_name = "住院转科信息"
        verbose_name_plural = verbose_name
        db_table_comment = '住院转科信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Diagnosis(models.Model):
    """ 诊断信息 """

    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号',
                              help_text="部分厂商为patient_id+times组合成就诊流水号")
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    diagnosis_id = models.CharField(max_length=36, db_comment="诊断ID", verbose_name='诊断ID', unique=True)
    index = models.PositiveSmallIntegerField(db_comment="诊断排序号", verbose_name='诊断排序号')
    gmt_diag = models.DateTimeField(auto_now_add=True, db_comment='诊断下达时间', verbose_name='诊断下达时间')
    diag_dept_id = models.CharField(max_length=36, db_comment="诊断下达科室唯一标识",
                                    verbose_name='诊断下达科室唯一标识')
    diag_dept_name = models.CharField(max_length=36, db_comment="诊断下达科室名称",
                                      verbose_name='诊断下达科室名称')
    diag_ward_id = models.CharField(max_length=36, db_comment="诊断下达病区唯一标识",
                                    verbose_name='诊断下达病区唯一标识',
                                    null=True, blank=True)
    diag_ward_name = models.CharField(max_length=36, db_comment="诊断下达病区名称", verbose_name='诊断下达病区名称',
                                      null=True, blank=True)
    diag_doctor_id = models.CharField(max_length=36, db_comment="下达诊断的医生唯一标识",
                                      verbose_name='下达诊断的医生唯一标识')
    diag_doctor_name = models.CharField(max_length=36, db_comment="下达诊断的医生姓名",
                                        verbose_name='下达诊断的医生姓名')
    diag_category_code = models.CharField(max_length=36, db_comment="诊断分类代码", verbose_name='诊断分类代码')
    diag_category_name = models.CharField(max_length=36, db_comment="诊断分类名称", verbose_name='诊断分类名称')
    diag_code = models.CharField(max_length=36, db_comment="疾病诊断编码", verbose_name='疾病诊断编码')
    diag_name = models.CharField(max_length=36, db_comment="疾病诊断名称", verbose_name='疾病诊断名称')
    diag_desc = models.CharField(max_length=64, db_comment="诊断描述", verbose_name='诊断描述', null=True, blank=True)
    is_parent = models.BooleanField(default=False, db_comment="是否为父诊断", verbose_name='是否为父诊断')
    parent_id = models.CharField(max_length=36, db_comment="父诊断唯一标识", verbose_name='父诊断唯一标识')
    is_primary = models.BooleanField(default=False, db_comment="主诊标志", verbose_name='主诊标志')
    is_uncertain = models.BooleanField(db_comment="待查标志", verbose_name="待查标志", null=True, blank=True)
    is_infection = models.BooleanField(db_comment="院感标志", verbose_name='院感标志', null=True, blank=True)
    is_infection_report = models.BooleanField(db_comment="院感上报标志", verbose_name='院感上报标志', null=True,
                                              blank=True)
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    def __str__(self):
        return f'{self.adm_no}-{self.patient_id} - {self.diag_name}'

    class Meta:
        verbose_name = "诊断信息"
        verbose_name_plural = verbose_name
        db_table_comment = '诊断信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]


class Visit(models.Model):
    """ 门诊就诊信息 """
    adm_no = models.CharField(max_length=36, db_comment="就诊流水号", verbose_name='就诊流水号',
                              help_text="部分厂商为patient_id+times组合成就诊流水号")
    patient_id = models.CharField(max_length=36, db_comment="患者唯一标识ID", verbose_name='患者唯一标识ID')
    times = models.PositiveIntegerField(db_comment='就诊次数', verbose_name='就诊次数')
    is_first = models.BooleanField(db_comment="初诊标识", verbose_name='初诊标识', default=True)
    dept_id = models.CharField(max_length=10, db_comment="就诊科室ID", verbose_name='就诊科室ID')
    dept_name = models.CharField(max_length=36, db_comment="就诊科室名称", verbose_name='就诊科室名称')
    doctor_id = models.CharField(max_length=10, db_comment="接诊医生ID", verbose_name='接诊医生ID')
    doctor_name = models.CharField(max_length=36, db_comment="接诊医生姓名", verbose_name='接诊医生姓名')
    schedule_id = models.CharField(max_length=36, db_comment="排班ID", verbose_name='排班ID', null=True, blank=True)
    index = models.PositiveSmallIntegerField(db_comment='排队号', verbose_name='排队号', default=1)
    gmt_visit_start = models.DateTimeField(db_comment='接诊开始时间', verbose_name='接诊开始时间')
    gmt_visit_end = models.DateTimeField(db_comment='接诊结束时间', verbose_name='接诊结束时间', null=True, blank=True)
    adm_cls_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                    verbose_name='就诊类别代码')
    org_code = models.CharField(max_length=18, choices=FromOrgCodeChoices, db_comment="医疗卫生机构代码",
                                verbose_name='医疗卫生机构代码')
    from_src = models.CharField(max_length=36, db_comment='来源系统', verbose_name='来源系统')
    gmt_created = models.DateTimeField(auto_now_add=True, db_comment='系统记录时间', verbose_name='系统记录时间')

    def __str__(self):
        return f'{self.adm_no}-{self.patient_id}'

    class Meta:
        verbose_name = "门诊就诊信息"
        verbose_name_plural = verbose_name
        db_table_comment = '门诊就诊信息'

        indexes = [
            models.Index(fields=('adm_no',)),
            models.Index(fields=('patient_id',)),
        ]
