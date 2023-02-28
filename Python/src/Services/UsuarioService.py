from src.Models import *

class UsuarioService:
    def __init__(self, lista = None):
        if lista:
            self.__lista_usuario = lista
        else:
            self.__lista_usuario = []

    def adicionarUsuario(self):
        user = Usuario()

        user.Ra = input("Digite o RA do novo usuário: ")
        user.Nome = input("Digite o Nome do novo usuário: ")

        #self.lista_usuario.append(user)     # Adiciona no final da lista
        self.__lista_usuario.insert(0, user)   # Adiciona no inicio da lista

        return True
    
    def imprimirUsuario(self):
        print("Imprimindo todos os Usuários")

        for usuario in self.__lista_usuario:
            imprimeUsuario(usuario)

    def obterUsuario(self):        
        valor = input("Digite o RA do usuário: ")

        try:
            usuarioEncontrado = obterUsuarioPorRA("333")
        except ex:
            print(ex)

        # print("Executou")
        # print(usuarioEncontrado)

        # if usuarioEncontrado is not None:
        #     print("Usuário Encontrado")
        #     imprimeUsuario(usuarioEncontrado)
        # else:
        #     print("Usuário Não Encontrado")
    
    def obterUsuarioPorIndice(self, indice):
        try:
            return self.__lista_usuario[indice]
        except:
            return None
    
    def obterUsuarioPorRA(self, ra):
        return next((usuario for usuario in self.__lista_usuario if usuario.Ra == ra), None)
    
    def obterTotalUsuarios(self):
        return len(self.__lista_usuario)

    def imprimeUsuario(self, usuario):
        print("RA:", usuario.Ra)
        print("Nome:", usuario.Nome)
