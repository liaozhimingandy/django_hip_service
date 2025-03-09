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

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from django_hip_service import settings
from hipmessageservice.views import index, download as download_count, generate_report
from .api import api
from .schema import schema

urlpatterns = [
    path('', index),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('download/', download_count, name='download-count'),
    path("test/", generate_report),
    path('v3/', api.urls),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),  # graphiql=True 打开 GraphiQL 浏览器

]

# 开发调试时使用
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += staticfiles_urlpatterns()


