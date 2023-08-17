from rest_framework import serializers

from product.models import Product
from seller.serializers.sellerSerializer import SellerSerializer


class ProductSerializer(serializers.ModelSerializer):
    is_sellable = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'intro',
            'price',
            'category',
            'thumbnail',
            'video',
            'seller',
            'end_at',
            'is_sellable',
            'review_score',
        )

    def get_is_sellable(self, obj):
        return obj.time_passed

    def get_seller(self, obj):
        seller_data = SellerSerializer(obj.seller).data if obj.seller else None
        return seller_data
