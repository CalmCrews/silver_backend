from django.urls import path

from review.views import ReviewListCreateAPIView

urlpatterns = [
    path("", ReviewListCreateAPIView.as_view()),
]
