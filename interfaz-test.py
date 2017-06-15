from tkinter import *
from tkinter import messagebox
from threading import Thread
import os

ventana_principal = Tk()
ventana_principal.title("Estacion TEC")
ventana_principal.minsize(1560, 1000)
ventana_principal.resizable(width=NO, height=NO)

contenedor_principal = Canvas(ventana_principal, width=1560, height=1000, bg="#ffffff")
contenedor_principal.place(x=0, y=0)


def cargarImagen(nombre):
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


frame_tec = cargarImagen("tec.png")
tec = Label(contenedor_principal, bg='white', image=frame_tec)
tec.place(x=1100, y=200)

frame_rail = cargarImagen("rail.png")
rail = Label(contenedor_principal, bg='white', image=frame_rail)
rail.place(x=300, y=300)

gam_frame = cargarImagen("gam.png")
gam = Label(contenedor_principal, bg='white', image=gam_frame)
gam.place(x=300, y=150)


ventana_principal.mainloop()
