from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from item.models import Item
import requests


def index_view(request):

    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'home/index.html', context)
