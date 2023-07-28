from product.models import Product
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'thumbnail',
            'seller',
            'end_at',
        )