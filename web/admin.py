from django.contrib import admin
from .models import Contact,Testimonial,Blog,Product,Cart,CartItem

# Register your models here.


admin.site.register(Contact)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)