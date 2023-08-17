from rest_framework.generics import RetrieveUpdateDestroyAPIView

from service.models import ServiceQuestion, ServiceQnA
from service.serializers import ServiceQuestionSerializer


class ServiceQuestionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceQuestion.objects.all()
    serializer_class = ServiceQuestionSerializer
    lookup_url_kwarg = 'service_question_id'

    def get_queryset(self):
        queryset = ServiceQuestion.objects.filter(id=self.kwargs.get('service_question_id'))
        return queryset

    def perform_destroy(self, instance):
        instance.delete()
        ServiceQnA.objects.filter(
            user=self.request.user,
            question=instance,
        ).delete()
