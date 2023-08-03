from django.urls import path

from club.views.clubListCreateAPIView import ClubListCreateAPIView
from club.views.clubRetrieveUpdateAPIView import ClubRetrieveUpdateAPIView

urlpatterns = [
    path("", ClubListCreateAPIView.as_view()),
    path("<int:club_id>", ClubRetrieveUpdateAPIView.as_view()),
]
