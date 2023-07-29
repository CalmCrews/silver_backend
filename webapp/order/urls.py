from django.urls import path

from order.views import OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", OrderListCreateAPIView.as_view()),
    path("<int:order_id>/", OrderRetrieveUpdateDestroyAPIView.as_view()),
]
