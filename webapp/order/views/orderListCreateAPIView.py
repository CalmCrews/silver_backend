from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from club.models import ClubProduct, Club
from order.models import Order
from order.serializers import OrderSerializer
from product.models import Product


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(user=self.request.user, product=self.get_club_product())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        club_product = self.get_club_product()
        serializer.save(
            user=self.request.user,
            product=club_product,
            initial_price=club_product.product.price,
            status='PREPAYMENT',
        )

        if serializer.instance.final_price is None:
            serializer.instance.final_price = club_product.product.price
            serializer.save()
        user = self.request.user
        if user.balance < serializer.instance.total_initial_price:
            return "failed"
        user.balance -= serializer.instance.total_initial_price
        user.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.perform_create(serializer) == "failed":
            serializer.instance.delete()
            return Response({'message': '잔액이 부족합니다'}, status=400)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def post(self, request, *args, **kwargs):
        club_product = self.get_club_product()
        product = club_product.product
        if product.time_passed:
            return Response({'message': '해당 상품의 판매기간이 아닙니다.'}, status=400)
        return self.create(request, *args, **kwargs)

    def get_club_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        club_id = self.kwargs.get('club_id')
        club = get_object_or_404(Club, id=club_id)
        club_product = ClubProduct.objects.filter(product=product, club=club)
        if not club_product.exists():
            return NotFound("해당 모임에 등록된 상품이 아닙니다.")
        return club_product.first()
