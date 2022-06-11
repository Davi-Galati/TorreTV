
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Boxes
from produtos.models import Produtos
# Create your views here.
def boxes (request):
     boxes = Boxes.objects.all()
     dados = {'boxes': boxes}


     return render(request,'boxes.html',dados)

def box (request,box_id):
     produtos = Produtos.objects.filter(boxe=box_id)
     box = get_object_or_404(Boxes,pk=box_id)
     mostra_box = { 
          'box': box,
          'produtos':produtos
     }


     return render(request,'box.html',mostra_box)