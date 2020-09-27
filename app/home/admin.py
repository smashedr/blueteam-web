from django.contrib import admin
from .models import BlueProfile, BlueNews


@admin.register(BlueProfile)
class BlueProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('main_char', 'main_class', 'main_role', 'show_in_roster', 'discord_id',)
    list_filter = ('main_class', 'main_role', 'show_in_roster',)
    ordering = ('-main_role',)

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(BlueNews)
class BlueNewsAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('title', 'display_name', 'published', 'created_at')
    list_filter = ('published',)
    ordering = ('created_at',)
