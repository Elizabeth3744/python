from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Cancion


# Create your views here.
def inicio(request):
    lista_cancion = Cancion.objects.all()
    return render(request,"index.html",{"canciones": lista_cancion})
def plantilla_index(request):
    plantilla = loader.get_template('index.html')
    documento = plantilla.render()
    return HttpResponse(documento)
def plantilla_inicio (request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
