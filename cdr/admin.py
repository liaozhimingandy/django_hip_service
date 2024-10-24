from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from cdr.models import CheckReport, BloodTrans, Patient, Check, CheckAppointStatus, \
    CheckStatus, Exam, ExamStatus, InPatient, Operation, OperationSchedule, \
    OperationStatus, OrderFillerStatus, Order, Organization, OutpatientAppointStatus, \
    OutPatient, Pathology, Provider, SourceAndSchedule, Terminology, Transfer, ExamReport, \
    ExamResultDetail, ExamResultDetailAST, ExamResultMain, Discharge, Diagnosis, Visit, EncounterCard, CriticalValue, \
    PathologyReport

PER_PAGE = 10


# Register your models here.
@admin.register(CheckReport)
class CheckReportAdmin(admin.ModelAdmin):
    """ 检查报告 """
    list_per_page = PER_PAGE
    list_display = ('report_id', 'adm_code', 'adm_no', 'patient_id', 'item_code', 'item_name')
    list_display_links = ('report_id',)

    search_fields = ('report_id', 'adm_no', 'patient_id')


@admin.register(BloodTrans)
class BloodTransAppInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('apply_no', 'adm_no', 'patient_id')
    list_display_links = ('apply_no',)


@admin.register(Patient)
class PatientInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('patient_id', 'patient_name', 'sex_code', 'id_no', 'tel_no', 'gmt_birth')
    list_display_links = ('patient_id',)
    ordering = ['-gmt_created', ]

    search_fields = ('patient_id', 'id_no', 'patient_name', 'tel_no')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Check)
class CheckAppInfo(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('apply_no', 'adm_no', 'patient_id', 'item_name')
    list_display_links = ("apply_no",)


@admin.register(CheckAppointStatus)
class CheckAppointStatusInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'apply_no', 'patient_id')
    list_display_links = ('apply_no',)


@admin.register(CheckStatus)
class CheckStatusInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')
    list_display_links = ('apply_no',)


@admin.register(EncounterCard)
class EncounterCardAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('card_no', 'patient_name', 'id_no', 'tel_no')
    list_display_links = ('card_no',)


@admin.register(Exam)
class ExamAppInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('patient_id', 'apply_no', 'item_name')
    list_display_links = ('apply_no',)

    search_fields = ('patient_id', 'apply_no', 'item_name')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(ExamStatus)
class ExamStatusInfo(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')
    list_display_links = ('apply_no',)


@admin.register(ExamReport)
class ExamReportAdmin(admin.ModelAdmin):
    """ 检验报告 """
    list_per_page = PER_PAGE
    list_display = ('report_id', 'bar_code', 'url_report_pdf', 'patient_id', 'adm_no')
    list_display_links = ('report_id',)

    search_fields = ('bar_code', 'adm_no', 'report_id')


@admin.register(ExamResultMain)
class ExamResultMainAdmin(admin.ModelAdmin):
    """ 检验结果主表 """
    list_per_page = PER_PAGE
    list_display = ('apply_id', 'item_code', 'item_name', 'exam_report_id')
    list_display_links = ('exam_report_id',)

    search_fields = ('exam_report_id',)


@admin.register(ExamResultDetail)
class ExamResultDetailAdmin(admin.ModelAdmin):
    """检验结果明细表"""
    list_per_page = PER_PAGE
    list_display = ('exam_result_main_id', 'item_code', 'item_name', 'value')
    list_display_links = ('exam_result_main_id',)

    search_fields = ('exam_result_main_id',)


@admin.register(ExamResultDetailAST)
class ExamResultDetailASTAdmin(admin.ModelAdmin):
    """检验结果药敏结果"""
    list_per_page = PER_PAGE
    list_display = ('exam_result_detail_id', 'ast_code', 'ast_name', "value_qualitative", 'value_ration')
    list_display_links = ('exam_result_detail_id',)

    search_fields = ('exam_result_detail_id',)


@admin.register(InPatient)
class InPatientInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'gmt_effect_low', 'dept_name')
    list_display_links = ('adm_no', 'patient_id')

    search_fields = ('adm_no', 'patient_id')


@admin.register(Discharge)
class DischargeInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'gmt_discharge', 'dept_name')
    list_display_links = ('adm_no', 'patient_id')

    search_fields = ('adm_no', 'patient_id')


@admin.register(Operation)
class OperationInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('apply_no', 'surgical_code', 'surgical_name', 'adm_no', 'patient_id')
    list_display_links = ('apply_no',)

    search_fields = ('adm_no', 'patient_id', 'surgical_name')
    ordering = ('-gmt_created',)


@admin.register(OperationSchedule)
class OperationScheduleInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


@admin.register(OperationStatus)
class OperationStatusInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


@admin.register(OrderFillerStatus)
class OrderFillerStatusInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


@admin.register(Order)
class OrderInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('order_id', 'adm_no', 'patient_id', 'content', 'gmt_order')
    list_display_links = ('order_id',)

    search_fields = ('adm_no', 'patient_id')


@admin.register(Organization)
class OrganizationInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('dept_id', 'dept_name', 'dept_cls_name', 'pre_dept_name')
    list_display_links = ('dept_id', 'dept_name')

    search_fields = ('dept_id', 'dept_name',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(OutpatientAppointStatus)
class OutpatientAppointStatusInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('booking_id', 'patient_id', 'patient_name', 'schedule_id', 'gmt_schedule')
    list_display_links = ('booking_id',)

    search_fields = ('patient_id', 'patient_name',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(OutPatient)
class OutPatientInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'doc_name', 'dept_name', 'gmt_reg')
    list_display_links = ('adm_no',)

    search_fields = ('patient_id',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Pathology)
class PathologyAppInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE

    list_display = ('apply_no', 'adm_no', 'patient_id', 'item_name', 'adm_cls_code', 'gmt_created')
    list_display_links = ('apply_no',)

    search_fields = ('patient_id', 'item_name')


@admin.register(Provider)
class ProviderInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('emp_id', 'emp_name', 'sex_code', 'telecom')
    list_display_links = ('emp_id',)

    search_fields = ('emp_id', 'emp_name')


@admin.register(SourceAndSchedule)
class SourceAndScheduleInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE


@admin.register(Terminology)
class TerminologyAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('dataset_code', 'dataset_name', 'item_code', 'item_name')
    list_display_links = ('item_code',)

    search_fields = ('dataset_code', 'dataset_name', 'item_code', 'item_name')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Transfer)
class TransferInfoAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'gmt_in', 'gmt_out')
    list_display_links = ('adm_no',)

    search_fields = ('adm_no', 'patient_id')


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'diag_code', 'diag_name', 'adm_cls_code')
    list_display_links = ('adm_no',)

    search_fields = ('adm_no', 'patient_id')


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('adm_no', 'patient_id', 'gmt_visit_start', 'gmt_visit_end', 'adm_cls_code', 'index')
    list_display_links = ('adm_no',)

    search_fields = ('adm_no', 'patient_id')


@admin.register(CriticalValue)
class CriticalValueAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('critical_id', 'adm_no', 'patient_id', 'item_code', 'item_name', 'value')
    list_display_links = ('critical_id',)

    search_fields = ('adm_no', 'patient_id')


@admin.register(PathologyReport)
class PathologyReportAdmin(admin.ModelAdmin):
    list_per_page = PER_PAGE
    list_display = ('report_id', 'adm_no', 'patient_id', 'item_code', 'item_name', 'url_report_pdf')
    list_display_links = ('report_id',)

    search_fields = ('adm_no', 'patient_id')
