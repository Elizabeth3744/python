import os
resp = 1
while resp != 0:
    print("Paint (1)")
    print("Calculadora (2)")
    print("Apagar PC  en 2 horas (3)")
    print("Salilr (0)")
    print("Google (4)")
    print("Edge (5)")
    resp = int(input("seleccione: "))
    if(resp == 1):
        os.system("mspaint")
    elif(resp == 2):
        os. system("Calc")
    elif(resp == 3):
        os.system("shutdown -s -t 7200")
    elif(resp == 4):
        os. system ("Start chrome")
    elif(resp == 5):
        os.system("Start Edge")
    else:
        print("no entiendo esa orden")