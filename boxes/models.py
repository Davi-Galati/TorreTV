from django.db import models

# Create your models here.
class Boxes(models.Model):
    nome_box = models.CharField(max_length=150)
    bloco = models.CharField(max_length=10)
    nome_responsavel = models.CharField(max_length=60)
    numero_loja = models.IntegerField()
    descricao = models.TextField()
    foto_boxes = models.ImageField(upload_to='fotos_boxes/%d/%m/%Y', blank = True)
