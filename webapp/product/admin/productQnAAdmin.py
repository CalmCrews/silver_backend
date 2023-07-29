from django.contrib import admin

from product.models import ProductQnA


@admin.register(ProductQnA)
class ProductQnAAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'question',
        'answer',
    )
