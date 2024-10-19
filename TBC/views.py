from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from ChemiSivrce.models import Profile
from django.contrib.auth import login


def home_view(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, balance=0.0)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
