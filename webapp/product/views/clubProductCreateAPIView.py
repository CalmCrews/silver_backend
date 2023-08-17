from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import ClubProduct, UserClub, Club
from club.serializers import ClubProductSerializer
from notification.models import UserNotification, Notification
from notification.serializers import NotificationSerializer
from product.models import Product


class ClubProductCreateAPIView(CreateAPIView):
    queryset = ClubProduct.objects.all()
    serializer_class = ClubProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        club = self.request.GET.get('club')
        validate_if_my_club = UserClub.objects.filter(user=self.request.user, club=club)
        if not validate_if_my_club.exists():
            return Response({'message': '본인의 모임에만 상품을 추가할 수 있습니다.'}, status=400)
        club = get_object_or_404(Club, id=club)
        self.perform_create(serializer, club)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer, club):
        product = self.get_product()
        serializer.save(product=product, club=club)
        club_product = serializer.data.get('id')
        notification_data = {
            'sender': self.request.user.id,
            'title': "공동구매 초대장을 받았어요. 공동구매에 참여해볼까요?",
            'message': f"{club.name} 모임원이 신청한 함께구매 상품을 확인해보세요!",
            'category': "GROUPBUY",
            'clubproduct': f"{club_product}"
        }
        print(notification_data)
        notification_serializer = NotificationSerializer(data=notification_data)
        if notification_serializer.is_valid():
            notification_serializer.save()
        notification_id = notification_serializer.data.get('id')
        notification = Notification.objects.get(id=notification_id)
        userclubs = UserClub.objects.filter(club=club)
        user_ids = [userclub.user for userclub in userclubs]
        user_ids.remove(self.request.user)

        instances_to_create = []
        for user_id in user_ids:
            instances_to_create.append(UserNotification(notification=notification, receiver=user_id))
        UserNotification.objects.bulk_create(instances_to_create)

    def get_product(self):
        product_id = self.kwargs.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        return product
