from src.UI.message import EntradaInvalida, MenuUsuario
from ..Services import UsuarioService

usuarioService = UsuarioService()

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
    1: usuarioService.adicionarUsuarioAction,
    2: usuarioService.listarTodosUsuariosAction,
    3: usuarioService.buscarUsuarioAction,
    4: usuarioService.obterTotalUsuarios,
    5: usuarioService.editarUsuarioAction,
    6: usuarioService.deletarUsuarioAction
}

