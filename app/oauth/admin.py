from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'discriminator', 'is_staff', 'is_superuser',)
    list_filter = ('is_staff', 'is_superuser',)
    fieldsets = UserAdmin.fieldsets + (
        ('OAuth', {'fields': ('discord_username', 'discriminator', 'discord_id', 'discord_roles',
                              'blue_team_member', 'blue_team_officer',)}),
    )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('blue_team_member', 'blue_team_officer',)}),
    # )
    readonly_fields = ('discord_username', 'discriminator', 'discord_id', 'discord_roles',)
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
