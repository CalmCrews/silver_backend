from rest_framework import serializers

from club.models import ClubProduct
from product.serializers import ProductAbstractSerializer


class ClubProductAbstractSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
        )
        read_only_fields = (
            'id',
            'product',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
        )
