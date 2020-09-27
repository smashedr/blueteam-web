from django.contrib import admin
from home.models import BlueProfile, BlueNews


@admin.register(BlueProfile)
class BlueProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('main_char', 'main_class', 'show_in_roster', 'discord_id')

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(BlueNews)
class BlueNewsAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('title', 'display_name', 'published', 'created_at')
