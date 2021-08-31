"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import *
from django.urls import path, re_path
from django.views.generic import TemplateView
from firstapp.views import search
# RegisterUser, LoginView, ProfilePage
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView

from firstapp import views

from firstapp.views import data_table


# Uncomment the next two lines to enable the admin:

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('search/', search.as_view(), name='search_results'),
    path('map/', views.map, name='map'),
    path('edit/<int:id>/', views.edit, name='edit_page'),
    re_path(r'^about/$',views.about),
    path('contact/', TemplateView.as_view(template_name="contact.html")),



    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),


    path('profile/', views.profile, name='profile'),
   # path('about/', TemplateView.as_view(template_name="about.html")),
   # path('contact/', TemplateView.as_view(template_name="firstapp/contact.html")),
    

    path('admin/', admin.site.urls),
    path('index_test/', data_table.as_view()),
]





"""urlpatterns = [

    path('', views.mainpage),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),

]
"""





"""urlpatterns = [

    re_path(r'^products/$', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),

    re_path(r'^users/$', views.users),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),

]
"""



"""urlpatterns = [

    re_path(r'^about/contact', views.contact),
    re_path(r'^about', views.about),
    path('', views.index),
    
]
"""