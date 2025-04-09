from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from main.models import PersonalData
from main.forms import PersonalDataForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
# Create your views here.

def profil(request):

    if isinstance(request.user, AnonymousUser):
        return render(request, "main/profil.html", {"is_anonymous": True})
    
    try:
        profile = PersonalData.objects.get(user=request.user)
        context = {"profil": profile, "is_anonymous": False}
    except PersonalData.DoesNotExist:
        context = {"profil": None, "is_anonymous": False}
    
    return render(request, "main/profil.html", context)


def index_main(request):
    
    return render(request, "main/index_main.html")

def col(request):
    return render(request, "main/col.html")

@login_required
def edit_profil(request):
    profile, created = PersonalData.objects.get_or_create(
        user=request.user,
        defaults={'name': '', 'surname': ''} 
    )
    
    if request.method == 'POST':
        form = PersonalDataForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user 
            instance.save()
            return redirect('profil')
    else:
        form = PersonalDataForm(instance=profile)
    
    return render(request, 'main/edit_profil.html', {'form': form})
