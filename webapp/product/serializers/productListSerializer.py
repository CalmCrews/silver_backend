from rest_framework import serializers

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField()
    review_score = serializers.SerializerMethodField()

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
            'review_score',
        )

    def get_seller(self, obj):
        return obj.seller.name

    def get_review_score(self, obj):
        return obj.review_score
