usuarios_autenticados = {"admi":"12345", "ElIzAbEtH": "65426", "Raúl": "98765"}
usuario = input("Ingrese su usuario:")
password = input("Ingrese su contraseña:")
if (usuario in usuarios_autenticados):
    intentos = 3
    while (intentos > 0):
        if(usuarios_autenticados[usuario] == password):
         print("ACCESO CORRECTO")
         break
        else:
            if intentos <= 1:
                print("Ya ha exedido el número de intentos. Cuenta bloqueada")
                intentos -= 1
            else:
                intentos -= 1
                print (f"Error de contraseña. Intentos restantes {intentos} de 3")
                password = input("Introduzca nuevamente la contraseña: ")    
else:
    print ("El usuario no existe")