from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from club.models import ClubTag, UserClub
from club.serializers import ClubListSerializer, ClubTagSerializer, UserClubSerializer

class ClubListAPIView(ListCreateAPIView):
    serializer_class = ClubListSerializer

    def get_queryset(self):
        userclubs = UserClub.objects.filter(user=self.request.user).select_related('club__club_tags')
        clubs = [userclub.club for userclub in userclubs]
        return clubs

    def perform_create(self, serializer):
        club_instance = serializer.save()

        user_club_data = {
            'user': self.request.user.id,
            'club': club_instance.id,
            'nickname': self.request.data.get('nickname')
        }

        user_club_serializer = UserClubSerializer(data=user_club_data)
        user_club_serializer.is_valid(raise_exception=True)
        user_club_serializer.save()

        club_tag_data = self.request.data.get('club_tag')
        if club_tag_data:
            club_tag_data['club'] = club_instance.id
            club_tag_serializer = ClubTagSerializer(data=club_tag_data)
            club_tag_serializer.is_valid(raise_exception=True)
            club_tag_serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
