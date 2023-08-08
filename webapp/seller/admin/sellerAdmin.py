from django.contrib import admin

from seller.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'represent',
        'business_image',
        'business_number',
        'center_number',
        'email',
    )
