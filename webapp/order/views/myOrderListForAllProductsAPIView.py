from rest_framework.generics import ListAPIView

from order.models import Order
from order.serializers.orderSerializer import OrderSerializer


class MyOrderListForAllProductsAPIView(ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
