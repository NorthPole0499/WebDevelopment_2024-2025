from django.contrib import admin
from .models import LogoOrder


@admin.register(LogoOrder)
class LogoOrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at')
    search_fields = ('full_name', 'description')
    ordering = ('-created_at',)