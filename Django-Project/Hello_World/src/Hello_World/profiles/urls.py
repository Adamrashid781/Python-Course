from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_console', views.admin_console, name = 'admin_console'),
    path('<int:pk>/details/', views.details, name = 'details'),
    path('createRecord/', views.createRecord, name = 'createRecord'),
    path('<int:pk>/deleteProfile/', views.deleteProfile, name = 'deleteProfile'),
    path('confirmDelete/', views.confirmDelete, name = 'confirmDelete'),
]