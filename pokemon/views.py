from django.shortcuts import render

# Create your views here.

def pokemon_list(request):

    data_context = {
        'nombre': 'Pikachu',
        'tipo':  'Electrico',
        'genero':"Masculino",

    }

    return render(request,'pokemon_list.html',  context={'data': data_context})
