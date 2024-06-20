# url 命令空间
from rest_framework.routers import DefaultRouter

from hipmessageservice.views import VerificationViewset, HIPMessageServiceViewSet

app_name = 'openim'

urlpatterns = [
]
# api根路由
router = DefaultRouter()
router.register(r'verify', VerificationViewset, basename='verify')
router.register(r'service', HIPMessageServiceViewSet, basename="service")
urlpatterns += router.urls
