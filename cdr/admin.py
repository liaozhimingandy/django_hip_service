from django.contrib import admin

from cdr.models import CheckReport, BloodTransAppInfo, PatientInfo, CheckAppInfo, CheckAppointStatusInfo, \
    CheckStatusInfo, ExamAppInfo, ExamStatusInfo, InPatientDischargeInfo, OperationAppInfo, OperationScheduleInfo, \
    OperationStatusInfo, OrderFillerStatusInfo, OrderInfo, OrganizationInfo, OutpatientAppointStatusInfo, \
    OutPatientInfo, PathologyAppInfo, ProviderInfo, SourceAndScheduleInfo, Terminology, TransferInfo


# Register your models here.
@admin.register(CheckReport)
class CheckReportAdmin(admin.ModelAdmin):
    list_display = ('report_id', 'adm_code', 'adm_no', 'item_code', 'item_name')
    list_display_links = ('report_id',)


@admin.register(BloodTransAppInfo)
class BloodTransAppInfoAdmin(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id')


@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    list_display = ('patient_id', 'empi_id', 'patient_name', 'sex_code')
    list_display_links = ('patient_id',)


@admin.register(CheckAppInfo)
class CheckAppInfo(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'item_name')
    list_display_links = ("apply_no", )


@admin.register(CheckAppointStatusInfo)
class CheckAppointStatusInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'apply_no', 'patient_id')


@admin.register(CheckStatusInfo)
class CheckStatusInfoAdmin(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')


@admin.register(ExamAppInfo)
class ExamAppInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'apply_no', 'item_name')


@admin.register(ExamStatusInfo)
class ExamStatusInfo(admin.ModelAdmin):
    list_display = ('apply_no', 'adm_no', 'patient_id', 'status_code')


@admin.register(InPatientDischargeInfo)
class InPatientDischargeInfoAdmin(admin.ModelAdmin):
    list_display = ('adm_no', 'patient_id', 'gmt_effect_low', 'dept_name')


@admin.register(OperationAppInfo)
class OperationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OperationScheduleInfo)
class OperationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OperationStatusInfo)
class OperationStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderFillerStatusInfo)
class OrderFillerStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OrganizationInfo)
class OrganizationInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OutpatientAppointStatusInfo)
class OutpatientAppointStatusInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(OutPatientInfo)
class OutPatientInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(PathologyAppInfo)
class PathologyAppInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(ProviderInfo)
class ProviderInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(SourceAndScheduleInfo)
class SourceAndScheduleInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Terminology)
class TerminologyAdmin(admin.ModelAdmin):
    pass


@admin.register(TransferInfo)
class TransferInfoAdmin(admin.ModelAdmin):
    pass
