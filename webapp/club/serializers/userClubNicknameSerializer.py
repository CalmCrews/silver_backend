from rest_framework import serializers

from club.models import UserClub

class UserClubNicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClub
        fields = '__all__'
        read_only_fields = (
            'user',
            'club',
            'is_owner',
        )
