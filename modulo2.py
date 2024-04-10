"""mport random
import os
def lanzar_datos( ):
    num = random. randint(1, 6)
    return num
print(lanzar_datos())
print(lanzar_datos())
print(lanzar_datos())"""
from turtle import *
import random
colors = ["red", "cyan", "yellow", "gray", "orange","blue"]
bgcolor = "black"

speed(0)
for x in range(100):
    aleatorio = random.randrange(0, 6)
    pencolor(colors[aleatorio])
    circle(100)
    """width(x/100 + 1)
    forward( x) """
    left()