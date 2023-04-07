from unittest import TestCase
from src.Models import Operacao, opcoesOperacoes

class OperacaoModuleTest(TestCase):
    def test_Dado_UmaOperacaoSoma_Quando_ObterString_Deve_RetornarExpressaoCorreta(self):
        operacao = Operacao(opcoesOperacoes[1], [1, 2, 3, 4])
        self.assertEqual(f'{operacao}', '1 + 2 + 3 + 4')

    def test_Dado_UmaOperacaoSubtracao_Quando_ObterString_Deve_RetornarExpressaoCorreta(self):
        operacao = Operacao(opcoesOperacoes[2], [1, 2, 3, 4])
        self.assertEqual(f'{operacao}', '1 - 2 - 3 - 4')

    def test_Dado_UmaOperacaoMultiplicacao_Quando_ObterString_Deve_RetornarExpressaoCorreta(self):
        operacao = Operacao(opcoesOperacoes[3], [1, 2, 3, 4])
        self.assertEqual(f'{operacao}', '1 * 2 * 3 * 4')

    def test_Dado_UmaOperacaoDivisao_Quando_ObterString_Deve_RetornarExpressaoCorreta(self):
        operacao = Operacao(opcoesOperacoes[4], [1, 2, 3, 4])
        self.assertEqual(f'{operacao}', '1 / 2 / 3 / 4')

    def test_Dado_UmaOperacaoSoma_Quando_ExecutarDelegate_Deve_RetornarContaCorreta(self):
        operacao = Operacao(opcoesOperacoes[1], [1, 2, 3, -4])
        self.assertEqual(operacao.executarDelegate(), 2)

    def test_Dado_UmaOperacaoSubracao_Quando_ExecutarDelegate_Deve_RetornarContaCorreta(self):
        operacao = Operacao(opcoesOperacoes[2], [1, 2, 3, -4])
        self.assertEqual(operacao.executarDelegate(), 0)

    def test_Dado_UmaOperacaoMultiplicacao_Quando_ExecutarDelegate_Deve_RetornarContaCorreta(self):
        operacao = Operacao(opcoesOperacoes[3], [1, 2, 3, -4])
        self.assertEqual(operacao.executarDelegate(), -24)

    def test_Dado_UmaOperacaoDivisao_Quando_ExecutarDelegate_Deve_RetornarContaCorreta(self):
        operacao = Operacao(opcoesOperacoes[4], [2, 2, 0, 4])
        self.assertEqual(operacao.executarDelegate(), 0.25)