# Create web/urls.py and paste the following
from django.urls import path
from . import views
from  . import views

app_name = "web"

urlpatterns = [
    path('register',views.register_1,name="register"),
    path('login',views.login_1,name="login"),
    path('', views.index, name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    





]