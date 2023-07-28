from rest_framework.permissions import BasePermission

from product.models import ProductQnA


class IsProductQuestionOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        qna = ProductQnA.objects.get(question=obj)
        return qna.user == request.user
