from cloudinary.templatetags import cloudinary
from rest_framework import serializers

from photos.models import Photo
from photos.serializer_fields import CloudinaryField


class PhotoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    lat = serializers.FloatField(required=True)
    long = serializers.FloatField(required=True)
    created = serializers.DateTimeField(read_only=True)
    original = CloudinaryField()

    def create(self, validated_data):
        """
        Create and return a new `Photo` instance, given the validated data.
        """
        validated_data['original'] = cloudinary.uploader.upload(validated_data.pop('original'), folder='shareapp')

        return Photo.objects.create(**validated_data)