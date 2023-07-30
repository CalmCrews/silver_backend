from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_url_kwarg = 'order_id'

    def perform_destroy(self, instance):
        if instance.status == 'PREPAYMENT':
            instance.status = 'CANCEL'
            instance.save()

    def put(self, request, *args, **kwargs):
        product = self.get_product()
        order = self.get_object()

        if order.status != 'PREPAYMENT':
            return Response({'message': '해당 주문을 변경할 수 없습니다'}, status=400)

        if product.is_sellable:
            if product.current_buyable_quantity < int(request.data.get('quantity')):
                return Response({'message': '해당 상품의 재고가 부족합니다'}, status=400)
            return super().put(request, *args, **kwargs)
        return Response({'message': '해당 상품을 구매할 수 없습니다'}, status=400)

    def patch(self, request, *args, **kwargs):
        product = self.get_product()
        order = self.get_object()

        if order.status != 'PREPAYMENT':
            return Response({'message': '해당 주문을 변경할 수 없습니다'}, status=400)

        if product.is_sellable:
            if product.current_buyable_quantity < int(request.data.get('quantity')):
                return Response({'message': '해당 상품의 재고가 부족합니다'}, status=400)
            return super().put(request, *args, **kwargs)
        return Response({'message': '해당 상품을 구매할 수 없습니다'}, status=400)

    def delete(self, request, *args, **kwargs):
        order = self.get_object()
        if order.status == 'FINALPAYMENT':
            return Response({'message': '거래가 종료된 주문은 취소할 수 없습니다'}, status=400)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
