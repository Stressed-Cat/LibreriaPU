from django.db import models
from Libreria import articulo
from Usuarios import usuario

# Create your models here.
class ejemplar(models.Model):
    articulo = models.ForeignKey(articulo, on_delete=models.CASCADE)
    compra = models.ForeignKey(compra, on_delete=models.CASCADE)

class compra(models.Model):
    precio_total = models.IntegerField()
    fecha = models.DateField()
    comprador = models.ForeignKey(usuario, on_delete=models.CASCADE)
    vendedor =models.ForeignKey(usuario, on_delete=models.CASCADE)