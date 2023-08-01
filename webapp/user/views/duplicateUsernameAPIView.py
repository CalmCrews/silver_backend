from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User


class DuplicateUserNameAPIView(APIView):

    def post(self, request):
        user_id = request.data.get('userId')
        if user_id is None:
            return Response({'message': '아이디를 입력해주세요.'}, status=400)
        if User.objects.filter(username=user_id).exists():
            return Response({'message': '존재하는 이름입니다.'}, status=400)
        return Response({'message': '가능한 아이디입니다.'}, status=200)
