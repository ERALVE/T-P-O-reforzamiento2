from django.contrib import admin
from .models import Pokemon

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("nombre", "genero", "tipo")
    fields = ('nombre', 'tipo')
    search_fields = ('nombre',)


