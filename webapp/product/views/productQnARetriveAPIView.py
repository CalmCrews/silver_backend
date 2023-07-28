from rest_framework.generics import RetrieveAPIView

from product.models import ProductQnA
from product.serializers import ProductQnASerializer


class ProductQnARetrieveAPIView(RetrieveAPIView):
    queryset = ProductQnA.objects.all()
    serializer_class = ProductQnASerializer
    lookup_url_kwarg = 'product_qna_id'

    def get_queryset(self):
        queryset = ProductQnA.objects.filter(user=self.request.user)
        return queryset
   