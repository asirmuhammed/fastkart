# Create web/urls.py and paste the following
from django.urls import path
from . import views


app_name = "web"

urlpatterns = [
    path('register',views.register_1,name="register"),
    path('login',views.login_1,name="login"),
    path('', views.index, name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('shop',views.shop,name="shop"),
    # path('blog-detail',views.blog_detail,name="blog-detail"),
    path('blog-detail/<int:id>/',views.blog_detail,name="blog-detail"),
    path('product-detail/<int:id>/',views.product_detail,name="product-detail"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    

    





]