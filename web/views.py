# Edit web/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def index(request):
    context = {"is_index": True}

    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True}
    
    return render(request, "web/about.html", context)

def contact(request):
    context = {"is_contact": True}
    
    return render(request, "web/contact.html", context)


def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:register')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:register')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/signup.html")

def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:home')
        else:  
            print('hi')
            return redirect('web:register')
    return render(request,"web/login.html")



