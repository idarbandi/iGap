######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: model_mixins
Description: This module contains mixins for enhancing Django models with 
             additional functionality, including file management.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404


class IconFileMixin(models.Model):
    """
    Mixin to manage icon files for a model.

    Methods:
        delete_old_file(field_name, new_file): Deletes the old file if it is different from the new file.
        save(*args, **kwargs): Overrides the save method to delete the old file and convert the name to lowercase.
    """

    class Meta:
        abstract = True

    def delete_old_file(self, field_name, new_file):
        """
        Deletes the old file if it is different from the new file.

        Args:
            field_name (str): The name of the file field.
            new_file (File): The new file being saved.

        """
        if self.id:
            existing = get_object_or_404(self.__class__, id=self.id)
            old_file = getattr(existing, field_name)
            if old_file != new_file:
                old_file.delete(save=False)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to delete the old file and convert the name to lowercase.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        """
        self.name = self.name.lower()
        self.delete_old_file('icon', self.icon)
        super().save(*args, **kwargs)
