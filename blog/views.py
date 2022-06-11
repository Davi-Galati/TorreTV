from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs
# Create your views here.
def home (request):
    return render(request,'home.html')

def blog (request): 
    blogs = Blogs.objects.all()
    dados = {'blogs': blogs}


    return render(request,'blog.html',dados)