import cloudinary

from rest_framework.fields import ImageField



class CloudinaryField(ImageField):
    def to_representation(self, value):
        cloudinary.config()
        if not getattr(value, 'url', None):
            # If the file has not been saved it may not have a URL.
            return None
        url = value.url
        display_dict = {
            'format': value.format,
            'public_id': value.public_id,
            'cloud_name':cloudinary.config().cloud_name
            }
        request = self.context.get('request', None)
        if request is not None:
            display_dict['url'] = request.build_absolute_uri(url)
        return display_dict

