# club/serializers.py
from rest_framework import serializers
from club.models import ClubTag

class ClubTagListSerializer(serializers.ModelSerializer):
    club_name = serializers.SerializerMethodField()
    club_level = serializers.SerializerMethodField()
    class Meta:
        model = ClubTag
        fields = (
            'id',
            'club_name',
            'club_level',
            'clubtag',
        )
    def get_club_name(self, obj):
        return obj.club.name
    def get_club_level(self, obj):
        return obj.club.level




