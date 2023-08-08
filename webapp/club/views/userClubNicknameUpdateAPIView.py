from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import UserClub
from club.serializers import UserClubNicknameSerializer


class UserClubNicknameUpdateAPIView(UpdateAPIView):
    queryset = UserClub.objects.all()
    serializer_class = UserClubNicknameSerializer
    lookup_url_kwarg = 'club_id'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise PermissionDenied(detail='로그인 후 이용해 주세요.')
        club_id = self.kwargs.get('club_id')
        queryset = UserClub.objects.filter(user=self.request.user, club__id=club_id)
        if not queryset:
            return Response({'message': '참여하고 있는 모임이 아닙니다.'})
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_update(self, serializer):
        instance = self.get_object()
        nickname = self.request.data.get('nickname')
        if nickname is not None:
            instance.nickname = nickname
            instance.save()
        else:
            Response({'message': '닉네임을 입력해주세요.'})
