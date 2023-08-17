from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from service.models import ServiceQnA
from service.serializers import ServiceQnASerializer


class ServiceQnAListAPIView(ListAPIView):
    queryset = ServiceQnA.objects.all()
    serializer_class = ServiceQnASerializer

    def get_queryset(self):
        queryset = ServiceQnA.objects.filter(user=self.request.user)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # TODO: 프론트 요청에 맞추어 user 및 기타 정보 추가
        serializer = self.get_serializer(queryset, many=True)
        user = str(self.request.user)
        res = {
            'user': user,
            'data': serializer.data
        }

        return Response(res)
