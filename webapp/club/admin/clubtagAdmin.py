from django.contrib import admin

from club.models import ClubTag


# Register your models here.
@admin.register(ClubTag)
class ClubTagAdmin(admin.ModelAdmin):
    list_display = [
        'club',
        'gathering',
        'daily',
        'economic',
        'biology',
        'culture',
        'study',
        'life',
        'sports',
        'religion',
        'health',
        'etc',
    ]