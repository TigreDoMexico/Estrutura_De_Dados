from src.Models import *

class UsuarioRepository:
    def __init__(self, usuariosIniciais = None):
        if usuariosIniciais:
            self.__usuarios = usuariosIniciais
        else:
            self.__usuarios = []

    def adicionarUsuario(self, usuario):
        if isinstance(usuario, Usuario):
            self.__usuarios.append(usuario)
        else:
            raise Exception("Usuario enviado está no formato errado")

    def obterTodosUsuarios(self):
        return self.__usuarios.copy()

    def obterUsuarioPorRa(self, ra):
        return next((usuario for usuario in self.__usuarios if usuario.Ra == ra), None)

    def obterTotal(self):
        return len(self.__usuarios)