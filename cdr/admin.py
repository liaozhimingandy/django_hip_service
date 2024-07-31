from django.contrib import admin

from cdr.models import CheckReport, BloodTrans, Patient, Check, CheckAppointStatus, \
    CheckStatus, Exam, ExamStatus, InPatient, Operation, OperationSchedule, \
    OperationStatus, OrderFillerStatus, Order, Organization, OutpatientAppointStatus, \
    OutPatient, Pathology, Provider, SourceAndSchedule, Terminology, Transfer, ExamReport, \
    ExamResultDetail, ExamResultDetailAST, ExamResultMain, Discharge, Diagnosis, Visit, EncounterCard


# Register your models here.
@admin.register(CheckReport)
class CheckReportAdmin(admin.ModelAdmin):
    """ 检查报告 """
    list_display = ('report_id', 'adm_code', 'adm_no', 'patient_id', 'item_code', 'item_name')
    list_display_links = ('report_id',)

    search_fields = ('report_id', 'adm_no', 'patient_id')


@admin.register(BloodTrans)
class BloodTransAppInfoAdmin(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id')


@admin.register(Patient)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'patient_name', 'sex_code', 'id_no', 'tel_no', 'gmt_birth')
    list_display_links = ('patient_id',)

    search_fields = ('patient_id', 'id_no')


@admin.register(Check)
class CheckAppInfo(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'item_name')
    list_display_links = ("apply_no",)


@admin.register(CheckAppointStatus)
class CheckAppointStatusInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'apply_no', 'patient_id')
    list_display_links = ('apply_no',)


@admin.register(CheckStatus)
class CheckStatusInfoAdmin(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')
    list_display_links = ('apply_no',)


@admin.register(EncounterCard)
class EncounterCardAdmin(admin.ModelAdmin):
    list_display = ('card_no', 'patient_name', 'id_no', 'tel_no')
    list_display_links = ('card_no',)


@admin.register(Exam)
class ExamAppInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'apply_no', 'item_name')
    list_display_links = ('apply_no',)


@admin.register(ExamStatus)
class ExamStatusInfo(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')
    list_display_links = ('apply_no',)


@admin.register(ExamReport)
class ExamReportAdmin(admin.ModelAdmin):
    """ 检验报告 """
    list_display = ('report_id', 'bar_code', 'url_report_pdf', 'patient_id', 'adm_no')
    list_display_links = ('report_id',)

    search_fields = ('bar_code', 'adm_no', 'report_id')


@admin.register(ExamResultMain)
class ExamResultMainAdmin(admin.ModelAdmin):
    """ 检验结果主表 """
    list_display = ('apply_id', 'item_code', 'item_name', 'exam_report_id')
    list_display_links = ('exam_report_id',)


@admin.register(ExamResultDetail)
class ExamResultDetailAdmin(admin.ModelAdmin):
    """检验结果明细表"""
    list_display = ('exam_result_main_id', 'item_code', 'item_name', 'value')
    list_display_links = ('exam_result_main_id',)


@admin.register(ExamResultDetailAST)
class ExamResultDetailASTAdmin(admin.ModelAdmin):
    """检验结果药敏结果"""
    list_display = ('exam_result_detail_id', 'ast_code', 'ast_name', "value_qualitative", 'value_ration')
    list_display_links = ('exam_result_detail_id',)


@admin.register(InPatient)
class InPatientInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'gmt_effect_low', 'dept_name')
    list_display_links = ('adm_no', 'patient_id')


@admin.register(Discharge)
class DischargeInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'gmt_discharge', 'dept_name')
    list_display_links = ('adm_no', 'patient_id')


@admin.register(Operation)
class OperationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OperationSchedule)
class OperationScheduleInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OperationStatus)
class OperationStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderFillerStatus)
class OrderFillerStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OutpatientAppointStatus)
class OutpatientAppointStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OutPatient)
class OutPatientInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'doc_name', 'dept_name', 'gmt_reg')
    list_display_links = ('adm_no',)

    search_fields = ('patient_id',)


@admin.register(Pathology)
class PathologyAppInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Provider)
class ProviderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(SourceAndSchedule)
class SourceAndScheduleInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Terminology)
class TerminologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Transfer)
class TransferInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass
