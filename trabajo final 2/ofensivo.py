rom urllib import request
from urllib.error import URLError
def ver_contenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La Url ' + url +  ' no existe!')
    else:
        contenido = f.read()
        return contenido
def contar_palabras(url):
    try :
        f =request.urlopen(url)
    except URLError:
        return('¡La Url ' + url +  ' no existe!')
    else :
        contenido = f.read()
        return len(contenido.split())
url = 'https://identidad.mtess.gov.py/alumno/inscripcion_alumnos_usuario_list.php'
print(ver_contenido(url))
print("\n --------------------------\n")
print("En total hay unas:",contar_palabras(url), "palabras")