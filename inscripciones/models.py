from django.db import models


class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha_seminario = models.DateField()
    empresa = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

