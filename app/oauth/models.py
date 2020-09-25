from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discriminator = models.IntegerField(blank=True, default=0)
    discord_id = models.CharField(blank=True, default=0, max_length=32)
    avatar_hash = models.TextField(blank=True, default='')

    def __str__(self):
        return '{}#{}'.format(self.user, self.discriminator)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
