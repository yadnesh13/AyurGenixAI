from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views  # Importing views from the home app

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Main pages
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact_page'), 

    # Authentication & User Profile
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('make_profile/', views.make_profile, name='make_profile'),  

    # Chatbot API Endpoints
    path('chat/', views.chat_page, name='chat_page'),
    path('api/send-message/', views.send_message, name='send_message'),
    path('api/get-chat-history/', views.get_chat_history, name='get_chat_history'),
]

# Serve static and media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
