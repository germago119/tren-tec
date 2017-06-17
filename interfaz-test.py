from tkinter import *
from tkinter import messagebox
from threading import Thread
import os


ventana_principal = Tk()
ventana_principal.title("Estacion TEC")
ventana_principal.minsize(1560, 1000)
ventana_principal.resizable(width=NO, height=NO)

contenedor_principal = Canvas(ventana_principal, width=1560, height=1000, bg="#87ceeb")
contenedor_principal.place(x=0, y=0)

user_entry = StringVar()
demanda_variable = StringVar()
auto_var = 'VAGON 1'


def cargarImagen(nombre):
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

irazu_frame = cargarImagen('13.png')
irazu = Label(contenedor_principal, bg='white', image=irazu_frame)
irazu.place(x=750, y=3)

frame_tec = cargarImagen("tec.png")
tec = Label(contenedor_principal, bg='white', image=frame_tec)
tec.place(x=1100, y=200)

frame_rail = cargarImagen("rail.png")
rail = Label(contenedor_principal, bg='white', image=frame_rail)
rail.place(x=290, y=460)

gam_frame = cargarImagen("gam2.png")
gam = Label(contenedor_principal, bg='white', image=gam_frame)
gam.place(x=300, y=190)

canvas_r = Canvas(ventana_principal, width=300, height=700, bg='red')
canvas_r.place(x=0, y=0)

canvas_v = Canvas(ventana_principal, width=300, height=300, bg='green')
canvas_v.place(x=0, y=700)

consola = Canvas(ventana_principal, width=1260, height=300, bg='gray')
consola.place(x=300, y=700)

rutas_title = Label(canvas_r, text='Rutas proximas', bg='red', fg='white', font=("Roboto Slab", 24, "bold"))
rutas_title.place(x=10, y=10)

vagones_title = Label(canvas_v, text='Vagones Disponibles', bg='green', fg='white', font=("Roboto Slab", 20, "bold"))
vagones_title.place(x=10, y=10)

demanda_l = Label(consola,text="Demanda: ", bg="gray", fg='white', font=("Roboto Slab", 32, "bold"))
demanda_l.place(x=300, y=30)

demanda_var = Label(consola, text="Variable", bg="gray", fg='white', font=("Roboto Slab", 32, "bold"))
demanda_var.place(x=520, y=30)

body = 'Segun la demanda el programa selecciono los vagones ' + auto_var + ' para la siguiente salida.' \
                        ' Si desea puede escoger los vagones de forma manual o permiterle la salida del tren asi.'

message = Text(consola, height=9, width=87)
message.insert(END, body)
message.config(wrap=WORD)
message.tag_add("Body", 1.0, 99.9)
message.tag_config("Body", background='grey', foreground='white', font=("Roboto Slab", 20))
message.config(state=DISABLED)
message.place(x=270, y=110)


def ventanaManual():
    ventana_manual = Toplevel()
    ventana_manual.title("Modo Manual")
    ventana_manual.minsize(800, 500)
    ventana_manual.resizable(width=NO, height=NO)

    fondo = Canvas(ventana_manual, width=800, height=500, bg="white")
    fondo.place(x=0, y=0)

    demanda_title = Label(fondo, text='Demanda: ', fg="black", font=("Roboto Slab", 22, "bold") )
    demanda_title.place(x=20, y=20)

    demanda = Label(fondo, text="123456789", fg='black', font=("Roboto Slab", 22, "bold"))
    demanda.place(x=20, y=80)

    vagones_canvas = Canvas(ventana_manual, width=350, height=300, bg='blue')
    vagones_canvas.place(x=0, y=200)

    vagones_title = Label(vagones_canvas, text='Vagones Disponibles: ', fg='black', font=("Roboto Slab", 22, "bold"))
    vagones_title.place(x=20, y=0)

    vagones = Label(vagones_canvas, text="Vagones aqui", fg='black', font=("Roboto Slab", 22, "bold"))
    vagones.place(x=20, y=60)

    shell = Entry(fondo, width=17, bg='#272822', fg='white', insertwidth=10, borderwidth=3,
                  font=("Source Code Pro", 29, "bold"), textvariable=user_entry)
    shell.place(x=385, y=50)

    eng_i = Button(fondo, bg='white', fg='black', text='Enganchar\nal inicio', font=("Roboto Slab", 20, "bold"))
    eng_i.place(x=385, y=120)

    eng_m = Button(fondo, bg='white', fg='black', text='Enganchar\nal medio', font=("Roboto Slab", 20, "bold"))
    eng_m.place(x=585, y=120)

    eng_f = Button(fondo, bg='white', fg='black', text='Enganchar\nal final', font=("Roboto Slab", 20, "bold"))
    eng_f.place(x=385, y=250)

    quitar_v = Button(fondo, bg='white', fg='black', text='Quitar\nvagon', font=("Roboto Slab", 21, "bold"))
    quitar_v.place(x=585, y=250)


    def regresar():
        ventana_manual.destroy()

    def VentanaHelp():
        ventanahelp = Toplevel()
        ventanahelp.title("Help")
        ventanahelp.minsize(200, 200)
        ventanahelp.resizable(width=NO, height=NO)

        S = Scrollbar(ventanahelp)
        help_text = Text(ventanahelp, width=100, height=30)
        S.pack(side=RIGHT, fill=Y)
        help_text.pack(side=LEFT, fill=Y)
        S.config(command=help_text.yview)
        help_text.config(yscrollcommand=S.set)

        body = "Bienvenido a la ventana de ayuda del modo Manual.\n\nEn el cuadro de entrada de texto se deben escribir " \
               "el nombre de alguno de los vagones disponibles que se encuntran en cuadro izquierdo y presionar alguno " \
               "de los siguientes botones: " \
               "\nNote que se debe escribir EXACTAMENTE el nombre del vagon a como se muestra en el cuadro " \
               "de vagones disponibles." \
               "\n\nBotones: \n\nEnganchar al inicio: Se agrega el vagon escrito en la entrada de texto al inicio del tren." \
               "\nEnganchar en el medio: Se agrega el vagon escrito en la entrada de texto en el medio del tren. " \
               "\nEnganchar al final: Se agrega el vagon escrito en la entrada de texto al final del tren. " \
               "\nQuitar vagon: Se libera el vagon escrito en la entrada de texto del tren."

        #           ____________________________
        # __________/ Se crean tags para darle formato al contenido de la pantalla de Ayuda
        help_text.insert(END, body)
        help_text.config(wrap=WORD)
        help_text.tag_add("Body", 1.0, 99.9)
        help_text.tag_config("Body", font=("Roboto Slab", 20))
        help_text.config(state=DISABLED)


        ventanahelp.mainloop()

    imagenvolverbk = cargarImagen("exit.png")
    botonvolver = Button(fondo, image=imagenvolverbk, command=regresar, fg="#000000", bg="#00cc00",
                         activebackground="#cc2900")
    botonvolver.place(x=710, y=420)

    imagenhelp = cargarImagen("help.png")
    botonhelp = Button(fondo, image=imagenhelp, command=VentanaHelp, bg="#00cc00",
                       fg="#000000", activebackground="#cc2900")
    botonhelp.place(x=610, y=420)

    ventana_manual.mainloop()


bgreen = cargarImagen("bgreen.png")
manual_b = Button(consola, image=bgreen, command=ventanaManual, bg='gray')
manual_b.place(x=20, y=10)

manual_l = Label(consola, text="Manual", bg="gray", fg='white', font=("Roboto Slab", 28, "bold"))
manual_l.place(x=60, y=220)

bblue = cargarImagen("bblue.png")
auto_b = Button(consola, image=bblue, command=ventanaManual, bg='gray')
auto_b.place(x=1000, y=10)

manual_l = Label(consola, text="Automatico", bg="gray", fg='white', font=("Roboto Slab", 28, "bold"))
manual_l.place(x=1000, y=220)

ventana_principal.mainloop()
