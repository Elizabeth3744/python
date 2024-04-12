from urllib import request
from urllib.error import URLError
def ver_contenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La Url ' + url +  ' no existe!')
    else:
        contenido = f.read()
        return contenido
lista_ofensiva = ['hijoputa', 'bastardo', 'cornudo', 'baboso','carajo']
def verficar(url):
    try :
        f =request.urlopen(url)
    except URLError:
        return('¡La Url ' + url +  ' no existe!')
    else :
        aux = f.read()
        contenido = aux.split()
        palabras_encontradas = [ ]
        for l in lista_ofensiva:
            for con in contenido:
                if l in con.decode():
                    palabras_encontradas .append(l)
        return (f' se han encontrado {len(palabras_encontradas)} palabras ofensivas. Lista: {palabras_encontradas}')
    
    

url = 'https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales'
print(ver_contenido(url))
print("\n --------------------------\n")
print(verficar(url))