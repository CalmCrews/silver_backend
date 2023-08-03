from rest_framework.generics import UpdateAPIView

from club.models import UserClub
from club.serializers import UserClubSerializer


class UserClubNicknameUpdateAPIView(UpdateAPIView):
    queryset = UserClub.objects.all()
    serializer_class = UserClubSerializer
    lookup_url_kwarg = 'club_id'

    def get_queryset(self):
        club_id = self.kwargs.get('club_id')
        qureyset = UserClub.objects.filter(user=self.request.user, club__id=club_id)
        return qureyset