from django.contrib import admin

from club.models import ClubTag


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
