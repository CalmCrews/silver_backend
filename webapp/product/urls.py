from django.urls import path
from product.views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view()),
    path("<int:product_id>/", ProductRetrieveAPIView.as_view()),
]
