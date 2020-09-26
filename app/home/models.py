from django.db import models


class BlueProfileManager(models.Manager):
    def get_active(self):
        return self.filter(status__in=self.show_in_roster).order_by('-id')


class BlueProfile(models.Model):
    discord_id = models.CharField(primary_key=True, max_length=32)
    main_char = models.CharField(max_length=32)
    main_class = models.CharField(max_length=32)
    main_role = models.CharField(max_length=32)
    user_description = models.TextField(blank=True)
    show_in_roster = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlueProfileManager()

    def __str__(self):
        return '{} - {}'.format(self.main_char, self.main_class)

    class Meta:
        verbose_name = 'Blue Profile'
        verbose_name_plural = 'Blue Profiles'
