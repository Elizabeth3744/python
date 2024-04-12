def ordenar(l, orden):
    #orden ascendente(bubblesort: ordenamiento burbuja: 
    #se encarga de comparar cada elemento para ver si uno es mayor al otro
    lista = l[ : ]
    limite = len (lista) -1
    if (orden == "ASC"):
        for x in range (0,limite):
            for y in range(0, limite):
                if lista[y] < lista[y + 1]:
                    aux = lista[y]
                    lista[y] = lista[y +1]
                    lista[y +1] = aux
    elif (orden == "DESC"):
        for x in range (0,limite):
            for y in range(0, limite):
                if lista[y] > lista[y + 1]:
                    aux = lista[y]
                    lista[y] = lista[y +1]
                    lista[y +1] = aux
    return lista
    
subrayado= "lista desordeanda"
print("\033[4m{}\033[0m".format(subrayado))
temperatura = [45, 26, 30, 25, 74, -10, -50, 7430, -100, 18, 62, 0]
print(temperatura)

subrayado = "lista ordenada de forma ascendente"
print("\033[4m{}\033[0m".format(subrayado))
lista_ordenada = ordenar(temperatura, "ASC")
print(lista_ordenada)
subrayado ="Lista ordenada de forma descendente"
print("\033[4m{}\033[0m".format(subrayado))
lista_ordenada = ordenar(temperatura, "DESC")
print(lista_ordenada)
