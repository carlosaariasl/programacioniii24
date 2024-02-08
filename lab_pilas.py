#pila stack:
#Implementar una pila utilizando una lista en Python.
#Crear funciones para realizar las operaciones básicas de una pila: push (añadir elemento), pop (eliminar elemento) y peek (ver el elemento superior sin eliminarlo).
#Escribir un programa que utilice esta pila para invertir el orden de una lista dada.
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.esta_vacia() else None

# Ejemplo de uso:
p = Pila()
p.push(1)
p.push(2)
p.push(3)
print(p.pop())  # Output: 3
print(p.peek()) # Output: 2


#Cola (Queue):

#Implementar una cola utilizando una lista en Python.
#Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar elemento) y front (ver el primer elemento sin eliminarlo).
#Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en el orden en que llegan.

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[-1] if not self.esta_vacia() else None

# Ejemplo de uso:
c = Cola()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.dequeue())  # Output: 1
print(c.front())    # Output: 3


#Verificar paréntesis balanceados utilizando una pila:
#Escribir una función en Python que tome una cadena de paréntesis y determine si están balanceados.
#Utilizar una pila para rastrear la apertura y cierre de paréntesis.
def paréntesis_balanceados(cadena):
    pila = []
    for caracter in cadena:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila.pop() != '(':
                return False
    return not pila

# Ejemplo de uso:
cadena = "((()))"
print(paréntesis_balanceados(cadena))  # Output: True
cadena = "(()))"
print(paréntesis_balanceados(cadena))  # Output: False



#Implementar una cola utilizando dos pilas:
#Desarrollar una clase ColaConPilas que utilice dos pilas para simular el comportamiento de una cola.
#Implementar las operaciones enqueue y dequeue utilizando las operaciones de pilas.
class ColaConPilas:
    def __init__(self):
        self.pila_entrada = Pila()
        self.pila_salida = Pila()

    def enqueue(self, item):
        self.pila_entrada.push(item)

    def dequeue(self):
        if self.pila_salida.esta_vacia():
            while not self.pila_entrada.esta_vacia():
                self.pila_salida.push(self.pila_entrada.pop())
        return self.pila_salida.pop()

# Ejemplo de uso:
c = ColaConPilas()
c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
print(c.dequeue())  # Output: 1
print(c.dequeue())  # Output: 2


#Revertir la mitad de una cola:

#Escribir una función que tome una cola y revierta la mitad de sus elementos utilizando solo una pila adicional.
#La cola debe mantener la misma secuencia de elementos, pero la mitad debe estar en orden inverso.
def revertir_mitad_cola(cola):
    pila_auxiliar = Pila()
    tamaño = len(cola.items)
    mitad = tamaño // 2
    # Pasar la primera mitad de la cola a una pila
    for _ in range(mitad):
        pila_auxiliar.push(cola.dequeue())
    # Pasar los elementos de la pila de vuelta a la cola
    while not pila_auxiliar.esta_vacia():
        cola.enqueue(pila_auxiliar.pop())
    # Pasar los elementos de la cola a la pila auxiliar
    for _ in range(tamaño - mitad):
        pila_auxiliar.push(cola.dequeue())
    # Pasar los elementos de la pila auxiliar de vuelta a la cola
    while not pila_auxiliar.esta_vacia():
        cola.enqueue(pila_auxiliar.pop())

# Ejemplo de uso:
cola = Cola()
for i in range(1, 7):
    cola.enqueue(i)
revertir_mitad_cola(cola)
while not cola.esta_vacia():
    print(cola.dequeue(), end=" ")  # Output: 3 2 1 4 5 6

#Estos ejercicios cubren una variedad de conceptos relacionados con pilas y colas en Python y pueden ayudar a los estudiantes a comprender mejor cómo funcionan estas estructuras de datos y cómo implementarlas en código.




