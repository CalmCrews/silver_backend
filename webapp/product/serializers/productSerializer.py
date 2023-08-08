from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_sellable = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'intro',
            'price',
            'category',
            'thumbnail',
            'video',
            'seller',
            'end_at',
            'is_sellable',
        )

    def get_is_sellable(self, obj):
        return obj.time_passed
