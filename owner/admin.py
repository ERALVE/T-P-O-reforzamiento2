from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("nombre", "edad", "pais", "dni", "vigente")
    search_fields = ('nombre',)
