from rest_framework import serializers

from club.models import Club, UserClub
from user.serializers import UserNicknameSerializer


class ClubRetrieveSerializer(serializers.ModelSerializer):
    number_of_members = serializers.SerializerMethodField()
    members = serializers.SerializerMethodField()

    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'intro',
            'level',
            'tag',
            'code',
            'number_of_members',
            'members',
        )

        read_only_fields = (
            'level',
            'tag',
            'code',
            'number_of_members',
            'members',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tag_value = representation.get('tag', None)

        if tag_value:
            representation['tag'] = tag_value.split()

        return representation

    def get_number_of_members(self, obj):
        member_count = UserClub.objects.filter(club=obj).count()
        return member_count

    def get_members(self, obj):
        clubs = UserClub.objects.filter(club=obj)
        club_member = []
        for club in clubs:
            club_member.append(UserNicknameSerializer(club.user).data)
        return club_member
