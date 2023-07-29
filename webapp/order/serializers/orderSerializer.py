from rest_framework import serializers

from order.models import Order
from product.serializers import ProductAbstractSerializer


class OrderSerializer(serializers.ModelSerializer):
    total_initial_price = serializers.SerializerMethodField()
    total_final_price = serializers.SerializerMethodField()
    product = ProductAbstractSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            'product',
            'quantity',
            'status',
            'initial_price',
            'final_price',
            'total_initial_price',
            'total_final_price',
        )

        read_only_fields = (
            'id',
            'user',
            'product',
            'status',
            'initial_price',
            'final_price',
            'total_initial_price',
            'total_final_price',
        )

    def get_total_initial_price(self, obj):
        return obj.total_initial_price

    def get_total_final_price(self, obj):
        return obj.total_final_price
