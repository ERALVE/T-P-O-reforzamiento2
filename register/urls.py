from django.urls import path
from . import views

urlpatterns = [
    path('register_list/', views.register_list, name='register_list')

]