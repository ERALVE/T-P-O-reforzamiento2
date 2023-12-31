from django.shortcuts import render
from django.db.models import F, Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.core import serializers as sr
from django.http import HttpResponse

###Tokentizacion de la app se necesira estas librerias
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Owner
from owner.forms import OwnerForm
from owner.serializers import OwnerSerializers
from django.http import Http404


# Create your views here.

# def owner_list(request):
#
#     data_context =[
#         {
#             'nombre': 'Thania Peralta',
#             'edad': 17,
#             'dni':"98745612",
#             'pais': "Perú",
#             'vigente': False,
#             """Este campo pokemon va ser una lista como tal puede tener un diccionario adentro"""
#             'pokemons': [
#                 {
#                     'nombre_pokemon': 'Charizar',
#                     """Diccionario"""
#                     'ataques': ['Ataque 1 -Charizard', 'Ataque 2 -Charizar', 'Ataque 3 -Charizar']
#                 }
#             ],
#         },
#         {
#             'nombre': 'Mejia Gonzales',
#             'edad': 22,
#             'dni': "11111111",
#             'pais': "Brasil",
#             'vigente': False,
#             'pokemons': [],
#         },
#         {
#             'nombre': 'Benito Parede',
#             'edad': 17,
#             'dni': "45612378",
#             'pais': "Perú",
#             'vigente': True,
#             'pokemons': [],
#         }
#
#     ]
#     return render(request,'owner_list.html',  context={'data': data_context})


#REFORZAMIENTO 3


def owner_list(request):
    """Pregunta1"""
    data_context = Owner.objects.all()
    """pregunta3:contar cuantos owners son de  Perú y Argentina"""
    count_peru = Owner.objects.filter(pais='Perú').count()
    count_argentina = Owner.objects.filter(pais='Argentina').count()

    return render(request, 'pregunta_1.html', context={'data': data_context, 'count_peru': count_peru, 'count_argentina': count_argentina})


def owner_search(request):
    query = request.GET.get('q', '')
    """ Pregunta2:ealiza la búsqueda en la base de datos"""
    data_context = Owner.objects.filter(nombre__icontains=query) | Owner.objects.filter(pais__icontains=query)
    return render(request, 'owner_search.html', context={'data': data_context, 'query': query})

"""Pregunta 4"""
def owner_delete(request, id_owner):
    owner = Owner.objects.get(id=id_owner)
    if request.method == 'POST' and 'confirm-delete' in request.POST:
        owner.delete()
        '''El redirec hace un redireccionamiento cuando termine con esta vista, es decir a que url tiene que ir cuando termine de hacer la eliminacio de ese registro'''
        return redirect('owner_list')
        """Pregunta 6"""
    elif request.method == 'POST':
        return render(request, 'owner_confirm_delete.html', {'owner': owner})

    return render(request, 'owner_delete.html', context={'owner': owner})


"""Pregunta 5"""
def owner_update(request, id_owner):
    owner = Owner.objects.get(id=id_owner)

    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)

    return render(request, 'owner_update.html', context={'form': form, 'owner': owner})

"""Pregunta 7"""
class OwnerList(ListView):
    model = Owner
    template_name = 'owner_list_vc.html'
    context_object_name = 'owners'
    ordering = ['id']

"""Pregunta 8"""
class OwnerCreate(CreateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner_create.html'
    success_url = reverse_lazy('owner_list_vc')

"""Pregunta 9"""
class OwnerUpdate(UpdateView):
    """Clas para su cancelar y agregar """
    model = Owner
    form_class = OwnerForm
    template_name = 'owner_update_vc.html'
    success_url = reverse_lazy('owner_list_vc')

"""Pregunta 10"""
class OwnerDelete(DeleteView):
    """Clas para su cancelar y agregar """
    model = Owner
    #form_class = OwnerForm
    success_url = reverse_lazy('owner_list_vc')
    template_name = "owner_delete.html"

"""Pregunta 11"""
@api_view(['POST'])
def create_owner(request):
    serializers_class = OwnerSerializers(data=request.data)
    if serializers_class.is_valid():
        serializers_class.save()
        return Response(serializers_class.data, status=status.HTTP_201_CREATED)
    return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_owners(request):
    queryset = Owner.objects.all()
    serializers_class = OwnerSerializers(queryset, many=True)
    return Response(serializers_class.data, status=status.HTTP_200_OK)

"""Pregunta 12"""

@api_view(['GET', 'PUT', 'DELETE'])
def owner_details_view(request, pk):
    print("Entró a la vista owner_details_view")
    print("ID del owner:", pk)
    owner = Owner.objects.filter(id=pk).first()

    if owner:
        if request.method == 'GET':
            serializers_class = OwnerSerializers(owner)
            return Response(serializers_class.data)

        elif request.method == 'DELETE':
            print("Ingreso a DELETE")
            owner.delete()
            return Response("Owner ha sido eliminado de la base de datos", status=status.HTTP_200_OK)

        elif request.method == "PUT":
            serializers_class = OwnerSerializers(owner, data=request.data)
            if serializers_class.is_valid():
                serializers_class.save()

                return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)








def owner_orm(request):
    #data_context= []
    """Crear un objeto en la tabla owner de la base de datos"""
    #owner = Owner(nombre=" Leonardo Quispe", edad=23, dni="48484885", pais="Perú", vigente=True)
    #owner.save()
    """Obtner todos los owner de la base de datos, es decir,todos los registros con el all """
    #data_context = Owner.objects.all()

    """Filtracion de datos usando filter()"""
   # data_context = Owner.objects.filter(pais="Perú")

    """Filtracion de datos mas precisos: __contains si toma en cuenta las mayusculas y minusculas"""
   # data_context = Owner.objects.filter(nombre__contains= "Adelia")

    """Filtro de datos mas precisos buscara el objeto que termines con lo que definiste en el parebtesis: __endswith """
    #data_context = Owner.objects.filter(nombre__endswith='la')

    """obtener un solo objeto de la base de datos de owner"""
    #data_context = Owner.objects.get(dni="77777777")
    """ Ordenar por cualquier campo de la tabla"""
    #data_context = Owner.objects.order_by("-nombre")

    """oredenar por concatenamiento"""
    #data_context = Owner.objects.order_by("edad")
    """Ordenar concatenando diferentes metodos de ORM´s"""
    #data_context = Owner.objects.filter(nombre="Adelia").order_by("edad")

    """Acortar datos: Obtener un rango de registro de una tabla en la base de datos"""
    #data_context = Owner.objects.all()[0:5]

    """eliminar un dato facilmente"""
    #data_context = Owner.objects.get(id=7)
    #data_context.delete()

    """Actualizar la base de datos a un cierto grupo de registros """
    #Owner.objects.filter(edad=23).update(pais="Mexico")
    """Utilizando F expressions"""
    #Owner.objects.filter(edad__gte=25).update(edad=F('edad')+10)
    #data_context = Owner.objects.filter(edad__gte=25)
    #data_context = Owner.objects.all()

    """Consultas complejas"""
    #query = Q(pais__startswith= "Pe") | ~Q(edad=23)
    #data_context = Owner.objects.filter(query)
    query = Q(pais__startswith="Pe") | Q(pais__startswith="Me")
    data_context = Owner.objects.filter(query, edad__gte=70)
    """Error de consulta cuando con Q: cuando no es valido"""
    #query = Q(pais__startswith= 'Pe') | Q(pais__startswith= 'Es')
    #data_context = Owner.objects.filter(edad__lte=30, query)


    """print me muestra en la termina de pycharm los datos"""
   # print(data_context)


    return render(request, 'owner_orm.html', context={'data': data_context})

"""Estamos viendo la parte de los formularios con un solo campo"""

def owner_details(request):
    """Queremos obtener todos los owner de la tabla correspondiente de la base de datos"""
    data_context = Owner.objects.all()

    return render(request, 'owner_details.html', context={'data': data_context})

# def owner_delete(request, id_owner):
#     print("ID de owner: {}".format(id_owner))
#
#     owner = Owner.objects.get(id=id_owner)
#     owner.delete()
#     '''El redirec hace un redireccionamiento cuando termine con esta vista, es decir a que url tiene que ir cuando termine de hacer la eliminacio de ese registro'''
#     return redirect('owner_details')

# def owner_edit(request, id_owner):
#     print("ID de owner: {}".format(id_owner))
#     owner = Owner.objects.get(id=id_owner)
#     print("Datos del owner a editar: {}".format(owner))
#
#     form = OwnerForm(initial={'nombre': owner.nombre, 'edad': owner.edad, 'pais': owner.pais, 'dni': owner.dni})
#
#     if request.method == 'POST':
#         form = OwnerForm(request.POST, instance=owner)
#
#         if form.is_valid():
#             form.save()
#             return redirect('owner_details')
#     return render(request, 'owner_update.html', context={'data': form})

def owner_create(request):
    form = OwnerForm(request.POST)
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        edad = form.cleaned_data['edad']
        pais = form.cleaned_data['pais']
        form.save()
        """El redirect se usa cuando va terminar de guardar"""
        return redirect('owner_details')
    else:
        form = OwnerForm()
    """render para que me redericcione a ese owner create de html """
    return render(request, 'owner_create.html', {'data': form})
"""VCB"""
# class OwnerList(ListView):
#     model = Owner
#     template_name = 'owner_list_vc.html'

# class OwnerCreate(CreateView):
#     model = Owner
#     form_class = OwnerForm
#     template_name = 'owner_create.html'
#     success_url = reverse_lazy('owner_list_vc')

# class OwnerUpdate(UpdateView):
#     """Clas para su cancelar y agregar """
#     model = Owner
#     form_class = OwnerForm
#     template_name = 'owner_update_vc.html'
#     success_url = reverse_lazy('owner_list_vc')

# class OwnerDelete(DeleteView):
#     """Clas para su cancelar y agregar """
#     model = Owner
#     #form_class = OwnerForm
#     success_url = reverse_lazy('owner_list_vc')
#     template_name = "owner_confirm_delete.html"

    #URLs Django Framework

"""Se enviara informacion a la api el post lo recibira y guardara en la base de datos"""
"""GET solo muestra los dtaos """
# @api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticated])
# def Owner_api_view(request):
#
#     if request.method == 'POST':
#         print("Data OWNER: {}".format(request.data))
#         """objeto jason"""
#         serializers_class = OwnerSerializers(data=request.data)
#         if serializers_class.is_valid():
#             serializers_class.save()
#             return Response(serializers_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializers_class.data, status=status.HTTP_400_BAD_REQUEST )
#
#     elif request.method == 'GET':
#         print("Ingreso a GET")
#         queryset = Owner.objects.all()
#         serializers_class = OwnerSerializers(queryset, many=True)
#
#         return Response(serializers_class.data, status=status.HTTP_200_OK)
"""Apis"""
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def owner_details_view(request, pk):
#     owner = Owner.objects.filter(id=pk).first()
#
#     if owner:
#         if request.method == 'GET':
#             serializers_class = OwnerSerializers(owner)
#             return Response(serializers_class.data)
#
#         elif request.method == 'DELETE':
#             print("Ingreso a DELETE")
#             owner.delete()
#             return Response("Owner ha sido eliminado de la base de datos", status=status.HTTP_200_OK)
#
#         elif request.method == "PUT":
#             serializers_class = OwnerSerializers(owner, data=request.data)
#             if serializers_class.is_valid():
#                 serializers_class.save()
#
#                 return Response(serializers_class.data, status=status.HTTP_202_ACCEPTED)
#             return Response(serializers_class.errors, status=status.HTTP_400_BAD_REQUEST)





