from django.urls import path

from user.views import *

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("signin/", LoginAPIView.as_view()),
    path("signout/", LogoutAPIView.as_view()),
    path('kakao/login/', kakaoGetLogin),
    path('kakao/callback/', kakaoCallback, name="kakaoCallback"),
    path('naver/login/', naverGetLogin),
    path('naver/callback/', naverCallback, name="naverCallback"),
    path('duplicateUserId/', DuplicateUserNameAPIView.as_view()),
    path('<int:user_id>/charge/', ChargeBalanceAPIView.as_view()),
    path('nickname/', UserNicknameUpdateAPIView.as_view()),
    path('duplicateNickname/', DuplicateNickameAPIView.as_view()),
    path('userinfo', UserinfoAPIView.as_view()),
]
