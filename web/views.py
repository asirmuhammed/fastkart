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
from .models import Contact,Testimonial,Blog,Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart



def index(request):
    context = {"is_index": True}

    return render(request, "web/index.html", context)


def about(request):
    context = {"is_about": True,
               
               'testimonial' :Testimonial.objects.all(),
               'blog':Blog.objects.all()
               }
    
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



def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contactform = Contact(firstname=firstname,lastname=lastname,email=email,phone=phone,message=message)
        contactform.save()

    return render(request, "web/contact.html")

def shop (request):
    context={"is_shop": True,'product':Product.objects.all(),}
    return render (request,'web/shop.html',context)



def product_detail (request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product,
    }
    return render(request,'web/product-detail.html',context)

def blog_detail(request,id):
    blog=Blog.objects.get(id=id)
    context={
        'blog':blog,
    }
    return render(request,"web/blog-detail.html",context)


# def Cart (request):
#     context = {"is_cart": True}
    
#     return render(request, "web/cart.html", context)



@login_required(login_url="web:login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="web:login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="web:login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="web:login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="web:login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="web:login")
def cart_detail(request):
    return render(request, 'web/cart_detail.html')


