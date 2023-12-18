from django.shortcuts import render

# Create your views here.

def catalog_list(request):

    data_context = {
        'nombre': 'Katy Paredes',
        'edad': 20 ,
        'dni':"12345678",
        'pais': "Perú",
        'vigente': False,

    }


    return render(request,'catalog_list.html',  context={'data': data_context})