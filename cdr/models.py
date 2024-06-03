from django.db import models


# Create your models here.
class Patient(models.Model):
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
    addr_sta = models.CharField(max_length=36, db_comment="自治区、直辖市", verbose_name='自治区、直辖市', null=True, blank=True)
    addr_cty = models.CharField(max_length=36, db_comment="地址-市（地区）", verbose_name='地址-市（地区）', null=True, blank=True)
    addr_cnt = models.CharField(max_length=36, db_comment="地址-县（区）", verbose_name='地址-县（区）', null=True, blank=True)
    addr_stb = models.CharField(max_length=36, db_comment="地址-乡（镇、街道办事处）", verbose_name='地址-乡（镇、街道办事处）',
                                null=True, blank=True)
    addr_str = models.CharField(max_length=36, db_comment="地址-村（街、路、弄等）", verbose_name='地址-村（街、路、弄等）',
                                null=True, blank=True)
    addr_bnr = models.CharField(max_length=36, db_comment="地址-门牌号码", verbose_name='地址-门牌号码', null=True, blank=True)
    addr_zip = models.CharField(max_length=36, db_comment="邮政编码", verbose_name='邮政编码', null=True, blank=True)
    marital_status_code = models.CharField(max_length=36, db_comment="婚姻状况代码", verbose_name='婚姻状况代码')
    ethnic_group_code = models.CharField(max_length=36, db_comment="民族代码", verbose_name='民族代码')
    occupation_code = models.CharField(max_length=36, db_comment="职业类别代码", verbose_name='职业类别代码')
    work_org = models.CharField(max_length=36, db_comment="工作单位", verbose_name='工作单位', null=True, blank=True)
    work_org_tel = models.CharField(max_length=36, db_comment="工作单位联系电话", verbose_name='工作单位联系电话', null=True,
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
