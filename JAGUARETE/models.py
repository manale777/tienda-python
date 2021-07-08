from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.categoria} - {self.descripcion}"

class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    imagen = models.FileField(upload_to="imagenes/")
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(max_length=6)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria_producto")

    def __str__(self):
        return f"Producto {self.titulo} - {self.categoria}"

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    productos = models.ManyToManyField(Producto, blank=True, related_name="productos")
    total = models.FloatField(max_length=6)

    def __str__(self):
        return f"El usuario {self.usuario} adquirio los productos: {self.productos} con un precio de {self.total}"
