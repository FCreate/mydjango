from django.shortcuts import render
from .models import User
from myapp.forms import UserForm
from myapp.forms import ProductForm
from myapp.forms import RegistrationForm
from myapp.forms import BuyForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib import auth
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect 
from django.http import HttpResponse, HttpRequest
from myapp.models import Product
from myapp.models import Comment
from myapp.models import Buyer
from myapp.models import Address
from myapp.models import Order
from django.db.models import Q
from myapp.models import OrderPosition
from myapp.models import Category
from myapp.models import Comprod
from django.db.models import Count

from django.http import JsonResponse
from django.http import Http404
from django.core.urlresolvers import reverse
import string
from datetime import datetime, date, time
from django.utils import timezone
import random
from django.shortcuts import get_object_or_404
from generic_aggregation import generic_annotate
from generic_aggregation import generic_aggregate
import generic_aggregation
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers.python import Serializer
#from rest_framework import routers, serializers, viewsets
import random

'''
class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {'id': instance.pk, 'num_comments': instance.products__num_comments}
class Meta:
    model = Product
'''
def randstring(n):
    b=string.ascii_letters + string.digits
    return ''.join([random.choice(b) for i in range(n)])

def base (request):
    categ=Category.objects.all()
    str=reverse('base')
    return render(request, 'myapp/base.html', {'category': categ} )

@login_required
def profile(request):
    user=request.user
    user_id=user.id
    comments=Comment.objects.filter(user_id=user_id)
    buyer=Buyer.objects.get(user_id=user_id)
    orders=Order.objects.filter(buyer_id=buyer.id).annotate(nums=Count('orderposition'))
    #positions = OrderPosition.objects.filter(order__pk=order.id)
    formbuy=BuyForm()
    return render(request, 'myapp/profile.html',{'orders':orders,'comments':comments, 'buyer':buyer, 'formbuy':formbuy})

def register(request):
    form=UserForm(request.POST)
    if form.is_valid():
        form.save
    return render(
        request, 'registration/register.html',{'form':form}
    )

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/registration/logged_out.html")

def search(request, products=None):

    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        try:
            product = Product.objects.get(name=q)
        except Product.DoesNotExist:
            raise Http404()
        comments = Comment.objects.filter(Q(content_type_id=5)&Q(object_id=product.id))
        return render(request, 'myapp/product.html', {'product': product, 'comments': comments})
        if 'search_type' in request.GET and request.GET['search_type']:
            type=request.GET['search_type']
        if (type=="Normal"):
            return render(request, 'myapp/product.html', {'product': product,'comments':comments} )
        else:
            all_objects = list(products) + list(comments)
            data = serializers.serialize('json', all_objects)
            return HttpResponse(data)
       # message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
def catalog(request):
    if 'page' in request.GET and request.GET['page']:
        page=request.GET['page']
        a=0
        b=0
        if (int(page)==1):
            a = 0
            b=20
        else:
            a = (int(page) - 1) * 20
            b = a + 20


        products=Product.objects.all()[a:b].annotate(num_comments=Count('comments'))
    #a =(int(page))
    #b = random.randint(100, 200)
    #while (a >= b):
    #    b = random.randint(100, 200)
    #products = Product.objects.all()[0:20]
    #get_param = request.GET.get('example', 'EMPTY')
    else:
        products = Product.objects.all()[:20].annotate(num_comments=Count('comments'))
        #count=Product.objects.aggregate(Count('comments'))
        #annotated = generic_annotate(Product.objects.all(), Comment, Count('comments__id'))
        #generic_annotate(products, Comment, Count('comments_id'), alias='avg')
    return render(request, 'myapp/catalog.html', {'products': products})
    if 'catalog_type' in request.GET and request.GET['catalog_type']:
        type = request.GET['catalog_type']
        if (type=="Normal"):
            return render(request, 'myapp/catalog.html', {'products': products})
        else:
            data = serializers.serialize('json', products)
            return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("Что-то пошло не так")

def ajaxcatalog (request):
    if 'page' in request.GET and request.GET['page']:
        page=request.GET.get('page')
        a=0
        b=0
        if (int(page)==1):
            a = 0
            b=20
        else:
            a = (int(page) - 1) * 20
            b = a + 20
        products=Product.objects.all()[a:b].annotate(num_comments=Count('comments')).values()
        category=Category.objects.all().values()
        #products_dict=Product.objects.values()[a:b].annotate(num_comments=Count('comments'))
        data = json.dumps((list(products)+list(category)), cls=DjangoJSONEncoder)
        """
        author_count = serializers.IntegerField(
            source='products.num_comments',
            read_only=True
        )
        """
        #data = serializers.serialize('json', (list(products)+list(category)))
        return HttpResponse(data)
    else:
        return HttpResponse("Bad")

    #a =(int(page))
    #b = random.randint(100, 200)
    #while (a >= b):
    #    b = random.randint(100, 200)
    #products = Product.objects.all()[0:20]
    #get_param = request.GET.get('example', 'EMPTY')

        #products = Product.objects.all()[:20].annotate(num_comments=Count('comments'))
        #count=Product.objects.aggregate(Count('comments'))
        #annotated = generic_annotate(Product.objects.all(), Comment, Count('comments__id'))
        #generic_annotate(products, Comment, Count('comments_id'), alias='avg')
    #return render(request, 'myapp/catalog.html', {'products': products})
    '''if 'catalog_type' in request.GET and request.GET['catalog_type']:
        type = request.GET['catalog_type']
        if (type=="Normal"):
            return render(request, 'myapp/catalog.html', {'products': products})
        else:

    else:
        return HttpResponse("Что-то пошло не так")'''
'''
def catalog(request):
    if 'page' in request.GET and request.GET['page']:
        page=request.GET['page']
        a=0
        b=0
        if (int(page)==1):
            a = 0
            b=20
        else:
            a = (int(page) - 1) * 20
            b = a + 20


        products=Product.objects.all()[a:b].annotate(num_comments=Count('comments'))
    else:
        products = Product.objects.all()[:20].annotate(num_comments=Count('comments'))
    return render(request, 'myapp/catalog.html', {'products': products})
    if 'catalog_type' in request.GET and request.GET['catalog_type']:
        type = request.GET['catalog_type']
        if (type=="Normal"):
            return render(request, 'myapp/catalog.html', {'products': products})
        else:
            data = serializers.serialize('json', products)
            return HttpResponse(data)
    else:
        return HttpResponse("Что-то пошло не так")

'''
def search_category(request):
    categ = Category.objects.all()
    comments = Comment.objects.filter(content_type_id=5)

    if 'org_list' in request.GET and request.GET['org_list']:
        message = request.GET['org_list']
        request.session[0] = message
        category=Category.objects.filter(category=message)
        category_id=(category[0]).id
        #deep_message = message
        #message=message[:1]
        #str(message).upper()
        if 'page' in request.GET and request.GET['page']:
            page = request.GET['page']
            a = 0
            b = 0
            if (int(page) == 1):
                a = 0
                b = 20
            else:
                a = (int(page) - 1) * 20
                b = a + 20
            #return HttpResponse(page)
            products = Product.objects.filter(category_id=category_id)[a:b]

        else:
            products = Product.objects.filter(category_id=category_id)[0:20]

            # a =(int(page))
            # b = random.randint(100, 200)
            # while (a >= b):
            #    b = random.randint(100, 200)
            # products = Product.objects.all()[0:20]
            # get_param = request.GET.get('example', 'EMPTY')
        products = products.annotate(num_comments=Count('comments'))
        return render(request, 'myapp/search_category.html',
                      {'products': products, 'message': message, 'category': categ})
        if 'search_type_categ' in request.GET and request.GET['search_type_categ']:
            type = request.GET['search_type_categ']
            if (type == "Normal"):
                return render(request, 'myapp/search_category.html',
                              {'products': products, 'message': message, 'category': categ})
            else:
                all_data=list(products)
                data = serializers.serialize('json', all_data)
                return HttpResponse(data)
        else:
            return render(request, 'myapp/search_category.html',
                          {'products': products, 'message': message, 'category': categ})
    else:
        message="You aren't chose anything"
        return HttpResponse(message),
def ajaxsearch_category(request):
    categ = Category.objects.all()
    comments = Comment.objects.filter(content_type_id=5)

    if 'org_list' in request.GET and request.GET['org_list']:
        message = request.GET['org_list']
        request.session[0] = message
        category=Category.objects.filter(category=message)
        category_id=(category[0]).id
        #deep_message = message
        #message=message[:1]
        #str(message).upper()
        if 'page' in request.GET and request.GET['page']:
            page = request.GET['page']
            a = 0
            b = 0
            if (int(page) == 1):
                a = 0
                b = 20
            else:
                a = (int(page) - 1) * 20
                b = a + 20
            #return HttpResponse(page)
            products = Product.objects.filter(category_id=category_id)[a:b].annotate(num_comments=Count('comments')).values()

        else:
            products = Product.objects.filter(category_id=category_id)[0:20].annotate(num_comments=Count('comments')).values()

            # a =(int(page))
            # b = random.randint(100, 200)
            # while (a >= b):
            #    b = random.randint(100, 200)
            # products = Product.objects.all()[0:20]
            # get_param = request.GET.get('example', 'EMPTY')
        #products = Product.objects.all()[a:b].annotate(num_comments=Count('comments')).values()
        #products = products.annotate(num_comments=Count('comments'))
        cat=Category.objects.all().values()
        data = json.dumps((list(products) + list(cat)), cls=DjangoJSONEncoder)
        return HttpResponse(data)
    else:
        message="You aren't chose anything"
        return HttpResponse(message)
def register_buyer(request):
    if 'username' in request.POST and request.POST['username']:
        username=request.POST['username']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'pwd' in request.POST and request.POST['pwd']:
        password= request.POST['pwd']
    else:
        return HttpResponse("Введите пароль")
    if 'fist_name' in request.POST and request.POST['fist_name']:
        first_name= request.POST['fist_name']
    else:
        return HttpResponse("Введите ваше имя")
    if 'last_name' in request.POST and request.POST['last_name']:
        last_name= request.POST['last_name']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'email' in request.POST and request.POST['email']:
        email= request.POST['email']
    else:
        return HttpResponse("Введите email")
    if 'phone' in request.POST and request.POST['phone']:
        phone = request.POST['phone']
    else:
        return HttpResponse("Введите ваш номер телефона")
    if 'city' in request.POST and request.POST['city']:
        city = request.POST['city']
    else:
        return HttpResponse("Введите город")
    if 'street' in request.POST and request.POST['street']:
        street = request.POST['street']
    else:
        return HttpResponse("Введите город")
    if 'house' in request.POST and request.POST['house']:
        house = request.POST['house']
    else:
        return HttpResponse("Введите номер дома")
    if 'apartment' in request.POST and request.POST['apartment']:
        apartment = request.POST['apartment']
    else:
        return HttpResponse("Введите номер квартиры")

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, )
    user.set_password(str(password))
    user.save()
    address=Address(city=city,street=street,house=house,apartment=apartment,)
    address.save()
    user_saved=User.objects.filter(username=username)
    address_saved=Address.objects.filter(Q(city=city)&Q(street=street)&Q(house=house)&Q(apartment=int(apartment)))
    user_saved = User.objects.filter(username=username)
    buyer=Buyer( user_id=int((user_saved[0]).id), phone=phone, address_id=int((address_saved[0]).id), )
    buyer.save()
    buyer_saved = Buyer.objects.filter(Q(phone=phone)&Q(user_id=int((user_saved[0]).id))&Q(address_id=int((address_saved[0]).id)))
    return render(request, 'myapp/register_compl.html',{'str':str(buyer_saved[0].id)})


def product_detail(request,id):
    product = get_object_or_404(Product, id=id)
    comments = Comment.objects.filter(content_type_id=5).filter(object_id=product.id)
    return render(request,'myapp/product.html',{'product':product,'comments':comments})

    #comments = Comment.objects.filter(Q(content_type_id=3) & Q(object_id=product.id))
    #if request.session.get('products', False):
    #    string=request.session['products']
    #    string=string+" "+str(product.name)
    #    request.session['products'] =string
    #    string1=request.session['products_id']
    #    string1 =string+" "+str(product.id)
    #    request.session['products_id'] =string1
    #else:
    #    request.session['products'] =str(product.name)
    #    request.session['products_id'] = str(product.id)
    #return render(request, 'myapp/product_detail.html', {'product': product, 'comments': comments})

def buy(request,id):
    user = request.user
    user_id = user.id
    buyer = Buyer.objects.get(user_id=user_id)
    orders=Order.objects.filter(buyer_id=buyer.id)
    product=Product.objects.get(id=id)
    #id_false_valid_order=0
    #for order in orders:
    #    if (order.is_valid==False):
    #        id_false_valid_order=order.id
    #if (id_false_valid_order==0):
    #    order=Order(buyer_id=buyer.id, is_valid=True, closed_at=None, phone=random.randint(1, 10000), name=randstring(20), ))
    #
    id_order=0
    if "id_order" in request.session:
        id_order=request.session["id_order"]

    else:
        name = randstring(20)
        order=Order(buyer_id=buyer.id, is_valid=False, closed_at=None, phone=random.randint(1, 10000), name=name)
        order.save()
        order=Order.objects.get(name=name)
        id_order=order.id
        request.session["id_order"]=order.id


    order = Order.objects.get(id=id_order)
    positions=OrderPosition.objects.filter(order__pk=order.id)
    count=1
    for position in positions:
        if (position.product_id==product.id):
            count=count+position.count
            OrderPosition.objects.filter(id=position.id).update(count=count)
            return HttpResponse(count)
    if (count==1):
        order_pos=OrderPosition(order_id=order.id, product_id=product.id, count=1)
        order_pos.save()
    categ = Category.objects.all()
    return render(request, 'myapp/base.html', {'category': categ})

def buy_cart(request,id):
    user = request.user
    user_id = user.id
    buyer = Buyer.objects.get(user_id=user_id)
    order=Order.objects.filter(id=id).update(is_valid=True)
    del request.session["id_order"]
    comments = Comment.objects.filter(user_id=user_id)
    orders = Order.objects.filter(buyer_id=buyer.id).annotate(nums=Count('orderposition'))

    return render(request, 'myapp/profile.html',{'orders':orders,'comments':comments })

def addcomment(request, id):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        user = request.user
        user_id = user.id
        comment=Comment(user_id=user_id, object_id=id, content_type_id=5,  content=q,)
        comment.save()
        product = get_object_or_404(Product, id=id)
        comments = Comment.objects.filter(content_type_id=5).filter(object_id=product.id)
        return render(request, 'myapp/product.html', {'product': product, 'comments': comments})

def ajaxaddcomment(request, id):
    if 'q' in request.POST and request.POST['q']:
        q=request.POST['q']
        user = request.user
        user_id = user.id
        buyer=Buyer.objects.get(user_id=user_id)
        comment=Comment(user_id=buyer.id, object_id=id, content_type_id=5,  content=q,)
        comment.save()
        product = get_object_or_404(Product, id=id)
        comments = Comment.objects.filter(content_type_id=5).filter(object_id=product.id).values()
        data = json.dumps(list(comments), cls=DjangoJSONEncoder)
        return HttpResponse(data)

def about(request):
    return render(request, 'myapp/about.html')



def ajaxregister_buyer(request):
    print(request.POST['last_name']);
    if 'username' in request.POST and request.POST['username']:
        username=request.POST['username']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'pwd' in request.POST and request.POST['pwd']:
        password= request.POST['pwd']
    else:
        return HttpResponse("Введите пароль")
    if 'first_name' in request.POST and request.POST['first_name']:
        first_name= request.POST['first_name']
    else:
        return HttpResponse("Введите ваше имя")
    if 'last_name' in request.POST and request.POST['last_name']:
        last_name= request.POST['last_name']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'email' in request.POST and request.POST['email']:
        email= request.POST['email']
    else:
        return HttpResponse("Введите email")
    if 'phone' in request.POST and request.POST['phone']:
        phone = request.POST['phone']
    else:
        return HttpResponse("Введите ваш номер телефона")
    if 'city' in request.POST and request.POST['city']:
        city = request.POST['city']
    else:
        return HttpResponse("Введите город")
    if 'street' in request.POST and request.POST['street']:
        street = request.POST['street']
    else:
        return HttpResponse("Введите город")
    if 'house' in request.POST and request.POST['house']:
        house = request.POST['house']
    else:
        return HttpResponse("Введите номер дома")
    if 'apartment' in request.POST and request.POST['apartment']:
        apartment = request.POST['apartment']
    else:
        return HttpResponse("Введите номер квартиры")

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, )
    user.set_password(str(password))
    user.save()
    address=Address(city=city,street=street,house=house,apartment=apartment,)
    address.save()
    user_saved=User.objects.filter(username=username)
    address_saved=Address.objects.filter(Q(city=city)&Q(street=street)&Q(house=house)&Q(apartment=int(apartment)))
    user_saved = User.objects.filter(username=username)
    user_saved_for_form = User.objects.filter(username=username).values()
    buyer=Buyer( user_id=int((user_saved[0]).id), phone=phone, address_id=int((address_saved[0]).id), )
    buyer.save()
    buyer_saved = Buyer.objects.filter(Q(phone=phone)&Q(user_id=int((user_saved[0]).id))&Q(address_id=int((address_saved[0]).id))).values()
    data = json.dumps(list(buyer_saved)+list(user_saved_for_form), cls=DjangoJSONEncoder)
    return HttpResponse(data)



def ajaxchange_buyer(request):
    user = request.user
    user_id = user.id
    user= User.objects.get(id=user_id)
    buyer = Buyer.objects.get(user_id=user_id)

    if 'first_name' in request.POST and request.POST['first_name']:
        user.first_name= request.POST['first_name']
    if 'last_name' in request.POST and request.POST['last_name']:
        user.last_name= request.POST['last_name']
    if 'email' in request.POST and request.POST['email']:
        user.email= request.POST['email']
    if 'phone' in request.POST and request.POST['phone']:
        buyer.phone = request.POST['phone']
    user.save()
    buyer.save()
    user = User.objects.filter(id=user_id).values()
    buyer = Buyer.objects.filter(user_id=user_id).values()
    data = json.dumps(list(buyer)+list(user), cls=DjangoJSONEncoder)
    return HttpResponse(data)

def ajaxbuy(request,id):
    user = request.user
    user_id = user.id
    buyer = Buyer.objects.get(user_id=user_id)
    orders=Order.objects.filter(buyer_id=buyer.id)
    product=Product.objects.get(id=id)
    #id_false_valid_order=0
    #for order in orders:
    #    if (order.is_valid==False):
    #        id_false_valid_order=order.id
    #if (id_false_valid_order==0):
    #    order=Order(buyer_id=buyer.id, is_valid=True, closed_at=None, phone=random.randint(1, 10000), name=randstring(20), ))
    #
    id_order=0
    if "id_order" in request.session:
        id_order=request.session["id_order"]

    else:
        name = randstring(20)
        order=Order(buyer_id=buyer.id, is_valid=False, closed_at=None, phone=random.randint(1, 10000), name=name)
        order.save()
        order=Order.objects.get(name=name)
        id_order=order.id
        request.session["id_order"]=order.id


    order = Order.objects.get(id=id_order)
    positions=OrderPosition.objects.filter(order__pk=order.id)
    count=1
    for position in positions:
        if (position.product_id==product.id):
            count=count+position.count
            OrderPosition.objects.filter(id=position.id).update(count=count)
            #return HttpResponse(count)
    if (count==1):
        order_pos=OrderPosition(order_id=order.id, product_id=product.id, count=1)
        order_pos.save()
    categ = Category.objects.all()
    return HttpResponse(order.id)


def formregister(request):

        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("Hello")
            # create a form instance and populate it with data from the request:
        form = RegistrationForm(request.POST)
            # check whether it's valid:
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            house = form.cleaned_data['house']
            apartment = form.cleaned_data['apartment']

            user = User(username=username, email=email, first_name=first_name, last_name=last_name, )
            user.set_password(str(password))
            user.save()
            address = Address(city=city, street=street, house=house, apartment=apartment, )
            address.save()
            user_saved = User.objects.filter(username=username)
            address_saved = Address.objects.filter(Q(city=city) & Q(street=street) & Q(house=house) & Q(apartment=int(apartment)))
            user_saved = User.objects.filter(username=username)
            user_saved_for_form = User.objects.filter(username=username).values()
            buyer = Buyer(user_id=int((user_saved[0]).id), phone=phone, address_id=int((address_saved[0]).id), )
            buyer.save()
            buyer_saved = Buyer.objects.filter(
                Q(phone=phone) & Q(user_id=int((user_saved[0]).id)) & Q(address_id=int((address_saved[0]).id)))
            # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
            return HttpResponse((buyer_saved[0]).id)
        errors = form.errors
        return HttpResponse(json.dumps(errors))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistrationForm()

    return render(request, 'myapp/name.html', {'form': form})

def formbuy(request, id):
    if request.method == 'POST':
        formbuy = BuyForm(request.POST)
        if formbuy.is_valid():
            user = request.user
            user_id = user.id
            buyer = Buyer.objects.get(user_id=user_id)
            order = Order.objects.filter(id=id).update(is_valid=True)
            order = Order.objects.filter(id=id).update(name=formbuy.cleaned_data['text'])
            del request.session["id_order"]
            orders = Order.objects.filter(buyer_id=buyer.id).annotate(nums=Count('orderposition')).values()
            data=json.dumps(list(orders), cls=DjangoJSONEncoder)
            return HttpResponse(data)
    errors=formbuy.errors
    return HttpResponse(json.dumps(errors))

    '''print(request.POST['last_name']);
    if 'username' in request.POST and request.POST['username']:
        username=request.POST['username']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'pwd' in request.POST and request.POST['pwd']:
        password= request.POST['pwd']
    else:
        return HttpResponse("Введите пароль")
    if 'first_name' in request.POST and request.POST['first_name']:
        first_name= request.POST['first_name']
    else:
        return HttpResponse("Введите ваше имя")
    if 'last_name' in request.POST and request.POST['last_name']:
        last_name= request.POST['last_name']
    else:
        return HttpResponse("Введите имя пользователя")
    if 'email' in request.POST and request.POST['email']:
        email= request.POST['email']
    else:
        return HttpResponse("Введите email")
    if 'phone' in request.POST and request.POST['phone']:
        phone = request.POST['phone']
    else:
        return HttpResponse("Введите ваш номер телефона")
    if 'city' in request.POST and request.POST['city']:
        city = request.POST['city']
    else:
        return HttpResponse("Введите город")
    if 'street' in request.POST and request.POST['street']:
        street = request.POST['street']
    else:
        return HttpResponse("Введите город")
    if 'house' in request.POST and request.POST['house']:
        house = request.POST['house']
    else:
        return HttpResponse("Введите номер дома")
    if 'apartment' in request.POST and request.POST['apartment']:
        apartment = request.POST['apartment']
    else:
        return HttpResponse("Введите номер квартиры")

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, )
    user.set_password(str(password))
    user.save()
    address=Address(city=city,street=street,house=house,apartment=apartment,)
    address.save()
    user_saved=User.objects.filter(username=username)
    address_saved=Address.objects.filter(Q(city=city)&Q(street=street)&Q(house=house)&Q(apartment=int(apartment)))
    user_saved = User.objects.filter(username=username)
    user_saved_for_form = User.objects.filter(username=username).values()
    buyer=Buyer( user_id=int((user_saved[0]).id), phone=phone, address_id=int((address_saved[0]).id), )
    buyer.save()
    buyer_saved = Buyer.objects.filter(Q(phone=phone)&Q(user_id=int((user_saved[0]).id))&Q(address_id=int((address_saved[0]).id))).values()
    data = json.dumps(list(buyer_saved)+list(user_saved_for_form), cls=DjangoJSONEncoder)
    return HttpResponse(data)'''




