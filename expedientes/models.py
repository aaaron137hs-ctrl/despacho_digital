from django.db import models

class Caso(models.Model):
    # Definimos las columnas de nuestra tabla
    titulo = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    descripcion = models.TextField()
    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
# Create your models here.
