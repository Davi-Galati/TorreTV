from django.shortcuts import render
from django.http import HttpResponse
from .models import Eventos
# Create your views here.
def eventos (request):

    eventos = Eventos.objects.all()
    dados = {'eventos': eventos}



    return render(request,'eventos.html',dados)