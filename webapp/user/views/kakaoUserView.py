import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
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
    print(profile_json)
    kakaoId = profile_json.get("id")
    print(kakaoId)

    if kakaoId is not None:
        if User.objects.filter(kakaoId=kakaoId).exists():
            print("111111")
            print(User.objects.filter(kakaoId=kakaoId))
            # user_info = User.objects.get(kakaoId=kakaoId)

            refresh = RefreshToken.for_user(user_info)
            print(refresh.access_token)
            return HttpResponse(f' token:{access_token}')

        else:
            print("22222")
            User(kakaoId=kakaoId).save()
            user_info = User.objects.get(kakaoId=kakaoId)
            isMember = False
            return HttpResponse(f'user:{user_info}, token:{access_token}')
    return HttpResponse("kakaoId is None")
