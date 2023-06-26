from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
from tinymce.models import HTMLField
# Create your models here.


class Contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.firstname
    
    


# Create your models here.



# class Product(models.Model):
#     LANG_CHOICES = (
#         ('English', 'English'),
#         ('Malayalam', 'Malayalam'),
#         ('Arabic', 'Arabic'),
#     )
#     language = models.CharField(max_length=50, choices=LANG_CHOICES)
#     author=models.CharField(max_length=50)
#     name=models.CharField(max_length=50)
#     price=models.FloatField()
#     year=models.IntegerField()
#     image=models.ImageField(upload_to="")
#     publisher=models.CharField(max_length=50)
#     pdf= models.FileField(upload_to="pdf")
    
#     def _str_(self):
#         return self.name 
    
    
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
    