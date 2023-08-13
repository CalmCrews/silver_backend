from django.contrib import admin

from qna.models.serviceQuestion import ServiceQuestion


@admin.register(ServiceQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
