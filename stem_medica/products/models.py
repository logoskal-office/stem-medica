from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(blank=True)
    model = models.CharField(max_length=20, blank=True)
    brand = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField(blank=True)
    weight = models.FloatField(blank=True)
    description = models.CharField(max_length=1000)
    images = models.ImageField()
    status = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    images = models.ImageField()