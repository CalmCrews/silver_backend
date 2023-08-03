from club.models import UserClub
from rest_framework import serializers


class UserClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClub
        fields = '__all__'
