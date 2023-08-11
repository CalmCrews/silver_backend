from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from club.models import ClubProduct, Club
from product.models import Product


class ClubProductRegisterationAPIView(APIView):
    def post(self):
        club_id = self.kwargs.get('club_id')
        club_product_id = self.kwargs.get('club_product_id')
        club_product = get_object_or_404(ClubProduct, id=club_product_id)
        club = get_object_or_404(Club, id=club_id)
        product = get_object_or_404(Product, id=club_product.product.id)
        if product.time_passed == True:
            if club_product.final_achievement_rate == 100:
                club_product.registration = True
                club_product.save()
                club.achievement += 1
                club.save()
                return Response({'message':'달성률이 100%가 되었습니다.'}, status=200)
            else:
                return Response({'message':'달성률 100% 실패'}, status=400)
        else:
            return Response({'message':'공구기간이 지나지 않아 반영되지 않았습니다'}, status=400)


