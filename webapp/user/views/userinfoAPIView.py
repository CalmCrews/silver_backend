from rest_framework.views import APIView
from rest_framework.response import Response

from user.serializers import UserNicknameSerializer


class UserinfoAPIView(APIView):
    def get(self, request):
        serializer = UserNicknameSerializer(request.user)
        return Response(serializer.data)
