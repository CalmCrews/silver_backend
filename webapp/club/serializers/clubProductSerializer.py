from rest_framework import serializers

from club.models import ClubProduct
from club.serializers import ClubSerializer
from product.serializers import ProductAbstractSerializer
from seller.serializers import SellerSerializer


class ClubProductSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)
    club = ClubSerializer(read_only=True)
    seller = serializers.SerializerMethodField()

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'seller',
            'club',
        )
        read_only_fields = (
            'id',
            'product',
            'seller',
        )

    def get_seller(self, obj):
        seller = obj.product.seller
        return SellerSerializer(seller).data
