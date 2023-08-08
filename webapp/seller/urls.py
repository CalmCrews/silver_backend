from django.urls import path
from .views import *

urlpatterns = [
    path("<int:seller_id>", SellerRetrieveAPIView.as_view()),
]
