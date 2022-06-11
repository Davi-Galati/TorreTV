from django.contrib import admin
from .models import Blogs

# Register your models here.



class ListaBlogs(admin.ModelAdmin):
    list_display = ('id','titulo','data')
    list_display_links = ('id','titulo','data')



admin.site.register(Blogs,ListaBlogs)