from django.db import models


class BlueProfileManager(models.Manager):
    def get_active(self):
        return self.filter(status__in=self.show_in_roster)


class BlueProfile(models.Model):
    discord_id = models.CharField(primary_key=True, max_length=32)
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


class BlueNewsManager(models.Manager):
    def get_active(self):
        return self.filter(status__in=self.published)


class BlueNews(models.Model):
    title = models.CharField(max_length=64)
    display_name = models.CharField(max_length=32)
    description = models.TextField()
    published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlueNewsManager()

    def __str__(self):
        return '{} - {}'.format(self.display_name, self.title)

    class Meta:
        verbose_name = 'Blue News'
        verbose_name_plural = 'Blue News'
