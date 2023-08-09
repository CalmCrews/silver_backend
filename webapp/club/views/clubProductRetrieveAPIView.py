from rest_framework.generics import RetrieveAPIView

from club.models import ClubProduct
from club.serializers import ClubProductSerializer


class ClubProductRetrieveAPIView(RetrieveAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductSerializer
    lookup_url_kwarg = 'club_product_id'
