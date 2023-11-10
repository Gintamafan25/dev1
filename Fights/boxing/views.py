from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
from .models import *
# Create your views here.

def index(request):
    try:
        data = Fighters.objects.all()
        fighters = serializers.serialize("json", data)
        return JsonResponse({"fighters":fighters})
    except TypeError:
        return JsonResponse({"empty":"empty"})
    