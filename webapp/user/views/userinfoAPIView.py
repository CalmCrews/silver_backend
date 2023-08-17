from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer


class UserinfoAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        return Response({'message': '로그인 후 이용해주세요.'})
