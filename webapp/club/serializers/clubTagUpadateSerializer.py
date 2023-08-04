from rest_framework import serializers

from club.models import ClubTag
from club.serializers import ClubSerializer


class ClubTagUpdateSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    class Meta:
        model = ClubTag
        fields = (
            'club',
            'gathering',
            'daily',
            'economic',
            'biology',
            'culture',
            'study',
            'life',
            'sports',
            'religion',
            'health',
            'etc',
            'club_tag'
        )

        read_only_fields = (
            'club',
        )

