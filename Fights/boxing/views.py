from django.shortcuts import render
from django.http import JsonResponse
import json
from django.core import serializers
# Create your views here.

def index(request):
    list = ["empty"]
    return JsonResponse({"list": list})
    