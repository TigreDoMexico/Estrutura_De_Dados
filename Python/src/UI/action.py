from src.UI.console import clear, wait
from src.UI.message import EntradaInvalida, MenuOperacao, MenuUsuario, MenuExpressao
from ..Services import UsuarioService, OperacaoService, ExpressaoService

usuarioService = UsuarioService()
operacaoService = OperacaoService()
expressaoService = ExpressaoService()

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
    clear()

    MenuUsuario()
    opcao = ObterInputUsuario()

    try:
        opcoesUsuario[opcao]()
    except:
        EntradaInvalida()

    wait()

def ExecutarMenuOperacao():
    clear()

    MenuOperacao()
    opcao = ObterInputUsuario()

    try:
        opcoesOperacoes[opcao]()
    except:
        EntradaInvalida()

    wait()

def ExecutarMenuExpressao():
    clear()

    MenuExpressao()
    opcao = ObterInputUsuario()

    try:
        opcoesExpressoes[opcao]()
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

opcoesExpressoes = {
    1: expressaoService.validarExpressaoAction,
}
