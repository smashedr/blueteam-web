from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discriminator = models.CharField(max_length=4)
    discord_id = models.CharField(max_length=32)
    avatar_hash = models.TextField(blank=True)
    blue_team_member = models.BooleanField(blank=True, default=False)
    blue_team_officer = models.BooleanField(blank=True, default=False)
    discord_roles = models.JSONField(blank=True, default=list)

    def __str__(self):
        return '{}#{}'.format(self.user, self.discriminator)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
