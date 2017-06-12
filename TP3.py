import os
import time
import random
import csv

#ANTES DE HACER INTERFAZ Y PENSAR SOBRE TKINTER O PYGAME HAGAMOS TODA LA LOGICA DE PUNTEROS PRIMERO Y TRATAEMOS DE
#TERMIANR ESTO ANTES DEL VIERNES PARA TENER LA OTRA SEMANA SOLO PARA INTERFAZ Y ANIMACIONES...

random.seed() #Mejora la variabilidad del random

# f = open('estacion.txt')

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0],row[1],row[2])

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

    #def exit(self):
        #self._del_()

    #def llegar(self):
        #Lee documento de Config
       #self.__init__(tren, ruta, hora, maquina, vagones)



class Vagon:
    def __init__(self, num_vagon=None, next=None, prev=None, capacidad_p=None, estado = 0):#Estado = 0 si el vagon esta desocupado, si es 1 el vagon esta ocupado
        self.num_vagon = num_vagon
        self.next = next
        self.prev = prev
        self.capacidad_p = capacidad_p
        self.estado  = estado


    def valor(self):
        return self.num_vagon



#Lee el archivo con la info de los trenes
vagones = []
with open('vagones_prueba.csv', 'r') as archivo:
    lista = archivo.read().splitlines()
    lista.pop(0)
    for l in lista:
        linea = l.split(";")
        if linea[3] == '0':
            vagones.append(linea[2])
            print("hola")


def auto(cantidad): #Función para los vagones automaticos
    temp = vagones
    indice = 0
    conta = 0
    while conta <= cantidad:
        if temp == []:
            print("Cantidad de vagones insuficientes")
            break
        elif str(temp[0]) < str(cantidad):
            Tren.self.enganchar_f(indice)
            conta += cantidad
            print('si entro al ciclo')
        else:
            break


auto(50)

"""class Nodo:
    def __init__(self, next=None, prev=None, valor=None):
        self.next = next
        self.prev = prev
        self.valor = valor

    def __str__(self):
        return self.valor

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.largo = 0

    def printL(self):
        nodo = self.head
        res = "["
        while nodo != None:
            if nodo.next != None:
                res += str(nodo.__str__()) + ","
                nodo = nodo.next
            else:
                res += str(nodo.__str__())
                nodo = nodo.next
        res += "]"
        print(res)

    def rprintL(self):
        nodo = self.tail
        res = "["
        while nodo != None:
            if nodo.prev != None:
                res += str(nodo.__str__()) + ","
                nodo = nodo.prev
            else:
                res += str(nodo.__str__())
                nodo = nodo.prev
        res += "]"
        print(res)

    def appe(self, value):
        self.largo += 1
        if self.head == None and self.tail == None:  # lista vacia.
            self.head = Nodo(valor=value)
            self.tail = self.head
        else:
            temp = self.tail
            temp.next = Nodo(valor=value)
            x = temp.next
            self.tail = x
            x.prev = temp

    def _del_(self, valor):
        temp = self.head
        if self.largo == 0:
            return print("La Lista esta vacia")
        if temp.__str__() == valor:
            self.head = temp.next
            return
        while temp.next != None:
            if temp.next.__str__() == valor:
                temp.next = temp.next.next
                break
            temp = temp.next
        return

    def dela(self, valor):
        temp = self.head
        if self.largo == 0:
            return print("La Lista esta vacia")
        while temp != self.tail.next:
            if temp.__str__() == valor:
                self.head = temp.next
            if temp.next.__str__() == valor:
                temp.next = temp.next.next
            temp = temp.next
        return

    def insert(self, valor, pos):
        if not pos <= self.largo:
            return print("Error")
        temp = self.head
        i = 1
        if pos == 0:
            self.head = Nodo(valor=valor, next=temp)
            temp.prev = self.head
            self.largo += 1
            return
        while temp != None:
            if i != pos:
                temp = temp.next
                i += 1
            else:
                temp2 = Nodo(temp, temp.prev, valor)
                temp.prev.next = temp2
                temp.prev = temp2
                self.largo += 1
                break
        return"""

x = Tren("thomas","s-c", 13, 2)
x.enganchar_i(6)
x.enganchar_f(5)
x.enganchar_f(9)
x.enganchar_f(1)
x.enganchar_f(7)
x.printL()
x.enganchar_m(2)
x.printL()
