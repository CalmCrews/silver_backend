from rest_framework import serializers

from user.models import User


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password'
        ]

        read_only_fields = [
            'name',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
