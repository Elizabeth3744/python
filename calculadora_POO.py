class Calculadora:
    #datos, atributos
    primer_numero = None 
    segundo_numero = None
    resultado = None 
    historial = None 

    def __init__(self, p, s):
        self.primer_numero = p 
        self. segundo_numero = s
        self.resultado = 0.0
        self.historial = []

    def set_numeros(self, p, s):
        self.primer_numero = p 
        self.segundo_numero = s 

    def get_sumar(self):
        self.resultado =self.primer_numero + self.segundo_numero
        texto = str(self.primer_numero) + "+" + str(self.segundo_numero) + "=" + str(self.resultado)
        self.historial.append(texto)
    def get_sumar(self):
     return self.primer_numero + self.segundo_numero
    def get_restar(self):
        self.resultado =self.primer_numero - self.segundo_numero
        texto = str(self.primer_numero) + "-" + str(self.segundo_numero) + "=" + str(self.resultado)
        self:historial.append(texto)
    def get_restar(self):
        return self.primer_numero - self.segundo_numero
    def get_multiplicar(self):
       self.resultado =self.primer_numero * self.segundo_numero
        texto = str(self.primer_numero) + "*" + str(self.segundo_numero) + "=" + str(self.resultado)
        self:historial.append(texto) 

    def get_resultado(self):
        return self.resultado
    def get_historial(self):
        return self.historial
if __name__== "__main__":
        calcu = Calculadora(45, 15)
        print(calcu.get_sumar())
if __name__ == "__main__":
    m = Calculadora(52, 52)
    print(m.get_sumar())
if __name__ == "__main__":
    resta = Calculadora(8,2)
    print(resta.get_restar())