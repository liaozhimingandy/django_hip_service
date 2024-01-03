import logging

from django.contrib import admin, messages
from django.utils.html import format_html
from import_export.admin import ImportExportModelAdmin, ExportActionModelAdmin

from esb_standard.models import DictMain, Dict, DataSet, DataElement, Service, MessageFormat
from esb_standard.resources import DictMainModelResource, DictModelResource, DataElementModelResource, \
    DataSetModelResource

admin.AdminSite.site_title = "标准文档后台管理"
admin.AdminSite.site_header = "后台管理"

common_list_display = ["value", "comment", "is_deleted", "gmt_updated"]
common_set_change = {"value", "comment", "is_deleted"}

logger = logging.getLogger("mylogger")


# Register your models here.
@admin.register(DictMain)
class DictMainModelResourceAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    list_display = ["id"] + common_list_display
    list_editable = ["value", "comment"]
    # 导入导出类
    resource_class = DictMainModelResource

    # def message_user(self, request, message, level=messages.INFO, extra_tags="", fail_silently=False):
    #     return super().message_user(request, message, level, extra_tags, fail_silently)

    def save_model(self, request, obj, form, change):
        """
        重新保存模型方法
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if not common_set_change & set(form.changed_data):
            # 设置只显示警告以上的提示信息
            messages.set_level(request, messages.WARNING)
            messages.warning(request,
                             format_html(f'没有需要修改的数据,请点击此链接查看:<a href="{request.path}">{obj}</a>'))
            logger.info(f'没有需要修改的数据,请点击此链接查看:<a href="{request.path}">{obj}</a>')
            return

        if not change:
            obj.creator = request.user
        obj.reviser = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        过滤已删除的数据
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_deleted=0)

    def has_import_permission(self, request):  # 这是隐藏导入按钮，如果隐藏其他按钮也可以这样操作，
        return True if request.user.is_superuser else False

    def has_export_permission(self, request):
        # 已有action导出功能,屏蔽导出所有功能
        return False


@admin.register(Dict)
class DictModelResourceAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    list_display = ["value", "comment", "is_deleted", 'value_dict', "gmt_updated"]
    # 导入导出类
    resource_class = DictModelResource

    def save_model(self, request, obj, form, change):
        """
        重新保存模型方法
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if not common_set_change & set(form.changed_data):
            # 设置只显示警告以上的提示信息
            messages.set_level(request, messages.WARNING)
            messages.warning(request,
                             format_html(f'没有需要修改的数据,请点击此链接查看:<a href="{request.path}">{obj}</a>'))
            return

        if not change:
            obj.creator = request.user
        obj.reviser = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        过滤已删除的数据
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_deleted=0)

    def has_import_permission(self, request):  # 这是隐藏导入按钮，如果隐藏其他按钮也可以这样操作，
        return True if request.user.is_superuser else False

    def has_export_permission(self, request):
        # 已有action导出功能,屏蔽导出所有功能
        return False


@admin.register(DataSet)
class DataSetModelResourceModelAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    list_display = common_list_display
    # 导入导出类
    resource_class = DataSetModelResource

    def save_model(self, request, obj, form, change):
        """
        重新保存模型方法
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if not common_set_change & set(form.changed_data):
            # 设置只显示警告以上的提示信息
            messages.set_level(request, messages.WARNING)
            messages.warning(request,
                             format_html(f'没有需要修改的数据,请点击此链接查看:<a href="{request.path}">{obj}</a>'))
            return

        if not change:
            obj.creator = request.user
        obj.reviser = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        过滤已删除的数据
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_deleted=0)

    def has_import_permission(self, request):  # 这是隐藏导入按钮，如果隐藏其他按钮也可以这样操作，
        return True if request.user.is_superuser else False

    def has_export_permission(self, request):
        # 已有action导出功能,屏蔽导出所有功能
        return False


@admin.register(DataElement)
class DataElementModelResourceAdmin(ImportExportModelAdmin, ExportActionModelAdmin):
    list_display = ["hd_code", "de_code", "de_en_code", "de_name", "definition", "data_type", "expression",
                    "allowable_value", "length", "data_set"]
    # 导入导出类
    resource_class = DataElementModelResource

    def save_model(self, request, obj, form, change):
        """
        重新保存模型方法
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        if not {"hd_code", "de_code", "de_en_code", "de_name", "definition", "data_type", "expression",
                "allowable_value", "length", "data_set"} & set(form.changed_data):
            # 设置只显示警告以上的提示信息
            messages.set_level(request, messages.WARNING)
            messages.warning(request,
                             format_html(f'没有需要修改的数据,请点击此链接查看:<a href="{request.path}">{obj}</a>'))

            return

        if not change:
            obj.creator = request.user
        obj.reviser = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        过滤已删除的数据
        :param request:
        :return:
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_deleted=0)

    def has_import_permission(self, request):  # 这是隐藏导入按钮，如果隐藏其他按钮也可以这样操作，
        return True if request.user.is_superuser else False

    def has_export_permission(self, request):
        # 已有action导出功能,屏蔽导出所有功能
        return False


@admin.register(Service)
class ServiceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(MessageFormat)
class MessageFormatModelAdmin(admin.ModelAdmin):
    pass
