from club.models import ClubTag
from rest_framework import serializers


class ClubSerializer(serializers.ModelSerializer):
    club_name = serializers.SerializerMethodField()
    club_level = serializers.SerializerMethodField()
    club_code = serializers.SerializerMethodField()
    club_intro = serializers.SerializerMethodField()

    class Meta:
        model = ClubTag
        fields = (
            'id',
            'club_name',
            'club_level',
            'clubtag',
            'club_code',
            'club_intro',
        )
    def get_club_name(self, obj):
        return obj.club.name
    def get_club_level(self, obj):
        return obj.club.level
    def get_club_code(self, obj):
        return obj.club.code
    def get_club_intro(self, obj):
        return obj.club.intro
