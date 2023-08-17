from django.urls import path, include

from service.views import *

urlpatterns = [
    path("", ServiceQnAListAPIView.as_view()),
    path("<int:qna_id>/", ServiceQnARetrieveAPIView.as_view()),
    path("ask/", ServiceQuestionCreateAPIView.as_view()),
    path("ask/<int:service_question_id>/", ServiceQuestionRetrieveUpdateDestroyAPIView.as_view()),
]
