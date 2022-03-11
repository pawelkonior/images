from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Image
from .serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(author=user)

    def get_serializer_class(self):
        return ImageSerializer
