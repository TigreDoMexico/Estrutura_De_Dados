from unittest.mock import patch
from unittest import main, TestCase
import io
import sys

from src.Usuario.UsuarioManager import UsuarioManager

class UsuarioTests(TestCase):
    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_AsEntradasDoUsuario_Quando_AdicionarUsuario_Deve_AtualizarListaComUsuarioCriado(self):
        # ARRANGE
        manager = UsuarioManager()

        # ACT
        manager.adicionarUsuario()
        
        # ASSERT
        self.assertEqual(len(manager.lista_usuario), 1)

        self.assertEqual(manager.lista_usuario[0].Ra, 'ABCDEF')
        self.assertEqual(manager.lista_usuario[0].Nome, 'ABCDEF')
        self.assertEqual(manager.lista_usuario[0].Cpf, None)
        self.assertEqual(manager.lista_usuario[0].Email, None)
        self.assertEqual(manager.lista_usuario[0].DataNascimento, None)

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_AsEntradasDoUsuario_Quando_AdicionarUsuario_Deve_ImprimirNaTelaAMensagemDeUsuarioAdicionado(self):
        # ARRANGE
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        manager = UsuarioManager()

        # ACT
        manager.adicionarUsuario()
        
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'ADICINANDO NOVO USUÁRIO\n')

if __name__ == '__main__':
    main()