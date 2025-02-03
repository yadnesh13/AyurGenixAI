from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm 


def landing_page(request):
    return render(request, "home/index.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data (e.g., send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # ... send email logic ...
            return redirect('landing_page')  # Redirect to a success page

    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('landing_page')  # Redirect authenticated users to the homepage

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('landing_page')  # Redirect to the homepage
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home/login.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm  # You'll create this form next

# @login_required  # Ensure only authenticated users can access this page
# def make_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = request.user  # Associate the profile with the logged-in user
#             profile.save()
#             messages.success(request, 'Profile updated successfully!')
#             return redirect('landing_page')  # Redirect to the homepage after profile creation
#         else:
#             print(form.errors)  # Print form errors for debugging
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = ProfileForm()
#     return render(request, 'home/make_profile.html', {'form': form})    

def register_view(request):
    if request.user.is_authenticated:
        return redirect('make_profile')  # Redirect authenticated users to the profile page

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Account created successfully! Please complete your profile.')
            return redirect('make_profile')  # Redirect to the profile creation page
        else:
            print(form.errors)  # Print form errors for debugging
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email (optional)
            send_mail(
                f"Message from {name}",
                message,
                email,
                ['your_email@example.com'],  # Replace with your email
                fail_silently=False,
            )

            return redirect('success_page')  # Redirect to a success page or same page with a success message

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')  # Redirect to the login page after logout