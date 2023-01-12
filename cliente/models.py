from django.db import models

# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=45)
    telefono = models.IntegerField(null=True)
    direccion = models.CharField(max_length=60)
    
    def __str__(self): return self.nombre
    
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'