from rest_framework import serializers

from product.models import ProductQuestion


class ProductQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductQuestion
        fields = '__all__'
