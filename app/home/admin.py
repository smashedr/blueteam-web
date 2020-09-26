from django.contrib import admin
from home.models import BlueProfile


@admin.register(BlueProfile)
class BlueProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('main_char', 'main_class', 'show_in_roster', 'discord_id')

    def has_add_permission(self, request, obj=None):
        return False
