from rest_framework import serializers

from club.models import UserClub


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
