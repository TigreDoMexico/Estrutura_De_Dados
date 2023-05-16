from src.Models import ItemCompra

class CompraService:
    def __init__(self):
        self.lista_compra = set()
    
    def adicionar_item_lista(self):
        nome = input("Digite o nome do item: ")
        valor = float(input("Digite o valor do item: "))

        total_antes = len(self.lista_compra)

        item = ItemCompra(nome, valor)
        self.lista_compra.add(item)

        if(len(self.lista_compra) == total_antes + 1):
            print("Item Adicionado na Lista")
        else:
            print("Item já existe na Lista")
    
    def imprimir_lista_compra(self):
        print("LISTA DE PRODUTOS: ")
        for item in self.lista_compra:
            print("NOME", item.nome)
            print("VALOR", item.valor)
    


