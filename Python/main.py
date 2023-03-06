import os
from src import ExecutarMenuUsuario, BoasVindas, IniciarConexao

BoasVindas()

currentDirectory = os.getcwd()
IniciarConexao(currentDirectory + "\\local\\pythonsqlite.db")

while True:
    ExecutarMenuUsuario()