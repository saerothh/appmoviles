from django.db import models

from django.utils import timezone

# Create your models here.

class Movil(models.Model):
	modelo = models.CharField(max_length=50)
	fecha_lanzamiento = models.DateTimeField(default=timezone.now)
	fabricante = models.CharField(max_length=200)
	versionOS = models.CharField(max_length=5)

