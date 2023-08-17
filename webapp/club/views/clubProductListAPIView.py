from django.utils import timezone
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import ClubProduct, Club
from club.serializers import ClubProductAbstractSerializer


class ClubProductListAPIView(ListAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductAbstractSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(club=self.get_club())
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        current_datetime = timezone.now()
        queryset = queryset.filter(product__end_at__gte=current_datetime)
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

    def get_club(self):
        club_id = self.kwargs.get('club_id')
        club = get_object_or_404(Club, id=club_id)
        return club
