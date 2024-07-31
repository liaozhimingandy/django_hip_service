from django.contrib import admin
from django.utils.html import format_html

from django_hip_service import settings
from hipmessageservice.models import Service, Application, StatusShip, Firm, CDA


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
