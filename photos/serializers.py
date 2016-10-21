from cloudinary.templatetags import cloudinary
from rest_framework import serializers

from photos.models import Photo


class PhotoSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    lat = serializers.FloatField(required=True)
    long = serializers.FloatField(required=True)
    upload_at = serializers.DateTimeField(read_only=True)
    original = serializers.ImageField(max_length=1000)

    # dont need this field
    thumbnail = serializers.ImageField(max_length=1000, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        uploaded_image = validated_data.pop('original')
        image = cloudinary.uploader.upload(uploaded_image, eager=[
            {'width': 100, 'height': 150,
             'crop': 'fit', 'format': 'jpg'}], folder='shareogrpahy')
        original = 'v1475946077' + '/' + image['public_id']

        #this is wrong!
        thumbnail = 'c_fit,h_150,w_100/' + original
        return Photo.objects.create(original=original, thumbnail=thumbnail, **validated_data)
