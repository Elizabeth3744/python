#sumar , resta, multiplicar, dividir, raiz cuadrada, y exponente
#resultado = sumar(45, 78)
def sumar(x, y):
    return x + y
def sumador(*args):       # las parantesis sirven para recibir parametros
    resultado = 0
    for x in args:
        resultado += x
    return resultado
def restar(x, y):
    return x - y 
def multiplicar(x, y):
  return int(x * y)
def dividir(x, y):
    if (y != 0):
      return int( x/y)
    else:
     return "No se puede dividir entre cero"

  def raiz(x, y):
  return int(  (x)**(1/y))
  def potencia(x, y):
    return x ** y
print(restar(7, 5))
print(dividir(4, 2))
print(dividir(2, 0))
print(multiplicar(5, 6))
print(potencia(3, 2))
print( sumador(2, 3, 0, 4, 5 ,8))
print(raiz(-25, 2))
print(raiz(25, 2))