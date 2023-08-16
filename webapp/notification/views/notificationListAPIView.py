from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from notification.models import Notification
from notification.serializers import NotificationSerializer


class NotificationListAPIView(ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user_notification__receiver=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
