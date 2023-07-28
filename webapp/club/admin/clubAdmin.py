from django.contrib import admin

from club.models import Club


# Register your models here.
@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'code',
        'intro',
        'level',
    ]