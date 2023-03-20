from unittest.mock import patch, Mock
from unittest import main, TestCase
from src.Models import Usuario
from src import UsuarioService
from faker import Faker
import io
import sys

class UsuarioTests(TestCase):

    # ----------- ADICINAR USUÁRIO  ----------- #

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_AsEntradasDoUsuario_Quando_AdicionarUsuario_Deve_RetornarTrue(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertTrue(service.adicionarUsuarioAction())

    # ----------- OBTER TOTAL USUÁRIOS  ----------- #

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
        service.adicionarUsuarioAction()
        # ASSERT
        self.assertEqual(service.obterTotalUsuarios(), 1)

    def test_Dado_UmaListaComVariosUsuarios_Quando_ObterTotalDeUsuarios_Deve_RetornarOTamanhoTotalDaLista(self):
        # ARRANGE
        quantidadeEsperada = 3
        service = UsuarioService(self._criarListaUsuarios(quantidadeEsperada))
        # ACT E ASSERT
        self.assertEqual(service.obterTotalUsuarios(), quantidadeEsperada)

    # ----------- OBTER USUARIO POR ID  ----------- #

    @patch('builtins.input', lambda _: 'ABCDEF')
    def test_Dado_UmaListaVazia_Quando_AdicionarNovoUsuario_E_ObterUsuarioNoIndiceZero_Deve_RetornarOsDadosAdicionados(self):
        # ARRANGE
        ra = '12345'
        nome = 'David'
        cpf = '12345678901'
        email = 'david.tigre@teste.com.br'
        dataNasc = '11-10-1997'

        inputs = iter([ra, nome, cpf, email, dataNasc])
        with patch('builtins.input', lambda _: next(inputs)):
            service = UsuarioService()
            # ACT
            service.adicionarUsuarioAction()
            resultado = service.obterUsuarioPorIndice(0)
            # ASSERT
            self.assertIsNotNone(resultado)
            self.assertEqual(resultado.Ra, ra)
            self.assertEqual(resultado.Nome, nome)
            self.assertEqual(resultado.Cpf, cpf)
            self.assertEqual(resultado.Email, email)
            self.assertEqual(resultado.DataNascimento, dataNasc)

    def test_Dado_UmaListaVazia_Quando_ObterUsuarioNoIndiceZero_Deve_RetornarNone(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertIsNone(service.obterUsuarioPorIndice(0))

    # ----------- OBTER USUARIO POR RA  ----------- #

    def test_Dado_UmaListaComUsuarios_Quando_ObterUsuarioPeloRA_PassandoRACorreto_Deve_RetornarOUsuarioCompleto(self):
        # ARRANGE
        users = self._criarListaUsuarios(1)
        service = UsuarioService(users)
        # ACT
        resultado = service.obterUsuarioPorRA(users[0].Ra)
        # ASSERT
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.Ra, users[0].Ra)
        self.assertEqual(resultado.Nome, users[0].Nome)
        self.assertEqual(resultado.Cpf, users[0].Cpf)
        self.assertEqual(resultado.Email, users[0].Email)
        self.assertEqual(resultado.DataNascimento, users[0].DataNascimento)

    def test_Dado_UmaListaComUsuarios_Quando_ObterUsuarioPeloRA_PassandoRAErrado_Deve_RetornarNone(self):
        # ARRANGE
        users = self._criarListaUsuarios(1)
        service = UsuarioService(users)
        # ACT E ASSERT
        self.assertIsNone(service.obterUsuarioPorRA("ABCDEF"))

    def test_Dado_UmaListaVazia_Quando_ObterUsuarioPorRA_Deve_RetornarNone(self):
        # ARRANGE
        service = UsuarioService()
        # ACT E ASSERT
        self.assertIsNone(service.obterUsuarioPorRA('ABCDEF'))

    # ----------- OBTER USUARIO  ----------- #

    @patch('builtins.input', lambda _: '12345')
    def test_Dado_UmaListaDeUsuarios_Quando_ObterUsuario_PassandoRACerto_Deve_ImprimirOsDadosCertosNaTela(self):
        # ARRANGE
        output = self._configurarOutput()
        raEsperado = '12345'
        usuario = self._criarUsuario(raEsperado)
        service = UsuarioService([usuario])

        # ACT
        service.obterUsuario()

        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), f'Usuário Encontrado\nRA: {raEsperado}\nNome: {usuario.Nome}\n')

    @patch('builtins.input', lambda _: 'ABCDE')
    def test_Dado_UmaListaDeUsuarios_Quando_ObterUsuario_PassandoRAErrado_Deve_ImprimirQueNenhumUsuarioFoiEncontrado(self):
        # ARRANGE
        output = self._configurarOutput()
        service = UsuarioService([self._criarUsuario("12345")])
        # ACT
        service.obterUsuario()
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), 'Usuário Não Encontrado\n')

    # ----------- IMPRIMIR USUARIO  ----------- #

    def test_Dado_UmaListaDeUsuariosVazios_Quando_ImprimirUsuarios_Deve_ImprimirNadaNaTela(self):
        # ARRANGE
        output = self._configurarOutput()
        service = UsuarioService()
        # ACT
        service.imprimirUsuario()
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), '')

    def test_Dado_UmaListaDeUsuarios_Quando_ImprimirUsuarios_Deve_ImprimirOsDadosDaLista(self):
        # ARRANGE
        output = self._configurarOutput()
        raEsperado = "12345"
        usuario = self._criarUsuario(raEsperado)
        service = UsuarioService([usuario])
        # ACT
        service.imprimirUsuario()
        # ASSERT
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), f'RA: {raEsperado}\nNome: {usuario.Nome}\n')

    # ----------- EDITAR USUARIO  ----------- #

    def test_Dado_UmaListaComUsuario_Quando_EditarUsuario_PassandoRaCorreto_E_BuscarOMesmoUsuarioPorRa_Deve_AlterarONomeDoUsuarioComORAPassado(self):
        # ARRANGE
        raEsperado = "444555"
        nomeEsperado = "Nome-Teste"
        inputs = iter([raEsperado, nomeEsperado])
        with patch('builtins.input', lambda _: next(inputs)):
            usuario = self._criarUsuario(raEsperado)
            service = UsuarioService([usuario])
            # ACT
            service.editarUsuario()
            usuarioBuscado = service.obterUsuarioPorRA(raEsperado)
            # ASSERT
            self.assertEqual(usuarioBuscado.Nome, nomeEsperado)

    def test_Dado_UmaListaComUsuario_Quando_EditarUsuario_PassandoRaErrado_Deve_ImprimirQueUsuarioNaoFoiEncontrado_E_NenhumUsuarioDeveSerAlterado(self):
        # ARRANGE
        raCorreto = "444555"
        raBuscado = "123456"
        nomeEsperado = "Nome-Teste"
        inputs = iter([raBuscado, nomeEsperado])
        with patch('builtins.input', lambda _: next(inputs)):
            output = self._configurarOutput()
            usuario = self._criarUsuario(raCorreto)
            service = UsuarioService([usuario])
            # ACT
            service.editarUsuario()
            usuarioBuscado = service.obterUsuarioPorRA(raCorreto)
            sys.stdout = sys.__stdout__
            # ASSERT
            self.assertEqual(output.getvalue(), 'Usuário Não Encontrado\n')
            self.assertEqual(usuario.Nome, usuarioBuscado.Nome)

    # ----------- DELETAR USUARIO  ----------- #

    @patch('builtins.input', lambda _: '444555')
    def test_Dado_UmaListaComUsuario_Quando_DeletarUsuario_PassandoRaCorreto_E_BuscarOMesmoUsuarioPorRa_Deve_ExcluirUsuarioPassadoENaoTerMaisUsuariosNaLista(self):
        # ARRANGE
        raUsuario = "444555"
        service = UsuarioService([self._criarUsuario(raUsuario)])
        # ACT
        service.deletarUsuario()
        usuarioBuscado = service.obterUsuarioPorRA(raUsuario)
        # ASSERT
        self.assertIsNone(usuarioBuscado)

    @patch('builtins.input', lambda _: '123456')
    def test_Dado_UmaListaComUsuario_Quando_DeletarUsuario_PassandoRaErrado_E_BuscarOMesmoUsuarioPorRa_Deve_ImprimirQueUsuarioEstaErradoENaoAlterarAListadeUsuarios(self):
        # ARRANGE
        raUsuario = "444555"
        service = UsuarioService([self._criarUsuario(raUsuario)])
        # ACT
        service.deletarUsuario()
        usuarioBuscado = service.obterUsuarioPorRA(raUsuario)
        # ASSERT
        self.assertIsNotNone(usuarioBuscado)

    def _configurarOutput(self):
        output = io.StringIO()
        sys.stdout = output
        return output

    def _criarListaUsuarios(self, qnt):
        userList = []
        for i in range(qnt):
            userList.append(self._criarUsuario())
        return userList

    def _criarUsuario(self, ra=None):
        fake = Faker()
        usuario = Usuario()
        setattr(usuario, "Ra", str(fake.random_number()) if ra is None else ra)
        setattr(usuario, "Nome", fake.first_name())
        return usuario

if __name__ == '__main__':
    main()