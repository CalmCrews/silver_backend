from rest_framework import serializers

from club.models import ClubProduct


class ClubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubProduct
        fields = (
            'id',
            'product',
            'club',
        )
        read_only_fields = (
            'id',
            'product',
        )
