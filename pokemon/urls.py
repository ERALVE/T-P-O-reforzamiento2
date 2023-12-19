from django.urls import path
from . import views

urlpatterns = [
    path('pokemon_list/', views.pokemon_list, name='pokemon_list')

]