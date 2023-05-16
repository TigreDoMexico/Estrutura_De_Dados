class ItemCompra:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __eq__(self, other):
        return self.nome == other.nome and self.valor == other.valor

    def __hash__(self):
        return hash(self.nome + str(self.valor))
