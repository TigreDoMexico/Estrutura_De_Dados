from node import Node

class Queue:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.size = 0

    def __str__(self):
        cur = self.inicio
        out = "INICIO -> "
        while cur:
            out += "[" + str(cur.valor) + "]" + "->"
            cur = cur.prox
        return out

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def put(self, valor):
        novoNode = Node(valor)

        if (self.fim):
            self.fim.prox = novoNode
            self.fim = novoNode
            self.size += 1
        else:
            self.inicio = novoNode
            self.fim = novoNode

    def get(self):
        if (self.inicio):
            remove = self.inicio
            self.inicio = remove.prox
            self.size -= 1

            if(self.fim == remove):
                self.fim = None

            return remove.valor