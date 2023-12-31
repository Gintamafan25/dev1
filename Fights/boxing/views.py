from http import cookies
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.csrf import csrf_exempt, get_token, ensure_csrf_cookie  

# Create your views here.
CSRF_TOKEN = None

@ensure_csrf_cookie
def csrf(request):
    token = request.META.get('CSRF_COOKIE','')
    CSRF_TOKEN = token
    print(token, "First")
    if not request.session.session_key:
        request.session.save()
        
        
        return JsonResponse({"customToken": token})
    return JsonResponse({"customToken": token})
@ensure_csrf_cookie
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
        return JsonResponse({"fighters":fighters}, safe=False)
        
    except TypeError:
        return JsonResponse({"empty":"empty"})
    

@ensure_csrf_cookie
def register(request):
   
    if request.method == "POST":
        
        try:
            data = json.loads(request.body)
            username = data["username"]
            email = data["email"]
            password = data["password"]
            confirmed_password = data["confirm_password"]
          
            
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
        except TypeError:
            return JsonResponse({"message": "empty3"})
                
    else:
        return JsonResponse({"message":"empty"})
        
    