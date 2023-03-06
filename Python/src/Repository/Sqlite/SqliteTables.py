from src.Repository.Sqlite.SqliteConnection import *

def MontarBancoDeDados():
    sucesso = True

    if not CriarTabelaAcesso():
        sucesso = False
    if not CriarTabelaOperacao():
        sucesso = False
    if not CriarTabelaUsuario():
        sucesso = False
    return sucesso

def CriarTabelaAcesso():
    comando = """ CREATE TABLE IF NOT EXISTS ACESSO (
            Id INT PRIMARY KEY,
            SolicitanteId INT NOT NULL,
            SolicitanteNome VARCHAR(50) NOT NULL,
            DataAcesso TEXT NOT NULL,
            DestinatarioId INT NOT NULL,
            DestinatarioNome VARCHAR(50) NOT NULL
        ); """

    return ExecutarComandoDatabase(comando)

def CriarTabelaOperacao():
    comando = """ CREATE TABLE IF NOT EXISTS OPERACAO (
            Id INT PRIMARY KEY,
            Nome VARCHAR(50) NOT NULL,
            Tipo VARCHAR(50) NOT NULL,
            Valores VARCHAR(50) NOT NULL,
            Data TEXT NOT NULL
        ); """

    return ExecutarComandoDatabase(comando)

def CriarTabelaUsuario():
    comando = """ CREATE TABLE IF NOT EXISTS USUARIO (
            Ra VARCHAR(10) PRIMARY KEY,
            Nome VARCHAR(50) NOT NULL,
            Cpf CHAR(11) NOT NULL,
            Email VARCHAR(50) NOT NULL,
            DataNascimento TEXT
        ); """

    return ExecutarComandoDatabase(comando)
