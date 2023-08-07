from django.contrib import admin

from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'content',
        'rating',
        'created_at',
        'updated_at',
    )
   