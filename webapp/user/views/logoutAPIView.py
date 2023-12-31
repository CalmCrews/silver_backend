from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from user.serializers import LogoutSerializer


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({"message": "로그아웃 성공"},
                                status=200)
            except TokenError:
                return Response({"message": "유효하지 않은 토큰입니다."},
                                status=400)
        return Response({"message": "Refresh 토큰이 필요합니다."},
                        status=400)
