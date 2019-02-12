from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Categorie(models.Model):
    categorie = models.CharField(max_length=50)
    def __str__(self):
        return self.categorie


class Material(models.Model):
    material = models.CharField(max_length=50)
    def __str__(self):
        return self.material

class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="item/img/", blank=True)

    def __str__(self):
        return self.name