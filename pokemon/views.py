from django.shortcuts import render
from pokemon.models import Pokemon
# Create your views here.

def pokemon_list(request):

    data_context = {
        'nombre': 'Pikachu',
        'tipo':  'Electrico',
        'genero':"Masculino",

    }

    return render(request,'pokemon_list.html',  context={'data': data_context})
def pokemon_orm(request):

    """Obtner todos los owner de la base de datos"""
    data_context = Pokemon.objects.filter(tipo="Fuego")
    print(data_context)
    return render(request, 'pokemon_orm.html', context={'data': data_context})