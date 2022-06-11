from django.contrib import admin

from .models import Contatos

# Register your models here.

class ListaContatos(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')


admin.site.register(Contatos,ListaContatos)