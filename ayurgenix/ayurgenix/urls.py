from django.contrib import admin
from django.urls import path
from home import views  # Explicitly import views from the home app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),  # Home page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('about/', views.about, name='about'),  # About page
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Register page
    path('logout/', views.logout_view, name='logout'),  # Logout view
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
