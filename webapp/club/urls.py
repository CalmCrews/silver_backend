from django.urls import path

from club.views import *

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
    path("<int:club_id>/clubProducts", ClubProductListAPIView.as_view()),
    path("<int:club_id>/clubProducts/<int:club_product_id>", ClubProductRetrieveAPIView.as_view()),
    path("join/", UserClubJoinCreateAPIView.as_view()),
    path("userClubProducts/", UserClubProductListAPIView.as_view()),
    path("allClubProducts/", AllClubProductListAPIView.as_view()),
]
