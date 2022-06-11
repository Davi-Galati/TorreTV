from django.contrib import admin

from .models import Eventos

# Register your models here.


class ListaEventos(admin.ModelAdmin):
    list_display = ('id','titulo')
    list_display_links = ('id','titulo')
    

admin.site.register(Eventos,ListaEventos)