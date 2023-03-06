from src.Repository.Sqlite.SqliteConnection import *

def CriarTabelaOperacao():
    comando = """ CREATE TABLE USUARIO (
            Ra VARCHAR(10) PRIMARY KEY,
            Nome VARCHAR(50) NOT NULL,
            Cpf CHAR(11) NOT NULL,
            Email VARCHAR(50) NOT NULL,
            DataNascimento TEXT
        ); """

    ExecutarComandoDatabase(comando)

def CriarTabelaUsuario():
    comando = """ CREATE TABLE USUARIO (
            Ra VARCHAR(10) PRIMARY KEY,
            Nome VARCHAR(50) NOT NULL,
            Cpf CHAR(11) NOT NULL,
            Email VARCHAR(50) NOT NULL,
            DataNascimento TEXT
        ); """

    ExecutarComandoDatabase(comando)
