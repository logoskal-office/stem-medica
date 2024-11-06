from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=20, blank=True)
    brand = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=1000)
    images = models.ImageField()
    price = models.IntegerField(blank=True)
    category = models.ForeignKey(to='Category', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(blank=True)
    weight = models.FloatField(blank=True)
    status = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.ImageField()

class Images(models.Model):
    product = models.ForeignKey(to='Category', on_delete=models.CASCADE)
    image = models.ImageField()