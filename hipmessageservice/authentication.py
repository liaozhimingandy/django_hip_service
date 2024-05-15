from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from .common.token import verify_jwt_token


class AuthBearer(BaseAuthentication):
    """Bearer authentication
    todo: 后续完善错误详细,目前统一返回 "detail": "Unauthorized"
    """
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')[1]
        # 校验jwt token并解析数据
        grant_type = "access_token"
        jwt_decode = verify_jwt_token(token, grant_type=grant_type)

        # 如果验证成功,则返回多个key的数据
        if len(jwt_decode.keys()) < 2:
            raise AuthenticationFailed(jwt_decode)

        # 借用user保存登录信息
        user = User(id=jwt_decode['app_id'], username=jwt_decode['salt'])

        return user.id, user
