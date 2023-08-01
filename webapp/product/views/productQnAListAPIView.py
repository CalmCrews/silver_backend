from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from product.models import Product, ProductQnA
from product.serializers import ProductQnASerializer


class ProductQnAListAPIView(ListAPIView):
    queryset = ProductQnA.objects.all()
    serializer_class = ProductQnASerializer

    def get_queryset(self):
        queryset = ProductQnA.objects.filter(user=self.request.user, product=self.get_product())
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # TODO: 프론트 요청에 맞추어 user, product 정보 추가
        serializer = self.get_serializer(queryset, many=True)
        user = str(self.request.user)
        product = self.get_product().name
        res = {
            'user': user,
            'product': product,
            'data': serializer.data
        }

        return Response(res)

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
