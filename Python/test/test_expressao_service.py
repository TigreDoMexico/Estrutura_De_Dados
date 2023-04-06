import io
import sys
from unittest import TestCase
from unittest.mock import patch
from src import ExpressaoService


class ExpressaoTests(TestCase):
    def test_Dado_UmExpressaoInvalida_Quando_ValidarExpressaoAction_Deve_ImprimirQueEstaInvalido(self):
        service = ExpressaoService()
        casos = [
            '{[(])}',
            '{[()]',
            '1 + [ 2 ( 3 ) ] }',
            '{[(',
        ]

        for casoInvalido in casos:
            with patch('builtins.input', lambda _: casoInvalido):
                output = self._configurarOutput()

                service.validarExpressaoAction()

                sys.stdout = sys.__stdout__
                self.assertEqual(output.getvalue(), 'Expressão inválida\n')

    def test_Dado_UmExpressaoInvalida_Quando_ValidarExpressaoAction_Deve_ImprimirQueEstaInvalido(self):
        service = ExpressaoService()
        casos = [
            "{[()]}",
            "[()]",
            "()",
            "{}",
            "1 + { 5 [ 2 ( 3 ) ] }",
        ]

        for casoValido in casos:
            with patch('builtins.input', lambda _: casoValido):
                output = self._configurarOutput()

                service.validarExpressaoAction()

                sys.stdout = sys.__stdout__
                self.assertEqual(output.getvalue(), 'Expressão válida\n')

    def _configurarOutput(self):
        output = io.StringIO()
        sys.stdout = output
        return output
