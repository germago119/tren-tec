#           _____________________________
# __________/BIBLIOTECAS
import os
import random
import csv
from tkinter import *
from tkinter import messagebox

###################################################################################
"""
_________________________________________________________________________________
|                            Tercera Tarea Progradamada                          |
|                              Taller de Programacion                            |
|          Simulador de estación de trenes del Tecnológico de Costa Rica         |
|          ® All Rights Reserved to Kevyn Guadamuz and Roger Valderrama ®        |
|________________________________________________________________________________|
"""
random.seed()  # Mejora la variabilidad del random

#               ____________________________
#______________/
#Lee y asigna las horas de salida de las rutas
rutas = []
m1 = open("rutas.csv", "r")
m1_c = csv.reader(m1)
for nombre, hora in m1_c:
    rutas.append([nombre, hora])
m1.close()


#           ________________________
#__________/ Se define la clase Vagon
class Vagon:
    def __init__(self, nombre=None, num_vagon=None, next=None, prev=None, capacidad_p=None, estado=None):
        self.nombre = nombre
        self.num_vagon = num_vagon
        self.next = next
        self.prev = prev
        self.capacidad_p = capacidad_p
        self.estado = estado

    def valor(self):
        return self.num_vagon

#               _____________________________________________
#______________/Inicializa las instancias de los vagones
"""Lee los datos de los vagones en los archivos csv"""
vagones = []
m2 = open("vagones.csv", "r")
m2_c = csv.reader(m2)
for nombre, numero, capacidad, estado in m2_c:
    vagones.append([nombre, numero, capacidad, estado])
m2.close()


v1 = vagones[0]
v2 = vagones[1]
v3 = vagones[2]
v4 = vagones[3]
v5 = vagones[4]
v6 = vagones[5]
v7 = vagones[6]
v8 = vagones[7]
v9 = vagones[8]
v10 = vagones[9]

vagon1 = Vagon(v1[0], v1[1], None, None, v1[2], v1[3])
vagon2 = Vagon(v2[0], v2[1], None, None, v2[2], v2[3])
vagon3 = Vagon(v3[0], v3[1], None, None, v3[2], v3[3])
vagon4 = Vagon(v4[0], v4[1], None, None, v4[2], v4[3])
vagon5 = Vagon(v5[0], v5[1], None, None, v5[2], v5[3])
vagon6 = Vagon(v6[0], v6[1], None, None, v6[2], v6[3])
vagon7 = Vagon(v7[0], v7[1], None, None, v7[2], v7[3])
vagon8 = Vagon(v8[0], v8[1], None, None, v8[2], v8[3])
vagon9 = Vagon(v9[0], v9[1], None, None, v9[2], v9[3])
vagon10 = Vagon(v10[0], v10[1], None, None, v10[2], v10[3])

vagones_a_evaluar = [vagon1, vagon2, vagon3, vagon4, vagon5, vagon6, vagon7, vagon8, vagon9, vagon10]
####------------------------------------#####


#          ______________________________
#_________/Función que realiza una lista con los vagones que se encuentran disponibles
def vagon_libre(lista):
    vagones_libres = []
    for i in range(len(lista)):
        temp = lista[i]
        if temp.estado == "Libre":
            vagones_libres += [temp]
    return vagones_libres
#####--------------------------------#####


#           ___________________
#__________/Función que Imprime el nombre y la capacidad de los vagones disponibles
#Variable para que se use para printear los vagones disponibles
def print_nombres(lista):
    nombre_disponibles = []
    for i in range(len(lista)):
        temp = lista[i]
        if temp.estado == "Libre":
            nombre_disponibles.append([temp.nombre, temp.capacidad_p])
    return nombre_disponibles


#                ___________________________
#_______________/Se define la clase maquina
class Maquina:
    def __init__(self, num_maquina, capacidad_v):
        self.num_maquina = num_maquina
        self.capacidad_v = capacidad_v


#         ________________________
#________/Se define la clase Tren
class Tren:
    def __init__(self, tren=None, ruta=None, hora=None, num=None, estado=None):
        self.num_tren = tren
        self.ruta = ruta
        self.hora = hora
        self.num_maquina = num
        self.vagones = 0
        self.estado = estado
        self.head = None
        self.tail = None

    #         ________________________
    # ________/Metodo que imprime una lista con valores de los vagones
    def printL(self):
        nodo = self.head
        res = "["
        while nodo != None:
            if nodo.next != None:
                res += str(nodo.valor()) + ","
                nodo = nodo.next
            else:
                res += str(nodo.valor())
                nodo = nodo.next
        res += "]"
        print(res)
        return res

    #         ________________________
    # ________/Metodo que engancha un vagon al inicio
    def enganchar_i(self, num):
        self.vagones += 1
        if self.head == None and self.tail == None: #Cuando no hay vagones enganchados
            self.head = Vagon(num_vagon=num)
            self.tail = self.head
        else:
            self.head = Vagon(num_vagon=num)
            self.tail = self.tail.next

    #         ________________________
    # ________/Metodo que engancha un vagon al final
    def enganchar_f(self, num):
        self.vagones += 1
        temp = self.tail
        temp.next = Vagon(num_vagon=num)
        x = temp.next
        self.tail = x
        x.prev = temp

    #         ________________________
    # ________/Metodo que engancha un vagon en el medio
    def enganchar_m(self, num):
            if self.vagones == 0:
                return self.enganchar_i(num)
            temp = self.head
            medio = self.vagones//2 + 1
            i = 1
            while temp != None:
                if i != medio:
                    temp = temp.next
                    i += 1
                else:
                    temp2 = Vagon(next=temp, prev=temp.prev, num_vagon=num)
                    temp.prev.next = temp2
                    temp.prev = temp2
                    self.vagones += 1
                    break

    #         ________________________
    # ________/Metodo que libera el vagon seleccionado
    def remove(self, valor):
            temp = self.head
            if self.vagones == 0:
                return print("La Lista esta vacia")
            if temp.valor() == valor:
                self.head = temp.next
                return
            while temp.next != None:
                if temp.next.valor() == valor:
                    temp.next = temp.next.next
                    break
                temp = temp.next
            self.vagones -= 1
            return

    #                 ______________________________
    # ________________/Funcion que ejecuta lo automatico
    def auto(self, cantidad):  # Función para los vagones automaticos
        temp = vagon_libre(vagones_a_evaluar)
        i = 0
        conta = 0
        prueba = []
        while conta <= cantidad:
            if i == len(temp):
                print("Cantidad de vagones insuficientes")
                break
            elif self.vagones == 0:
                self.enganchar_i(temp[i].num_vagon)
                temp[i].estado = 'Ocupado'
                prueba += [temp[i].num_vagon]
                conta += int(temp[i].capacidad_p)
                i += 1
            else:
                self.enganchar_f(temp[i].num_vagon)
                temp[i].estado = 'Ocupado'
                prueba += [temp[i].num_vagon]
                conta += int(temp[i].capacidad_p)
                i += 1


#              _________________
#_____________/ Inicializa las instancias de la clase Tren
"""Lee los archivos de tren desde el archivo .csv"""
trenes = []
m3 = open("trenes.csv", "r")  # Se lee el archivo CSV
m3_c = csv.reader(m3)
for tren, ruta, hora, num, estado in m3_c:  # Se crea una sublista con los atributos de los trenes
    trenes.append([tren, ruta, hora, num, estado])


t1 = trenes[0]
t2 = trenes[1]
t3 = trenes[2]
t4 = trenes[3]
t5 = trenes[4]

"""Inicializa las instancias de los trenes"""
tren1 = Tren(t1[0], t1[1], t1[2], t1[3], t1[4])
tren2 = Tren(t2[0], t2[1], t2[2], t2[3], t2[4])
tren3 = Tren(t3[0], t3[1], t3[2], t3[3], t3[4])
tren4 = Tren(t4[0], t4[1], t4[2], t4[3], t4[4])
tren5 = Tren(t5[0], t5[1], t5[2], t5[3], t5[4])


#           _____________
#__________/ Función con el numero aleatorio de pasajeros
def random_pasajeros():
    pasa = (random.randint(1, 700))
    return pasa


#               __________________
#______________/Parte de Interfaz
def cargarImagen(nombre):#Función para cargar las imágenes
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen


#               ___________________
#______________/Interfaz Grafica
ventana_principal = Tk()
ventana_principal.title("Estacion TEC")
ventana_principal.minsize(1560, 1000)
ventana_principal.resizable(width=NO, height=NO)

sky_blue = "#87ceeb"  # Color de fondo

# se crea un Canvas donde iran las imagenes y los demas Canvas
contenedor_principal = Canvas(ventana_principal, width=1560, height=1000, bg=sky_blue)
contenedor_principal.place(x=0, y=0)

# Se definen variables con su respectivo tipo
user_entry = StringVar()
demanda_variable = IntVar()
demanda_variable.set(random_pasajeros())

# Se definen colores para el fondo de los Canvas
bg_r = '#EB6841'
bg_v = '#EDC951'

#Se define el reloj
time_var = 7
time = '{}:00'.format(time_var)

# Se define el Label que sera el reloj
time_clock = Label(contenedor_principal, bg='#272822', fg='white', text=time, font=("Roboto Slab", 60, "bold"))
time_clock.place(x=307, y=5)

# Se crea un label con imagen del Irazu
irazu_frame = cargarImagen('13.png')
irazu = Label(contenedor_principal, bg=sky_blue, image=irazu_frame)
irazu.place(x=750, y=3)

# Se crea un label con imagen de la estacion del TEC
frame_tec = cargarImagen("tec.png")
tec = Label(contenedor_principal, bg=sky_blue, image=frame_tec)
tec.place(x=1105, y=185)

# Se crean dos labels con imagen de los rieles
frame_rail = cargarImagen("rail.png")
rail = Label(contenedor_principal, bg='white', image=frame_rail)
rail.place(x=290, y=600)

rail_2 = Label(contenedor_principal, bg='white', image=frame_rail)
rail_2.place(x=1090, y=600)

# Se crea un label con imagen de la Gran Area Metropolitana
gam_frame = cargarImagen("gam.png")
gam = Label(contenedor_principal, bg=sky_blue, image=gam_frame)
gam.place(x=300, y=180)

# Se crea un canvas para las rutas
canvas_r = Canvas(ventana_principal, width=300, height=550, bg=bg_r)
canvas_r.place(x=0, y=0)

# Se crea un canvas para los vagones disponibles
canvas_v = Canvas(ventana_principal, width=300, height=450, bg=bg_v)
canvas_v.place(x=0, y=550)

# Se crea un canvas para los botones del simulador
consola = Canvas(ventana_principal, width=1260, height=300, bg='gray')
consola.place(x=300, y=700)

# Se crea un label con el titulo del Canvas de rutas
rutas_title = Label(canvas_r, text='Rutas proximas', bg=bg_r, fg='white', font=("Roboto Slab", 24, "bold"))
rutas_title.place(x=10, y=10)

# Se crea un label con la lista de rutas extraido del csv para el Canvas de rutas
rutas_lbl = Label(canvas_r, text="\n".join(map(str, rutas)), bg=bg_r, fg='white', font=("Roboto Slab", 21, "bold"))
rutas_lbl.place(x=10, y=70)

# Se crea un label con el titulo del Canvas de vagones
vagones_title = Label(canvas_v, text='Vagones Disponibles', bg=bg_v, fg='white', font=("Roboto Slab", 20, "bold"))
vagones_title.place(x=10, y=10)

# Se crea un label con la lista de vagones extraido del csv para el Canvas de vagones
vagones_lbl = Label(canvas_v, text="\n".join(map(str, print_nombres(vagones_a_evaluar))), bg=bg_v, fg='white',
                    font=("Roboto Slab", 21, "bold"))
vagones_lbl.place(x=10, y=55)

# Se crea un label para mostrar la demanda
demanda_l = Label(consola, text="Demanda: ", bg="gray", fg='white', font=("Roboto Slab", 32, "bold"))
demanda_l.place(x=300, y=30)

# Se crea un label para mostrar la demanda generada de manera aleatoria
demanda_var = Label(consola, textvariable=demanda_variable, bg="gray", fg='white', font=("Roboto Slab", 32, "bold"))
demanda_var.place(x=520, y=30)

#Se genera el texto para el widget message
body = 'Segun la demanda el programa seleccionara los vagones necesarios para la siguiente salida.\n' \
                        'Si desea puede escoger los vagones de forma manual o permiterle la salida del tren asi.'

#Se crea el Text con el mensaje de la consola
message = Text(consola, height=9, width=87)
message.insert(END, body)
message.config(wrap=WORD)
message.tag_add("Body", 1.0, 99.9)
message.tag_config("Body", background='grey', foreground='white', font=("Roboto Slab", 20))
message.config(state=DISABLED)
message.place(x=270, y=110)

radio_manual = IntVar()  # Variable para las opciones


#        _________
#_______/Ventana para ingresar los vagones manualmente
def ventanaManual():
    ventana_manual = Toplevel()
    ventana_manual.title("Modo Manual")
    ventana_manual.minsize(800, 500)
    ventana_manual.resizable(width=NO, height=NO)

    # Variables con colores para la ventana
    green_m = '#A6E22E'
    bg_entry = '#FD971F'
    bg = '#272822'

    # Se crea un canvas para el fondo de la Ventana
    fondo = Canvas(ventana_manual, width=800, height=500, bg=bg)
    fondo.place(x=0, y=0)

    # Se crea un Label para la demanda
    demanda_title = Label(fondo, text='Demanda: ', fg="white", font=("Roboto Slab", 22, "bold"), bg=bg)
    demanda_title.place(x=385, y=20)

    # Se crea un label para mostrar la demanda generada de manera aleatoria
    demanda = Label(fondo, textvariable=demanda_variable, fg='white', font=("Roboto Slab", 22, "bold"), bg=bg)
    demanda.place(x=540, y=20)

    #Se crea un canvas para los Trenes
    vagones_canvas = Canvas(ventana_manual, width=350, height=500, bg=bg)
    vagones_canvas.place(x=0, y=0)

    # Se crea un Label para mostrar la indicacion sobre trenes
    trenes_title = Label(vagones_canvas, text='Seleccione el tren \na modificar: ', fg='white',
                         font=("Roboto Slab", 22, "bold"), bg=bg)
    trenes_title.place(x=50, y=5)

    #Botones de Opciones
    RBTren1 = Radiobutton(vagones_canvas, text="Tren 1", variable=radio_manual, bg=bg, fg='white',
                          font=("Roboto Slab", 22, "bold"), value=1).place(x=25, y=100)
    RBTren2 = Radiobutton(vagones_canvas, text="Tren 2", variable=radio_manual, bg=bg, fg='white',
                          font=("Roboto Slab", 22, "bold"), value=2).place(x=25, y=140)
    RBTren3 = Radiobutton(vagones_canvas, text="Tren 3", variable=radio_manual, bg=bg, fg='white',
                          font=("Roboto Slab", 22, "bold"), value=3).place(x=25, y=180)
    RBTren4 = Radiobutton(vagones_canvas, text="Tren 4", variable=radio_manual, bg=bg, fg='white',
                          font=("Roboto Slab", 22, "bold"), value=4).place(x=25, y=220)

    # Se crea un Entry para digitar el vagon
    shell = Entry(fondo, width=17, bg=bg_entry, fg='white', insertwidth=10, borderwidth=3,
                  font=("Source Code Pro", 29, "bold"), textvariable=user_entry)
    shell.place(x=385, y=70)

#---------------------------------------------------------------------------------------------------------------------#
    # Se crea el texto para el Text Widget
    mensage = "Seleccione un tren y escriba en la entrada de texto el nombre del vagon que quiere agregar.\n" \
              "La lista de vagones disponibles se encuentra en la ventana principal."
    #Se crea un Text Widget
    nota = Text(vagones_canvas, height=30, width=42)
    nota.insert(END, mensage)
    nota.config(wrap=WORD)
    nota.tag_add("Body", 1.0, 99.9)
    nota.tag_config("Body", background=bg, foreground='white', font=("Roboto Slab", 17))
    nota.config(state=DISABLED)
    nota.place(x=7, y=286)

#---------------------------------------------------------------------------------------------------------------------#
    """Funcion que verifica el comando del boton enganchar al inicio"""
    def verifica_manual_inicio():
        rm = radio_manual.get()
        a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
        if rm == 1 and tren5.estado == "Libre":#Verifica si el tren1 se encuentra en la condicion para ser modificado y asi mismo los vagones
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren5.enganchar_i(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren5.enganchar_i(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren5.enganchar_i(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren5.enganchar_i(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren5.enganchar_i(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren5.enganchar_i(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren5.enganchar_i(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren5.enganchar_i(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren5.enganchar_i(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren5.enganchar_i(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 2 and tren2.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren2.enganchar_i(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren2.enganchar_i(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren2.enganchar_i(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren2.enganchar_i(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren2.enganchar_i(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren2.enganchar_i(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren2.enganchar_i(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren2.enganchar_i(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren2.enganchar_i(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren2.enganchar_i(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 3 and tren3.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren3.enganchar_i(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren3.enganchar_i(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren3.enganchar_i(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren3.enganchar_i(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren3.enganchar_i(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren3.enganchar_i(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren3.enganchar_i(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren3.enganchar_i(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren3.enganchar_i(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren3.enganchar_i(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 4 and tren4.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren4.enganchar_i(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren4.enganchar_i(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren4.enganchar_i(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren4.enganchar_i(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren4.enganchar_i(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren4.enganchar_i(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren4.enganchar_i(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren4.enganchar_i(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren4.enganchar_i(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren4.enganchar_i(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        else:
            vagones_lbl.config(text=a)
            ventana_principal.update()
            messagebox.showerror("Tren NO disponible", "El tren que ha seleccionado no esta disponible \n"
                                                       "O no ha seleccionado ningun tren")
    #------------------------------------------------------------------------------------------------------------------#

    """Funcion que verifica el comando del boton enganchar al medio"""
    def verifica_manual_medio():
        rm = radio_manual.get()
        a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
        if rm == 1 and tren5.estado == "Libre":  #Verifica si el tren1 se encuentra en la condicion para ser modificado y asi mismo los vagones
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren5.enganchar_m(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren5.enganchar_m(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren5.enganchar_m(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren5.enganchar_m(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren5.enganchar_m(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren5.enganchar_m(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren5.enganchar_m(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren5.enganchar_m(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren5.enganchar_m(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren5.enganchar_m(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 2 and tren2.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren2.enganchar_m(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren2.enganchar_m(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren2.enganchar_m(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren2.enganchar_m(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren2.enganchar_m(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren2.enganchar_m(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren2.enganchar_m(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren2.enganchar_m(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren2.enganchar_m(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren2.enganchar_m(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 3 and tren3.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren3.enganchar_m(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren3.enganchar_m(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren3.enganchar_m(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren3.enganchar_m(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren3.enganchar_m(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren3.enganchar_m(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren3.enganchar_m(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren3.enganchar_m(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren3.enganchar_m(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren3.enganchar_m(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 4 and tren4.estado == "Libre":
            if shell.get() == "vagon1"and vagon1.estado == "Libre":
                tren4.enganchar_m(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2"and vagon2.estado == "Libre":
                tren4.enganchar_m(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3"and vagon3.estado == "Libre":
                tren4.enganchar_m(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4"and vagon4.estado == "Libre":
                tren4.enganchar_m(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5"and vagon5.estado == "Libre":
                tren4.enganchar_m(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6"and vagon6.estado == "Libre":
                tren4.enganchar_m(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7"and vagon7.estado == "Libre":
                tren4.enganchar_m(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8"and vagon8.estado == "Libre":
                tren4.enganchar_m(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9"and vagon9.estado == "Libre":
                tren4.enganchar_m(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren4.enganchar_m(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        else:
            vagones_lbl.config(text=a)
            ventana_principal.update()
            messagebox.showerror("Tren NO disponible", "El tren que ha seleccionado no esta disponible")

    #----------------------------------------------------------------------------------------------------------------#

    """Funcion que verifica el comando del boton enganchar al final"""
    def verifica_manual_final():
        rm = radio_manual.get()
        a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
        if rm == 1 and tren5.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Libre":
                tren5.enganchar_f(vagon2.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Libre":
                tren5.enganchar_f(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Libre":
                tren5.enganchar_f(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Libre":
                tren5.enganchar_f(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Libre":
                tren5.enganchar_f(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Libre":
                tren5.enganchar_f(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Libre":
                tren5.enganchar_f(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Libre":
                tren5.enganchar_f(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Libre":
                tren5.enganchar_f(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren5.enganchar_f(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 2 and tren2.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Libre":
                tren2.enganchar_f(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Libre":
                tren2.enganchar_f(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Libre":
                tren2.enganchar_f(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Libre":
                tren2.enganchar_f(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Libre":
                tren2.enganchar_f(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Libre":
                tren2.enganchar_f(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Libre":
                tren2.enganchar_f(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Libre":
                tren2.enganchar_f(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Libre":
                tren2.enganchar_f(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren2.enganchar_f(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 3 and tren3.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Libre":
                tren3.enganchar_f(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Libre":
                tren3.enganchar_f(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Libre":
                tren3.enganchar_f(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Libre":
                tren3.enganchar_f(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Libre":
                tren3.enganchar_f(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Libre":
                tren3.enganchar_f(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Libre":
                tren3.enganchar_f(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Libre":
                tren3.enganchar_f(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Libre":
                tren3.enganchar_f(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren3.enganchar_f(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 4 and tren4.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Libre":
                tren4.enganchar_f(vagon1.num_vagon)
                vagon1.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Libre":
                tren4.enganchar_f(vagon2.num_vagon)
                vagon2.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Libre":
                tren4.enganchar_f(vagon3.num_vagon)
                vagon3.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Libre":
                tren4.enganchar_f(vagon4.num_vagon)
                vagon4.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Libre":
                tren4.enganchar_f(vagon5.num_vagon)
                vagon5.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Libre":
                tren4.enganchar_f(vagon6.num_vagon)
                vagon6.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Libre":
                tren4.enganchar_f(vagon7.num_vagon)
                vagon7.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Libre":
                tren4.enganchar_f(vagon8.num_vagon)
                vagon8.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Libre":
                tren4.enganchar_f(vagon9.num_vagon)
                vagon9.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Libre":
                tren4.enganchar_f(vagon10.num_vagon)
                vagon10.estado = "Ocupado"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        else:
            vagones_lbl.config(text=a)
            ventana_principal.update()
            messagebox.showerror("Tren NO disponible", "El tren que ha seleccionado no esta disponible")

    #---------------------------------------------------------------------------------------------------------------#
    """Funcion que verifica el comando de quitar vagon"""
    def quitar_vagon():
        rm = radio_manual.get()
        a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
        if rm == 1 and tren5.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Ocupado":
                tren5.remove(1)
                vagon1.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Ocupado":
                tren5.remove(2)
                vagon2.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Ocupado":
                tren5.remove(3)
                vagon3.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Ocupado":
                tren5.remove(4)
                vagon4.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Ocupado":
                tren5.remove(5)
                vagon5.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Ocupado":
                tren5.remove(6)
                vagon6.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Ocupado":
                tren5.remove(7)
                vagon7.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Ocupado":
                tren5.remove(8)
                vagon8.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Ocupado":
                tren5.remove(9)
                vagon9.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Ocupado":
                tren5.remove(10)
                vagon10.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra libre")
        elif rm == 2 and tren2.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Ocupado":
                tren2.remove(1)
                vagon1.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Ocupado":
                tren2.remove(2)
                vagon2.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Ocupado":
                tren2.remove(3)
                vagon3.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Ocupado":
                tren2.remove(4)
                vagon4.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Ocupado":
                tren2.remove(5)
                vagon5.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Ocupado":
                tren2.remove(6)
                vagon6.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Ocupado":
                tren2.remove(7)
                vagon7.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Ocupado":
                tren2.remove(8)
                vagon8.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Ocupado":
                tren2.remove(9)
                vagon9.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Ocupado":
                tren2.remove(10)
                vagon10.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 3 and tren3.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Ocupado":
                tren3.remove(1)
                vagon1.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Ocupado":
                tren3.remove(2)
                vagon2.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Ocupado":
                tren3.remove(3)
                vagon3.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Ocupado":
                tren3.remove(4)
                vagon4.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Ocupado":
                tren3.remove(5)
                vagon5.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Ocupado":
                tren3.remove(6)
                vagon6.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Ocupado":
                tren3.remove(7)
                vagon7.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Ocupado":
                tren3.remove(8)
                vagon8.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Ocupado":
                tren3.remove(9)
                vagon9.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Ocupado":
                tren3.remove(10)
                vagon10.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        elif rm == 4 and tren4.estado == "Libre":
            if shell.get() == "vagon1" and vagon1.estado == "Ocupado":
                tren4.remove(1)
                vagon1.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon2" and vagon2.estado == "Ocupado":
                tren4.remove(2)
                vagon2.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon3" and vagon3.estado == "Ocupado":
                tren4.remove(3)
                vagon3.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon4" and vagon4.estado == "Ocupado":
                tren4.remove(4)
                vagon4.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon5" and vagon5.estado == "Ocupado":
                tren4.remove(5)
                vagon5.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon6" and vagon6.estado == "Ocupado":
                tren4.remove(6)
                vagon6.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon7" and vagon7.estado == "Ocupado":
                tren4.remove(7)
                vagon7.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon8" and vagon8.estado == "Ocupado":
                tren4.remove(8)
                vagon8.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon9" and vagon9.estado == "Ocupado":
                tren4.remove(9)
                vagon9.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            elif shell.get() == "vagon10" and vagon10.estado == "Ocupado":
                tren4.remove(10)
                vagon10.estado = "Libre"
                vagones_lbl.config(text=a)
                ventana_principal.update()
            else:
                vagones_lbl.config(text=a)
                ventana_principal.update()
                messagebox.showerror("No seleccionó un vágon", "Por favor escriba el vagón a utilizar \n"
                                                               "o el vagon seleccionado se encuentra ocupado")
        else:
            vagones_lbl.config(text=a)
            ventana_principal.update()
            messagebox.showerror("Tren NO disponible", "El tren que ha seleccionado no esta disponible")

    #Mensaje que ayuda con la información de los trenes en modo manual
    def info_tren():
        rm = radio_manual.get()
        if rm == 1:
            messagebox.showinfo("Informacion sobre el tren modificado", "El tren seleccionado es el 1 \n"
                                "Los vagones utilizados por el tren son:" + str(tren5.printL()))
        elif rm == 2:
            messagebox.showinfo("Informacion sobre el tren modificado", "El tren seleccionado es el 2 \n"
                                                                        "Los vagones utilizados por el tren son:" + str(
                tren2.printL()))

        elif rm == 3:
            messagebox.showinfo("Informacion sobre el tren modificado", "El tren seleccionado es el 3 \n"
                                                                        "Los vagones utilizados por el tren son:" + str(
                tren3.printL()))

        elif rm == 4:
            messagebox.showinfo("Informacion sobre el tren modificado", "El tren seleccionado es el 4 \n"
                                                                        "Los vagones utilizados por el tren son:" + str(
                tren4.printL()))
        else:
            messagebox.showerror("No selecciono ningún tren", "No se ha seleccionado ningun tren")

    #Funcion que hace que el tren parta de la estación
    def partir_tren():
        rm = radio_manual.get()
        if rm == 1 and tren5.estado == "Libre":
            if tren5.vagones == 0:
                messagebox.showerror("No esta autorizado", "El tren no posee vagones enganchados")
            else:
                messagebox.showinfo("¡TODOS A BORDO!", "El tren 1 partira de la estación en este momento \n"
                                                       "Buen Viaje")
                tren5.estado = "Ocupado"
                verificar_vagones(tren5.vagones)

        elif rm == 2 and tren2.estado == "Libre":
            if tren2.vagones == 0:
                messagebox.showerror("No esta autorizado", "El tren no posee vagones enganchados")
            else:
                messagebox.showinfo("¡TODOS A BORDO!", "El tren  partira de la estación en este momento \n"
                                                       "Buen Viaje")
                tren2.estado = "Ocupado"
                verificar_vagones(tren2.vagones)

        elif rm == 3 and tren3.estado == "Libre":
            if tren3.vagones == 0:
                messagebox.showerror("No esta autorizado", "El tren no posee vagones enganchados")
            else:
                messagebox.showinfo("¡TODOS A BORDO!", "El tren 3 partira de la estación en este momento \n"
                                                       "Buen Viaje")
                tren3.estado = "Ocupado"
                verificar_vagones(tren3.vagones)


        elif rm == 4 and tren4.estado == "Libre":
            if tren4.vagones == 0:
                messagebox.showerror("No esta autorizado", "El tren no posee vagones enganchados")
            else:
                messagebox.showinfo("¡TODOS A BORDO!", "El tren 4 partira de la estación en este momento \n"
                                                       "Buen Viaje")
                tren4.estado = "Ocupado"
                verificar_vagones(tren4.vagones)
        else:
            messagebox.showerror("No selecciono ningún tren", "No se ha seleccionado ningun tren\n"
                                                              "O el tren seleccionado ya no se encuentra en la estación")

    # ----------------------------------------------------------------------------------------------------------------#
    #        _________
    # _______/Botones con los comandos para unir y quitar vagones de forma manual
    eng_i = Button(fondo, fg='white', text='Enganchar\nal inicio', font=("Roboto Slab", 20, "bold"), bg=bg,
                   command=verifica_manual_inicio)
    eng_i.place(x=385, y=140)

    eng_m = Button(fondo, fg='white', text='Enganchar\nal medio', font=("Roboto Slab", 20, "bold"), bg=bg,
                   command=verifica_manual_medio)
    eng_m.place(x=585, y=140)

    eng_f = Button(fondo, fg='white', text='Enganchar\nal final', font=("Roboto Slab", 20, "bold"), bg=bg,
                   command=verifica_manual_final)
    eng_f.place(x=385, y=270)

    quitar_v = Button(fondo, fg='white', text='Quitar\nvagon', font=("Roboto Slab", 21, "bold"), bg=bg,
                      command=quitar_vagon)
    quitar_v.place(x=585, y=270)

    #Funcion para cerrar la ventana
    def regresar():
        ventana_manual.destroy()

    #Funcion de ventana auxiliar con ayuda
    def VentanaHelp():
        ventanahelp = Toplevel()
        ventanahelp.title("Help")
        ventanahelp.minsize(200, 200)
        ventanahelp.resizable(width=NO, height=NO)

        #Se crea un scrollbar para el texto
        S = Scrollbar(ventanahelp)
        help_text = Text(ventanahelp, width=100, height=30)
        S.pack(side=RIGHT, fill=Y)
        help_text.pack(side=LEFT, fill=Y)
        S.config(command=help_text.yview)
        help_text.config(yscrollcommand=S.set)

        #Se crea el texto para el widget de Texto
        body = "Bienvenido a la ventana de ayuda del modo Manual.\n\nEn el cuadro de entrada de texto se " \
               "deben escribir " \
               "el nombre de alguno de los vagones disponibles que se encuntran en cuadro izquierdo y " \
               "presionar alguno " \
               "de los siguientes botones: " \
               "\nNote que se debe escribir EXACTAMENTE el nombre del vagon a como se muestra en el cuadro " \
               "de vagones disponibles." \
               "\n\nBotones: \n\nEnganchar al inicio: Se agrega el vagon escrito en la entrada de texto al " \
               "inicio del tren." \
               "\nEnganchar en el medio: Se agrega el vagon escrito en la entrada de texto en el medio del tren. " \
               "\nEnganchar al final: Se agrega el vagon escrito en la entrada de texto al final del tren. " \
               "\nQuitar vagon: Se libera el vagon escrito en la entrada de texto del tren."

        #            ____________________________
        # __________/ Se crean tags para darle formato al contenido de la pantalla de Ayuda
        help_text.insert(END, body)  # Se inserta el texto al Text
        help_text.config(wrap=WORD)  # se justifica para que no corte las palabras
        help_text.tag_add("Body", 1.0, 99.9)  # Se crea un tag
        help_text.tag_config("Body", font=("Roboto Slab", 20))  # Se da formato al tag
        help_text.config(state=DISABLED)  # Se desabilita la seleccion de texto

        ventanahelp.mainloop()
    #_______________________________________________________________________________________________________________#
    #        _________
    # _______/Botones en el extremo inferior de la Ventana
    wagon = cargarImagen("tr_b.png")
    train_status = Button(fondo, image=wagon, command=info_tren, bg=green_m, activebackground=bg_entry)
    train_status.place(x=520, y=425)

    imagenplay = cargarImagen("play.png")
    botonplay = Button(fondo, image=imagenplay, command=partir_tren, bg=green_m,
                         activebackground=bg_entry)
    botonplay.place(x=710, y=425)

    imagenvolverbk = cargarImagen("exit.png")
    botonvolver = Button(fondo, image=imagenvolverbk, command=regresar, bg=green_m,
                         activebackground=bg_entry)
    botonvolver.place(x=360, y=425)

    imagenhelp = cargarImagen("help.png")
    botonhelp = Button(fondo, image=imagenhelp, command=VentanaHelp, bg=green_m, activebackground=bg_entry)
    botonhelp.place(x=440, y=425)

    ventana_manual.mainloop()

#Se define la variable como int
radio = IntVar()


#        _______________________________
#_______/Ventana que realiza el ajuste automatico de los vagones
def ventanaAuto():
    ventana_auto = Toplevel()
    ventana_auto.title("Modo Automatico")
    ventana_auto.minsize(350, 200)
    ventana_auto.resizable(width=NO, height=NO)

    # Se crean variables para los colores
    bg = '#272822'
    w = 'white'

    # Se crea el Canvas de fondo
    fondo = Canvas(ventana_auto, width=350, height=200, bg=bg)
    fondo.place(x=0, y=0)

    #Se crea un Label con texto para el titulo
    title = Label(ventana_auto, text='Seleccione un Tren\ndisponible', fg=w, bg=bg, font=("Roboto Slab", 24, "bold"))
    title.place(x=10, y=10)

    """Botones de opciones"""

    RBTren1 = Radiobutton(ventana_auto, text="Tren 1", variable=radio, bg=bg, fg=w,
                          font=("Roboto Slab", 22, "bold"), value=1, command=evalua)
    RBTren1.place(x=10, y=100)

    RBTren2 = Radiobutton(ventana_auto, text="Tren 2", variable=radio, bg=bg, fg=w,
                          font=("Roboto Slab", 22, "bold"), value=2, command=evalua)
    RBTren2.place(x=10, y=140)

    RBTren3 = Radiobutton(ventana_auto, text="Tren 3", variable=radio, bg=bg, fg=w,
                          font=("Roboto Slab", 22, "bold"), value=3, command=evalua)
    RBTren3.place(x=170, y=100)

    RBTren4 = Radiobutton(ventana_auto, text="Tren 4", variable=radio, bg=bg, fg=w,
                          font=("Roboto Slab", 22, "bold"), value=4, command=evalua)
    RBTren4.place(x=170, y=140)


#Funcion que evalua los CheckButton seleccionados
def evalua():
    r = radio.get()
    a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
    if r == 1 and tren5.estado == "Libre":
        tren5.auto(demanda_variable.get())
        messagebox.showinfo("Los vagones que añadieron al Tren 1 son: ",
                            str(tren5.printL() + " \nSaldra de la estación en este momento "))
        tren5.printL()
        tren5.estado = "Ocupado"
        vagones_lbl.config(text=a)
        ventana_principal.update()
        verificar_vagones(tren5.vagones)
        actualiza()

    elif r == 2 and tren2.estado == "Libre":
        tren2.auto(demanda_variable.get())
        messagebox.showinfo("Los vagones que añadieron al Tren 2 son: ",
                            str(tren2.printL() + " \nSaldra de la estación en este momento "))
        tren2.printL()
        tren2.estado = "Ocupado"
        vagones_lbl.config(text=a)
        ventana_principal.update()
        verificar_vagones(tren2.vagones)
        actualiza()

    elif r == 3 and tren3.estado == "Libre":
        tren3.auto(demanda_variable.get())
        messagebox.showinfo("Los vagones que añadieron al Tren 3 son: ",
                            str(tren3.printL() + " \nSaldra de la estación en este momento "))
        tren3.printL()
        tren3.estado = "Ocupado"
        vagones_lbl.config(text=a)
        ventana_principal.update()
        verificar_vagones(tren3.vagones)
        actualiza()

    elif r == 4 and tren4.estado == "Libre":
        tren4.auto(demanda_variable.get())
        messagebox.showinfo("Los vagones que añadieron al Tren 4 son: ",
                            str(tren4.printL() + " \nSaldra de la estación en este momento "))
        tren4.printL()
        tren4.estado = "Ocupado"
        vagones_lbl.config(text=a)
        ventana_principal.update()
        verificar_vagones(tren4.vagones)
        actualiza()

    else:
        messagebox.showerror("Tren no disponible", "El tren que ha seleccionado no se encuentra disponible")


#Funcion que actualiza la demanda
def actualiza():
    demanda_variable.set(random_pasajeros())


#Funcion que actualiza la lista de vagones disponibles
def actualiza2():
    a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
    vagones_lbl.config(text=a)
    ventana_principal.update()


##-----------------------------------------------------------------------##
#           ____________
#__________/Animaciones
# Frames de Trenes por cantidad de vagones y orientacion
train_wg1_frames = [['tbk1.png', 'tbk1.1.png', 'tbk1.2.png', 'tbk1.3.png'],
                    ['tr1.png', 'tr1.1.png', 'tr1.2.png', 'tr1.3.png'],
                    ['tbl1.png', 'tbl1.1.png', 'tbl1.2.png', 'tbl1.3.png']]

train_wg2_frames = [['tbk2.png', 'tbk2.1.png', 'tbk2.2.png', 'tbk2.3.png'],
                    ['tr2.png', 'tr2.1.png', 'tr2.2.png', 'tr2.3.png'],
                    ['tbl2.png', 'tbl2.1.png', 'tbl2.2.png', 'tbl2.3.png']]

train_wg3_frames = [['tbk3.png', 'tbk3.1.png', 'tbk3.2.png', 'tbk3.3.png'],
                    ['tr3.png', 'tr3.1.png', 'tr3.2.png', 'tr3.3.png'],
                    ['tbl3.png', 'tbl3.1.png', 'tbl3.2.png', 'tbl3.3.png']]

train_wg1_frames_reverse = [['tbk1r.png', 'tbk1.1r.png', 'tbk1.2r.png', 'tbk1.3r.png'],
                          ['tr1r.png', 'tr1.1r.png', 'tr1.2r.png', 'tr1.3r.png'],
                          ['tbl1r.png', 'tbl1.1r.png', 'tbl1.2r.png', 'tbl1.3r.png']]

train_wg2_frames_reverse = [['tbk2r.png', 'tbk2.1r.png', 'tbk2.2r.png', 'tbk2.3r.png'],
                           ['tr2r.png', 'tr2.1r.png', 'tr2.2r.png', 'tr2.3r.png'],
                           ['tbl2r.png', 'tbl2.1r.png', 'tbl2.2r.png', 'tbl2.3r.png']]

train_wg3_frames_reverse = [['tbk3r.png', 'tbk3.1r.png', 'tbk3.2r.png', 'tbk3.3r.png'],
                            ['tr3r.png', 'tr3.1r.png', 'tr3.2r.png', 'tr3.3r.png'],
                            ['tbl3r.png', 'tbl3.1r.png', 'tbl3.2r.png', 'tbl3.3r.png']]


#Verifica cuantos vagones tiene el tren para llamar a la animación correspondiente
def verificar_vagones(vagones):
    if vagones == 1:
        return right_wg1()
    if vagones == 2:
        return right_wg2()
    if vagones >= 3:
        return right_wg3()

def time_up():
    global time_var
    time_var += 1
    a = '{}:00'.format(time_var)
    time_clock.config(text=a)
    ventana_principal.update()


#Animacion de salida con un vagon
def right_wg1():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = 1600
    frame = cargarImagen(train_wg1_frames[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren -= 5
        if x_tren < -200:
            break
        ventana_principal.update()
    actualiza2()


#Animacion de salida con dos vagones
def right_wg2():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = 1620
    frame = cargarImagen(train_wg2_frames[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren -= 6
        if x_tren < -400:
            break
        ventana_principal.update()
    actualiza2()


#Animacion de salida con tres vagones
def right_wg3():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = 1620
    frame = cargarImagen(train_wg3_frames[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren -= 7
        if x_tren < -600:
            break
        ventana_principal.update()
    actualiza2()


#Animacion de llegada con un vagon
def left_wg1():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = -300
    frame = cargarImagen(train_wg1_frames_reverse[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren += 5
        if x_tren > 1650:
            break
        ventana_principal.update()
    actualiza2()


#Animacion de llegada con dos vagones
def left_wg2():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = -400
    frame = cargarImagen(train_wg2_frames_reverse[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren += 6
        if x_tren > 1650:
            break
        ventana_principal.update()
    actualiza2()


#Animacion de llegada con tres vagones
def left_wg3():
    time_up()
    tren = random.randint(0, 2)
    vagon = random.randint(0, 3)
    x_tren = -630
    frame = cargarImagen(train_wg3_frames_reverse[tren][vagon])
    tren_l = Label(contenedor_principal, bg=sky_blue, image=frame)
    while True:
        tren_l.place(x=x_tren, y=502)
        x_tren += 7
        if x_tren > 1650:
            break
        ventana_principal.update()
    actualiza2()


def refresh():
    vagon1.estado = "Libre"
    vagon2.estado = "Libre"
    vagon3.estado = "Libre"
    vagon4.estado = "Libre"
    vagon5.estado = "Libre"
    vagon6.estado = "Libre"
    vagon7.estado = "Libre"
    vagon8.estado = "Libre"
    vagon9.estado = "Libre"
    vagon10.estado = "Libre"
    tren5.estado = "Libre"
    tren2.estado = "Libre"
    tren3.estado = "Libre"
    tren3.estado = "Libre"
    a = "\n".join(map(str, print_nombres(vagones_a_evaluar)))
    vagones_lbl.config(text=a)
    ventana_principal.update()


#           ____________
#__________/Botones de la consola en la Ventana Principal y su respectivo Label con su nombre

bgreen = cargarImagen("bgreen.png")
manual_b = Button(consola, image=bgreen, command=ventanaManual, bg='gray')
manual_b.place(x=20, y=10)

manual_l = Label(consola, text="Manual", bg="gray", fg='white', font=("Roboto Slab", 28, "bold"))
manual_l.place(x=50, y=220)

bblue = cargarImagen("bblue.png")
auto_b = Button(consola, image=bblue, command=ventanaAuto, bg='gray')
auto_b.place(x=1000, y=10)

manual_l = Label(consola, text="Automatico", bg="gray", fg='white', font=("Roboto Slab", 28, "bold"))
manual_l.place(x=1000, y=220)

#Boton de RESET
brefresh = cargarImagen("refresh.png")
refresh_b = Button(ventana_principal, image=brefresh, command=refresh, bg='gray')
refresh_b.place(x=550, y=5)
#reverse 1
left1 = Button(ventana_principal, image=brefresh, command=left_wg1, bg='gray')
left1.place(x=600, y=5)
#reverse 2
left2 = Button(ventana_principal, image=brefresh, command=left_wg2, bg='gray')
left2.place(x=550, y=30)
#reverse 3
left3 = Button(ventana_principal, image=brefresh, command=left_wg3, bg='gray')
left3.place(x=600, y=30)


ventana_principal.mainloop()
