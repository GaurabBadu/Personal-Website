from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Home page of the 'travello' app
    path('home/', views.homePage, name='home'),  # Home page
    path('about/', views.About, name='about'),  # About page
    path('experience/', views.Experience, name='experience'),  # Experience page
    path('projects/', views.Projects, name='projects'),  # Projects page
    path('contact/', views.contact, name='contact'),  # Projects page
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
