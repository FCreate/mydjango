import os

import random
import string
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

import django
django.setup()
from myapp.models import Order, OrderPosition, Product, Buyer, Address, Category
from comments.models import Comment
from datetime import datetime, date, time
from django.utils import timezone
def randstring(n):
    b=string.ascii_letters + string.digits
    return ''.join([random.choice(b) for i in range(n)])

com=[]
for i in range (1,100001):
    com.append(Comment(user_id=random.randint(1,10000), object_id=i, content_type_id=3,  content=randstring(20),))
Comment.objects.bulk_create(com)
com.clear()