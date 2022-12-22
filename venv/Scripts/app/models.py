from django.db import models

# Create your models here.

class Carros(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()