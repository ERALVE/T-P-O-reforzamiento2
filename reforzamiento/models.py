from django.db import models

class Reforzamiento(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    pais = models.CharField(max_length=27, default='')
    dni = models.CharField(max_length=8, default='')
    vigente = models.BooleanField(default=True)