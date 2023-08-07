import requests
from django.conf import settings
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def naverGetLogin(request):
    client_id = settings.NAVER_CONFIG['NAVER_CLIENT_ID']
    state = "RANDOM_STATE"
    redirect_uri = settings.NAVER_CONFIG['NAVER_REDIRECT_URI']
    url = f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}"
    return redirect(url)


@api_view(['GET'])
@permission_classes([AllowAny])
def naverCallback(request):
    client_id = settings.NAVER_CONFIG['NAVER_CLIENT_ID']
    client_secret = settings.NAVER_CONFIG['NAVER_CLIENT_SECRET']
    state = "RANDOM_STATE"
    redirect_uri = settings.NAVER_CONFIG['NAVER_REDIRECT_URI']

    code = request.GET.get("code")

    if code is None:
        return Response({"message": "code is none"}, status=400)

    url = "https://nid.naver.com/oauth2.0/token"
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code,
        'state': state,
    }

    token_response = requests.post(url, data=data)
    token_data = token_response.json()

    if 'access_token' in token_data:
        access_token = token_data['access_token']
        user_info_response = requests.get('https://openapi.naver.com/v1/nid/me', headers={'Authorization': f'Bearer {access_token}'})
        profile_json = user_info_response.json()

        if 'response' in profile_json:
            naverId = profile_json['response'].get("id")
            username = profile_json['response'].get("nickname")

            if naverId is not None:
                if User.objects.filter(naverId=naverId).exists():
                    user_info = User.objects.get(naverId=naverId)
                    refresh = RefreshToken.for_user(user_info)
                    res = {
                        "user": {
                            "id": user_info.id,
                            "naverId": user_info.naverId,
                            "username": user_info.username,
                        },
                        "token": {
                            "access": f"{str(refresh.access_token)}",
                            "refresh": f"{str(refresh)}"
                        }
                    }
                    return Response(res, status=status.HTTP_200_OK)

                else:
                    User(naverId=naverId, username=username).save()
                    user_info = User.objects.get(naverId=naverId)
                    refresh = RefreshToken.for_user(user_info)
                    res = {
                        "user": {
                            "id": user_info.id,
                            "naverId": user_info.naverId,
                            "username": user_info.username,
                        },
                        "token": {
                            "access": f"{str(refresh.access_token)}",
                            "refresh": f"{str(refresh)}"
                        }
                    }
                    return Response(res, status=201)

    return Response({"message": "네이버에서 정보를 가져오는데 실패하였습니다."}, status=400)
