from rest_framework.generics import RetrieveAPIView, get_object_or_404

from notification.models import UserNotification
from notification.serializers.usernotificationRetrieveSerializer import UserNotificationRetrieveSerializer


class UserNotificationRetrieveAPIView(RetrieveAPIView):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationRetrieveSerializer
    lookup_url_kwarg = 'notification_id'

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {
            'notification': self.kwargs[lookup_url_kwarg],
            'receiver': self.request.user
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        print(obj)
        self.check_object_permissions(self.request, obj)

        return obj
