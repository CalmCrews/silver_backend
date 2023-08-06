from rest_framework import status
from rest_framework.generics import get_object_or_404, CreateAPIView
from rest_framework.response import Response

from club.models import Club, UserClub
from club.serializers import UserClubSerializer, UserClubJoinSerializer


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

        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
            serializer = UserClubSerializer(data=user_club_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer
        else:
            return Response({'message': '이미 참가중인 모임입니다.'}, status=status.HTTP_400_BAD_REQUEST)
