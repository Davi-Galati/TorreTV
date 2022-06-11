from django.db import models
from boxes.models import Boxes
# Create your models here.

class Produtos (models.Model): 
    nome_produto = models.CharField(max_length=150)
    descricao = models.TextField()
    foto_produtos = models.ImageField(upload_to='fotos_produtos/%d/%m/%Y', blank = True)
    boxe = models.ForeignKey(Boxes, on_delete=models.CASCADE)
