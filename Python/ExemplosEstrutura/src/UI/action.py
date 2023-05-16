from src.UI.console import clear, wait
from src.UI.message import EntradaInvalida, MenuOperacao, MenuUsuario, MenuExpressao, MenuRaiz, MenuListaCompra
from src.UI.inputUsuario import ObterInputUsuario
from ..Services import UsuarioService, OperacaoService, ExpressaoService, CompraService

usuarioService = UsuarioService()
operacaoService = OperacaoService()
expressaoService = ExpressaoService()
listaCompraService = CompraService()

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
    while ExecutarMenu(MenuUsuario, opcoesUsuario) == 0:
        continue

def ExecutarMenuOperacao():
    while ExecutarMenu(MenuOperacao, opcoesOperacoes) == 0:
        continue

def ExecutarMenuExpressao():
    while ExecutarMenu(MenuExpressao, opcoesExpressoes) == 0:
        continue

def ExecutarMenuListaCompra():
    while ExecutarMenu(MenuListaCompra, opcoesListaCompra) == 0:
        continue

opcoesMenuRaiz = {
    1: ExecutarMenuUsuario,
    2: ExecutarMenuOperacao,
    3: ExecutarMenuExpressao,
    4: ExecutarMenuListaCompra
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

opcoesListaCompra = {
    1: listaCompraService.adicionar_item_lista,
    2: listaCompraService.imprimir_lista_compra
}
