from django.contrib import admin

from order.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'product',
        'quantity',
        'status',
        'initial_price',
        'final_price',
    )
