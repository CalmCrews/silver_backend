from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import ClubProduct, UserClub
from club.serializers import ClubProductSerializer
from product.models import Product


class ClubProductCreateAPIView(CreateAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        club = serializer.validated_data.get('club')
        validate_if_my_club = UserClub.objects.filter(user=self.request.user, club=club)
        if not validate_if_my_club.exists():
            return Response({'message': '본인의 모임에만 상품을 추가할 수 있습니다.'}, status=400)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        product = self.get_product()
        serializer.save(product=product)

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
