from rest_framework import serializers

from service.models import ServiceAnswer


class ServiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnswer
        fields = '__all__'
