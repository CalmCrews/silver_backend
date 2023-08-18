from rest_framework import serializers

from club.models import ClubProduct
from club.serializers import ClubSerializer
from order.models import Order
from product.serializers import ProductAbstractSerializer
from user.serializers import UserNicknameSerializer
from seller.serializers import SellerSerializer


class ClubProductSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)
    club = ClubSerializer(read_only=True)
    participants = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'seller',
            'club',
            'participants',
        )
        read_only_fields = (
            'id',
            'product',
            'participants',
            'seller',
        )

    def get_participants(self, obj):
        orders = Order.objects.filter(product=obj)
        participants = []
        for order in orders:
            participants.append(UserNicknameSerializer(order.user).data)
        return participants

    def get_seller(self, obj):
        seller = obj.product.seller
        return SellerSerializer(seller).data
