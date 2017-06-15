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
rail.place(x=290, y=460)

gam_frame = cargarImagen("gam2.png")
gam = Label(contenedor_principal, bg='white', image=gam_frame)
gam.place(x=300, y=190)

canvas = Canvas(ventana_principal, width=300, height=700, bg='red')
canvas.place(x=0, y=0)

canvas_v = Canvas(ventana_principal, width=300, height=300, bg='green')
canvas_v.place(x=0, y=700)

consola = Canvas(ventana_principal, width=1260, height=300, bg='gray')
consola.place(x=300, y=700)

ventana_principal.mainloop()
