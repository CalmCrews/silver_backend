from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response

from club.models import Club, UserClub
from club.serializers import ClubRetrieveSerializer


class ClubRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubRetrieveSerializer
    lookup_url_kwarg = 'club_id'

    def retrieve(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'message': '로그인 후 이용해 주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        res = {
            'club': serializer.data,
            'nickname': self.request.user.nickname,
        }
        return Response(res)
