from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def contatos (request):
    return render(request,'contatos.html')