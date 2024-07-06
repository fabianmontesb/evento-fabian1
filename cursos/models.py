import roles
from django.db import models

# Create your models here.
from django.contrib.auth.models import abstractuser

class usuario(abstractuser):
    roles = (
        ('admin',"administrador"),
        ("normal","usuario normal")
    )
   rol=models.CharField(max_length=7, choices = roles , default='normal')

class curso(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupos=models.PositiveIntegerField()
    estados=models.BooleanField(default=True)
    inscritos=models.ManyToManyField(usuario, related_name='cursos_inscritos,')
    def __str__(self):
        return self.nombre

