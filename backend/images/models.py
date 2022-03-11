from django.contrib.auth import get_user_model
from django.db import models

from images.validators import validate_file_type


class Image(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='images')
    url = models.FileField(upload_to='images_files/', validators=[validate_file_type])
    name = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.url.name
        return super().save(*args, **kwargs)


class Thumbnail(models.Model):
    image = models.ForeignKey('Image', on_delete=models.CASCADE, related_name='thumbnails')
    url = models.FileField(upload_to='resized_images')
    height = models.PositiveIntegerField()

    def __str__(self):
        return self.url.name
