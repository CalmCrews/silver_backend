from rest_framework import serializers

from product.models import ProductQnA


class ProductQnASerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = ProductQnA
        fields = [
            'id',
            'question',
            'answer',
        ]

        read_only_fields = [
            'answer',
        ]

    def get_question(self, product_qna_id):
        from product.serializers import ProductQuestionSerializer

        question_serializer = ProductQuestionSerializer(product_qna_id.question)
        return question_serializer.data if product_qna_id.question else None

    def get_answer(self, product_qna_id):
        from product.serializers import ProductAnswerSerializer

        answer_serializer = ProductAnswerSerializer(product_qna_id.answer)
        return answer_serializer.data if product_qna_id.answer else None
