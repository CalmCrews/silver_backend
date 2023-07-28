from rest_framework.generics import ListAPIView

from product.models import Product
from product.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
