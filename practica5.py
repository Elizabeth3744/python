
Traductor = {"amor":"love", "abrazo":"hug", "balón": "ball"}
palabra = " "
while palabra != "0":
    palabra = input("Ingrese la palabra a traducir: ")
    if palabra in Traductor :
        print(f"(esp) {palabra}: (en) {Traductor[palabra]}")
    elif(palabra != "0"):
        print("No se encuentra la palabra. ¿Desea agregarlo al Diccionario?")
        resp = input("S/N : ")
        if resp == "S":
            Traductor[palabra]= input(" Ingrese la traducción de dicha palabra: ")
            print("se ha agregado al diccionario")
        elif resp != "S" and resp != "0":
            print("Bueno")
        elif(resp == "0"):
            print("Cerrando Diccionario")
            break
    else:
        print("Cerrando Diccionario")