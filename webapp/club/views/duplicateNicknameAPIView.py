from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from club.models import UserClub


class DuplicateNickNameAPIView(APIView):

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({'message': '로그인 후 이용해 주세요.'}, status=400)
        club_id = self.kwargs.get('club_id')
        user_clubs = UserClub.objects.filter(club=club_id)
        if user_clubs is None:
            return Response({'message': '참여하고 있는 모임이 아닙니다.'}, status=400)
        nickname = self.request.data.get('nickname')
        if user_clubs.exists() and nickname:
            for user_club in user_clubs:
                if user_club.nickname == nickname:
                    return Response({'message': '존재하는 이름입니다.'}, status=400)
            return Response({'message': '가능한 닉네임입니다.'}, status=200)
        return Response({'message': '닉네임을 입력해주세요.'}, status=400)
