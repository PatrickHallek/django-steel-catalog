from django.contrib import admin
from .models import Item, Categorie, Material


admin.site.register(Categorie)
admin.site.register(Material)
admin.site.register(Item)