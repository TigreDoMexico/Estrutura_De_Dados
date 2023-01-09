from src.Usuario.Usuario import *

class UsuarioManager:
    def __init__(self):
        self.lista_usuario = []

    def adicionarUsuario(self):
        user = Usuario()

        print("ADICINANDO NOVO USUÁRIO")

        user.Ra = input("Digite o RA: ")
        user.Nome = input("Digite o Nome: ")

        self.lista_usuario.append(user)
    
    def imprimirUsuario(self):
        for usuario in self.lista_usuario:
            print("RA:", usuario.Ra)
            print("Nome:", usuario.Nome)