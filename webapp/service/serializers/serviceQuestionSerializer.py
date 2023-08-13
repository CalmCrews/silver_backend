from rest_framework import serializers

from service.models import ServiceQuestion


class ServiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceQuestion
        fields = '__all__'
