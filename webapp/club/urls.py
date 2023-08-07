from django.urls import path

from club.views.clubListCreateAPIView import ClubListCreateAPIView
from club.views.clubRetrieveUpdateAPIView import ClubRetrieveUpdateAPIView
from club.views.duplicateNicknameAPIView import DuplicateNickNameAPIView
from club.views.userClubJoinCreateAPIVIew import UserClubJoinCreateAPIView
from club.views.userClubNicknameUpdateAPIView import UserClubNicknameUpdateAPIView

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
    path("<int:club_id>/nickname", UserClubNicknameUpdateAPIView.as_view()),
    path("join/", UserClubJoinCreateAPIView.as_view()),
    path("<int:club_id>/duplicatenickname", DuplicateNickNameAPIView.as_view()),
]
