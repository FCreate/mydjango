"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.conf.urls import include
from myapp.views import base
from myapp.views import profile
from myapp.views import register
from myapp.views import logout
from myapp.views import search
from myapp.views import catalog
from myapp.views import search_category
from myapp.views import product_detail
from myapp.views import register_buyer
from myapp.views import buy
from myapp.views import buy_cart
from myapp.views import ajaxcatalog
from myapp.views import ajaxsearch_category
from myapp.views import addcomment
from myapp.views import about
from myapp.views import ajaxaddcomment
from myapp.views import ajaxregister_buyer
from myapp.views import ajaxchange_buyer
from myapp.views import ajaxbuy
from myapp.views import formregister
from myapp.views import formbuy


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^(?P<page>[0-100000]+)/$', base, name='base'),
    url(r'^$', base, name='base'),
    #url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^accounts/profile/(\d+)$', profile, name='profile'),
    url(r'^accounts/profile/(\d+)/buy$', buy_cart, name='buy_cart'),
    url(r'^accounts/profile/$', profile, name='profile_not_setup'),
    url(r'^register/$', register, name='register'),
    url(r'^search/$', search),
    url(r'^catalog/$', catalog),
    url(r'^search_category/$',search_category),
    url(r'^product_detail/(\d+)$',product_detail, name='product_detail'),
    url(r'^product_detail/buy/(\d+)$', buy, name='product_detail_buy'),
    url(r'^register_buyer/$', register_buyer),
    url(r'^ajaxcatalog/$', ajaxcatalog, name='ajaxcatalog'),
    url(r'^ajaxsearch_category/$', ajaxsearch_category, name='ajaxsearch_category'),
    url(r'^addcomment/(\d+)/$', addcomment,name='addcomment' ),
    url(r'^ajaxaddcomment/(\d+)/$', ajaxaddcomment,name='ajaxaddcomment' ),
    url(r'^about/$', about, name='about'),
    url(r'^ajaxregister_buyer/$', ajaxregister_buyer, name='ajaxregister_buyer'),
    url(r'^ajaxchange_buyer/$', ajaxchange_buyer, name='ajaxchange_buyer'),
    url(r'^ajaxbuy/(\d+)$', ajaxbuy, name='ajaxbuy'),
    url(r'^formregister/$', formregister, name='formregister'),
    url(r'^formbuy/(\d+)$', formbuy, name='formbuy')
    #url(r'^buy/$', buy),
    # url(r'^users/login/$', auth_views.login, {'template_name': 'login.html'}),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^login/$', auth_views.login, name="login"),
    # url('^', include('django.contrib.auth.urls')),
]