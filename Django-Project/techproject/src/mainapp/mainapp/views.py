from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    # This prints the username of the logged in user into the command line
    # user = request.user
    products = {"Cherries", "Apples", "Bananas", "strawberries", "Grapes", "Oranges"}
    context = {
        'products': products,
    }
    # print(user)
    
    return render(request, 'home.html', context )