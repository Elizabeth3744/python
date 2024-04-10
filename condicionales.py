
"""edad = int(input("Ingrese su edad"))
if (edad > 15 and edad < 18):
 print("Licencia con permiso del padre")
   elif(edad >= 18 and edad <= 65):
       print("licencia standart")
  elif(edad >= 65 and edad <= 75):
      print("debe realizar un sicotécnico")
  else (edad >= 75):
    print("usted no puede obtener una licencia")"""
print("Ejercicio 1 de Condicionales")
numero_1 = int(input("Ingrese el primer número"))
numero_2 = int(input("ingrese el segundo numero"))
if(numero_1 > numero_2):
    print("{} es mayor a {}".format(numero_1,numero_2))
    if(numero_1 % 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
elif(numero_1 < numero_2):
    print("{} es mayor a {}".format(numero_2,numero_1))
    if(numero_2% 2 == 0):
        print("El numero es par")
    else:
        print("El numero es impar")
else:
    print("Los numeros ingreados son iguales")
print("_________________________________________")
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su password: ")
if(usuario == "admin" and password == "12345"):
    print("Acceso correcto")
else:
    print("Acceso incorrecto")