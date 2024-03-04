
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views 

urlpatterns = [
    path('admin_console', views.admin_console, name = 'admin_console'),
    path('<int:pk>/details/', views.details, name = 'details'),
    path('createRecord/', views.createRecord, name = 'createRecord'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('confirmDelete/', views.confirmed, name = 'confirmed'), 
    
]

