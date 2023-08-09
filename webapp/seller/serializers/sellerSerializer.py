from rest_framework import serializers

from seller.models import Seller


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'name',
            'represent',
            'business_image',
            'business_number',
            'center_number',
            'email',
        )
