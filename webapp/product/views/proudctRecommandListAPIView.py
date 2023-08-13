import random
from time import timezone

from django.db.models import Q
from django.utils import timezone
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import UserClub, Club
from product.models import Product
from product.serializers import ProductListSerializer


class ProductRecommandListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        current_datetime = timezone.now()
        queryset = queryset.filter(Q(end_at__gte=current_datetime))
        userclubs = list(UserClub.objects.filter(user=self.request.user))
        clubs = []
        first_club = userclubs[0].club
        for userclub in userclubs:
            clubs.append({'id': userclub.club.id, 'name': userclub.club.name})
        club_id = self.request.GET.get('clubs')

        if club_id:
            club_tags = get_object_or_404(Club, id=club_id).tag.split()
        else:
            club_tags = first_club.tag.split()
        tag_conditions = Q()
        for tag in club_tags:
            tag_conditions |= Q(tag__contains=tag)
        queryset = queryset.filter(tag_conditions)
        exclude_club_products = Q()
        for club in clubs:
            exclude_club_products |= Q(clubproduct__club=club['id'])
        queryset = queryset.exclude(exclude_club_products)

        if queryset:
            random_products = random.sample(list(queryset), min(3, len(queryset)))
            serializer = self.get_serializer(random_products, many=True)
            res = {
                'product': serializer.data,
                'clubs': clubs
            }
            return Response(res)
        else:
            return Response({'product': [], 'clubs': clubs})
