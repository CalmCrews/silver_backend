from django.urls import path, include

from order.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("clubs/<int:club_id>/", OrderListCreateAPIView.as_view()),
    path("<int:order_id>/", OrderRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:order_id>/reviews/", include('review.urls')),
]
