from django.contrib import admin
from django.utils.html import format_html
from rich.status import Status

from django_hip_service import settings
from hipmessageservice.models import Service, Application, StatusShip, Firm, CDA, Mock


# Register your models here.


class StatusShipInline(admin.TabularInline):
    """服务系统状态"""
    model = Service.applications.through


class CDAStatusAdmin(admin.TabularInline):
    """cda厂商状态"""
    model = CDA.firm.through


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["service_code", "service_name", "service_category", "service_rank", "service_status",
                    "is_lookup"]
    search_fields = ["service_name"]
    list_filter = ["service_category", "service_rank", "is_v3", "is_lookup", "service_status"]
    ordering = ["service_queue", ]
    list_per_page = 10

    inlines = [StatusShipInline, ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["application_name", "application_category", ]
    ordering = ["application_category", ]
    search_fields = ["application_name"]
    list_filter = ["application_category", "firm__firm_name", "is_customer", "is_deleted"]
    list_per_page = 10
    inlines = [StatusShipInline, ]
    readonly_fields = ["display_application_id", ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()

    def display_application_id(self, obj):
        return f"{settings.PREFIX_ID}{obj.application_id}"

    display_application_id.short_description = "您的应用唯一ID"


@admin.register(StatusShip)
class StatusShipAdmin(admin.ModelAdmin):
    list_display = ["application", "service", "status", "is_online"]
    search_fields = ["service__service_name", "application__application_name", ]
    list_filter = ["service__service_name", "application__application_name", "is_online"]
    list_per_page = 10

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()


@admin.register(Firm)
class FirmAdmin(admin.ModelAdmin):
    list_display = ["firm_id", "firm_name", "firm_name_short"]
    list_editable = ["firm_name", "firm_name_short"]
    search_fields = ["firm_name"]
    list_per_page = 10
    readonly_fields = ['firm_id', ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()


@admin.register(CDA)
class CDAAdmin(admin.ModelAdmin):
    list_display = ["value", "comment"]
    list_display_links = ["value"]
    search_fields = ["value", "comment"]
    list_per_page = 10
    ordering = ["value", ]
    list_filter = ["firm"]
    filter_horizontal = ["firm", ]

    inlines = [CDAStatusAdmin, ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_deleted=False)

    def delete_queryset(self, request, queryset):
        for item in queryset:
            item.is_deleted = True
            item.save()

@admin.register(Mock)
class MockAdmin(admin.ModelAdmin):
    list_per_page = 10
    fields = ("send", "service", "receive")
    list_display = ("send_application_name", "service_name", "receive_application_name")
    list_display_links = ["service_name"]
    list_filter  = ["service__service_name",]
    search_fields = ["service__service_name", "send__application_name", "receive__application_name"]
    search_help_text = "您可以根据服务名称,系统名称进行搜索"

    @admin.display(description="发送方", empty_value="未知", ordering="send__application_name")
    def send_application_name(self, obj):
        return obj.send.application_name

    @admin.display(description="接收方", empty_value="未知", ordering="receive__application_name")
    def receive_application_name(self, obj):
        return obj.receive.application_name

    @admin.display(description="服务名称", empty_value="未知", ordering="service__service_name")
    def service_name(self, obj):
        return obj.service.service_name