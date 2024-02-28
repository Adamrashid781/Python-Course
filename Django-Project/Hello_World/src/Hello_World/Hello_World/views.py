


from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile 

def home(request):
    user = request.user
    profile = Profile.objects.all()
    print(user)
    #return HttpResponse("<h1>Hello {}!</h1>".format(user))
    names = {'Adam', 'Tutu', 'Alex', 'John', 'Sally'}
    context = {
        # 'user': user
        # 'names' : names
        'profile': Profile
        
    }
    print(context)
    print(profile)
    # return render(request, 'home.html', context)
    return render(request, 'home.html', context)


