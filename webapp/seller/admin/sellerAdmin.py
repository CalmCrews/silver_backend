from django.contrib import admin

from seller.models import Seller


@admin.register(Seller)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'represent',
        'business_number',
        'center_number',
        'email',
    )
