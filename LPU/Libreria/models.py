from django.db import models

# Create your models here.
class articulo(models.Model):
    nombre = models.CharField(max_length=45)
    precio = models.IntegerField()
    stock = models.IntegerField()
    editorial = models.ForeignKey(editorial, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo, on_delete=models.CASCADE)
    idioma = models.ForeignKey(idioma, on_delete=models.CASCADE)


class articulo_has_genero(models.Model):
    articulo = models.ForeignKey(articulo, on_delete=models.CASCADE)
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)


class genero(models.Model):
    nombre = models.CharField(max_length=45)

class editorial(models.Model):
    nombre = models.CharField(max_length=45)

class tipo(models.Model):
    nombre = models.CharField(max_length=45)

class idioma(models.Model):
    nombre = models.CharField(max_length=45)