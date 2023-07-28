from rest_framework.permissions import BasePermission


class IsProductQuestionOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.product.owner == request.user
