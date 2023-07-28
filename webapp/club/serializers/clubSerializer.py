from club.models import Club, ClubTag
from rest_framework import serializers


class ClubTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    club_tags = ClubTagSerializer(many=True)  # Assuming you have a ForeignKey from Club to ClubTag

    class Meta:
        model = Club
        fields = '__all__'