from django.contrib import admin

from .models import Image, Thumbnail

admin.site.register(Image)
admin.site.register(Thumbnail)
