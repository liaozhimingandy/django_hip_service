from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class AdmCodeChoices(models.IntegerChoices):
    A = (1, '门诊')
    B = (2, '急诊')
    C = (3, '住院')
    D = (4, '体检')
    E = (9, '其他')


# Create your models here.
class Patient(models.Model):
    """患者信息"""
    patient_id = models.CharField(max_length=36, db_comment="Patient ID", help_text="Patient ID", db_index=True,
                                  unique=True)
    gmt_reg = models.DateTimeField(db_comment="患者登记时间", help_text="患者登记时间", verbose_name='患者登记时间')
    id_no = models.CharField(max_length=36, db_comment="证件号码", verbose_name='证件号码')
    id_code = models.CharField(max_length=2, db_comment="证件类型代码", verbose_name='证件类型代码')
    patient_name = models.CharField(max_length=36, db_comment="患者姓名", verbose_name='患者姓名')
    tel_no = models.CharField(max_length=36, db_comment="联系电话", verbose_name='联系电话')
    sex_code = models.CharField(max_length=36, db_comment="性别代码", verbose_name='性别代码')
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
                                      null=True, blank=True)
    gcard_no = models.CharField(max_length=36, db_comment="城乡居民健康档案编号", verbose_name='城乡居民健康档案编号',
                                null=True, blank=True)
    gcard_org_code = models.CharField(max_length=36, db_comment="建档医疗机构组织机构代码",
                                      verbose_name='建档医疗机构组织机构代码', null=True, blank=True)
    contact_code = models.CharField(max_length=36, db_comment="联系人关系代码", verbose_name='联系人关系代码')
    contact_tel = models.CharField(max_length=36, db_comment="联系人电话", verbose_name='联系人电话')
    contact_cname = models.CharField(max_length=36, db_comment="联系人姓名", verbose_name='联系人姓名')
    org_code = models.CharField(max_length=36, db_comment="组织机构代码", verbose_name='组织机构代码')
    org_name = models.CharField(max_length=36, db_comment="组织机构名称", verbose_name='组织机构名称')
    ins_code = models.CharField(max_length=36, db_comment="医疗保险类别代码", verbose_name='医疗保险类别代码')
    author_id = models.CharField(max_length=36, db_comment="登记人ID", verbose_name='登记人ID')
    author = models.CharField(max_length=36, db_comment="登记人", verbose_name='登记人')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统')
    empi = models.CharField(max_length=36, db_comment="EMPI号", verbose_name='EMPI号', null=True, blank=True)
    gmt_updated = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='最后更新时间')

    def __str__(self):
        return f"{self.patient_name}-{self.patient_id}"

    class Meta:
        verbose_name = "患者信息"
        verbose_name_plural = verbose_name


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
    adm_no = models.CharField(max_length=18, db_comment="就诊流水号", verbose_name='就诊流水号', help_text='就诊流水号')
    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码', help_text='就诊类别代码')
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
    executor = models.CharField(max_length=36, db_comment="执行者姓名", verbose_name='执行者姓名',
                                help_text='执行者姓名')
    gmt_execute = models.DateTimeField(db_comment="执行日期", verbose_name='执行日期', help_text='执行日期')
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id', help_text='报告人id')
    author = models.CharField(max_length=36, db_comment="报告人", verbose_name='报告人', help_text='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间', help_text='报告日期时间')
    reviewer_id = models.CharField(max_length=36, db_comment="复核医生", verbose_name='复核医生', help_text='复核医生')
    reviewer = models.CharField(max_length=36, db_comment="复核医生姓名", verbose_name='复核医生姓名',
                                help_text='复核医生姓名')
    gmt_review = models.DateTimeField(db_comment="复核日期时间", verbose_name='复核日期时间', help_text='复核日期时间')
    from_src = models.CharField(max_length=36, db_comment="来源系统", verbose_name='来源系统', help_text='来源系统')
    org_code = models.CharField(max_length=18, db_comment="医疗卫生机构代码", verbose_name='医疗卫生机构代码',
                                help_text='社会统一信用代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构',
                                help_text='医疗卫生机构')


class ExamResultMain(models.Model):
    """检验结果主表"""
    apply_id = models.CharField(max_length=36, db_comment="申请单id", help_text='申请单id', verbose_name='申请单id')
    order_id = models.CharField(max_length=36, db_comment="医嘱id", help_text='医嘱id', verbose_name='医嘱id')
    doc_id = models.CharField(max_length=36, db_comment="申请单医生工号", help_text='申请单医生工号',
                              verbose_name='申请单医生工号')
    doc_name = models.CharField(max_length=36, db_comment="申请单医生姓名", help_text='申请单医生姓名',
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
    item_cls_name = models.CharField(max_length=36, db_comment="检验项目名称", help_text='检验项目名称',
                                     verbose_name='检验项目名称', null=True, blank=True)
    exam_report_id = models.CharField(max_length=36, db_comment="检验报告", help_text='检验报告',
                                      verbose_name='检验报告')


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
                                         verbose_name='参考值上限', null=True,
                                         blank=True)
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
                                      verbose_name='细菌代码（用于耐药性和细菌培养）', null=True, blank=True)
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
                           verbose_name='最小抑菌浓度')
    exam_result_detail_id = models.CharField(max_length=128, db_comment="检验结果明细表",
                                             help_text='检验结果明细表', verbose_name='检验结果明细表')


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
    adm_no = models.CharField(max_length=18, db_comment="就诊流水号", verbose_name='就诊流水号', help_text='就诊流水号')
    adm_code = models.PositiveSmallIntegerField(choices=AdmCodeChoices, db_comment="就诊类别代码",
                                                verbose_name='就诊类别代码', help_text='就诊类别代码')
    apply_id = models.CharField(max_length=36, db_comment="申请单id", verbose_name='申请单id', help_text='申请单id')
    gmt_apply = models.DateTimeField(db_comment="申请时间", verbose_name='申请时间', help_text='申请时间')
    apply_dept_code = models.CharField(max_length=36, db_comment="申请科室代码", verbose_name='申请科室代码',
                                       help_text='申请科室代码')
    apply_dept_name = models.CharField(max_length=36, db_comment="申请科室名称", verbose_name='申请科室名称',
                                       help_text='申请科室名称')
    apply_doc_id = models.CharField(max_length=36, db_comment="开单医生id", verbose_name='开单医生id',
                                    help_text='开单医生id')
    apply_doc = models.CharField(max_length=36, db_comment="开单医生姓名", verbose_name='开单医生姓名',
                                 help_text='开单医生姓名')
    item_code = models.CharField(max_length=36, db_comment="项目代码", verbose_name='项目代码',
                                 help_text='项目代码')
    item_name = models.CharField(max_length=36, db_comment="项目名称", verbose_name='项目名称',
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
    dept_name = models.CharField(max_length=36, db_comment="报告科室名称", help_text='报告科室名称',
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
                                   help_text='检查医生ID', default="")
    executor = models.CharField(max_length=36, db_comment="检查医生姓名", verbose_name='检查医生姓名',
                                help_text='检查医生姓名', default="")
    gmt_execute = models.DateTimeField(db_comment="检查时间", verbose_name='检查时间', help_text='检查时间', default=timezone.now)
    author_id = models.CharField(max_length=36, db_comment="报告人id", verbose_name='报告人id', help_text='报告人id')
    author = models.CharField(max_length=36, db_comment="报告人", verbose_name='报告人', help_text='报告人')
    gmt_author = models.DateTimeField(db_comment="报告日期时间", verbose_name='报告日期时间', help_text='报告日期时间')
    verifier_id = models.CharField(max_length=36, db_comment="审核者ID", verbose_name='审核者ID', help_text='审核者ID')
    verifier = models.CharField(max_length=36, db_comment="审核者姓名", verbose_name='审核者姓名',
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
    org_code = models.CharField(max_length=18, db_comment="医疗卫生机构代码", verbose_name='医疗卫生机构代码',
                                help_text='社会统一信用代码')
    org_name = models.CharField(max_length=64, db_comment="医疗卫生机构", verbose_name='医疗卫生机构')

    def clean(self):
        # 先调用父类的clean方法来执行字段级别的验证
        super().clean()
        # 自定义验证逻辑
        if not any((isinstance(self.extra_infos, dict), self.extra_infos is None)):
            raise ValidationError(message="extra_infos中的值: '%(value)s'必须是一个字典类型或者null",
                                  code='extra_infos_error', params={'value': self.extra_infos})
