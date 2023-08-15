from rest_framework import serializers

from club.models import ClubProduct
from order.models import Order
from product.serializers import ProductAbstractSerializer


class ClubProductAbstractSerializer(serializers.ModelSerializer):
    product = ProductAbstractSerializer(read_only=True)
    participants = serializers.SerializerMethodField()

    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
            'achievement_rate',
            'participants',
        )
        read_only_fields = (
            'id',
            'product',
            'participant_count',
            'quantity_sum',
            'current_price',
            'discount_rate',
            'achievement_rate',
            'participants',
        )

    def get_participants(self, obj):
        orders = Order.objects.filter(product=obj)
        participants = []
        for order in orders:
            if order.user.profile_image:
                participants.append({
                    'id': order.user.id,
                    'nickname': order.user.nickname,
                    'profile_image': order.user.profile_image,
                })
            else:
                participants.append({
                    'id': order.user.id,
                    'nickname': order.user.nickname,
                    'profile_image': 'null',
                })

        return participants
