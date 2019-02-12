from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import math


class Categorie(models.Model):
    categorie = models.CharField(max_length=50)
    multiplicator = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.categorie


class Material(models.Model):
    material = models.CharField(max_length=50)
    multiplicator = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.material


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    image = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    image_url = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_price(self):
        price= 30 +(self.width * self.length)**(1/2) * float(self.categorie.multiplicator * self.material.multiplicator) / 2
        price = round(price,2)
        return price
