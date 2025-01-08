from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def landing_page(request):
    return render(request, "home/index.html")

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "home/contact.html", context)

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing_page')  # Redirect to the homepage
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'home/login.html')
    return render(request, 'home/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout
