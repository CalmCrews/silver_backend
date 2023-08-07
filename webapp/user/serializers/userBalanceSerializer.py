from rest_framework import serializers

from user.models import User


class UserBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile_image',
            'balance',
        ]

        read_only_fields = [
            'id',
            'username',
            'profile_image',
        ]
