from django.contrib import admin
from myapp.models import Buyer, Product, Order, OrderPosition, Address, Comment, Category

#from myapp.models import User, Ship, Chat


# Register your models here.
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderPosition)
admin.site.register(Address)
admin.site.register(Comment)
admin.site.register(Category)
#==============================================================================
# admin.site.register(Chat)
# admin.site.register(Ship)
# admin.site.register(User)
# 
#==============================================================================
