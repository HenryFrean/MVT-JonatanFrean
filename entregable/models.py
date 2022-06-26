from django.db import models
from django.forms import CharField

# Create your models here.
class Prueba(models.Model):
    nombre = models.CharField(max_length=30)