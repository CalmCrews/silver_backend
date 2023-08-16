from rest_framework import serializers

from club.models import ClubProduct
from club.serializers import ClubProductSerializer
from notification.models import UserNotification
from notification.serializers import NotificationSerializer


class UserNotificationRetrieveSerializer(serializers.ModelSerializer):
    notification = NotificationSerializer()
    clubproduct = serializers.SerializerMethodField()

    class Meta:
        model = UserNotification
        fields = (
            'notification',
            'receiver',
            'is_read',
            'clubproduct',
        )

    def get_clubproduct(self, obj):
        club_product_id = obj.notification.clubproduct
        print(club_product_id)
        club_product = ClubProduct.objects.get(id=club_product_id)
        print(club_product)
        return ClubProductSerializer(club_product).data
