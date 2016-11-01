import collections

from rest_framework.fields import ImageField


# Custom Field For CloudinaryImage model, allows model to be treated as a standard image field for uploading, but
# displayed as a dictionary when serialized.
class CloudinaryImageField(ImageField):
    def to_representation(self, value):
        d = collections.OrderedDict()
        d['public_id'] = value.id
        d['url'] = value.url()
        d['format'] = value.format
        d['height'] = value.height
        d['width'] = value.width
        d['bytes'] = value.bytes

        return d
