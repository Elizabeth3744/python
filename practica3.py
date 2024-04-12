notas = []
for x in range (3):
    nota= int (input ("ingrese la nota:"))
    notas. append(nota)


suma = 0
for x in range(3):
    suma += notas [x] 


promedio = suma /  3
print(notas)
print(f"El promedio es {promedio}")
if promedio>1.7 :
    print( "Has aprobado")
else:
    print(" Has reprobado")