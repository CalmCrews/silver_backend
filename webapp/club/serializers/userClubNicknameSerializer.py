from rest_framework import serializers

from club.models import UserClub
from user.serializers import UserSerializer


class UserClubNicknameSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    class Meta:
        model = UserClub
        fields = (
            'club',
            'is_owner',
            'user_profile',
            'nickname',
        )

        read_only_fields = (
            'club',
            'is_owner',
            'user_profile',
        )

    def get_user_profile(self, obj):
        user_profile_serializer = UserSerializer(instance=self.context['request'].user)
        return user_profile_serializer.data
