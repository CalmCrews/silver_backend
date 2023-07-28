from django.shortcuts import render
from requests import Response
from rest_framework.generics import ListAPIView

from club.models import ClubTag
from club.serializers import ClubTagListSerializer


class ClubListAPIView(ListAPIView):
    queryset = ClubTag.objects.all()
    serializer_class = ClubTagListSerializer
