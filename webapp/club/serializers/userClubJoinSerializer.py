from rest_framework import serializers

from club.models import UserClub
from club.serializers import ClubSerializer
from user.serializers import UserSerializer


class UserClubJoinSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    club = ClubSerializer(read_only=True)
    club_code = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserClub
        fields = (
            'club',
            'user',
            'is_owner',
            'nickname',
            'club_code',
        )

        read_only_fields = (
            'club',
            'user',
            'is_owner',
            'nickname',
        )


    def to_internal_value(self, data):
        nickname = data.get('nickname', None)
        if nickname == "null":
            data['nickname'] = None
        return super().to_internal_value(data)

