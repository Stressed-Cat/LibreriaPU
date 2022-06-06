from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    mail = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    ciudad = models.ForeignKey(ciudad, on_delete=models.CASCADE)
  # super_usuario = models.BinaryField() --> Supuestamente no es editable, asi que no estoy seguro si funciona

class ciudad(models.Model):
    nombre = models.CharField(max_length=45)
