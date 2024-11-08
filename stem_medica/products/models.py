from django.db import models
from multiupload.fields import MultiImageField
from PIL import Image as PilImage
from io import BytesIO
from django.core.files import File

class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=20, blank=True, null=True)
    brand = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(related_name='products',blank=True, null=True, to='Category', on_delete=models.DO_NOTHING)
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image:
            img = PilImage.open(self.image.path)
            if img.width > 500 or img.height > 500:
                output_size = (500,500)
                img.thumbnail(output_size)
                img.save(self.image.path)
