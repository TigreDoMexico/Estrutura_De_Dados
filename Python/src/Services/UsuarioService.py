from src.Models import *

class UsuarioService:
    def __init__(self, lista = None):
        if lista:
            self.__lista_usuario = lista
        else:
            self.__lista_usuario = []

    def adicionarUsuarioAction(self):        
        try:
            usuario = self._gerarUsuarioComProps(self._obterPropsDoUsuario())
            self.adicionarUsuarioNaLista(usuario)
        except Exception as ex:
            print(ex)
            return False
        return True

    def adicionarUsuarioNaLista(self, usuario):        
        if isinstance(usuario, Usuario):
            self.__lista_usuario.append(usuario)
        else:
            raise Exception("Usuario enviado está no formato errado")

    def imprimirUsuario(self):
        for usuario in self.__lista_usuario:
            self.imprimeUsuario(usuario)

    def obterUsuario(self):
        valor = input("Digite o RA do usuário: ")

        usuarioEncontrado = self.obterUsuarioPorRA(valor)

        if usuarioEncontrado is not None:
            print("Usuário Encontrado")
            self.imprimeUsuario(usuarioEncontrado)
        else:
            print("Usuário Não Encontrado")

    def editarUsuario(self):
        valor = input("Digite o RA do usuário: ")

        usuarioEncontrado = self.obterUsuarioPorRA(valor)

        if usuarioEncontrado is not None:
            novoNome = input("Digite o novo nome do usuário: ")
            usuarioEncontrado.Nome = novoNome
        else:
            print("Usuário Não Encontrado")

    def deletarUsuario(self):
        valor = input("Digite o RA do usuário: ")

        usuarioEncontrado = self.obterUsuarioPorRA(valor)

        if usuarioEncontrado is not None:
            index = self.__lista_usuario.index(usuarioEncontrado)
            del self.__lista_usuario[index]
        else:
            print("Usuário Não Encontrado")

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
    
    def _obterPropsDoUsuario(self, comRa = True):
        ra = input("Digite o RA do Usuário: ") if comRa else None
        nome = input("Digite o Nome: ")
        cpf = input("Digite o CPF: ")
        email = input("Digite o Email: ")
        dataNascimento = input("Digite a Data de Nascimento: ")

        return (ra, nome, cpf, email, dataNascimento)
    
    def _gerarUsuarioComProps(self, props):
        usuario = Usuario()
        setattr(usuario, "Ra", props[0])
        setattr(usuario, "Nome", props[1])
        setattr(usuario, "Cpf", props[2])
        setattr(usuario, "Email", props[3])
        setattr(usuario, "DataNascimento", props[4])
        
        return usuario
