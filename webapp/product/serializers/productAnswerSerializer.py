from rest_framework import serializers

from product.models import ProductAnswer


class ProductAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAnswer
        fields = '__all__'
