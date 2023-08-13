from django.contrib import admin

from qna.models.serviceQnA import ServiceQnA


@admin.register(ServiceQnA)
class ServiceQnAAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'question',
        'answer',
    )
