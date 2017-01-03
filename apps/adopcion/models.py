from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.IntegerField()
	email = models.EmailField()
	direccion = models.TextField()

	def __str__(self):
		return self.nombre + " " + self.apellido
