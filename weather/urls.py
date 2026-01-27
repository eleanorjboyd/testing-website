from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_weather, name='search_weather'),
    path('random/', views.random_weather, name='random_weather'),
    path('about/', views.about, name='about'),
]
