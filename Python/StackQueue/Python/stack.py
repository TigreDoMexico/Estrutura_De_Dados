from node import Node

class Stack:
    def __init__(self):
        self.topo = None
        self.size = 0

    def __str__(self):
        cur = self.topo
        out = "TOPO -> "
        while cur:
            out += "[" + str(cur.valor) + "]" + "->"
            cur = cur.prox
        return out

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, valor):
        novoNode = Node(valor)

        if (self.topo):
            novoNode.prox = self.topo
            self.topo = novoNode
            self.size += 1
        else:
            self.topo = novoNode

    def pop(self):
        if (self.topo):
            remove = self.topo
            self.topo = remove.prox
            self.size -= 1
            return remove.valor