from django.db import models
from .managers import BlueProfileManager, BlueNewsManager


class BlueProfile(models.Model):
    discord_id = models.CharField(unique=True, max_length=32)
    main_char = models.CharField(max_length=32)
    main_class = models.CharField(max_length=32)
    main_role = models.CharField(max_length=32)
    user_description = models.TextField(blank=True)
    show_in_roster = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlueProfileManager()

    def __str__(self):
        return '{} - {}'.format(self.main_char, self.main_class)

    class Meta:
        verbose_name = 'Blue Profile'
        verbose_name_plural = 'Blue Profiles'


class BlueNews(models.Model):
    title = models.CharField(max_length=64)
    display_name = models.CharField(max_length=32)
    description = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlueNewsManager()

    def __str__(self):
        return '{} - {}'.format(self.display_name, self.title)

    class Meta:
        verbose_name = 'Blue News'
        verbose_name_plural = 'Blue News'


class GuildApplicants(models.Model):
    PENDING = 'PE'
    APPROVED = 'AP'
    DECLINED = 'DE'
    APP_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (DECLINED, 'Declined'),
    ]
    char_name = models.CharField(max_length=32)
    char_role = models.CharField(max_length=32)
    warcraft_logs = models.URLField()
    speed_test = models.URLField()
    spoken_langs = models.CharField(max_length=32)
    native_lang = models.CharField(max_length=32)
    fri_raid = models.BooleanField(default=False)
    sat_raid = models.BooleanField(default=False)
    raid_exp = models.TextField(blank=True)
    why_blue = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    app_status = models.CharField(
        max_length=2,
        choices=APP_STATUS_CHOICES,
        default=PENDING,
    )

    def __str__(self):
        return '{} - {}'.format(self.char_name, self.char_role)

    class Meta:
        verbose_name = 'Guild Applicants'
        verbose_name_plural = 'Guild Applicants'
