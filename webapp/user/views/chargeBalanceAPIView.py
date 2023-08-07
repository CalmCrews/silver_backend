from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from user.models import User
from user.permissions import IsUserCurrentUser
from user.serializers import UserBalanceSerializer


class ChargeBalanceAPIView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserBalanceSerializer
    lookup_url_kwarg = 'user_id'
    permission_classes = [IsUserCurrentUser, ]

    def update(self, request, *args, **kwargs):
        balance = request.data.get('balance')
        instance = request.user
        instance.balance += int(balance)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
