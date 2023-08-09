from rest_framework import serializers

from club.models import ClubProduct
from club.serializers import ClubSerializer
from product.serializers import ProductAbstractSerializer


class ClubProductSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)
    club = ClubSerializer(read_only=True)

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'club',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
            'achievement_rate',
        )
        read_only_fields = (
            'id',
            'product',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
            'achievement_rate',
        )
