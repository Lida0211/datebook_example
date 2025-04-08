from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from main.models import PersonalData
from main.forms import PersonalDataForm
from django.contrib import messages
# Create your views here.

def profil(request):
    template = loader.get_template("main/profil.html")
    profil = PersonalData.objects.all()
    context = {"profil":profil}
    return HttpResponse(template.render(context, request))


def index_main(request):
    
    return render(request, "main/index_main.html")

def otobr(request):
    return render(request, "registration/login.html")


def col(request):
    return render(request, "main/col.html")

def edit_profil (request):
    profile = get_object_or_404(PersonalData, pk=1)
    
    if request.method == 'POST':
        form = PersonalDataForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = PersonalDataForm(instance=profile)
    
    return render(request, 'main/edit_profil.html', {'form': form})