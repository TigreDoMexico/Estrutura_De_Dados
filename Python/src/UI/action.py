from src.UI.console import clear, wait
from src.UI.message import EntradaInvalida, MenuOperacao, MenuUsuario
from ..Services import UsuarioService, OperacaoService

usuarioService = UsuarioService()
operacaoService = OperacaoService()

def ObterInputUsuario(mensagem = 'Digite um valor: \n'):
    valor = 0
    valorValido = False

    while not(valorValido):
        valorDigitado = input(mensagem)
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

def ExecutarMenuOperacao():
    clear()

    MenuOperacao()
    opcao = ObterInputUsuario()

    try:
        opcoesOperacoes[opcao]()
    except:
        EntradaInvalida()

    wait()

opcoesUsuario = {
    1: usuarioService.adicionarUsuarioAction,
    2: usuarioService.listarTodosUsuariosAction,
    3: usuarioService.buscarUsuarioAction,
    4: usuarioService.obterTotalUsuarios,
    5: usuarioService.editarUsuarioAction,
    6: usuarioService.deletarUsuarioAction
}

opcoesOperacoes = {
    1: operacaoService.adicionarNovaOperacaoAction,
    2: operacaoService.executarProximaOperacaoAction,
    3: operacaoService.executarTodasOperacoesAction
}
