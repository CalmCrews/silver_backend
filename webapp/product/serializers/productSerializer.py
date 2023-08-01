from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_sellable = serializers.SerializerMethodField()
    current_buyable_quantity = serializers.SerializerMethodField()

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
            'total',
            'end_at',
            'is_sellable',
            'current_buyable_quantity',
        )

    def get_is_sellable(self, obj):
        return obj.is_sellable

    def get_current_buyable_quantity(self, obj):
        return obj.current_buyable_quantity
