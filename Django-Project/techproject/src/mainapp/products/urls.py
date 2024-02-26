
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views 

urlpatterns = [
    path('admin_console', views.admin_console, name = 'admin_console'),

]

