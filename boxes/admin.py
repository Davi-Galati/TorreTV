from django.contrib import admin
from .models import Boxes

# Register your models here.



class ListaBoxes(admin.ModelAdmin):
    list_display = ('id','nome_box','numero_loja')
    list_display_links = ('id','nome_box','numero_loja')


admin.site.register(Boxes,ListaBoxes)