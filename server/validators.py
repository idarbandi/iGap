######################################################################
#                             iGap Project                           #
######################################################################

"""
Module: image_validators
Description: This module contains custom validation functions for image files.
Author: idarbandi
Date: 04 December 2024
Contact: darbandidr99@gmail.com
Github: https://github.com/idarbandi
"""

import os

from django.core.exceptions import ValidationError
from PIL import Image


def validate_icon_image_size(image):
    """
    Validates the dimensions of an uploaded icon image.

    Args:
        image (File): The image file to validate.

    Raises:
        ValidationError: If the image dimensions exceed 70x70 pixels.

    """
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height > 70:
                raise ValidationError(
                    f"The maximum allowed size is 70x70. Your size = {img.size}"
                )


def validate_image_file_extension(value):
    """
    Validates the file extension of an uploaded image.

    Args:
        value (File): The image file to validate.

    Raises:
        ValidationError: If the image file extension is not one of the valid extensions.

    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(
            f"Your extension must be one of {valid_extensions}, but got {ext}"
        )
