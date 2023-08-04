from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from club.models import ClubTag
from club.serializers import ClubTagUpdateSerializer


class ClubTagUpadateAPIView(UpdateAPIView):
    queryset = ClubTag.objects.all()
    serializer_class = ClubTagUpdateSerializer
    lookup_url_kwarg = 'club_id'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            raise PermissionDenied(detail='로그인 후 이용해 주세요.')
        club_id = self.kwargs.get('club_id')
        qureyset = ClubTag.objects.filter(club__id=club_id)
        if not qureyset:
            return Response({'message': '해당 모임은 존재하지 않습니다.'})
        return qureyset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
