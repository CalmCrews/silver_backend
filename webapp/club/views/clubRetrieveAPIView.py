from django.shortcuts import render
from requests import Response
from rest_framework.generics import RetrieveAPIView

from club.models import ClubTag
from club.serializers import ClubSerializer


class ClubRetrieveAPIView(RetrieveAPIView):
    queryset = ClubTag.objects.all()
    serializer_class = ClubSerializer
    lookup_url_kwarg = 'club_id'
