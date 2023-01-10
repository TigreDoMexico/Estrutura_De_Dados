from unittest.mock import patch
from unittest import main, TestCase
from src.Models import Usuario
from src import UsuarioService
import io
import sys

class UsuarioTests(TestCase):
    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_AsEntradasDoUsuario_Quando_AdicionarUsuario_Deve_RetornarTrue(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertTrue(service.adicionarUsuario())

    def test_Dado_UmaListaVazia_Quando_ObterTotalDeUsuarios_Deve_RetornarZero(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertEqual(service.obterTotalUsuarios(), 0)

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_UmaListaVazia_Quando_AdicionarNovoUsuario_E_ObterTotalDeUsuarios_Deve_RetornarUm(self):
        # ARRANGE
        service = UsuarioService()
        # ACT
        service.adicionarUsuario()        
        # ASSERT
        self.assertEqual(service.obterTotalUsuarios(), 1)

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_UmaListaVazia_Quando_AdicionarNovoUsuario_E_ObterUsuarioNoIndiceZero_Deve_RetornarOsDadosAdicionados(self):
        # ARRANGE
        service = UsuarioService()
        # ACT
        service.adicionarUsuario()
        resultado = service.obterUsuarioPorIndice(0)        
        # ASSERT
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.Ra, 'ABCDEF')
        self.assertEqual(resultado.Nome, 'ABCDEF')
        self.assertEqual(resultado.Cpf, None)
        self.assertEqual(resultado.Email, None)
        self.assertEqual(resultado.DataNascimento, None)
    
    def test_Dado_UmaListaVazia_Quando_ObterUsuarioNoIndiceZero_Deve_RetornarNone(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertIsNone(service.obterUsuarioPorIndice(0))

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_UmaListaVazia_Quando_AdicionarNovoUsuario_E_ObterUsuarioPeloRA_Deve_RetornarOsDadosAdicionados(self):
        # ARRANGE
        service = UsuarioService()
        # ACT
        service.adicionarUsuario()
        resultado = service.obterUsuarioPorRA('ABCDEF')        
        # ASSERT
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.Ra, 'ABCDEF')
        self.assertEqual(resultado.Nome, 'ABCDEF')
        self.assertEqual(resultado.Cpf, None)
        self.assertEqual(resultado.Email, None)
        self.assertEqual(resultado.DataNascimento, None)

    def test_Dado_UmaListaVazia_Quando_ObterUsuarioPorRA_Deve_RetornarNone(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertIsNone(service.obterUsuarioPorRA('ABCDEF'))

    def test_Dado_UmaListaDeUsuariosVazios_Quando_ImprimirUsuarios_Deve_ImprimirNadaNaTela(self):
        # ARRANGE
        output = self.configurarOutput()
        service = UsuarioService()
        # ACT
        service.imprimirUsuario()        
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '')

    def test_Dado_UmaListaDeUsuarios_Quando_ImprimirUsuarios_Deve_ImprimirOsDadosDaLista(self):
        # ARRANGE
        output = self.configurarOutput()

        usuario = Usuario()
        usuario.Ra = "12345"
        usuario.Nome = "12345"

        service = UsuarioService([usuario])

        # ACT
        service.imprimirUsuario()        
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), 'RA: 12345\nNome: 12345\n')
    
    def configurarOutput(self):
        output = io.StringIO()
        sys.stdout = output
        return output

if __name__ == '__main__':
    main()