from rest_framework import serializers

from club.models import Club


class ClubRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'intro',
            'level',
            'tag',
            'code',
        )

        read_only_fields = (
            'level',
            'tag',
            'code',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tag_value = representation.get('tag', None)

        if tag_value:
            representation['tag'] = tag_value.split()

        return representation