from rest_framework import serializers

from .models import Image, Thumbnail


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
        read_only_fields = ['name']
