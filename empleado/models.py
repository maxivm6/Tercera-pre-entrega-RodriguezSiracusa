from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    salario = models.IntegerField()
    area = models.CharField(max_length=60)
    
    def __str__(self): return self.nombre
    
    class Meta:
        verbose_name = 'empleado'
        verbose_name_plural = 'empleados'