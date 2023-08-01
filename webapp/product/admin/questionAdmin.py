from django.contrib import admin

from product.models import ProductQuestion


@admin.register(ProductQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )
