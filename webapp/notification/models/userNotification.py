from django.db import models

from config.models import BaseModel
from notification.models.notification import Notification
from user.models import User


class UserNotification(BaseModel):
    class Meta:
        db_table = 'user_notification'
        verbose_name = 'UserNotification'
        verbose_name_plural = 'UserNotifications'

    notification = models.ForeignKey(
        Notification,
        on_delete=models.CASCADE,
        related_name='user_notification',
        verbose_name='알림',
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='받는 사람',
    )

    is_read = models.BooleanField(
        default=False
    )
