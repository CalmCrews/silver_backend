from django.urls import path
from product.views import ProductListAPIView, ProductRetrieveAPIView, ProductQuestionRetrieveUpdateDestroyAPIView, ProductQuestionCreateAPIView, \
    ProductQnAListAPIView, ProductQnARetrieveAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view()),
    path("<int:product_id>/", ProductRetrieveAPIView.as_view()),
    path("<int:product_id>/qna/", ProductQnAListAPIView.as_view()),
    path("<int:product_id>/qna/<int:product_qna_id>/", ProductQnARetrieveAPIView.as_view()),
    path("<int:product_id>/ask/", ProductQuestionCreateAPIView.as_view()),
    path("<int:product_id>/ask/<int:product_question_id>/", ProductQuestionRetrieveUpdateDestroyAPIView.as_view()),
]
