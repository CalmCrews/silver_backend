from django.contrib import admin

from club.models import ClubProduct


@admin.register(ClubProduct)
class ClubProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'club',
        'maximum',
    ]
