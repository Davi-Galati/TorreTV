from django.shortcuts import render
from django.http import HttpResponse
from .models import Produtos
# Create your views here.
def produtos (request):
    produtos = Produtos.objects.all()
    dados = {'produtos': produtos}


    return render(request,'produtos.html',dados)
