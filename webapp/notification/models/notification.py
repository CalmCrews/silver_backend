from django.db import models

from user.models import User

NOTIFICATION_CATEGORY_CHOICES = (
    ('GROUPBUY', 'GROUPBUY'),
    ('STING', 'STING')
)


class Notification(models.Model):
    class Meta:
        db_table = 'notification'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255
    )
    message = models.CharField(
        max_length=255
    )
    category = models.CharField(
        choices=NOTIFICATION_CATEGORY_CHOICES,
        max_length=100,
    )
    clubproduct = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
