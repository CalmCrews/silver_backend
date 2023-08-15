from functools import reduce
from operator import or_

from django.db.models import Q
from rest_framework.generics import ListAPIView

from club.models import ClubProduct
from club.serializers import ClubProductAbstractSerializer
from order.models import Order


class UserClubProductListAPIView(ListAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductAbstractSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(self.get_product()).order_by('product__end_at')[:3]
        return queryset

    def get_product(self):
        user_orders = Order.objects.filter(user=self.request.user)
        user_product = []
        for user_order in user_orders:
            if user_order.status == 'PREPAYMENT':
                user_product.append(user_order.product)

        product = reduce(or_, [Q(pk=product.pk) for product in user_product])
        return product
