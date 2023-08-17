from functools import reduce
from operator import or_

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from club.models import ClubProduct
from club.serializers import ClubProductAbstractSerializer
from order.models import Order


class UserClubProductListAPIView(ListAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductAbstractSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(self.get_product())
        current_datetime = timezone.now()
        queryset = queryset.filter(product__end_at__gte=current_datetime)
        queryset = queryset.order_by('product__end_at')[:3]
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        updated_data = []

        for query, serialized_data in zip(queryset, serializer.data):
            participant_count = query.participant_count
            quantity_sum = query.quantity_sum
            current_price = query.current_price
            discount_rate = query.discount_rate
            achievement_rate = query.achievement_rate

            extra_data = {
                'participant_count': participant_count,
                'quantity_sum': quantity_sum,
                'current_price': current_price,
                'discount_rate': discount_rate,
                'achievement_rate': achievement_rate,
            }

            serialized_data['product'].update(extra_data)
            updated_data.append(serialized_data)
        return Response(updated_data)

    def get_product(self):
        user_orders = Order.objects.filter(user=self.request.user)
        user_product = []
        for user_order in user_orders:
            if user_order.status == 'PREPAYMENT':
                user_product.append(user_order.product)
        if not user_product:
            return Q(pk__in=[])
        product = reduce(or_, [Q(pk=product.pk) for product in user_product])
        return product
