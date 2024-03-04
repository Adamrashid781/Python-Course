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
        return render(request, 'profile_details_page.html', {'form': form})

def createRecord(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else: 
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'createRecord.html', context)

def deleteProfile(request, pk): 
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {
        'item': item
        }
    print(item.Username)
    return render(request, 'confirmDelete.html', context)

def confirmDelete(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST or None)

        # Check whether it's valid:
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')