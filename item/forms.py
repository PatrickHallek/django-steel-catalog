from django import forms
from crispy_forms.helper import FormHelper
from .models import Item, Categorie, Material


class ItemForm(Item):
    class Meta:
        model = Item
        fields = ['categorie','description','material','length', 'width', 'price']

class CategorieForm(Categorie):
    class Meta:
        model = Categorie
        fields = ['categorie']

class MaterialForm(Material):
    class Meta:
        model = Item
        fields = ['material']