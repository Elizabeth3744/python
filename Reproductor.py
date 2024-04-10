from pygame import mixer
class Reproductor:
    #atributos
    archivo = None
    #Constructor
    def __init__ (self, archivo):
     self.archivo = archivo
     mixer.init( )
     mixer.music.load(archivo)
     self. valor_volumen = 0
     
    def play(self):
        mixer.music.play()
        return "Reproduciendo música 🎶"
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"
    def stop(self):
     mixer.music.stop()
     return "la música se detuvo"
    def volume(self, v):
        mixer.music.set_volume(v)
        return "definiendo volumen a {}".format(v)
    def volume(self, v):
        self. valor_volumen += v 
        if (self.valor_volumen > 1):
            self.valor_volumen = 1
        elif (self.valor_volumen < 0):
            self.valor_volumen = 0
        mixer.music.set_volume(self. valor_volumen)
        return f" definiendo volumen a {valor_volumen}"