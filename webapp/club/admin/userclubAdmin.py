from django.contrib import admin

from club.models import UserClub


# Register your models here.
@admin.register(UserClub)
class UserClubAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'club',
        'is_owner',
    ]
