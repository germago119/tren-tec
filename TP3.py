import os


class Tren:
    def __init__(self, tren, ruta, hora, maquina, vagones):
        self.num_tren = tren
        self.ruta = ruta
        self.hora = hora
        self.num_maquina = maquina
        self.vagones = vagones
        self.head = None
        self.tail = None
        self.lenght = 0

    def engancahar_i(self):
        pass

    def enganchar_f(self):
        pass

    def enganchar_m(self):
        pass

    def remove(self):
        pass

    def exit(self):
        pass

    def llegar(self):
        pass

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


class Maquina:
    def __init__(self, num, capacidad_v):
        self.num_maquina = num
        self.capacidad_v = capacidad_v


class Vagon:
    def __init__(self, num_vagon=None, next=None, prev=None, capacidad_p=None):
        self.num_vagon = num_vagon
        self.next = next
        self.prev = prev
        self.capacidad_p = capacidad_p
