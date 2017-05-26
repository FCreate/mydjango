#coding:utf-8
import os

import random
import string
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
django.setup()
from datetime import datetime, date, time
from django.utils import timezone
from django.contrib.auth.models import User
from myapp.models import Order, OrderPosition, Product, Buyer, Address, Category, Comment, Comprod
def randstring(n):
    b=string.ascii_letters + string.digits
    return ''.join([random.choice(b) for i in range(n)])

print ("Address")
#Адреса
adr=[]
for i in range (10000):
    adr.append(Address(city=randstring(10),street=randstring(10),house=randstring(2),apartment=random.randint(1,1000),))
Address.objects.bulk_create(adr)
adr.clear()
#Добавить покупателей
a=[]
user1=User(username=randstring(10), email=randstring(10),first_name=randstring(10),last_name=randstring(10),)
print (user1.username)
user1.set_password('qwert123')
a.append(user1)
print("Users")
for i in range(10000):
    #print (i)
    user =User(username=randstring(10),password='qwert123', email=randstring(10),first_name=randstring(10),last_name=randstring(10),)
    #user.set_password('qwert123')
    a.append(user)
User.objects.bulk_create(a)
a.clear()

print ('Buyers')
b=[]
#for j in range (1000):
for i in range (1,10001):
    #print (i)
    b.append(Buyer(user_id=i,phone=random.randint(1,10000),address_id=i,))
Buyer.objects.bulk_create(b)
b.clear()
#Категории
c=[]
c.append(Category(category='Fruit'))
c.append(Category(category='Vegetable'))
c.append(Category(category='Grocery'))
c.append(Category(category='Honey'))
c.append(Category(category='Basket'))
Category.objects.bulk_create(c)
c.clear()

c=list(Category.objects.all())
#Товары
print("Products")
for i in range (100000):
    product=Product(name=randstring(10), description=randstring(10), manufacturer=randstring(10), 
        all_weight=random.randint(1,10000),
        weight_for_one=random.randint(1,10000),
        price=random.randint(1,10000),category_id=(random.choice(c)).id)
    a.append(product)
Product.objects.bulk_create(a)
a.clear()



a=list(User.objects.exclude().order_by('id'))
#values list random choice
#Добавить статусы заказов

print("Order")
order=[]
for i in range (1,10001):
    order.append(Order(buyer_id=i, is_valid=True, closed_at=None, phone=random.randint(1,10000), name=randstring(20), ))
Order.objects.bulk_create(order)
#Добавить заказы
orders=list(Order.objects.all())
products=list(Product.objects.all())
print("Order_Pos")
order_pos=[]
#random_choice

for i in range (1,100001):
    order_pos.append(OrderPosition(order_id=((random.choice(orders)).id), product_id=((random.choice(products)).id), count=random.randint(1, 10)))
OrderPosition.objects.bulk_create(order_pos)


com=[]
for i in range (1,100001):
    com.append(Comment(user_id=random.randint(1,10000), object_id=i, content_type_id=4,  content=randstring(20),))
Comment.objects.bulk_create(com)
com.clear()
comprod=[]
for i in range (1,100001):
    comprod.append(Comprod(user_id=random.randint(1,10000), content_object_id=random.randint(1,100001),  content=randstring(20),))
Comment.objects.bulk_create(com)
com.clear()

#comprod=[]
#for i in range (1,100001):



















#member=[]
#for i in range (1,100001):
##
 #   j=random.randint(1,10)
 #   for k in range (1,j):
 #       member.append(MembershipOP(product_id=k, order_pos_id=i, count=random.randint(1,10),))
#MembershipOP.objects.bulk_create(member)



#==============================================================================
#     j=random.randint(1,10)
#     for k in range(1, j):
#         order_pos[i].product.add(product_id=random.randint(1,100000))
# 
#==============================================================================
#можно не выбирать user_id из таблицы user
#b=Buyer.objects.exclude()














#buyer=Buyer(user=User(username=randstring(10),password='qwert123', email=randstring(10),first_name=randstring(10),last_name=randstring(10),),phone=random.randint(1,10000),address=randstring(10),)
#buyer.save()
#print randstring(10)
#==============================================================================
# objs=[
#         Product(name='banana', description='banana', manufacturer='Russia', 
#         all_weight=13,
#         weight_for_one=1,
#         price=50,),
#         Product(name='banana', description='banana', manufacturer='Russia', 
#         all_weight=13,
#         weight_for_one=1,
#         price=50,),
#         Product(name='banana', description='banana', manufacturer='Russia', 
#         all_weight=13,
#         weight_for_one=1,
#         price=50,)
# ]
#==============================================================================

#==============================================================================
# Product(name='banana', description='banana', manufacturer='Russia', 
#         all_weight=13,
#         weight_for_one=1,
#         price=50,),
#         Product(name='banana', description='banana', manufacturer='Russia', 
#         all_weight=13,
#         weight_for_one=1,
#         price=50,)
#==============================================================================
    

#def book_list(request):
#i=0
#==============================================================================
# while (i<10):
#     product=Product.objects.create(name='banana', description='banana', manufacturer='Russia',
#     all_weight=13,
#     weight_for_one=1,
#     price=50,)
#     product.save
#==============================================================================
    #return render(request, 'book_list.html', {'books': books})




#==============================================================================
# from myapp.models import Order, OrderPosition, Product, Buyer
# 
# product=Product(name='banana',     description='banana'
#     manufacturer='Russia',
#     all_weight=13,
#     weight_for_one=1,
#     price=50,
# )
# #buyer=Buyer.Objects.create()
#==============================================================================
