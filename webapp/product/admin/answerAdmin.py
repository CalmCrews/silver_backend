from django.contrib import admin

from product.models import ProductAnswer


@admin.register(ProductAnswer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'content',
    )
