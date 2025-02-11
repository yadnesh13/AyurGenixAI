from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings  # Import settings for email configuration
import json

from .forms import ContactForm, UserProfileForm
from .models import ChatMessage, UserProfile
from home.utils.ai_response import generate_ayurvedic_response


def landing_page(request):
    return render(request, "home/index.html")

def about(request):
    context = {'page': 'About'}
    return render(request, "home/about.html", context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Ensure email backend is configured correctly in settings.py
            send_mail(
                f"Message from {name}",
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # Use configured email instead of hardcoded one
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('landing_page')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('landing_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('landing_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'home/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('make_profile')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Please complete your profile.')
            return redirect('make_profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'home/register.html', {'form': form})

@login_required
def make_profile(request):
    # Get or create the profile without tuple unpacking
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('landing_page')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'home/make_profile.html', {'form': form})

@login_required
def chat_page(request):
    return render(request, 'chat/chat_page.html')

@login_required
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').strip()
            
            if not user_message:
                return JsonResponse({'error': 'Message cannot be empty'}, status=400)
            
            # Store user message
            ChatMessage.objects.create(
                user=request.user,
                message=user_message,
                is_ai=False
            )
            
            # Get AI response
            ai_response = generate_ayurvedic_response(user_message)
            
            # Store AI response
            ChatMessage.objects.create(
                user=request.user,
                message=ai_response,
                is_ai=True
            )
            
            return JsonResponse({
                'status': 'success',
                'response': ai_response
            })
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@login_required
def get_chat_history(request):
    try:
        messages = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
        chat_history = [{
            'message': msg.message,
            'is_ai': msg.is_ai,
            'timestamp': msg.timestamp.isoformat()
        } for msg in messages]
        
        return JsonResponse({'history': chat_history})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')
