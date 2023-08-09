from rest_framework.generics import ListAPIView, get_object_or_404

from club.models import ClubProduct, Club
from club.serializers import ClubProductAbstractSerializer


class ClubProductListAPIView(ListAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductAbstractSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(club=self.get_club())
        return queryset

    def get_club(self):
        club_id = self.kwargs.get('club_id')
        club = get_object_or_404(Club, id=club_id)
        return club
