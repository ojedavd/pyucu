from django.db import models

# Create your models here.
class Certificado(models.Model):
    dni = models.CharField(max_length=200, verbose_name="DNI")
    name = models.CharField(max_length=200, verbose_name="Nombre del alumno")
    description = models.CharField(max_length=200, verbose_name="Descripción del certificado")
    observation = models.TextField(verbose_name="Observación", null=True, blank=True)
    published = models.DateTimeField(verbose_name="Fecha de publicación")
    
    def __str__(self):
        return self.name   