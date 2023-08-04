from rest_framework import serializers

from club.models import ClubTag


class ClubTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'
