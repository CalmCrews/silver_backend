from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from club.models import ClubProduct
from club.serializers import ClubProductSerializer
from notification.models import UserNotification
from notification.serializers import NotificationSerializer


class UserNotificationRetrieveSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()
    club_product = serializers.SerializerMethodField()

    class Meta:
        model = UserNotification
        fields = (
            'notification',
            'receiver',
            'is_read',
            'club_product',
        )

    def get_club_product(self, obj):
        club_product_id = obj.notification.clubproduct
        club_product = get_object_or_404(ClubProduct, id=club_product_id)
        serializer = ClubProductSerializer(club_product).data
        participant_count = club_product.participant_count
        quantity_sum = club_product.quantity_sum
        current_price = club_product.current_price
        discount_rate = club_product.discount_rate
        achievement_rate = club_product.achievement_rate

        extra_data = {
            'participant_count': participant_count,
            'quantity_sum': quantity_sum,
            'current_price': current_price,
            'discount_rate': discount_rate,
            'achievement_rate': achievement_rate,
        }
        serializer['product'].update(extra_data)
        return serializer
