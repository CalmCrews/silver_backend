from django.urls import path

from club.views import ClubListCreateAPIView, ClubRetrieveUpdateAPIView, UserClubNicknameUpdateAPIView, ClubTagUpadateAPIView

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
    path("<int:club_id>/nickname", UserClubNicknameUpdateAPIView.as_view()),
    path("<int:club_id>/tag", ClubTagUpadateAPIView.as_view())
]
