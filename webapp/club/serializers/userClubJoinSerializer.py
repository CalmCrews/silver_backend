from rest_framework import serializers

from club.models import UserClub
from club.serializers import ClubSerializer
from user.serializers import UserSerializer


class UserClubJoinSerializer(serializers.ModelSerializer):
    club_code = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserClub
        fields = (
            'club',
            'user',
            'is_owner',
            'club_code',
        )

        read_only_fields = (
            'club',
            'user',
            'is_owner',
        )
