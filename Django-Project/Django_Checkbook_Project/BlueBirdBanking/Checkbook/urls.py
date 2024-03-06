from django.urls import path
from . import views

urlpatterns = [
    # Sets the url for the home page
    path('', views.home, name='index'),
    
    # sets the url path to Create New Account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    
    # sets the url path to Balance sheet page BalanceSheet.html
    path('balance/', views.balance, name='balance'),

    # sets the url path to Transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction'),
]
