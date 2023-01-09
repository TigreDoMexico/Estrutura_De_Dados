from unittest.mock import patch
from unittest import main, TestCase
from src.Usuario.Usuario import Usuario
from src.Usuario.UsuarioManager import UsuarioManager
import io
import sys

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

    def test_Dado_UmaListaDeUsuariosVazios_Quando_ImprimirUsuarios_Deve_ImprimirNadaNaTela(self):
        # ARRANGE
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        manager = UsuarioManager()

        # ACT
        manager.imprimirUsuario()
        
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), '')

    def test_Dado_UmaListaDeUsuarios_Quando_ImprimirUsuarios_Deve_ImprimirOsDadosDaLista(self):
        # ARRANGE
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        manager = UsuarioManager()

        usuario = Usuario()
        usuario.Ra = "12345"
        usuario.Nome = "12345"

        manager.lista_usuario.append(usuario)

        # ACT
        manager.imprimirUsuario()
        
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'RA: 12345\nNome: 12345\n')

if __name__ == '__main__':
    main()