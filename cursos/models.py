
from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):  # Corregido el nombre del modelo
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField()
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_creados')

class Inscripcion(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)  # Corregido el nombre del modelo
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)


