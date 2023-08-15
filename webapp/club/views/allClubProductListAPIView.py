from rest_framework.generics import ListAPIView

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
