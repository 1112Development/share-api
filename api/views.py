from rest_framework import generics

from photos.models import Photo
from photos.serializers import PhotoSerializer


class PhotoList(generics.ListCreateAPIView):
    """List all Photos in An Area, Or add a new one"""

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
