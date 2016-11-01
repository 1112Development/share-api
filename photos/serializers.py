from cloudinary.api import delete_resources
from cloudinary.templatetags import cloudinary
from django.db import transaction
from rest_framework import serializers

from photos.models import Photo, CloudinaryImage
from photos.serializer_fields import CloudinaryImageField


class PhotoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    lat = serializers.FloatField(required=True)
    long = serializers.FloatField(required=True)
    created = serializers.DateTimeField(read_only=True)
    image = CloudinaryImageField()

    # device = serializers.DictField(write_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Photo` instance, given the validated data.
        """
        upload_data = cloudinary.uploader.upload(validated_data.pop('image'))
        # The try/except and atomic transaction causes errors in the to be displayed incorrectly. This usually
        #  resulting in all errors being treated as a field error (specificly, 'lat'not being a field).
        # This makes debugging harder, but the trade-off is an increase in DB integrity.
        try:
            with transaction.atomic():
                image = CloudinaryImage.objects.create(id=upload_data['public_id'],
                                                       format=upload_data['format'],
                                                       height=upload_data['height'],
                                                       width=upload_data['width'],
                                                       bytes=upload_data['bytes'],
                                                       )
                # uploads from DRF Browers do not have a device, set as '0
                # device, created = Device.objects.get_or_create(id=validated_data.get('device', '0'))
                return Photo.objects.create(image=image, **validated_data)
        except Exception as e:
            delete_resources(public_ids=[upload_data['public_id']])
            return e
