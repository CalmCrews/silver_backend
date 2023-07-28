import requests
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakaoGetLogin(request):
    CLIENT_ID = settings.KAKAO_CONFIG['KAKAO_REST_API_KEY']
    REDIRET_URL = settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI']
    url = f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRET_URL}&response_type=code"
    return redirect(url)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def kakaoCallback(request):
    url = "https://kauth.kakao.com/oauth/token"
    code = request.GET.get("code")

    if code is None:
        raise Exception("code is none")

    res = {
        'grant_type': 'authorization_code',
        "client_id": settings.KAKAO_CONFIG['KAKAO_REST_API_KEY'],
        "redirect_uri": settings.KAKAO_CONFIG['KAKAO_REDIRECT_URI'],
        'code': code,
    }
    token_response = requests.post(url, data=res)
    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer {access_token}'})
    profile_json = user_info_response.json()
    kakaoId = profile_json.get("id")

    if kakaoId is not None:
        if User.objects.filter(kakaoId=kakaoId).exists():
            user_info = User.objects.get(kakaoId=kakaoId)
            refresh = RefreshToken.for_user(user_info)
            res = {
                "user": {
                    "id": user_info.id,
                    "kakaoId": user_info.kakaoId,
                },
                "token": {
                    "access": f"{str(refresh.access_token)}",
                    "refresh": f"{str(refresh)}"
                }
            }
            return Response(res, status=200)

        else:
            User(kakaoId=kakaoId).save()
            user_info = User.objects.get(kakaoId=kakaoId)
            refresh = RefreshToken.for_user(user_info)
            res = {
                "user": {
                    "id": user_info.id,
                    "kakaoId": user_info.kakaoId,
                },
                "token": {
                    "access": f"{str(refresh.access_token)}",
                    "refresh": f"{str(refresh)}"
                }
            }
            return Response(res, status=201)
    return Response({"message": "kakaoId가 존재하지 않습니다."}, status=400)
