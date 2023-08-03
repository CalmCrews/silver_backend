from rest_framework import serializers

from club.models import UserClub


class UserClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClub
        fields = '__all__'
