from rest_framework import serializers

from club.models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        tag_value = representation.get('tag', None)

        if tag_value:
            representation['tag'] = tag_value.split()

        return representation