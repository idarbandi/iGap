from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from server.models import Category, Server


def category_icon_upload_path(instance, filename):
    return f"category/{instance.id}/category_icon/{filename}"


# تعریف یک مدل برای Category با یک نام و توضیحات اختیاری
class Category(models.Model):
    """
    مدل برای تعریف یک دسته‌بندی.

    صفات:
        name (str): نام دسته‌بندی.
        description (str, اختیاری): توضیحات اختیاری برای دسته‌بندی.
    """

    name = models.CharField(max_length=150)  # Name of the category
    description = models.TextField(
        blank=True, null=True
    )  # Optional description of the category
    icon = models.FileField(null=True, blank=True)

    def __str__(self):
        """
        بازگشت نام دسته‌بندی به عنوان نمایشگر رشته‌ای آن.

        Returns:
            str: نام دسته‌بندی.
        """
        return self.name  # Return the name of the category as its string representation

    def save(self, *args, **kwargs):
        if self.id:
            existing = get_object_or_404(Category, id=self.id)
            if existing.icon != self.icon:
                existing.icon.delete(save=False)
        super(Category, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="server.Category")
    def category_delete_files(sender, **kwargs):
        for field in insance._meta.fields:
            if field.name == 'icon':
                file = getattr(instance, field.name)
                file.delete(save=False)


# تعریف یک مدل برای Server با فیلدها و ارتباطات مختلف
class Server(models.Model):
    """
    مدل برای تعریف یک سرور.

    صفات:
        name (str): نام سرور.
        owner (ForeignKey): مالک سرور.
        category (ForeignKey): دسته‌بندی سرور.
        description (str, اختیاری): توضیحات اختیاری برای سرور.
        member (ManyToManyField): اعضای مرتبط با سرور.
    """

    name = models.CharField(max_length=150)  # Name of the server
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="srv_owner"
    )  # Owner of the server
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="server_category"
    )  # Category of the server
    description = models.CharField(
        max_length=250, null=True
    )  # Optional description of the server
    member = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )  # Members associated with the server

    def __str__(self):
        """
        بازگشت نام سرور به عنوان نمایشگر رشته‌ای آن.

        Returns:
            str: نام سرور.
        """
        return f"{self.name}-{self.id}"  # Return the name of the server as its string representation


# تعریف یک مدل برای Channel با فیلدها و ارتباطات مختلف
class Channel(models.Model):
    """
    مدل برای تعریف یک کانال.

    صفات:
        name (str): نام کانال.
        owner (ForeignKey): مالک کانال.
        topic (str): موضوع کانال.
        server (ForeignKey): سروری که کانال به آن تعلق دارد.
    """

    name = models.CharField(max_length=150)  # Name of the channel
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ch_owner"
    )  # Owner of the channel
    topic = models.CharField(max_length=150)  # Topic of the channel
    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="channel_server"
    )  # Server to which the channel belongs

    def save(self, *args, **kwargs):
        """
        ذخیره نام کانال به صورت حروف کوچک قبل از ذخیره‌سازی.

        Args:
            *args: آرگومان‌های موقعیتی.
            **kwargs: آرگومان‌های کلیدی.
        """
        self.name = self.name.lower()
        super(Channel, self).save(*args, **kwargs)

    def __str__(self):
        """
        بازگشت نام کانال به عنوان نمایشگر رشته‌ای آن.

        Returns:
            str: نام کانال.
        """
        return self.name  # Return the name of the channel as its string representation
