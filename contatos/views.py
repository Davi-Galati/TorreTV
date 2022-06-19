from django.shortcuts import render
from django.http import HttpResponse
from .models import Contatos
# Create your views here.
def contatos (request):
     contatos = Contatos.objects.all()
     dados = {'contatos': contatos}
     return render(request,'contatos.html',dados)