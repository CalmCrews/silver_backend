from django.urls import path, include
from product.views import *

urlpatterns = [
    path("", ProductListAPIView.as_view()),
    path("<int:product_id>/", ProductRetrieveAPIView.as_view()),
    path("<int:product_id>/qna/", ProductQnAListAPIView.as_view()),
    path("<int:product_id>/qna/<int:product_qna_id>/", ProductQnARetrieveAPIView.as_view()),
    path("<int:product_id>/ask/", ProductQuestionCreateAPIView.as_view()),
    path("<int:product_id>/ask/<int:product_question_id>/", ProductQuestionRetrieveUpdateDestroyAPIView.as_view()),
    path("<int:product_id>/joinProductToClub/", ClubProductCreateAPIView.as_view()),
    path('<int:product_id>/orders/', include('order.urls'), )
]
