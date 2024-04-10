class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def avanza(self):
       return "Ando caminando"

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def avanza(self):
        return "Ando moviendome en mi bicicleta"
if __name__ =='__main__':
    persona = Persona('Alan')
    print(persona.avanza())

    ciclista = Ciclista('Eli')
    print(ciclista.avanza())
