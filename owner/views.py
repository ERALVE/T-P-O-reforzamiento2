from django.shortcuts import render
from owner.models import Owner
# Create your views here.

def owner_list(request):

    data_context =[
        {
            'nombre': 'Thania Peralta',
            'edad': 17,
            'dni':"98745612",
            'pais': "Perú",
            'vigente': False,
            'pokemons': [
                {
                    'nombre_pokemon': 'Charizar',
                    'ataques': ['Ataque 1 -Charizard', 'Ataque 2 -Charizar', 'Ataque 3 -Charizar']
                }
            ],
        },
        {
            'nombre': 'Mejia Gonzales',
            'edad': 22,
            'dni': "11111111",
            'pais': "Brasil",
            'vigente': False,
            'pokemons': [],
        },
        {
            'nombre': 'Benito Parede',
            'edad': 17,
            'dni': "45612378",
            'pais': "Perú",
            'vigente': True,
            'pokemons': [],
        }

    ]
    return render(request,'owner_list.html',  context={'data': data_context})

def owner_orm(request):
    #data_context= []
    """Crear un objeto en la tabla owner de la base de datos"""
    #owner = Owner(nombre=" Leonardo Quispe", edad=23, dni="48484885", pais="Perú", vigente=True)
    #owner.save()
    """Obtner todos los owner de la base de datos"""
    data_context = Owner.objects.filter(pais="Perú")
    print(data_context)


    return render(request, 'owner_orm.html', context={'data': data_context})
