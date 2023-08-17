from requests import Response
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from club.models import ClubProduct, UserClub
from club.serializers import ClubProductAbstractSerializer


class AllClubProductListAPIView(ListAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductAbstractSerializer

    def get_queryset(self):
        user_clubs = UserClub.objects.filter(user=self.request.user)
        club_ids = [user_club.club.pk for user_club in user_clubs]
        queryset = self.queryset.filter(club__id__in=club_ids).order_by('product__end_at')
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
