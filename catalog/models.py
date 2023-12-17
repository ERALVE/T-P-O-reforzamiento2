from django.db import models

class Catalog(models.Model):
    nombre = models.CharField(max_length=40)
    especie = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
