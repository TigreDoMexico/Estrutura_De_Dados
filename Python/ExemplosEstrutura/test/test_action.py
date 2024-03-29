import io
import sys
from unittest.mock import patch
from unittest import main, TestCase
from src import ObterInputUsuario

class ActionTests(TestCase):
    @patch('builtins.input', lambda _: '2')
    def test_Quando_ObterImputUsuario_Deve_RetornarONumeroInseridoPeloUsuario(self):
        self._configurarOutput()
        assert ObterInputUsuario() == 2

    @patch('builtins.input', side_effect=['E', '+', '2'])
    def test_Dado_VariasEntradasDoUsuario_Quando_ObterImputUsuario_Deve_RetornarSomenteAquelaQueEhUmNumero(self, patched):
        self._configurarOutput()
        assert ObterInputUsuario() == 2
        assert patched.call_count == 3

    def _configurarOutput(self):
        output = io.StringIO()
        sys.stdout = output
        return output

if __name__ == '__main__':
    main()