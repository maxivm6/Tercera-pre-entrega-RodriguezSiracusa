from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    precio = models.IntegerField()
    
    def __str__(self): return self.nombre
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'