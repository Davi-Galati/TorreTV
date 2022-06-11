from django.db import models

# Create your models here.
class Eventos(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    foto_eventos = models.ImageField(upload_to='fotos_eventos/%d/%m/%Y', blank = True)
