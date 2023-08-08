from django.urls import path

from club.views.clubListCreateAPIView import ClubListCreateAPIView
from club.views.clubRetrieveUpdateAPIView import ClubRetrieveUpdateAPIView
from club.views.userClubJoinCreateAPIVIew import UserClubJoinCreateAPIView

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
    path("join/", UserClubJoinCreateAPIView.as_view()),
]
