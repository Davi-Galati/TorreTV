from django.db import models
from datetime import datetime
# Create your models here.
class Blogs(models.Model): 
    descricao = models.TextField()
    data = models.DateField(default=datetime.now,blank=True)
    foto_blog = models.ImageField(upload_to='fotos_blog/%d/%m/%Y', blank = True)
    titulo = models.CharField(max_length=50, default="Title")
