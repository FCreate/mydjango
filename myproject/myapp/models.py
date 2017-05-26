from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


# сделать модель адресов
# есть
class Address(models.Model):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=10)
    apartment = models.PositiveIntegerField()


class Buyer(models.Model):
    user = models.OneToOneField(User)
    phone = models.IntegerField(max_length=10, )
    address = models.ForeignKey(Address)


class Comment(models.Model):
    user = models.ForeignKey(Buyer)
    # product=models.ForeignKey(Product)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, db_index=True)
    object_id = models.PositiveIntegerField(null=True, db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    category = models.CharField(max_length=30)


# create models to category
class Product(models.Model):
    name = models.CharField(max_length=300)
    category = models.ForeignKey(Category)
    description = models.TextField()
    manufacturer = models.CharField(max_length=80)
    all_weight = models.IntegerField()
    weight_for_one = models.IntegerField()
    comments = GenericRelation(Comment)

    # category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default=FRUIT)
    # decimal
    price = models.DecimalField(db_index=True, max_digits=10, decimal_places=2)


class Order(models.Model):
    buyer = models.ForeignKey(Buyer)
    is_valid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True, default=None)
    is_closed = models.BooleanField(db_index=True, default=False)
    is_processed = models.BooleanField(default=False)
    phone = models.IntegerField(max_length=10, null=True)
    # address=models.CharField(max_length=200, null=True,db_index=True)
    name = models.TextField(null=True)


class OrderPosition(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    # создать количество товаров through
    # product = models.ManyToManyField(Product, through='MembershipOP')
    count = models.PositiveIntegerField(default=0)


class Comprod(models.Model):
    user = models.ForeignKey(Buyer)
    content_object = models.ForeignKey(Product)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# убрать MembershipOP заменить manytomany и добавить поле count

# class MembershipOP(models.Model):
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)
#    order_pos = models.ForeignKey(OrderPosition, on_delete=models.CASCADE)
#    count = models.PositiveIntegerField()
#    # decimal field
#    # count=models.DecimalField(db_index=True, default=0, , max_length=10, decimal_places=2)

# product=Product(name='banana',     description='banana',
#    manufacturer='Russia',
#    all_weight=13,
#    weight_for_one=1,
#    price=50,
# )

# product.save()
# product.save()
# i=0
# while (i<5):
#    product.save()





# ==============================================================================
# class Chat(models.Model):
#     message=models.CharField(max_length=200)
#     @classmethod    
#     def create(cls, text):
#         chat=cls(message=text)
#         return chat
#   
# class Ship (models.Model):
#     health=models.IntegerField(default=0)
#     x_coord=models.IntegerField()
#     y_coord=models.IntegerField()
#     direction=models.CharField(max_length=10)
#     @classmethod 
#     def create(cls,health1, x1, y1, direct1):
#         ship=cls(health=health1, x=x1, y=y1, direction=direct1)
#         return ship        
#              
# chat = Chat.create("Hello")
# chat.save()
# ship=Ship.create(4,3,4,"left",)
# ship.save()
# 
# ==============================================================================
# ==============================================================================
# 
# class Chat(models.Model):
#     message=models.CharField(max_length=200)
#     @classmethod
#     def create(cls,some_text):
#         chat=cls(message=some_text)
#         return chat
#         
# class Ship (models.Model):
#     health=models.IntegerField(default=0)
#     x_coord=models.IntegerField()
#     y_coord=models.IntegerField()
#     direction=models.CharField(max_length=10)
#     @classmethod
#     def create(cls, health1, x1, y1, direct1):
#         ship=cls(health=health1, x_coord=x1, y_coord=y1, direction=direct1)
#         return ship        
# 
# class User(models.Model):
#     name=models.CharField(max_length=30)
#     email=models.CharField(max_length=80)
#     score=models.IntegerField(default=0)
#     health=models.IntegerField(default=20)
#     ship_4=models.ForeignKey(Ship)
#     ship_3_1=models.ForeignKet(Ship)
#     ship_3_2=models.ForeignKey(Ship)
#     ship2_1=models.ForeignKey(Ship)
#     chat=models.ManyToManyField(Chat)
#     @classmethod
#     def CreateUser(cls,name1, email1, x1, y1, direct1, text1):
#         ship1=Ship.create(4, x1, y1, direct1)
#         ship1.save()
#         chat1=Chat.create(text1)
#         chat1.save()
#         user=cls(name=name1, email=email1, score=0, health=20,ship=ship1, chat=chat1)
#         return user
# ==============================================================================

# name=User.CreateUser('m','312',3, 4,'left', 'Hello')
# ==============================================================================
# ship=Ship.create(4, 3, 4, "left")
# chat=Chat.create("Hello")
# ==============================================================================
# ==============================================================================
# ('mike', 'i@m', 2, 3, 'left', 'Hello')
# ==============================================================================
# ==============================================================================
# 
# ship.save()
# chat.save()
# ==============================================================================
