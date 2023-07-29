from django.urls import path

from order.views import OrderCreateAPIView

urlpatterns = [
    path("", OrderCreateAPIView.as_view()),

]
