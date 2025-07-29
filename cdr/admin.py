from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget

from cdr.models import CheckReport, BloodTrans, Patient, Check, CheckAppointStatus, \
    CheckStatus, Exam, ExamStatus, InPatient, Operation, OperationSchedule, \
    OperationStatus, OrderFillerStatus, Order, Organization, OutpatientAppointStatus, \
    OutPatient, Pathology, Provider, SourceAndSchedule, Terminology, Transfer, ExamReport, \
    ExamResultDetail, ExamResultDetailAST, ExamResultMain, Discharge, Diagnosis, Visit, EncounterCard, CriticalValue, \
    PathologyReport, CallPatient, PatientInfoCollector


# 基类，自动将所有字段设置为只读
class ReadOnlyAdmin(admin.ModelAdmin):
    list_per_page = 10

    # 禁用删除权限
    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        # 获取所有字段的名称并设置为只读
        readonly_fields = [field.name for field in self.model._meta.fields]
        # 排除某些字段
        # readonly_fields.remove('editable_field')  # 假设 'editable_field' 是你不想让它只读的字段
        return readonly_fields


# Register your models here.
@admin.register(CheckReport)
class CheckReportAdmin(ReadOnlyAdmin):
    """ 检查报告 """

    list_display = ('report_id', 'adm_code', 'adm_no', 'patient_id_new', "patient_name", 'item_code', 'item_name')
    list_display_links = ('report_id',)
    raw_id_fields = ('patient',)

    search_fields = ('report_id', 'adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(BloodTrans)
class BloodTransAppInfoAdmin(ReadOnlyAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id_new', "patient_name", 'apply_desc')
    list_display_links = ('apply_no',)
    raw_id_fields = ('patient',)
    search_fields = ('patient__patient_id', 'apply_no')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Patient)
class PatientInfoAdmin(ReadOnlyAdmin):
    list_display = ('patient_id', 'patient_name', 'sex_code', 'id_no', 'tel_no', 'gmt_birth')
    list_display_links = ('patient_id',)
    ordering = ['-gmt_created', ]

    search_fields = ('patient_id', 'id_no', 'patient_name', 'tel_no')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Check)
class CheckAdmin(ReadOnlyAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id_new', "patient_name", 'item_name', "gmt_effect_high")
    list_display_links = ("apply_no",)
    raw_id_fields = ('patient',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    search_fields = ('apply_no',  'adm_no', 'item_name', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(CheckAppointStatus)
class CheckAppointStatusInfoAdmin(ReadOnlyAdmin):
    list_display = ('adm_no', 'apply_no', 'patient_id_new', "patient_name",)
    raw_id_fields = ('patient',)
    list_display_links = ('apply_no',)

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(CheckStatus)
class CheckStatusInfoAdmin(ReadOnlyAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id_new', "patient_name", 'status_code')
    list_display_links = ('apply_no',)
    raw_id_fields = ('patient',)
    search_fields = ('apply_no', 'adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(EncounterCard)
class EncounterCardAdmin(ReadOnlyAdmin):
    list_display = ('card_no', 'patient_name', 'id_no', 'tel_no')
    list_display_links = ('card_no',)


@admin.register(Exam)
class ExamAppInfoAdmin(ReadOnlyAdmin):
    list_display = ('apply_no', 'patient_id_new', "patient_name", 'item_name')
    list_display_links = ('apply_no',)
    raw_id_fields = ('patient',)
    search_fields = ('patient__patient_id', 'apply_no', 'item_name')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(ExamStatus)
class ExamStatusInfo(ReadOnlyAdmin):
    list_display = ('apply_no', 'adm_no', 'apply_desc', 'patient_id_new', "patient_name", 'status_code')
    raw_id_fields = ('patient',)
    list_display_links = ('apply_no',)
    search_fields = ('apply_no', 'adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(ExamReport)
class ExamReportAdmin(ReadOnlyAdmin):
    """ 检验报告 """
    list_display = ('report_id', 'bar_code', 'url_report_pdf', 'patient_id_new', "patient_name", 'adm_no')
    list_display_links = ('report_id',)
    raw_id_fields = ('patient',)
    search_fields = ('bar_code', 'adm_no', 'report_id', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(ExamResultMain)
class ExamResultMainAdmin(ReadOnlyAdmin):
    """ 检验结果主表 """
    list_display = ('apply_id', 'item_code', 'item_name', 'exam_report_id')
    list_display_links = ('exam_report_id',)
    search_fields = ('exam_report_id',)


@admin.register(ExamResultDetail)
class ExamResultDetailAdmin(ReadOnlyAdmin):
    """检验结果明细表"""
    list_display = ('exam_result_main_id', 'item_code', 'item_name', 'value')
    list_display_links = ('exam_result_main_id',)
    search_fields = ('exam_result_main_id',)


@admin.register(ExamResultDetailAST)
class ExamResultDetailASTAdmin(ReadOnlyAdmin):
    """检验结果药敏结果"""
    list_display = ('exam_result_detail_id', 'ast_code', 'ast_name', "value_qualitative", 'value_ration')
    list_display_links = ('exam_result_detail_id',)
    search_fields = ('exam_result_detail_id',)


@admin.register(InPatient)
class InPatientInfoAdmin(ReadOnlyAdmin):
    list_display = ('adm_no', 'patient_id_new', "patient_name", 'gmt_effect_low', 'dept_name')
    list_display_links = ('adm_no', 'patient_id_new')
    search_fields = ('adm_no', 'patient__patient_id')
    raw_id_fields = ('patient',)
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Discharge)
class DischargeInfoAdmin(ReadOnlyAdmin):
    list_display = ('adm_no', 'patient_id_new', "patient_name", 'gmt_discharge', 'dept_name')
    list_display_links = ('adm_no', 'patient_id_new')
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Operation)
class OperationInfoAdmin(ReadOnlyAdmin):
    list_display = ('apply_no', 'surgical_code', 'surgical_name', 'adm_no', 'patient_id_new', "patient_name",
                    'gmt_apply')
    list_display_links = ('apply_no',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id', 'surgical_name')
    ordering = ('-gmt_created',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(OperationSchedule)
class OperationScheduleInfoAdmin(ReadOnlyAdmin):
    list_display = ('patient_id_new', "patient_name", 'adm_no')
    search_fields = ('patient__patient_id', "patient_name")
    raw_id_fields = ('patient', )

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(OperationStatus)
class OperationStatusInfoAdmin(ReadOnlyAdmin):
    list_display = ('patient_id_new', "patient_name", "adm_no",)
    raw_id_fields = ('patient', )

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(OrderFillerStatus)
class OrderFillerStatusInfoAdmin(ReadOnlyAdmin):
    list_display = ('patient_id_new', "patient_name",)
    raw_id_fields = ('patient', )

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Order)
class OrderInfoAdmin(ReadOnlyAdmin):
    list_display = ('order_id', 'adm_no', 'patient_id_new', "patient_name", 'content', 'gmt_order')
    list_display_links = ('order_id',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')
    # :todo 补充就诊流水号查询
    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Organization)
class OrganizationInfoAdmin(ReadOnlyAdmin):
    list_display = ('dept_id', 'dept_name', 'dept_cls_name', 'pre_dept_name')
    list_display_links = ('dept_id', 'dept_name')

    search_fields = ('dept_id', 'dept_name',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(OutpatientAppointStatus)
class OutpatientAppointStatusInfoAdmin(ReadOnlyAdmin):
    """门诊预约状态"""
    list_display = ('booking_id', 'patient_id_new', "patient_name", 'schedule_id', 'gmt_schedule')
    list_display_links = ('booking_id',)
    raw_id_fields = ('patient',)
    search_fields = ('patient__patient_id', 'patient_name',)

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(OutPatient)
class OutPatientInfoAdmin(ReadOnlyAdmin):
    """门急诊挂号信息"""
    list_display = ('adm_no', 'patient_id_new', 'patient_name', 'doc_name', 'dept_name', 'gmt_reg')
    list_display_links = ('adm_no',)
    raw_id_fields = ('patient',)

    search_fields = ('patient__patient_id', "adm_no")

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    list_select_related = ("patient", )

    def changelist_view(self, request, extra_context=None):
        # 获取 queryset，避免重复计算
        queryset = self.get_queryset(request)
        total_count = queryset.count()  # 获取总数，确保只查询一次
        extra_context = extra_context or {}
        extra_context['total_count'] = total_count
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Pathology)
class PathologyAppInfoAdmin(ReadOnlyAdmin):
    """病理申请单信息"""
    list_display = ('apply_no', 'adm_no', 'patient_id_new', 'patient_name', 'item_name', 'adm_cls_code', 'gmt_created')
    list_display_links = ('apply_no',)
    raw_id_fields = ('patient',)
    search_fields = ('patient__patient_id', 'apply_no')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Provider)
class ProviderInfoAdmin(ReadOnlyAdmin):
    """卫生人员机构"""
    list_display = ('emp_id', 'emp_name', 'id_no', 'sex_code', 'telecom')
    list_display_links = ('emp_id',)

    search_fields = ('emp_id', 'emp_name')


@admin.register(SourceAndSchedule)
class SourceAndScheduleInfoAdmin(ReadOnlyAdmin):
    pass


@admin.register(Terminology)
class TerminologyAdmin(ReadOnlyAdmin):
    """术语信息"""
    list_display = ('dataset_code', 'dataset_name', 'item_code', 'item_name')
    list_display_links = ('item_code',)

    search_fields = ('dataset_code', 'dataset_name', 'item_code', 'item_name')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }


@admin.register(Transfer)
class TransferInfoAdmin(ReadOnlyAdmin):
    """转科信息"""
    list_display = ('adm_no', 'patient_id_new', "patient_name", 'gmt_in', 'gmt_out')
    list_display_links = ('adm_no',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Diagnosis)
class DiagnosisAdmin(ReadOnlyAdmin):
    """诊断信息"""
    list_display = ('diagnosis_id', 'adm_no', 'patient_id_new', "patient_name", 'diag_code', 'diag_name', 'adm_cls_code', 'from_src')
    list_display_links = ('diagnosis_id',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(Visit)
class VisitAdmin(ReadOnlyAdmin):
    """就诊信息"""
    list_display = ('adm_no', 'patient_id_new', "patient_name", "doctor_id", "doctor_name",
                    'visit_status', 'gmt_visit_start', 'gmt_visit_end', 'adm_cls_code', 'index')
    list_display_links = ('adm_no',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(CriticalValue)
class CriticalValueAdmin(ReadOnlyAdmin):
    """危急值信息"""
    list_display = ('critical_id', 'adm_no', 'patient_id_new', "patient_name", 'item_code', 'item_name',
                    'value', 'gmt_report')
    list_display_links = ('critical_id',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(PathologyReport)
class PathologyReportAdmin(ReadOnlyAdmin):
    """病理报告"""
    list_display = ('report_id', 'adm_no', 'patient_id_new', "patient_name", 'item_code', 'item_name', 'url_report_pdf')
    list_display_links = ('report_id',)
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(CallPatient)
class CallPatientAdmin(ReadOnlyAdmin):
    list_display = ('patient_id_new', "patient_name", 'adm_no', 'gmt_call', 'index', 'doc_id', 'doc_name',
                    'dept_id', 'dept_name')
    raw_id_fields = ('patient',)
    search_fields = ('adm_no', 'patient__patient_id')
    list_display_links = ('adm_no',)

    @admin.display(description="患者ID")
    def patient_id_new(self, obj):
        return f"{obj.patient.patient_id}"

    @admin.display(description="患者姓名")
    def patient_name(self, obj):
        return f"{obj.patient.patient_name}"


@admin.register(PatientInfoCollector)
class PatientInfoCollectorAdmin(ReadOnlyAdmin):
    list_display = ('id_no', "name", 'mobile_phone', "contact_code", 'debit_card_name', 'debit_card_no', 'bank_name', 'gmt_created')
    search_fields = ('id_no', 'mobile_phone', 'name')
    list_display_links = ('id_no',)