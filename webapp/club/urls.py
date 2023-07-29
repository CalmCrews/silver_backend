from django.urls import path

from club.views.clubListAPIView import ClubListAPIView
from club.views.clubRetrieveAPIView import ClubRetrieveAPIView

urlpatterns = [
    path("", ClubListAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveAPIView.as_view()),
]
