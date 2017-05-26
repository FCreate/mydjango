from django.shortcuts import render
from myapp.models import Order, OrderPosition, Product, Buyer

#def book_list(request):
product=Product.objects.create(name='banana', description='banana', manufacturer='Russia',
    all_weight=13,
    weight_for_one=1,
    price=50,)
product.save
#==============================================================================
# import django
# print(django.get_version())
#==============================================================================
