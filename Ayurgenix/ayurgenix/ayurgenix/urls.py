from django.contrib import admin
from django.urls import path  # Removed unused `include`
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name='landing_page'),
    path('contact/', views.contact_view, name='contact_page'), 
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    # path('make_profile/', views.make_profile, name='make_profile'),  # Uncomment if needed
    # path('make_profile/', make_profile_view, name='make_profile'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
