import io
from queue import Queue
import sys
from unittest import TestCase
from unittest.mock import patch
from src.Models import Operacao, opcoesOperacoes
from src import OperacaoService

class OperacaoServiceTest(TestCase):
    def test_Quando_AdicionarNovaOperacao_Deve_SalvarNaFilaAOperacaoEOsValores(self):
        inputs = iter(['1', '1 2 3 4'])
        with patch('builtins.input', lambda _: next(inputs)):
            self._configurarOutput()
            service = OperacaoService()
            service.adicionarNovaOperacaoAction()

            fila = service.getFilaOperacoes()

            self.assertEqual(fila._qsize(), 1)

            filaContent = fila.get()
            self.assertEqual(filaContent.Valores, [1, 2, 3, 4])
            self.assertIsNotNone(filaContent.Delegate)
            self.assertIsNotNone(filaContent.Simbolo)

    def test_Quando_AdicionarNovaOperacao_Deve_ImprimirNaTelaQueUmaOperacaoEstaNaFila(self):
        inputs = iter(['1', '1 2 3 4'])
        with patch('builtins.input', lambda _: next(inputs)):
            output = self._configurarOutput()
            service = OperacaoService()
            service.adicionarNovaOperacaoAction()

            sys.stdout = sys.__stdout__
            outputTela = output.getvalue().split('\n')[-2]
            self.assertEqual(outputTela, 'Temos 1 operações na Fila')
    
    def test_Dado_UmaOpcaoErrada_Quando_AdicionarNovaOperacao_Deve_ImprimirNaTelaQueFoiSelecionadoUmaOperacaoInvalida(self):
        inputs = iter(['5', '1', '1 2 3 4'])
        with patch('builtins.input', lambda _: next(inputs)):
            output = self._configurarOutput()
            service = OperacaoService()
            service.adicionarNovaOperacaoAction()

            sys.stdout = sys.__stdout__
            outputTela = output.getvalue().split('\n')[-3]
            self.assertEqual(outputTela, 'Opção Inválida - Selecione uma das operações disponíveis')

    def test_DadoUmaFilaVazia_Quando_ExecutarProximaOperacao_Deve_ImprimirNaTelaQueNaoTemOperacoesParaExecutar(self):
        output = self._configurarOutput()

        service = OperacaoService()
        self.assertFalse(service.executarProximaOperacaoAction())

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), 'Não tem nenhuma operação para executar\n')

    def test_DadoUmaFilaComUmItem_Quando_ExecutarProximaOperacao_Deve_ImprimirOResultadoNaTela(self):
        # ARRANGE
        fila = self._gerarFila()
        service = OperacaoService(fila)

        # ACT
        output = self._configurarOutput()
        service.executarProximaOperacaoAction()

        # ASSERT
        sys.stdout = sys.__stdout__
        outputTela = output.getvalue().split('\n')
        outputCalculo = outputTela[0]
        outputTotalItens = outputTela[1]

        self.assertEqual(outputCalculo, 'Executando: 1 + 2 + 3 + 4 = 10')
        self.assertEqual(outputTotalItens, 'Faltam 0 operações na Fila')

    def test_DadoUmaFilaComItens_Quando_ExecutarTodasOperacoes_Deve_ImprimirOsResultadosNaTela(self):
        # ARRANGE
        fila = self._gerarFila()
        fila.put(Operacao(opcoesOperacoes[1], [1, 2, 3, 4]))
        fila.put(Operacao(opcoesOperacoes[1], [1, 2, 3, 4]))
        service = OperacaoService(fila)

        # ACT
        output = self._configurarOutput()
        service.executarTodasOperacoesAction()

        # ASSERT
        sys.stdout = sys.__stdout__
        outputTela = output.getvalue().split('\n')

        self.assertEqual(outputTela[0], 'Executando: 1 + 2 + 3 + 4 = 10')
        self.assertEqual(outputTela[1], 'Executando: 1 + 2 + 3 + 4 = 10')
        self.assertEqual(outputTela[2], 'Executando: 1 + 2 + 3 + 4 = 10')

    def test_DadoUmaFilaVazia_Quando_ExecutarTodasOperacoes_Deve_ImprimirNadaNaTela(self):
        # ARRANGE
        service = OperacaoService()
        # ACT
        output = self._configurarOutput()
        service.executarTodasOperacoesAction()
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '')

    def _gerarFila(self):
        fila = Queue()
        fila.put(Operacao(opcoesOperacoes[1], [1, 2, 3, 4]))
        return fila

    def _configurarOutput(self):
        output = io.StringIO()
        sys.stdout = output
        return output