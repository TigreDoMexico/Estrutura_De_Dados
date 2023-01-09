from src.UI.message import EntradaInvalida, MenuUsuario
from src.Usuario.UsuarioManager import UsuarioManager

usuarioManager = UsuarioManager()

def ObterInputUsuario():
    valor = 0
    valorValido = False

    while not(valorValido):
        valorDigitado = input("Digite um valor: \n")
        try:
            valor = int(valorDigitado)
            valorValido = True
        except:
            EntradaInvalida()

    return valor

def ExecutarMenuUsuario():
    MenuUsuario()
    opcao = ObterInputUsuario()

    try:
        opcoesUsuario[opcao]()
    except:
        EntradaInvalida()

opcoesUsuario = {
    1: usuarioManager.adicionarUsuario,
    2: usuarioManager.imprimirUsuario
}

