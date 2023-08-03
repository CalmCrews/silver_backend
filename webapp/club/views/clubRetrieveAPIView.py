from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from club.models import Club
from club.serializers import ClubRetrieveSerializer

class ClubRetrieveAPIView(RetrieveUpdateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubRetrieveSerializer
    lookup_url_kwarg = 'club_id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        club = instance.club

        name = request.data.get('club_name')
        intro = request.data.get('club_intro')

        if name:
            club.name = name
        if intro:
            club.intro = intro
        club.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

