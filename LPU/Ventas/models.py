from django.db import models

# Create your models here.
#class ejemplar(models.Model):
    # Se meteria la foreign key creo, despues lo hago a excepción que lo hagas tu primero

class compra(models.Model):
    precio_total = models.IntegerField()
    precio_total = models.DateField()