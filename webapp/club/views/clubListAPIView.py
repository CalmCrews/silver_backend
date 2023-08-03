from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from club.models import ClubTag, UserClub
from club.serializers import ClubListSerializer

class ClubListAPIView(ListCreateAPIView):
    serializer_class = ClubListSerializer

    def get_queryset(self):
        # Retrieve the UserClub queryset with related Club and ClubTag data
        userclubs = UserClub.objects.filter(user=self.request.user).select_related('club__club_tags')
        clubs = [userclub.club for userclub in userclubs]
        return clubs
