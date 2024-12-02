from django.db import models
from django.shortcuts import get_object_or_404
from django.dispatch import receiver
from django.dispatch import receiver

class IconFileMixin(models.Model):
    class Meta:
        abstract = True

    def delete_old_file(self, field_name, new_file):
        if self.id:
            existing = get_object_or_404(self.__class__, id=self.id)
            old_file = getattr(existing, field_name)
            if old_file != new_file:
                old_file.delete(save=False)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.delete_old_file('icon', self.icon)
        super().save(*args, **kwargs)