"""
URL configuration for hosptal_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from webpage.views import *

urlpatterns = [
    path('admin', admin.site.urls),
    path('home', index, name='index'),
    path('contact', contact, name='contact'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
<<<<<<< HEAD
    path('error', error, name='error')
=======
>>>>>>> c5086efc209da7ebea1a51e7b15374339758b831
]