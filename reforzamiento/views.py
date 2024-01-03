from django.shortcuts import render
from .models import Reforzamiento

def reforzamiento_list(request):
    data_context = Reforzamiento.objects.all()
    return render(request, 'reforzamiento_list_template.html', context={'data': data_context})
