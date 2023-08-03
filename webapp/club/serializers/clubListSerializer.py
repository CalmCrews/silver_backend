# club/serializers.py
from rest_framework import serializers
from club.models import Club, ClubTag
from club.serializers.clubTagSerializer import ClubTagSerializer


class ClubListSerializer(serializers.ModelSerializer):
    club_tags = serializers.SerializerMethodField()
    class Meta:
        model = Club
        fields = [
            'name',
            'level',
            'club_tags',
        ]

    def get_club_tags(self, obj):
        club_tags = ClubTag.objects.filter(club=obj)
        return [tag.club_tag for tag in club_tags]




