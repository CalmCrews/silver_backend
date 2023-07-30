from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView

from product.models import ProductQuestion, Product, ProductQnA
from product.serializers import ProductQuestionSerializer


class ProductQuestionCreateAPIView(CreateAPIView):
    queryset = ProductQuestion.objects.all()
    serializer_class = ProductQuestionSerializer

    def perform_create(self, serializer):
        serializer.save()
        ProductQnA.objects.create(
            product=self.get_product(),
            user=self.request.user,
            question=serializer.instance,
        )

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
