from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile_image',
            'nickname',
            'password',
            'balance',
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user
