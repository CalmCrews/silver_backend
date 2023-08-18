from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from club.models import ClubProduct, UserClub
from club.serializers import ClubProductSerializer
from order.models import Order


class ClubProductRetrieveAPIView(RetrieveAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductSerializer
    lookup_url_kwarg = 'club_product_id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        is_my_club_product = UserClub.objects.filter(club=instance.club, user=request.user).exists()
        if is_my_club_product == False:
            res = {
                'message': '모임에 추가된 상품이 아닙니다.',
                'product_id': instance.product.id,
                'product_name': instance.product.name,
            }
            return Response(res)
        is_not_buyable = Order.objects.filter(user=self.request.user, product=instance).exists()
        serializer = self.get_serializer(instance)
        participant_count = instance.participant_count
        quantity_sum = instance.quantity_sum
        current_price = instance.current_price
        discount_rate = instance.discount_rate
        achievement_rate = instance.achievement_rate

        # Create a dictionary with your additional data
        extra_data = {
            'participant_count': participant_count,
            'quantity_sum': quantity_sum,
            'current_price': current_price,
            'discount_rate': discount_rate,
            'achievement_rate': achievement_rate,
            'is_not_buyable': is_not_buyable,
        }

        # Create a new dictionary for the response data
        serializer.data['product'].update(extra_data)

        return Response(serializer.data)
