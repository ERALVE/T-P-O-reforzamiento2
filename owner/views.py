from django.shortcuts import render

# Create your views here.

def owner_list(request):

    data_context = {
        'nombre': 'Thania Peralta',
        'edad': 17,
        'dni':"98745612",
        'pais': "Perú",
        'vigente': False,

    }
    return render(request,'owner_list.html',  context={'data': data_context})
