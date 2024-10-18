"""
URL configuration for django_hip_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from django_hip_service import settings

from evaluation.views import DownloadZipView

from hipmessageservice.views import index, download as download_count, generate_report

from .api import api
from .schema import schema

urlpatterns = [
    path('', index),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('download/', download_count, name='download-count'),
    path("test/", generate_report),
    # path('messsage/download/', download),
    path('v3/', api.urls),
    path('download-zip/<str:content_type>/<uuid:temp_dir_path>/', DownloadZipView.as_view(), name='download_zip'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),  # graphiql=True 打开 GraphiQL 浏览器

]

# 开发环境提供静态文件和多媒体查看功能;这一般会在 DEBUG is set to True 情况下由 runserver 自动完成
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 开发调试时使用
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


