from django.urls import path

from notification.views import *

urlpatterns = [
    path("", NotificationListAPIView.as_view()),
    path("<int:notification_id>", UserNotificationRetrieveAPIView.as_view())
]
