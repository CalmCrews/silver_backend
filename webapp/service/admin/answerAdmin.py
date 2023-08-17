from django.contrib import admin

from service.models import ServiceAnswer


@admin.register(ServiceAnswer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
