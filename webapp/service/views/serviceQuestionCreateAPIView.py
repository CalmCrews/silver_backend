from rest_framework.generics import CreateAPIView

from service.models import ServiceQuestion, ServiceQnA
from service.serializers import ServiceQuestionSerializer


class ServiceQuestionCreateAPIView(CreateAPIView):
    queryset = ServiceQuestion.objects.all()
    serializer_class = ServiceQuestionSerializer

    def perform_create(self, serializer):
        serializer.save()
        ServiceQnA.objects.create(
            user=self.request.user,
            question=serializer.instance,
        )
