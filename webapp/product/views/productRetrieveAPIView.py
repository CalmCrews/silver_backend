from rest_framework.generics import RetrieveAPIView

from product.models import Product
from product.serializers import ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
