from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
from .models import *
# Create your views here.

def index(request):
    try:
        data = Fighters.objects.all()
        fighters = [
            {
                "id": fighter.pk,
                "first_name": fighter.first_name,
                "initial": fighter.initial,
                "last_name": fighter.last_name
            }
            for fighter in data
        ]
        return JsonResponse(fighters, safe=False)
    except TypeError:
        return JsonResponse({"empty":"empty"})
    