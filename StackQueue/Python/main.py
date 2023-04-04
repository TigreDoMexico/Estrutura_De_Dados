from stack import Stack
from queue import Queue

pilha = Stack()

pilha.push(10)
pilha.push(20)
pilha.push(30)

pilha.pop()

pilha.push(40)

print(pilha)

fila = Queue()

fila.put(10)
fila.put(20)
fila.put(30)

fila.get()

fila.put(40)

print(fila)