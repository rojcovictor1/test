import os
import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(
        upload_to=get_file_path, default='', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='author')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_file_path, default='', blank=True, null=True)
