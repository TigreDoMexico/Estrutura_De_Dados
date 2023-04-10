from src.UI.console import clear, wait
from src.UI.message import EntradaInvalida, MenuOperacao, MenuUsuario, MenuExpressao, MenuRaiz
from src.UI.inputUsuario import ObterInputUsuario
from ..Services import UsuarioService, OperacaoService, ExpressaoService

usuarioService = UsuarioService()
operacaoService = OperacaoService()
expressaoService = ExpressaoService()

def ExecutarMenu(mensagem, opcoes):
    clear()
    mensagem()

    opcao = ObterInputUsuario()

    if(opcao == 0):
        return 1

    try:
        opcoes[opcao]()
    except:
        EntradaInvalida()
    finally:
        wait()
        return 0

def ExecutarMenuRaiz():
    return ExecutarMenu(MenuRaiz, opcoesMenuRaiz)

def ExecutarMenuUsuario():
    return ExecutarMenu(MenuUsuario, opcoesUsuario)

def ExecutarMenuOperacao():
    return ExecutarMenu(MenuOperacao, opcoesOperacoes)

def ExecutarMenuExpressao():
    return ExecutarMenu(MenuExpressao, opcoesExpressoes)

opcoesMenuRaiz = {
    1: ExecutarMenuUsuario,
    2: ExecutarMenuOperacao,
    3: ExecutarMenuExpressao
}

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
