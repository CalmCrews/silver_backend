from rest_framework import serializers

from product.models import Product


class ProductAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'seller',
            'end_at',
        )
