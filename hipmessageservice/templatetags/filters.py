from django import template

register = template.Library()


dict_status_map = {1: '订阅', 2: '发布', 3: '全部'}


@register.simple_tag
def getSubjectStatusTag(dict_status, service, application):
    """得到服务发布订阅要显示都名称"""
    key = f"{service.id}-{application.id}"
    value = dict_status.get(key, '')
    return dict_status_map.get(value, '')
