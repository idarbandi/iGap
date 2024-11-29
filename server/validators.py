import os

from django.core.exceptions import ValidationError
from PIL import Image


def icon_image_size_validator(image):
    if image:
        with Image.open(image) as img:
            if img.height > 70 or img.width > 70:
                raise ValidationError(
                    f"The Maximun Allowed Dimensions For The Image Are 70x70 - The Image You Have Uploaded is f{image.size}"
                )


def image_file_extension_validator(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported File Extensions')
