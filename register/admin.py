from django.contrib import admin
from .models import Register
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    pass
