from django.db.models import QuerySet
from rest_framework.generics import UpdateAPIView, get_object_or_404
from rest_framework.response import Response

from user.models import User
from user.serializers import UserNicknameSerializer


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

    def update(self, request, *args, **kwargs):
        nickname = self.request.data.get('nickname')
        if not nickname:
            return Response({'message': '닉네임을 입력해주세요.'}, status=400)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
