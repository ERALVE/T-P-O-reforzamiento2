from django.urls import path
from . import views

urlpatterns = [
    path('catalog_list/', views.catalog_list, name='catalog_list')

]