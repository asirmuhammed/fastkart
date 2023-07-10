from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import uuid
# Create your models here.


class Contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.firstname
       
    
class Testimonial (models.Model):
    name =models.CharField(max_length=50)
    post =models.CharField(max_length=30)
    testimonial_tittle =models.CharField(max_length=60)
    testimonial_sentence =models.TextField()
    image =models.ImageField()
    
    def __str__(self):
        return self.name



class Blog(models.Model):
    title=models.CharField(max_length=225)
    summary=models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    image = VersatileImageField('blog_Image',upload_to='update/')
    ppoi = PPOIField('Image PPOI')
    content= HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
class Product (models.Model):
    class CategoryChoices(models.TextChoices):
        VegitablesFruits ="Vegitables & Fruits"
        MeatsSeafood  ="MeatsSeafood"
        BreakfastDairy ="BreakfastDairy"
        FrozenFood = "FrozenFood"
        
        
        
    product_name=models.CharField(max_length=60)
    product_weight=models.CharField(max_length=30)
    image = VersatileImageField('Image',upload_to='update/')
    # product_category=Product.objects.filter(category='')
    category= models.CharField(max_length=20,choices=CategoryChoices.choices)
    product_description= models.TextField()
    product_price= models.CharField(max_length=20)
    del_price=models.CharField(max_length=20)
    
    def __str__(self):
        return self.product_name
    
    
    

    
class Cart (models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.id
    
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='items')
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cartitems")
    quantity=models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.product.product_name