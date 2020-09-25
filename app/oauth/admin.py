from django.contrib import admin
from oauth.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('-pk',)
    list_display = ('user', 'discriminator', 'discord_id')

    def has_add_permission(self, request, obj=None):
        return False
