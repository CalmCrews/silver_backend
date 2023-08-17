from rest_framework.generics import RetrieveAPIView

from service.models import ServiceQnA
from service.serializers import ServiceQnASerializer


class ServiceQnARetrieveAPIView(RetrieveAPIView):
    queryset = ServiceQnA.objects.all()
    serializer_class = ServiceQnASerializer
    lookup_url_kwarg = 'qna_id'

    def get_queryset(self):
        queryset = ServiceQnA.objects.filter(user=self.request.user)
        return queryset
