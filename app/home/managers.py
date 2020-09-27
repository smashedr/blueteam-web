from django.db import models


class BlueProfileManager(models.Manager):
    def get_active(self):
        return self.filter(status__in=self.show_in_roster)


class BlueNewsManager(models.Manager):
    def get_active(self):
        return self.filter(status__in=self.published)
