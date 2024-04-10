#numeros primos
numero = 100000000
while True :
    bandera = 0
    for x in range(2, numero):
        if(numero % x == 0):
            bandera = 1
            #si bandera es 1 ya no es primo
            
            break
     #romper el primer ciclo
    if (bandera == 0):
        print(numero)

    bandera = 0
    numero += 1
