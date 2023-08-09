from rest_framework import serializers

from club.models import Club


class ClubListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'intro',
            'level',
            'tag',
        )

        read_only_fields = (
            'level',
        )
