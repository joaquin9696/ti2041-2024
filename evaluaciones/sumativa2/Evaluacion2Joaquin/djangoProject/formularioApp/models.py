from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
