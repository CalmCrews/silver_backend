from rest_framework import status
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.response import Response

from club.models import Club, UserClub
from club.serializers import UserClubSerializer, UserClubJoinSerializer, ClubSerializer
from user.serializers import UserSerializer


class UserClubJoinCreateAPIView(CreateAPIView):
    queryset = UserClub.objects.all()
    serializer_class = UserClubJoinSerializer

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'message': '로그인 후 이용해 주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = self.perform_create(serializer)
        user = UserSerializer(self.request.user).data
        club_code = self.request.data.get('club_code')
        club = get_object_or_404(Club, code=club_code)
        club = ClubSerializer(club).data
        if serializer.data.get('message'):
            headers = self.get_success_headers(serializer)
            return Response(serializer.data, headers=headers)
        res = {
            'user': user,
            'club': club,
            'data': serializer.data,
        }
        headers = self.get_success_headers(serializer)
        return Response(res, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        club_code = self.request.data.get('club_code')
        if not club_code:
            return Response({'message': '클럽 코드를 입력해 주세요.'}, status=status.HTTP_400_BAD_REQUEST)

        club = get_object_or_404(Club, code=club_code)
        user_club_data = {
            'club': club.id,
            'user': self.request.user.id,
            'is_owner': False,
        }

        already_club = UserClub.objects.filter(user=self.request.user.id, club=club.id)
        if not already_club:
            user_club_serializer = UserClubSerializer(data=user_club_data)
            user_club_serializer.is_valid(raise_exception=True)
            user_club_serializer.save()
            return user_club_serializer
        else:
            return Response({'message': '이미 참여중인 모임입니다.', 'club': club.id}, status=status.HTTP_400_BAD_REQUEST)
