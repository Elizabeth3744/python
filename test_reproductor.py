from tkinter import *
from tkinter.ttk import *
from Reproductor import *
musica = Reproductor("wefere (1).mp3")
display = "reproductor de música"
def play_music():
    musica.volume(0.8)
    display = musica.play()
    Label.config(text=display)
def pause_music( ):
    display = musica.pause()
    Label.config(text=display)
def stop_music():
    display = musica.stop()
    Label.config(text=display)
def vol_menos():
    display =  musica.volume(-0.1)
    Label.config(text=display)
def vol_mas ():
    display = musica.volume (0.1)
    Label.config(text=display)
master = Tk()
master.geometry("240x500")

Label = Label(master, text=display)

Label.pack(pady = 10)

btn_play = Button(master, text = " ▶ ", command = play_music)
btn_play.pack(pady = 10)
btn_play = Button(master, text = " ⏸ ", command = pause_music)
btn_play.pack(pady = 10)
btn_play = Button(master, text = " ⏹ ", command = stop_music)
btn_play.pack(pady = 10)
btn_play = Button(master, text = " ➕ ", command = vol_mas)
btn_play.pack(pady = 10)
btn_play = Button(master, text = " ➖", command = vol_menos)
btn_play.pack(pady = 10)
mainloop()
