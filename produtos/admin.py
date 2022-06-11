from django.contrib import admin

from .models import Produtos

# Register your models here.

class ListaProdutos(admin.ModelAdmin):
    list_display = ('id','nome_produto','boxe')
    list_display_links = ('id','nome_produto','boxe')


admin.site.register(Produtos,ListaProdutos)