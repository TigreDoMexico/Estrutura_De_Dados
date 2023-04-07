import copy
from queue import Queue
from src.Models.Operacao import Operacao, opcoesOperacoes

class OperacaoService:
    def __init__(self, queueOperacoes = None):
        if queueOperacoes:
            self.__fila_operacoes = queueOperacoes
        else:
            self.__fila_operacoes = Queue()

    def adicionarNovaOperacaoAction(self):
        self._imprimirOpcoesOperacoes()

        operacao = self._retornarOperacao(int(input('Digite a operação desejada: ')))
        valores = self._obterValoresDaString(input('Digite os valores separados por espaço: '))

        self._putOperacaoNaFila(operacao, valores)
        print(f"Temos {self.__fila_operacoes._qsize()} operações na Fila")

    def executarProximaOperacaoAction(self):
        if(self.__fila_operacoes.empty()):
            print("Não tem nenhuma operação para executar")
            return False

        operacao = self.__fila_operacoes.get()
        self._executarOperacao(operacao)
        print(f"Faltam {self.__fila_operacoes._qsize()} operações na Fila")

    def executarTodasOperacoesAction(self):
        while not self.__fila_operacoes.empty():
            operacao = self.__fila_operacoes.get()
            self._executarOperacao(operacao)

    def getFilaOperacoes(self):
        return copy.copy(self.__fila_operacoes)

    def _executarOperacao(self, operacao):
        try:
            print(f"Executando: {operacao} = {operacao.executarDelegate()}")
        except Exception as ex:
            print(ex)
            print('Não foi possível executar a operação')

    def _imprimirOpcoesOperacoes(self):
        print('1 - Adição (+)')
        print('2 - Subtração (-)')
        print('3 - Multiplicação (*)')
        print('4 - Divisão (/)')

    def _retornarOperacao(self, operacao: int):
        return opcoesOperacoes[operacao]

    def _obterValoresDaString(self, valoresString):
        return [int(x) for x in valoresString.split(' ')]

    def _putOperacaoNaFila(self, operacao, valores):
        self.__fila_operacoes.put(Operacao(operacao, valores))