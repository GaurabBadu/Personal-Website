from django.urls import path, include
from travello import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.index, name='index'),  # Homepage
    # path('', views.homePage, name='header'),  # Home page
    path('about/', views.About, name='about'),  # About page
    path('experience/', views.Experience, name='experience'),  # Experience page
    path('projects/', views.Projects, name='projects'),  # Projects page
    path('travello/', include('travello.urls')), # Include 'travello' app's URL
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
