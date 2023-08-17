from django.contrib import admin

from service.models.serviceQnA import ServiceQnA


@admin.register(ServiceQnA)
class ServiceQnAAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'question',
        'answer',
    )
