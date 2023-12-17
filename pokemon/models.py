from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
