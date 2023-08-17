from django.contrib import admin

from notification.models import UserNotification


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'notification',
        'receiver',
        'is_read',
    ]
