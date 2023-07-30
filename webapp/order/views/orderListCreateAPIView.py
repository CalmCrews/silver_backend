from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user, product=self.get_product())
        return queryset

    def perform_create(self, serializer):
        product = self.get_product()
        serializer.save(
            user=self.request.user,
            product=product,
            initial_price=product.price,
            status='PREPAYMENT'
        )
        if serializer.instance.final_price is None:
            serializer.instance.final_price = product.price
            serializer.save()

    def post(self, request, *args, **kwargs):
        product = self.get_product()
        if product.is_sellable:
            if product.current_buyable_quantity < int(request.data.get('quantity')):
                return Response({'message': '해당 상품의 재고가 부족합니다'}, status=400)
            return super().post(request, *args, **kwargs)
        return Response({'message': '해당 상품을 구매할 수 없습니다'}, status=400)

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
