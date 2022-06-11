from tokenize import blank_re
from django.db import models

# Create your models here.
class Contatos(models.Model):
    nome = models.CharField(max_length=50)
    contato = models.TextField(default='')

