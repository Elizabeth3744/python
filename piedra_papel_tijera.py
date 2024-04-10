import random
while True:
    aleatorio = random.randrange(0,3)
    elijePc = ""
    print("1. piedra")
    print("2. papel")
    print("3. tijera")
    opcion = int(input(" elige tu opción"))
    if opcion == 1:
        elijeUsuario = "piedra"
    elif opcion == 2: 
        elijeUsuario = "papel"
    elif opcion == 3:
        elijeUsuario = "tijera"
    print("Elegiste: ", elijeUsuario)
    if aleatorio == 0:
        elijePc = "piedra"
    elif aleatorio == 1: 
        elijePc = "papel"
    elif aleatorio == 2:
       elijePc = "tijera"
    print("La maquina elijio:", elijePc)
    print("......")
    if elijePc == "piedra" and elijeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
    elif elijePc == "papel"  and elijeUsuario == "tijera":
        print("Ganaste, tijera corta Papel")
    elif elijePc == "tijera" and elijeUsuario == "piedra":
        print("Ganaste, piedra machaca tijera")
    if elijePc== "papel" and elijeUsuario =="piedra":
        print("perdiste, papel envuelve piedra") 
    elif elijePc == "tijera" and elijeUsuario == "papel":
        print("perdiste tijera corta papel")
    elif elijePc == "piedra" and elijeUsuario == "tijera":
        print("perdiste, piedra machaca tijera")
    elif elijePc == elijeUsuario:
        print("empate")

