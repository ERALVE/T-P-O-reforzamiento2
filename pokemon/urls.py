from django.urls import path
from . import views

urlpatterns = [
    path('pokemon_list/', views.pokemon_list, name='pokemon_list'),
    path('pokemon_orm/', views.pokemon_orm, name='pokemon_orm'),
]