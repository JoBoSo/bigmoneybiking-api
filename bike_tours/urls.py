"""bike_tours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bike_tours import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/bike_tours/', views.bike_tours),
    path('api/bike_tours/<str:name>/', views.bike_tour),
    path('api/bike_tour_pages/', views.bike_tour_pages),
    path('api/bike_tour_pages/<str:bike_tour>/', views.bike_tour_page),
    path('api/bike_tour_cards/', views.bike_tour_cards),
    path('api/bike_tour_cards/<str:bike_tour>/', views.bike_tour_card),
]

if settings.DEBUG:
    urlpatterns += static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
