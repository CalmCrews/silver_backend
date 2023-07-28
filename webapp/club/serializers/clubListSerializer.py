from club.models import Club, ClubTag
from rest_framework import serializers



class ClubTagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'

class ClubListSerializer(serializers.ModelSerializer):
    club_tags = ClubTagListSerializer

    class Meta:
        model = Club
        fields = (
            'name',
            'level',
        )