from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from . forms import CustomUserCreationForm, CustomAuthenticationForm


# Create your views here.

def ProfileView(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request, 'profile.html', context)

def LogoutView(request):
    logout(request)
    return redirect('home')

def LoginView(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = CustomAuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def Registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration.html', context)
