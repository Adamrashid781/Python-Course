from django.shortcuts import render
from .models import Profile 

# Create your views here.
def admin_console(request):
    profile = Profile.objects.all()
    return render(request, 'profiles_page.html', {'profile': profile})


