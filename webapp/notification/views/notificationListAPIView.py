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
        updated_data = []

        for query, serialized_data in zip(queryset, serializer.data):
            user_notifications = query.user_notification.filter(receiver=request.user)
            is_read = all(notification.is_read for notification in user_notifications)
            extra_data = {
                'is_read': is_read,
            }
            serialized_data.update(extra_data)
            updated_data.append(serialized_data)

        return Response(updated_data)
