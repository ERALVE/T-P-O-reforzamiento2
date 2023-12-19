from django.shortcuts import render

# Create your views here.

def register_list(request):

    data_context = {
        'nombre': 'Charizard',
        'tipo': "Fuego",
        'genero': "M",

    }


    return render(request,'register_list.html',  context={'data': data_context})