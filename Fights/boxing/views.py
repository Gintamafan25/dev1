from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

def index(request):
    print(request.COOKIES)
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

def register(request):
    if request.method == "OPTIONS":
        print("Preflight request headers:", request.headers)
        print("Preflight request method:", request.method)
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = 'http://localhost:4200'  # Replace with the actual origin of your Angular application
        response['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, Authorization'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        return response
    if request.method == "POST":
        data = json.loads(request.body)
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirmed_password = data["confirm_password"]
        print("trying to register")
        
        if password != confirmed_password:
            return JsonResponse({"message": "Passwords do not match"})
        
        users = User.objects.all()
        
        username_exists = False 
        email_exists = False
        
        for user in users:
            if user.username == username:
                username_exists = True
                break
        for user in users:
            if user.email == email:
                email_exists = True
                break
        
        if email_exists == True:
            return JsonResponse({"message": "Email already registered"})
        
        if username_exists == True:
            return JsonResponse({"message": "Username not available"})
        
        user = User(username=username, email=email, password=password)
        user.save() 
        
        user = authenticate(username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            token = default_token_generator.make_token(user)
            
            response = JsonResponse({"message":"Success"})
            response.set_cookie("session_token",token, max_age=3600, httponly=True)
            return response
        else:
            return JsonResponse({"message": "Failed to register user"})
            
    else:
        return JsonResponse({"message":"empty"})
        
    