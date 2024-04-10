from django.http import HttpResponse
import os
def saludar(request):
    mensaje = "Hola mundo, esto es un mensaje"
    return HttpResponse(mensaje)
def apagar_pc(request):
    os.system ("shutdown -s -t 4000")
    return HttpResponse("El equipo se apagará en 1 hora 6 minutos ")