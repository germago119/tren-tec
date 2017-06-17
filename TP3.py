import os
import time
import random
import csv
from tkinter import *
from threading import Thread

 #  ANTES DE HACER INTERFAZ Y PENSAR SOBRE TKINTER O PYGAME HAGAMOS TODA LA LOGICA DE PUNTEROS PRIMERO Y TRATAEMOS DE
 #  TERMIANR ESTO ANTES DEL VIERNES PARA TENER LA OTRA SEMANA SOLO PARA INTERFAZ Y ANIMACIONES...

random.seed()  # Mejora la variabilidad del random

A_TEC = ""
SJ_TEC = ""
TEC_SJ = ""
TEC_A = ""



#               ____________________________
#______________/
#Lee y asigna las horas de salida de las rutas
rutas = []
m1 = open("rutas.csv", "r")
m1_c = csv.reader(m1)
for nombre, hora in m1_c:
    rutas.append([nombre, hora])
m1.close()



#           _________________
#__________/ Se define la clase Vagon
class Vagon:
    def __init__(self, nombre = None, num_vagon=None, next=None, prev=None, capacidad_p=None, estado = None):
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
m2 = open("vagones_prueba.csv", "r")
m2_c = csv.reader(m2)
for nombre, numero, capacidad, estado in m2_c:
    vagones.append([nombre, numero, capacidad, estado])
m2.close()


v1=vagones[0]
v2=vagones[1]
v3=vagones[2]
v4=vagones[3]
v5=vagones[4]
v6=vagones[5]
v7=vagones[6]
v8=vagones[7]
v9=vagones[8]
v10=vagones[9]

vagon1 = Vagon(v1[0], v1[1],None,None,v1[2],v1[3])
vagon2 = Vagon(v2[0], v2[1],None,None,v2[2],v2[3])
vagon3 = Vagon(v3[0], v3[1],None,None,v3[2],v3[3])
vagon4 = Vagon(v4[0], v4[1],None,None,v4[2],v4[3])
vagon5 = Vagon(v5[0], v5[1],None,None,v5[2],v5[3])
vagon6 = Vagon(v6[0], v6[1],None,None,v6[2],v6[3])
vagon7 = Vagon(v7[0], v7[1],None,None,v7[2],v7[3])
vagon8 = Vagon(v8[0], v8[1],None,None,v8[2],v8[3])
vagon9 = Vagon(v9[0], v9[1],None,None,v9[2],v9[3])
vagon10 = Vagon(v10[0], v10[1],None,None,v10[2],v10[3])

vagones_a_evaluar=[vagon1,vagon2,vagon3,vagon4,vagon5,vagon6,vagon7,vagon8,vagon9,vagon10]
####------------------------------------#####

#          ______________________________
#_________/Función que realiza una lista con los vagones que se encuentran disponibles
def vagon_libre(lista):
    vagones_libres = []
    for i in range(len(lista)):
        temp = lista[i]
        if temp.estado == 'Libre':
            vagones_libres += [temp]
    return vagones_libres
#####--------------------------------#####

#           ___________________
#__________/Función que Imprime el nombre y la capacidad de los vagones disponibles

para_print= vagon_libre(vagones_a_evaluar) #Variable para que se use para printear los vagones disponibles
def print_nombres(lista):
    nombre_disponibles = []
    for i in range(len(lista)):
        temp = lista[i]
        nombre_disponibles.append([temp.nombre, temp.capacidad_p])
    print(nombre_disponibles)

#def print_rutas(ruta)

#                ______________________
#_______________/
class Maquina:
    def __init__(self, num_maquina, capacidad_v):
        self.num_maquina = num_maquina
        self.capacidad_v = capacidad_v

class Tren:
    def __init__(self, tren, ruta, hora, num):
        self.num_tren = tren
        self.ruta = ruta
        self.hora = hora
        self.num_maquina = num
        self.vagones = 0
        self.head = None
        self.tail = None

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

    def enganchar_i(self, num):
        self.vagones += 1
        if self.head == None and self.tail == None: #Cuando no hay vagones enganchados
            self.head = Vagon(num_vagon=num)
            self.tail = self.head
        else:
            self.head = Vagon(num_vagon=num)
            self.tail = self.tail.next


    def enganchar_f(self, num):
        self.vagones += 1
        temp = self.tail
        temp.next = Vagon(num_vagon=num)
        x = temp.next
        self.tail = x
        x.prev = temp


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
            self.vagones -=1
            return

    #                 ______________________________
    # ________________/Funcion que ejecuta lo automatico(No terminada)
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
                temp[i].estado = "Ocupado"
                prueba += [temp[i].num_vagon]
                conta += int(temp[i].capacidad_p)
                i += 1


            else:
                self.enganchar_f(temp[i].num_vagon)
                temp[i].estado = "Ocupado"
                prueba += [temp[i].num_vagon]
                conta += int(temp[i].capacidad_p)
                i += 1
        print(prueba)

    #def exit(self):
        #self._del_()

    #def llegar(self):
        #Lee documento de Config
       #self.__init__(tren, ruta, hora, maquina, vagones)



#           _____________
#__________/ Función con el numero aleatorio de pasajeros
def random_pasajeros():
    pasa = (random.randrange(0, 101))
    return pasa



#                __________________
#______________/Parte de Interfaz
def cargarImagen(nombre):#Función para cargar las imágenes
    ruta = os.path.join('Imagenes', nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

root = Tk()
root.title("Estacion de Tren del TEC")
root.minsize(1100, 900)
canvas_fondo = Canvas(root, width = 1100, height = 900, bg = "#000000" )
canvas_fondo.place(x=0, y = 0)


fondo = cargarImagen("estacion.png")
lbl_fondo = Label(canvas_fondo, bg='white')
lbl_fondo.config(image=fondo)
lbl_fondo.place(x=0, y=0)

lbl_rutas= Label(root, text = "Rutas Disponibles", font=("Comic Sans MS", 18), bg= "grey", fg = "white")
lbl_rutas.pack()
lbl_rutas.place(x= 825, y = 150)
lbl_a_tec = Label(root, text = "Alajuela-TEC", font=("Comic Sans MS", 18), bg= "grey", fg = "white")
lbl_a_tec.pack()
lbl_a_tec.place(x= 825, y = 200)
lbl_sj_tec = Label(root, text = "San Jose-TEC", font=("Comic Sans MS", 18), bg= "grey", fg = "white")
lbl_sj_tec.pack()
lbl_sj_tec.place(x= 825, y = 250)
lbl_tec_a = Label(root, text = "TEC-Alajuela", font=("Comic Sans MS", 18), bg= "grey", fg = "white")
lbl_tec_a.pack()
lbl_tec_a.place(x= 825, y = 300)
lbl_tec_sj = Label(root, text = "TEC-San Jose", font=("Comic Sans MS", 18), bg= "grey", fg = "white")
lbl_tec_sj.pack()
lbl_tec_sj.place(x= 825, y = 350)

#               _________________________
#______________/Animacion del Reloj
"""clock = Label(root, font=('Consolas', 40), bg="Black", fg="green")
clock.pack()
clock.place (x=800, y=70)
time1 = ""
def reloj ():
    global time1
    time2 = time.strftime ('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.configure (text=time2)
    clock.after(500,reloj)

a = Thread(target = reloj, args = ())
a.start()"""
#-----------------------------------------------#


"""x = Tren("thomas","s-c", 13, 2)
x.printL()
x.auto(100)
x.printL()
b = Tren("Ricardo","s-c", 13, 2)
b.auto(100)
b.printL()
a = Tren("Lola", "SS", 13, 2)
a.auto(600)
print(print_nombres(vagon_libre(vagones_a_evaluar)))"""
root.mainloop()
