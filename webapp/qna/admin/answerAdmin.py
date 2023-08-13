from django.contrib import admin

from qna.models.serviceAnswer import ServiceAnswer


@admin.register(ServiceAnswer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
