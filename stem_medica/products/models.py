from django.db import models
from multiupload.fields import MultiImageField

class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(blank=True, null=True, to='Category', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/category/thumbnails/')

class Image(models.Model):
    product = models.ForeignKey(to='Product', related_name='images' ,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product images/')