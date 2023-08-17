from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filterset_fields = [
        'category',
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        current_datetime = timezone.now()
        queryset = queryset.filter(end_at__gte=current_datetime)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
