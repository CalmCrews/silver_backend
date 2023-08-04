# club/serializers.py
from rest_framework import serializers

from club.models import Club, ClubTag


class ClubRetrieveSerializer(serializers.ModelSerializer):
    club_tag = serializers.SerializerMethodField()
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'intro',
            'level',
            'club_tag',
        )

        read_only_fields = (
            'level',
        )

    def get_club_tag(self, obj):
        club_tag = ClubTag.objects.get(club=obj)
        return club_tag.club_tag




