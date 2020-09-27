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
