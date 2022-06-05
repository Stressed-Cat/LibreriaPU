from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=125)
    apellido = models.CharField(max_length=125)
    mail = models.CharField(max_length=125)
    contrasena = models.CharField(max_length=125)
  # super_usuario = models.BinaryField() --> Supuestamente no es editable, asi que no estoy seguro si funciona

class ciudad(models.Model):
    nombre = models.CharField(max_length=125)
