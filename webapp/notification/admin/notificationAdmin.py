from django.contrib import admin

from notification.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sender',
        'title',
        'message',
        'category',
    ]
