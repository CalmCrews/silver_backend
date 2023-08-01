from django.urls import path

from user.views import RegisterAPIView, LoginAPIView, LogoutAPIView, kakaoCallback, kakaoGetLogin, naverGetLogin, naverCallback
from order.views import MyOrderListForAllProductsAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("signin/", LoginAPIView.as_view()),
    path("signout/", LogoutAPIView.as_view()),
    path('kakao/login/', kakaoGetLogin),
    path('kakao/callback/', kakaoCallback, name="kakaoCallback"),
    path('naver/login/', naverGetLogin),
    path('naver/callback/', naverCallback, name="naverCallback"),
    path('myorders/', MyOrderListForAllProductsAPIView.as_view()),
]
