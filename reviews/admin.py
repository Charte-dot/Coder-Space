from django.contrib import admin
from .models import Reviews


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'approved', 'product')
    actions = ['approve_review']


admin.site.register(Reviews)
