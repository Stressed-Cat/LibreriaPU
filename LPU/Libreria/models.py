from django.db import models

# Create your models here.
class articulo(models.Model):
    nombre = models.CharField(max_length=125)
    precio = models.IntegerField()
    stock = models.IntegerField()

class genero(models.Model):
    nombre = models.CharField(max_length=125)

class editorial(models.Model):
    nombre = models.CharField(max_length=125)

class tipo(models.Model):
    nombre = models.CharField(max_length=125)

class idioma(models.Model):
    nombre = models.CharField(max_length=125)