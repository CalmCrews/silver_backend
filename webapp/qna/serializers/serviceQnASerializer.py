from rest_framework import serializers

from qna.models import ServiceQnA


class ServiceQnASerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    class Meta:
        model = ServiceQnA
        fields = [
            'id',
            'question',
            'answer',
        ]

        read_only_fields = [
            'answer',
        ]

    def get_question(self, product_qna_id):
        from qna.serializers import ServiceQuestionSerializer

        question_serializer = ServiceQuestionSerializer(product_qna_id.question)
        return question_serializer.data if product_qna_id.question else None

    def get_answer(self, product_qna_id):
        from qna.serializers import ServiceAnswerSerializer

        answer_serializer = ServiceAnswerSerializer(product_qna_id.answer)
        return answer_serializer.data if product_qna_id.answer else None
