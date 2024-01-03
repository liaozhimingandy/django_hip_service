from django.apps import AppConfig


class EsbStandardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'esb_standard'
    verbose_name = "集成平台标准数据"
