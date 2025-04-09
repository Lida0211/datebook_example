from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('profil')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required  
def protected_view(request):
    return render(request, 'protected.html')