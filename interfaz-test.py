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

user_entry = StringVar()

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


def ventanaManual():
    ventana_manual = Toplevel()
    ventana_manual.title("Modo Manual")
    ventana_manual.minsize(1000, 500)
    ventana_manual.resizable(width=NO, height=NO)

    fondo = Canvas(ventana_manual, width=1000, height=500, bg="white")
    fondo.place(x=0, y=0)

    demanda_title = Label(fondo, text='Demanda: ', fg="black", font=("Roboto Slab", 22, "bold") )
    demanda_title.place(x=20, y=20)

    demanda = Label(fondo, text="123456789", fg='black', font=("Roboto Slab", 22, "bold"))
    demanda.place(x=20, y=80)

    vagones_title = Label(fondo, text='Vagones Disponibles: ', fg='black', font=("Roboto Slab", 22, "bold"))
    vagones_title.place(x=20, y=180)

    vagones = Label(fondo, text="Vagones aqui", fg='black', font=("Roboto Slab", 22, "bold"))
    vagones.place(x=20, y=260)

    vagones_1 = Label(fondo, text="Vagones aqui", fg='black', font=("Roboto Slab", 22, "bold"))
    vagones_1.place(x=20, y=320)

    vagones_2 = Label(fondo, text="Vagones aqui", fg='black', font=("Roboto Slab", 22, "bold"))
    vagones_2.place(x=20, y=380)

    vagones_3 = Label(fondo, text="Vagones aqui", fg='black', font=("Roboto Slab", 22, "bold"))
    vagones_3.place(x=20, y=450)


    shell = Entry(fondo, width=30, bg='#272822', fg='white', insertwidth=10, borderwidth=3,
                  font=("Source Code Pro", 20, "bold"), textvariable=user_entry)
    shell.place(x=370, y=50)

    eng_i = Button(fondo, bg='white', fg='black', text='Enganchar\nal inicio', font=("Roboto Slab", 20, "bold"))
    eng_i.place(x=370, y=120)

    eng_m = Button(fondo, bg='white', fg='black', text='Enganchar\nal medio', font=("Roboto Slab", 20, "bold"))
    eng_m.place(x=570, y=120)

    eng_f = Button(fondo, bg='white', fg='black', text='Enganchar\nal final', font=("Roboto Slab", 20, "bold"))
    eng_f.place(x=770, y=120)

    quitar_v = Button(fondo, bg='white', fg='black', text='Quitar\nultimo vagon', font=("Roboto Slab", 20, "bold"))
    quitar_v.place(x=570, y=240)


    def regresar():
        ventana_manual.destroy()

    def VentanaHelp():
        ventanahelp = Toplevel()
        ventanahelp.title("Help")
        ventanahelp.minsize(500, 500)
        ventanahelp.resizable(width=NO, height=NO)

        ventanahelp.mainloop()

    imagenvolverbk = cargarImagen("exit.png")
    botonvolver = Button(fondo, image=imagenvolverbk, command=regresar, fg="#000000", bg="#00cc00",
                         activebackground="#cc2900")
    botonvolver.place(x=900, y=410)

    imagenhelp = cargarImagen("help.png")
    botonhelp = Button(fondo, image=imagenhelp, command=VentanaHelp, bg="#00cc00",
                       fg="#000000", activebackground="#cc2900")
    botonhelp.place(x=800, y=410)

    ventana_manual.mainloop()



manual = Button(consola, text='Manual', command = ventanaManual, fg='white', bg='black', font=("Source Code Pro", 20, "bold"))
manual.place(x=20, y=50)

ventana_principal.mainloop()
