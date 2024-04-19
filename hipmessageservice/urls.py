# url 命令空间
from django.urls import path
from rest_framework.routers import DefaultRouter

from hipmessageservice import views
from hipmessageservice.views import verificationViewSet

app_name = 'service'

urlpatterns = [
]
# api根路由
router = DefaultRouter()
router.register(r'verify', verificationViewSet, basename='verify')

urlpatterns += router.urls