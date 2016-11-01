import uuid

import cloudinary
import cloudinary.api
from django.db import models


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    lat = models.FloatField(max_length=255, blank=False, null=False)
    long = models.FloatField(max_length=255, blank=False, null=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    image = models.OneToOneField(to='CloudinaryImage', null=False, blank=False)

    # device = models.ForeignKey(to='Device', null=True, blank=True)

    def self_destruct(self):
        """Determine if photo should be deleted"""
        pass

    def location(self):
        """Return latitude and longitude Tuple"""
        return self.lat, self.long

    def delete(self, using=None, keep_parents=False):
        """Delete Cloudinary stored photo along with photo Model"""
        cloudinary.api.delete_resources(public_ids=[self.original.public_id])
        return super(Photo, self).delete()


class CloudinaryImage(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    format = models.CharField(max_length=255, null=False, editable=False)
    height = models.CharField(max_length=255, null=False, editable=False)
    width = models.CharField(max_length=255, null=False, editable=False)
    bytes = models.IntegerField(null=False, editable=False)

    def url(self):
        """Create the URL for the Image"""
        # We create the URL dynamically so in case we change schemas or hosts in the future, we won't need to migrate
        # all the data in the database.
        config = cloudinary.config()
        return 'http://res.cloudinary.com/' + config.cloud_name + '/' + self.id

        # class Device(models.Model):
        #     id = models.CharField(max_length=255, primary_key=True)
