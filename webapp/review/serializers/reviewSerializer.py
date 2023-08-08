from rest_framework import serializers

from product.serializers import ProductAbstractSerializer
from review.models import Review
from user.serializers import UserSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductAbstractSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'order',
            'user',
            'product',
            'rating',
            'content',
            'created_at',
        )

        read_only_fields = (
            'id',
            'order',
            'created_at',
        )
