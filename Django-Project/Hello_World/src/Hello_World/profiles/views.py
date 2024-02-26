from django.shortcuts import render

# Create your views here.
def admin_console(request):
    return render(request, 'profiles/profiles_page.html')