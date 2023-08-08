from django.urls import path

from club.views import *

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
    path("join/", UserClubJoinCreateAPIView.as_view()),
]
