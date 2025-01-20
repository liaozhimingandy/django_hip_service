import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Demo(models.Model):
    age = models.PositiveSmallIntegerField(blank=True, null=True, db_comment='年龄',
                                           validators=[MinValueValidator(1), MaxValueValidator(150)])

class SexCodeChoices(models.IntegerChoices):
    """
    性别代码
    """
    A = (0, '未知的性别')
    B = (1, '男性')
    C = (2, '女性')
    D = (9, '未说明的性别')


class BaseModel(models.Model):
    """
    CAD模型公共信息部分
    """

    id = models.AutoField("表主键", primary_key=True, db_comment='表主键')
    gmt_created = models.DateTimeField("记录时间", db_comment='记录创建日期时间', auto_now=True)
    is_finished = models.BooleanField("完成标识", db_comment='文档完成标识,1:已完成生成,0未生成,默认为0', default=False)
    gmt_finish = models.DateTimeField("文档生成日期时间", blank=True, null=True, db_comment='文档生成日期时间')
    doc_id = models.UUIDField("文档流水号", default=uuid.uuid4, db_comment='文档流水号', db_index=True, unique=True)
    adm_no = models.CharField("就诊流水号", max_length=36, db_comment='就诊流水号', db_index=True)
    data_src = models.CharField("数据来源", max_length=32, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        abstract = True


class Position(models.Model):
    """位置模型"""
    dept_id = models.CharField("科室代码", max_length=36, db_comment="科室代码")
    dept_name = models.CharField("科室名称", max_length=36, db_comment="科室名称")
    ward_code = models.CharField("病区代码", max_length=36, db_comment="病区代码", null=True, blank=True)
    ward_name = models.CharField("病区名称", max_length=36, db_comment="病区名称", null=True, blank=True)
    ward_id = models.CharField("病房号id", max_length=36, db_comment="病房号id", null=True, blank=True)
    ward_no = models.CharField("病房号", max_length=36, db_comment="病房号", null=True, blank=True)
    bed_id = models.CharField("病床号Id", max_length=36, db_comment="病床号Id", null=True, blank=True)
    bed_no = models.CharField("病床号", max_length=36, db_comment="病床号", null=True, blank=True)

    class Meta:
        abstract = True


class C0001(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    record_id = models.CharField(db_column='recordId', max_length=100, blank=True, null=True,
                                 db_comment='城乡居民健康档案编号')
    health_id = models.CharField(db_column='healthId', max_length=100, blank=True, null=True,
                                 db_comment='居民健康卡号')
    addrcode = models.CharField(db_column='addrCode', max_length=100, blank=True, null=True,
                                db_comment='地址类别代码')
    state = models.CharField(max_length=100, blank=True, null=True, db_comment='地址-省（自治区、直辖市）')
    city = models.CharField(max_length=100, blank=True, null=True, db_comment='地址-市（地区、州）')
    county = models.CharField(max_length=100, blank=True, null=True, db_comment='地址-县（区）')
    township = models.CharField(max_length=100, blank=True, null=True, db_comment='地址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=100, blank=True, null=True,
                                  db_comment='地址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=100, blank=True, null=True,
                                   db_comment='地址-门牌号码')
    postalcode = models.CharField(db_column='postalCode', max_length=100, blank=True, null=True,
                                  db_comment='邮政编码')
    telecom = models.CharField(max_length=100, blank=True, null=True, db_comment='患者电话号码')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=100, blank=True, null=True,
                                 db_comment='出生日期')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=100, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=100, blank=True, null=True,
                                       db_comment='民族名称')
    employerorgname = models.CharField(db_column='employerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='工作单位名称')
    employerorgtelecom = models.CharField(db_column='employerOrgTelecom', max_length=100, blank=True, null=True,
                                          db_comment='工作单位电话号码')
    occupationcode = models.CharField(db_column='occupationCode', max_length=100, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=100, blank=True, null=True,
                                      db_comment='职业类别名称')
    authortime = models.CharField(db_column='authorTime', max_length=100, blank=True, null=True,
                                  db_comment='建档日期时间')
    assignedpersonid = models.CharField(db_column='assignedPersonId', max_length=100, blank=True, null=True,
                                        db_comment='建档者工号')
    assignedpersonname = models.CharField(db_column='assignedPersonName', max_length=100, blank=True, null=True,
                                          db_comment='建档者姓名')
    authororgid = models.CharField(db_column='authorOrgId', max_length=100, blank=True, null=True,
                                   db_comment='建档医疗机构组织机构代码(建档机构)')
    authororgname = models.CharField(db_column='authorOrgName', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称(建档机构)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=100, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=100, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系名称')
    associatedentitystate = models.CharField(db_column='associatedEntityState', max_length=100, blank=True, null=True,
                                             db_comment='地址-省（自治区、直辖市）')
    associatedentitycity = models.CharField(db_column='associatedEntityCity', max_length=100, blank=True, null=True,
                                            db_comment='地址-市（地区、州）')
    associatedentitycounty = models.CharField(db_column='associatedEntityCounty', max_length=100, blank=True, null=True,
                                              db_comment='地址-县（区）')
    associatedentitytownship = models.CharField(db_column='associatedEntityTownship', max_length=100, blank=True,
                                                null=True,
                                                db_comment='地址-乡（镇、街道办事处）')
    associatedentitystreetname = models.CharField(db_column='associatedEntityStreetName', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='地址-村（街、路、弄等）')
    associatedentityhousenumber = models.CharField(db_column='associatedEntityHouseNumber', max_length=100, blank=True,
                                                   null=True, db_comment='地址-门牌号码')
    associatedentitypostalcode = models.CharField(db_column='associatedEntityPostalCode', max_length=100, blank=True,
                                                  null=True, db_comment='邮政编码')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=100, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=100, blank=True, null=True,
                                            db_comment='联系人姓名')
    abocode = models.CharField(db_column='ABOCode', max_length=100, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=100, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=100, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=100, blank=True, null=True,
                              db_comment='Rh血型名称')
    diseasehistory = models.TextField(db_column='diseaseHistory', blank=True, null=True,
                                      db_comment='疾病史（含外伤）')
    infectioushistory = models.TextField(db_column='infectiousHistory', blank=True, null=True,
                                         db_comment='传染病史')
    surgicalhistory = models.TextField(db_column='surgicalHistory', blank=True, null=True,
                                       db_comment='手术史')
    marriagechildbearinghistory = models.TextField(db_column='marriageChildbearingHistory', blank=True, null=True,
                                                   db_comment='婚育史')
    bloodtransfusionhistory = models.TextField(db_column='bloodTransfusionHistory', blank=True, null=True,
                                               db_comment='输血史')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    vaccinationhistory = models.TextField(db_column='vaccinationHistory', blank=True, null=True,
                                          db_comment='预防接种史')
    personalhistory = models.TextField(db_column='personalHistory', blank=True, null=True,
                                       db_comment='个人史')
    menstrualhistory = models.TextField(db_column='menstrualHistory', blank=True, null=True,
                                        db_comment='月经史')
    familyhistory = models.TextField(db_column='familyHistory', blank=True, null=True,
                                     db_comment='家族史')
    deptname = models.CharField(db_column='deptName', max_length=100, blank=True, null=True,
                                db_comment='医疗机构科室名称')
    visittype = models.CharField(db_column='visitType', max_length=100, blank=True, null=True,
                                 db_comment='患者类型代码')
    patienttypename = models.CharField(db_column='patientTypeName', max_length=100, blank=True, null=True,
                                       db_comment='患者类型名称')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=50, blank=True, null=True,
                                         db_comment='入院日期时间')
    leavedatetime = models.CharField(db_column='leaveDateTime', max_length=50, blank=True, null=True,
                                     db_comment='出院日期时间')
    onsetdatetime = models.CharField(db_column='onsetDateTime', max_length=50, blank=True, null=True,
                                     db_comment='发病日期时间')
    visitdatetime = models.CharField(db_column='visitDateTime', max_length=50, blank=True, null=True,
                                     db_comment='就诊日期时间')
    visitreason = models.CharField(db_column='visitReason', max_length=100, blank=True, null=True,
                                   db_comment='就诊原因')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=100, blank=True, null=True,
                                             db_comment='西医诊断编码')
    westerndiagnosticname = models.CharField(db_column='westernDiagnosticName', max_length=100, blank=True, null=True,
                                             db_comment='西医诊断名称')
    diseaseoutcomecode = models.CharField(db_column='diseaseOutcomeCode', max_length=100, blank=True, null=True,
                                          db_comment='病情转归代码')
    diseaseoutcomename = models.CharField(db_column='diseaseOutcomeName', max_length=100, blank=True, null=True,
                                          db_comment='病情转归名称')
    otherwesterndiagnosticcode = models.CharField(db_column='otherWesternDiagnosticCode', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='其他西医诊断编码')
    otherwesterndiagnosticname = models.CharField(db_column='otherWesternDiagnosticName', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='其他西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=100, blank=True, null=True,
                                      db_comment='中医病名代码')
    tcmdiseasename = models.CharField(db_column='TCMDiseaseName', max_length=100, blank=True, null=True,
                                      db_comment='中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=100, blank=True, null=True,
                                       db_comment='中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=100, blank=True, null=True,
                                       db_comment='中医证候名称')
    cdiseaseoutcomecode = models.CharField(db_column='cdiseaseOutcomeCode', max_length=100, blank=True, null=True,
                                           db_comment='中医病情转归代码')
    cdiseaseoutcomename = models.CharField(db_column='cdiseaseOutcomeName', max_length=100, blank=True, null=True,
                                           db_comment='中医病情转归名称')
    operationcode = models.CharField(db_column='operationCode', max_length=100, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True, null=True,
                                     db_comment='手术及操作名称')
    keydrugname = models.CharField(db_column='keyDrugName', max_length=100, blank=True, null=True,
                                   db_comment='关键药物名称')
    keydrugusage = models.CharField(db_column='keyDrugUsage', max_length=100, blank=True, null=True,
                                    db_comment='关键药物用法')
    adversedrugreactions = models.CharField(db_column='adverseDrugReactions', max_length=100, blank=True, null=True,
                                            db_comment='药物不良反应情况')
    tcmcode = models.CharField(db_column='TCMCode', max_length=100, blank=True, null=True,
                               db_comment='中药使用类别代码')
    tcmname = models.CharField(db_column='TCMName', max_length=100, blank=True, null=True,
                               db_comment='中药使用类别名称')
    othermedicaltreatment = models.CharField(db_column='otherMedicalTreatment', max_length=100, blank=True, null=True,
                                             db_comment='其他医学处置')
    deathcode = models.CharField(db_column='deathCode', max_length=100, blank=True, null=True,
                                 db_comment='根本死因代码')
    deathname = models.CharField(db_column='deathName', max_length=100, blank=True, null=True,
                                 db_comment='根本死因名称')
    responsiblephysicianname = models.CharField(db_column='responsiblePhysicianName', max_length=100, blank=True,
                                                null=True, db_comment='责任医师姓名')
    insurancetypecode = models.CharField(db_column='insuranceTypeCode', max_length=100, blank=True, null=True,
                                         db_comment='医疗保险类别代码')
    insurancetypename = models.CharField(db_column='insuranceTypeName', max_length=100, blank=True, null=True,
                                         db_comment='医疗保险类别名称')
    paymenttypecode = models.CharField(db_column='paymentTypeCode', max_length=100, blank=True, null=True,
                                       db_comment='医疗付费方式代码')
    paymenttypename = models.CharField(db_column='paymentTypeName', max_length=100, blank=True, null=True,
                                       db_comment='医疗付费方式名称')
    outpatientamount = models.DecimalField(db_column='outpatientAmount', max_digits=8, decimal_places=2, blank=True,
                                           null=True, db_comment='门诊费用金额')
    inpatientamount = models.DecimalField(db_column='inpatientAmount', max_digits=10, decimal_places=2, blank=True,
                                          null=True, db_comment='住院费用金额')
    personalamount = models.DecimalField(db_column='personalAmount', max_digits=10, decimal_places=2, blank=True,
                                         null=True, db_comment='个人承担费用金额')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    cacheid = models.BigIntegerField(db_column='CacheID', blank=True, null=True)
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0002(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=20, blank=True, null=True,
                                  db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    deptcode = models.CharField(db_column='deptCode', max_length=50, blank=True, null=True,
                                db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    authororgid = models.CharField(db_column='authorOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码')
    authororgname = models.CharField(db_column='authorOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称')
    visitdatetime = models.CharField(db_column='visitDateTime', max_length=15, blank=True, null=True,
                                     db_comment='就诊日期时间')
    assignedauthorid = models.CharField(db_column='assignedAuthorId', max_length=50, blank=True, null=True,
                                        db_comment='就诊医师工号')
    assignedauthorname = models.CharField(db_column='assignedAuthorName', max_length=50, blank=True, null=True,
                                          db_comment='就诊医师名称')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    assignedentityid = models.CharField(db_column='assignedEntityId', max_length=50, blank=True, null=True,
                                        db_comment='责任医生工号')
    assignedentityname = models.CharField(db_column='assignedEntityName', max_length=50, blank=True, null=True,
                                          db_comment='责任医生签名')
    allergichistoryflag = models.SmallIntegerField(db_column='allergicHistoryFlag', blank=True, null=True,
                                                   db_comment='过敏史标志')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    chiefcomplaint = models.TextField(db_column='chiefComplaint', blank=True, null=True,
                                      db_comment='主诉')
    presentillnesshistory = models.TextField(db_column='presentIllnessHistory', blank=True, null=True,
                                             db_comment='现病史')
    pasthistory = models.TextField(db_column='pastHistory', blank=True, null=True,
                                   db_comment='既往史')
    physicalexamination = models.TextField(db_column='physicalExamination', blank=True, null=True,
                                           db_comment='体格检查')
    auxiliaryinspectionitems = models.CharField(db_column='auxiliaryInspectionItems', max_length=100, blank=True,
                                                null=True, db_comment='辅助检查项目')
    auxiliaryinspectionresults = models.TextField(db_column='auxiliaryInspectionResults', blank=True, null=True,
                                                  db_comment='辅助检查结果')
    firstvisitcode = models.CharField(db_column='firstVisitCode', max_length=20, blank=True, null=True,
                                      db_comment='初诊标志代码')
    firstvisitname = models.CharField(db_column='firstVisitName', max_length=50, blank=True,
                                      null=True)
    observationresults = models.TextField(db_column='observationResults', blank=True, null=True,
                                          db_comment='中医“四诊”观察结果')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=20, blank=True, null=True,
                                             db_comment='初步诊断-西医诊断编码')
    westerndiagnosticname = models.TextField(db_column='westernDiagnosticName', blank=True, null=True,
                                             db_comment='初步诊断-西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=20, blank=True, null=True,
                                      db_comment='初步诊断-中医病名代码')
    tcmdiseasename = models.CharField(db_column='TCMDiseaseName', max_length=50, blank=True, null=True,
                                      db_comment='初步诊断-中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=20, blank=True, null=True,
                                       db_comment='初步诊断-中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='初步诊断-中医证候名称')
    dialecticalbasis = models.CharField(db_column='dialecticalBasis', max_length=100, blank=True, null=True,
                                        db_comment='辨证依据')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    orderitemtype = models.CharField(db_column='orderItemType', max_length=20, blank=True, null=True,
                                     db_comment='医嘱项目类型代码')
    orderitemtypename = models.CharField(db_column='orderItemTypeName', max_length=255, blank=True, null=True,
                                         db_comment='医嘱项目类型名称')
    orderitem = models.CharField(db_column='orderItem', max_length=100, blank=True, null=True,
                                 db_comment='医嘱项目内容')
    effectivetimelow = models.CharField(db_column='effectiveTimeLow', max_length=15, blank=True, null=True,
                                        db_comment='医嘱计划开始日期时间')
    effectivetimehigh = models.CharField(db_column='effectiveTimeHigh', max_length=15, blank=True, null=True,
                                         db_comment='医嘱计划结束日期时间')
    orderplan = models.CharField(db_column='orderPlan', max_length=100, blank=True, null=True,
                                 db_comment='医嘱计划信息')
    orderitemcomments = models.CharField(db_column='orderItemComments', max_length=100, blank=True, null=True,
                                         db_comment='医嘱备注信息')
    orderissuingdeptname = models.CharField(db_column='orderIssuingDeptName', max_length=50, blank=True, null=True,
                                            db_comment='医嘱开立科室')
    orderissuer = models.CharField(db_column='orderIssuer', max_length=50, blank=True, null=True,
                                   db_comment='医嘱开立者签名')
    orderissuingdatetime = models.CharField(db_column='orderIssuingDateTime', max_length=15, blank=True, null=True,
                                            db_comment='医嘱开立日期时间')
    orderreviewer = models.CharField(db_column='orderReviewer', max_length=50, blank=True, null=True,
                                     db_comment='医嘱审核者签名')
    orderreviewdatetime = models.CharField(db_column='orderReviewDateTime', max_length=15, blank=True, null=True,
                                           db_comment='医嘱审核日期时间')
    orderexecdept = models.CharField(db_column='orderExecDept', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行科室')
    orderexecutor = models.CharField(db_column='orderExecutor', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行者签名')
    orderexecdatetime = models.CharField(db_column='orderExecDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医嘱执行日期时间')
    orderexecstatus = models.CharField(db_column='orderExecStatus', max_length=50, blank=True, null=True,
                                       db_comment='医嘱执行状态')
    cancelorderersignature = models.CharField(db_column='cancelOrdererSignature', max_length=50, blank=True, null=True,
                                              db_comment='取消医嘱者签名')
    ordercancellationdatetime = models.CharField(db_column='orderCancellationDateTime', max_length=15, blank=True,
                                                 null=True, db_comment='医嘱取消日期时间')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0003(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    telecom = models.CharField(max_length=20, blank=True, null=True, db_comment='患者电话号码')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    authororgid = models.CharField(db_column='authorOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码')
    authororgname = models.CharField(db_column='authorOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称')
    recorddatetime = models.CharField(db_column='recordDateTime', max_length=15, blank=True, null=True,
                                      db_comment='记录日期时间')
    assignedauthorid = models.CharField(db_column='assignedAuthorId', max_length=50, blank=True, null=True,
                                        db_comment='就诊医师工号')
    assignedauthorname = models.CharField(db_column='assignedAuthorName', max_length=50, blank=True, null=True,
                                          db_comment='就诊医师名称')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    assignedentityid = models.CharField(db_column='assignedEntityId', max_length=50, blank=True, null=True,
                                        db_comment='责任医生工号')
    assignedentityname = models.CharField(db_column='assignedEntityName', max_length=50, blank=True, null=True,
                                          db_comment='责任医生签名')
    allergichistoryflag = models.SmallIntegerField(db_column='allergicHistoryFlag', blank=True, null=True,
                                                   db_comment='过敏史标志')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    presentillnesshistory = models.TextField(db_column='presentIllnessHistory', blank=True, null=True,
                                             db_comment='现病史')
    pasthistory = models.TextField(db_column='pastHistory', blank=True, null=True,
                                   db_comment='既往史')
    physicalexamination = models.TextField(db_column='physicalExamination', blank=True, null=True,
                                           db_comment='体格检查')
    auxiliaryinspectionitems = models.CharField(db_column='auxiliaryInspectionItems', max_length=100, blank=True,
                                                null=True, db_comment='辅助检查项目')
    auxiliaryinspectionresults = models.TextField(db_column='auxiliaryInspectionResults', blank=True, null=True,
                                                  db_comment='辅助检查结果')
    firstvisitcode = models.CharField(db_column='firstVisitCode', max_length=1, blank=True, null=True,
                                      db_comment='初诊标志代码')
    firstvisitname = models.CharField(db_column='firstVisitName', max_length=10, blank=True, null=True,
                                      db_comment='初诊标志名称')
    observationresults = models.TextField(db_column='observationResults', blank=True, null=True,
                                          db_comment='中医“四诊”观察结果')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=11, blank=True, null=True,
                                             db_comment='初步诊断-西医诊断编码')
    westerndiagnosticname = models.CharField(db_column='westernDiagnosticName', max_length=50, blank=True, null=True,
                                             db_comment='初步诊断-西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=9, blank=True, null=True,
                                      db_comment='初步诊断-中医病名代码')
    tcmdiseasename = models.CharField(db_column='TCMDiseaseName', max_length=50, blank=True, null=True,
                                      db_comment='初步诊断-中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=9, blank=True, null=True,
                                       db_comment='初步诊断-中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='初步诊断-中医证候名称')
    dialecticalbasis = models.CharField(db_column='dialecticalBasis', max_length=100, blank=True, null=True,
                                        db_comment='辨证依据')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    orderitemtypecode = models.CharField(db_column='orderItemTypeCode', max_length=1, blank=True, null=True,
                                         db_comment='医嘱项目类型代码')
    orderitemtypename = models.CharField(db_column='orderItemTypeName', max_length=50, blank=True, null=True,
                                         db_comment='医嘱项目类型名称')
    orderitem = models.CharField(db_column='orderItem', max_length=100, blank=True, null=True,
                                 db_comment='医嘱项目内容')
    orderplanenddatetime = models.CharField(db_column='orderPlanEndDateTime', max_length=15, blank=True, null=True,
                                            db_comment='医嘱计划结束日期时间')
    orderplanstartdatetime = models.CharField(db_column='orderPlanStartDateTime', max_length=15, blank=True, null=True,
                                              db_comment='医嘱计划开始日期时间')
    orderitemcomments = models.CharField(db_column='orderItemComments', max_length=100, blank=True, null=True,
                                         db_comment='医嘱备注信息')
    orderissuingdept = models.CharField(db_column='orderIssuingDept', max_length=50, blank=True, null=True,
                                        db_comment='医嘱开立科室')
    orderissuer = models.CharField(db_column='orderIssuer', max_length=50, blank=True, null=True,
                                   db_comment='医嘱开立者签名')
    orderissuerid = models.CharField(db_column='orderIssuerId', max_length=50, blank=True, null=True,
                                     db_comment='医嘱开立者工号')
    orderissuingdatetime = models.CharField(db_column='orderIssuingDateTime', max_length=15, blank=True, null=True,
                                            db_comment='医嘱开立日期时间')
    orderreviewer = models.CharField(db_column='orderReviewer', max_length=50, blank=True, null=True,
                                     db_comment='医嘱审核者签名')
    orderreviewerid = models.CharField(db_column='orderReviewerId', max_length=50, blank=True, null=True,
                                       db_comment='医嘱审核者工号')
    orderreviewdatetime = models.CharField(db_column='orderReviewDateTime', max_length=15, blank=True, null=True,
                                           db_comment='医嘱审核日期时间')
    orderexecdept = models.CharField(db_column='orderExecDept', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行科室')
    orderexecutor = models.CharField(db_column='orderExecutor', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行者签名')
    orderexecutorid = models.CharField(db_column='orderExecutorId', max_length=50, blank=True, null=True,
                                       db_comment='医嘱执行者工号')
    orderexecdatetime = models.CharField(db_column='orderExecDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医嘱执行日期时间')
    orderexecstatus = models.CharField(db_column='orderExecStatus', max_length=50, blank=True, null=True,
                                       db_comment='医嘱执行状态')
    cancelorderersignature = models.CharField(db_column='cancelOrdererSignature', max_length=50, blank=True, null=True,
                                              db_comment='取消医嘱者签名')
    cancelorderersignatureid = models.CharField(db_column='cancelOrdererSignatureId', max_length=50, blank=True,
                                                null=True, db_comment='取消医嘱者工号')
    ordercancellationdatetime = models.CharField(db_column='orderCancellationDateTime', max_length=15, blank=True,
                                                 null=True, db_comment='医嘱取消日期时间')
    operationcode = models.CharField(db_column='operationCode', max_length=5, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=80, blank=True, null=True,
                                     db_comment='手术及操作名称')
    operationtargetsite = models.CharField(db_column='operationTargetSite', max_length=50, blank=True, null=True,
                                           db_comment='手术及操作目标部位名称')
    interventionname = models.CharField(db_column='interventionName', max_length=100, blank=True, null=True,
                                        db_comment='介入物名称')
    operationmethod = models.TextField(db_column='operationMethod', blank=True, null=True,
                                       db_comment='手术及操作方法')
    operationtimes = models.IntegerField(db_column='operationTimes', blank=True, null=True,
                                         db_comment='手术及操作次数')
    rescuestartdatetime = models.CharField(db_column='rescueStartDateTime', max_length=15, blank=True, null=True,
                                           db_comment='抢救开始日期时间')
    rescueenddatetime = models.CharField(db_column='rescueEndDateTime', max_length=15, blank=True, null=True,
                                         db_comment='抢救结束日期时间')
    emergencyrecord = models.TextField(db_column='emergencyRecord', blank=True, null=True,
                                       db_comment='急诊抢救记录')
    listrescuepersonnel = models.CharField(db_column='listreScuePersonnel', max_length=200, blank=True, null=True,
                                           db_comment='参加抢救人员名单')
    technicaljobcode = models.CharField(db_column='technicalJobCode', max_length=1, blank=True, null=True,
                                        db_comment='专业技术职务类别代码')
    technicaljobname = models.CharField(db_column='technicalJobName', max_length=50, blank=True, null=True,
                                        db_comment='专业技术职务类别名称')
    enterobservationroomdatetime = models.CharField(db_column='enterObservationRoomDateTime', max_length=15, blank=True,
                                                    null=True,
                                                    db_comment='收入观察室日期时间（抢救室时间）')
    observationrecord = models.TextField(db_column='observationRecord', blank=True, null=True,
                                         db_comment='急诊留观病程记录')
    note = models.TextField(blank=True, null=True, db_comment='注意事项')
    destinationcode = models.CharField(db_column='destinationCode', max_length=1, blank=True, null=True,
                                       db_comment='患者去向代码')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0004(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    orderid = models.CharField(db_column='orderId', max_length=30, blank=True, null=True,
                               db_comment='处方编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    orderdeptname = models.CharField(db_column='orderDeptName', max_length=50, blank=True, null=True,
                                     db_comment='处方开立科室名称')
    authororgid = models.CharField(db_column='authorOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码')
    authororgname = models.CharField(db_column='authorOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称')
    prescriptionissuedatetime = models.CharField(db_column='prescriptionIssueDatetime', max_length=8, blank=True,
                                                 null=True, db_comment='处方开立日期')
    prescribingphysicianid = models.CharField(db_column='prescribingPhysicianId', max_length=50, blank=True, null=True,
                                              db_comment='处方开立医师工号')
    prescribingphysicianname = models.CharField(db_column='prescribingPhysicianName', max_length=50, blank=True,
                                                null=True, db_comment='处方开立医师签名')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    recipelreviewpharmacistid = models.CharField(db_column='recipelReviewPharmacistId', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='处方审核药剂师工号')
    recipelreviewpharmacistname = models.CharField(db_column='recipelReviewPharmacistName', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='处方审核药剂师签名')
    prescriptionpharmacistid = models.CharField(db_column='prescriptionPharmacistId', max_length=50, blank=True,
                                                null=True,
                                                db_comment='处方调配药剂师工号')
    prescriptionpharmacistname = models.CharField(db_column='prescriptionPharmacistName', max_length=50, blank=True,
                                                  null=True,
                                                  db_comment='处方调配药剂师签名')
    prescriptioncheckpharmacistid = models.CharField(db_column='prescriptionCheckPharmacistId', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='处方核对药剂师工号')
    prescriptioncheckpharmacistname = models.CharField(db_column='prescriptionCheckPharmacistName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='处方核对药剂师签名')
    prescriptiondispensingagentid = models.CharField(db_column='prescriptionDispensingAgentId', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='处方发药药剂师工号')
    prescriptiondispensingagentname = models.CharField(db_column='prescriptionDispensingAgentName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='处方发药药剂师签名')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=20, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    druguseroutecode = models.CharField(db_column='drugUseRouteCode', max_length=20, blank=True, null=True,
                                        db_comment='药物使用途径代码')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=50, blank=True, null=True,
                                        db_comment='药物使用途径名称')
    drugusedose = models.DecimalField(db_column='drugUseDose', max_digits=5, decimal_places=2, blank=True, null=True,
                                      db_comment='药物使用次剂量')
    drugdosageunit = models.CharField(db_column='drugDosageUnit', max_length=6, blank=True, null=True,
                                      db_comment='药物使用剂量单位')
    frequencydruguse = models.CharField(db_column='frequencyDrugUse', max_length=2, blank=True, null=True,
                                        db_comment='药物使用频率')
    frequencydrugunit = models.CharField(db_column='frequencyDrugUnit', max_length=2, blank=True, null=True,
                                         db_comment='药物使用频率单位')
    frequencyusecode = models.CharField(db_column='frequencyUseCode', max_length=20, blank=True, null=True,
                                        db_comment='药物使用频次代码')
    frequencyusename = models.CharField(db_column='frequencyUseName', max_length=50, blank=True, null=True,
                                        db_comment='药物使用频次名称')
    drugdosagecode = models.CharField(db_column='drugDosageCode', max_length=20, blank=True, null=True,
                                      db_comment='药物剂型代码')
    drugdosagename = models.CharField(db_column='drugDosageName', max_length=50, blank=True, null=True,
                                      db_comment='药物剂型名称')
    drugcode = models.CharField(db_column='drugCode', max_length=50, blank=True, null=True,
                                db_comment='药品代码')
    drugname = models.CharField(db_column='drugName', max_length=50, blank=True, null=True,
                                db_comment='药物名称')
    drugspecification = models.CharField(db_column='drugSpecification', max_length=20, blank=True, null=True,
                                         db_comment='药物规格')
    prescriptioneffectivedays = models.IntegerField(db_column='prescriptionEffectiveDays', blank=True, null=True,
                                                    db_comment='处方有效天数')
    totaldrugdose = models.DecimalField(db_column='totalDrugDose', max_digits=12, decimal_places=2, blank=True,
                                        null=True, db_comment='药物使用总剂量')
    prescriptiondrugno = models.CharField(db_column='prescriptionDrugNo', max_length=3, blank=True, null=True,
                                          db_comment='处方药品组号')
    prescriptionnotes = models.CharField(db_column='prescriptionNotes', max_length=100, blank=True, null=True,
                                         db_comment='处方备注信息')
    prescriptiondrugamount = models.DecimalField(db_column='prescriptionDrugAmount', max_digits=8, decimal_places=2,
                                                 blank=True, null=True,
                                                 db_comment='处方药品金额')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0005(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=50, blank=True, null=True, db_comment='门（急）诊号')
    orderid = models.CharField(db_column='orderId', max_length=50, blank=True, null=True,
                               db_comment='处方编号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    orderdeptname = models.CharField(db_column='orderDeptName', max_length=50, blank=True, null=True,
                                     db_comment='处方开立科室名称')
    authororgcode = models.CharField(db_column='authorOrgCode', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码')
    authororgname = models.CharField(db_column='authorOrgName', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称')
    prescriptionissuedatetime = models.CharField(db_column='prescriptionIssueDatetime', max_length=8, blank=True,
                                                 null=True, db_comment='处方开立日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    prescriptionsignaturedatetime = models.CharField(db_column='prescriptionsignatureDateTime', max_length=8,
                                                     blank=True, null=True,
                                                     db_comment='处方签名日期')
    prescribingphysicianid = models.CharField(db_column='prescribingPhysicianId', max_length=50, blank=True, null=True,
                                              db_comment='处方开立医师工号')
    prescribingphysicianname = models.CharField(db_column='prescribingPhysicianName', max_length=50, blank=True,
                                                null=True, db_comment='处方开立医师签名')
    recipelreviewpharmacistid = models.CharField(db_column='recipelReviewPharmacistId', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='处方审核药剂师工号')
    recipelreviewpharmacistname = models.CharField(db_column='recipelReviewPharmacistName', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='处方审核药剂师签名')
    prescriptionpharmacistid = models.CharField(db_column='prescriptionPharmacistId', max_length=50, blank=True,
                                                null=True,
                                                db_comment='处方调配药剂师工号')
    prescriptionpharmacistname = models.CharField(db_column='prescriptionPharmacistName', max_length=50, blank=True,
                                                  null=True,
                                                  db_comment='处方调配药剂师签名')
    prescriptioncheckpharmacistid = models.CharField(db_column='prescriptionCheckPharmacistId', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='处方核对药剂师工号')
    prescriptioncheckpharmacistname = models.CharField(db_column='prescriptionCheckPharmacistName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='处方核对药剂师签名')
    prescriptiondispensingagentid = models.CharField(db_column='prescriptionDispensingAgentId', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='处方发药药剂师工号')
    prescriptiondispensingagentname = models.CharField(db_column='prescriptionDispensingAgentName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='处方发药药剂师签名')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=50, blank=True, null=True,
                                             db_comment='西医诊断编码')
    westerndiagnosticname = models.CharField(db_column='westernDiagnosticName', max_length=50, blank=True, null=True,
                                             db_comment='西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=50, blank=True, null=True,
                                      db_comment='中医病名代码')
    tcmdiseasename = models.CharField(db_column='TCMDiseaseName', max_length=50, blank=True, null=True,
                                      db_comment='中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=50, blank=True, null=True,
                                       db_comment='中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='中医证候名称')
    druguseroutecode = models.CharField(db_column='drugUseRouteCode', max_length=50, blank=True, null=True,
                                        db_comment='药物使用途径代码')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=50, blank=True, null=True,
                                        db_comment='药物使用途径名称')
    drugusedose = models.DecimalField(db_column='drugUseDose', max_digits=5, decimal_places=2, blank=True, null=True,
                                      db_comment='药物使用次剂量')
    drugusedoseunit = models.CharField(db_column='DrugUseDoseUnit', max_length=50, blank=True, null=True,
                                       db_comment='药物使用次剂量单位')
    frequencydruguse = models.CharField(db_column='frequencyDrugUse', max_length=50, blank=True, null=True,
                                        db_comment='药物使用频率')
    frequencyusecode = models.CharField(db_column='frequencyUseCode', max_length=50, blank=True, null=True,
                                        db_comment='药物使用频次代码')
    frequencyusename = models.CharField(db_column='frequencyUseName', max_length=50, blank=True, null=True,
                                        db_comment='药物使用频次名称')
    frequencydrugunit = models.CharField(db_column='frequencyDrugUnit', max_length=50, blank=True, null=True,
                                         db_comment='药物使用频率单位')
    drugdosagecode = models.CharField(db_column='drugDosageCode', max_length=50, blank=True, null=True,
                                      db_comment='药物剂型代码')
    drugdosagename = models.CharField(db_column='drugDosageName', max_length=50, blank=True, null=True,
                                      db_comment='药物剂型名称')
    drugcode = models.CharField(db_column='drugCode', max_length=50, blank=True, null=True,
                                db_comment='药品代码')
    drugname = models.CharField(db_column='drugName', max_length=50, blank=True, null=True,
                                db_comment='药物名称')
    drugspecification = models.CharField(db_column='drugSpecification', max_length=50, blank=True, null=True,
                                         db_comment='药物规格')
    totaldrugdose = models.DecimalField(db_column='totalDrugDose', max_digits=12, decimal_places=2, blank=True,
                                        null=True, db_comment='药物使用总剂量')
    totaldrugusedoseunit = models.CharField(db_column='totalDrugUseDoseUnit', max_length=50, blank=True, null=True,
                                            db_comment='药物使用总剂量使用的单位')
    prescriptioneffectivedays = models.IntegerField(db_column='prescriptionEffectiveDays', blank=True, null=True,
                                                    db_comment='处方有效天数')
    prescriptiondrugno = models.CharField(db_column='prescriptionDrugNo', max_length=50, blank=True, null=True,
                                          db_comment='处方药品组号')
    tcmprescriptiondesc = models.TextField(db_column='TCMPrescriptionDesc', blank=True, null=True,
                                           db_comment='中药饮片处方')
    tcmnumber = models.IntegerField(db_column='TCMNumber', blank=True, null=True,
                                    db_comment='中药饮片剂数（剂）')
    tcmdecoctingmethod = models.CharField(db_column='TCMDecoctingMethod', max_length=100, blank=True, null=True,
                                          db_comment='中药饮片煎煮法')
    tcmmethods = models.CharField(db_column='TCMMethods', max_length=100, blank=True, null=True,
                                  db_comment='中药用药方法')
    prescriptiontypecode = models.CharField(db_column='prescriptionTypeCode', max_length=50, blank=True, null=True,
                                            db_comment='处方类别代码')
    prescriptiontypename = models.CharField(db_column='prescriptionTypeName', max_length=50, blank=True, null=True,
                                            db_comment='处方类别名称')
    prescriptiondrugamount = models.DecimalField(db_column='prescriptionDrugAmount', max_digits=8, decimal_places=2,
                                                 blank=True, null=True,
                                                 db_comment='处方药品金额')
    prescriptionnotes = models.CharField(db_column='prescriptionNotes', max_length=100, blank=True, null=True,
                                         db_comment='处方备注信息')
    treatmentmethods = models.CharField(db_column='treatmentMethods', max_length=100, blank=True, null=True,
                                        db_comment='治则治法')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0006(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    examreportno = models.CharField(db_column='examReportNo', max_length=100, blank=True, null=True,
                                    db_comment='检查报告单编号')
    applyid = models.CharField(db_column='applyId', max_length=100, blank=True, null=True,
                               db_comment='电子申请单编号')
    sampleno = models.CharField(db_column='sampleNo', max_length=100, blank=True, null=True,
                                db_comment='检查标本号')
    patienttypecode = models.CharField(db_column='patientTypeCode', max_length=100, blank=True, null=True,
                                       db_comment='患者类型代码')
    patienttypename = models.CharField(db_column='patientTypeName', max_length=100, blank=True, null=True,
                                       db_comment='患者类型名称')
    telecom = models.CharField(max_length=100, blank=True, null=True, db_comment='电话号码')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    age = models.CharField(max_length=100, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    reportdate = models.CharField(db_column='reportDate', max_length=8, blank=True, null=True,
                                  db_comment='检查报告日期')
    reportingphysicianid = models.CharField(db_column='reportingPhysicianId', max_length=100, blank=True, null=True,
                                            db_comment='报告医师工号')
    reportingphysicianname = models.CharField(db_column='reportingPhysicianName', max_length=100, blank=True, null=True,
                                              db_comment='报告医师签名')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    auditphysicianid = models.CharField(db_column='auditPhysicianId', max_length=100, blank=True, null=True,
                                        db_comment='审核医师工号')
    auditphysicianname = models.CharField(db_column='auditPhysicianName', max_length=100, blank=True, null=True,
                                          db_comment='审核医师签名')
    checktechnicianid = models.CharField(db_column='checkTechnicianId', max_length=100, blank=True, null=True,
                                         db_comment='检查技师工号')
    checktechnicianname = models.CharField(db_column='checkTechnicianName', max_length=100, blank=True, null=True,
                                           db_comment='检查技师签名')
    examphysicianid = models.CharField(db_column='examPhysicianId', max_length=100, blank=True, null=True,
                                       db_comment='检查医师工号')
    examphysicianname = models.CharField(db_column='examPhysicianName', max_length=100, blank=True, null=True,
                                         db_comment='检查医师签名')
    examapplydeptcode = models.CharField(db_column='examApplyDeptCode', max_length=100, blank=True, null=True,
                                         db_comment='检查申请科室代码')
    examapplydeptname = models.CharField(db_column='examApplyDeptName', max_length=100, blank=True, null=True,
                                         db_comment='检查申请科室名称')
    examapplyorgid = models.CharField(db_column='examApplyOrgId', max_length=100, blank=True, null=True,
                                      db_comment='检查申请机构代码')
    examapplyorgname = models.CharField(db_column='examApplyOrgName', max_length=100, blank=True, null=True,
                                        db_comment='检查申请机构名称')
    deptid = models.CharField(db_column='deptId', max_length=100, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=100, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=100, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=100, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=100, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=100, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    diagnosisdate = models.CharField(db_column='diagnosisDate', max_length=8, blank=True, null=True,
                                     db_comment='诊断日期')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=100, blank=True, null=True,
                                            db_comment='诊断代码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=100, blank=True, null=True,
                                            db_comment='诊断名称')
    diagnoseorgid = models.CharField(db_column='diagnoseOrgId', max_length=100, blank=True, null=True,
                                     db_comment='诊断机构代码')
    diagnoseorgname = models.CharField(db_column='diagnoseOrgName', max_length=100, blank=True, null=True,
                                       db_comment='诊断机构名称')
    chiefcomplaint = models.TextField(db_column='chiefComplaint', blank=True, null=True,
                                      db_comment='主诉')
    symptomstartdatetime = models.CharField(db_column='symptomStartDateTime', max_length=15, blank=True, null=True,
                                            db_comment='症状开始日期时间')
    symptomenddatetime = models.CharField(db_column='symptomEndDateTime', max_length=15, blank=True, null=True,
                                          db_comment='症状停止日期时间')
    symptomdesc = models.TextField(db_column='symptomDesc', blank=True, null=True,
                                   db_comment='症状描述')
    operationcode = models.CharField(db_column='operationCode', max_length=100, blank=True, null=True,
                                     db_comment='操作编码')
    operationname = models.TextField(db_column='operationName', blank=True, null=True,
                                     db_comment='操作名称')
    operationdatetime = models.CharField(db_column='operationDateTime', max_length=15, blank=True, null=True,
                                         db_comment='操作日期时间')
    operationpositioncode = models.CharField(db_column='operationPositionCode', max_length=200, blank=True, null=True,
                                             db_comment='操作部位编码')
    interventionname = models.CharField(db_column='interventionName', max_length=200, blank=True, null=True,
                                        db_comment='介入物名称')
    operationmethoddesc = models.TextField(db_column='operationMethodDesc', blank=True, null=True,
                                           db_comment='操作方法描述')
    operationtimes = models.IntegerField(db_column='operationTimes', blank=True, null=True,
                                         db_comment='操作次数')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=100, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=100, blank=True, null=True,
                                            db_comment='麻醉方法名称')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=100, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignature = models.CharField(db_column='anesthesiologistSignature', max_length=100, blank=True,
                                                 null=True, db_comment='麻醉医师签名')
    anesthesiaobservationresult = models.TextField(db_column='anesthesiaObservationResult', blank=True, null=True,
                                                   db_comment='麻醉观察结果')
    anesthesiacwcode = models.CharField(db_column='anesthesiaCWCode', max_length=100, blank=True, null=True,
                                        db_comment='麻醉中西医标识代码')
    anesthesiacwname = models.CharField(db_column='anesthesiaCWName', max_length=100, blank=True, null=True,
                                        db_comment='麻醉中西医标识名称')
    specialexamflag = models.CharField(db_column='specialExamFlag', max_length=8, blank=True, null=True,
                                       db_comment='特殊检查标志')
    exammethodname = models.CharField(db_column='examMethodName', max_length=100, blank=True, null=True,
                                      db_comment='检查方法名称')
    examclass = models.CharField(db_column='examClass', max_length=100, blank=True, null=True,
                                 db_comment='检查类别')
    examdate = models.CharField(db_column='examDate', max_length=8, blank=True, null=True,
                                db_comment='检查日期')
    examitemcode = models.CharField(db_column='examItemCode', max_length=100, blank=True, null=True,
                                    db_comment='检查项目代码')
    specimentakedatetime = models.CharField(db_column='specimenTakeDateTime', max_length=15, blank=True, null=True,
                                            db_comment='标本采样日期时间')
    specimenrcvdatetime = models.CharField(db_column='specimenRcvDateTime', max_length=15, blank=True, null=True,
                                           db_comment='接收标本日期时间')
    specimenclass = models.CharField(db_column='specimenClass', max_length=100, blank=True, null=True,
                                     db_comment='标本类别')
    specimenstatus = models.CharField(db_column='specimenStatus', max_length=100, blank=True, null=True,
                                      db_comment='标本状态')
    specimenfixsolutionname = models.CharField(db_column='specimenFixSolutionName', max_length=100, blank=True,
                                               null=True, db_comment='标本固定液名称')
    examresultcode = models.CharField(db_column='examResultCode', max_length=100, blank=True, null=True,
                                      db_comment='检查结果代码')
    examresultname = models.CharField(db_column='examResultName', max_length=100, blank=True, null=True,
                                      db_comment='检查结果名称')
    examquantitativeresult = models.DecimalField(db_column='examQuantitativeResult', max_digits=14, decimal_places=4,
                                                 blank=True, null=True,
                                                 db_comment='检查定量结果')
    examquantitativeresultunit = models.CharField(db_column='examQuantitativeResultUnit', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='检查定量结果计量单位')
    examprocessdesc = models.TextField(db_column='examProcessDesc', blank=True, null=True,
                                       db_comment='诊疗过程描述')
    examreportresultobj = models.TextField(db_column='examReportResultObj', blank=True, null=True,
                                           db_comment='检查报告结果-客观所见')
    examreportresultsub = models.TextField(db_column='examReportResultSub', blank=True, null=True,
                                           db_comment='检查报告结果-主观提示')
    examreportdept = models.CharField(db_column='examReportDept', max_length=100, blank=True, null=True,
                                      db_comment='检查报告科室')
    examreportorg = models.CharField(db_column='examReportOrg', max_length=100, blank=True, null=True,
                                     db_comment='检查报告机构名称')
    examreportnotes = models.TextField(db_column='examReportNotes', blank=True, null=True,
                                       db_comment='检查报告备注')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    cacheid = models.BigIntegerField(db_column='CacheID', blank=True, null=True)
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    examitemname = models.CharField(db_column='examItemName', max_length=255, blank=True, null=True,
                                    db_comment='检查项目名称')
    gmt_created = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, blank=True, null=True,
                                db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0007(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    examreportno = models.CharField(db_column='examReportNo', max_length=100, blank=True, null=True,
                                    db_comment='检验报告单编号')
    applyid = models.CharField(db_column='applyId', max_length=100, blank=True, null=True,
                               db_comment='电子申请单编号')
    sampleno = models.CharField(db_column='sampleNo', max_length=100, blank=True, null=True,
                                db_comment='检验标本号')
    patienttypecode = models.CharField(db_column='patientTypeCode', max_length=100, blank=True, null=True,
                                       db_comment='患者类型代码')
    patienttypename = models.CharField(db_column='patientTypeName', max_length=100, blank=True, null=True,
                                       db_comment='患者类型名称')
    telecom = models.CharField(max_length=100, blank=True, null=True, db_comment='电话号码')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    labreportdate = models.CharField(db_column='labReportDate', max_length=8, blank=True, null=True,
                                     db_comment='检验报告日期')
    reportingphysicianid = models.CharField(db_column='reportingPhysicianId', max_length=100, blank=True, null=True,
                                            db_comment='报告医师工号')
    reportingphysicianname = models.CharField(db_column='reportingPhysicianName', max_length=100, blank=True, null=True,
                                              db_comment='报告医师签名')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    auditphysicianid = models.CharField(db_column='auditPhysicianId', max_length=100, blank=True, null=True,
                                        db_comment='审核医师工号')
    auditphysicianname = models.CharField(db_column='auditPhysicianName', max_length=100, blank=True, null=True,
                                          db_comment='审核医师签名')
    labtechnicianid = models.CharField(db_column='labTechnicianId', max_length=100, blank=True, null=True,
                                       db_comment='检验技师工号')
    labtechnicianname = models.CharField(db_column='labTechnicianName', max_length=100, blank=True, null=True,
                                         db_comment='检验技师签名')
    labphysicianid = models.CharField(db_column='labPhysicianId', max_length=100, blank=True, null=True,
                                      db_comment='检验医师工号')
    labphysicianname = models.CharField(db_column='labPhysicianName', max_length=100, blank=True, null=True,
                                        db_comment='检验医师签名')
    labapplydeptcode = models.CharField(db_column='labApplyDeptCode', max_length=100, blank=True, null=True,
                                        db_comment='检验申请科室代码')
    labapplydeptname = models.CharField(db_column='labApplyDeptName', max_length=100, blank=True, null=True,
                                        db_comment='检验申请科室名称')
    labapplyorgid = models.CharField(db_column='labApplyOrgId', max_length=100, blank=True, null=True,
                                     db_comment='检验申请机构代码')
    labapplyorgname = models.CharField(db_column='labApplyOrgName', max_length=100, blank=True, null=True,
                                       db_comment='检验申请机构名称')
    deptid = models.CharField(db_column='deptId', max_length=100, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=100, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=100, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=100, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=100, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=100, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    diagnosisdate = models.CharField(db_column='diagnosisDate', max_length=8, blank=True, null=True,
                                     db_comment='诊断日期')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=100, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=100, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    diagnoseorgid = models.CharField(db_column='diagnoseOrgId', max_length=100, blank=True, null=True,
                                     db_comment='诊断机构代码')
    diagnoseorgname = models.CharField(db_column='diagnoseOrgName', max_length=100, blank=True, null=True,
                                       db_comment='诊断机构名称')
    labmethodname = models.CharField(db_column='labMethodName', max_length=100, blank=True, null=True,
                                     db_comment='检验方法名称')
    labclass = models.CharField(db_column='labClass', max_length=100, blank=True, null=True,
                                db_comment='检验类别')
    labdate = models.CharField(db_column='labDate', max_length=8, blank=True, null=True,
                               db_comment='检验日期')
    labitemcode = models.CharField(db_column='labItemCode', max_length=100, blank=True, null=True,
                                   db_comment='检验项目代码')
    specimentakedatetime = models.CharField(db_column='specimenTakeDateTime', max_length=15, blank=True, null=True,
                                            db_comment='标本采样日期时间')
    specimenrcvdatetime = models.CharField(db_column='specimenRcvDateTime', max_length=15, blank=True, null=True,
                                           db_comment='接收标本日期时间')
    specimenclass = models.CharField(db_column='specimenClass', max_length=100, blank=True, null=True,
                                     db_comment='标本类别')
    specimenstatus = models.CharField(db_column='specimenStatus', max_length=100, blank=True, null=True,
                                      db_comment='标本状态')
    labresultcode = models.CharField(db_column='labResultCode', max_length=100, blank=True, null=True,
                                     db_comment='检验结果代码')
    labresultname = models.CharField(db_column='labResultName', max_length=100, blank=True, null=True,
                                     db_comment='检验结果名称')
    labquantitativeresult = models.CharField(db_column='labQuantitativeResult', max_length=200, blank=True, null=True,
                                             db_comment='检验定量结果')
    labquantitativeresultunit = models.CharField(db_column='labQuantitativeResultUnit', max_length=100, blank=True,
                                                 null=True,
                                                 db_comment='检验定量结果计量单位')
    labreportresult = models.CharField(db_column='labReportResult', max_length=200, blank=True, null=True,
                                       db_comment='检验报告结果')
    labreportdept = models.CharField(db_column='labReportDept', max_length=100, blank=True, null=True,
                                     db_comment='检验报告科室名称')
    labreportorg = models.CharField(db_column='labReportOrg', max_length=100, blank=True, null=True,
                                    db_comment='检验报告机构名称')
    labreportnotes = models.CharField(db_column='labReportNotes', max_length=100, blank=True, null=True,
                                      db_comment='检验报告备注')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, blank=True, null=True,
                                db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0007Detail(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True)
    labitemcode = models.CharField(db_column='labItemCode', max_length=50, blank=True,
                                   null=True)
    labitemname = models.CharField(db_column='labItemName', max_length=200, blank=True,
                                   null=True)
    labresultcode = models.CharField(db_column='labResultCode', max_length=10, blank=True,
                                     null=True)
    labresultname = models.CharField(db_column='labResultName', max_length=20, blank=True,
                                     null=True)
    labquantitativeresult = models.CharField(db_column='labQuantitativeResult', max_length=200, blank=True,
                                             null=True)
    labquantitativeresultunit = models.CharField(db_column='labQuantitativeResultUnit', max_length=20, blank=True,
                                                 null=True)
    labreportresult = models.CharField(db_column='labReportResult', max_length=200, blank=True,
                                       null=True)
    labreportnotes = models.TextField(db_column='labReportNotes', blank=True, null=True)
    create_datetime = models.DateTimeField(blank=True, null=True)
    tid = models.BigIntegerField(primary_key=True)

    class Meta:
        db_table_comment = '检验明细表'


class C0008(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=50, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=50, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=50, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    orderexecid = models.CharField(db_column='orderExecId', max_length=50, blank=True, null=True,
                                   db_comment='医嘱执行者工号')
    orderexecname = models.CharField(db_column='orderExecName', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行者签名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=50, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=50, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    diagnosistreatmentflag = models.SmallIntegerField(db_column='diagnosisTreatmentFlag', blank=True, null=True,
                                                      db_comment='有创诊疗操作标志')
    allergichistoryflag = models.SmallIntegerField(db_column='allergicHistoryFlag', blank=True, null=True,
                                                   db_comment='过敏史标志')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    handlingguidance = models.TextField(db_column='handlingGuidance', blank=True, null=True,
                                        db_comment='处理及指导意见')
    orderusenotes = models.CharField(db_column='orderUseNotes', max_length=100, blank=True, null=True,
                                     db_comment='医嘱使用备注')
    futuretreatmentoptions = models.TextField(db_column='futureTreatmentOptions', blank=True, null=True,
                                              db_comment='今后治疗方案')
    followupdate = models.CharField(db_column='followUpDate', max_length=50, blank=True, null=True,
                                    db_comment='随访日期')
    followupmodecode = models.CharField(db_column='followUpModeCode', max_length=50, blank=True, null=True,
                                        db_comment='随访方式代码')
    followupmodename = models.CharField(db_column='followUpModeName', max_length=50, blank=True, null=True,
                                        db_comment='随访方式名称')
    followupcycleadvisecode = models.CharField(db_column='followUpCycleAdviseCode', max_length=50, blank=True,
                                               null=True, db_comment='随访周期建议代码')
    followupcycleadvisename = models.CharField(db_column='followUpCycleAdviseName', max_length=50, blank=True,
                                               null=True, db_comment='随访周期建议名称')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='操作编码')
    operationname = models.CharField(db_column='operationName', max_length=80, blank=True, null=True,
                                     db_comment='操作名称')
    operationdatetime = models.CharField(db_column='operationDateTime', max_length=15, blank=True, null=True,
                                         db_comment='操作日期时间')
    operationpositioncode = models.CharField(db_column='operationPositionCode', max_length=50, blank=True, null=True,
                                             db_comment='操作目标部位名称')
    interventionname = models.CharField(db_column='interventionName', max_length=100, blank=True, null=True,
                                        db_comment='介入物名称')
    operationmethoddesc = models.TextField(db_column='operationMethodDesc', blank=True, null=True,
                                           db_comment='操作方法描述')
    operationtimes = models.IntegerField(db_column='operationTimes', blank=True, null=True,
                                         db_comment='操作次数')
    druguseroutecode = models.CharField(db_column='drugUseRouteCode', max_length=50, blank=True, null=True,
                                        db_comment='药物使用途径代码')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=100, blank=True, null=True,
                                        db_comment='药物使用途径名称')
    drugusedose = models.DecimalField(db_column='DrugUseDose', max_digits=5, decimal_places=2, blank=True, null=True,
                                      db_comment='药物使用次剂量')
    drugusedoseunit = models.CharField(db_column='DrugUseDoseUnit', max_length=50, blank=True, null=True,
                                       db_comment='药物使用次剂量单位')
    drugcode = models.CharField(db_column='drugCode', max_length=50, blank=True, null=True,
                                db_comment='药品代码')
    drugname = models.CharField(db_column='drugName', max_length=50, blank=True, null=True,
                                db_comment='药物名称')
    drugusage = models.CharField(db_column='drugUsage', max_length=100, blank=True, null=True,
                                 db_comment='药物用法')
    tcmcode = models.CharField(db_column='TCMCode', max_length=50, blank=True, null=True,
                               db_comment='中药使用类别代码')
    tcmname = models.CharField(db_column='TCMName', max_length=50, blank=True, null=True,
                               db_comment='中药使用类别名称')
    frequencydruguse = models.CharField(db_column='frequencyDrugUse', max_length=50, blank=True, null=True,
                                        db_comment='药物使用频率')
    frequencydrugcode = models.CharField(db_column='frequencyDrugCode', max_length=50, blank=True, null=True,
                                         db_comment='药物使用频率代码')
    drugdosagecode = models.CharField(db_column='drugDosageCode', max_length=50, blank=True, null=True,
                                      db_comment='药物剂型代码')
    drugdosagename = models.CharField(db_column='drugDosageName', max_length=50, blank=True, null=True,
                                      db_comment='药物剂型名称')
    drugdosageunit = models.CharField(db_column='drugDosageUnit', max_length=50, blank=True, null=True,
                                      db_comment='药物使用剂量单位')
    totaldrugusedose = models.DecimalField(db_column='totalDrugUseDose', max_digits=12, decimal_places=2, blank=True,
                                           null=True, db_comment='药物使用总剂量')
    totaldrugusedoseunit = models.CharField(db_column='totalDrugUseDoseUnit', max_length=50, blank=True, null=True,
                                            db_comment='药物使用总剂量单位')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0009(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=50, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=50, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    surgeonsignatureid = models.CharField(db_column='surgeonSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='手术者签名工号')
    surgeonsignaturename = models.CharField(db_column='surgeonSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='手术者签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=50, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=50, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    surgicalhistoryflag = models.SmallIntegerField(db_column='surgicalHistoryFlag', blank=True, null=True,
                                                   db_comment='手术史标志')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationstartdatetime = models.CharField(db_column='operationStartDateTime', max_length=15, blank=True, null=True,
                                              db_comment='手术开始日期时间')
    operationenddatetime = models.CharField(db_column='operationEndDateTime', max_length=15, blank=True, null=True,
                                            db_comment='手术结束日期时间')
    surgeonid = models.CharField(db_column='surgeonId', max_length=50, blank=True, null=True,
                                 db_comment='手术者工号')
    surgeonname = models.CharField(db_column='surgeonName', max_length=50, blank=True, null=True,
                                   db_comment='手术者姓名')
    firstassistantsurgeryid = models.CharField(db_column='firstAssistantSurgeryId', max_length=50, blank=True,
                                               null=True, db_comment='Ⅰ助工号')
    firstassistantsurgeryname = models.CharField(db_column='firstAssistantSurgeryName', max_length=50, blank=True,
                                                 null=True, db_comment='Ⅰ助姓名')
    secondassistantsurgeryid = models.CharField(db_column='secondAssistantSurgeryId', max_length=50, blank=True,
                                                null=True, db_comment='Ⅱ助工号')
    secondassistantsurgeryname = models.CharField(db_column='secondAssistantSurgeryName', max_length=50, blank=True,
                                                  null=True, db_comment='Ⅱ助姓名')
    instrumentnurseid = models.CharField(db_column='instrumentNurseId', max_length=50, blank=True, null=True,
                                         db_comment='器械护士工号')
    instrumentnursename = models.CharField(db_column='instrumentNurseName', max_length=50, blank=True, null=True,
                                           db_comment='器械护士姓名')
    patrolnurseid = models.CharField(db_column='patrolNurseId', max_length=50, blank=True, null=True,
                                     db_comment='巡台护士工号')
    patrolnursename = models.CharField(db_column='patrolNurseName', max_length=50, blank=True, null=True,
                                       db_comment='巡台护士姓名')
    operationname = models.CharField(db_column='operationName', max_length=80, blank=True, null=True,
                                     db_comment='手术名称')
    operationno = models.CharField(db_column='operationNo', max_length=50, blank=True, null=True,
                                   db_comment='手术间编号')
    surgicalgradecode = models.CharField(db_column='surgicalGradeCode', max_length=50, blank=True, null=True,
                                         db_comment='手术级别代码')
    surgicalgradename = models.CharField(db_column='surgicalGradeName', max_length=50, blank=True, null=True,
                                         db_comment='手术级别名称')
    bleedingvolume = models.IntegerField(db_column='bleedingVolume', blank=True, null=True,
                                         db_comment='出血量（mL）')
    bloodtransfusionvolume = models.IntegerField(db_column='bloodTransfusionVolume', blank=True, null=True,
                                                 db_comment='输血量（mL）')
    transfusionreactionflag = models.SmallIntegerField(db_column='transfusionReactionFlag', blank=True, null=True,
                                                       db_comment='输血反应标志')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=50, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=50, blank=True, null=True,
                                            db_comment='麻醉方法名称')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignature = models.CharField(db_column='anesthesiologistSignature', max_length=50, blank=True,
                                                 null=True, db_comment='麻醉医师姓名')
    premedicatedesc = models.CharField(db_column='premedicateDesc', max_length=100, blank=True, null=True,
                                       db_comment='术前用药')
    intraoperativemedicationdesc = models.CharField(db_column='intraoperativeMedicationDesc', max_length=100,
                                                    blank=True, null=True,
                                                    db_comment='术中用药')
    infusionvolume = models.IntegerField(db_column='infusionVolume', blank=True, null=True,
                                         db_comment='输液量（mL）')
    postoperativediagnosiscode = models.CharField(db_column='postoperativeDiagnosisCode', max_length=50, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    operationprocessdesc = models.TextField(db_column='operationProcessDesc', blank=True, null=True,
                                            db_comment='手术过程描述')
    surgicaltargetsite = models.CharField(db_column='surgicalTargetSite', max_length=50, blank=True, null=True,
                                          db_comment='手术目标部位名称')
    interventionname = models.CharField(db_column='interventionName', max_length=100, blank=True, null=True,
                                        db_comment='介入物名称')
    surgicalpositioncode = models.CharField(db_column='surgicalPositionCode', max_length=50, blank=True, null=True,
                                            db_comment='手术体位代码')
    surgicalpositionname = models.CharField(db_column='surgicalPositionName', max_length=100, blank=True, null=True,
                                            db_comment='手术体位名称')
    skindisinfectiondesc = models.CharField(db_column='skinDisinfectionDesc', max_length=200, blank=True, null=True,
                                            db_comment='皮肤消毒描述')
    surgicalincisiondesc = models.CharField(db_column='surgicalIncisionDesc', max_length=200, blank=True, null=True,
                                            db_comment='手术切口描述')
    drainageflag = models.SmallIntegerField(db_column='drainageFlag', blank=True, null=True,
                                            db_comment='引流标志')
    drainagematerialname = models.CharField(db_column='drainageMaterialName', max_length=200, blank=True, null=True,
                                            db_comment='引流材料名称')
    drainagematerialcount = models.CharField(db_column='drainageMaterialCount', max_length=200, blank=True, null=True,
                                             db_comment='引流材料数目')
    drainagematerialposition = models.CharField(db_column='drainageMaterialPosition', max_length=50, blank=True,
                                                null=True, db_comment='放置部位')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0010(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignature = models.CharField(db_column='anesthesiologistSignature', max_length=50, blank=True,
                                                 null=True, db_comment='麻醉医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断名称')
    preoperativecomplication = models.CharField(db_column='preoperativeComplication', max_length=100, blank=True,
                                                null=True, db_comment='术前合并疾病')
    briefmedicalhistory = models.CharField(db_column='briefMedicalHistory', max_length=100, blank=True, null=True,
                                           db_comment='简要病史')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    generalexamresult = models.TextField(db_column='generalExamResult', blank=True, null=True,
                                         db_comment='一般状况检查结果')
    mentalnormalflag = models.SmallIntegerField(db_column='mentalNormalFlag', blank=True, null=True,
                                                db_comment='精神状态正常标志')
    cardiacauscultationresult = models.CharField(db_column='cardiacAuscultationResult', max_length=100, blank=True,
                                                 null=True, db_comment='心脏听诊结果')
    pulmonaryauscultationresult = models.CharField(db_column='pulmonaryAuscultationResult', max_length=100, blank=True,
                                                   null=True, db_comment='肺部听诊结果')
    limbexamresult = models.TextField(db_column='limbExamResult', blank=True, null=True,
                                      db_comment='四肢检查结果')
    spinalexamresult = models.TextField(db_column='spinalExamResult', blank=True, null=True,
                                        db_comment='脊柱检查结果')
    abdominalexamresult = models.TextField(db_column='abdominalExamResult', blank=True, null=True,
                                           db_comment='腹部检查结果')
    trachealexamresult = models.CharField(db_column='trachealExamResult', max_length=100, blank=True, null=True,
                                          db_comment='气管检查结果')
    dentalexamresult = models.CharField(db_column='dentalExamResult', max_length=100, blank=True, null=True,
                                        db_comment='牙齿检查结果')
    abocode = models.CharField(db_column='ABOCode', max_length=1, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=10, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=1, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=1, blank=True, null=True,
                              db_comment='Rh血型名称')
    ecgresult = models.CharField(db_column='ECGResult', max_length=100, blank=True, null=True,
                                 db_comment='心电图检查结果')
    chestxrayfinding = models.CharField(db_column='chestXrayFinding', max_length=100, blank=True, null=True,
                                        db_comment='胸部X线检查结果')
    ctfinding = models.CharField(db_column='CTFinding', max_length=100, blank=True, null=True,
                                 db_comment='CT检查结果')
    bultrasoundexamresult = models.CharField(db_column='bultrasoundExamResult', max_length=100, blank=True, null=True,
                                             db_comment='B超检查结果')
    mrifinding = models.TextField(db_column='MRIFinding', blank=True, null=True,
                                  db_comment='MRI超检查结果')
    pulmonaryfunctiontestresult = models.TextField(db_column='pulmonaryFunctionTestResult', blank=True, null=True,
                                                   db_comment='肺功能检查结果')
    bloodroutineexamresult = models.TextField(db_column='bloodRoutineExamResult', blank=True, null=True,
                                              db_comment='血常规检查结果')
    urineroutineexamresult = models.CharField(db_column='urineRoutineExamResult', max_length=100, blank=True, null=True,
                                              db_comment='尿常规检查结果')
    coagulationfunctiontestresult = models.CharField(db_column='coagulationFunctionTestResult', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='凝血功能检查结果')
    liverfunctiontestresult = models.CharField(db_column='liverFunctionTestResult', max_length=100, blank=True,
                                               null=True, db_comment='肝功能检查结果')
    bloodgasanalysisresult = models.TextField(db_column='bloodGasAnalysisResult', blank=True, null=True,
                                              db_comment='血气分析检查结果')
    planoperationcode = models.CharField(db_column='planOperationCode', max_length=5, blank=True, null=True,
                                         db_comment='拟实施手术及操作编码')
    planoperationname = models.CharField(db_column='planOperationName', max_length=100, blank=True, null=True,
                                         db_comment='拟实施手术及操作名称')
    operatingroomno = models.CharField(db_column='operatingRoomNo', max_length=20, blank=True, null=True,
                                       db_comment='手术间编号')
    plananesthesiamethodcode = models.CharField(db_column='planAnesthesiaMethodCode', max_length=2, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法代码')
    plananesthesiamethodname = models.CharField(db_column='planAnesthesiaMethodName', max_length=100, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法名称')
    preanesthesiaorder = models.TextField(db_column='preAnesthesiaOrder', blank=True, null=True,
                                          db_comment='术前麻醉医嘱')
    anestheticindications = models.CharField(db_column='anestheticIndications', max_length=100, blank=True, null=True,
                                             db_comment='麻醉适应证')
    note = models.TextField(blank=True, null=True, db_comment='注意事项')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0011(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignaturename = models.CharField(db_column='anesthesiologistSignatureName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='麻醉医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    abocode = models.CharField(db_column='ABOCode', max_length=1, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=10, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=1, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=1, blank=True, null=True,
                              db_comment='Rh血型名称')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    postoperativediagnosiscode = models.CharField(db_column='postoperativeDiagnosisCode', max_length=11, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    postoperativediagnosisname = models.CharField(db_column='postoperativeDiagnosisName', max_length=50, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    druguseroutecode = models.CharField(db_column='drugUseRouteCode', max_length=3, blank=True, null=True,
                                        db_comment='药物使用途径代码')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=3, blank=True, null=True,
                                        db_comment='药物使用途径名称')
    drugusedose = models.DecimalField(db_column='drugUseDose', max_digits=5, decimal_places=2, blank=True, null=True,
                                      db_comment='药物使用次剂量')
    drugdosageunit = models.CharField(db_column='drugDosageUnit', max_length=6, blank=True, null=True,
                                      db_comment='药物使用剂量单位')
    drugcode = models.CharField(db_column='drugCode', max_length=50, blank=True, null=True,
                                db_comment='药品代码')
    drugname = models.CharField(db_column='drugName', max_length=50, blank=True, null=True,
                                db_comment='药物名称')
    drugusagedesc = models.CharField(db_column='drugUsageDesc', max_length=100, blank=True, null=True,
                                     db_comment='药物用法')
    frequencydruguse = models.CharField(db_column='frequencyDrugUse', max_length=2, blank=True, null=True,
                                        db_comment='药物使用频率')
    frequencydrugunit = models.CharField(db_column='frequencyDrugUnit', max_length=2, blank=True, null=True,
                                         db_comment='药物使用频率单位')
    totaldrugdose = models.DecimalField(db_column='totalDrugDose', max_digits=12, decimal_places=2, blank=True,
                                        null=True, db_comment='药物使用总剂量')
    totaldrugusedoseunit = models.CharField(db_column='totalDrugUseDoseUnit', max_length=50, blank=True, null=True,
                                            db_comment='药物使用总剂量单位')
    intraoperativeinfusiondesc = models.TextField(db_column='intraoperativeInfusionDesc', blank=True, null=True,
                                                  db_comment='术中输液项目')
    bloodtransfusiondatetime = models.CharField(db_column='bloodTransfusionDateTime', max_length=15, blank=True,
                                                null=True, db_comment='输血日期时间')
    bloodtransvarietiescode = models.CharField(db_column='bloodTransVarietiesCode', max_length=2, blank=True, null=True,
                                               db_comment='输血品种代码')
    bloodtransvarietiesname = models.CharField(db_column='bloodTransVarietiesName', max_length=50, blank=True,
                                               null=True, db_comment='输血品种名称')
    bloodtransvolume = models.IntegerField(db_column='bloodTransVolume', blank=True, null=True,
                                           db_comment='输血量（mL）')
    bloodtransvolumeunit = models.CharField(db_column='bloodTransVolumeUnit', max_length=10, blank=True, null=True,
                                            db_comment='输血量计量单位')
    bloodtransreactionflag = models.SmallIntegerField(db_column='bloodTransReactionFlag', blank=True, null=True,
                                                      db_comment='输血反应标志')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=2, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=2, blank=True, null=True,
                                            db_comment='麻醉方法名称')
    anesthesiastartdatetime = models.CharField(db_column='anesthesiaStartDateTime', max_length=15, blank=True,
                                               null=True, db_comment='麻醉开始日期时间')
    asaclsstandardcode = models.CharField(db_column='ASAClsStandardCode', max_length=1, blank=True, null=True,
                                          db_comment='ASA分级标准代码')
    asaclsstandardname = models.CharField(db_column='ASAClsStandardName', max_length=1, blank=True, null=True,
                                          db_comment='ASA分级标准名称')
    endotrachealintubationclsdesc = models.CharField(db_column='endotrachealIntubationClsDesc', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='气管插管分类')
    narcoticdrugsname = models.CharField(db_column='narcoticDrugsName', max_length=50, blank=True, null=True,
                                         db_comment='麻醉药物名称')
    anesthesiapositiondesc = models.CharField(db_column='anesthesiaPositionDesc', max_length=100, blank=True, null=True,
                                              db_comment='麻醉体位')
    respiratorytypecode = models.CharField(db_column='respiratoryTypeCode', max_length=1, blank=True, null=True,
                                           db_comment='呼吸类型代码')
    respiratorytypename = models.CharField(db_column='respiratoryTypeName', max_length=1, blank=True, null=True,
                                           db_comment='呼吸类型名称')
    anesthesiadesc = models.CharField(db_column='anesthesiaDesc', max_length=200, blank=True, null=True,
                                      db_comment='麻醉描述')
    anesthesiacomplicationscode = models.CharField(db_column='anesthesiaComplicationsCode', max_length=1, blank=True,
                                                   null=True,
                                                   db_comment='麻醉合并症标志代码')
    anesthesiacomplicationsname = models.CharField(db_column='anesthesiaComplicationsName', max_length=1, blank=True,
                                                   null=True,
                                                   db_comment='麻醉合并症标志名称')
    punctureprocessdesc = models.TextField(db_column='punctureProcessDesc', blank=True, null=True,
                                           db_comment='穿刺过程')
    anestheticeffectdesc = models.CharField(db_column='anestheticEffectDesc', max_length=100, blank=True, null=True,
                                            db_comment='麻醉效果')
    preanesthesiamedication = models.CharField(db_column='preAnesthesiaMedication', max_length=100, blank=True,
                                               null=True, db_comment='麻醉前用药')
    routinemonitoringitemname = models.CharField(db_column='RoutineMonitoringItemName', max_length=100, blank=True,
                                                 null=True, db_comment='常规监测项目名称')
    routinemonitoringitemresult = models.CharField(db_column='RoutineMonitoringItemResult', max_length=200, blank=True,
                                                   null=True,
                                                   db_comment='常规监测项目结果')
    specialmonitoringitemname = models.CharField(db_column='specialMonitoringItemName', max_length=200, blank=True,
                                                 null=True, db_comment='特殊监测项目名称')
    specialmonitoringitemresult = models.CharField(db_column='specialMonitoringItemResult', max_length=200, blank=True,
                                                   null=True,
                                                   db_comment='特殊监测项目结果')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    temperature = models.IntegerField(blank=True, null=True, db_comment='体温（℃）')
    heartrate = models.IntegerField(db_column='heartRate', blank=True, null=True,
                                    db_comment='心率（次/min）')
    pulserate = models.IntegerField(db_column='pulseRate', blank=True, null=True,
                                    db_comment='脉率（次/min）')
    respiratoryrate = models.IntegerField(db_column='respiratoryRate', blank=True, null=True,
                                          db_comment='呼吸频率（次/min）')
    systolicpressure = models.IntegerField(db_column='systolicPressure', blank=True, null=True,
                                           db_comment='收缩压（mmHg）')
    diastolicpressure = models.IntegerField(db_column='diastolicPressure', blank=True, null=True,
                                            db_comment='舒张压（mmHg）')
    operationcode = models.CharField(db_column='operationCode', max_length=5, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationstartdatetime = models.CharField(db_column='operationStartDateTime', max_length=15, blank=True, null=True,
                                              db_comment='手术开始日期时间')
    operationenddatetime = models.CharField(db_column='operationEndDateTime', max_length=15, blank=True, null=True,
                                            db_comment='手术结束日期时间')
    surgeonid = models.CharField(db_column='surgeonId', max_length=50, blank=True, null=True,
                                 db_comment='手术者工号')
    surgeonname = models.CharField(db_column='surgeonName', max_length=50, blank=True, null=True,
                                   db_comment='手术者姓名')
    surgeonroomno = models.CharField(db_column='surgeonRoomNo', max_length=20, blank=True, null=True,
                                     db_comment='手术间编号')
    surgicalpositioncode = models.CharField(db_column='surgicalPositionCode', max_length=1, blank=True, null=True,
                                            db_comment='手术体位代码')
    surgicalpositionname = models.CharField(db_column='surgicalPositionName', max_length=50, blank=True, null=True,
                                            db_comment='手术体位代码')
    examprocessdesc = models.TextField(db_column='examProcessDesc', blank=True, null=True,
                                       db_comment='诊疗过程描述')
    leavingoperatiingroomdatetime = models.CharField(db_column='leavingOperatiingRoomDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='出手术室日期时间')
    bleedingvolume = models.IntegerField(db_column='bleedingVolume', blank=True, null=True,
                                         db_comment='出血量（mL）')
    destinationcode = models.CharField(db_column='destinationCode', max_length=1, blank=True, null=True,
                                       db_comment='患者去向代码')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0012(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignaturename = models.CharField(db_column='anesthesiologistSignatureName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='麻醉医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    generalexamresult = models.TextField(db_column='generalExamResult', blank=True, null=True,
                                         db_comment='一般状况检查结果')
    abocode = models.CharField(db_column='ABOCode', max_length=1, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=10, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=1, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=10, blank=True, null=True,
                              db_comment='Rh血型名称')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    postoperativediagnosiscode = models.CharField(db_column='postoperativeDiagnosisCode', max_length=11, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    postoperativediagnosisname = models.CharField(db_column='postoperativeDiagnosisName', max_length=50, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    operationcode = models.CharField(db_column='operationCode', max_length=5, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=80, blank=True, null=True,
                                     db_comment='手术及操作名称')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=2, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anestheticindications = models.CharField(db_column='anestheticIndications', max_length=100, blank=True, null=True,
                                             db_comment='麻醉适应证')
    anesthesiarecovery = models.CharField(db_column='anesthesiaRecovery', max_length=100, blank=True, null=True,
                                          db_comment='麻醉恢复情况')
    awakedatetime = models.CharField(db_column='awakeDateTime', max_length=15, blank=True, null=True,
                                     db_comment='清醒日期时间')
    rmendotrachealintubationflag = models.SmallIntegerField(db_column='rmEndotrachealIntubationFlag', blank=True,
                                                            null=True,
                                                            db_comment='拔除气管插管标志')
    exceptionalcase = models.TextField(db_column='exceptionalCase', blank=True, null=True,
                                       db_comment='特殊情况')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=255, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0013(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=20, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    signatureid = models.CharField(db_column='SignatureId', max_length=50, blank=True, null=True,
                                   db_comment='医师工号')
    signaturename = models.CharField(db_column='SignatureName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    visitdatetime = models.CharField(db_column='visitDateTime', max_length=15, blank=True, null=True,
                                     db_comment='就医日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    abocode = models.CharField(db_column='ABOCode', max_length=1, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=10, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=1, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=1, blank=True, null=True,
                              db_comment='Rh血型名称')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=11, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    bloodtransdatetime = models.CharField(db_column='bloodTransDateTime', max_length=15, blank=True, null=True,
                                          db_comment='输血日期时间')
    bloodtranshistorycode = models.CharField(db_column='bloodTransHistoryCode', max_length=1, blank=True, null=True,
                                             db_comment='输血史标识代码')
    bloodtranshistoryname = models.CharField(db_column='bloodTransHistoryName', max_length=1, blank=True, null=True,
                                             db_comment='输血史标识代名称')
    bloodnaturetranscode = models.CharField(db_column='bloodNatureTransCode', max_length=1, blank=True, null=True,
                                            db_comment='输血性质代码')
    bloodnaturetransname = models.CharField(db_column='bloodNatureTransName', max_length=10, blank=True, null=True,
                                            db_comment='输血性质名称')
    applyabocode = models.CharField(db_column='applyABOCode', max_length=1, blank=True, null=True,
                                    db_comment='申请ABO血型代码')
    applyaboname = models.CharField(db_column='applyABOName', max_length=10, blank=True, null=True,
                                    db_comment='申请ABO血型名称')
    applyrhcode = models.CharField(db_column='applyRHCode', max_length=1, blank=True, null=True,
                                   db_comment='申请Rh血型代码')
    applyrhname = models.CharField(db_column='applyRHName', max_length=10, blank=True, null=True,
                                   db_comment='Rh血型名称')
    transfusiontrigger = models.TextField(db_column='transfusionTrigger', blank=True, null=True,
                                          db_comment='输血指征')
    bloodtransprocessrecord = models.TextField(db_column='bloodTransProcessRecord', blank=True, null=True,
                                               db_comment='输血过程记录')
    bloodtransvarietiescode = models.CharField(db_column='bloodTransVarietiesCode', max_length=2, blank=True, null=True,
                                               db_comment='输血品种代码')
    bloodtransvarietiesname = models.CharField(db_column='bloodTransVarietiesName', max_length=50, blank=True,
                                               null=True, db_comment='输血品种名称')
    bloodbagcode = models.IntegerField(db_column='bloodBagCode', blank=True, null=True,
                                       db_comment='血袋编码')
    bloodtransfusionvolume = models.IntegerField(db_column='bloodTransfusionVolume', blank=True, null=True,
                                                 db_comment='输血量（mL）')
    bloodtransfusionvolumeunit = models.CharField(db_column='bloodTransfusionVolumeUnit', max_length=10, blank=True,
                                                  null=True, db_comment='输血量计量单位')
    bloodtransreactionflag = models.SmallIntegerField(db_column='bloodTransReactionFlag', blank=True, null=True,
                                                      db_comment='输血反应标志')
    typetransreactioncode = models.CharField(db_column='typeTransReactionCode', max_length=1, blank=True, null=True,
                                             db_comment='输血反应类型')
    typetransreactionname = models.CharField(db_column='typeTransReactionName', max_length=50, blank=True, null=True,
                                             db_comment='输血反应类型名称')
    bloodtransfusiontimes = models.IntegerField(db_column='bloodTransfusionTimes', blank=True, null=True,
                                                db_comment='输血次数')
    bloodtransfusioncauses = models.CharField(db_column='bloodTransfusionCauses', max_length=100, blank=True, null=True,
                                              db_comment='输血原因')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0014(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    parturientid = models.CharField(db_column='parturientId', max_length=18, blank=True, null=True,
                                    db_comment='产妇身份证件号码')
    parturientname = models.CharField(db_column='parturientName', max_length=50, blank=True, null=True,
                                      db_comment='产妇姓名')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='产程检查签名日期时间')
    laborprocessexaminerid = models.CharField(db_column='laborProcessExaminerId', max_length=50, blank=True, null=True,
                                              db_comment='产程检查者工号')
    laborprocessexaminername = models.CharField(db_column='laborProcessExaminerName', max_length=50, blank=True,
                                                null=True, db_comment='产程检查者签名')
    recorddatetime = models.CharField(db_column='RecordDateTime', max_length=15, blank=True, null=True,
                                      db_comment='记录人签名日期时间')
    recorderid = models.CharField(db_column='recorderId', max_length=50, blank=True, null=True,
                                  db_comment='记录人工号')
    recordername = models.CharField(db_column='recorderName', max_length=50, blank=True, null=True,
                                    db_comment='记录人签名')
    contacttelecom = models.CharField(db_column='contactTelecom', max_length=20, blank=True, null=True,
                                      db_comment='联系人电话号码')
    contacts = models.CharField(max_length=50, blank=True, null=True, db_comment='联系人姓名')
    visitdatetime = models.CharField(db_column='visitDateTime', max_length=15, blank=True, null=True,
                                     db_comment='就医日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    waitingdatetime = models.CharField(db_column='waitingDateTime', max_length=15, blank=True, null=True,
                                       db_comment='待产日期时间')
    pregnancytimes = models.IntegerField(db_column='pregnancyTimes', blank=True, null=True,
                                         db_comment='孕次')
    birthtimes = models.IntegerField(db_column='birthTimes', blank=True, null=True,
                                     db_comment='产次')
    lastmenstrualdate = models.CharField(db_column='lastMenstrualDate', max_length=8, blank=True, null=True,
                                         db_comment='末次月经日期')
    conceptionformcode = models.CharField(db_column='conceptionFormCode', max_length=1, blank=True, null=True,
                                          db_comment='受孕形式代码')
    conceptionformname = models.CharField(db_column='conceptionFormName', max_length=10, blank=True, null=True,
                                          db_comment='受孕形式名称')
    expectedchildbirthdate = models.CharField(db_column='expectedChildbirthDate', max_length=8, blank=True, null=True,
                                              db_comment='预产期')
    prenatalexamflag = models.SmallIntegerField(db_column='prenatalExamFlag', blank=True, null=True,
                                                db_comment='产前检查标志')
    prenatalabnormalexamflag = models.CharField(db_column='prenatalAbnormalExamFlag', max_length=200, blank=True,
                                                null=True, db_comment='产前检查异常情况')
    thisspecialpregnancydesc = models.CharField(db_column='thisSpecialPregnancyDesc', max_length=200, blank=True,
                                                null=True, db_comment='此次妊娠特殊情况')
    pregnancyweight = models.DecimalField(db_column='pregnancyWeight', max_digits=5, decimal_places=2, blank=True,
                                          null=True, db_comment='孕前体重（kg）')
    height = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, db_comment='身高（cm）')
    pregnancyheight = models.DecimalField(db_column='pregnancyHeight', max_digits=5, decimal_places=2, blank=True,
                                          null=True, db_comment='产前体重（kg）')
    systolicpressure = models.IntegerField(db_column='systolicPressure', blank=True, null=True,
                                           db_comment='收缩压（mmHg）')
    diastolicpressure = models.IntegerField(db_column='diastolicPressure', blank=True, null=True,
                                            db_comment='舒张压（mmHg）')
    temperature = models.IntegerField(blank=True, null=True, db_comment='体温（℃）')
    pulserate = models.IntegerField(db_column='pulseRate', blank=True, null=True,
                                    db_comment='脉率（次/min）')
    respiratoryrate = models.IntegerField(db_column='respiratoryRate', blank=True, null=True,
                                          db_comment='呼吸频率（次/min）')
    pasthistory = models.TextField(db_column='pastHistory', blank=True, null=True,
                                   db_comment='既往史')
    surgicalhistory = models.TextField(db_column='surgicalHistory', blank=True, null=True,
                                       db_comment='手术史')
    pregnancychildbirthhistory = models.TextField(db_column='pregnancyChildbirthHistory', blank=True, null=True,
                                                  db_comment='既往孕产史')
    fundusheight = models.DecimalField(db_column='fundusHeight', max_digits=4, decimal_places=1, blank=True, null=True,
                                       db_comment='宫底高度（cm）')
    abdominalgirth = models.DecimalField(db_column='abdominalGirth', max_digits=5, decimal_places=1, blank=True,
                                         null=True, db_comment='腹围（cm）')
    tireorientationcode = models.CharField(db_column='tireOrientationCode', max_length=2, blank=True, null=True,
                                           db_comment='胎方位代码')
    tireorientationname = models.CharField(db_column='tireOrientationName', max_length=20, blank=True, null=True,
                                           db_comment='胎方位名称')
    fetalheartrate = models.IntegerField(db_column='fetalHeartRate', blank=True, null=True,
                                         db_comment='胎心率（次/min）')
    cephalicdystociadesc = models.CharField(db_column='cephalicDystociaDesc', max_length=200, blank=True, null=True,
                                            db_comment='头位难产情况的评估')
    outtransversediameter = models.DecimalField(db_column='outTransverseDiameter', max_digits=3, decimal_places=1,
                                                blank=True, null=True,
                                                db_comment='出口横径（cm）')
    sacralexternaldiameter = models.IntegerField(db_column='sacralExternalDiameter', blank=True, null=True,
                                                 db_comment='骶耻外径（cm）')
    diameterischialtubercle = models.DecimalField(db_column='diameterIschialTubercle', max_digits=4, decimal_places=1,
                                                  blank=True, null=True,
                                                  db_comment='坐骨结节间径（cm）')
    uterinecontractiondesc = models.CharField(db_column='uterineContractionDesc', max_length=200, blank=True, null=True,
                                              db_comment='宫缩情况')
    cervicalthickness = models.CharField(db_column='cervicalThickness', max_length=30, blank=True, null=True,
                                         db_comment='宫颈厚度')
    conditionuterineorificedesc = models.CharField(db_column='conditionUterineOrificeDesc', max_length=100, blank=True,
                                                   null=True, db_comment='宫口情况')
    fetalmembraneconditioncode = models.CharField(db_column='fetalMembraneConditionCode', max_length=1, blank=True,
                                                  null=True, db_comment='胎膜情况代码')
    fetalmembraneconditionname = models.CharField(db_column='fetalMembraneConditionName', max_length=30, blank=True,
                                                  null=True, db_comment='胎膜情况名称')
    membranebreakingmodecode = models.CharField(db_column='membraneBreakingModeCode', max_length=1, blank=True,
                                                null=True, db_comment='破膜方式代码')
    membranebreakingmodename = models.CharField(db_column='membraneBreakingModeName', max_length=30, blank=True,
                                                null=True, db_comment='破膜方式名称')
    firstexposedposition = models.CharField(db_column='firstExposedPosition', max_length=100, blank=True, null=True,
                                            db_comment='先露位置')
    amnioticfluiddesc = models.CharField(db_column='amnioticFluidDesc', max_length=100, blank=True, null=True,
                                         db_comment='羊水情况')
    bladderfillingflag = models.SmallIntegerField(db_column='bladderFillingFlag', blank=True, null=True,
                                                  db_comment='膀胱充盈标志')
    flatulenceflag = models.SmallIntegerField(db_column='flatulenceFlag', blank=True, null=True,
                                              db_comment='肠胀气标志')
    exammodecode = models.CharField(db_column='examModeCode', max_length=1, blank=True, null=True,
                                    db_comment='检查方式代码')
    exammodename = models.CharField(db_column='examModeName', max_length=100, blank=True, null=True,
                                    db_comment='检查方式名称')
    disposalplandesc = models.TextField(db_column='disposalPlanDesc', blank=True, null=True,
                                        db_comment='处置计划')
    planneddeliverymodecode = models.CharField(db_column='plannedDeliveryModeCode', max_length=2, blank=True, null=True,
                                               db_comment='计划选取的分娩方式')
    planneddeliverymodename = models.CharField(db_column='plannedDeliveryModeName', max_length=100, blank=True,
                                               null=True,
                                               db_comment='计划选取的分娩方式名称')
    laborprocessrecorddatetime = models.CharField(db_column='laborProcessRecordDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='产程记录日期时间')
    courselabordesc = models.CharField(db_column='courseLaborDesc', max_length=200, blank=True, null=True,
                                       db_comment='产程经过')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0015(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    parturientid = models.CharField(db_column='parturientId', max_length=18, blank=True, null=True,
                                    db_comment='产妇身份证件号码')
    parturientname = models.CharField(db_column='parturientName', max_length=50, blank=True, null=True,
                                      db_comment='产妇姓名')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    midwifesignaturedatetime = models.CharField(db_column='midwifesignatureDateTime', max_length=15, blank=True,
                                                null=True,
                                                db_comment='接生者签名日期时间')
    midwifeid = models.CharField(db_column='midwifeId', max_length=50, blank=True, null=True,
                                 db_comment='接生者工号')
    midwifename = models.CharField(db_column='midwifeName', max_length=50, blank=True, null=True,
                                   db_comment='接生者签名')
    deliversignaturedatetime = models.CharField(db_column='deliversignatureDateTime', max_length=15, blank=True,
                                                null=True,
                                                db_comment='助产者签名日期时间')
    deliverid = models.CharField(db_column='deliverId', max_length=50, blank=True, null=True,
                                 db_comment='助产者工号')
    delivername = models.CharField(db_column='deliverName', max_length=50, blank=True, null=True,
                                   db_comment='助产者签名')
    assistantsignaturedatetime = models.CharField(db_column='assistantsignatureDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='助手签名日期时间')
    assistantid = models.CharField(db_column='assistantId', max_length=50, blank=True, null=True,
                                   db_comment='助手工号')
    assistantname = models.CharField(db_column='assistantName', max_length=50, blank=True, null=True,
                                     db_comment='助手签名')
    babysttersignaturedatetime = models.CharField(db_column='babySttersignatureDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='护婴者签名日期时间')
    babystterid = models.CharField(db_column='babyStterId', max_length=50, blank=True, null=True,
                                   db_comment='护婴者工号')
    babysttername = models.CharField(db_column='babyStterName', max_length=50, blank=True, null=True,
                                     db_comment='护婴者签名')
    instructorsignaturedatetime = models.CharField(db_column='instructorsignatureDateTime', max_length=15, blank=True,
                                                   null=True,
                                                   db_comment='指导者签名日期时间')
    instructorid = models.CharField(db_column='instructorId', max_length=50, blank=True, null=True,
                                    db_comment='指导者工号')
    instructorname = models.CharField(db_column='instructorName', max_length=50, blank=True, null=True,
                                      db_comment='指导者签名')
    recordersignaturedatetime = models.CharField(db_column='recordersignatureDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='记录人签名日期时间')
    recorderid = models.CharField(db_column='recorderId', max_length=50, blank=True, null=True,
                                  db_comment='记录人工号')
    recordername = models.CharField(db_column='recorderName', max_length=50, blank=True, null=True,
                                    db_comment='记录人签名')
    contacttelecom = models.CharField(db_column='contactTelecom', max_length=20, blank=True, null=True,
                                      db_comment='联系人电话号码')
    contacts = models.CharField(max_length=50, blank=True, null=True, db_comment='联系人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=20, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=10, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    pregnancytimes = models.IntegerField(db_column='pregnancyTimes', blank=True, null=True,
                                         db_comment='孕次')
    birthtimes = models.IntegerField(db_column='birthTimes', blank=True, null=True,
                                     db_comment='产次')
    expectedchildbirthdate = models.CharField(db_column='expectedChildbirthDate', max_length=8, blank=True, null=True,
                                              db_comment='预产期')
    labordatetime = models.CharField(db_column='laborDateTime', max_length=15, blank=True, null=True,
                                     db_comment='临产日期时间')
    rupturefetalmembranedatetime = models.CharField(db_column='ruptureFetalMembraneDateTime', max_length=15, blank=True,
                                                    null=True,
                                                    db_comment='胎膜破裂日期时间')
    anterioramnioticfluidtraitsdesc = models.CharField(db_column='anteriorAmnioticFluidTraitsDesc', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='前羊水性状')
    watervolumefrontsheep = models.IntegerField(db_column='waterVolumeFrontSheep', blank=True, null=True,
                                                db_comment='前羊水量（mL）')
    uterinecontractionstartdatetime = models.CharField(db_column='uterineContractionStartDateTime', max_length=15,
                                                       blank=True, null=True,
                                                       db_comment='宫缩开始日期时间')
    firstdurationstagelabor = models.IntegerField(db_column='firstDurationStageLabor', blank=True, null=True,
                                                  db_comment='第1产程时长（min）')
    fullpalaceopeningdatetime = models.CharField(db_column='fullPalaceOpeningDateTime', max_length=15, blank=True,
                                                 null=True, db_comment='宫口开全日期时间')
    seconddurationstagelabor = models.IntegerField(db_column='secondDurationStageLabor', blank=True, null=True,
                                                   db_comment='第2产程时长（min）')
    fetaldeliverydatetime = models.CharField(db_column='fetalDeliveryDateTime', max_length=15, blank=True, null=True,
                                             db_comment='胎儿娩出日期时间')
    thirddurationstagelabor = models.IntegerField(db_column='thirdDurationStageLabor', blank=True, null=True,
                                                  db_comment='第3产程时长（min）')
    placentadeliverydatetime = models.CharField(db_column='placentaDeliveryDateTime', max_length=15, blank=True,
                                                null=True, db_comment='胎盘娩出日期时间')
    totaldurationstagelabor = models.IntegerField(db_column='totalDurationStageLabor', blank=True, null=True,
                                                  db_comment='总产程时长（min）')
    tireorientationcode = models.CharField(db_column='tireOrientationCode', max_length=2, blank=True, null=True,
                                           db_comment='胎方位代码')
    tireorientationname = models.CharField(db_column='tireOrientationName', max_length=20, blank=True, null=True,
                                           db_comment='胎方位名称')
    midwiferyfetaldeliveryflag = models.SmallIntegerField(db_column='midwiferyFetalDeliveryFlag', blank=True, null=True,
                                                          db_comment='胎儿娩出助产标志')
    midwiferymode = models.CharField(db_column='midwiferyMode', max_length=100, blank=True, null=True,
                                     db_comment='助产方式')
    placentaldeliverydesc = models.CharField(db_column='placentalDeliveryDesc', max_length=100, blank=True, null=True,
                                             db_comment='胎盘娩出情况')
    fetalmembraneintegrityflag = models.SmallIntegerField(db_column='fetalMembraneIntegrityFlag', blank=True, null=True,
                                                          db_comment='胎膜完整情况标志')
    amnioticfluidcharacterdesc = models.CharField(db_column='amnioticFluidCharacterDesc', max_length=100, blank=True,
                                                  null=True, db_comment='羊水性状')
    amnioticfluidvolume = models.IntegerField(db_column='amnioticFluidVolume', blank=True, null=True,
                                              db_comment='羊水量（mL）')
    umbilicalcordlength = models.IntegerField(db_column='umbilicalCordLength', blank=True, null=True,
                                              db_comment='脐带长度（cm）')
    aroundneck = models.IntegerField(db_column='aroundNeck', blank=True, null=True,
                                     db_comment='绕颈身（周）')
    umbilicalcordabnormalityflag = models.SmallIntegerField(db_column='umbilicalCordAbnormalityFlag', blank=True,
                                                            null=True,
                                                            db_comment='脐带异常情况标志')
    partummedication = models.CharField(db_column='partumMedication', max_length=50, blank=True, null=True,
                                        db_comment='产时用药')
    preventivemeasure = models.CharField(db_column='preventiveMeasure', max_length=200, blank=True, null=True,
                                         db_comment='预防措施')
    perinealincisionflag = models.SmallIntegerField(db_column='perinealIncisionFlag', blank=True, null=True,
                                                    db_comment='产妇会阴切开标志')
    perinealincisionposition = models.CharField(db_column='perinealIncisionPosition', max_length=100, blank=True,
                                                null=True, db_comment='会阴切开位置')
    perinealsuturecount = models.IntegerField(db_column='perinealSutureCount', blank=True, null=True,
                                              db_comment='产妇会阴缝合针数')
    degreeperineallacerationcode = models.CharField(db_column='degreePerinealLacerationCode', max_length=1, blank=True,
                                                    null=True,
                                                    db_comment='产妇会阴裂伤程度代码')
    degreeperineallacerationname = models.CharField(db_column='degreePerinealLacerationName', max_length=100,
                                                    blank=True, null=True,
                                                    db_comment='产妇会阴裂伤程度名称')
    perinealhematomaflag = models.SmallIntegerField(db_column='perinealHematomaFlag', blank=True, null=True,
                                                    db_comment='会阴血肿标志')
    sizeperinealhematoma = models.CharField(db_column='sizePerinealHematoma', max_length=50, blank=True, null=True,
                                            db_comment='会阴血肿大小')
    treatmentperinealhematoma = models.CharField(db_column='treatmentPerinealHematoma', max_length=200, blank=True,
                                                 null=True, db_comment='会阴血肿处理')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=2, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    narcoticdrugsname = models.CharField(db_column='narcoticDrugsName', max_length=50, blank=True, null=True,
                                         db_comment='麻醉药物名称')
    vaginallacerationflag = models.SmallIntegerField(db_column='vaginalLacerationFlag', blank=True, null=True,
                                                     db_comment='阴道裂伤标志')
    vaginalhematomaflag = models.SmallIntegerField(db_column='vaginalHematomaFlag', blank=True, null=True,
                                                   db_comment='阴道血肿标志')
    cervicallacerationflag = models.SmallIntegerField(db_column='cervicalLacerationFlag', blank=True, null=True,
                                                      db_comment='宫颈裂伤标志')
    cervicalsuturedesc = models.CharField(db_column='cervicalSutureDesc', max_length=100, blank=True, null=True,
                                          db_comment='宫颈缝合情况')
    postpartummedication = models.CharField(db_column='postpartumMedication', max_length=50, blank=True, null=True,
                                            db_comment='产后用药')
    summarydeliveryprocess = models.CharField(db_column='summaryDeliveryProcess', max_length=200, blank=True, null=True,
                                              db_comment='分娩过程摘要')
    uterinecontractiondesc = models.CharField(db_column='uterineContractionDesc', max_length=200, blank=True, null=True,
                                              db_comment='宫缩情况')
    uterinecondition = models.CharField(db_column='uterineCondition', max_length=100, blank=True, null=True,
                                        db_comment='子宫情况')
    lochiaconditiondesc = models.CharField(db_column='lochiaConditionDesc', max_length=100, blank=True, null=True,
                                           db_comment='恶露状况')
    perinealcondition = models.CharField(db_column='perinealCondition', max_length=100, blank=True, null=True,
                                         db_comment='会阴情况')
    repairprocedure = models.CharField(db_column='repairProcedure', max_length=100, blank=True, null=True,
                                       db_comment='修补手术过程')
    cordbloodstorageflag = models.SmallIntegerField(db_column='cordBloodStorageFlag', blank=True, null=True,
                                                    db_comment='存脐带血情况标志')
    postpartumdiagnosis = models.CharField(db_column='postpartumDiagnosis', max_length=200, blank=True, null=True,
                                           db_comment='产后诊断')
    postpartumobservationdatetime = models.CharField(db_column='postpartumObservationDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='产后观察日期时间')
    postpartumexamtime = models.IntegerField(db_column='postpartumExamTime', blank=True, null=True,
                                             db_comment='产后检查时间（min）')
    postpartumsystolicbloodpressure = models.IntegerField(db_column='postpartumSystolicBloodpressure', blank=True,
                                                          null=True,
                                                          db_comment='产后收缩压（mmHg ）')
    postpartumdiastolicbloodpressure = models.IntegerField(db_column='postpartumDiastolicBloodPressure', blank=True,
                                                           null=True,
                                                           db_comment='产后舒张压（mmHg ）')
    postpartumpulse = models.IntegerField(db_column='postpartumPulse', blank=True, null=True,
                                          db_comment='产后脉搏（次/min ）')
    postpartumheartrate = models.IntegerField(db_column='postpartumHeartRate', blank=True, null=True,
                                              db_comment='产后心率（次/min ）')
    postpartumhemorrhage = models.IntegerField(db_column='postpartumHemorrhage', blank=True, null=True,
                                               db_comment='产后出血量（mL）')
    postpartumuterinecontraction = models.CharField(db_column='postpartumUterineContraction', max_length=200,
                                                    blank=True, null=True,
                                                    db_comment='产后宫缩')
    postpartumfundusheight = models.DecimalField(db_column='postpartumFundusHeight', max_digits=4, decimal_places=1,
                                                 blank=True, null=True,
                                                 db_comment='产后宫底高度（cm）')
    analeaminationdesc = models.CharField(db_column='analEaminationDesc', max_length=100, blank=True, null=True,
                                          db_comment='肛查')
    neonatalsexcode = models.CharField(db_column='neonatalSexCode', max_length=1, blank=True, null=True,
                                       db_comment='新生儿性别代码')
    neonatalsexname = models.CharField(db_column='neonatalSexName', max_length=10, blank=True, null=True,
                                       db_comment='新生儿性别名称')
    neonatalbirthweight = models.IntegerField(db_column='neonatalBirthWeight', blank=True, null=True,
                                              db_comment='新生儿出生体重（g）')
    birthlengthnewborn = models.DecimalField(db_column='birthLengthNewborn', max_digits=5, decimal_places=1, blank=True,
                                             null=True, db_comment='新生儿出生身长（cm）')
    tumorsize = models.CharField(db_column='tumorSize', max_length=100, blank=True, null=True,
                                 db_comment='产瘤大小')
    tumorproducingsite = models.CharField(db_column='tumorProducingSite', max_length=100, blank=True, null=True,
                                          db_comment='产瘤部位')
    apgarscoreintervalcode = models.CharField(db_column='apgarScoreIntervalCode', max_length=1, blank=True, null=True,
                                              db_comment='Apgar评分间隔时间代码  ')
    apgarscore = models.IntegerField(db_column='apgarScore', blank=True, null=True,
                                     db_comment='Apgar评分值')
    deliveryoutcomecode = models.CharField(db_column='deliveryOutcomeCode', max_length=1, blank=True, null=True,
                                           db_comment='分娩结局代码')
    deliveryoutcomename = models.CharField(db_column='deliveryOutcomeName', max_length=10, blank=True, null=True,
                                           db_comment='分娩结局名称')
    neonatalanomalycode = models.CharField(db_column='neonatalAnomalyCode', max_length=1, blank=True, null=True,
                                           db_comment='新生儿异常情况代码')
    neonatalanomalyname = models.CharField(db_column='neonatalAnomalyName', max_length=1, blank=True, null=True,
                                           db_comment='新生儿异常情况名称')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0016(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField(max_length=100, blank=True, null=True, db_comment='住院号')
    parturientid = models.CharField(db_column='parturientId', max_length=100, blank=True, null=True,
                                    db_comment='产妇身份证件号码')
    parturientname = models.CharField(db_column='parturientName', max_length=100, blank=True, null=True,
                                      db_comment='产妇姓名')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    createdate = models.CharField(db_column='createDate', max_length=100, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=100, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=100, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    surgeonsignaturedatetime = models.CharField(db_column='surgeonsignatureDateTime', max_length=100, blank=True,
                                                null=True,
                                                db_comment='手术者签名日期时间')
    surgeonsignatureid = models.CharField(db_column='surgeonSignatureId', max_length=100, blank=True, null=True,
                                          db_comment='手术者签名工号')
    surgeonsignaturename = models.CharField(db_column='surgeonSignatureName', max_length=100, blank=True, null=True,
                                            db_comment='手术者签名')
    anesthesiologistsignaturedatetime = models.CharField(db_column='anesthesiologistsignatureDateTime', max_length=100,
                                                         blank=True, null=True,
                                                         db_comment='麻醉医师签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=100, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignaturename = models.CharField(db_column='anesthesiologistSignatureName', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='麻醉医师签名')
    instrumentnursedatetime = models.CharField(db_column='instrumentNurseDateTime', max_length=100, blank=True,
                                               null=True,
                                               db_comment='器械护士签名日期时间')
    instrumentnurseid = models.CharField(db_column='instrumentNurseId', max_length=100, blank=True, null=True,
                                         db_comment='器械护士工号')
    instrumentnursename = models.CharField(db_column='instrumentNurseName', max_length=100, blank=True, null=True,
                                           db_comment='器械护士签名')
    assistantsignaturedatetime = models.CharField(db_column='assistantsignatureDateTime', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='助手签名日期时间')
    assistantid = models.CharField(db_column='assistantId', max_length=100, blank=True, null=True,
                                   db_comment='助手工号')
    assistantname = models.CharField(db_column='assistantName', max_length=100, blank=True, null=True,
                                     db_comment='助手签名')
    babysttersignaturedatetime = models.CharField(db_column='babySttersignatureDateTime', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='护婴者签名日期时间')
    babystterid = models.CharField(db_column='babyStterId', max_length=100, blank=True, null=True,
                                   db_comment='护婴者工号')
    babysttername = models.CharField(db_column='babyStterName', max_length=100, blank=True, null=True,
                                     db_comment='护婴者签名')
    instructorsignaturedatetime = models.CharField(db_column='instructorsignatureDateTime', max_length=100, blank=True,
                                                   null=True,
                                                   db_comment='指导者签名日期时间')
    instructorid = models.CharField(db_column='instructorId', max_length=100, blank=True, null=True,
                                    db_comment='指导者工号')
    instructorname = models.CharField(db_column='instructorName', max_length=100, blank=True, null=True,
                                      db_comment='指导者签名')
    recorddatetime = models.CharField(db_column='RecordDateTime', max_length=100, blank=True, null=True,
                                      db_comment='记录人签名日期时间')
    recorderid = models.CharField(db_column='recorderId', max_length=100, blank=True, null=True,
                                  db_comment='记录人工号')
    recordername = models.CharField(db_column='recorderName', max_length=100, blank=True, null=True,
                                    db_comment='记录人签名')
    contacttelecom = models.CharField(db_column='contactTelecom', max_length=100, blank=True, null=True,
                                      db_comment='联系人电话号码')
    contacts = models.CharField(max_length=100, blank=True, null=True, db_comment='联系人姓名')
    deptid = models.CharField(db_column='deptId', max_length=100, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=100, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=100, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=100, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    orgid = models.CharField(db_column='orgId', max_length=100, blank=True, null=True,
                             db_comment='医疗机构组织机构代码')
    orgname = models.CharField(db_column='orgName', max_length=100, blank=True, null=True,
                               db_comment='医疗机构组织机构名称')
    waitingdatetime = models.CharField(db_column='waitingDateTime', max_length=100, blank=True, null=True,
                                       db_comment='待产日期时间')
    fetalmembraneintegrityflag = models.CharField(db_column='fetalMembraneIntegrityFlag', max_length=50, blank=True,
                                                  null=True,
                                                  db_comment='胎膜完整情况标志')
    umbilicalcordlength = models.CharField(db_column='umbilicalCordLength', max_length=50, blank=True, null=True,
                                           db_comment='脐带长度（cm）')
    aroundneck = models.CharField(db_column='aroundNeck', max_length=50, blank=True, null=True,
                                  db_comment='绕颈身（周）')
    prenataldiagnosis = models.TextField(db_column='prenatalDiagnosis', blank=True, null=True,
                                         db_comment='产前诊断')
    surgicalindication = models.TextField(db_column='surgicalIndication', blank=True, null=True,
                                          db_comment='手术指征')
    operationcode = models.CharField(db_column='operationCode', max_length=100, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True, null=True,
                                     db_comment='手术及操作名称')
    operationstartdatetime = models.CharField(db_column='operationStartDateTime', max_length=100, blank=True, null=True,
                                              db_comment='手术开始日期时间')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=100, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=100, blank=True, null=True,
                                            db_comment='麻醉方法名称')
    anesthesiaposition = models.CharField(db_column='anesthesiaPosition', max_length=100, blank=True, null=True,
                                          db_comment='麻醉体位')
    anestheticeffect = models.CharField(db_column='anestheticEffect', max_length=100, blank=True, null=True,
                                        db_comment='麻醉效果')
    cesareansectionprocedure = models.TextField(db_column='cesareanSectionProcedure', blank=True, null=True,
                                                db_comment='剖宫产手术过程')
    uterinecondition = models.TextField(db_column='uterineCondition', blank=True, null=True,
                                        db_comment='子宫情况')
    tireorientationcode = models.CharField(db_column='tireOrientationCode', max_length=100, blank=True, null=True,
                                           db_comment='胎方位代码')
    tireorientationname = models.CharField(db_column='tireOrientationName', max_length=100, blank=True, null=True,
                                           db_comment='胎方位名称')
    fetaldeliverymode = models.CharField(db_column='fetalDeliveryMode', max_length=100, blank=True, null=True,
                                         db_comment='胎儿娩出方式')
    placentalyellowstain = models.CharField(db_column='placentalYellowStain', max_length=100, blank=True, null=True,
                                            db_comment='胎盘黄染')
    fetalmembraneyellowstain = models.CharField(db_column='fetalMembraneYellowStain', max_length=100, blank=True,
                                                null=True, db_comment='胎膜黄染')
    umbilicalcordwinding = models.TextField(db_column='umbilicalCordWinding', blank=True, null=True,
                                            db_comment='脐带缠绕情况')
    umbilicalcordtrsion = models.CharField(db_column='umbilicalCordTrsion', max_length=50, blank=True, null=True,
                                           db_comment='脐带扭转（周）')
    cordbloodstorageflag = models.CharField(db_column='cordBloodStorageFlag', max_length=50, blank=True, null=True,
                                            db_comment='存脐带血情况标志')
    sutureuterinewalldesc = models.TextField(db_column='sutureUterineWallDesc', blank=True, null=True,
                                             db_comment='子宫壁缝合情况')
    uterinecontractionagentname = models.CharField(db_column='uterineContractionAgentName', max_length=100, blank=True,
                                                   null=True, db_comment='宫缩剂名称')
    uterinecontractionagentusage = models.CharField(db_column='uterineContractionAgentUsage', max_length=100,
                                                    blank=True, null=True,
                                                    db_comment='宫缩剂使用方法')
    surgicalmedication = models.CharField(db_column='surgicalMedication', max_length=100, blank=True, null=True,
                                          db_comment='手术用药')
    dosageoperation = models.CharField(db_column='dosageOperation', max_length=100, blank=True, null=True,
                                       db_comment='手术用药量')
    abdominalexplorationuterus = models.CharField(db_column='abdominalExplorationUterus', max_length=100, blank=True,
                                                  null=True, db_comment='腹腔探查子宫')
    abdominalexplorationaccessories = models.CharField(db_column='abdominalExplorationAccessories', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='腹腔探查附件')
    abnormalflag = models.CharField(db_column='abnormalFlag', max_length=50, blank=True, null=True,
                                    db_comment='宫腔探查异常情况标志')
    hysteromyomaexplorationflag = models.CharField(db_column='hysteromyomaExplorationFlag', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='宫腔探查肌瘤标志')
    explorationtreatmentuterinecavity = models.CharField(db_column='explorationTreatmentUterineCavity', max_length=100,
                                                         blank=True, null=True,
                                                         db_comment='宫腔探查处理情况')
    maternalconditionduringoperation = models.TextField(db_column='maternalConditionDuringOperation', blank=True,
                                                        null=True,
                                                        db_comment='手术时产妇情况')
    bleedingvolume = models.CharField(db_column='bleedingVolume', max_length=50, blank=True, null=True,
                                      db_comment='出血量（mL）')
    transfusioncomponents = models.CharField(db_column='transfusionComponents', max_length=100, blank=True, null=True,
                                             db_comment='输血成分')
    bloodtransvolume = models.CharField(db_column='bloodTransVolume', max_length=50, blank=True, null=True,
                                        db_comment='输血量（mL）')
    infusionvolume = models.CharField(db_column='infusionVolume', max_length=50, blank=True, null=True,
                                      db_comment='输液量（mL）')
    oxygensupplytime = models.CharField(db_column='oxygenSupplyTime', max_length=50, blank=True, null=True,
                                        db_comment='供氧时间（min）')
    otherdrugs = models.CharField(db_column='otherDrugs', max_length=100, blank=True, null=True,
                                  db_comment='其他用药')
    otherdesc = models.CharField(db_column='otherDesc', max_length=100, blank=True, null=True,
                                 db_comment='其他情况')
    operationenddatetime = models.CharField(db_column='operationEndDateTime', max_length=100, blank=True, null=True,
                                            db_comment='手术结束日期时间')
    wholeoperationtime = models.CharField(db_column='wholeOperationTime', max_length=50, blank=True, null=True,
                                          db_comment='手术全程时间（min）')
    postpartumdiagnosis = models.TextField(db_column='postpartumDiagnosis', blank=True, null=True,
                                           db_comment='产后诊断')
    postpartumobservationdatetime = models.CharField(db_column='postpartumObservationDateTime', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='产后观察日期时间')
    postpartumexamtime = models.CharField(db_column='postpartumExamTime', max_length=50, blank=True, null=True,
                                          db_comment='产后检查时间（min）')
    postpartumsystolicbloodpressure = models.CharField(db_column='postpartumSystolicBloodpressure', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='产后收缩压（mmHg ）')
    postpartumdiastolicbloodpressure = models.CharField(db_column='postpartumDiastolicBloodPressure', max_length=50,
                                                        blank=True, null=True,
                                                        db_comment='产后舒张压（mmHg ）')
    postpartumpulse = models.CharField(db_column='postpartumPulse', max_length=50, blank=True, null=True,
                                       db_comment='产后脉搏（次/min ）')
    postpartumheartrate = models.CharField(db_column='postpartumHeartRate', max_length=50, blank=True, null=True,
                                           db_comment='产后心率（次/min ）')
    postpartumhemorrhage = models.CharField(db_column='postpartumHemorrhage', max_length=50, blank=True, null=True,
                                            db_comment='产后出血量（mL）')
    postpartumuterinecontraction = models.CharField(db_column='postpartumUterineContraction', max_length=200,
                                                    blank=True, null=True,
                                                    db_comment='产后宫缩')
    postpartumfundusheight = models.DecimalField(db_column='postpartumFundusHeight', max_digits=4, decimal_places=1,
                                                 blank=True, null=True,
                                                 db_comment='产后宫底高度（cm）')
    neonatalsexcode = models.CharField(db_column='neonatalSexCode', max_length=100, blank=True, null=True,
                                       db_comment='新生儿性别代码')
    neonatalbirthweight = models.IntegerField(db_column='neonatalBirthWeight', blank=True, null=True,
                                              db_comment='新生儿出生体重（g）')
    birthlengthnewborn = models.DecimalField(db_column='birthLengthNewborn', max_digits=5, decimal_places=1, blank=True,
                                             null=True, db_comment='新生儿出生身长（cm）')
    tumorsize = models.CharField(db_column='tumorSize', max_length=100, blank=True, null=True,
                                 db_comment='产瘤大小')
    tumorproducingsite = models.CharField(db_column='tumorProducingSite', max_length=100, blank=True, null=True,
                                          db_comment='产瘤部位')
    apgarscoreintervalcode = models.CharField(db_column='apgarScoreIntervalCode', max_length=100, blank=True, null=True,
                                              db_comment='Apgar评分间隔时间代码  ')
    apgarscore = models.CharField(db_column='apgarScore', max_length=50, blank=True, null=True,
                                  db_comment='Apgar评分值')
    deliveryoutcomecode = models.CharField(db_column='deliveryOutcomeCode', max_length=100, blank=True, null=True,
                                           db_comment='分娩结局代码')
    deliveryoutcomename = models.CharField(db_column='deliveryOutcomeName', max_length=100, blank=True, null=True,
                                           db_comment='分娩结局名称')
    neonatalanomalycode = models.CharField(db_column='neonatalAnomalyCode', max_length=100, blank=True, null=True,
                                           db_comment='新生儿异常情况代码')
    neonatalanomalyname = models.CharField(db_column='neonatalAnomalyName', max_length=100, blank=True, null=True,
                                           db_comment='新生儿异常情况名称')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    neonatalsexname = models.CharField(db_column='neonatalSexName', max_length=100, blank=True, null=True,
                                       db_comment='新生儿性别名称')
    apgarscoreintervalname = models.CharField(db_column='apgarScoreIntervalName', max_length=100, blank=True, null=True,
                                              db_comment='Apgar评分间隔时间名称')
    adm_no = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        verbose_name = '一般护理记录'
        verbose_name_plural = verbose_name
        db_table_comment = '一般护理记录'


class C0017(Position, BaseModel):
    """
    一般护理记录
    """

    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField(db_column='ageUnit', max_length=8, blank=True, null=True,
                                db_comment='年龄单位')
    provider_org_id = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                       db_comment='医疗机构组织机构代码(提供患者服务机构)')
    provider_org_name = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                         db_comment='医疗机构组织机构名称(提供患者服务机构)')
    create_date = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                   db_comment='文档创作日期')
    author_id = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                 db_comment='护士工号(文档创作者)')
    author_name = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                   db_comment='护士签名(文档创作者)')
    gen_doc_org_id = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                      db_comment='医疗机构组织机构代码(文档生成机构)')
    gen_doc_org_name = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                        db_comment='医疗机构组织机构名称(文档生成机构)')
    signature_datetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                          db_comment='签名日期时间')
    nurse_id = models.CharField(db_column='nurseId', max_length=50, blank=True, null=True,
                                db_comment='护士工号')
    nurse_name = models.CharField(db_column='nurseName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名')
    disease_diagnosis_code = models.CharField("疾病诊断编码", max_length=32, db_comment='疾病诊断编码')
    disease_diagnosis_name = models.CharField("疾病诊断名称", max_length=64, db_comment='疾病诊断名称')
    allergic_history = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                        db_comment='过敏史')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重(kg)')
    temperature = models.IntegerField(blank=True, null=True, db_comment='体温(℃)')
    respiratory_rate = models.IntegerField(db_column='respiratoryRate', blank=True, null=True,
                                           db_comment='呼吸频率(次/min)')
    pulse_rate = models.IntegerField(db_column='pulseRate', blank=True, null=True,
                                     db_comment='脉率(次/min)')
    systolic_pressure = models.IntegerField(db_column='systolicPressure', blank=True, null=True,
                                            db_comment='收缩压(mmHg)')
    diastolic_pressure = models.IntegerField(db_column='diastolicPressure', blank=True, null=True,
                                             db_comment='舒张压(mmHg)')
    blood_oxy_gen_saturation = models.DecimalField(db_column='bloodOxygenSaturation', max_digits=4, decimal_places=1,
                                                   blank=True, null=True,
                                                   db_comment='血氧饱和度(%%)')
    dorsal_artery_foot_flag = models.SmallIntegerField(db_column='dorsalArteryFootFlag', blank=True, null=True,
                                                       db_comment='足背动脉搏动标志')
    diet_code = models.CharField(db_column='dietCode', max_length=1, blank=True, null=True,
                                 db_comment='饮食情况代码')
    diet_name = models.CharField(db_column='dietName', max_length=10, blank=True, null=True,
                                 db_comment='饮食情况名称')
    dietary_guidance_code = models.CharField(db_column='dietaryGuidanceCode', max_length=2, blank=True, null=True,
                                             db_comment='饮食指导代码')
    dietary_guidance_name = models.CharField(db_column='dietaryGuidanceName', max_length=10, blank=True, null=True,
                                             db_comment='饮食指导名称')
    nursing_grade_code = models.CharField(db_column='nursingGradeCode', max_length=1, blank=True, null=True,
                                          db_comment='护理等级代码')
    nursing_grade_name = models.CharField(db_column='nursingGradeName', max_length=10, blank=True, null=True,
                                          db_comment='护理等级名称')
    nursing_type_code = models.CharField(db_column='nursingTypeCode', max_length=1, blank=True, null=True,
                                         db_comment='护理类型代码')
    nursing_type_name = models.CharField(db_column='nursingTypeName', max_length=10, blank=True, null=True,
                                         db_comment='护理类型名称')
    catheter_care_desc = models.TextField(db_column='catheterCareDesc', blank=True, null=True,
                                          db_comment='导管护理描述')
    tracheal_care_code = models.CharField(db_column='trachealCareCode', max_length=1, blank=True, null=True,
                                          db_comment='气管护理代码')
    tracheal_care_name = models.CharField(db_column='trachealCareName', max_length=1, blank=True, null=True,
                                          db_comment='气管护理名称')
    postural_nursing = models.CharField(db_column='posturalNursing', max_length=30, blank=True, null=True,
                                        db_comment='体位护理')
    skincare_desc = models.CharField(db_column='skinCareDesc', max_length=50, blank=True, null=True,
                                     db_comment='皮肤护理')
    nutrition_nursing = models.CharField(db_column='nutritionNursing', max_length=100, blank=True, null=True,
                                         db_comment='营养护理')
    mental_nursing_code = models.CharField(db_column='mentalNursingCode', max_length=1, blank=True, null=True,
                                           db_comment='心理护理代码')
    mental_nursing_name = models.CharField(db_column='mentalNursingName', max_length=50, blank=True, null=True,
                                           db_comment='心理护理名称')
    safety_nursing_code = models.CharField(db_column='safetyNursingCode', max_length=1, blank=True, null=True,
                                           db_comment='安全护理代码')
    safety_nursing_name = models.CharField(db_column='safetyNursingName', max_length=30, blank=True, null=True,
                                           db_comment='安全护理名称')
    brief_condition = models.TextField(db_column='briefCondition', blank=True, null=True,
                                       db_comment='简要病情')
    nursing_observation_item_name = models.CharField(db_column='nursingObservationItemName', max_length=30, blank=True,
                                                     null=True,
                                                     db_comment='护理观察项目名称')
    nursing_observation_result = models.TextField(db_column='nursingObservationResult', blank=True, null=True,
                                                  db_comment='护理观察结果')
    nursing_operation_name = models.CharField(db_column='nursingOperationName', max_length=100, blank=True, null=True,
                                              db_comment='护理操作名称')
    nursing_operation_item_cls_name = models.CharField(db_column='nursingOperationItemClsName', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='护理操作项目类目名称')
    nursing_operation_result = models.TextField(db_column='nursingOperationResult', blank=True, null=True,
                                                db_comment='护理操作结果')
    send_operation_safety_checklist_flag = models.SmallIntegerField(db_column='sendOperationSafetyChecklistFlag',
                                                                    blank=True, null=True,
                                                                    db_comment='发出手术安全核对表标志')
    rcv_operation_safety_checklist_flag = models.SmallIntegerField(db_column='rcvOperationSafetyChecklistFlag',
                                                                   blank=True, null=True,
                                                                   db_comment='收回手术安全核对表标志')
    send_risk_assessment_flag = models.SmallIntegerField(db_column='sendRiskAssessmentFlag', blank=True, null=True,
                                                         db_comment='发出手术风险评估表标志')
    rcv_risk_assessment_flag = models.SmallIntegerField(db_column='rcvRiskAssessmentFlag', blank=True, null=True,
                                                        db_comment='收回手术风险评估表标志')
    is_olation_flag = models.SmallIntegerField(db_column='isolationFlag', blank=True, null=True,
                                               db_comment='隔离标志')
    is_olation_cls_code = models.CharField(db_column='isolationClsCode', max_length=1, blank=True, null=True,
                                           db_comment='隔离种类代码')
    is_olation_cls_name = models.CharField(db_column='isolationClsName', max_length=100, blank=True, null=True,
                                           db_comment='隔离种类名称')

    class Meta:
        verbose_name = '一般护理记录'
        verbose_name_plural = verbose_name
        db_table_comment = '一般护理记录'


class C0018(Position, BaseModel):
    """
    病重（病危）护理记录
    """

    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄')
    age_unit = models.CharField(db_column='ageUnit', max_length=8, blank=True, null=True,
                                db_comment='年龄单位')
    provider_org_id = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                       db_comment='医疗机构组织机构代码(提供患者服务机构)')
    provider_org_name = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                         db_comment='医疗机构组织机构名称(提供患者服务机构)')
    create_date = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                   db_comment='文档创作日期')
    author_id = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                 db_comment='护士工号(文档创作者)')
    author_name = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                   db_comment='护士签名(文档创作者)')
    gen_doc_org_id = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                      db_comment='医疗机构组织机构代码(文档生成机构)')
    gen_doc_org_name = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                        db_comment='医疗机构组织机构名称(文档生成机构)')
    gmt_signature = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                     db_comment='签名日期时间')
    nurse_id = models.CharField(db_column='nurseId', max_length=50, blank=True, null=True,
                                db_comment='护士工号')
    nurse_name = models.CharField(db_column='nurseName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名')
    allergic_flag = models.SmallIntegerField(db_column='allergicFlag', blank=True, null=True,
                                             db_comment='过敏史标志')
    allergic_history = models.TextField(db_column='allergicHistory', blank=True, null=True, db_comment='过敏史')
    disease_diagnosis_code = models.CharField("疾病诊断编码", max_length=32, db_comment='疾病诊断编码')
    disease_diagnosis_name = models.CharField("疾病诊断名称", max_length=64, db_comment='疾病诊断名称')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    temperature = models.IntegerField(blank=True, null=True, db_comment='体温（℃）')
    heartrate = models.IntegerField(db_column='heartRate', blank=True, null=True,
                                    db_comment='心率（次/min）')
    respiratory_rate = models.IntegerField(db_column='respiratoryRate', blank=True, null=True,
                                           db_comment='呼吸频率（次/min）')
    systolic_pressure = models.IntegerField(db_column='systolicPressure', blank=True, null=True,
                                            db_comment='收缩压（mmHg）')
    diastolicp_ressure = models.IntegerField(db_column='diastolicPressure', blank=True, null=True,
                                             db_comment='舒张压（mmHg）')
    blood_sugar_value = models.DecimalField(db_column='bloodSugarValue', max_digits=4, decimal_places=1, blank=True,
                                            null=True, db_comment='血糖检测值（mmol/L）')
    diet_code = models.CharField(db_column='dietCode', max_length=1, blank=True, null=True,
                                 db_comment='饮食情况代码')
    diet_name = models.CharField(db_column='dietName', max_length=10, blank=True, null=True,
                                 db_comment='饮食情况名称')
    nursing_grade_code = models.CharField(db_column='nursingGradeCode', max_length=1, blank=True, null=True,
                                          db_comment='护理等级代码')
    nursing_grade_name = models.CharField(db_column='nursingGradeName', max_length=10, blank=True, null=True,
                                          db_comment='护理等级名称')
    nursing_type_code = models.CharField(db_column='nursingTypeCode', max_length=1, blank=True, null=True,
                                         db_comment='护理类型代码')
    nursing_type_name = models.CharField(db_column='nursingTypeName', max_length=10, blank=True, null=True,
                                         db_comment='护理类型名称')
    nursing_observation_item_name = models.CharField(db_column='nursingObservationItemName', max_length=30, blank=True,
                                                     null=True,
                                                     db_comment='护理观察项目名称')
    nursing_observation_result = models.TextField(db_column='nursingObservationResult', blank=True, null=True,
                                                  db_comment='护理观察结果')
    nursing_operation_name = models.CharField(db_column='nursingOperationName', max_length=100, blank=True, null=True,
                                              db_comment='护理操作名称')
    nursing_operation_item_cls_name = models.CharField(db_column='nursingOperationItemClsName', max_length=100,
                                                       blank=True,
                                                       null=True,
                                                       db_comment='护理操作项目类目名称')
    nursing_operation_result = models.TextField(db_column='nursingOperationResult', blank=True, null=True,
                                                db_comment='护理操作结果')
    ventilator_monitoring_item = models.CharField(db_column='ventilatorMonitoringitem', max_length=20, blank=True,
                                                  null=True, db_comment='呼吸机监护项目')

    class Meta:
        verbose_name = '病重（病危）护理记录'
        verbose_name_plural = verbose_name
        db_table_comment = '病重（病危）护理记录'


class C0019(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='护士工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名(文档创作者)')
    gendocorgid = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码(文档生成机构)')
    gendocorgname = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称(文档生成机构)')
    patrolsignaturedatetime = models.CharField(db_column='patrolsignatureDateTime', max_length=15, blank=True,
                                               null=True,
                                               db_comment='巡台护士签名日期时间(签名)')
    patrolnurseid = models.CharField(db_column='patrolNurseId', max_length=50, blank=True, null=True,
                                     db_comment='巡台护士签名(签名)')
    patrolnursename = models.CharField(db_column='patrolNurseName', max_length=50, blank=True, null=True,
                                       db_comment='巡台护士签名(签名)')
    instrumentnursedatetime = models.CharField(db_column='instrumentNurseDateTime', max_length=15, blank=True,
                                               null=True,
                                               db_comment='器械护士签名日期时间(签名)')
    iinstrumentnurseid = models.CharField(db_column='iinstrumentNurseId', max_length=50, blank=True, null=True,
                                          db_comment='器械护士工号(签名)')
    istrumentnursename = models.CharField(db_column='istrumentNurseName', max_length=50, blank=True, null=True,
                                          db_comment='器械护士签名(签名)')
    handovernursedatetime = models.CharField(db_column='handoverNurseDateTime', max_length=15, blank=True, null=True,
                                             db_comment='交接护士签名日期(签名)')
    handovernurseid = models.CharField(db_column='handoverNurseId', max_length=50, blank=True, null=True,
                                       db_comment='交接护士工号(签名)')
    handovernursename = models.CharField(db_column='handoverNurseName', max_length=50, blank=True, null=True,
                                         db_comment='交接护士签名(签名)')
    transporterdatetime = models.CharField(db_column='transporterDateTime', max_length=15, blank=True, null=True,
                                           db_comment='转运者签名日期时间(签名)')
    transporterid = models.CharField(db_column='transporterId', max_length=50, blank=True, null=True,
                                     db_comment='转运者工号(签名)')
    transportername = models.CharField(db_column='transporterName', max_length=50, blank=True, null=True,
                                       db_comment='转运者签名(签名)')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断编码')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    abocode = models.CharField(db_column='ABOCode', max_length=1, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=10, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=1, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=1, blank=True, null=True,
                              db_comment='Rh血型名称')
    skinexamdesc = models.TextField(db_column='skinExamDesc', blank=True, null=True,
                                    db_comment='皮肤检查描述')
    allergicflag = models.SmallIntegerField(db_column='allergicFlag', blank=True, null=True,
                                            db_comment='过敏史标志')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    nursinggradecode = models.CharField(db_column='nursingGradeCode', max_length=1, blank=True, null=True,
                                        db_comment='护理等级代码')
    nursinggradename = models.CharField(db_column='nursingGradeName', max_length=10, blank=True, null=True,
                                        db_comment='护理等级名称')
    nursingtypecode = models.CharField(db_column='nursingTypeCode', max_length=1, blank=True, null=True,
                                       db_comment='护理类型代码')
    nursingtypename = models.CharField(db_column='nursingTypeName', max_length=10, blank=True, null=True,
                                       db_comment='护理类型名称')
    nursingobservationitemname = models.CharField(db_column='nursingObservationItemName', max_length=30, blank=True,
                                                  null=True,
                                                  db_comment='护理观察项目名称')
    nursingobservationresult = models.TextField(db_column='nursingObservationResult', blank=True, null=True,
                                                db_comment='护理观察结果')
    nursingoperationname = models.CharField(db_column='nursingOperationName', max_length=100, blank=True, null=True,
                                            db_comment='护理操作项目类目名称')
    nursingoperationitemclsname = models.CharField(db_column='nursingOperationItemClsName', max_length=100, blank=True,
                                                   null=True, db_comment='护理操作名称')
    nursingoperationresult = models.TextField(db_column='nursingOperationResult', blank=True, null=True,
                                              db_comment='护理操作结果')
    prepatrolsignaturedatetime = models.CharField(db_column='prePatrolsignatureDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='术前巡台护士签名日期时间')
    prepatrolnurseid = models.CharField(db_column='prePatrolNurseId', max_length=50, blank=True, null=True,
                                        db_comment='术前巡台护士签名')
    prepatrolnursename = models.CharField(db_column='prePatrolNurseName', max_length=50, blank=True, null=True,
                                          db_comment='术前巡台护士签名')
    preinstrumentnursedatetime = models.CharField(db_column='preInstrumentNurseDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='术前器械护士签名日期时间')
    preiinstrumentnurseid = models.CharField(db_column='preIinstrumentNurseId', max_length=50, blank=True, null=True,
                                             db_comment='术前器械护士工号')
    preinstrumentnursename = models.CharField(db_column='preInstrumentNurseName', max_length=50, blank=True, null=True,
                                              db_comment='术前器械护士签名')
    pregoodsused = models.CharField(db_column='preGoodsUsed', max_length=50, blank=True, null=True,
                                    db_comment='术前术中所用物品名称')
    preoperativeinventoryflag = models.SmallIntegerField(db_column='preoperativeInventoryFlag', blank=True, null=True,
                                                         db_comment='术前清点标志')
    spatrolsignaturedatetime = models.CharField(db_column='sPatrolsignatureDateTime', max_length=15, blank=True,
                                                null=True,
                                                db_comment='关前巡台护士签名日期时间')
    spatrolnurseid = models.CharField(db_column='sPatrolNurseId', max_length=50, blank=True, null=True,
                                      db_comment='关前巡台护士签名')
    spatrolnursename = models.CharField(db_column='sPatrolNurseName', max_length=50, blank=True, null=True,
                                        db_comment='关前巡台护士签名')
    sinstrumentnursedatetime = models.CharField(db_column='sInstrumentNurseDateTime', max_length=15, blank=True,
                                                null=True,
                                                db_comment='关前器械护士签名日期时间')
    siinstrumentnurseid = models.CharField(db_column='sIinstrumentNurseId', max_length=50, blank=True, null=True,
                                           db_comment='关前器械护士工号')
    sinstrumentnursename = models.CharField(db_column='sInstrumentNurseName', max_length=50, blank=True, null=True,
                                            db_comment='关前器械护士签名')
    sgoodsused = models.CharField(db_column='sGoodsUsed', max_length=50, blank=True, null=True,
                                  db_comment='关前术中所用物品名称')
    precosingcheckflag = models.SmallIntegerField(db_column='preCosingCheckFlag', blank=True, null=True,
                                                  db_comment='关前核对标志')
    postpatrolsignaturedatetime = models.CharField(db_column='postPatrolsignatureDateTime', max_length=15, blank=True,
                                                   null=True,
                                                   db_comment='关后巡台护士签名日期时间')
    postpatrolnurseid = models.CharField(db_column='postPatrolNurseId', max_length=50, blank=True, null=True,
                                         db_comment='关后巡台护士签名')
    postpatrolnursename = models.CharField(db_column='postPatrolNurseName', max_length=50, blank=True, null=True,
                                           db_comment='关后巡台护士签名')
    postinstrumentnursedatetime = models.CharField(db_column='postInstrumentNurseDateTime', max_length=15, blank=True,
                                                   null=True,
                                                   db_comment='关后器械护士签名日期时间')
    postiinstrumentnurseid = models.CharField(db_column='postIinstrumentNurseId', max_length=50, blank=True, null=True,
                                              db_comment='关后器械护士工号')
    postinstrumentnursename = models.CharField(db_column='postInstrumentNurseName', max_length=50, blank=True,
                                               null=True, db_comment='关后器械护士签名')
    postgoodsused = models.CharField(db_column='postGoodsUsed', max_length=50, blank=True, null=True,
                                     db_comment='关后术中所用物品名称')
    postcosingcheckflag = models.SmallIntegerField(db_column='postCosingCheckFlag', blank=True, null=True,
                                                   db_comment='关后核对标志')
    operationcode = models.CharField(db_column='operationCode', max_length=5, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作名称')
    operationstartdatetime = models.CharField(db_column='operationStartDateTime', max_length=15, blank=True, null=True,
                                              db_comment='手术结束日期时间')
    operationenddatetime = models.CharField(db_column='operationEndDateTime', max_length=15, blank=True, null=True,
                                            db_comment='手术开始日期时间')
    surgicaltargetsitecode = models.CharField(db_column='surgicalTargetSiteCode', max_length=50, blank=True, null=True,
                                              db_comment='手术目标部位代码')
    surgicaltargetsite = models.CharField(db_column='surgicalTargetSite', max_length=50, blank=True, null=True,
                                          db_comment='手术目标部位名称')
    surgeonid = models.CharField(db_column='surgeonId', max_length=50, blank=True, null=True,
                                 db_comment='手术者工号')
    surgeonname = models.CharField(db_column='surgeonName', max_length=50, blank=True, null=True,
                                   db_comment='手术者姓名')
    inpathologicalflag = models.SmallIntegerField(db_column='inPathologicalFlag', blank=True, null=True,
                                                  db_comment='术中病理标志')
    preparation = models.CharField(db_column='Preparation', max_length=100, blank=True, null=True,
                                   db_comment='准备事项')
    operationno = models.CharField(db_column='operationNo', max_length=20, blank=True, null=True,
                                   db_comment='手术间编号')
    enteringoperatroomdatetime = models.CharField(db_column='enteringOperatRoomDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='入手术室日期时间')
    outoperatroomdatetime = models.CharField(db_column='outOperatRoomDateTime', max_length=15, blank=True, null=True,
                                             db_comment='出手术室日期时间')
    patienthandovercheckitem = models.CharField(db_column='patientHandoverCheckItem', max_length=50, blank=True,
                                                null=True, db_comment='病人交接核对项目')
    handoverdatetime = models.CharField(db_column='handoverDateTime', max_length=15, blank=True, null=True,
                                        db_comment='交接日期时间(术后)')
    posthandovernurseid = models.CharField(db_column='postHandoverNurseId', max_length=50, blank=True, null=True,
                                           db_comment='交接护士工号(术后)')
    posthandovernursename = models.CharField(db_column='postHandoverNurseName', max_length=50, blank=True, null=True,
                                             db_comment='交接护士签名(术后)')
    pasttransporterid = models.CharField(db_column='pastTransporterId', max_length=50, blank=True, null=True,
                                         db_comment='转运者工号(术后)')
    pasttransportername = models.CharField(db_column='pastTransporterName', max_length=50, blank=True, null=True,
                                           db_comment='转运者签名(术后)')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0020(Position, BaseModel):
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='护士工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名(文档创作者)')
    gendocorgid = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码(文档生成机构)')
    gendocorgname = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称(文档生成机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    nurseid = models.CharField(db_column='nurseId', max_length=50, blank=True, null=True,
                               db_comment='护士工号')
    nursename = models.CharField(db_column='nurseName', max_length=50, blank=True, null=True,
                                 db_comment='护士签名')
    daysafterdelivery = models.IntegerField(db_column='daysAfterDelivery', blank=True, null=True,
                                            db_comment='手术或分娩后天数')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    offsetdays = models.IntegerField(db_column='offsetDays', blank=True, null=True,
                                     db_comment='实际住院天数')
    disease_diagnosis_code = models.CharField("疾病诊断编码", max_length=32, db_comment='疾病诊断编码')
    disease_diagnosis_name = models.CharField("疾病诊断名称", max_length=64, db_comment='疾病诊断名称')
    respiratoryrate = models.IntegerField(db_column='respiratoryRate', blank=True, null=True,
                                          db_comment='呼吸频率（次/min）')
    ventilatoruseflag = models.SmallIntegerField(db_column='ventilatorUseFlag', blank=True, null=True,
                                                 db_comment='使用呼吸机标志')
    pulserate = models.IntegerField(db_column='pulseRate', blank=True, null=True,
                                    db_comment='脉率（次/min）')
    pacemakerheartrate = models.IntegerField(db_column='pacemakerHeartRate', blank=True, null=True,
                                             db_comment='起搏器心率（次/min）')
    temperature = models.IntegerField(blank=True, null=True, db_comment='体温（℃）')
    systolicpressure = models.IntegerField(db_column='systolicPressure', blank=True, null=True,
                                           db_comment='收缩压（mmHg）')
    diastolicpressure = models.IntegerField(db_column='diastolicPressure', blank=True, null=True,
                                            db_comment='舒张压（mmHg）')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    abdominalgirth = models.DecimalField(db_column='abdominalGirth', max_digits=5, decimal_places=1, blank=True,
                                         null=True, db_comment='腹围（cm）')
    nursingobservationitemname = models.CharField(db_column='nursingObservationItemName', max_length=30, blank=True,
                                                  null=True,
                                                  db_comment='护理观察项目名称')
    nursingobservationresult = models.TextField(db_column='nursingObservationResult', blank=True, null=True,
                                                db_comment='护理观察结果')

    class Meta:
        verbose_name = '生命体征测量记录'
        verbose_name_plural = verbose_name
        db_table_comment = '生命体征测量记录'


class C0021(models.Model):
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='护士工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名(文档创作者)')
    gendocorgid = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码(文档生成机构)')
    gendocorgname = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称(文档生成机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    nurseid = models.CharField(db_column='nurseId', max_length=50, blank=True, null=True,
                               db_comment='护士工号')
    nursename = models.CharField(db_column='nurseName', max_length=50, blank=True, null=True,
                                 db_comment='护士签名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    disease_diagnosis_code = models.CharField("疾病诊断编码", max_length=32, db_comment='疾病诊断编码')
    disease_diagnosis_name = models.CharField("疾病诊断名称", max_length=64, db_comment='疾病诊断名称')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    nursinggradecode = models.CharField(db_column='nursingGradeCode', max_length=1, blank=True, null=True,
                                        db_comment='护理等级代码')
    nursinggradename = models.CharField(db_column='nursingGradeName', max_length=10, blank=True, null=True,
                                        db_comment='护理等级名称')
    nursingtypecode = models.CharField(db_column='nursingTypeCode', max_length=1, blank=True, null=True,
                                       db_comment='护理类型代码')
    nursingtypename = models.CharField(db_column='nursingTypeName', max_length=10, blank=True, null=True,
                                       db_comment='护理类型名称')
    nursingobservationitemname = models.CharField(db_column='nursingObservationItemName', max_length=30, blank=True,
                                                  null=True,
                                                  db_comment='护理观察项目名称')
    nursingobservationresult = models.TextField(db_column='nursingObservationResult', blank=True, null=True,
                                                db_comment='护理观察结果')
    nursingoperationitemclsname = models.CharField(db_column='nursingOperationItemClsName', max_length=100, blank=True,
                                                   null=True,
                                                   db_comment='护理操作项目类目名称')
    nursingoperationname = models.CharField(db_column='nursingOperationName', max_length=100, blank=True, null=True,
                                            db_comment='护理操作名称')
    nursingoperationresult = models.TextField(db_column='nursingOperationResult', blank=True, null=True,
                                              db_comment='护理操作结果')
    druguseroutecode = models.CharField(db_column='drugUseRouteCode', max_length=3, blank=True, null=True,
                                        db_comment='药物使用途径代码')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=100, blank=True, null=True,
                                        db_comment='药物使用途径名称')
    drugusedose = models.DecimalField(db_column='drugUseDose', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='药物使用次剂量')
    drugdosageunit = models.CharField(db_column='drugDosageUnit', max_length=6, blank=True, null=True,
                                      db_comment='药物使用剂量单位')
    frequencydruguse = models.CharField(db_column='frequencyDrugUse', max_length=2, blank=True, null=True,
                                        db_comment='药物使用频率')
    frequencydrugunit = models.CharField(db_column='frequencyDrugUnit', max_length=2, blank=True, null=True,
                                         db_comment='药物使用频率单位')
    drugcode = models.CharField(db_column='drugCode', max_length=50, blank=True, null=True,
                                db_comment='药品代码')
    drugname = models.CharField(db_column='drugName', max_length=50, blank=True, null=True,
                                db_comment='药物名称')
    drugusage = models.CharField(db_column='drugUsage', max_length=100, blank=True, null=True,
                                 db_comment='药物用法')
    tcmcode = models.CharField(db_column='TCMCode', max_length=1, blank=True, null=True,
                               db_comment='中药使用类别代码')
    tcmname = models.CharField(db_column='TCMName', max_length=50, blank=True, null=True,
                               db_comment='中药使用类别名称')
    totaldrugdose = models.DecimalField(db_column='totalDrugDose', max_digits=12, decimal_places=2, blank=True,
                                        null=True, db_comment='药物使用总剂量')
    totaldrugusedoseunit = models.CharField(db_column='totalDrugUseDoseUnit', max_length=6, blank=True, null=True,
                                            db_comment='药物使用总剂量使用的单位')
    vomitingflag = models.SmallIntegerField(db_column='vomitingFlag', blank=True, null=True,
                                            db_comment='呕吐标志')
    dysuriaflag = models.SmallIntegerField(db_column='dysuriaFlag', blank=True, null=True,
                                           db_comment='排尿困难标志')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    adm_no = models.CharField(max_length=50, blank=True, null=True, db_comment='门诊流水号')
    gmt_created = models.DateTimeField(db_comment='文档记录时间')
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0022(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='护士工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='护士签名(文档创作者)')
    gendocorgid = models.CharField(db_column='genDocOrgId', max_length=20, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码(文档生成机构)')
    gendocorgname = models.CharField(db_column='genDocOrgName', max_length=10, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称(文档生成机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    nurseid = models.CharField(db_column='nurseId', max_length=50, blank=True, null=True,
                               db_comment='护士工号')
    nursename = models.CharField(db_column='nurseName', max_length=50, blank=True, null=True,
                                 db_comment='护士签名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    disease_diagnosis_code = models.CharField("疾病诊断编码", max_length=32, db_comment='疾病诊断编码')
    disease_diagnosis_name = models.CharField("疾病诊断名称", max_length=64, db_comment='疾病诊断名称')
    druguseroutename = models.CharField(db_column='drugUseRouteName', max_length=30, blank=True, null=True,
                                        db_comment='使用途径')
    consumablescount = models.IntegerField(db_column='consumablesCount', blank=True, null=True,
                                           db_comment='耗材数量')
    consumablesunit = models.CharField(db_column='consumablesUnit', max_length=6, blank=True, null=True,
                                       db_comment='耗材单位')
    productcode = models.CharField(db_column='productCode', max_length=20, blank=True, null=True,
                                   db_comment='产品编码')
    materialcode = models.CharField(db_column='materialCode', max_length=200, blank=True, null=True,
                                    db_comment='材料编码')
    materialname = models.CharField(db_column='materialName', max_length=200, blank=True, null=True,
                                    db_comment='材料名称')
    productmanufacturer = models.CharField(db_column='productManufacturer', max_length=70, blank=True, null=True,
                                           db_comment='产品生产厂家')
    productsupplier = models.CharField(db_column='productSupplier', max_length=70, blank=True, null=True,
                                       db_comment='产品供应商')
    inconsumableflag = models.SmallIntegerField(db_column='inConsumableFlag', blank=True, null=True,
                                                db_comment='植入性耗材标志')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    gmt_created = models.DateTimeField()
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0023(Position, BaseModel):
    """
    入院评估
    """
    health_id = models.CharField("居民健康卡号", max_length=18, db_comment='居民健康卡号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    telecom = models.CharField(max_length=16, db_comment='患者电话号码')
    employerorgtelecom = models.CharField(db_column='employerOrgTelecom', max_length=16,
                                          db_comment='工作单位电话号码')
    email = models.CharField(max_length=100, db_comment='患者电子邮件地址')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField(max_length=30, blank=True, null=True, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=1,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=12,
                                  db_comment='性别名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=20, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=20, blank=True, null=True,
                                       db_comment='民族名称')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=2, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=20, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    nationcode = models.CharField(db_column='nationCode', max_length=3, blank=True, null=True,
                                  db_comment='国籍代码')
    nationname = models.CharField(db_column='nationName', max_length=6,
                                  db_comment='国籍名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=2, db_comment='年龄单位')
    educode = models.CharField(db_column='eduCode', max_length=2, blank=True, null=True,
                               db_comment='学历代码')
    eduname = models.CharField(db_column='eduName', max_length=16, db_comment='学历名称')
    occupationcode = models.CharField(db_column='occupationCode', max_length=2,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=12,
                                      db_comment='职业类别名称')
    createdate = models.TextField(db_column='createDate', blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=16, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=18,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=20,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.TextField(db_column='signatureDateTime', blank=True, null=True,
                                         db_comment='签名日期时间')
    assignednurseid = models.CharField(db_column='assignedNurseId', max_length=8, blank=True, null=True,
                                       db_comment='责任医生工号')
    assignednursename = models.CharField(db_column='assignedNurseName', max_length=20, blank=True, null=True,
                                         db_comment='责任护士签名')
    rcvnurseid = models.CharField(db_column='rcvNurseId', max_length=8, blank=True, null=True,
                                  db_comment='接诊护士工号')
    rcvnursename = models.CharField(db_column='rcvNurseName', max_length=20, blank=True, null=True,
                                    db_comment='接诊护士签名')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=20, blank=True, null=True,
                                            db_comment='联系人姓名')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=16, blank=True,
                                               null=True, db_comment='联系人电话号码')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=18,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=20,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    admissionreasons = models.TextField(db_column='admissionReasons',
                                        db_comment='入院原因')
    admissionroutecode = models.CharField(db_column='admissionRouteCode', max_length=50, blank=True, null=True,
                                          db_comment='入院途径代码')
    admissionroutename = models.CharField(db_column='admissionRouteName', max_length=50, blank=True, null=True,
                                          db_comment='入院途径名称')
    wardmodedesc = models.CharField(db_column='wardModeDesc', max_length=6,
                                    db_comment='入病房方式')
    mainsymptomsdesc = models.TextField(db_column='mainSymptomsDesc',
                                        db_comment='主要症状')
    weight = models.DecimalField(max_digits=10, decimal_places=2, db_comment='体重（kg）')
    temperature = models.DecimalField(max_digits=10, decimal_places=1, db_comment='体温（℃）')
    pulserate = models.DecimalField(db_column='pulseRate', max_digits=10, decimal_places=0,
                                    db_comment='呼吸频率（次/min）')
    respiratoryrate = models.DecimalField(db_column='respiratoryRate', max_digits=10, decimal_places=0,
                                          db_comment='脉率（次/min）')
    systolicpressure = models.TextField(db_column='systolicPressure',
                                        db_comment='收缩压（mmHg）')
    diastolicpressure = models.TextField(db_column='diastolicPressure',
                                         db_comment='舒张压（mmHg）')
    diseasehistory = models.TextField(db_column='diseaseHistory',
                                      db_comment='疾病史（含外伤）')
    infectioushistory = models.CharField(db_column='infectiousHistory', max_length=4,
                                         db_comment='传染病史')
    vaccinationhistory = models.CharField(db_column='vaccinationHistory', max_length=2,
                                          db_comment='预防接种史')
    surgicalhistory = models.CharField(db_column='surgicalHistory', max_length=4,
                                       db_comment='手术史')
    bloodtransfusionhistory = models.CharField(db_column='bloodTransfusionHistory', max_length=4,
                                               db_comment='输血史')
    generalhealthflag = models.CharField(db_column='generalHealthFlag', max_length=4,
                                         db_comment='一般健康状况标志')
    patientinfectiouflag = models.CharField(db_column='patientInfectiouFlag', max_length=5,
                                            db_comment='患者传染性标志')
    allergichistory = models.TextField(db_column='allergicHistory', db_comment='过敏史')
    familyhistory = models.CharField(db_column='familyHistory', max_length=4,
                                     db_comment='家族史')
    apgarscore = models.IntegerField(db_column='apgarScore', db_comment='Apgar评分值')
    devdegreecode = models.CharField(db_column='devDegreeCode', max_length=1,
                                     db_comment='发育程度代码')
    devdegreename = models.CharField(db_column='devDegreeName', max_length=6,
                                     db_comment='发育程度名称')
    normalmentalflag = models.CharField(db_column='normalMentalFlag', max_length=4,
                                        db_comment='精神状态正常标志')
    sleepdesc = models.TextField(db_column='sleepDesc', blank=True, null=True,
                                 db_comment='睡眠状况')
    exceptionalcase = models.CharField(db_column='exceptionalCase', max_length=2,
                                       db_comment='特殊情况')
    mentalitystatuscode = models.CharField(db_column='mentalityStatusCode', max_length=1,
                                           db_comment='心理状态代码')
    mentalitystatusname = models.CharField(db_column='mentalityStatusName', max_length=4,
                                           db_comment='心理状态名称')
    nutritionalstatuscode = models.CharField(db_column='nutritionalStatusCode', max_length=1,
                                             db_comment='营养状态代码')
    nutritionalstatusname = models.CharField(db_column='nutritionalStatusName', max_length=4,
                                             db_comment='营养状态名称')
    selfcareabilitycode = models.CharField(db_column='selfCareAbilityCode', max_length=1,
                                           db_comment='自理能力代码')
    selfcareabilityname = models.CharField(db_column='selfCareAbilityName', max_length=8,
                                           db_comment='自理能力名称')
    smokingsignflag = models.CharField(db_column='smokingSignFlag', max_length=5,
                                       db_comment='吸烟标志')
    smokingstatuscode = models.CharField(db_column='smokingStatusCode', max_length=1,
                                         db_comment='吸烟状况代码')
    smokingstatusname = models.CharField(db_column='smokingStatusName', max_length=8,
                                         db_comment='吸烟状况名称')
    dailysmoking = models.TextField(db_column='dailySmoking', db_comment='日吸烟量（支）')
    daysstopsmoking = models.CharField(db_column='daysStopSmoking', max_length=4,
                                       db_comment='停止吸烟天数')
    drinkingsignflag = models.CharField(db_column='drinkingSignFlag', max_length=5,
                                        db_comment='饮酒标志')
    drinkfrequencycode = models.CharField(db_column='drinkFrequencyCode', max_length=1,
                                          db_comment='饮酒频率代码')
    drinkfrequencyname = models.CharField(db_column='drinkFrequencyName', max_length=4,
                                          db_comment='饮酒频率名称')
    dailyalcoholconsumption = models.DecimalField(db_column='dailyAlcoholConsumption', max_digits=10, decimal_places=0,
                                                  db_comment='日饮酒量（mL）')
    dietcode = models.CharField(db_column='dietCode', max_length=1,
                                db_comment='饮食情况代码')
    dietname = models.CharField(db_column='dietName', max_length=4,
                                db_comment='饮食情况名称')
    admissiondiagnosticcode = models.CharField(db_column='admissionDiagnosticCode', max_length=50, blank=True,
                                               null=True, db_comment='入院诊断编码')
    admissiondiagnosticname = models.CharField(db_column='admissionDiagnosticName', max_length=100, blank=True,
                                               null=True, db_comment='入院诊断名称')
    nursingobservationitemname = models.CharField(db_column='nursingObservationItemName', max_length=2,
                                                  db_comment='护理观察项目名称')
    nursingobservationresult = models.CharField(db_column='nursingObservationResult', max_length=2,
                                                db_comment='护理观察结果')
    notifyphysicianflag = models.CharField(db_column='notifyPhysicianFlag', max_length=4,
                                           db_comment='通知医师标志')
    notifyphysiciandatetime = models.TextField(db_column='notifyPhysicianDateTime', blank=True, null=True,
                                               db_comment='通知医师日期时间')
    assessmentdatetime = models.TextField(db_column='assessmentDateTime', blank=True, null=True,
                                          db_comment='评估日期时间')
    rcvnursedatetime = models.CharField(db_column='rcvNurseDateTime', max_length=14, blank=True, null=True,
                                        db_comment='接诊护士签名时间')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=14, blank=True, null=True,
                                         db_comment='入院时间')

    class Meta:
        verbose_name = '入院评估'
        verbose_name_plural = verbose_name
        db_table_comment = '入院评估'


class C0024(models.Model):
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    health_id = models.CharField("居民健康卡号", max_length=18, db_comment='居民健康卡号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    assignednurseid = models.CharField(db_column='assignedNurseId', max_length=50, blank=True, null=True,
                                       db_comment='护士工号')
    assignednursename = models.CharField(db_column='assignedNurseName', max_length=50, blank=True, null=True,
                                         db_comment='护士签名')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=10, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    nursinggradecode = models.CharField(db_column='nursingGradeCode', max_length=1, blank=True, null=True,
                                        db_comment='护理等级代码')
    nursinggradename = models.CharField(db_column='nursingGradeName', max_length=50, blank=True, null=True,
                                        db_comment='护理等级名称')
    nursingtypecode = models.CharField(db_column='nursingTypeCode', max_length=1, blank=True, null=True,
                                       db_comment='护理类型代码')
    nursingtypename = models.CharField(db_column='nursingTypeName', max_length=50, blank=True, null=True,
                                       db_comment='护理类型名称')
    nursieproblems = models.TextField(db_column='nursieProblems', blank=True, null=True,
                                      db_comment='护理问题')
    nursingoperationitemclsname = models.CharField(db_column='nursingOperationItemClsName', max_length=100, blank=True,
                                                   null=True,
                                                   db_comment='护理操作项目类目名称')
    nursingoperationname = models.CharField(db_column='nursingOperationName', max_length=100, blank=True, null=True,
                                            db_comment='护理操作名称')
    nursingoperationresult = models.TextField(db_column='nursingOperationResult', blank=True, null=True,
                                              db_comment='护理操作结果')
    cathetercaredesc = models.TextField(db_column='catheterCareDesc', blank=True, null=True,
                                        db_comment='导管护理描述')
    posturalnursing = models.CharField(db_column='posturalNursing', max_length=30, blank=True, null=True,
                                       db_comment='体位护理')
    skincaredesc = models.CharField(db_column='skinCareDesc', max_length=50, blank=True, null=True,
                                    db_comment='皮肤护理')
    trachealcarecode = models.CharField(db_column='trachealCareCode', max_length=1, blank=True, null=True,
                                        db_comment='气管护理代码')
    trachealcarename = models.CharField(db_column='trachealCareName', max_length=50, blank=True, null=True,
                                        db_comment='气管护理名称')
    safetynursingcode = models.CharField(db_column='safetyNursingCode', max_length=1, blank=True, null=True,
                                         db_comment='安全护理代码')
    safetynursingname = models.CharField(db_column='safetyNursingName', max_length=30, blank=True, null=True,
                                         db_comment='安全护理名称')
    dietaryguidancecode = models.CharField(db_column='dietaryGuidanceCode', max_length=2, blank=True, null=True,
                                           db_comment='饮食指导代码')
    dietaryguidancename = models.CharField(db_column='dietaryGuidanceName', max_length=10, blank=True, null=True,
                                           db_comment='饮食指导名称')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    adm_no = models.CharField(max_length=50, blank=True, null=True, db_comment='就诊流水号')
    gmt_created = models.DateTimeField(db_comment='数据记录时间')
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0025(models.Model):
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    health_id = models.CharField("居民健康卡号", max_length=18, db_comment='居民健康卡号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='填表日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    rcvnursename = models.CharField(db_column='rcvNurseName', max_length=50, blank=True, null=True,
                                    db_comment='接诊护士工号')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=50, blank=True, null=True,
                                            db_comment='接诊护士签名')
    dischargediagcode = models.CharField(db_column='dischargeDiagCode', max_length=11, blank=True, null=True,
                                         db_comment='出院诊断编码')
    dischargediagname = models.CharField(db_column='dischargeDiagName', max_length=11, blank=True, null=True,
                                         db_comment='出院诊断名称')
    dischargedatetime = models.CharField(db_column='dischargeDateTime', max_length=15, blank=True, null=True,
                                         db_comment='出院日期时间')
    dischargedesc = models.TextField(db_column='dischargeDesc', blank=True, null=True,
                                     db_comment='出院情况')
    leavingwaycode = models.CharField(db_column='leavingWayCode', max_length=1, blank=True, null=True,
                                      db_comment='离院方式代码')
    leavingwayname = models.CharField(db_column='leavingWayName', max_length=1, blank=True, null=True,
                                      db_comment='离院方式名称')
    dietaryguidancecode = models.CharField(db_column='dietaryGuidanceCode', max_length=2, blank=True, null=True,
                                           db_comment='饮食指导代码')
    dietaryguidancename = models.CharField(db_column='dietaryGuidanceName', max_length=10, blank=True, null=True,
                                           db_comment='饮食指导名称')
    lifestyleguidance = models.CharField(db_column='lifestyleGuidance', max_length=50, blank=True, null=True,
                                         db_comment='生活方式指导')
    educontents = models.CharField(db_column='eduContents', max_length=100, blank=True, null=True,
                                   db_comment='宣教内容')
    followupguidance = models.CharField(db_column='followUpGuidance', max_length=100, blank=True, null=True,
                                        db_comment='复诊指导')
    medicationguidance = models.CharField(db_column='medicationGuidance', max_length=100, blank=True, null=True,
                                          db_comment='用药指导')
    selfcareabilitycode = models.CharField(db_column='selfCareAbilityCode', max_length=1, blank=True, null=True,
                                           db_comment='自理能力代码')
    selfcareabilityname = models.CharField(db_column='selfCareAbilityName', max_length=10, blank=True, null=True,
                                           db_comment='自理能力名称')
    dietcode = models.CharField(db_column='dietCode', max_length=1, blank=True, null=True,
                                db_comment='饮食情况代码')
    dietname = models.CharField(db_column='dietName', max_length=10, blank=True, null=True,
                                db_comment='饮食情况名称')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    adm_no = models.CharField(max_length=50, blank=True, null=True, db_comment='就诊流水号')
    gmt_created = models.DateTimeField(db_comment='记录时间')
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0026(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=50, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=50, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=50, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=50, blank=True, null=True,
                                         db_comment='经治医师签名日期时间')
    treatephysicianid = models.CharField(db_column='treatePhysicianId', max_length=50, blank=True, null=True,
                                         db_comment='经治医师工号')
    treatephysicianname = models.CharField(db_column='treatePhysicianName', max_length=50, blank=True, null=True,
                                           db_comment='经治医师签名')
    surgeonsignaturedatetime = models.CharField(db_column='surgeonsignatureDateTime', max_length=50, blank=True,
                                                null=True,
                                                db_comment='手术者医师签名日期时间')
    surgeonsignatureid = models.CharField(db_column='surgeonSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='手术者签名工号')
    surgeonsignaturename = models.CharField(db_column='surgeonSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='手术者签名')
    patientsignaturedatetime = models.CharField(db_column='patientsignatureDateTime', max_length=50, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    agentsignaturedatetime = models.CharField(db_column='agentsignatureDateTime', max_length=50, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='代理人证件Id')
    relcode = models.CharField(db_column='relCode', max_length=50, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=50, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    planoperationcode = models.CharField(db_column='planOperationCode', max_length=50, blank=True, null=True,
                                         db_comment='拟实施手术及操作编码')
    planoperationname = models.CharField(db_column='planOperationName', max_length=200, blank=True, null=True,
                                         db_comment='拟实施手术及操作名称')
    planoperationdatetime = models.CharField(db_column='planOperationDateTime', max_length=50, blank=True, null=True,
                                             db_comment='拟实施手术及操作日期时间')
    operationmodedesc = models.TextField(db_column='operationModeDesc', blank=True, null=True,
                                         db_comment='手术方式')
    preoperativepreparation = models.TextField(db_column='preoperativePreparation', blank=True, null=True,
                                               db_comment='术前准备')
    surgicalcontraindication = models.TextField(db_column='surgicalContraindication', blank=True, null=True,
                                                db_comment='手术禁忌症')
    surgicalindication = models.TextField(db_column='surgicalIndication', blank=True, null=True,
                                          db_comment='手术指征')
    plananesthesiamethodcode = models.CharField(db_column='planAnesthesiaMethodCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法代码')
    plananesthesiamethodname = models.CharField(db_column='planAnesthesiaMethodName', max_length=200, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法名称')
    alternatives = models.TextField(blank=True, null=True, db_comment='替代方案')
    opinionsmedicalinstitutions = models.TextField(db_column='opinionsMedicalInstitutions', blank=True, null=True,
                                                   db_comment='医疗机构意见')
    opinionspatientrepresent = models.TextField(db_column='opinionsPatientRepresent', blank=True, null=True,
                                                db_comment='患者/法定代理人意见')
    risksduringoperation = models.TextField(db_column='risksDuringOperation', blank=True, null=True,
                                            db_comment='手术中可能出现的意外及风险')
    risksafteroperation = models.TextField(db_column='risksAfterOperation', blank=True, null=True,
                                           db_comment='手术后可能出现的意外及并发症')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0027(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=20, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    anesthesiologistsignaturedatetime = models.CharField(db_column='anesthesiologistsignatureDateTime', max_length=15,
                                                         blank=True, null=True,
                                                         db_comment='麻醉医师签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignature = models.CharField(db_column='anesthesiologistSignature', max_length=50, blank=True,
                                                 null=True, db_comment='麻醉医师签名')
    patientsignaturedatetime = models.CharField(db_column='patientsignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    agentsignaturedatetime = models.CharField(db_column='agentSignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='患者证件Id')
    relcode = models.CharField(db_column='relCode', max_length=1, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=1, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=11, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    plananesthesiamethodcode = models.CharField(db_column='planAnesthesiaMethodCode', max_length=2, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法代码')
    plananesthesiamethodname = models.CharField(db_column='planAnesthesiaMethodName', max_length=2, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法名称')
    planoperationdatetime = models.CharField(db_column='planOperationDateTime', max_length=15, blank=True, null=True,
                                             db_comment='拟实施手术及操作日期时间')
    planoperationcode = models.CharField(db_column='planOperationCode', max_length=5, blank=True, null=True,
                                         db_comment='拟实施手术及操作编码')
    planoperationname = models.CharField(db_column='planOperationName', max_length=5, blank=True, null=True,
                                         db_comment='拟实施手术及操作名称')
    monitoringmethod = models.TextField(db_column='monitoringMethod', blank=True, null=True,
                                        db_comment='拟行有创操作和监测方法')
    influence = models.TextField(blank=True, null=True, db_comment='基础疾病对麻醉可能产生的影响')
    patientsbasicdiseases = models.TextField(db_column='patientsBasicDiseases', blank=True, null=True,
                                             db_comment='患者基础疾病')
    analgesiapumpflag = models.SmallIntegerField(db_column='analgesiaPumpFlag', blank=True, null=True,
                                                 db_comment='使用麻醉镇痛泵标志')
    insuranceflag = models.SmallIntegerField(db_column='insuranceFlag', blank=True, null=True,
                                             db_comment='参加麻醉安全保险标志')
    opinionsmedicalinstitutions = models.TextField(db_column='opinionsMedicalInstitutions', blank=True, null=True,
                                                   db_comment='医疗机构意见')
    opinionspatientrepresent = models.TextField(db_column='opinionsPatientRepresent', blank=True, null=True,
                                                db_comment='患者/法定代理人意见')
    risksafteranaesthesia = models.TextField(db_column='risksAfterAnaesthesia', blank=True, null=True,
                                             db_comment='麻醉中、麻醉后可能发生的意外及并发症')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0028(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=100, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=100, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医师签名日期时间')
    signatureid = models.CharField(db_column='signatureId', max_length=50, blank=True, null=True,
                                   db_comment='医师工号')
    signaturename = models.CharField(db_column='signatureName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    patientsignaturedatetime = models.CharField(db_column='patientsignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    agentsignaturedatetime = models.CharField(db_column='agentsignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='代理人证件Id')
    relcode = models.CharField(db_column='relCode', max_length=100, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=100, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=100, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    bloodtranshistorycode = models.CharField(db_column='bloodTransHistoryCode', max_length=100, blank=True, null=True,
                                             db_comment='输血史标识代码')
    bloodtranshistoryname = models.CharField(db_column='bloodTransHistoryName', max_length=100, blank=True, null=True,
                                             db_comment='输血史标识代名称')
    planbloodtransfusiondatetime = models.CharField(db_column='planBloodTransfusionDateTime', max_length=15, blank=True,
                                                    null=True,
                                                    db_comment='拟定输血日期时间')
    bloodtransfusionmode = models.CharField(db_column='bloodTransfusionMode', max_length=50, blank=True, null=True,
                                            db_comment='输血方式')
    transfusiontrigger = models.TextField(db_column='transfusionTrigger', blank=True, null=True,
                                          db_comment='输血指征')
    bloodtransvarietiescode = models.CharField(db_column='bloodTransVarietiesCode', max_length=100, blank=True,
                                               null=True, db_comment='输血品种代码')
    bloodtransvarietiesname = models.CharField(db_column='bloodTransVarietiesName', max_length=50, blank=True,
                                               null=True, db_comment='输血品种名称')
    results = models.CharField(max_length=200, blank=True, null=True, db_comment='输血前有关检查项目及结果')
    opinionsmedicalinstitutions = models.TextField(db_column='opinionsMedicalInstitutions', blank=True, null=True,
                                                   db_comment='医疗机构意见')
    opinionspatientrepresent = models.TextField(db_column='opinionsPatientRepresent', blank=True, null=True,
                                                db_comment='患者/法定代理人意见')
    risksafteranaesthesia = models.TextField(db_column='risksAfterAnaesthesia', blank=True, null=True,
                                             db_comment='输血风险及可能发生的不良后果')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0029(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=20, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医师签名日期时间')
    signatureid = models.CharField(db_column='signatureId', max_length=50, blank=True, null=True,
                                   db_comment='医师工号')
    signaturename = models.CharField(db_column='signatureName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    patientsignaturedatetime = models.CharField(db_column='patientSignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    agentsignaturedatetime = models.CharField(db_column='agentsignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='代理人证件Id')
    relcode = models.CharField(db_column='relCode', max_length=20, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=10, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=20, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    entryname = models.CharField(db_column='entryName', max_length=100, blank=True, null=True,
                                 db_comment='特殊检查及特殊治疗项目名称')
    therapeuticpurpose = models.CharField(db_column='therapeuticPurpose', max_length=100, blank=True, null=True,
                                          db_comment='特殊检查及特殊治疗目的')
    alternatives = models.TextField(blank=True, null=True, db_comment='替代方案')
    risksdesc = models.TextField(db_column='risksDesc', blank=True, null=True,
                                 db_comment='特殊检查及特殊治疗可能引起的并发症及风险')
    opinionsmedicalinstitutions = models.TextField(db_column='opinionsMedicalInstitutions', blank=True, null=True,
                                                   db_comment='医疗机构意见')
    opinionspatientrepresent = models.TextField(db_column='opinionsPatientRepresent', blank=True, null=True,
                                                db_comment='患者/法定代理人意见')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0030(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=20, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医师签名日期时间')
    signatureid = models.CharField(db_column='signatureId', max_length=50, blank=True, null=True,
                                   db_comment='医师工号')
    patientsignaturedatetime = models.CharField(db_column='patientsignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    signaturename = models.CharField(db_column='signatureName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    agentsignaturedatetime = models.CharField(db_column='agentsignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='代理人证件Id')
    relcode = models.CharField(db_column='relCode', max_length=20, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=20, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=20, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    mainrescuemeasures = models.TextField(db_column='mainRescueMeasures', blank=True, null=True,
                                          db_comment='病情概括及主要抢救措施')
    criticalnotificationdatetime = models.CharField(db_column='criticalNotificationDateTime', max_length=15, blank=True,
                                                    null=True,
                                                    db_comment='病危（重）通知日期时间')
    criticalnotificationdesc = models.TextField(db_column='criticalNotificationDesc', blank=True, null=True,
                                                db_comment='病危（重）通知内容')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0031(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    outpatient_id = models.CharField("门（急）诊号", max_length=18, blank=True, null=True, db_comment='门（急）诊号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    noinformedconsent = models.CharField(db_column='noInformedConsent', max_length=100, blank=True, null=True,
                                         db_comment='知情同意书编号')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=100, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='医师签名日期时间')
    signatureid = models.CharField(db_column='signatureId', max_length=50, blank=True, null=True,
                                   db_comment='医师工号')
    patientsignaturedatetime = models.CharField(db_column='patientsignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='患者签名日期时间')
    patientsignatureid = models.CharField(db_column='patientSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='患者证件Id')
    patientsignaturename = models.CharField(db_column='patientSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='患者姓名')
    signaturename = models.CharField(db_column='signatureName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    agentsignaturedatetime = models.CharField(db_column='agentsignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='患者/法定代理人签名日期时间')
    agentsignatureid = models.CharField(db_column='agentSignatureId', max_length=50, blank=True, null=True,
                                        db_comment='代理人证件Id')
    relcode = models.CharField(db_column='relCode', max_length=100, blank=True, null=True,
                               db_comment='法定代理人与患者的关系代码')
    relname = models.CharField(db_column='relName', max_length=100, blank=True, null=True,
                               db_comment='法定代理人与患者的关系名称')
    agentsignaturename = models.CharField(db_column='agentSignatureName', max_length=50, blank=True, null=True,
                                          db_comment='法定代理人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=100, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    nameinformedform = models.CharField(db_column='nameInformedForm', max_length=200, blank=True, null=True,
                                        db_comment='知情同意书名称')
    contentinformedform = models.TextField(db_column='contentInformedForm', blank=True, null=True,
                                           db_comment='知情同意内容')
    opinionsmedicalinstitutions = models.TextField(db_column='opinionsMedicalInstitutions', blank=True, null=True,
                                                   db_comment='医疗机构意见')
    opinionspatientrepresent = models.TextField(db_column='opinionsPatientRepresent', blank=True, null=True,
                                                db_comment='患者/法定代理人意见')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0032(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    healthid = models.CharField(db_column='healthId', max_length=100, blank=True, null=True,
                                db_comment='健康卡号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    nomedicalrecord = models.CharField(db_column='NoMedicalRecord', max_length=100, blank=True, null=True,
                                       db_comment='病案号')
    statecurrent = models.CharField(db_column='stateCurrent', max_length=200, blank=True, null=True,
                                    db_comment='现住址-省（自治区、直辖市）')
    citycurrent = models.CharField(db_column='cityCurrent', max_length=200, blank=True, null=True,
                                   db_comment='现住址-市（地区、州）')
    countycurrent = models.CharField(db_column='countyCurrent', max_length=200, blank=True, null=True,
                                     db_comment='现住址-县（区）')
    townshipcurrent = models.CharField(db_column='townshipCurrent', max_length=200, blank=True, null=True,
                                       db_comment='现住址-乡（镇、街道办事处）')
    streetnamecurrent = models.CharField(db_column='streetNameCurrent', max_length=200, blank=True, null=True,
                                         db_comment='现住址-村（街、路、弄等）')
    housenumbercurrent = models.CharField(db_column='houseNumberCurrent', max_length=200, blank=True, null=True,
                                          db_comment='现住址-门牌号码')
    postalcodecurrent = models.CharField(db_column='postalCodeCurrent', max_length=100, blank=True, null=True,
                                         db_comment='现住址-邮政编码')
    telecom = models.CharField(max_length=100, blank=True, null=True, db_comment='患者电话号码')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField(max_length=200, blank=True, null=True, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=100, blank=True, null=True,
                                 db_comment='出生日期')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=100, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=100, blank=True, null=True,
                                       db_comment='民族名称')
    statebirth = models.CharField(db_column='stateBirth', max_length=200, blank=True, null=True,
                                  db_comment='出生地-省（自治区、直辖市）')
    citybirth = models.CharField(db_column='cityBirth', max_length=200, blank=True, null=True,
                                 db_comment='出生地-市（地区、州）')
    countybirth = models.CharField(db_column='countyBirth', max_length=200, blank=True, null=True,
                                   db_comment='出生地-县（区）')
    postalcodebirth = models.CharField(db_column='postalCodeBirth', max_length=100, blank=True, null=True,
                                       db_comment='出生地-邮政编码')
    nationcode = models.CharField(db_column='nationCode', max_length=100, blank=True, null=True,
                                  db_comment='国籍代码')
    nationname = models.CharField(db_column='nationName', max_length=100, blank=True, null=True,
                                  db_comment='国籍名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    employerorgname = models.CharField(db_column='employerOrgName', max_length=200, blank=True, null=True,
                                       db_comment='工作单位名称')
    employerorgtel = models.CharField(db_column='employerOrgTel', max_length=100, blank=True, null=True,
                                      db_comment='工作单位电话号码')
    stateemporg = models.CharField(db_column='stateEmpOrg', max_length=200, blank=True, null=True,
                                   db_comment='工作单位地址-省（自治区、直辖市）')
    cityemporg = models.CharField(db_column='cityEmpOrg', max_length=200, blank=True, null=True,
                                  db_comment='工作单位地址-市（地区、州）')
    countyemporg = models.CharField(db_column='countyEmpOrg', max_length=200, blank=True, null=True,
                                    db_comment='工作单位地址-县（区）')
    townshipemporg = models.CharField(db_column='townshipEmpOrg', max_length=200, blank=True, null=True,
                                      db_comment='工作单位地址-乡（镇、街道办事处）')
    streetnameemporg = models.CharField(db_column='streetNameEmpOrg', max_length=200, blank=True, null=True,
                                        db_comment='工作单位地址-村（街、路、弄等）')
    housenumberemporg = models.CharField(db_column='houseNumberEmpOrg', max_length=200, blank=True, null=True,
                                         db_comment='工作单位地址-门牌号码')
    postalcodeemporg = models.CharField(db_column='postalCodeEmpOrg', max_length=100, blank=True, null=True,
                                        db_comment='工作单位地址-邮政编码')
    statereg = models.CharField(db_column='stateReg', max_length=200, blank=True, null=True,
                                db_comment='户口地址-省（自治区、直辖市）')
    cityreg = models.CharField(db_column='cityReg', max_length=200, blank=True, null=True,
                               db_comment='户口地址-市（地区、州）')
    countyreg = models.CharField(db_column='countyReg', max_length=200, blank=True, null=True,
                                 db_comment='户口地址-县（区）')
    townshipreg = models.CharField(db_column='townshipReg', max_length=200, blank=True, null=True,
                                   db_comment='户口地址-乡（镇、街道办事处）')
    streetnamereg = models.CharField(db_column='streetNameReg', max_length=200, blank=True, null=True,
                                     db_comment='户口地址-村（街、路、弄等）')
    housenumberreg = models.CharField(db_column='houseNumberReg', max_length=200, blank=True, null=True,
                                      db_comment='户口地址-门牌号码')
    postalcodereg = models.CharField(db_column='postalCodeReg', max_length=100, blank=True, null=True,
                                     db_comment='户口地址-邮政编码')
    statenative = models.CharField(db_column='stateNative', max_length=200, blank=True, null=True,
                                   db_comment='籍贯-省（自治区、直辖市）')
    citynative = models.CharField(db_column='cityNative', max_length=200, blank=True, null=True,
                                  db_comment='籍贯-市（地区、州）')
    occupationcode = models.CharField(db_column='occupationCode', max_length=100, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=100, blank=True, null=True,
                                      db_comment='职业类别名称')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=20, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=200, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=200, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    sectiondirectordatetime = models.CharField(db_column='sectionDirectorDateTime', max_length=20, blank=True,
                                               null=True, db_comment='签名日期时间')
    sectiondirectorid = models.CharField(db_column='sectionDirectorId', max_length=200, blank=True, null=True,
                                         db_comment='科主任工号')
    sectiondirectorname = models.CharField(db_column='sectionDirectorName', max_length=200, blank=True, null=True,
                                           db_comment='科主任姓名')
    deputydirectordatetime = models.CharField(db_column='deputyDirectorDateTime', max_length=20, blank=True, null=True,
                                              db_comment='签名日期时间')
    deputydirectorid = models.CharField(db_column='deputyDirectorId', max_length=200, blank=True, null=True,
                                        db_comment='主任（副主任）医师签名')
    deputydirectorname = models.CharField(db_column='deputyDirectorName', max_length=200, blank=True, null=True,
                                          db_comment='主任（副主任）医师签名')
    attendingdoctordatetime = models.CharField(db_column='attendingDoctorDateTime', max_length=20, blank=True,
                                               null=True, db_comment='签名日期时间')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=200, blank=True, null=True,
                                         db_comment='主治医师工号')
    attendingdoctorname = models.CharField(db_column='attendingDoctorName', max_length=200, blank=True, null=True,
                                           db_comment='主治医师签名')
    residentdatetime = models.CharField(db_column='residentDateTime', max_length=20, blank=True, null=True,
                                        db_comment='签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=200, blank=True, null=True,
                                  db_comment='住院医师工号')
    residentname = models.CharField(db_column='residentName', max_length=200, blank=True, null=True,
                                    db_comment='住院医师签名')
    assignednursedatetime = models.CharField(db_column='assignedNurseDateTime', max_length=20, blank=True, null=True,
                                             db_comment='签名日期时间')
    assignednurseid = models.CharField(db_column='assignedNurseId', max_length=200, blank=True, null=True,
                                       db_comment='责任护士工号')
    assignednursename = models.CharField(db_column='assignedNurseName', max_length=200, blank=True, null=True,
                                         db_comment='责任护士签名')
    refresherdoctordatetime = models.CharField(db_column='refresherDoctorDateTime', max_length=20, blank=True,
                                               null=True, db_comment='签名日期时间')
    refresherdoctorid = models.CharField(db_column='refresherDoctorId', max_length=200, blank=True, null=True,
                                         db_comment='进修医师工号')
    refresherdoctorname = models.CharField(db_column='refresherDoctorName', max_length=200, blank=True, null=True,
                                           db_comment='进修医师签名')
    interndatetime = models.CharField(db_column='internDateTime', max_length=20, blank=True, null=True,
                                      db_comment='签名日期时间')
    internid = models.CharField(db_column='internId', max_length=200, blank=True, null=True,
                                db_comment='实习医师签名')
    internname = models.CharField(db_column='internName', max_length=200, blank=True, null=True,
                                  db_comment='实习医师签名')
    coderdatetime = models.CharField(db_column='coderDateTime', max_length=20, blank=True, null=True,
                                     db_comment='签名日期时间')
    coderid = models.CharField(db_column='coderId', max_length=200, blank=True, null=True,
                               db_comment='编码员工号')
    codername = models.CharField(db_column='coderName', max_length=200, blank=True, null=True,
                                 db_comment='编码员签名 ')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=100, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=100, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系名称')
    associatedentitystate = models.CharField(db_column='associatedEntityState', max_length=200, blank=True, null=True,
                                             db_comment='联系人地址-省（自治区、直辖市）')
    associatedentitycity = models.CharField(db_column='associatedEntityCity', max_length=200, blank=True, null=True,
                                            db_comment='联系人地址-市（地区、州）')
    associatedentitycounty = models.CharField(db_column='associatedEntityCounty', max_length=200, blank=True, null=True,
                                              db_comment='联系人地址-县（区）')
    associatedentitytownship = models.CharField(db_column='associatedEntityTownship', max_length=200, blank=True,
                                                null=True,
                                                db_comment='联系人地址-乡（镇、街道办事处）')
    associatedentitystreetname = models.CharField(db_column='associatedEntityStreetName', max_length=200, blank=True,
                                                  null=True,
                                                  db_comment='联系人地址-村（街、路、弄等）')
    associatedentityhousenumber = models.CharField(db_column='associatedEntityHouseNumber', max_length=200, blank=True,
                                                   null=True,
                                                   db_comment='联系人地址-门牌号码')
    associatedentitypostalcode = models.CharField(db_column='associatedEntityPostalCode', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='联系人地址-邮政编码')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=100, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=200, blank=True, null=True,
                                            db_comment='联系人姓名')
    admissionroutecode = models.CharField(db_column='admissionRouteCode', max_length=100, blank=True, null=True,
                                          db_comment='入院途径代码')
    admissionroutename = models.CharField(db_column='admissionRouteName', max_length=100, blank=True, null=True,
                                          db_comment='入院途径名称')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=20, blank=True, null=True,
                                         db_comment='入院日期时间')
    leavedatetime = models.CharField(db_column='leaveDateTime', max_length=20, blank=True, null=True,
                                     db_comment='出院日期时间')
    admissiondeptcode = models.CharField(db_column='admissionDeptCode', max_length=200, blank=True, null=True,
                                         db_comment='入院科别代码')
    admissiondeptname = models.CharField(db_column='admissionDeptName', max_length=200, blank=True, null=True,
                                         db_comment='入院科别')
    admissionwardcode = models.CharField(db_column='admissionWardCode', max_length=100, blank=True, null=True,
                                         db_comment='入院病房代码')
    admissionwardname = models.CharField(db_column='admissionWardName', max_length=100, blank=True, null=True,
                                         db_comment='入院病房')
    neonatalbirthweight = models.CharField(db_column='neonatalBirthWeight', max_length=100, blank=True, null=True,
                                           db_comment='新生儿出生体重（g）')
    neonataladmissionweight = models.CharField(db_column='neonatalAdmissionWeight', max_length=100, blank=True,
                                               null=True, db_comment='新生儿入院体重（g）')
    outpatientdiagnosis = models.CharField(db_column='outpatientDiagnosis', max_length=200, blank=True, null=True,
                                           db_comment='门（急）诊诊断名称')
    outpatientdiagnosisdiseasecode = models.CharField(db_column='outpatientDiagnosisDiseaseCode', max_length=100,
                                                      blank=True, null=True,
                                                      db_comment='门（急）诊诊断疾病编码')
    outpatientdiagnosisdiseasename = models.CharField(db_column='outpatientDiagnosisDiseaseName', max_length=100,
                                                      blank=True, null=True,
                                                      db_comment='门（急）诊诊断疾病名称')
    nopathology = models.CharField(db_column='NoPathology', max_length=100, blank=True, null=True,
                                   db_comment='病理号')
    pathologicaldiagdesc = models.CharField(db_column='pathologicalDiagDesc', max_length=200, blank=True, null=True,
                                            db_comment='病理诊断名称')
    pathologicaldiagdiseasecode = models.CharField(db_column='pathologicalDiagDiseaseCode', max_length=100, blank=True,
                                                   null=True,
                                                   db_comment='病理诊断疾病编码')
    pathologicaldiagdiseasename = models.CharField(db_column='pathologicalDiagDiseaseName', max_length=100, blank=True,
                                                   null=True,
                                                   db_comment='病理诊断疾病名称')
    inpatientdiseasestatuscode = models.CharField(db_column='inpatientDiseaseStatusCode', max_length=100, blank=True,
                                                  null=True,
                                                  db_comment='住院者疾病状态代码')
    externalcausesdamagedesc = models.TextField(db_column='externalCausesDamageDesc', blank=True, null=True,
                                                db_comment='损伤中毒的外部原因')
    externalcausesdiseasepoisoncode = models.CharField(db_column='externalCausesDiseasePoisonCode', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='损伤中毒的外部原因疾病编码')
    daysbeforeadmission = models.IntegerField(db_column='daysBeforeAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院前昏迷时间-d')
    hoursbeforeadmission = models.IntegerField(db_column='hoursBeforeAdmission', blank=True, null=True,
                                               db_comment='颅脑损伤患者入院前昏迷时间-h')
    minsbeforeadmission = models.IntegerField(db_column='minsBeforeAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院前昏迷时间-min')
    daysafteradmission = models.IntegerField(db_column='daysAfterAdmission', blank=True, null=True,
                                             db_comment='颅脑损伤患者入院后昏迷时间-d')
    hoursafteradmission = models.IntegerField(db_column='hoursAfterAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院后昏迷时间-h')
    minsafteradmission = models.IntegerField(db_column='minsAfterAdmission', blank=True, null=True,
                                             db_comment='颅脑损伤患者入院后昏迷时间-min')
    transfersection = models.CharField(db_column='transferSection', max_length=200, blank=True, null=True,
                                       db_comment='转科科别')
    dischargediagmain = models.CharField(db_column='dischargeDiagMain', max_length=200, blank=True, null=True,
                                         db_comment='出院诊断-主要诊断名称')
    diagnosisdate = models.CharField(db_column='diagnosisDate', max_length=20, blank=True, null=True,
                                     db_comment='确诊日期')
    dischargediagmaindiseasecode = models.CharField(db_column='dischargeDiagMainDiseaseCode', max_length=100,
                                                    blank=True, null=True,
                                                    db_comment='出院诊断-主要诊断疾病编码')
    dischargediagmainillnesscode = models.CharField(db_column='dischargeDiagMainIllnessCode', max_length=100,
                                                    blank=True, null=True,
                                                    db_comment='出院诊断-主要诊断入院病情代码')
    dischargedate = models.CharField(db_column='dischargeDate', max_length=20, blank=True, null=True,
                                     db_comment='确诊日期')
    dischargediagother = models.CharField(db_column='dischargeDiagOther', max_length=200, blank=True, null=True,
                                          db_comment='出院诊断-其他诊断名称')
    dischargediagotherdiseasecode = models.CharField(db_column='dischargeDiagOtherDiseaseCode', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='出院诊断-其他诊断疾病编码')
    dischargediagotherillnesscode = models.CharField(db_column='dischargeDiagOtherIllnessCode', max_length=100,
                                                     blank=True, null=True,
                                                     db_comment='出院诊断-其他诊断入院病情代码')
    leavingwaycode = models.CharField(db_column='leavingWayCode', max_length=100, blank=True, null=True,
                                      db_comment='离院方式代码')
    planrcvorgname = models.CharField(db_column='planRcvOrgName', max_length=200, blank=True, null=True,
                                      db_comment='拟接收医疗机构名称')
    drugallergyflag = models.SmallIntegerField(db_column='drugAllergyFlag', blank=True, null=True,
                                               db_comment='药物过敏标志')
    allergicdrugsdesc = models.TextField(db_column='allergicDrugsDesc', blank=True, null=True,
                                         db_comment='过敏药物')
    abocode = models.CharField(db_column='ABOCode', max_length=100, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=100, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=100, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=100, blank=True, null=True,
                              db_comment='Rh血型名称')
    operationcode = models.CharField(db_column='operationCode', max_length=100, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationdatetime = models.CharField(db_column='operationDateTime', max_length=20, blank=True, null=True,
                                         db_comment='手术及操作日期')
    surgeonid = models.CharField(db_column='surgeonId', max_length=200, blank=True, null=True,
                                 db_comment='手术者工号')
    surgeonname = models.CharField(db_column='surgeonName', max_length=200, blank=True, null=True,
                                   db_comment='手术者姓名')
    firstassistantsurgeryid = models.CharField(db_column='firstAssistantSurgeryId', max_length=200, blank=True,
                                               null=True, db_comment='Ⅰ助工号')
    firstassistantsurgeryname = models.CharField(db_column='firstAssistantSurgeryName', max_length=200, blank=True,
                                                 null=True, db_comment='Ⅰ助姓名')
    secondassistantsurgeryid = models.CharField(db_column='secondAssistantSurgeryId', max_length=200, blank=True,
                                                null=True, db_comment='Ⅱ助工号')
    secondassistantsurgeryname = models.CharField(db_column='secondAssistantSurgeryName', max_length=200, blank=True,
                                                  null=True, db_comment='Ⅱ助姓名')
    operationdesc = models.CharField(db_column='operationDesc', max_length=200, blank=True, null=True,
                                     db_comment='手术及操作名称')
    surgicalgradecode = models.CharField(db_column='surgicalGradeCode', max_length=100, blank=True, null=True,
                                         db_comment='手术级别代码')
    surgicalincisionclscode = models.CharField(db_column='surgicalIncisionClsCode', max_length=100, blank=True,
                                               null=True, db_comment='手术切口类别代码')
    woundhealinggradecode = models.CharField(db_column='woundHealingGradeCode', max_length=100, blank=True, null=True,
                                             db_comment='切口愈合等级代码')
    woundhealinggradename = models.CharField(db_column='woundHealingGradeName', max_length=200, blank=True, null=True,
                                             db_comment='切口愈合等级名称')
    anesthesiamodecode = models.CharField(db_column='anesthesiaModeCode', max_length=100, blank=True, null=True,
                                          db_comment='麻醉方式代码')
    anesthesiologistid = models.CharField(db_column='anesthesiologistId', max_length=200, blank=True, null=True,
                                          db_comment='麻醉医师工号')
    anesthesiologistname = models.CharField(db_column='anesthesiologistName', max_length=200, blank=True, null=True,
                                            db_comment='麻醉医师姓名')
    times = models.IntegerField(blank=True, null=True, db_comment='住院次数')
    daysactualstay = models.IntegerField(db_column='daysActualStay', blank=True, null=True,
                                         db_comment='实际住院天数')
    dischargedatetime = models.CharField(db_column='dischargeDateTime', max_length=20, blank=True, null=True,
                                         db_comment='出院日期时间')
    dischargedeptid = models.CharField(db_column='DischargeDeptId', max_length=200, blank=True, null=True,
                                       db_comment='出院科别id')
    dischargedeptname = models.CharField(db_column='DischargeDeptName', max_length=200, blank=True, null=True,
                                         db_comment='出院科别')
    dischargewardid = models.CharField(db_column='DischargeWardId', max_length=100, blank=True, null=True,
                                       db_comment='出院病房id')
    dischargewardname = models.CharField(db_column='DischargeWardName', max_length=100, blank=True, null=True,
                                         db_comment='出院病房')
    autopsydeadpatientflag = models.SmallIntegerField(db_column='autopsyDeadPatientFlag', blank=True, null=True,
                                                      db_comment='死亡患者尸检标志')
    medicalrecordqualityflag = models.CharField(db_column='medicalRecordQualityFlag', max_length=100, blank=True,
                                                null=True, db_comment='病案质量代码')
    qcdate = models.CharField(db_column='QCDate', max_length=20, blank=True, null=True,
                              db_comment='质控日期')
    qcphysicianid = models.CharField(db_column='QCPhysicianId', max_length=200, blank=True, null=True,
                                     db_comment='质控医师工号')
    qcphysicianname = models.CharField(db_column='QCPhysicianName', max_length=200, blank=True, null=True,
                                       db_comment='质控医师签名')
    qcnurseid = models.CharField(db_column='QCNurseId', max_length=200, blank=True, null=True,
                                 db_comment='质控护士工号')
    qcnursename = models.CharField(db_column='QCNurseName', max_length=200, blank=True, null=True,
                                   db_comment='质控护士签名')
    readmissionin31dflag = models.SmallIntegerField(db_column='readmissionIn31dFlag', blank=True, null=True,
                                                    db_comment='出院31d内再住院标志')
    readmissionin32ddesc = models.CharField(db_column='readmissionIn32dDesc', max_length=100, blank=True, null=True,
                                            db_comment='出院31d内再住院目的')
    paymenttypecode = models.CharField(db_column='paymentTypeCode', max_length=100, blank=True, null=True,
                                       db_comment='医疗付费方式代码')
    paymenttypename = models.CharField(db_column='paymentTypeName', max_length=100, blank=True, null=True,
                                       db_comment='医疗付费方式名称')
    totalfee = models.DecimalField(db_column='totalFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                   db_comment='住院总费用')
    totalfeeself = models.DecimalField(db_column='totalFeeSelf', max_digits=10, decimal_places=2, blank=True, null=True,
                                       db_comment='住院总费用-自付金额')
    amedicalservicefee = models.DecimalField(db_column='aMedicalServiceFee', max_digits=10, decimal_places=2,
                                             blank=True, null=True,
                                             db_comment='综合医疗服务类-一般医疗服务费')
    atreatmentoperationfee = models.DecimalField(db_column='aTreatmentOperationFee', max_digits=10, decimal_places=2,
                                                 blank=True, null=True,
                                                 db_comment='综合医疗服务类-一般治疗操作费')
    anursingfee = models.DecimalField(db_column='aNursingFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='综合医疗服务类-护理费')
    aotherfee = models.DecimalField(db_column='aOtherFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='综合医疗服务类-其他费用')
    dpathologicaldiagfee = models.DecimalField(db_column='dPathologicalDiagFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='诊断类-病理诊断费')
    dlabdiagfee = models.DecimalField(db_column='dLabDiagFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='诊断类-实验室诊断费')
    dimagdiagfee = models.DecimalField(db_column='dImagDiagFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                       db_comment='诊断类-影像学诊断费')
    dclinicaldiagprojectfee = models.DecimalField(db_column='dClinicalDiagprojectFee', max_digits=10, decimal_places=2,
                                                  blank=True, null=True,
                                                  db_comment='诊断类-临床诊断项目费')
    tnonsurgicaltreatmentfee = models.DecimalField(db_column='tNonSurgicalTreatmentFee', max_digits=10,
                                                   decimal_places=2, blank=True, null=True,
                                                   db_comment='治疗类-非手术治疗项目费')
    tclinicalphysicaltherapyfee = models.DecimalField(db_column='tClinicalPhysicalTherapyFee', max_digits=10,
                                                      decimal_places=2, blank=True, null=True,
                                                      db_comment='治疗类-非手术治疗项目费-临床物理治疗费')
    tsurgicaltreatmentfee = models.DecimalField(db_column='tSurgicalTreatmentFee', max_digits=10, decimal_places=2,
                                                blank=True, null=True,
                                                db_comment='治疗类-手术治疗费')
    tanesthesiafee = models.DecimalField(db_column='tAnesthesiaFee', max_digits=10, decimal_places=2, blank=True,
                                         null=True, db_comment='治疗类-手术治疗费-麻醉费')
    toperationfee = models.DecimalField(db_column='tOperationFee', max_digits=10, decimal_places=2, blank=True,
                                        null=True, db_comment='治疗类-手术治疗费-手术费')
    hrehabilitationfee = models.DecimalField(db_column='hRehabilitationFee', max_digits=10, decimal_places=2,
                                             blank=True, null=True,
                                             db_comment='康复类-康复费')
    ctcmtreatmentfee = models.DecimalField(db_column='cTCMTreatmentFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True, db_comment='中医类-中医治疗费')
    wwesternmedicinefee = models.DecimalField(db_column='wWesternMedicineFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='西药类-西药费')
    wantibioticsfee = models.DecimalField(db_column='wAntibioticsFee', max_digits=10, decimal_places=2, blank=True,
                                          null=True,
                                          db_comment='西药类-西药费-抗菌药物费用')
    ecpmfee = models.DecimalField(db_column='eCPMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                  db_comment='中药类-中成药费')
    echmfee = models.DecimalField(db_column='eCHMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                  db_comment='中药类-中草药费')
    bbloodfee = models.DecimalField(db_column='bBloodFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='血液和血液制品类-血费')
    balbuminproductsfee = models.DecimalField(db_column='bAlbuminProductsFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='血液和血液制品类-白蛋白类制品费')
    bglobulinproductsfee = models.DecimalField(db_column='bGlobulinProductsFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='血液和血液制品类-球蛋白类制品费')
    bcoagulationfactorproducts = models.DecimalField(db_column='bCoagulationFactorProducts', max_digits=10,
                                                     decimal_places=2, blank=True, null=True,
                                                     db_comment='血液和血液制品类-凝血因子类制品费')
    bcytokineproducts = models.DecimalField(db_column='bCytokineProducts', max_digits=10, decimal_places=2, blank=True,
                                            null=True,
                                            db_comment='血液和血液制品类-细胞因子类制品费')
    fexamdmmfee = models.DecimalField(db_column='fExamDMMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='耗材类-检查用一次性医用材料费')
    ftraeatdmmfee = models.DecimalField(db_column='fTraeatDMMFee', max_digits=10, decimal_places=2, blank=True,
                                        null=True,
                                        db_comment='耗材类-治疗用一次性医用材料费')
    foperationdmmfee = models.DecimalField(db_column='fOperationDMMFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True,
                                           db_comment='耗材类-手术用一次性医用材料费')
    ootherfee = models.DecimalField(db_column='oOtherFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='其他类-其他费')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    medicalrecordqualityname = models.CharField(db_column='medicalRecordQualityName', max_length=100, blank=True,
                                                null=True)
    leavingwayname = models.CharField(db_column='leavingWayName', max_length=100, blank=True,
                                      null=True)
    externalcausesdiseasepoisonname = models.CharField(db_column='externalCausesDiseasePoisonName', max_length=100,
                                                       blank=True, null=True)
    dischargediagmaindiseasename = models.CharField(db_column='dischargeDiagMainDiseaseName', max_length=100,
                                                    blank=True, null=True)
    dischargediagmainillnessname = models.CharField(db_column='dischargeDiagMainIllnessName', max_length=100,
                                                    blank=True, null=True)
    dischargediagotherdiseasename = models.CharField(db_column='dischargeDiagOtherDiseaseName', max_length=100,
                                                     blank=True, null=True)
    dischargediagotherillnessname = models.CharField(db_column='dischargeDiagOtherIllnessName', max_length=100,
                                                     blank=True, null=True)
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True,
                                     null=True)
    surgicalgradename = models.CharField(db_column='surgicalGradeName', max_length=100, blank=True,
                                         null=True)
    surgicalincisionclsname = models.CharField(db_column='surgicalIncisionClsName', max_length=100, blank=True,
                                               null=True)
    anesthesiamodename = models.CharField(db_column='anesthesiaModeName', max_length=100, blank=True,
                                          null=True)
    adm_no = models.CharField(max_length=200, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    fzyid = models.CharField(db_column='FZYID', max_length=50, blank=True, null=True)
    inpatientdiseasestatusname = models.TextField(db_column='inpatientDiseaseStatusName', blank=True,
                                                  null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0033(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    healthid = models.CharField(db_column='healthId', max_length=50, blank=True, null=True,
                                db_comment='健康卡号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    nomedicalrecord = models.CharField(db_column='NoMedicalRecord', max_length=50, blank=True, null=True,
                                       db_comment='病案号')
    state = models.CharField(max_length=70, blank=True, null=True, db_comment='现住址-省（自治区、直辖市）')
    city = models.CharField(max_length=70, blank=True, null=True, db_comment='现住址-市（地区、州）')
    county = models.CharField(max_length=70, blank=True, null=True, db_comment='现住址-县（区）')
    township = models.CharField(max_length=70, blank=True, null=True, db_comment='现住址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=70, blank=True, null=True,
                                  db_comment='现住址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=70, blank=True, null=True,
                                   db_comment='现住址-门牌号码')
    postalcode = models.CharField(db_column='postalCode', max_length=50, blank=True, null=True,
                                  db_comment='现住址-邮政编码')
    telecom = models.CharField(max_length=50, blank=True, null=True, db_comment='患者电话号码')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=50, blank=True, null=True,
                                 db_comment='出生日期')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=50, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=50, blank=True, null=True,
                                       db_comment='民族名称')
    statebirth = models.CharField(db_column='stateBirth', max_length=70, blank=True, null=True,
                                  db_comment='出生地-省（自治区、直辖市）')
    citybirth = models.CharField(db_column='cityBirth', max_length=70, blank=True, null=True,
                                 db_comment='出生地-市（地区、州）')
    countybirth = models.CharField(db_column='countyBirth', max_length=70, blank=True, null=True,
                                   db_comment='出生地-县（区）')
    postalcodebirth = models.CharField(db_column='postalCodeBirth', max_length=50, blank=True, null=True,
                                       db_comment='出生地-邮政编码')
    nationcode = models.CharField(db_column='nationCode', max_length=50, blank=True, null=True,
                                  db_comment='国籍代码')
    nationname = models.CharField(db_column='nationName', max_length=50, blank=True, null=True,
                                  db_comment='国籍名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    employerorgname = models.CharField(db_column='employerOrgName', max_length=70, blank=True, null=True,
                                       db_comment='工作单位名称')
    employerorgtel = models.CharField(db_column='employerOrgTel', max_length=50, blank=True, null=True,
                                      db_comment='工作单位电话号码')
    stateemporg = models.CharField(db_column='stateEmpOrg', max_length=70, blank=True, null=True,
                                   db_comment='工作单位地址-省（自治区、直辖市）')
    cityemporg = models.CharField(db_column='cityEmpOrg', max_length=70, blank=True, null=True,
                                  db_comment='工作单位地址-市（地区、州）')
    countyemporg = models.CharField(db_column='countyEmpOrg', max_length=70, blank=True, null=True,
                                    db_comment='工作单位地址-县（区）')
    townshipemporg = models.CharField(db_column='townshipEmpOrg', max_length=70, blank=True, null=True,
                                      db_comment='工作单位地址-乡（镇、街道办事处）')
    streetnameemporg = models.CharField(db_column='streetNameEmpOrg', max_length=70, blank=True, null=True,
                                        db_comment='工作单位地址-村（街、路、弄等）')
    housenumberemporg = models.CharField(db_column='houseNumberEmpOrg', max_length=70, blank=True, null=True,
                                         db_comment='工作单位地址-门牌号码')
    postalcodeemporg = models.CharField(db_column='postalCodeEmpOrg', max_length=50, blank=True, null=True,
                                        db_comment='工作单位地址-邮政编码')
    statereg = models.CharField(db_column='stateReg', max_length=70, blank=True, null=True,
                                db_comment='户口地址-省（自治区、直辖市）')
    cityreg = models.CharField(db_column='cityReg', max_length=70, blank=True, null=True,
                               db_comment='户口地址-市（地区、州）')
    countyreg = models.CharField(db_column='countyReg', max_length=70, blank=True, null=True,
                                 db_comment='户口地址-县（区）')
    townshipreg = models.CharField(db_column='townshipReg', max_length=70, blank=True, null=True,
                                   db_comment='户口地址-乡（镇、街道办事处）')
    streetnamereg = models.CharField(db_column='streetNameReg', max_length=70, blank=True, null=True,
                                     db_comment='户口地址-村（街、路、弄等）')
    housenumberreg = models.CharField(db_column='houseNumberReg', max_length=70, blank=True, null=True,
                                      db_comment='户口地址-门牌号码')
    postalcodereg = models.CharField(db_column='postalCodeReg', max_length=50, blank=True, null=True,
                                     db_comment='户口地址-邮政编码')
    statenative = models.CharField(db_column='stateNative', max_length=70, blank=True, null=True,
                                   db_comment='籍贯-省（自治区、直辖市）')
    citynative = models.CharField(db_column='cityNative', max_length=70, blank=True, null=True,
                                  db_comment='籍贯-市（地区、州）')
    occupationcode = models.CharField(db_column='occupationCode', max_length=50, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=50, blank=True, null=True,
                                      db_comment='职业类别名称')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    createdate = models.CharField(db_column='createDate', max_length=15, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    sectiondirectordatetime = models.CharField(db_column='sectionDirectorDateTime', max_length=15, blank=True,
                                               null=True, db_comment='签名日期时间')
    sectiondirectorid = models.CharField(db_column='sectionDirectorId', max_length=50, blank=True, null=True,
                                         db_comment='科主任工号')
    sectiondirectorname = models.CharField(db_column='sectionDirectorName', max_length=50, blank=True, null=True,
                                           db_comment='科主任姓名')
    deputydirectordatetime = models.CharField(db_column='deputyDirectorDateTime', max_length=15, blank=True, null=True,
                                              db_comment='签名日期时间')
    deputydirectorid = models.CharField(db_column='deputyDirectorId', max_length=50, blank=True, null=True,
                                        db_comment='主任（副主任）医师签名')
    deputydirectorname = models.CharField(db_column='deputyDirectorName', max_length=50, blank=True, null=True,
                                          db_comment='主任（副主任）医师签名')
    attendingdoctordatetime = models.CharField(db_column='attendingDoctorDateTime', max_length=15, blank=True,
                                               null=True, db_comment='签名日期时间')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='主治医师工号')
    attendingdoctorname = models.CharField(db_column='attendingDoctorName', max_length=50, blank=True, null=True,
                                           db_comment='主治医师签名')
    residentdatetime = models.CharField(db_column='residentDateTime', max_length=15, blank=True, null=True,
                                        db_comment='签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师工号')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师签名')
    assignednursedatetime = models.CharField(db_column='assignedNurseDateTime', max_length=15, blank=True, null=True,
                                             db_comment='签名日期时间')
    assignednurseid = models.CharField(db_column='assignedNurseId', max_length=50, blank=True, null=True,
                                       db_comment='责任护士工号')
    assignednursename = models.CharField(db_column='assignedNurseName', max_length=50, blank=True, null=True,
                                         db_comment='责任护士签名')
    refresherdoctordatetime = models.CharField(db_column='refresherDoctorDateTime', max_length=15, blank=True,
                                               null=True, db_comment='签名日期时间')
    refresherdoctorid = models.CharField(db_column='refresherDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='进修医师工号')
    refresherdoctorname = models.CharField(db_column='refresherDoctorName', max_length=50, blank=True, null=True,
                                           db_comment='进修医师签名')
    interndatetime = models.CharField(db_column='internDateTime', max_length=15, blank=True, null=True,
                                      db_comment='签名日期时间')
    internid = models.CharField(db_column='internId', max_length=50, blank=True, null=True,
                                db_comment='实习医师签名')
    internname = models.CharField(db_column='internName', max_length=50, blank=True, null=True,
                                  db_comment='实习医师签名')
    coderdatetime = models.CharField(db_column='coderDateTime', max_length=15, blank=True, null=True,
                                     db_comment='签名日期时间')
    coderid = models.CharField(db_column='coderId', max_length=50, blank=True, null=True,
                               db_comment='编码员工号')
    codername = models.CharField(db_column='coderName', max_length=50, blank=True, null=True,
                                 db_comment='编码员签名 ')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='联系人与患者的关系名称')
    associatedentitystate = models.CharField(db_column='associatedEntityState', max_length=70, blank=True, null=True,
                                             db_comment='联系人地址-省（自治区、直辖市）')
    associatedentitycity = models.CharField(db_column='associatedEntityCity', max_length=70, blank=True, null=True,
                                            db_comment='联系人地址-市（地区、州）')
    associatedentitycounty = models.CharField(db_column='associatedEntityCounty', max_length=70, blank=True, null=True,
                                              db_comment='联系人地址-县（区）')
    associatedentitytownship = models.CharField(db_column='associatedEntityTownship', max_length=70, blank=True,
                                                null=True,
                                                db_comment='联系人地址-乡（镇、街道办事处）')
    associatedentitystreetname = models.CharField(db_column='associatedEntityStreetName', max_length=70, blank=True,
                                                  null=True,
                                                  db_comment='联系人地址-村（街、路、弄等）')
    associatedentityhousenumber = models.CharField(db_column='associatedEntityHouseNumber', max_length=70, blank=True,
                                                   null=True,
                                                   db_comment='联系人地址-门牌号码')
    associatedentitypostalcode = models.CharField(db_column='associatedEntityPostalCode', max_length=50, blank=True,
                                                  null=True,
                                                  db_comment='联系人地址-邮政编码')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=50, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=50, blank=True, null=True,
                                            db_comment='联系人姓名')
    admissionroutecode = models.CharField(db_column='admissionRouteCode', max_length=50, blank=True, null=True,
                                          db_comment='入院途径代码')
    admissionroutename = models.CharField(db_column='admissionRouteName', max_length=50, blank=True, null=True,
                                          db_comment='入院途径名称')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    leavedatetime = models.CharField(db_column='leaveDateTime', max_length=15, blank=True, null=True,
                                     db_comment='出院日期时间')
    admissiondeptcode = models.CharField(db_column='admissionDeptCode', max_length=50, blank=True, null=True,
                                         db_comment='入院科别代码')
    admissiondeptname = models.CharField(db_column='admissionDeptName', max_length=50, blank=True, null=True,
                                         db_comment='入院科别')
    admissionwardcode = models.CharField(db_column='admissionWardCode', max_length=50, blank=True, null=True,
                                         db_comment='入院病房代码')
    admissionwardname = models.CharField(db_column='admissionWardName', max_length=50, blank=True, null=True,
                                         db_comment='入院病房')
    neonatalbirthweight = models.CharField(db_column='neonatalBirthWeight', max_length=50, blank=True, null=True,
                                           db_comment='新生儿出生体重（g）')
    neonataladmissionweight = models.CharField(db_column='neonatalAdmissionWeight', max_length=50, blank=True,
                                               null=True, db_comment='新生儿入院体重（g）')
    tcmdiagnosis = models.CharField(db_column='TCMDiagnosis', max_length=50, blank=True, null=True,
                                    db_comment='门（急）诊诊断（中医诊断）病名名称')
    tcmdiagdiseasecode = models.CharField(db_column='TCMDiagDiseaseCode', max_length=50, blank=True, null=True,
                                          db_comment='门（急）诊诊断（中医诊断）病名编码')
    tcmdiagdiseasename = models.CharField(db_column='TCMDiagDiseaseName', max_length=50, blank=True, null=True,
                                          db_comment='门（急）诊诊断（中医诊断）病名名称')
    tcmsyndrome = models.CharField(db_column='TCMsyndrome', max_length=50, blank=True, null=True,
                                   db_comment='门（急）诊诊断（中医证候）名称')
    tcmsyndromecode = models.CharField(db_column='TCMsyndromeCode', max_length=50, blank=True, null=True,
                                       db_comment='门（急）诊诊断（中医证候）证候编码')
    tcmsyndromename = models.CharField(db_column='TCMsyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='门（急）诊诊断（中医证候）证候名称')
    wmd = models.CharField(db_column='WMD', max_length=50, blank=True, null=True,
                           db_comment='门（急）诊诊断（西医诊断）名称')
    wmddiseasecode = models.CharField(db_column='WMDDiseaseCode', max_length=50, blank=True, null=True,
                                      db_comment='门（急）诊诊断（西医诊断）疾病编码')
    wmddiseasename = models.CharField(db_column='WMDDiseaseName', max_length=50, blank=True, null=True,
                                      db_comment='门（急）诊诊断（西医诊断）疾病名称')
    nopathology = models.CharField(db_column='NoPathology', max_length=50, blank=True, null=True,
                                   db_comment='病理号')
    pathologicaldiagdesc = models.CharField(db_column='pathologicalDiagDesc', max_length=50, blank=True, null=True,
                                            db_comment='病理诊断名称')
    pathologicaldiagdiseasecode = models.CharField(db_column='pathologicalDiagDiseaseCode', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='病理诊断疾病编码')
    pathologicaldiagdiseasename = models.CharField(db_column='pathologicalDiagDiseaseName', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='病理诊断疾病名称')
    treatmentclscode = models.CharField(db_column='treatmentClsCode', max_length=50, blank=True, null=True,
                                        db_comment='治疗类别代码')
    treatmentclsname = models.CharField(db_column='treatmentClsName', max_length=50, blank=True, null=True,
                                        db_comment='治疗类别名称')
    clinicalpathwaycode = models.CharField(db_column='clinicalPathwayCode', max_length=50, blank=True, null=True,
                                           db_comment='实施临床路径标志代码')
    clinicalpathwayname = models.CharField(db_column='clinicalPathwayName', max_length=50, blank=True, null=True,
                                           db_comment='实施临床路径标志名称')
    diseasestatuscode = models.CharField(db_column='diseaseStatusCode', max_length=50, blank=True, null=True,
                                         db_comment='住院者疾病状态代码')
    diseasestatusname = models.CharField(db_column='diseaseStatusName', max_length=50, blank=True, null=True,
                                         db_comment='住院者疾病状态名称')
    externalcausesdamagedesc = models.TextField(db_column='externalCausesDamageDesc', blank=True, null=True,
                                                db_comment='损伤中毒的外部原因')
    externalcausesdiseasepoisoncode = models.CharField(db_column='externalCausesDiseasePoisonCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='损伤中毒的外部原因疾病编码')
    daysbeforeadmission = models.IntegerField(db_column='daysBeforeAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院前昏迷时间-d')
    hoursbeforeadmission = models.IntegerField(db_column='hoursBeforeAdmission', blank=True, null=True,
                                               db_comment='颅脑损伤患者入院前昏迷时间-h')
    minsbeforeadmission = models.IntegerField(db_column='minsBeforeAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院前昏迷时间-min')
    daysafteradmission = models.IntegerField(db_column='daysAfterAdmission', blank=True, null=True,
                                             db_comment='颅脑损伤患者入院后昏迷时间-d')
    hoursafteradmission = models.IntegerField(db_column='hoursAfterAdmission', blank=True, null=True,
                                              db_comment='颅脑损伤患者入院后昏迷时间-h')
    minsafteradmission = models.IntegerField(db_column='minsAfterAdmission', blank=True, null=True,
                                             db_comment='颅脑损伤患者入院后昏迷时间-min')
    transfersection = models.CharField(db_column='transferSection', max_length=50, blank=True, null=True,
                                       db_comment='转科科别')
    cdischargediagmain = models.CharField(db_column='cdischargeDiagMain', max_length=50, blank=True, null=True,
                                          db_comment='出院中医诊断-主病名称')
    cdischargediagmaintcmcode = models.CharField(db_column='cdischargeDiagMainTCMCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='出院中医诊断-主病编码')
    cdischargediagmaintcmname = models.CharField(db_column='cdischargeDiagMainTCMName', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='出院中医诊断-主病名称')
    cdischargediagmainillnesscode = models.CharField(db_column='cdischargeDiagMainIllnessCode', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院中医诊断-主病-入院病情代码')
    cdischargediagmainillnessname = models.CharField(db_column='cdischargeDiagMainIllnessName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院中医诊断-主病-入院病情名称')
    cdischargediagmaster = models.CharField(db_column='cdischargeDiagMaster', max_length=50, blank=True, null=True,
                                            db_comment='出院中医诊断-主证名称')
    cdischargediagmastercode = models.CharField(db_column='cdischargeDiagMasterCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='出院中医诊断-主证编码')
    cdischargediagmasterillnesscode = models.CharField(db_column='cdischargeDiagMasterIllnessCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='出院中医诊断-主证-入院病情代码')
    cdischargediagmasterillnessname = models.CharField(db_column='cdischargeDiagMasterIllnessName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='出院中医诊断-主证-入院病情名称')
    dischargediagmain = models.CharField(db_column='dischargeDiagMain', max_length=50, blank=True, null=True,
                                         db_comment='出院西医诊断-主要诊断名称')
    dischargediagmaindiseasecode = models.CharField(db_column='dischargeDiagMainDiseaseCode', max_length=50, blank=True,
                                                    null=True,
                                                    db_comment='出院西医诊断-主要诊断疾病编码')
    dischargediagmaindiseasename = models.CharField(db_column='dischargeDiagMainDiseaseName', max_length=50, blank=True,
                                                    null=True,
                                                    db_comment='出院西医诊断-主要诊断疾病名称')
    dischargediagmainillnesscode = models.CharField(db_column='dischargeDiagMainIllnessCode', max_length=50, blank=True,
                                                    null=True,
                                                    db_comment='出院西医诊断-主要诊断-入院病情代码')
    dischargediagmainillnessname = models.CharField(db_column='dischargeDiagMainIllnessName', max_length=50, blank=True,
                                                    null=True,
                                                    db_comment='出院西医诊断-主要诊断-入院病情名称')
    dischargediagother = models.CharField(db_column='dischargeDiagOther', max_length=50, blank=True, null=True,
                                          db_comment='出院西医诊断-其他诊断名称')
    dischargediagotherdiseasecode = models.CharField(db_column='dischargeDiagOtherDiseaseCode', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院西医诊断-其他诊断疾病编码')
    dischargediagotherdiseasename = models.CharField(db_column='dischargeDiagOtherDiseaseName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院西医诊断-其他诊断疾病名称')
    dischargediagotherillnesscode = models.CharField(db_column='dischargeDiagOtherIllnessCode', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院西医诊断-其他诊断-入院病情代码')
    dischargediagotherillnessname = models.CharField(db_column='dischargeDiagOtherIllnessName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='出院西医诊断-其他诊断-入院病情名称')
    leavingwaycode = models.CharField(db_column='leavingWayCode', max_length=50, blank=True, null=True,
                                      db_comment='离院方式代码')
    leavingwayname = models.CharField(db_column='leavingWayName', max_length=50, blank=True, null=True,
                                      db_comment='离院方式名称')
    planrcvorgname = models.CharField(db_column='planRcvOrgName', max_length=70, blank=True, null=True,
                                      db_comment='拟接收医疗机构名称')
    drugallergyflag = models.SmallIntegerField(db_column='drugAllergyFlag', blank=True, null=True,
                                               db_comment='药物过敏标志')
    allergicdrugsdesc = models.TextField(db_column='allergicDrugsDesc', blank=True, null=True,
                                         db_comment='过敏药物')
    abocode = models.CharField(db_column='ABOCode', max_length=50, blank=True, null=True,
                               db_comment='ABO血型代码')
    aboname = models.CharField(db_column='ABOName', max_length=50, blank=True, null=True,
                               db_comment='ABO血型名称')
    rhcode = models.CharField(db_column='RHCode', max_length=50, blank=True, null=True,
                              db_comment='Rh血型代码')
    rhname = models.CharField(db_column='RHName', max_length=50, blank=True, null=True,
                              db_comment='Rh血型名称')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=70, blank=True, null=True,
                                     db_comment='手术及操作名称')
    operationdatetime = models.CharField(db_column='operationDateTime', max_length=15, blank=True, null=True,
                                         db_comment='手术及操作日期')
    surgeonid = models.CharField(db_column='surgeonId', max_length=50, blank=True, null=True,
                                 db_comment='手术者工号')
    surgeonname = models.CharField(db_column='surgeonName', max_length=50, blank=True, null=True,
                                   db_comment='手术者姓名')
    firstassistantsurgeryid = models.CharField(db_column='firstAssistantSurgeryId', max_length=50, blank=True,
                                               null=True, db_comment='Ⅰ助工号')
    firstassistantsurgeryname = models.CharField(db_column='firstAssistantSurgeryName', max_length=50, blank=True,
                                                 null=True, db_comment='Ⅰ助姓名')
    secondassistantsurgeryid = models.CharField(db_column='secondAssistantSurgeryId', max_length=50, blank=True,
                                                null=True, db_comment='Ⅱ助工号')
    secondassistantsurgeryname = models.CharField(db_column='secondAssistantSurgeryName', max_length=50, blank=True,
                                                  null=True, db_comment='Ⅱ助姓名')
    operationdesc = models.CharField(db_column='operationDesc', max_length=80, blank=True, null=True,
                                     db_comment='手术及操作名称')
    surgicalgradecode = models.CharField(db_column='surgicalGradeCode', max_length=50, blank=True, null=True,
                                         db_comment='手术级别代码')
    surgicalgradename = models.CharField(db_column='surgicalGradeName', max_length=50, blank=True, null=True,
                                         db_comment='手术级别名称')
    surgicalincisionclscode = models.CharField(db_column='surgicalIncisionClsCode', max_length=50, blank=True,
                                               null=True, db_comment='手术切口类别代码')
    surgicalincisionclsname = models.CharField(db_column='surgicalIncisionClsName', max_length=50, blank=True,
                                               null=True, db_comment='手术切口类别名称')
    woundhealinggradecode = models.CharField(db_column='woundHealingGradeCode', max_length=50, blank=True, null=True,
                                             db_comment='切口愈合等级代码')
    woundhealinggradename = models.CharField(db_column='woundHealingGradeName', max_length=50, blank=True, null=True,
                                             db_comment='切口愈合等级名称')
    anesthesiamodecode = models.CharField(db_column='anesthesiaModeCode', max_length=50, blank=True, null=True,
                                          db_comment='麻醉方法代码')
    anesthesiamodename = models.CharField(db_column='anesthesiaModeName', max_length=50, blank=True, null=True,
                                          db_comment='麻醉方法名称')
    anesthesiologistid = models.CharField(db_column='anesthesiologistId', max_length=50, blank=True, null=True,
                                          db_comment='麻醉医师工号')
    anesthesiologistname = models.CharField(db_column='anesthesiologistName', max_length=50, blank=True, null=True,
                                            db_comment='麻醉医师姓名')
    times = models.IntegerField(blank=True, null=True, db_comment='住院次数')
    autopsydeadpatientflag = models.SmallIntegerField(db_column='autopsyDeadPatientFlag', blank=True, null=True,
                                                      db_comment='死亡患者尸检标志')
    medicalrecordqualitycode = models.CharField(db_column='medicalRecordQualityCode', max_length=50, blank=True,
                                                null=True, db_comment='病案质量代码')
    medicalrecordqualityname = models.CharField(db_column='medicalRecordQualityName', max_length=50, blank=True,
                                                null=True, db_comment='病案质量名称')
    qcdate = models.CharField(db_column='QCDate', max_length=8, blank=True, null=True,
                              db_comment='质控日期')
    qcphysicianid = models.CharField(db_column='QCPhysicianId', max_length=50, blank=True, null=True,
                                     db_comment='质控医师工号')
    qcphysicianname = models.CharField(db_column='QCPhysicianName', max_length=50, blank=True, null=True,
                                       db_comment='质控医师签名')
    qcnurseid = models.CharField(db_column='QCNurseId', max_length=50, blank=True, null=True,
                                 db_comment='质控护士工号')
    qcnursename = models.CharField(db_column='QCNurseName', max_length=50, blank=True, null=True,
                                   db_comment='质控护士签名')
    daysactualstay = models.IntegerField(db_column='daysActualStay', blank=True, null=True,
                                         db_comment='实际住院天数')
    dischargedatetime = models.CharField(db_column='dischargeDateTime', max_length=15, blank=True, null=True,
                                         db_comment='出院日期时间')
    dischargedeptid = models.CharField(db_column='DischargeDeptId', max_length=50, blank=True, null=True,
                                       db_comment='出院科别id')
    dischargedeptname = models.CharField(db_column='DischargeDeptName', max_length=50, blank=True, null=True,
                                         db_comment='出院科别')
    dischargewardid = models.CharField(db_column='DischargeWardId', max_length=50, blank=True, null=True,
                                       db_comment='出院病房id')
    dischargewardname = models.CharField(db_column='DischargeWardName', max_length=50, blank=True, null=True,
                                         db_comment='出院病房')
    readmissionin31dflag = models.SmallIntegerField(db_column='readmissionIn31dFlag', blank=True, null=True,
                                                    db_comment='出院31d内再住院标志')
    readmissionin32ddesc = models.CharField(db_column='readmissionIn32dDesc', max_length=100, blank=True, null=True,
                                            db_comment='出院31d内再住院目的')
    paymenttypecode = models.CharField(db_column='paymentTypeCode', max_length=50, blank=True, null=True,
                                       db_comment='医疗付费方式代码')
    paymenttypename = models.CharField(db_column='paymentTypeName', max_length=100, blank=True, null=True,
                                       db_comment='医疗付费方式名称')
    totalfee = models.DecimalField(db_column='totalFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                   db_comment='住院总费用')
    totalfeeself = models.DecimalField(db_column='totalFeeSelf', max_digits=10, decimal_places=2, blank=True, null=True,
                                       db_comment='住院总费用-自付金额')
    amedicalservicefee = models.DecimalField(db_column='aMedicalServiceFee', max_digits=10, decimal_places=2,
                                             blank=True, null=True,
                                             db_comment='综合医疗服务类-一般医疗服务费')
    atcmtreatmentfee = models.DecimalField(db_column='aTCMTreatmentFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True,
                                           db_comment='综合医疗服务类-一般医疗服务费-中医辨证论治费')
    atcmtreatmentconsultationfee = models.DecimalField(db_column='aTCMTreatmentConsultationFee', max_digits=10,
                                                       decimal_places=2, blank=True, null=True,
                                                       db_comment='综合医疗服务类-一般医疗服务费-中医辨证论治会诊费')
    atreatmentoperationfee = models.DecimalField(db_column='aTreatmentOperationFee', max_digits=10, decimal_places=2,
                                                 blank=True, null=True,
                                                 db_comment='综合医疗服务类-一般治疗操作费')
    anursingfee = models.DecimalField(db_column='aNursingFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='综合医疗服务类-护理费')
    aotherfee = models.DecimalField(db_column='aOtherFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='综合医疗服务类-其他费用')
    dpathologicaldiagfee = models.DecimalField(db_column='dPathologicalDiagFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='诊断类-病理诊断费')
    dlabdiagfee = models.DecimalField(db_column='dLabDiagFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='诊断类-实验室诊断费')
    dimagdiagfee = models.DecimalField(db_column='dImagDiagFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                       db_comment='诊断类-影像学诊断费')
    dclinicaldiagprojectfee = models.DecimalField(db_column='dClinicalDiagprojectFee', max_digits=10, decimal_places=2,
                                                  blank=True, null=True,
                                                  db_comment='诊断类-临床诊断项目费')
    tnonsurgicaltreatmentfee = models.DecimalField(db_column='tNonSurgicalTreatmentFee', max_digits=10,
                                                   decimal_places=2, blank=True, null=True,
                                                   db_comment='治疗类-非手术治疗项目费')
    tclinicalphysicaltherapyfee = models.DecimalField(db_column='tClinicalPhysicalTherapyFee', max_digits=10,
                                                      decimal_places=2, blank=True, null=True,
                                                      db_comment='治疗类-非手术治疗项目费-临床物理治疗费')
    tsurgicaltreatmentfee = models.DecimalField(db_column='tSurgicalTreatmentFee', max_digits=10, decimal_places=2,
                                                blank=True, null=True,
                                                db_comment='治疗类-手术治疗费')
    tanesthesiafee = models.DecimalField(db_column='tAnesthesiaFee', max_digits=10, decimal_places=2, blank=True,
                                         null=True, db_comment='治疗类-手术治疗费-麻醉费')
    toperationfee = models.DecimalField(db_column='tOperationFee', max_digits=10, decimal_places=2, blank=True,
                                        null=True, db_comment='治疗类-手术治疗费-手术费')
    hrehabilitationfee = models.DecimalField(db_column='hRehabilitationFee', max_digits=10, decimal_places=2,
                                             blank=True, null=True,
                                             db_comment='康复类-康复费')
    usetcminstitutionflag = models.SmallIntegerField(db_column='UseTCMInstitutionFlag', blank=True, null=True,
                                                     db_comment='使用医疗机构中药制剂标志')
    usetcmflag = models.SmallIntegerField(db_column='UseTCMFlag', blank=True, null=True,
                                          db_comment='使用中医诊疗技术标志')
    syndromediffnurseflag = models.SmallIntegerField(db_column='SyndromeDiffNurseFlag', blank=True, null=True,
                                                     db_comment='辨证施护标志')
    ctcmdiagnosisfee = models.DecimalField(db_column='cTCMDiagnosisFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True, db_comment='中医类-中医诊断费')
    ctcmtreatmentfee = models.DecimalField(db_column='cTCMTreatmentFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True, db_comment='中医类-中医治疗费')
    ctcmtreatmentextfee = models.DecimalField(db_column='cTCMTreatmentExtFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='中医类-中医治疗费-中医外治费')
    ctcmtreatmentbonefee = models.DecimalField(db_column='cTCMTreatmentBoneFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='中医类-中医治疗费-中医骨伤费')
    ctcmtreatmentacufee = models.DecimalField(db_column='cTCMTreatmentAcuFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='中医类-中医治疗费-针刺与灸法费')
    ctcmtreatmentmassagefee = models.DecimalField(db_column='cTCMTreatmentMassageFee', max_digits=10, decimal_places=2,
                                                  blank=True, null=True,
                                                  db_comment='中医类-中医治疗费-中医推拿治疗费')
    ctcmtreatmentanorectalfee = models.DecimalField(db_column='cTCMTreatmentAnorectalFee', max_digits=10,
                                                    decimal_places=2, blank=True, null=True,
                                                    db_comment='中医类-中医治疗费-中医肛肠治疗费')
    ctcmtreatmentspecialfee = models.DecimalField(db_column='cTCMTreatmentSpecialFee', max_digits=10, decimal_places=2,
                                                  blank=True, null=True,
                                                  db_comment='中医类-中医治疗费-中医特殊治疗费')
    ctcmtreatmentotherfee = models.DecimalField(db_column='cTCMTreatmentOtherFee', max_digits=10, decimal_places=2,
                                                blank=True, null=True,
                                                db_comment='中医类-中医其他费')
    ctcmtreatmentprocessfee = models.DecimalField(db_column='cTCMTreatmentProcessFee', max_digits=10, decimal_places=2,
                                                  blank=True, null=True,
                                                  db_comment='中医类-中医其他费-中医特殊调配加工费')
    ctcmtreatmentfoodfee = models.DecimalField(db_column='cTCMTreatmentFoodFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='中医类-中医其他费-辨证施膳费')
    wwesternmedicinefee = models.DecimalField(db_column='wWesternMedicineFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='西药类-西药费')
    wantibioticsfee = models.DecimalField(db_column='wAntibioticsFee', max_digits=10, decimal_places=2, blank=True,
                                          null=True,
                                          db_comment='西药类-西药费-抗菌药物费用')
    ecpmfee = models.DecimalField(db_column='eCPMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                  db_comment='中药类-中成药费')
    ecpmmakefee = models.DecimalField(db_column='eCPMMakeFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='中药类-中成药费-医疗机构中药制剂费')
    echmfee = models.DecimalField(db_column='eCHMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                  db_comment='中药类-中草药费')
    bbloodfee = models.DecimalField(db_column='bBloodFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='血液和血液制品类-血费')
    balbuminproductsfee = models.DecimalField(db_column='bAlbuminProductsFee', max_digits=10, decimal_places=2,
                                              blank=True, null=True,
                                              db_comment='血液和血液制品类-白蛋白类制品费')
    bglobulinproductsfee = models.DecimalField(db_column='bGlobulinProductsFee', max_digits=10, decimal_places=2,
                                               blank=True, null=True,
                                               db_comment='血液和血液制品类-球蛋白类制品费')
    bcoagulationfactorproducts = models.DecimalField(db_column='bCoagulationFactorProducts', max_digits=10,
                                                     decimal_places=2, blank=True, null=True,
                                                     db_comment='血液和血液制品类-凝血因子类制品费')
    bcytokineproducts = models.DecimalField(db_column='bCytokineProducts', max_digits=10, decimal_places=2, blank=True,
                                            null=True,
                                            db_comment='血液和血液制品类-细胞因子类制品费')
    ctcmdevflag = models.SmallIntegerField(db_column='cTCMDevFlag', blank=True, null=True,
                                           db_comment='使用中医诊疗设备标志')
    fexamdmmfee = models.DecimalField(db_column='fExamDMMFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                      db_comment='耗材类-检查用一次性医用材料费')
    ftraeatdmmfee = models.DecimalField(db_column='fTraeatDMMFee', max_digits=10, decimal_places=2, blank=True,
                                        null=True,
                                        db_comment='耗材类-治疗用一次性医用材料费')
    foperationdmmfee = models.DecimalField(db_column='fOperationDMMFee', max_digits=10, decimal_places=2, blank=True,
                                           null=True,
                                           db_comment='耗材类-手术用一次性医用材料费')
    ootherfee = models.DecimalField(db_column='oOtherFee', max_digits=10, decimal_places=2, blank=True, null=True,
                                    db_comment='其他类-其他费')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    externalcausesdiseasepoisonname = models.TextField(db_column='externalCausesDiseasePoisonName', blank=True,
                                                       null=True)
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    cdischargediagmastername = models.CharField(db_column='cdischargeDiagMasterName', max_length=50, blank=True,
                                                null=True)
    fzyid = models.CharField(db_column='FZYID', max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0034(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    state = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-省（自治区、直辖市）')
    city = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-市（地区、州）')
    county = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-县（区）')
    township = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=70, blank=True, null=True,
                                  db_comment='地址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=70, blank=True, null=True,
                                   db_comment='地址-门牌号码')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=100, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=100, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=100, blank=True, null=True,
                                       db_comment='民族名称')
    age = models.CharField(max_length=100, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    occupationcode = models.CharField(db_column='occupationCode', max_length=100, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=100, blank=True, null=True,
                                      db_comment='职业类别名称')
    createdate = models.CharField(db_column='createDate', max_length=8, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    historynarratorid = models.CharField(db_column='historyNarratorId', max_length=100, blank=True, null=True,
                                         db_comment='病史陈述者号码')
    historynarrator = models.CharField(db_column='historyNarrator', max_length=50, blank=True, null=True,
                                       db_comment='病史陈述者姓名')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=100, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=100, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系名称')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    chiefphysiciansignaturedatetime = models.CharField(db_column='chiefPhysicianSignatureDateTime', max_length=15,
                                                       blank=True, null=True,
                                                       db_comment='主任医师签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    rcvphysiciansignaturedatetime = models.CharField(db_column='rcvPhysicianSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='接诊医师签名日期时间')
    rcvphysicianid = models.CharField(db_column='rcvPhysicianId', max_length=50, blank=True, null=True,
                                      db_comment='接诊医师工号')
    rcvphysicianname = models.CharField(db_column='rcvPhysicianName', max_length=50, blank=True, null=True,
                                        db_comment='接诊医师签名')
    residentsignaturedatetime = models.CharField(db_column='residentSignatureDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='住院医师签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师工号')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师签名')
    attenddoctorsignaturedatetime = models.CharField(db_column='attendDoctorSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='住院医师签名日期时间')
    attenddoctorid = models.CharField(db_column='attendDoctorId', max_length=50, blank=True, null=True,
                                      db_comment='主治医师工号')
    attenddoctorname = models.CharField(db_column='attendDoctorName', max_length=50, blank=True, null=True,
                                        db_comment='主治医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    presentillnesshistory = models.TextField(db_column='presentIllnessHistory', blank=True, null=True,
                                             db_comment='现病史')
    generalhealthflag = models.SmallIntegerField(db_column='generalHealthFlag', blank=True, null=True,
                                                 db_comment='一般健康状况标志')
    diseasehistory = models.TextField(db_column='diseaseHistory', blank=True, null=True,
                                      db_comment='疾病史（含外伤）')
    patientinfectiouflag = models.SmallIntegerField(db_column='patientInfectiouFlag', blank=True, null=True,
                                                    db_comment='患者传染性标志')
    infectioushistory = models.TextField(db_column='infectiousHistory', blank=True, null=True,
                                         db_comment='传染病史')
    vaccinationhistory = models.TextField(db_column='vaccinationHistory', blank=True, null=True,
                                          db_comment='预防接种史')
    surgicalhistory = models.TextField(db_column='surgicalHistory', blank=True, null=True,
                                       db_comment='手术史')
    bloodtransfusionhistory = models.TextField(db_column='bloodTransfusionHistory', blank=True, null=True,
                                               db_comment='输血史')
    allergichistory = models.TextField(db_column='allergicHistory', blank=True, null=True,
                                       db_comment='过敏史')
    personalhistory = models.TextField(db_column='personalHistory', blank=True, null=True,
                                       db_comment='个人史')
    marriagechildbearinghistory = models.TextField(db_column='marriageChildbearingHistory', blank=True, null=True,
                                                   db_comment='婚育史')
    menstrualhistory = models.TextField(db_column='menstrualHistory', blank=True, null=True,
                                        db_comment='月经史')
    familyhistory = models.TextField(db_column='familyHistory', blank=True, null=True,
                                     db_comment='家族史')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
                                      db_comment='体格检查--体温（℃）')
    pulserate = models.CharField(db_column='pulseRate', max_length=100, blank=True, null=True,
                                 db_comment='体格检查--脉率（次/min）')
    respiratoryrate = models.CharField(db_column='respiratoryRate', max_length=100, blank=True, null=True,
                                       db_comment='体格检查--呼吸频率（次/min）')
    systolicpressure = models.CharField(db_column='systolicPressure', max_length=100, blank=True, null=True,
                                        db_comment='体格检查--收缩压（mmHg）')
    diastolicpressure = models.CharField(db_column='diastolicPressure', max_length=100, blank=True, null=True,
                                         db_comment='体格检查--舒张压（mmHg）')
    height = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True,
                                 db_comment='体格检查--身高（cm）')
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                 db_comment='体格检查--体重（kg）')
    generalexamresult = models.TextField(db_column='generalExamResult', blank=True, null=True,
                                         db_comment='体格检查--一般状况检查结果')
    skinmucousmembraneexamresults = models.TextField(db_column='skinMucousMembraneExamResults', blank=True, null=True,
                                                     db_comment='体格检查--皮肤和黏膜检查结果')
    lymphexaminationresults = models.TextField(db_column='lymphExaminationResults', blank=True, null=True,
                                               db_comment='体格检查--全身浅表淋巴结检查结果')
    headorgansexaminationresults = models.TextField(db_column='headOrgansExaminationResults', blank=True, null=True,
                                                    db_comment='体格检查--头部及其器官检查结果')
    neckexaminationresults = models.TextField(db_column='neckExaminationResults', blank=True, null=True,
                                              db_comment='体格检查--颈部检查结果')
    chestexaminationresults = models.TextField(db_column='chestExaminationResults', blank=True, null=True,
                                               db_comment='体格检查--胸部检查结果')
    abdominalexaminationresults = models.TextField(db_column='abdominalExaminationResults', blank=True, null=True,
                                                   db_comment='体格检查--腹部检查结果')
    analdigitalexaminationresults = models.TextField(db_column='analDigitalExaminationResults', blank=True, null=True,
                                                     db_comment='体格检查--肛门指诊检查结果描述')
    extgenitalexaminationresults = models.TextField(db_column='extGenitalExaminationResults', blank=True, null=True,
                                                    db_comment='体格检查--外生殖器检查结果')
    spinalexaminationresults = models.TextField(db_column='spinalExaminationResults', blank=True, null=True,
                                                db_comment='体格检查--脊柱检查结果')
    limbexaminationresults = models.TextField(db_column='limbExaminationResults', blank=True, null=True,
                                              db_comment='体格检查--四肢检查结果')
    neurologicalexaminationresults = models.TextField(db_column='NeurologicalExaminationResults', blank=True, null=True,
                                                      db_comment='体格检查--神经系统检查结果')
    specialtysituation = models.TextField(db_column='specialtySituation', blank=True, null=True,
                                          db_comment='专科情况')
    auxiliaryinspectionresults = models.TextField(db_column='auxiliaryInspectionResults', blank=True, null=True,
                                                  db_comment='辅助检查结果')
    contentreliableflag = models.SmallIntegerField(db_column='contentReliableFlag', blank=True, null=True,
                                                   db_comment='陈述内容可靠标志')
    initialdiagnosisdatea = models.CharField(db_column='initialDiagnosisDateA', max_length=8, blank=True, null=True,
                                             db_comment='初步诊断日期')
    initialdiagnosiscode = models.CharField(db_column='initialDiagnosisCode', max_length=50, blank=True, null=True,
                                            db_comment='初步诊断-西医诊断名称')
    initialdiagnosisname = models.CharField(db_column='initialDiagnosisName', max_length=100, blank=True, null=True,
                                            db_comment='初步诊断-西医诊断编码')
    seqadmissiondiaga = models.CharField(db_column='seqAdmissionDiagA', max_length=100, blank=True, null=True,
                                         db_comment='入院诊断顺位')
    observationresults = models.TextField(db_column='observationResults', blank=True, null=True,
                                          db_comment='中医“四诊”观察结果')
    initialdiagnosisdateb = models.CharField(db_column='initialDiagnosisDateB', max_length=8, blank=True, null=True,
                                             db_comment='初步诊断日期')
    initialtcmdiseasename = models.CharField(db_column='initialTCMDiseaseName', max_length=50, blank=True, null=True,
                                             db_comment='初步诊断-中医病名名称')
    initialtcmdiseasecode = models.CharField(db_column='initialTCMDiseaseCode', max_length=100, blank=True, null=True,
                                             db_comment='初步诊断-中医病名代码')
    initialtcmsyndromename = models.CharField(db_column='initialTCMsyndromeName', max_length=50, blank=True, null=True,
                                              db_comment='初步诊断-中医证候名称')
    initialtcmsyndromecode = models.CharField(db_column='initialTCMsyndromeCode', max_length=100, blank=True, null=True,
                                              db_comment='初步诊断-中医证候代码')
    seqadmissiondiagnosisb = models.CharField(db_column='seqAdmissionDiagnosisB', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    correcteddiagnosisdatec = models.CharField(db_column='correctedDiagnosisDateC', max_length=8, blank=True, null=True,
                                               db_comment='修正诊断日期')
    correcteddiagnosiscode = models.CharField(db_column='correctedDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='修正诊断-西医诊断名称')
    correcteddiagnosisname = models.CharField(db_column='correctedDiagnosisName', max_length=100, blank=True, null=True,
                                              db_comment='修正诊断-西医诊断编码')
    seqadmissiondiagnosisc = models.CharField(db_column='seqAdmissionDiagnosisC', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    correcteddiagnosisdated = models.CharField(db_column='correctedDiagnosisDateD', max_length=8, blank=True, null=True,
                                               db_comment='修正诊断日期')
    correctedtcmdiseasename = models.CharField(db_column='correctedTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='修正诊断-中医病名名称')
    correctedtcmdiseasecode = models.CharField(db_column='correctedTCMDiseaseCode', max_length=100, blank=True,
                                               null=True,
                                               db_comment='修正诊断-中医病名代码')
    correctedtcmsyndromename = models.CharField(db_column='correctedTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='修正诊断-中医证候名称')
    correctedtcmsyndromecode = models.CharField(db_column='correctedTCMsyndromeCode', max_length=100, blank=True,
                                                null=True,
                                                db_comment='修正诊断-中医证候代码')
    seqadmissiondiagnosisd = models.CharField(db_column='seqAdmissionDiagnosisD', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    determinediagnosisdatee = models.CharField(db_column='determineDiagnosisDateE', max_length=8, blank=True, null=True,
                                               db_comment='确定诊断日期')
    determinediagnosiscode = models.CharField(db_column='determineDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='确定诊断-西医诊断名称')
    determinediagnosisname = models.CharField(db_column='determineDiagnosisName', max_length=100, blank=True, null=True,
                                              db_comment='确定诊断-西医诊断编码')
    seqadmissiondiagnosise = models.CharField(db_column='seqAdmissionDiagnosisE', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    determinediagnosisdatef = models.CharField(db_column='determineDiagnosisDateF', max_length=8, blank=True, null=True,
                                               db_comment='确定诊断日期')
    determinetcmdiseasename = models.CharField(db_column='determineTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='确定诊断-中医病名名称')
    determinetcmdiseasecode = models.CharField(db_column='determineTCMDiseaseCode', max_length=100, blank=True,
                                               null=True,
                                               db_comment='确定诊断-中医病名代码')
    determinetcmsyndromename = models.CharField(db_column='determineTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='确定诊断-中医证候名称')
    determinetcmsyndromecode = models.CharField(db_column='determineTCMsyndromeCode', max_length=100, blank=True,
                                                null=True,
                                                db_comment='确定诊断-中医证候代码')
    seqadmissiondiagnosisf = models.CharField(db_column='seqAdmissionDiagnosisF', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    supplementarydiagnosisdateg = models.CharField(db_column='supplementaryDiagnosisDateG', max_length=8, blank=True,
                                                   null=True, db_comment='补充诊断日期')
    supplementarydiagnosiscode = models.CharField(db_column='supplementaryDiagnosisCode', max_length=50, blank=True,
                                                  null=True, db_comment='补充诊断名称')
    supplementarydiagnosisname = models.CharField(db_column='supplementaryDiagnosisName', max_length=100, blank=True,
                                                  null=True, db_comment='补充诊断编码')
    seqadmissiondiagnosisg = models.CharField(db_column='seqAdmissionDiagnosisG', max_length=100, blank=True, null=True,
                                              db_comment='入院诊断顺位')
    treatmentmethods = models.CharField(db_column='treatmentMethods', max_length=100, blank=True, null=True,
                                        db_comment='治则治法')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0035(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    state = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-省（自治区、直辖市）')
    city = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-市（地区、州）')
    county = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-县（区）')
    township = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=70, blank=True, null=True,
                                  db_comment='地址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=70, blank=True, null=True,
                                   db_comment='地址-门牌号码')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=2, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=18, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=2, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=18, blank=True, null=True,
                                       db_comment='民族名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    occupationcode = models.CharField(db_column='occupationCode', max_length=20, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=100, blank=True, null=True,
                                      db_comment='职业类别名称')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    historynarratorid = models.CharField(db_column='historyNarratorId', max_length=18, blank=True, null=True,
                                         db_comment='病史陈述者号码')
    historynarrator = models.CharField(db_column='historyNarrator', max_length=50, blank=True, null=True,
                                       db_comment='病史陈述者姓名')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=20, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=100, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系名称')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    chiefphysiciansignaturedatetime = models.CharField(db_column='chiefPhysicianSignatureDateTime', max_length=15,
                                                       blank=True, null=True,
                                                       db_comment='主任医师签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    rcvphysiciansignaturedatetime = models.CharField(db_column='rcvPhysicianSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='接诊医师签名日期时间')
    rcvphysicianid = models.CharField(db_column='rcvPhysicianId', max_length=50, blank=True, null=True,
                                      db_comment='接诊医师工号')
    rcvphysicianname = models.CharField(db_column='rcvPhysicianName', max_length=50, blank=True, null=True,
                                        db_comment='接诊医师签名')
    residentsignaturedatetime = models.CharField(db_column='residentSignatureDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='住院医师签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师工号')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师签名')
    attenddoctorsignaturedatetime = models.CharField(db_column='attendDoctorSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='住院医师签名日期时间')
    attenddoctorid = models.CharField(db_column='attendDoctorId', max_length=50, blank=True, null=True,
                                      db_comment='主治医师工号')
    attenddoctorname = models.CharField(db_column='attendDoctorName', max_length=50, blank=True, null=True,
                                        db_comment='主治医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    dischargedatetime = models.CharField(db_column='dischargeDateTime', max_length=15, blank=True, null=True,
                                         db_comment='出院日期时间')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    presentillnesshistory = models.TextField(db_column='presentIllnessHistory', blank=True, null=True,
                                             db_comment='现病史')
    contentreliableflag = models.SmallIntegerField(db_column='contentReliableFlag', blank=True, null=True,
                                                   db_comment='陈述内容可靠标志')
    symptomname = models.CharField(db_column='symptomName', max_length=50, blank=True, null=True,
                                   db_comment='症状名称')
    symptomdesc = models.TextField(db_column='symptomDesc', blank=True, null=True,
                                   db_comment='症状描述')
    observationresults = models.TextField(db_column='observationResults', blank=True, null=True,
                                          db_comment='中医“四诊”观察结果')
    admissiondiagnosisname = models.TextField(db_column='admissionDiagnosisName', blank=True, null=True,
                                              db_comment='入院诊断-西医诊断名称')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=20, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断编码')
    admissiontcmdiseasename = models.TextField(db_column='admissionTCMDiseaseName', blank=True, null=True,
                                               db_comment='入院诊断-中医病名名称')
    admissiontcmdiseasecode = models.CharField(db_column='admissionTCMDiseaseCode', max_length=20, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名代码')
    admissiontcmsyndromename = models.TextField(db_column='admissionTCMsyndromeName', blank=True, null=True,
                                                db_comment='入院诊断-中医证候名称')
    admissiontcmsyndromecode = models.CharField(db_column='admissionTCMsyndromeCode', max_length=20, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候代码')
    treatmentmethods = models.TextField(db_column='treatmentMethods', blank=True, null=True,
                                        db_comment='治则治法')
    admissiondesc = models.TextField(db_column='admissionDesc', blank=True, null=True,
                                     db_comment='入院情况')
    examprocessdesc = models.TextField(db_column='examProcessDesc', blank=True, null=True,
                                       db_comment='诊疗过程描述')
    dischargedesc = models.TextField(db_column='dischargeDesc', blank=True, null=True,
                                     db_comment='出院情况')
    dischargediagnosisname = models.TextField(db_column='dischargeDiagnosisName', blank=True, null=True,
                                              db_comment='出院诊断-西医诊断名称')
    dischargediagnosiscode = models.CharField(db_column='dischargeDiagnosisCode', max_length=20, blank=True, null=True,
                                              db_comment='出院诊断-西医诊断编码')
    dischargetcmdiseasename = models.TextField(db_column='dischargeTCMDiseaseName', blank=True, null=True,
                                               db_comment='出院诊断-中医病名名称')
    dischargetcmdiseasecode = models.CharField(db_column='dischargeTCMDiseaseCode', max_length=20, blank=True,
                                               null=True,
                                               db_comment='出院诊断-中医病名代码')
    dischargetcmsyndromename = models.TextField(db_column='dischargeTCMsyndromeName', blank=True, null=True,
                                                db_comment='出院诊断-中医证候名称')
    dischargetcmsyndromecode = models.CharField(db_column='dischargeTCMsyndromeCode', max_length=20, blank=True,
                                                null=True,
                                                db_comment='出院诊断-中医证候代码')
    dischargeorder = models.TextField(db_column='dischargeOrder', blank=True, null=True,
                                      db_comment='出院医嘱')
    dischargeorderissuedatetime = models.CharField(db_column='dischargeOrderIssueDateTime', max_length=15, blank=True,
                                                   null=True,
                                                   db_comment='出院医嘱开立日期时间')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0036(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    state = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-省（自治区、直辖市）')
    city = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-市（地区、州）')
    county = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-县（区）')
    township = models.CharField(max_length=70, blank=True, null=True, db_comment='地址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=70, blank=True, null=True,
                                  db_comment='地址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=70, blank=True, null=True,
                                   db_comment='地址-门牌号码')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    ethnicgroupcode = models.CharField(db_column='ethnicGroupCode', max_length=50, blank=True, null=True,
                                       db_comment='民族代码')
    ethnicgroupname = models.CharField(db_column='ethnicGroupName', max_length=50, blank=True, null=True,
                                       db_comment='民族名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    occupationcode = models.CharField(db_column='occupationCode', max_length=50, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=50, blank=True, null=True,
                                      db_comment='职业类别名称')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    historynarratorid = models.CharField(db_column='historyNarratorId', max_length=50, blank=True, null=True,
                                         db_comment='病史陈述者号码')
    historynarrator = models.CharField(db_column='historyNarrator', max_length=50, blank=True, null=True,
                                       db_comment='病史陈述者姓名')
    associatedentityrelcode = models.CharField(db_column='associatedEntityRelCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系代码')
    associatedentityrelname = models.CharField(db_column='associatedEntityRelName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='病史陈述者与患者的关系名称')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    chiefphysiciansignaturedatetime = models.CharField(db_column='chiefPhysicianSignatureDateTime', max_length=15,
                                                       blank=True, null=True,
                                                       db_comment='主任医师签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    rcvphysiciansignaturedatetime = models.CharField(db_column='rcvPhysicianSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='接诊医师签名日期时间')
    rcvphysicianid = models.CharField(db_column='rcvPhysicianId', max_length=50, blank=True, null=True,
                                      db_comment='接诊医师工号')
    rcvphysicianname = models.CharField(db_column='rcvPhysicianName', max_length=50, blank=True, null=True,
                                        db_comment='接诊医师签名')
    residentsignaturedatetime = models.CharField(db_column='residentSignatureDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='住院医师签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师工号')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师签名')
    attenddoctorsignaturedatetime = models.CharField(db_column='attendDoctorSignatureDateTime', max_length=15,
                                                     blank=True, null=True,
                                                     db_comment='住院医师签名日期时间')
    attenddoctorid = models.CharField(db_column='attendDoctorId', max_length=50, blank=True, null=True,
                                      db_comment='主治医师工号')
    attenddoctorname = models.CharField(db_column='attendDoctorName', max_length=50, blank=True, null=True,
                                        db_comment='主治医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    contentreliableflag = models.SmallIntegerField(db_column='contentReliableFlag', blank=True, null=True,
                                                   db_comment='陈述内容可靠标志')
    observationresults = models.TextField(db_column='observationResults', blank=True, null=True,
                                          db_comment='中医“四诊”观察结果')
    admissiondiagnosisname = models.CharField(db_column='admissionDiagnosisName', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断名称')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断编码')
    admissiontcmdiseasename = models.CharField(db_column='admissionTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名名称')
    admissiontcmdiseasecode = models.CharField(db_column='admissionTCMDiseaseCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名代码')
    admissiontcmsyndromename = models.CharField(db_column='admissionTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候名称')
    admissiontcmsyndromecode = models.CharField(db_column='admissionTCMsyndromeCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候代码')
    treatmentmethods = models.CharField(db_column='treatmentMethods', max_length=100, blank=True, null=True,
                                        db_comment='治则治法')
    admissiondesc = models.TextField(db_column='admissionDesc', blank=True, null=True,
                                     db_comment='入院情况')
    examprocessdesc = models.TextField(db_column='examProcessDesc', blank=True, null=True,
                                       db_comment='诊疗过程描述')
    deathdatetime = models.CharField(db_column='deathDateTime', max_length=15, blank=True, null=True,
                                     db_comment='死亡日期时间')
    deathcause = models.CharField(db_column='deathCause', max_length=100, blank=True, null=True,
                                  db_comment='死亡原因')
    deathdiagnosisname = models.CharField(db_column='deathDiagnosisName', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断-西医诊断名称')
    deathdiagnosiscode = models.CharField(db_column='deathDiagnosisCode', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断-西医诊断编码')
    deathtcmdiseasename = models.CharField(db_column='deathTCMDiseaseName', max_length=50, blank=True, null=True,
                                           db_comment='死亡诊断-中医病名名称')
    deathtcmdiseasecode = models.CharField(db_column='deathTCMDiseaseCode', max_length=50, blank=True, null=True,
                                           db_comment='死亡诊断-中医病名代码')
    deathtcmsyndromename = models.CharField(db_column='deathTCMsyndromeName', max_length=50, blank=True, null=True,
                                            db_comment='死亡诊断-中医证候名称')
    deathtcmsyndromecode = models.CharField(db_column='deathTCMsyndromeCode', max_length=50, blank=True, null=True,
                                            db_comment='死亡诊断-中医证候代码')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0037(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=50, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=50, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师ID')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师签名')
    superiorphysicianid = models.CharField(db_column='superiorPhysicianId', max_length=50, blank=True, null=True,
                                           db_comment='上级医师ID')
    superiorphysicianname = models.CharField(db_column='superiorPhysicianName', max_length=50, blank=True, null=True,
                                             db_comment='上级医师姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    casecharacteristics = models.TextField(db_column='caseCharacteristics', blank=True, null=True,
                                           db_comment='病例特点')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    diagnosticbasis = models.TextField(db_column='diagnosticBasis', blank=True, null=True,
                                       db_comment='诊断依据')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=50, blank=True, null=True,
                                             db_comment='初步诊断-西医诊断编码')
    westerndiagnosticname = models.TextField(db_column='westernDiagnosticName', blank=True, null=True,
                                             db_comment='初步诊断-西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=50, blank=True, null=True,
                                      db_comment='初步诊断-中医病名代码')
    tcmdiseasename = models.TextField(db_column='TCMDiseaseName', blank=True, null=True,
                                      db_comment='初步诊断-中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=50, blank=True, null=True,
                                       db_comment='初步诊断-中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='初步诊断-中医证候名称')
    differentialdiagnosiswesternmedicinediagnosiscode = models.CharField(
        db_column='differentialDiagnosisWesternMedicineDiagnosisCode', max_length=50, blank=True, null=True,
        db_comment='鉴别诊断-西医诊断代码')
    differentialdiagnosiswesternmedicinediagnosisname = models.CharField(
        db_column='differentialDiagnosisWesternMedicineDiagnosisName', max_length=50, blank=True, null=True,
        db_comment='鉴别诊断-西医诊断名称')
    differentialdiagnosistcmdiseasecode = models.CharField(db_column='differentialDiagnosisTCMDiseaseCode',
                                                           max_length=50, blank=True, null=True,
                                                           db_comment='鉴别诊断-中医病名代码')
    differentialdiagnosistcmdiseasename = models.CharField(db_column='differentialDiagnosisTCMDiseaseName',
                                                           max_length=50, blank=True, null=True,
                                                           db_comment='鉴别诊断-中医病名名称')
    differentialdiagnosistcmsyndromecode = models.CharField(db_column='differentialDiagnosisTCMSyndromeCode',
                                                            max_length=50, blank=True, null=True,
                                                            db_comment='鉴别诊断-中医证候代码')
    differentialdiagnosistcmsyndromename = models.CharField(db_column='differentialDiagnosisTCMSyndromeName',
                                                            max_length=50, blank=True, null=True,
                                                            db_comment='鉴别诊断-中医证候名称')
    diagnosistreatmentplan = models.TextField(db_column='diagnosisTreatmentPlan', blank=True, null=True,
                                              db_comment='诊疗计划')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0038(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    physiciansignatureid = models.CharField(db_column='physicianSignatureId', max_length=50, blank=True, null=True,
                                            db_comment='医师工号')
    physiciansignaturename = models.CharField(db_column='physicianSignatureName', max_length=50, blank=True, null=True,
                                              db_comment='医师签名')
    occupationcode = models.CharField(db_column='occupationCode', max_length=20, blank=True, null=True,
                                      db_comment='专业技术职务类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=100, blank=True, null=True,
                                      db_comment='专业技术职务类别名称')
    recorddatetime = models.CharField(db_column='recordDateTime', max_length=15, blank=True, null=True,
                                      db_comment='记录日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    hospitalizationcourse = models.TextField(db_column='hospitalizationCourse', blank=True, null=True,
                                             db_comment='住院病程')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    orderablecontent = models.TextField(db_column='orderableContent', blank=True, null=True,
                                        db_comment='医嘱内容?')
    detailsyndromedifftreatdesc = models.TextField(db_column='detailSyndromeDiffTreatDesc', blank=True, null=True,
                                                   db_comment='辨证论治详细描述')
    decoctmethodtcm = models.CharField(db_column='decoctMethodTCM', max_length=100, blank=True, null=True,
                                       db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0039(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    chiefphysiciandatetime = models.CharField(db_column='chiefPhysicianDateTime', max_length=15, blank=True, null=True,
                                              db_comment='签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    recorderid = models.CharField(db_column='recorderId', max_length=50, blank=True, null=True,
                                  db_comment='记录人ID')
    signaturerecorder = models.CharField(db_column='signatureRecorder', max_length=50, blank=True, null=True,
                                         db_comment='记录人签名')
    attendingdoctordatetime = models.CharField(db_column='attendingDoctorDateTime', max_length=15, blank=True,
                                               null=True, db_comment='签名日期时间')
    attendingdoctorsignatureid = models.CharField(db_column='attendingDoctorSignatureId', max_length=50, blank=True,
                                                  null=True, db_comment='主治医师工号')
    attendingdoctorsignature = models.CharField(db_column='attendingDoctorSignature', max_length=50, blank=True,
                                                null=True, db_comment='主治医师签名')
    wardrounddatetime = models.CharField(db_column='wardRoundDateTime', max_length=15, blank=True, null=True,
                                         db_comment='查房日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    wardroundrecord = models.TextField(db_column='wardRoundRecord', blank=True, null=True,
                                       db_comment='查房记录')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    diagnosistreatmentplan = models.TextField(db_column='diagnosisTreatmentPlan', blank=True, null=True,
                                              db_comment='诊疗计划')
    detaileddescriptionsyndromedifferentiationtreatment = models.TextField(
        db_column='detailedDescriptionSyndromeDifferentiationTreatment', blank=True, null=True,
        db_comment='辨证论治详细描述')
    orderablecontent = models.TextField(db_column='orderableContent', blank=True, null=True,
                                        db_comment='医嘱内容?')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0040(models.Model):
    doc_id = models.CharField(max_length=32, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField('患者身份证件号码', max_length=32, db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField("性别名称", max_length=20, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    age_unit = models.CharField('年龄单位', max_length=10, db_comment='年龄单位')
    discussiondatetime = models.CharField(db_column='discussionDateTime', max_length=15, blank=True, null=True,
                                          db_comment='讨论日期时间')
    discussionplace = models.CharField(db_column='discussionPlace', max_length=50, blank=True, null=True,
                                       db_comment='讨论地点')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=20, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=10, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    physicianid = models.CharField(db_column='physicianId', max_length=50, blank=True, null=True,
                                   db_comment='医师id')
    physicianname = models.CharField(db_column='physicianName', max_length=50, blank=True, null=True,
                                     db_comment='医师签名')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='主治医师工号')
    attendingdoctorname = models.CharField(db_column='attendingDoctorName', max_length=50, blank=True, null=True,
                                           db_comment='主治医师签名')
    hostid = models.CharField(db_column='hostId', max_length=50, blank=True, null=True,
                              db_comment='主持人id')
    hostname = models.CharField(db_column='hostName', max_length=50, blank=True, null=True,
                                db_comment='主持人姓名')
    listparticipants = models.CharField(db_column='listParticipants', max_length=200, blank=True, null=True,
                                        db_comment='参加讨论人员名单')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=10, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=10, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=10, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=10, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=20, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=10, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    discussionopinions = models.TextField(db_column='discussionOpinions', blank=True, null=True,
                                          db_comment='讨论意见')
    moderatorconcludingcomments = models.TextField(db_column='moderatorConcludingComments', blank=True, null=True,
                                                   db_comment='主持人总结意见')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    detaileddescriptionsyndromedifferentiationtreatment = models.TextField(
        db_column='detailedDescriptionSyndromeDifferentiationTreatment', blank=True, null=True,
        db_comment='辨证论治详细描述')
    tcmprescriptionordercontent = models.TextField(db_column='TCMPrescriptionOrderContent', blank=True, null=True,
                                                   db_comment='中药处方医嘱内容?')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0041(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    shifthandoverdatetime = models.CharField(db_column='shiftHandoverDateTime', max_length=15, blank=True, null=True,
                                             db_comment='交班日期时间')
    shifthandoverid = models.CharField(db_column='shiftHandoverId', max_length=50, blank=True, null=True,
                                       db_comment='交班者ID')
    signatureshiftsupervisor = models.CharField(db_column='signatureShiftSupervisor', max_length=50, blank=True,
                                                null=True, db_comment='交班者签名')
    successiondatetime = models.CharField(db_column='successionDateTime', max_length=15, blank=True, null=True,
                                          db_comment='接班日期时间')
    successorid = models.CharField(db_column='successorId', max_length=50, blank=True, null=True,
                                   db_comment='接班者ID')
    signaturesuccessor = models.CharField(db_column='signatureSuccessor', max_length=50, blank=True, null=True,
                                          db_comment='接班者签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    admission = models.TextField(blank=True, null=True, db_comment='入院情况')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断编码')
    admissiondiagnosisname = models.CharField(db_column='admissionDiagnosisName', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断名称')
    admissiontcmdiseasecode = models.CharField(db_column='admissionTCMDiseaseCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名代码')
    admissiontcmdiseasename = models.CharField(db_column='admissionTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名名称')
    admissiontcmsyndromecode = models.CharField(db_column='admissionTCMsyndromeCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候代码')
    admissiontcmsyndromename = models.CharField(db_column='admissionTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候名称')
    surrentsituation = models.TextField(db_column='surrentSituation', blank=True, null=True,
                                        db_comment='目前情况')
    cdiagnosiswesternmedicinediagnosiscode = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisCode',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊断编码')
    cdiagnosiswesternmedicinediagnosisname = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisName',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊断名称')
    cdiagnosistcmdiseasecode = models.CharField(db_column='cDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名代码')
    cdiagnosistcmdiseasename = models.CharField(db_column='cDiagnosisTCMDiseaseName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名名称')
    cdiagnosistcmsyndromecode = models.CharField(db_column='cDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候代码')
    cdiagnosistcmsyndromename = models.CharField(db_column='cDiagnosisTCMSyndromeName', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候名称')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    successiontreatmentplan = models.TextField(db_column='successionTreatmentPlan', blank=True, null=True,
                                               db_comment='接班诊疗计划')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0042(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    transferoutdatetime = models.CharField(db_column='transferOutDateTime', max_length=15, blank=True, null=True,
                                           db_comment='转出日期时间')
    transferoutphysicianid = models.CharField(db_column='transferOutPhysicianId', max_length=50, blank=True, null=True,
                                              db_comment='转出医师工号')
    signaturetransferoutphysician = models.CharField(db_column='signatureTransferOutPhysician', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='转出医师签名')
    transferindatetime = models.CharField(db_column='transferInDateTime', max_length=15, blank=True, null=True,
                                          db_comment='转入日期时间')
    transferredphysicianid = models.CharField(db_column='transferredPhysicianId', max_length=50, blank=True, null=True,
                                              db_comment='转入医师工号')
    transferredphysicianname = models.CharField(db_column='transferredPhysicianName', max_length=50, blank=True,
                                                null=True, db_comment='转入医师签名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    admission = models.TextField(blank=True, null=True, db_comment='入院情况')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断编码')
    admissiondiagnosisname = models.CharField(db_column='admissionDiagnosisName', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断名称')
    admissiontcmdiseasecode = models.CharField(db_column='admissionTCMDiseaseCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名代码')
    admissiontcmdiseasename = models.CharField(db_column='admissionTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名名称')
    admissiontcmsyndromecode = models.CharField(db_column='admissionTCMsyndromeCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候代码')
    admissiontcmsyndromename = models.CharField(db_column='admissionTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候名称')
    surrentsituation = models.TextField(db_column='surrentSituation', blank=True, null=True,
                                        db_comment='目前情况')
    cdiagnosiswesternmedicinediagnosiscode = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisCode',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊断编码')
    cdiagnosiswesternmedicinediagnosisname = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisName',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊名称')
    cdiagnosistcmdiseasecode = models.CharField(db_column='cDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名代码')
    cdiagnosistcmdiseasename = models.CharField(db_column='cDiagnosisTCMDiseaseName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名名称')
    cdiagnosistcmsyndromecode = models.CharField(db_column='cDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候代码')
    cdiagnosistcmsyndromename = models.CharField(db_column='cDiagnosisTCMSyndromeName', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候名称')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    successiontreatmentplan = models.TextField(db_column='successionTreatmentPlan', blank=True, null=True,
                                               db_comment='接班诊疗计划')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    transferrecordtypecode = models.CharField(db_column='transferRecordTypeCode', max_length=50, blank=True, null=True,
                                              db_comment='转科记录类型代码')
    transferrecordtypename = models.CharField(db_column='transferRecordTypeName', max_length=50, blank=True, null=True,
                                              db_comment='转科记录类型名称')
    transferoutdepartment = models.CharField(db_column='transferOutDepartment', max_length=50, blank=True, null=True,
                                             db_comment='转出科室')
    transfertodepartment = models.CharField(db_column='transferToDepartment', max_length=50, blank=True, null=True,
                                            db_comment='转入科室')
    transferpurpose = models.CharField(db_column='transferPurpose', max_length=200, blank=True, null=True,
                                       db_comment='转科目的')
    tcmprescriptionordercontent = models.TextField(db_column='TCMPrescriptionOrderContent', blank=True, null=True,
                                                   db_comment='中药处方医嘱内容?')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0043(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    physiciansignatureid = models.CharField(db_column='physicianSignatureId', max_length=50, blank=True, null=True,
                                            db_comment='医师工号')
    physiciansignaturename = models.CharField(db_column='physicianSignatureName', max_length=50, blank=True, null=True,
                                              db_comment='医师签名')
    summarydatetime = models.CharField(db_column='summaryDateTime', max_length=15, blank=True, null=True,
                                       db_comment='小结日期时间')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    chiefcomplaint = models.CharField(db_column='chiefComplaint', max_length=100, blank=True, null=True,
                                      db_comment='主诉')
    admission = models.TextField(blank=True, null=True, db_comment='入院情况')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断编码')
    admissiondiagnosisname = models.CharField(db_column='admissionDiagnosisName', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断-西医诊断名称')
    admissiontcmdiseasecode = models.CharField(db_column='admissionTCMDiseaseCode', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名代码')
    admissiontcmdiseasename = models.CharField(db_column='admissionTCMDiseaseName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='入院诊断-中医病名名称')
    admissiontcmsyndromecode = models.CharField(db_column='admissionTCMsyndromeCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候代码')
    admissiontcmsyndromename = models.CharField(db_column='admissionTCMsyndromeName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医证候名称')
    surrentsituation = models.TextField(db_column='surrentSituation', blank=True, null=True,
                                        db_comment='目前情况')
    cdiagnosiswesternmedicinediagnosiscode = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisCode',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊断编码')
    cdiagnosiswesternmedicinediagnosisname = models.CharField(db_column='cDiagnosisWesternMedicineDiagnosisName',
                                                              max_length=50, blank=True, null=True,
                                                              db_comment='目前诊断-西医诊断名称')
    cdiagnosistcmdiseasecode = models.CharField(db_column='cDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名代码')
    cdiagnosistcmdiseasename = models.CharField(db_column='cDiagnosisTCMDiseaseName', max_length=50, blank=True,
                                                null=True,
                                                db_comment='目前诊断-中医病名名称')
    cdiagnosistcmsyndromecode = models.CharField(db_column='cDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候代码')
    cdiagnosistcmsyndromename = models.CharField(db_column='cDiagnosisTCMSyndromeName', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='目前诊断-中医证候名称')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    futuretreatmentoptions = models.TextField(db_column='futureTreatmentOptions', blank=True, null=True,
                                              db_comment='今后治疗方案')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    orderitem = models.TextField(db_column='orderItem', blank=True, null=True,
                                 db_comment='医嘱内容?')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0044(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    physiciansignatureid = models.CharField(db_column='physicianSignatureId', max_length=50, blank=True, null=True,
                                            db_comment='医师工号')
    physiciansignaturename = models.CharField(db_column='physicianSignatureName', max_length=50, blank=True, null=True,
                                              db_comment='医师签名')
    occupationcode = models.CharField(db_column='occupationCode', max_length=50, blank=True, null=True,
                                      db_comment='专业技术职务类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=50, blank=True, null=True,
                                      db_comment='专业技术职务类别名称')
    listrescuepersonnel = models.TextField(db_column='listreScuePersonnel', blank=True, null=True,
                                           db_comment='参加抢救人员名单')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    diseasediagnosisname = models.CharField(db_column='diseaseDiagnosisName', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断名称')
    diseasediagnosiscode = models.CharField(db_column='diseaseDiagnosisCode', max_length=50, blank=True, null=True,
                                            db_comment='疾病诊断编码')
    conditionchange = models.TextField(db_column='conditionChange', blank=True, null=True,
                                       db_comment='病情变化情况')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=80, blank=True, null=True,
                                     db_comment='手术及操作名称')
    operationtargetsitename = models.CharField(db_column='operationTargetSiteName', max_length=50, blank=True,
                                               null=True,
                                               db_comment='手术及操作目标部位名称')
    interventionname = models.CharField(db_column='interventionName', max_length=100, blank=True, null=True,
                                        db_comment='介入物名称')
    operationmethod = models.TextField(db_column='operationMethod', blank=True, null=True,
                                       db_comment='操作方法')
    operationsnumber = models.IntegerField(db_column='operationsNumber', blank=True, null=True,
                                           db_comment='操作次数')
    rescuemeasures = models.TextField(db_column='rescueMeasures', blank=True, null=True,
                                      db_comment='抢救措施')
    rescuestartdatetime = models.CharField(db_column='rescueStartDateTime', max_length=15, blank=True, null=True,
                                           db_comment='抢救开始日期时间')
    rescueenddatetime = models.CharField(db_column='rescueEndDateTime', max_length=15, blank=True, null=True,
                                         db_comment='抢救结束日期时间')
    inspectionitemname = models.CharField(db_column='inspectionItemName', max_length=80, blank=True, null=True,
                                          db_comment='检查/检验项目名称')
    inspectionresults = models.TextField(db_column='inspectionResults', blank=True, null=True,
                                         db_comment='检查/检验结果 ')
    inspectionquantitativeresults = models.DecimalField(db_column='inspectionQuantitativeResults', max_digits=14,
                                                        decimal_places=4, blank=True, null=True,
                                                        db_comment='检查/检验定量结果')
    inspectionresultcode = models.CharField(db_column='inspectionResultCode', max_length=50, blank=True, null=True,
                                            db_comment='检查/检验结果代码')
    inspectionresultname = models.CharField(db_column='inspectionResultName', max_length=100, blank=True, null=True,
                                            db_comment='检查/检验结果名称')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0045(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    applyid = models.CharField(db_column='applyId', max_length=50, blank=True, null=True,
                               db_comment='电子申请单编号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    consultationdatetime = models.CharField(db_column='consultationDateTime', max_length=15, blank=True, null=True,
                                            db_comment='会诊日期时间')
    consultationdoctorapplycode = models.CharField(db_column='ConsultationDoctorApplyCode', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='会诊申请医师签名')
    consultationdoctorapplyname = models.CharField(db_column='ConsultationDoctorApplyName', max_length=50, blank=True,
                                                   null=True,
                                                   db_comment='会诊申请医师签名')
    signatureconsultantid = models.CharField(db_column='signatureConsultantId', max_length=50, blank=True, null=True,
                                             db_comment='会诊医师工号')
    signatureconsultantname = models.CharField(db_column='signatureConsultantName', max_length=50, blank=True,
                                               null=True, db_comment='会诊医师签名')
    medicalinstitutiontheconsultantname = models.CharField(db_column='medicalInstitutionTheConsultantName',
                                                           max_length=70, blank=True, null=True,
                                                           db_comment='会诊医师所在医疗机构名称')
    consultationapplicationdeptcode = models.CharField(db_column='consultationApplicationDeptCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='会诊申请科室代码')
    consultationapplicationdeptname = models.CharField(db_column='consultationApplicationDeptName', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='会诊申请科室名称')
    consultationapplyorgid = models.CharField(db_column='consultationApplyOrgId', max_length=70, blank=True, null=True,
                                              db_comment='会诊申请医疗机构编号')
    consultationapplyorgname = models.CharField(db_column='consultationApplyOrgName', max_length=70, blank=True,
                                                null=True,
                                                db_comment='会诊申请医疗机构名称')
    consultationdeptcode = models.CharField(db_column='consultationDeptCode', max_length=50, blank=True, null=True,
                                            db_comment='会诊所在科室代码')
    consultationdeptname = models.CharField(db_column='consultationDeptName', max_length=50, blank=True, null=True,
                                            db_comment='会诊所在科室名称')
    orgid = models.CharField(db_column='orgId', max_length=70, blank=True, null=True,
                             db_comment='会诊所在医疗机构代码')
    orgname = models.CharField(db_column='orgName', max_length=70, blank=True, null=True,
                               db_comment='会诊所在医疗机构名称')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    medicalrecordsummary = models.CharField(db_column='medicalRecordSummary', max_length=200, blank=True, null=True,
                                            db_comment='病历摘要')
    westerndiagnosticcode = models.CharField(db_column='westernDiagnosticCode', max_length=50, blank=True, null=True,
                                             db_comment='西医诊断编码')
    westerndiagnosticname = models.CharField(db_column='westernDiagnosticName', max_length=50, blank=True, null=True,
                                             db_comment='西医诊断名称')
    tcmdiseasecode = models.CharField(db_column='TCMDiseaseCode', max_length=50, blank=True, null=True,
                                      db_comment='中医病名代码')
    tcmdiseasename = models.CharField(db_column='TCMDiseaseName', max_length=50, blank=True, null=True,
                                      db_comment='中医病名名称')
    tcmsyndromecode = models.CharField(db_column='TCMSyndromeCode', max_length=50, blank=True, null=True,
                                       db_comment='中医证候代码')
    tcmsyndromename = models.CharField(db_column='TCMSyndromeName', max_length=50, blank=True, null=True,
                                       db_comment='中医证候名称')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    auxiliaryinspectionresults = models.TextField(db_column='auxiliaryInspectionResults', blank=True, null=True,
                                                  db_comment='辅助检查结果')
    diagnosistreatmentprocessname = models.TextField(db_column='diagnosisTreatmentProcessName', blank=True, null=True,
                                                     db_comment='诊疗过程名称')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    consultationpurpose = models.CharField(db_column='consultationPurpose', max_length=50, blank=True, null=True,
                                           db_comment='会诊目的')
    consultationtype = models.CharField(db_column='consultationType', max_length=50, blank=True, null=True,
                                        db_comment='会诊类型')
    consultationreason = models.CharField(db_column='consultationReason', max_length=200, blank=True, null=True,
                                          db_comment='会诊原因')
    consultationopinion = models.TextField(db_column='consultationOpinion', blank=True, null=True,
                                           db_comment='会诊意见')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0046(models.Model):
    doc_id = models.CharField(max_length=100, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField("住院号", max_length=10, blank=True, null=True, db_comment='住院号')
    id = models.CharField(max_length=100, blank=True, null=True, db_comment='患者身份证件号码')
    name = models.CharField(max_length=100, blank=True, null=True, db_comment='患者姓名')
    gendercode = models.CharField(db_column='genderCode', max_length=100, blank=True, null=True,
                                  db_comment='性别代码')
    gendername = models.CharField(db_column='genderName', max_length=100, blank=True, null=True,
                                  db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=100, blank=True, null=True,
                               db_comment='年龄单位')
    summarydatetime = models.CharField(db_column='summaryDateTime', max_length=15, blank=True, null=True,
                                       db_comment='小结日期时间')
    authorid = models.CharField(db_column='authorId', max_length=100, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=100, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=100, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=100, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    surgeonsignaturedatetime = models.CharField(db_column='surgeonSignatureDateTime', max_length=15, blank=True,
                                                null=True, db_comment='签名日期时间')
    surgeonsignatureid = models.CharField(db_column='surgeonSignatureId', max_length=100, blank=True, null=True,
                                          db_comment='手术者工号')
    surgeonsignaturename = models.CharField(db_column='surgeonSignatureName', max_length=100, blank=True, null=True,
                                            db_comment='手术者签名')
    physiciansignaturedatetime = models.CharField(db_column='physicianSignatureDateTime', max_length=15, blank=True,
                                                  null=True, db_comment='签名日期时间')
    physiciansignatureid = models.CharField(db_column='physicianSignatureId', max_length=100, blank=True, null=True,
                                            db_comment='医师工号')
    physiciansignaturename = models.CharField(db_column='physicianSignatureName', max_length=100, blank=True, null=True,
                                              db_comment='医师签名')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=100, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=100, blank=True, null=True,
                                            db_comment='联系人姓名')
    deptid = models.CharField(db_column='deptId', max_length=100, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=100, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=100, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=100, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=100, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=100, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=100, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=100, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=100, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=100, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    medicalrecordsummary = models.CharField(db_column='medicalRecordSummary', max_length=200, blank=True, null=True,
                                            db_comment='病历摘要')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=100, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=100, blank=True, null=True,
                                        db_comment='术前诊断名称')
    diagnosticbasis = models.TextField(db_column='diagnosticBasis', blank=True, null=True,
                                       db_comment='诊断依据')
    allergyhistorymarkers = models.SmallIntegerField(db_column='allergyHistoryMarkers', blank=True, null=True,
                                                     db_comment='过敏史标志')
    allergyhistory = models.TextField(db_column='allergyHistory', blank=True, null=True,
                                      db_comment='过敏史')
    auxiliaryinspectionresults = models.TextField(db_column='auxiliaryInspectionResults', blank=True, null=True,
                                                  db_comment='辅助检查结果')
    surgicalindications = models.CharField(db_column='surgicalIndications', max_length=100, blank=True, null=True,
                                           db_comment='手术适应证')
    surgicalcontraindications = models.CharField(db_column='surgicalContraindications', max_length=100, blank=True,
                                                 null=True, db_comment='手术禁忌症')
    surgicalindication = models.TextField(db_column='surgicalIndication', blank=True, null=True,
                                          db_comment='手术指征')
    consultationopinion = models.TextField(db_column='consultationOpinion', blank=True, null=True,
                                           db_comment='会诊意见')
    proposedoperationcode = models.CharField(db_column='proposedOperationCode', max_length=100, blank=True, null=True,
                                             db_comment='拟实施手术及操作编码')
    proposedoperationname = models.CharField(db_column='proposedOperationName', max_length=100, blank=True, null=True,
                                             db_comment='拟实施手术及操作名称')
    targetsiteoperationperformedname = models.CharField(db_column='targetSiteOperationPerformedName', max_length=100,
                                                        blank=True, null=True,
                                                        db_comment='拟实施手术目标部位名称')
    proposedoperationdatetime = models.CharField(db_column='proposedOperationDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='拟实施手术及操作日期时间')
    plananesthesiamethodcode = models.CharField(db_column='planAnesthesiaMethodCode', max_length=100, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法代码')
    plananesthesiamethodname = models.CharField(db_column='planAnesthesiaMethodName', max_length=100, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法名称')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    operationkeypoints = models.CharField(db_column='operationKeyPoints', max_length=200, blank=True, null=True,
                                          db_comment='手术要点')
    preoperativepreparation = models.TextField(db_column='preoperativePreparation', blank=True, null=True,
                                               db_comment='术前准备')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=100, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0047(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    discussiondatetime = models.CharField(db_column='discussionDateTime', max_length=15, blank=True, null=True,
                                          db_comment='讨论日期时间')
    discussionplace = models.CharField(db_column='discussionPlace', max_length=50, blank=True, null=True,
                                       db_comment='讨论地点')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    surgeonsignatureid = models.CharField(db_column='surgeonSignatureId', max_length=50, blank=True, null=True,
                                          db_comment='手术者签名工号')
    surgeonsignaturename = models.CharField(db_column='surgeonSignatureName', max_length=50, blank=True, null=True,
                                            db_comment='手术者签名')
    surgeonoccupationcode = models.CharField(db_column='surgeonOccupationCode', max_length=50, blank=True, null=True,
                                             db_comment='专业技术职务类别代码')
    surgeonoccupationname = models.CharField(db_column='surgeonOccupationName', max_length=50, blank=True, null=True,
                                             db_comment='专业技术职务类别名称')
    anestsignaturedatetime = models.CharField(db_column='anestSignatureDateTime', max_length=15, blank=True, null=True,
                                              db_comment='签名日期时间')
    anesthesiologistsignatureid = models.CharField(db_column='anesthesiologistSignatureId', max_length=50, blank=True,
                                                   null=True, db_comment='麻醉医师工号')
    anesthesiologistsignaturename = models.CharField(db_column='anesthesiologistSignatureName', max_length=50,
                                                     blank=True, null=True,
                                                     db_comment='麻醉医师签名')
    anestoccupationcode = models.CharField(db_column='anestOccupationCode', max_length=50, blank=True, null=True,
                                           db_comment='专业技术职务类别代码')
    anestoccupationname = models.CharField(db_column='anestOccupationName', max_length=50, blank=True, null=True,
                                           db_comment='专业技术职务类别名称')
    physiciansignaturedatetime = models.CharField(db_column='physicianSignatureDateTime', max_length=15, blank=True,
                                                  null=True,
                                                  db_comment='医师签名日期时间')
    physiciansignatureid = models.CharField(db_column='physicianSignatureId', max_length=50, blank=True, null=True,
                                            db_comment='医师工号')
    physiciansignaturename = models.CharField(db_column='physicianSignatureName', max_length=50, blank=True, null=True,
                                              db_comment='医师签名')
    doctoroccupationcode = models.CharField(db_column='doctorOccupationCode', max_length=50, blank=True, null=True,
                                            db_comment='专业技术职务类别代码')
    doctoroccupationname = models.CharField(db_column='doctorOccupationName', max_length=50, blank=True, null=True,
                                            db_comment='专业技术职务类别名称')
    listparticipants = models.CharField(db_column='listParticipants', max_length=200, blank=True, null=True,
                                        db_comment='参加讨论人员名单')
    hostid = models.CharField(db_column='hostId', max_length=50, blank=True, null=True,
                              db_comment='主持人id')
    hostname = models.CharField(db_column='hostName', max_length=50, blank=True, null=True,
                                db_comment='主持人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    prediagnosiscode = models.CharField(db_column='preDiagnosisCode', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断编码')
    prediagnosisname = models.CharField(db_column='preDiagnosisName', max_length=50, blank=True, null=True,
                                        db_comment='术前诊断名称')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=15, blank=True, null=True,
                                         db_comment='入院日期时间')
    proposedoperationname = models.CharField(db_column='proposedOperationName', max_length=80, blank=True, null=True,
                                             db_comment='拟实施手术及操作名称')
    proposedoperationcode = models.CharField(db_column='proposedOperationCode', max_length=50, blank=True, null=True,
                                             db_comment='拟实施手术及操作编码')
    targetsiteoperationperformedname = models.CharField(db_column='targetSiteOperationPerformedName', max_length=50,
                                                        blank=True, null=True,
                                                        db_comment='拟实施手术目标部位名称')
    proposedoperationdatetime = models.CharField(db_column='proposedOperationDateTime', max_length=15, blank=True,
                                                 null=True,
                                                 db_comment='拟实施手术及操作日期时间')
    plananesthesiamethodcode = models.CharField(db_column='planAnesthesiaMethodCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法代码')
    plananesthesiamethodname = models.CharField(db_column='planAnesthesiaMethodName', max_length=100, blank=True,
                                                null=True,
                                                db_comment='拟实施麻醉方法名称')
    operationkeypoints = models.CharField(db_column='operationKeyPoints', max_length=200, blank=True, null=True,
                                          db_comment='手术要点')
    preoperativepreparation = models.TextField(db_column='preoperativePreparation', blank=True, null=True,
                                               db_comment='术前准备')
    surgicalindication = models.TextField(db_column='surgicalIndication', blank=True, null=True,
                                          db_comment='手术指征')
    surgicalprogram = models.TextField(db_column='surgicalProgram', blank=True, null=True,
                                       db_comment='手术方案')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    discussionopinions = models.TextField(db_column='discussionOpinions', blank=True, null=True,
                                          db_comment='讨论意见')
    discussionconclusion = models.TextField(db_column='discussionConclusion', blank=True, null=True,
                                            db_comment='讨论结论')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0048(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=50, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    signaturedatetime = models.CharField(db_column='signatureDateTime', max_length=50, blank=True, null=True,
                                         db_comment='签名日期时间')
    physicianid = models.CharField(db_column='physicianId', max_length=50, blank=True, null=True,
                                   db_comment='医师ID')
    physiciansignature = models.CharField(db_column='physicianSignature', max_length=50, blank=True, null=True,
                                          db_comment='医师签名')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=50, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=50, blank=True, null=True,
                                            db_comment='联系人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationname = models.CharField(db_column='operationName', max_length=200, blank=True, null=True,
                                     db_comment='手术名称')
    surgicaltargetsite = models.CharField(db_column='surgicalTargetSite', max_length=50, blank=True, null=True,
                                          db_comment='手术目标部位名称')
    operationdatetime = models.CharField(db_column='operationDateTime', max_length=50, blank=True, null=True,
                                         db_comment='手术日期时间')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=200, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=200, blank=True, null=True,
                                            db_comment='麻醉方法名称')
    operationprocess = models.TextField(db_column='operationProcess', blank=True, null=True,
                                        db_comment='手术过程')
    postoperativediagnosiscode = models.CharField(db_column='postoperativeDiagnosisCode', max_length=50, blank=True,
                                                  null=True, db_comment='术后诊断编码')
    postoperativediagnosisname = models.CharField(db_column='postoperativeDiagnosisName', max_length=200, blank=True,
                                                  null=True, db_comment='术后诊断名称')
    diagnosticbasis = models.TextField(db_column='diagnosticBasis', blank=True, null=True,
                                       db_comment='诊断依据')
    mattersneedingattention = models.TextField(db_column='mattersNeedingAttention', blank=True, null=True,
                                               db_comment='注意事项')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0049(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=50, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    chiefphysiciandatetime = models.CharField(db_column='chiefPhysicianDateTime', max_length=50, blank=True, null=True,
                                              db_comment='签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysiciansignature = models.CharField(db_column='chiefPhysicianSignature', max_length=50, blank=True,
                                               null=True, db_comment='主任医师签名')
    attendingdatetime = models.CharField(db_column='attendingDateTime', max_length=50, blank=True, null=True,
                                         db_comment='签名日期时间')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='主治医师工号')
    attendingdoctorname = models.CharField(db_column='attendingDoctorName', max_length=50, blank=True, null=True,
                                           db_comment='主治医师签名')
    residentdatetime = models.CharField(db_column='residentDateTime', max_length=50, blank=True, null=True,
                                        db_comment='签名日期时间')
    residentsignatureid = models.CharField(db_column='residentSignatureId', max_length=50, blank=True, null=True,
                                           db_comment='住院医师工号')
    residentsignature = models.CharField(db_column='residentSignature', max_length=50, blank=True, null=True,
                                         db_comment='住院医师签名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=50, blank=True, null=True,
                                         db_comment='入院日期时间')
    admissiondesc = models.TextField(db_column='admissionDesc', blank=True, null=True,
                                     db_comment='入院情况')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断编码')
    admissiondiagnosisname = models.TextField(db_column='admissionDiagnosisName', blank=True, null=True,
                                              db_comment='入院诊断名称')
    positiveauxiliarytestresults = models.TextField(db_column='positiveAuxiliaryTestResults', blank=True, null=True,
                                                    db_comment='阳性辅助检查结果')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    principlesmethodstreatment = models.TextField(db_column='principlesMethodsTreatment', blank=True, null=True,
                                                  db_comment='治则治法')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    dischargestatus = models.TextField(db_column='dischargeStatus', blank=True, null=True,
                                       db_comment='出院情况')
    leavedatetime = models.CharField(db_column='leaveDateTime', max_length=50, blank=True, null=True,
                                     db_comment='出院日期时间')
    ddiagnosiswesterndiagnosticcode = models.CharField(db_column='dDiagnosisWesternDiagnosticCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='出院诊断-西医诊断编码')
    ddiagnosiswesterndiagnosticname = models.TextField(db_column='dDiagnosisWesternDiagnosticName', blank=True,
                                                       null=True,
                                                       db_comment='出院诊断-西医诊断名称')
    ddiagnosistcmdiseasecode = models.CharField(db_column='dDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='出院诊断-中医病名代码')
    ddiagnosistcmdiseasename = models.TextField(db_column='dDiagnosisTCMDiseaseName', blank=True, null=True,
                                                db_comment='出院诊断-中医病名名称')
    ddiagnosistcmsyndromecode = models.CharField(db_column='dDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='出院诊断-中医证候代码')
    ddiagnosistcmsyndromename = models.TextField(db_column='dDiagnosisTCMSyndromeName', blank=True, null=True,
                                                 db_comment='出院诊断-中医证候名称')
    symptomssignsdischarge = models.TextField(db_column='symptomsSignsDischarge', blank=True, null=True,
                                              db_comment='出院时症状与体征')
    dischargeorder = models.TextField(db_column='dischargeOrder', blank=True, null=True,
                                      db_comment='出院医嘱')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0050(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    residentdate = models.CharField(db_column='residentDate', max_length=50, blank=True, null=True,
                                    db_comment='签名日期时间')
    residentsignatureid = models.CharField(db_column='residentSignatureId', max_length=50, blank=True, null=True,
                                           db_comment='住院医师工号')
    residentsignaturename = models.CharField(db_column='residentSignatureName', max_length=50, blank=True, null=True,
                                             db_comment='住院医师签名')
    attendingdate = models.CharField(db_column='attendingDate', max_length=50, blank=True, null=True,
                                     db_comment='签名日期时间')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='主治医师ID')
    attendingdoctorsignature = models.CharField(db_column='attendingDoctorSignature', max_length=50, blank=True,
                                                null=True, db_comment='主治医师签名')
    chiefphysiciandate = models.CharField(db_column='chiefPhysicianDate', max_length=50, blank=True, null=True,
                                          db_comment='签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师ID')
    chiefphysiciansignature = models.CharField(db_column='chiefPhysicianSignature', max_length=50, blank=True,
                                               null=True, db_comment='主任医师签名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    admissiondate = models.CharField(db_column='admissionDate', max_length=50, blank=True, null=True,
                                     db_comment='入院日期')
    admissiondiagnosiscode = models.CharField(db_column='admissionDiagnosisCode', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断编码')
    admissiondiagnosisname = models.CharField(db_column='admissionDiagnosisName', max_length=50, blank=True, null=True,
                                              db_comment='入院诊断名称')
    admission = models.TextField(blank=True, null=True, db_comment='入院情况')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    deathdatetime = models.CharField(db_column='deathDatetime', max_length=15, blank=True, null=True,
                                     db_comment='死亡日期时间')
    directcausedeathcode = models.CharField(db_column='directCauseDeathCode', max_length=50, blank=True, null=True,
                                            db_comment='直接死亡原因编码')
    directcausedeathname = models.CharField(db_column='directCauseDeathName', max_length=50, blank=True, null=True,
                                            db_comment='直接死亡原因名称')
    deathdiagnosiscode = models.CharField(db_column='deathDiagnosisCode', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断编码')
    deathdiagnosisname = models.CharField(db_column='deathDiagnosisName', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断名称')
    familyagreeflag = models.SmallIntegerField(db_column='familyAgreeFlag', blank=True, null=True,
                                               db_comment='家属是否同意尸体解剖标志')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0051(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.PositiveSmallIntegerField('年龄', db_comment='年龄', validators=[MinValueValidator(1), MaxValueValidator(150)])
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    discussiondatetime = models.CharField(db_column='discussionDateTime', max_length=15, blank=True, null=True,
                                          db_comment='讨论日期时间')
    placediscussion = models.CharField(db_column='placeDiscussion', max_length=50, blank=True, null=True,
                                       db_comment='讨论地点')
    createdatetime = models.CharField(db_column='createDateTime', max_length=15, blank=True, null=True,
                                      db_comment='文档创作日期时间')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医生工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医生签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    residentdatetime = models.CharField(db_column='residentDateTime', max_length=15, blank=True, null=True,
                                        db_comment='签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师ID')
    residentsignature = models.CharField(db_column='residentSignature', max_length=50, blank=True, null=True,
                                         db_comment='住院医师签名')
    residentoccupationcode = models.CharField(db_column='residentOccupationCode', max_length=50, blank=True, null=True,
                                              db_comment='专业技术职务类别代码')
    residentoccupationname = models.CharField(db_column='residentOccupationName', max_length=50, blank=True, null=True,
                                              db_comment='专业技术职务类别名称')
    attendingdatetime = models.CharField(db_column='attendingDateTime', max_length=15, blank=True, null=True,
                                         db_comment='签名日期时间')
    attendingdoctorid = models.CharField(db_column='attendingDoctorId', max_length=50, blank=True, null=True,
                                         db_comment='主治医师ID')
    attendingdoctorsignature = models.CharField(db_column='attendingDoctorSignature', max_length=50, blank=True,
                                                null=True, db_comment='主治医师签名')
    attendoccupationcode = models.CharField(db_column='attendOccupationCode', max_length=50, blank=True, null=True,
                                            db_comment='专业技术职务类别代码')
    attendoccupationname = models.CharField(db_column='attendOccupationName', max_length=50, blank=True, null=True,
                                            db_comment='专业技术职务类别名称')
    chiefphysiciandatetime = models.CharField(db_column='chiefPhysicianDateTime', max_length=15, blank=True, null=True,
                                              db_comment='签名日期时间')
    chiefphysicianid = models.CharField(db_column='chiefPhysicianId', max_length=50, blank=True, null=True,
                                        db_comment='主任医师工号')
    chiefphysicianname = models.CharField(db_column='chiefPhysicianName', max_length=50, blank=True, null=True,
                                          db_comment='主任医师签名')
    occupationcode = models.CharField(db_column='occupationCode', max_length=50, blank=True, null=True,
                                      db_comment='专业技术职务类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=50, blank=True, null=True,
                                      db_comment='专业技术职务类别名称')
    listparticipants = models.TextField(db_column='listParticipants', blank=True, null=True,
                                        db_comment='参加讨论人员名单')
    hostid = models.CharField(db_column='hostId', max_length=50, blank=True, null=True,
                              db_comment='主持人工号')
    hostname = models.CharField(db_column='hostName', max_length=50, blank=True, null=True,
                                db_comment='主持人姓名')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码(提供患者服务机构)')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称(提供患者服务机构)')
    directcausedeathcode = models.CharField(db_column='directCauseDeathCode', max_length=50, blank=True, null=True,
                                            db_comment='直接死亡原因编码')
    directcausedeathname = models.CharField(db_column='directCauseDeathName', max_length=50, blank=True, null=True,
                                            db_comment='直接死亡原因名称')
    deathdiagnosiscode = models.CharField(db_column='deathDiagnosisCode', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断编码')
    deathdiagnosisname = models.CharField(db_column='deathDiagnosisName', max_length=50, blank=True, null=True,
                                          db_comment='死亡诊断名称')
    deathdiscussionrecord = models.TextField(db_column='deathDiscussionRecord', blank=True, null=True,
                                             db_comment='死亡讨论记录')
    moderatorconcludingcomments = models.TextField(db_column='moderatorConcludingComments', blank=True, null=True,
                                                   db_comment='主持人总结意见')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0052(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    telecom = models.CharField(max_length=50, blank=True, null=True, db_comment='患者电话号码')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称')
    createdate = models.CharField(db_column='createDate', max_length=50, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    authororgid = models.CharField(db_column='authorOrgId', max_length=50, blank=True, null=True,
                                   db_comment='医疗机构组织机构代码')
    authororgname = models.CharField(db_column='authorOrgName', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构名称')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, db_comment='体重（kg）')
    ordercategorycode = models.CharField(db_column='orderCategoryCode', max_length=50, blank=True, null=True,
                                         db_comment='医嘱类别代码')
    ordercategoryname = models.CharField(db_column='orderCategoryName', max_length=50, blank=True, null=True,
                                         db_comment='医嘱类别名称')
    orderitemtype = models.CharField(db_column='orderItemType', max_length=50, blank=True, null=True,
                                     db_comment='医嘱项目类型代码')
    orderitemname = models.CharField(db_column='orderItemName', max_length=50, blank=True, null=True,
                                     db_comment='医嘱项目类型名称')
    effectivetimelow = models.CharField(db_column='effectiveTimeLow', max_length=50, blank=True, null=True,
                                        db_comment='医嘱计划开始日期时间')
    effectivetimehigh = models.CharField(db_column='effectiveTimeHigh', max_length=50, blank=True, null=True,
                                         db_comment='医嘱计划结束日期时间')
    orderitem = models.CharField(db_column='orderItem', max_length=100, blank=True, null=True,
                                 db_comment='医嘱项目内容')
    orderissuingdatetime = models.CharField(db_column='orderIssuingDateTime', max_length=14, blank=True, null=True,
                                            db_comment='医嘱开立日期时间')
    orderissuerid = models.CharField(db_column='orderIssuerId', max_length=50, blank=True, null=True,
                                     db_comment='医嘱开立者签名')
    orderissuer = models.CharField(db_column='orderIssuer', max_length=50, blank=True, null=True,
                                   db_comment='医嘱开立者签名')
    orderissuingdept = models.CharField(db_column='orderIssuingDept', max_length=50, blank=True, null=True,
                                        db_comment='医嘱开立科室')
    orderreviewdatetime = models.CharField(db_column='orderReviewDateTime', max_length=14, blank=True, null=True,
                                           db_comment='医嘱审核日期时间')
    orderreviewerid = models.CharField(db_column='orderReviewerId', max_length=50, blank=True, null=True,
                                       db_comment='医嘱审核人工号')
    orderreviewer = models.CharField(db_column='orderReviewer', max_length=50, blank=True, null=True,
                                     db_comment='医嘱审核人签名')
    ordercheckdatetime = models.CharField(db_column='orderCheckDateTime', max_length=14, blank=True, null=True,
                                          db_comment='医嘱核对日期时间')
    checkdoctorordernurseid = models.CharField(db_column='checkDoctorOrderNurseId', max_length=50, blank=True,
                                               null=True, db_comment='核对医嘱护士ID')
    checkdoctorordernurse = models.CharField(db_column='checkDoctorOrderNurse', max_length=50, blank=True, null=True,
                                             db_comment='核对医嘱护士签名')
    orderstopdatetime = models.CharField(db_column='orderStopDateTime', max_length=14, blank=True, null=True,
                                         db_comment='医嘱停止日期时间')
    stopordererid = models.CharField(db_column='stopOrdererId', max_length=50, blank=True, null=True,
                                     db_comment='停止医嘱者ID')
    stoporderername = models.CharField(db_column='stopOrdererName', max_length=50, blank=True, null=True,
                                       db_comment='停止医嘱者签名')
    ordercancellationdatetime = models.CharField(db_column='orderCancellationDateTime', max_length=14, blank=True,
                                                 null=True, db_comment='医嘱取消日期时间')
    cancelordererid = models.CharField(db_column='cancelOrdererId', max_length=50, blank=True, null=True,
                                       db_comment='取消医嘱者ID')
    cancelorderername = models.CharField(db_column='cancelOrdererName', max_length=50, blank=True, null=True,
                                         db_comment='取消医嘱者姓名')
    orderitemcomments = models.CharField(db_column='orderItemComments', max_length=100, blank=True, null=True,
                                         db_comment='医嘱备注信息')
    orderexecstatusdesc = models.CharField(db_column='orderExecStatusDesc', max_length=50, blank=True, null=True,
                                           db_comment='医嘱执行状态')
    orderexecdatetime = models.CharField(db_column='orderExecDateTime', max_length=14, blank=True, null=True,
                                         db_comment='医嘱执行日期时间')
    orderexecutorid = models.CharField(db_column='orderExecutorId', max_length=50, blank=True, null=True,
                                       db_comment='医嘱执行者ID')
    orderexecutor = models.CharField(db_column='orderExecutor', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行者姓名')
    orderexecdept = models.CharField(db_column='orderExecDept', max_length=50, blank=True, null=True,
                                     db_comment='医嘱执行科室')
    applyid = models.CharField(db_column='applyId', max_length=50, blank=True, null=True,
                               db_comment='电子申请单编号')
    prescriptiondrugno = models.CharField(db_column='prescriptionDrugNo', max_length=50, blank=True, null=True,
                                          db_comment='处方药品组号')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    data_src = models.CharField(max_length=2, blank=True, null=True,
                                db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''


class C0053(models.Model):
    doc_id = models.CharField(max_length=50, blank=True, null=True, db_comment='文档流水号')
    healthid = models.CharField(db_column='healthId', max_length=50, blank=True, null=True,
                                db_comment='居民健康卡号')
    inpatient_id = models.CharField('住院号', max_length=18, blank=True, null=True, db_comment='住院号')
    state = models.CharField(max_length=200, blank=True, null=True, db_comment='地址-省（自治区、直辖市）')
    city = models.CharField(max_length=200, blank=True, null=True, db_comment='地址-市（地区、州）')
    county = models.CharField(max_length=200, blank=True, null=True, db_comment='地址-县（区）')
    township = models.CharField(max_length=200, blank=True, null=True, db_comment='地址-乡（镇、街道办事处）')
    streetname = models.CharField(db_column='streetName', max_length=70, blank=True, null=True,
                                  db_comment='地址-村（街、路、弄等）')
    housenumber = models.CharField(db_column='houseNumber', max_length=70, blank=True, null=True,
                                   db_comment='地址-门牌号码')
    postalcode = models.CharField(db_column='postalCode', max_length=50, blank=True, null=True,
                                  db_comment='邮政编码')
    telecom = models.CharField(max_length=50, blank=True, null=True, db_comment='患者电话号码')
    id_no = models.CharField("患者身份证件号码", max_length=18,  db_comment='患者身份证件号码')
    name = models.CharField('患者姓名', max_length=64, db_comment='患者姓名')
    gender_code = models.PositiveSmallIntegerField("性别代码", choices=SexCodeChoices, db_comment='性别代码')
    gender_name = models.CharField('性别名称', max_length=10, db_comment='性别名称')
    birthtime = models.CharField(db_column='birthTime', max_length=8, blank=True, null=True,
                                 db_comment='出生日期')
    maritalstatuscode = models.CharField(db_column='maritalStatusCode', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况代码')
    maritalstatusname = models.CharField(db_column='maritalStatusName', max_length=50, blank=True, null=True,
                                         db_comment='婚姻状况名称')
    age = models.CharField(max_length=50, blank=True, null=True, db_comment='年龄')
    ageunit = models.CharField(db_column='ageUnit', max_length=50, blank=True, null=True,
                               db_comment='年龄单位')
    occupationcode = models.CharField(db_column='occupationCode', max_length=50, blank=True, null=True,
                                      db_comment='职业类别代码')
    occupationname = models.CharField(db_column='occupationName', max_length=50, blank=True, null=True,
                                      db_comment='职业类别名称')
    providerorgid = models.CharField(db_column='providerOrgId', max_length=50, blank=True, null=True,
                                     db_comment='医疗机构组织机构代码')
    providerorgname = models.CharField(db_column='providerOrgName', max_length=50, blank=True, null=True,
                                       db_comment='医疗机构组织机构名称')
    createdate = models.CharField(db_column='createDate', max_length=50, blank=True, null=True,
                                  db_comment='文档创作日期')
    authorid = models.CharField(db_column='authorId', max_length=50, blank=True, null=True,
                                db_comment='医师工号(文档创作者)')
    authorname = models.CharField(db_column='authorName', max_length=50, blank=True, null=True,
                                  db_comment='医师签名(文档创作者)')
    representedorgid = models.CharField(db_column='representedOrgId', max_length=50, blank=True, null=True,
                                        db_comment='医疗机构组织机构代码(保管机构)')
    representedorgname = models.CharField(db_column='representedOrgName', max_length=50, blank=True, null=True,
                                          db_comment='医疗机构组织机构名称(保管机构)')
    residentsignaturedatetime = models.CharField(db_column='residentsignatureDateTime', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='住院医师签名日期时间')
    residentid = models.CharField(db_column='residentId', max_length=50, blank=True, null=True,
                                  db_comment='住院医师ID')
    residentname = models.CharField(db_column='residentName', max_length=50, blank=True, null=True,
                                    db_comment='住院医师姓名')
    superiorsignaturedatetime = models.CharField(db_column='superiorSignatureDateTime', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='上级医师签名日期时间')
    superiorphysicianid = models.CharField(db_column='superiorPhysicianId', max_length=50, blank=True, null=True,
                                           db_comment='上级医师ID')
    superiorphysicianname = models.CharField(db_column='superiorPhysicianName', max_length=50, blank=True, null=True,
                                             db_comment='上级医师签名')
    associatedentitytelecom = models.CharField(db_column='associatedEntityTelecom', max_length=50, blank=True,
                                               null=True, db_comment='联系人电话号码')
    associatedentityname = models.CharField(db_column='associatedEntityName', max_length=50, blank=True, null=True,
                                            db_comment='联系人姓名')
    admissiondatetime = models.CharField(db_column='admissionDateTime', max_length=50, blank=True, null=True,
                                         db_comment='入院日期时间')
    leavedatetime = models.CharField(db_column='leaveDateTime', max_length=50, blank=True, null=True,
                                     db_comment='出院日期时间')
    deptid = models.CharField(db_column='deptId', max_length=50, blank=True, null=True,
                              db_comment='科室代码')
    deptname = models.CharField(db_column='deptName', max_length=50, blank=True, null=True,
                                db_comment='科室名称')
    wardcode = models.CharField(db_column='wardCode', max_length=50, blank=True, null=True,
                                db_comment='病区代码')
    wardname = models.CharField(db_column='wardName', max_length=50, blank=True, null=True,
                                db_comment='病区名称')
    wardid = models.CharField(db_column='wardId', max_length=50, blank=True, null=True,
                              db_comment='病房号id')
    wardno = models.CharField(db_column='wardNo', max_length=50, blank=True, null=True,
                              db_comment='病房号')
    bedid = models.CharField(db_column='bedId', max_length=50, blank=True, null=True,
                             db_comment='病床号Id')
    bedno = models.CharField(db_column='bedNo', max_length=50, blank=True, null=True,
                             db_comment='病床号')
    admission = models.TextField(blank=True, null=True, db_comment='入院情况')
    adiagnosiswesterndiagnosticcode = models.CharField(db_column='aDiagnosisWesternDiagnosticCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='入院诊断-西医诊断编码')
    adiagnosiswesterndiagnosticname = models.CharField(db_column='aDiagnosisWesternDiagnosticName', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='入院诊断-西医诊断名称')
    adiagnosistcmdiseasecode = models.CharField(db_column='aDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医病名代码')
    adiagnosistcmdiseasename = models.CharField(db_column='aDiagnosisTCMDiseaseName', max_length=100, blank=True,
                                                null=True,
                                                db_comment='入院诊断-中医病名名称')
    adiagnosistcmsyndromecode = models.CharField(db_column='aDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='入院诊断-中医证候代码')
    adiagnosistcmsyndromename = models.CharField(db_column='aDiagnosisTCMSyndromeName', max_length=100, blank=True,
                                                 null=True,
                                                 db_comment='入院诊断-中医证候名称')
    ddiagnosiswesterndiagnosticcode = models.CharField(db_column='dDiagnosisWesternDiagnosticCode', max_length=50,
                                                       blank=True, null=True,
                                                       db_comment='出院诊断-西医诊断编码')
    ddiagnosiswesterndiagnosticname = models.CharField(db_column='dDiagnosisWesternDiagnosticName', max_length=100,
                                                       blank=True, null=True,
                                                       db_comment='出院诊断-西医诊断名称')
    ddiagnosistcmdiseasecode = models.CharField(db_column='dDiagnosisTCMDiseaseCode', max_length=50, blank=True,
                                                null=True,
                                                db_comment='出院诊断-中医病名代码')
    ddiagnosistcmdiseasename = models.CharField(db_column='dDiagnosisTCMDiseaseName', max_length=100, blank=True,
                                                null=True,
                                                db_comment='出院诊断-中医病名名称')
    ddiagnosistcmsyndromecode = models.CharField(db_column='dDiagnosisTCMSyndromeCode', max_length=50, blank=True,
                                                 null=True,
                                                 db_comment='出院诊断-中医证候代码')
    ddiagnosistcmsyndromename = models.CharField(db_column='dDiagnosisTCMSyndromeName', max_length=100, blank=True,
                                                 null=True,
                                                 db_comment='出院诊断-中医证候名称')
    oresultsfourdiagnosistcm = models.TextField(db_column='oResultsFourDiagnosisTCM', blank=True, null=True,
                                                db_comment='中医“四诊”观察结果')
    symptomssignsdischarge = models.TextField(db_column='symptomsSignsDischarge', blank=True, null=True,
                                              db_comment='出院时症状与体征')
    dischargedesc = models.TextField(db_column='dischargeDesc', blank=True, null=True,
                                     db_comment='出院情况')
    operationcode = models.CharField(db_column='operationCode', max_length=50, blank=True, null=True,
                                     db_comment='手术及操作编码')
    operationstartdatetime = models.CharField(db_column='operationStartDateTime', max_length=50, blank=True, null=True,
                                              db_comment='手术及操作开始日期时间')
    surgicalincisioncategorycode = models.CharField(db_column='surgicalIncisionCategoryCode', max_length=50, blank=True,
                                                    null=True,
                                                    db_comment='手术切口类别代码')
    woundhealinggradecode = models.CharField(db_column='woundHealingGradeCode', max_length=50, blank=True, null=True,
                                             db_comment='切口愈合等级代码')
    woundhealinggradename = models.CharField(db_column='woundHealingGradeName', max_length=50, blank=True, null=True,
                                             db_comment='切口愈合等级名称')
    anesthesiamethodcode = models.CharField(db_column='anesthesiaMethodCode', max_length=50, blank=True, null=True,
                                            db_comment='麻醉方法代码')
    operationprocessdesc = models.TextField(db_column='operationProcessDesc', blank=True, null=True,
                                            db_comment='手术过程')
    principlesmethodstreatment = models.CharField(db_column='principlesMethodsTreatment', max_length=100, blank=True,
                                                  null=True, db_comment='治则治法')
    descriptiondiagnosistreatmentprocess = models.TextField(db_column='descriptionDiagnosisTreatmentProcess',
                                                            blank=True, null=True,
                                                            db_comment='诊疗过程描述')
    treatmentresultcode = models.CharField(db_column='treatmentResultCode', max_length=50, blank=True, null=True,
                                           db_comment='治疗结果代码')
    treatmentresultname = models.CharField(db_column='treatmentResultName', max_length=100, blank=True, null=True,
                                           db_comment='治疗结果名称')
    actuallengthstay = models.IntegerField(db_column='actualLengthStay', blank=True, null=True,
                                           db_comment='实际住院天数')
    decoctingmethodtcm = models.CharField(db_column='decoctingMethodTCM', max_length=100, blank=True, null=True,
                                          db_comment='中药煎煮方法')
    medicationmethodstcm = models.CharField(db_column='medicationMethodsTCM', max_length=100, blank=True, null=True,
                                            db_comment='中药用药方法')
    dischargeorder = models.TextField(db_column='dischargeOrder', blank=True, null=True,
                                      db_comment='出院医嘱')
    positiveauxiliarytestresults = models.TextField(db_column='positiveAuxiliaryTestResults', blank=True, null=True,
                                                    db_comment='阳性辅助检查结果')
    is_finished = models.SmallIntegerField(db_comment='文档完成标识,1:已完成生成,0未生成,默认为0')
    create_datetime = models.DateTimeField(blank=True, null=True, db_comment='记录创建日期时间')
    finished_datetime = models.DateTimeField(blank=True, null=True, db_comment='文档生成日期时间')
    tid = models.BigIntegerField(primary_key=True, db_comment='表主键')
    operationname = models.CharField(db_column='operationName', max_length=100, blank=True,
                                     null=True)
    surgicalincisioncategoryname = models.CharField(db_column='surgicalIncisionCategoryName', max_length=100,
                                                    blank=True, null=True)
    anesthesiamethodname = models.CharField(db_column='anesthesiaMethodName', max_length=100, blank=True,
                                            null=True)
    adm_no = models.CharField(max_length=50, blank=True, null=True)
    updatetime = models.DateTimeField(blank=True, null=True)
    fzyid = models.CharField(db_column='FZYID', max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2, db_comment='数据来源,请参照主数据标准字典:医疗卫生机构')

    class Meta:
        db_table_comment = ''
