from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

valoraciones = (
	(0,'0'),
	(1,'1'),
	(2,'2'),
	(3,'3'),
	(4,'4'),
	(5,'5'),
)

BOOL_CHOICES = (
	(True, 'Si'),
	(False, 'No')
)

class Movil(models.Model):
	nombre = models.CharField(max_length=30, unique=True)
	fecha_lanzamiento = models.DateField(default=timezone.now)
	fabricante = models.CharField(max_length=30)
	versionOS = models.CharField(max_length=30)
	tam_pantalla = models.CharField(max_length=4)
	mem_ram = models.CharField(default = '--', max_length=10)
	microsd = models.BooleanField(choices=BOOL_CHOICES)
	image = models.ImageField(upload_to='moviles', blank= True)

	class Meta:
		verbose_name = 'Movil'
		verbose_name_plural = 'Moviles'

	def __str__(self):
		return self.nombre

class Valoracion(models.Model):
	valoracion = models.PositiveIntegerField(choices= valoraciones, default=0)
	usuario = models.ForeignKey(User)
	movil = models.ForeignKey(Movil)
	class Meta:
		verbose_name = 'Valoracion'
		verbose_name_plural = 'Valoraciones'

	def __str__(self):
		return str(self.valoracion)



class Comentario(models.Model):
	movil = models.ForeignKey(Movil)
	nombre = models.CharField(max_length=100, default = 'Anonimo')
	texto = models.TextField(help_text='Tu comentario', verbose_name='Comentario')
	fecha = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.texto 

	class Meta:
		verbose_name = 'Comentario'
		verbose_name_plural = 'Comentarios'

