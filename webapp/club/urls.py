from django.urls import path

from club.views.clubListAPIView import ClubListAPIView

urlpatterns = [
    path("", ClubListAPIView.as_view()),
    ]
