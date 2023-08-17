from rest_framework import serializers

from club.models import ClubProduct
from order.models import Order
from product.serializers import ProductAbstractSerializer
from user.serializers import UserNicknameSerializer


class ClubProductAbstractSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)
    participants = serializers.SerializerMethodField()

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'participants',
        )
        read_only_fields = (
            'id',
            'product',
            'participants',
        )

    def get_participants(self, obj):
        orders = Order.objects.filter(product=obj)
        participants = []
        for order in orders:
            participants.append(UserNicknameSerializer(order.user).data)
        return participants
