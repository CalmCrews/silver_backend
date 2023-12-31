from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from product.models import ProductQuestion, ProductQnA, Product
from product.permissions import IsProductQuestionOwner
from product.serializers import ProductQuestionSerializer


class ProductQuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductQuestion.objects.all()
    serializer_class = ProductQuestionSerializer
    lookup_url_kwarg = 'product_question_id'
    permission_classes = [IsProductQuestionOwner]

    def get_queryset(self):
        queryset = ProductQuestion.objects.filter(id=self.kwargs.get('product_question_id'))
        return queryset

    def perform_destroy(self, instance):
        instance.delete()
        ProductQnA.objects.filter(
            product=self.get_product(),
            user=self.request.user,
            question=instance,
        ).delete()

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
