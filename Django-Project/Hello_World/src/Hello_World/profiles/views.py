from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse 
from .models import Profile 
from .forms import ProfileForm


# Create your views here.
def admin_console(request):
    Profiles = Profile.objects.all()
    context = {'Profiles': Profiles}
    return render(request, 'profiles_page.html', context)


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data = request.POST or None, instance=item)
    if request.method == "POST":
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_page.html', {'form': form})