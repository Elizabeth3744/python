from tkinter import *
from tkinter import ttk 
root = Tk()
frm = ttk.Frame(root,padding = 50)
frm.grid()
ttk.Label (frm, text = "Hola mundo").grid (column = 5, row=5)
ttk.Button(frm, text = "Quitar", command = root.destroy).grid(column=5,row= 6)
root.mainloop()