from club.models import ClubTag
from rest_framework import serializers


class ClubTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubTag
        fields = '__all__'
