from django.contrib import admin

from service.models import ServiceQuestion


@admin.register(ServiceQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
