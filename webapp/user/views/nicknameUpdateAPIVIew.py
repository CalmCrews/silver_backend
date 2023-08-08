from django.db.models import QuerySet
from rest_framework.generics import UpdateAPIView, get_object_or_404

from user.models import User
from user.serializers.userNicknameSerializer import UserNicknameSerializer


class UserNicknameUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserNicknameSerializer
    def get_queryset(self):
        queryset = self.queryset.filter(id=self.request.user.id)
        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        self.check_object_permissions(self.request, obj)
        return obj
